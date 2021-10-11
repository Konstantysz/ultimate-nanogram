class Cell:
 
    # default constructor
    def __init__(self, value):
        self._clicked = False
        self._value = value
        
    def GetValue(self):
        return self._value

    def GetClicked(self):
        return self._clicked

    def SetClicked(self, clicked):
        self._clicked = clicked
