from enum import IntEnum

class Code(IntEnum):
    UNKNOWN = -1
    SUCCESS = 0
    UNAUTHORIZED = 1
    EXISTS = 2
    PERMISSON_DENIED = 3
    NOT_FOUND = 4
    INVALID_PARAM = 5
    SERVER_ERROR = 6
    BAD_REQUEST = 999
