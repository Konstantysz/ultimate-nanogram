from src.GameController import GameController


class Engine:
 
    # default constructor
    def __init__(self):
        self._gameController = GameController()
         
    # default constructor
    def Play(self):
        print("Play!")
         
    # default constructor
    def Stop(self):
        print("Stop!")

    def NewGame(self):
        print("NewGame!")