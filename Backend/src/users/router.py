# src/users/router.py
from uuid import UUID
from fastapi import APIRouter, HTTPException, Body
from ..core.models import Player, players_db

router = APIRouter(prefix='/users', tags=['Пользователи'])

@router.get("/player/{player_id}", response_model=Player)
async def get_player(player_id: UUID) -> Player:
    player = players_db.get(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Игрок не найден")
    return player

@router.get("/players")
async def get_all_players():
    return list(players_db.values())
    
@router.post("/new_user/", response_model=Player)
async def new_user(player_data: Player = Body(...)) -> Player:
    players_db[player_data.id] = player_data
    return player_data