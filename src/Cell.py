class Cell:
 
    # default constructor
    def __init__(self, value):
        self._clicked = False
        self._value = value

    def GetClicked(self):
        return self._clicked

    def SetClick(self, clicked):
        self._clicked = clicked
