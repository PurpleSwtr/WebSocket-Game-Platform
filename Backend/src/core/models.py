# src/core/models.py
from pydantic import BaseModel, Field
from uuid import UUID, uuid4

class Player(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str

players_db: dict[UUID, Player] = {}

class GameSession(BaseModel):
    session_id: str
    players: dict[UUID, Player] = {}
    field: list[list[str]] = None
    current_turn: UUID = None
    status: str = "waiting"
    
active_sessions: dict[str, GameSession] = {}