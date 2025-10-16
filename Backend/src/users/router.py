from typing import Annotated
# from fastapi.datastructures import FormData
from fastapi import APIRouter, Depends, Form, HTTPException
from ..core.models import Player, GameSession
from ..core.session_data import session_data
router = APIRouter(prefix='/users', tags=['Пользователи'])

@router.get("/player/{username}", response_model=Player)
async def player(username: str) -> Player:
    username = str(username)
    if session_data.players and username in session_data.players:
        return session_data.players[username]
    raise HTTPException(status_code=404, detail="Игрок не найден")

@router.get("/players")
async def players():
    return session_data.players
    
@router.post("/new_user/")
async def new_user(data: Annotated[Player, Form()]) -> Player:
    session_data.players[data.name] = data
    return data