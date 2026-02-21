from enum import Enum


class DIRECTION(Enum):
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3


class ENEMY_STATUS(Enum):
    ACTIVE = 0
    PASSIVE = 1


class COLOR(Enum):
    RED = (255, 16, 16, 0)
    GREEN = (16, 255, 16, 0)
    BLUE = (16, 16, 255, 0)
    YELLOW = (255, 255, 16, 0)
    PURPLE = (255, 16, 255, 0)
    CYAN = (16, 255, 255, 0)
    BLACK = (16, 16, 16, 0)
    WHITE = (255, 255, 255, 0)


class DISPLAY_MODES(Enum):
    D_M_640_480 = (640, 480)
    D_M_1600_900 = (1600, 900)
    D_M_1920_1080 = (1920, 1080)


SPRITE_SHEET_WINDOW = (32, 32)
SPRITE_WINDOW = (8, 8)
