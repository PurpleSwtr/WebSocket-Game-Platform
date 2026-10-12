import json
from typing import List
from uuid import UUID

from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect

from ..core.models import active_sessions

router = APIRouter(prefix="/websocket", tags=["Веб-сокет"])

REQUIRED_PLAYERS = 2


class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, session_id: str):
        await websocket.accept()
        if session_id not in self.active_connections:
            self.active_connections[session_id] = []
        self.active_connections[session_id].append(websocket)

    def disconnect(self, websocket: WebSocket, session_id: str):
        if session_id in self.active_connections:
            self.active_connections[session_id].remove(websocket)
            if not self.active_connections[session_id]:
                del self.active_connections[session_id]

    async def broadcast_to_session(self, game_data: str, session_id: str):
        if session_id in self.active_connections:
            for connection in self.active_connections[session_id]:
                await connection.send_text(game_data)


manager = ConnectionManager()
# Примерное сообщение с форнтенда:
# {"user": "uuid", "action": "move", "row": 1, "col": 2}
# NOTE: В дальнейшем переехали в основной файл RULES.md,
# который описывает вообще весь state, примеры запросов от пользователей и прочие нюансы логики


@router.get("/connections")
async def get_active_connections(request: Request):
    """Возвращает список всех активных WebSocket-подключений с готовыми ссылками."""

    base_url = str(request.base_url)
    ws_base = base_url.replace("http://", "ws://").replace("https://", "wss://")

    result = []
    for session_id, connections in manager.active_connections.items():
        result.append(
            {
                "url": f"{ws_base}api_v1/websocket/ws/{session_id}",
                "connections_count": len(connections),
                "session_status": active_sessions[session_id].status
                if session_id in active_sessions
                else "unknown",
                "players_count": len(active_sessions[session_id].players)
                if session_id in active_sessions
                else 0,
            }
        )

    return {"connections": result}


@router.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    # Зарегестрированна ли в сессия через REST API?
    if session_id not in active_sessions:
        await websocket.close(code=1008, reason="session undefined")
        return

    await manager.connect(websocket, session_id)
    session = active_sessions[session_id]

    await websocket.send_text(session.model_dump_json())

    if len(session.players) == REQUIRED_PLAYERS and session.status == "ready":
        await manager.broadcast_to_session(session.model_dump_json(), session_id)

    try:
        # Тут прям жёстко намудрил с логикой, и однажды это станет большой проблемой.
        # TODO: Стоит переписать на какие-нибудь elif'ы, либо вообще прописать какую-нибудь
        # машину состояний в отдельном классе, и к перемеру уже адекватно свитчкейсом всё делать. А так игровой цикл рабочий, осталось только красоту навести.
        # NOTE: Ну и вообще желательно так-то из роутера всю логику вынести, нехорошо всё таки что всё тут в куче... И передавать параметры например просто те же massage или session.
        while True:
            data = await websocket.receive_text()

            massage = json.loads(data)
            session = active_sessions[session_id]
            if session.status == "ready":
                if massage["action"] == "choose":
                    if massage["type"] != "":
                        session.choose_img(
                            user_id=UUID(massage["user"]), marker_type=massage["type"]
                        )

                if massage["action"] == "prepared":
                    user_uuid = UUID(massage["user"])
                    if user_uuid not in session.prepared_players:
                        session.prepared_players.append(user_uuid)

                if (
                    len(session.markers) == REQUIRED_PLAYERS
                    and len(session.prepared_players) == REQUIRED_PLAYERS
                ):
                    session.status = "starting"

            if session.status == "starting":
                session.roll_first_turn()
                session.status = "playing"

            if session.status == "playing":
                if massage["action"] == "move":
                    user_uuid = UUID(massage["user"])
                    if user_uuid == session.current_turn:
                        move_successful = session.action_move(
                            user_id=user_uuid,
                            row=str(massage["row"]),
                            col=str(massage["col"]),
                        )
                        if move_successful:
                            session.change_turn()
            if session.status == "finished":
                if massage["action"] == "restart":
                    session.voted_restart.append(UUID(massage["user"]))
                if massage["action"] == "exit":
                    user_to_remove = UUID(massage["user"])
                    if user_to_remove in session.players:
                        session.players.pop(user_to_remove)
                    session.status = "waiting"
                if len(session.voted_restart) == REQUIRED_PLAYERS:
                    # NOTE: Вот тут важно подумать над механикой рестарта, возможно лучше откидывать игроков заново на выбор своего значка которым он будет ходить, для разнообразия, либо придумать отдельный для этого вообще state
                    # TODO: Тут 100% нет вообще никакой логики очищения поля, голосования, смены хода, выигравшего игрока и всё остальное
                    session.status = "starting"
            # TODO: Продумать логику для уже задуманной фичи emote, но она не первостепенная для mvp так что отложим
            data = session
            # await manager.broadcast_to_session(data, session_id)
            # TODO: Вполне вероятно что будет удобнее распаковать это дело
            # На фронтенде нужно протестить
            await manager.broadcast_to_session(data.model_dump_json(), session_id)
    except WebSocketDisconnect:
        manager.disconnect(websocket, session_id)
