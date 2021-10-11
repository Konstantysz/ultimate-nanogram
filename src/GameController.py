from src.BoardController import BoardController
from src.GameConsts import LIVESNUMBER, InputMode

class GameController:

    # default constructor
    def __init__(self, boardSize):
        self._lives = LIVESNUMBER
        self._input_mode = InputMode.IMAGECELL
        self._gameController = BoardController(boardSize)