from src.GameController import GameController
from src.GameConsts import Difficulty

class Engine:
 
    # default constructor
    def __init__(self):
        self._difficulty = Difficulty.NORMAL
        self._gameController = GameController(self._difficulty)
         
    # default constructor
    def play(self):
        print("Play!")
         
    # default constructor
    def stop(self):
        print("Stop!")

    def new_game(self):
        print("NewGame!")