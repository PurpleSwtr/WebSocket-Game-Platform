from typing import Any, Optional
from pydantic import BaseModel
from uuid import uuid4

class Player(BaseModel):
    id: str = uuid4().hex
    name: str
    ws_session: Optional[Any] = None

class GameSession(BaseModel):
    session_id: str
    players: dict[str, Player] = {}
    field: list[list[str]] = None
    current_turn: str = None
    status: str = "waiting"
    
active_sessions: dict[str, GameSession] = {}