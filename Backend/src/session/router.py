# src/session/router.py
from uuid import UUID, uuid4
from fastapi import APIRouter, Depends, HTTPException, Body

from ..core.models import GameSession, Player, active_sessions, players_db

router = APIRouter(prefix='/session', tags=['Комнаты'])

async def get_player_by_id(player_id: UUID) -> Player:
    player = players_db.get(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Игрок не найден")
    return player

@router.post("/create_session/", response_model=GameSession)
async def create_session(player: Player = Depends(get_player_by_id)):
    session_id = str(uuid4())
    new_session = GameSession(
        session_id=session_id,
        players={player.id: player},
        current_turn=player.id
    )
    active_sessions[session_id] = new_session
    return new_session

@router.get("/sessions")
async def get_sessions() -> dict:
    return active_sessions

@router.delete("/close_session")
async def delete_session(id_session: UUID) -> None:
    active_sessions[id_session] = None