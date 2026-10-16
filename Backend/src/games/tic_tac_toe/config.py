from src.core.enums import Markers
from src.games.base.config import GameConfig
from src.games.registry import GameType


class TicTacToeConfig(GameConfig):
    game_type = GameType.TIC_TAC_TOE
    displayed_name = "Tic Tac Toe"
    description = "Classic game about cross and circles. Make 3 in row for win!"
    required_players = 2
    min_players = 2
    max_players = 2
    preparation_phase = True
    allowed_markers = tuple(Markers)
