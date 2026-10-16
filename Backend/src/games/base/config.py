from abc import ABC

from src.core.enums import Markers
from src.games.registry import GameType


class GameConfig(ABC):
    game_type: GameType
    displayed_name: str
    description: str
    required_players: int
    min_players: int
    max_players: int
    preparation_phase: bool
    allowed_markers: tuple[Markers, ...] | None = None
