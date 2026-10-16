from enum import Enum, auto


class SessionState(Enum):
    """
    WAITING_PLAYERS →
    PREPARING →
    PLAYING →
    FINISHED →
    VOTING →
    (RESTARTED | CLOSED)
    RESTARTED ->
    PREPARING
    """

    WAITING_PLAYERS = auto()
    PREPARING = auto()
    PLAYING = auto()
    FINISHED = auto()
    VOTING = auto()
    CLOSED = auto()


class SessionEvent(Enum):
    # TODO: Можно разделить ещё на GameEvent чтобы разделить слои происходящего именно с сессией в целом, и в игре
    PLAYER_JOINED = auto()
    PLAYER_READY = auto()
    PLAYER_LEAVE = auto()
    PLAYER_DISCONECTED = auto()
    PLAYER_EMOTE = auto()
    PLATER_VOTED = auto()
    GAME_CHANGED = auto()


class SessionVoted(Enum):
    RESTART = auto()
    GAME = auto()
    EXIT = auto()


class GameEvent(Enum):
    PLAYER_MOVE = auto()
    PLAYER_PREPARE = auto()
    GAME_WINNER = auto()
    GAME_DRAW = auto()


class Markers(str, Enum):
    FIRE = "fire"
    SQUARE = "square"
    LIGHTNING = "lightning"
    CROSS = "cross"
    CIRCLE = "circle"
    WATER = "water"
    TRIANGLE = "triangle"
