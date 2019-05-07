from algo import Algo
import sys

class AStar(Algo):
    """
    Implements the A* search algorithm to be used in the ui.

    This design was inpsired by:
    https://github.com/bsharvari/A-Star-Search
    """
    def __init__(self, board):
        super().__init__(board)

        self._path = []
        self._val = 1
        
        self._visited = [[0 for _ in range(self._board.width())] 
            for _ in range(self._board.height())]
        self._visited[self._start[0]][self._start[1]] = 1

        self._expanded = [[-1 for _ in range(self._board.width())] 
            for _ in range(self._board.height())]
        self._expanded[self._start[0]][self._start[1]] = 0

        self._x = self._start[0]
        self._y = self._start[1]
        g = 0
        f = g + 1
        self._minlist = [f, g, self._x, self._y]

    def build_heuristic(self):
        self._heuristic = [[-1 for _ in range(self._board.width())] for _ in range(self._board.height())]

        for x in range(len(self._heuristic)):
            for y in range(len(self._heuristic[0])):
                weight = abs(x - self._end[0]) + abs(y - self._end[1])
                self._heuristic[x][y] = weight

