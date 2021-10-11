class Cell:
 
    # default constructor
    def __init__(self, value):
        self._clicked = False
        self._value = value

    def get_value(self):
        return self._value

    def get_clicked(self):
        return self._clicked

    def set_clicked(self, clicked):
        self._clicked = clicked
