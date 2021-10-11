from enum import Enum

class Difficulty(Enum):
    EASY = 5
    NORMAL = 10
    HARD = 15
    TURBO = 30

class InputMode(Enum):
    IMAGECELL = 0
    EMPTYSQUARE = 1
    HINT = 2

LIVESNUMBER = 3