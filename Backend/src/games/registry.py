"""
Файл регистрации новых игр. Именно отсюда как из единой точки входа будут оркестрироваться игровые конфиги и движки под каждую игру.
"""

from enum import Enum
from typing import ClassVar

from src.games.base.config import GameConfig
from src.games.base.engine import GameEngine
from src.games.tic_tac_toe.config import TicTacToeConfig
from src.games.tic_tac_toe.engine import TicTacToeEngine
from src.games.tic_tac_toe_ultimate.config import TicTacToeUltimateConfig
from src.games.tic_tac_toe_ultimate.engine import TicTacToeUltimateEngine


class GameType(str, Enum):
    """
    Перечисление для игр. Используется для передачи типа игр в остальные функции по всему приложению.
    """

    TIC_TAC_TOE = "tic_tac_toe"
    TIC_TAC_TOE_ULTIMATE = "tic_tac_toe_ultimate"


class GameRegistry:
    """
    Класс для регистрации игр.

    Именно этот класс является точкой входа для получения данных о конфигурации игры и самого игрового движка для взаимодействия, и передачи всех этих параметров игровой сессии.
    """

    _REGISTRY: ClassVar[dict[GameType, tuple[type[GameConfig], type[GameEngine]]]] = {
        GameType.TIC_TAC_TOE: (TicTacToeConfig, TicTacToeEngine),
        GameType.TIC_TAC_TOE_ULTIMATE: (
            TicTacToeUltimateConfig,
            TicTacToeUltimateEngine,
        ),
    }

    @classmethod
    def get_game(cls, game_type: GameType) -> tuple[GameConfig, GameEngine]:
        if game_type not in cls._REGISTRY:
            raise ValueError(f"Unknown game type: {game_type}")
        config, engine = cls._REGISTRY[game_type]
        return config(), engine()

    @staticmethod
    def get_list_game_types() -> list[GameType]:
        return list(GameType)

    @classmethod
    def list_games(cls) -> list[GameConfig]:
        return [config_cls() for config_cls, _ in cls._REGISTRY.values()]
