from pydantic import BaseModel, Field
from uuid import UUID, uuid4

class Player(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str

players_db: dict[UUID, Player] = {}

class GameSession(BaseModel):
    session_id: str
    players: dict[UUID, Player] = {}
    field: list[list[str]] = Field(default_factory=lambda: [[None, None, None] for _ in range(3)])
    current_turn: UUID = None
    winner_player: UUID = None
    markers: dict[UUID, str] = {}
    status: str = "waiting"

    async def choose_img(self, user_id: str, marker_type: str) -> None:
        self.markers[user_id] = marker_type

    async def move(self, user_id: str, row: int, col: int) -> None:
        self.field[row][col] =self.markers[user_id]

    #   0 1 2
    # 0 * * *
    # 1 * * * 
    # 2 * * *

    async def win_check(self):
        win_combos = [
            [(0,0),(1,1),(2,2)],
            [(0,2),(1,1),(2,0)],
            [(0,0),(0,1),(0,2)],
            [(1,0),(1,1),(1,2)],
            [(2,0),(2,1),(2,2)],
            [(0,0),(1,0),(2,0)],
            [(0,1),(1,1),(2,1)],
            [(0,2),(1,2),(2,2)],
        ]
        for comb in win_combos:
            ...



    
active_sessions: dict[str, GameSession] = {}