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
    RESTARTED = auto()
    CLOSED = auto()


class SessionEvent(Enum):
    PLAYER_JOINED = auto()
    PLAYER_PREPARE = auto()
    PLAYER_LEAVE = auto()
    PLAYER_DISCONECTED = auto()
    PLATER_VOTED = auto()

    PLAYER_MOVE = auto()

    PLAYER_EMOTE = auto()

    GAME_WINNER = auto()
    GAME_DRAW = auto()
    GAME_CHANGE_GAME = auto()


