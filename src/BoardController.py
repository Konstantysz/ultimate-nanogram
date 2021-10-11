from src.Cell import Cell
import numpy as np
from src.GameConsts import BOARDFILEPATH

class BoardController:
    # default constructor
    def __init__(self, boardSize):
        print("Board {}x{} created!".format(boardSize.value, boardSize.value))

        self._horizontalNumbers = np.array([])
        self._verticalNumbers = np.array([])

        self._board = np.array([
            [Cell(True), Cell(True), Cell(True), Cell(True), Cell(True)], 
            [Cell(False), Cell(False), Cell(False), Cell(False), Cell(False)], 
            [Cell(True), Cell(True), Cell(True), Cell(True), Cell(True)], 
            [Cell(False), Cell(False), Cell(False), Cell(False), Cell(False)], 
            [Cell(True), Cell(True), Cell(True), Cell(True), Cell(True)]
        ])

    def import_board_image(self):
        # Bogdan algorithm to import image from BOARDFILEPATH
        return

    def calculate_info_numbers(self):
        # self.calculate_info_numbers_horizontal()
        self.calculate_info_numbers_vertical()
        return

    def calculate_info_numbers_vertical(self):
        res = []
        for i in range(self._board.shape[1]):
            nums = []
            prev_val = False
            num = 0
            for j in range(self._board.shape[0]):
                if (self._board[j][i].get_value()):
                    num += 1
                    prev_val = True
                    if (j == self._board.shape[0] - 1):
                        nums.append(num)
                else:
                    nums.append(num)
                    prev_val = False
                    num = 0
            res.append(nums)
            
        self._verticalNumbers = np.array(res)