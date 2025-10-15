from typing import Annotated

from fastapi import FastAPI, Form
# from fastapi.datastructures import FormData

from .core.models import Player, GameSession


app = FastAPI()

players_cnt = 0

players = {
}

@app.get("/player/{user_id}", response_model=Player)
async def read_items(user_id: str) -> Player:
    return players[user_id]

    
@app.post("/new_user/")
async def new_user(data: Annotated[Player, Form()]) -> Player:
    players[data.id] = data
    return data