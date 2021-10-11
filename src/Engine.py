from src.GameController import GameController
from src.Difficulty import Difficulty

class Engine:
 
    # default constructor
    def __init__(self):
        self._difficulty = Difficulty.NORMAL
        self._gameController = GameController(self._difficulty)
         
    # default constructor
    def Play(self):
        print("Play!")
         
    # default constructor
    def Stop(self):
        print("Stop!")

    def NewGame(self):
        print("NewGame!")