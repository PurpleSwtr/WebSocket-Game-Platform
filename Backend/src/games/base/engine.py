from typing import Any, Protocol
from uuid import UUID

from src.core.enums import GameState, SessionState
from src.core.models import Player


class GameEngine(Protocol):
    """Контракт для описания правил конкретной игры."""

    def initial_state(self, players: dict[UUID, Player]) -> Any: ...

    def validate_move(self, state: Any, player: UUID, move: Any) -> NotYourTurnException: ...

    def apply_move(self): ...

    def end_check(
        self, state: GameState
    ) -> SessionState.PLAYING | SessionState.FINISHED: ...
