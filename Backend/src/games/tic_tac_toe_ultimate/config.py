from src.games.base.config import GameConfig


class TicTacToeUltimateConfig(GameConfig):
    game_type: str
    displayed_name: str
    required_players: int
    min_players: int
    max_players: int
    allowed_markers: list[str] | None
    preparation_phase: bool
    description: str
