import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List
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

@router.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    # Зарегестрированна ли в сессия через REST API?
    if session_id not in active_sessions:
        await websocket.close(code=1008, reason="session undefined")
        return

    await manager.connect(websocket, session_id)
    try:
        while True:
            data = await websocket.receive_text()

            massage = json.loads(data)
            session = active_sessions[session_id]
            if len(session.players) == REQUIRED_PLAYERS:
                session.status = "ready"
            if session.status == "ready":
                if massage["action"] == "choose":
                    if massage["type"] != '':
                        session.choose_img(user_id=massage["user"], marker_type=massage["type"])
                
                if massage["action"] == "prepared":
                    session.prepared_players.append(massage["user"])

                if len(session.markers == REQUIRED_PLAYERS):
                    if len(session.prepared_players) == REQUIRED_PLAYERS:
                        session.status = "starting"

                if session.status == "starting":
                    session.status == "playing"
                    session.roll_first_turn()
                    if massage["action"] == "move":
                        if massage["user"] == session.current_turn:
                            session.action_move(user_id=massage["user"], row=massage["row"], col=massage["col"])
                if  session.status == "finished":
                    if massage["action"] == "restart":
                        session.voted_restart.append(massage["user"])
                    if massage["action"] == "exit":
                        session.players.pop(session.player_id)
                        session.status = "waiting"
                    if len(session.voted_restart) == REQUIRED_PLAYERS:
                        # NOTE: Вот тут важно подумать над механикой рестарта, возможно лучше откидывать игроков заново на выбор своего значка которым он будет ходить, для разнообразия, либо придумать отдельный для этого вообще state
                        session.status = "starting"
                # TODO: Продумать логику для уже задуманной фичи emote, но она не первостепенная для mvp так что отложим
            data = session
            # await manager.broadcast_to_session(data, session_id)
            # TODO: Вполне вероятно что будет удобнее распаковать это дело 
            # На фронтенде нужно протестить
            await manager.broadcast_to_session(*data, session_id)
    except WebSocketDisconnect:
        manager.disconnect(websocket, session_id)