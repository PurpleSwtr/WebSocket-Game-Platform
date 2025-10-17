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
    
    # Реализовать: 
    # переход хода

    async def choose_img(self, user_id: str, marker_type: str) -> None:
        self.markers[user_id] = marker_type

    async def move(self, user_id: str, row: int, col: int) -> None:
        self.field[row][col] =self.markers[user_id]

    #   0 1 2
    # 0 * * *
    # 1 * * * 
    # 2 * * *

    # async def win_check(self):
    def win_check(self):
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

        for win_comb in win_combos:
            symbols = []
            for r, c in win_comb:
                symb = self.field[c][r]
                symbols.append(symb)
            if len(set(symbols)) == 1 and not None in set(symbols):
                return True
        return False
    
    def draw_check(self):
        for col in range(3):
            cells = []
            for cell in self.field[col]:
                cells.append(cell)
        if None in cells:
            return False
        else: return True

    def change_turn(self, user_id: UUID):
        players = list(self.players.keys())
        if not players:
            return None
        if self.current_turn is None:
            self.current_turn = players[0]
        else:
            current_index = players.index(self.current_turn)
            next_index = (current_index + 1) % len(players)
            self.current_turn = players[next_index]
        
        return self.current_turn
active_sessions: dict[str, GameSession] = {}

gs = GameSession(session_id="1")

p1 = Player(name="jonh")
p2 = Player(name="bob")

gs.players[p1.id] = p1
gs.players[p2.id] = p2

gs.change_turn(user_id=p1.id)
print(gs.current_turn)
gs.change_turn(user_id=p1.id)
print(gs.current_turn)
gs.change_turn(user_id=p1.id)
print(gs.current_turn)
gs.change_turn(user_id=p1.id)
print(gs.current_turn)

# gs.field=[
#     ["1","0","1"],
#     ["1","1","1"],
#     ["0",None,"0"]
#     ]
# draw_check = gs.draw_check()
# win_check = gs.win_check()
    
# print(win_check)
# print(draw_check)