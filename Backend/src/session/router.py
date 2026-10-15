from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException, Query
from src.core.models import GameSession, Player, active_sessions, players_db
from src.websocket.router import manager

router = APIRouter(prefix="/session", tags=["Комнаты"])


async def get_player_by_id(player_id: UUID) -> Player:
    player = players_db.get(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Игрок не найден")
    return player


@router.post("/create_session/", response_model=GameSession)
async def create_session(player_id: UUID = Query(..., alias="player_id")):
    player = await get_player_by_id(player_id)
    session_id = str(uuid4())
    new_session = GameSession(
        session_id=session_id, players={player.id: player}, current_turn=player.id
    )
    active_sessions[session_id] = new_session
    return new_session


@router.get("/sessions", response_model=list[GameSession])
async def get_sessions():
    return list(active_sessions.values())


@router.delete("/close_session")
async def delete_session(id_session: str) -> None:
    if id_session not in active_sessions:
        raise HTTPException(status_code=404, detail="Сессия не найдена")
    del active_sessions[id_session]


@router.patch("/join_session/{session_id}", response_model=GameSession)
async def join_to_session(session_id: str, player_id: UUID | None = Query(None)):
    current_session = active_sessions.get(session_id)
    if not current_session:
        raise HTTPException(status_code=404, detail="Сессия не найдена")

    if len(current_session.players) >= 2:
        if player_id is None or player_id not in current_session.players:
            raise HTTPException(status_code=409, detail="Сессия уже заполнена")

    player: Player | None = None

    if player_id:
        player = players_db.get(player_id)
        if not player:
            raise HTTPException(status_code=404, detail="Игрок не найден")
    else:
        guest_name = f"Гость#{str(uuid4())[:-8]}"
        player = Player(name=guest_name)
        players_db[player.id] = player

    if player.id in current_session.players:
        return current_session

    current_session.players[player.id] = player

    if len(current_session.players) == 2:
        current_session.status = "ready"
        await manager.broadcast_to_session(
            current_session.model_dump_json(), session_id
        )

    return current_session
