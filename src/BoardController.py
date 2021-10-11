from src.Cell import Cell
import numpy as np
from src.Cell import Cell


class BoardController:
    # default constructor
    def __init__(self, boardSize):
        print("Board {}x{} created!".format(boardSize.value, boardSize.value))
        self._board = np.array([[Cell(True), Cell(True), Cell(True), Cell(True), Cell(True)], [Cell(False), Cell(False), Cell(False),
                Cell(False), Cell(False)], [Cell(True), Cell(True), Cell(True), Cell(True), Cell(True)], [Cell(False), Cell(False), Cell(False),
                Cell(False), Cell(False)], [Cell(True), Cell(True), Cell(True), Cell(True), Cell(True)]])
