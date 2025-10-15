from typing import Any, Optional
from pydantic import BaseModel

class Player(BaseModel):
    id: str
    name: str
    ws_session: Optional[Any] = None

class GameSession(BaseModel):
    session_id: str
    players: dict[str, Player] = {}
    field: list[list[str]] = None
    current_turn: str = None
    status: str = "waiting"
    
active_sessions: dict[str, GameSession] = {}