from pydantic import BaseModel, Field
from uuid import UUID, uuid4
import random
class Player(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str

players_db: dict[UUID, Player] = {}

# TODO: Подумать над тем, чтобы сделать все методы асинхронными
# Потому что это перерастёт в большую проблему, если вдруг окажется что сессия
# не может выдержать больше чем два подключения из-за этого...
class GameSession(BaseModel):
    session_id: str
    players: dict[UUID, Player] = {}
    field: list[list[str]] = Field(default_factory=lambda: [[None, None, None] for _ in range(3)])
    current_turn: UUID = None
    winner_player: UUID = None
    markers: dict[UUID, str] = {}
    prepared_players: list[UUID] = []
    voted_restart: list[UUID] = []
    status: str = "waiting"
    # TODO: Сделать проерку на несуществующие типы, задать те которые подразумеваются,
    # по типу крестик, ноль, другие фигуры которые подразумеваются для разнообразия, как фича.
    # При этом также учитывать, что пользователи не могут выбрать одну и ту же, если она уже выбрана
    # TODO: Сделать отображение на фронте как бы залоченных уже значков
    def choose_img(self, user_id: UUID, marker_type: str) -> None:
        self.markers[user_id] = marker_type

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
                symb = self.field[r][c]
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

    def roll_first_turn(self) -> None:
        self.current_turn = list(self.players.keys())[random.randint(0,1)]

    def change_turn(self):
        players = list(self.players.keys())
        if not players:
            return None
        # Она тут по факту уже не нужна, так как вынесена в отдельный метод перед началом игры, но во избежании ошибок когда никто вдруг не может походить можно и оставить проверочку
        if self.current_turn is None:
            self.current_turn = players[random.randint(0,1)]
        else:
            current_index = players.index(self.current_turn)
            next_index = (current_index + 1) % len(players)
            self.current_turn = players[next_index]
        
        return self.current_turn
    
    def action_move(self, user_id: UUID, row: str, col: str) -> bool:
        row = int(row)
        col = int(col)
        if not isinstance(row, int) or not isinstance(col, int):
            return False
        if row > 2 or col > 2:
            return False
        if user_id != self.current_turn:
            return False
        if self.field[row][col] is not None:
            return False

        self.field[row][col] = self.markers[user_id] 

        if self.win_check():
            self.status = "finished"
            self.winner_player = user_id
        elif self.draw_check():
            self.status = "finished"
        return True
    
    def action_exit(self, user_id: UUID):
        self.players[user_id] = None

    def dev_draw_field(self):
        for row in range(3):
            line = ""
            for col in range(3):
                cell = self.field[row][col]
                if cell is None:
                    line += " - "
                else:
                    line += f" {cell} "
            print(line)

active_sessions: dict[str, GameSession] = {}

# NOTE: МОЯ ТЕСТОВАЯ ЗОНА - НЕ ЗАБЫВАЙ, ЕЁ НУЖНО КОММЕНТИРОВАТЬ ПРИ ЗАПУСКЕ СЕРВЕРА, 
# ПОТОМУ ЧТО ЭТО ИСПОЛНЯЕМЫЙ КОД, А В ДАЛЬНЕЙШЕМ ОН ИМПОРТИРУЕТСЯ КАК МОДУЛЬ

# gs = GameSession(session_id="1")

# p1 = Player(name="jonh")
# p2 = Player(name="bob")

# gs.markers[p1.id] = "X"
# gs.markers[p2.id] = "O"

# gs.players[p1.id] = p1
# gs.players[p2.id] = p2

# gs.current_turn = p1.id

# while gs.status == "waiting":
#     r = input()
#     c = input()
#     move = gs.action_move(user_id=gs.current_turn, row=r, col=c)
#     if move:
#         gs.change_turn()

#     gs.dev_draw_field()

# print(gs.status)

# print(gs.winner_player)

# gs.change_turn(user_id=p1.id)
# print(gs.current_turn)
# gs.change_turn(user_id=p1.id)
# print(gs.current_turn)
# gs.change_turn(user_id=p1.id)
# print(gs.current_turn)
# gs.change_turn(user_id=p1.id)
# print(gs.current_turn)

# gs.field=[
#     ["1","0","1"],
#     ["1","1","1"],
#     ["0",None,"0"]
#     ]
# draw_check = gs.draw_check()
# win_check = gs.win_check()
    
# print(win_check)
# print(draw_check)