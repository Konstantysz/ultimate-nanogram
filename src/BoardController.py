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
