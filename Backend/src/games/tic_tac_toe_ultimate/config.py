from src.core.enums import Markers
from src.games.base.config import GameConfig
from src.games.registry import GameType


class TicTacToeUltimateConfig(GameConfig):
    game_type: GameType = GameType.TIC_TAC_TOE_ULTIMATE
    description = "Improved version of the classic tic-tac-toe, but now on the 9x9 board!"
    displayed_name: str = "Tic Tac Toe Ultimate"
    required_players = 2
    min_players = 2
    max_players = 2
    preparation_phase = True
    allowed_markers = tuple(Markers)
