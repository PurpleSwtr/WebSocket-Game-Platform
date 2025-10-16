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

@router.get("/sessions", response_model=list[GameSession])
async def get_sessions():
    return list(active_sessions.values())

@router.delete("/close_session")
async def delete_session(id_session: str) -> None:
    if id_session not in active_sessions:
        raise HTTPException(status_code=404, detail="Сессия не найдена")
    active_sessions[id_session] = None
    return

@router.patch("/join_session/{session_id}", response_model=GameSession)
async def join_to_session(session_id: str, player: Player = Depends(get_player_by_id)):
    current_session = active_sessions.get(session_id)
    if not current_session:
        raise HTTPException(status_code=404, detail="Сессия не найдена")
        
    if len(current_session.players) >= 2:
        raise HTTPException(status_code=409, detail="Сессия уже заполнена")
    
    if player.id in current_session.players:
        raise HTTPException(status_code=400, detail="Игрок уже в этой сессии")

    current_session.players[player.id] = player
    
    if len(current_session.players) == 2:
        current_session.status = "ready_to_start"
        
    return current_session