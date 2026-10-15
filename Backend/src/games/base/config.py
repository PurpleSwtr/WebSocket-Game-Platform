from abc import ABC


class GameConfig(ABC):
    game_type: str
    displayed_name: str
    required_players: int
    min_players: int
    max_players: int
    allowed_markers: list[str] | None
    preparation_phase: bool
    description: str
