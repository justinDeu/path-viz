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

        self.build_heuristic()

        self._x = self._start[0]
        self._y = self._start[1]
        g = 0
        f = g + 1
        self._minlist = [f, g, self._x, self._y]

    def step(self):
        offsets = [-1, 1]
        x = self._minlist[2]
        y = self._minlist[3]

        for o in offsets:
            if 0 <= x + o < self._board.width():
                if self._visited[x + o][y] == 0 and self._board.state(x + o, y) != 1:
                    g2 = self._minlist[1] + 1
                    f2 = g2 + self._heuristic[x + o][y]
                    self._path.append([f2, g2, x + o, y])
                    self._board.explore(x + o, y)
            if 0 <= y + o < self._board.height(): 
                if self._visited[x][y + o] == 0 and self._board.state(x, y + o) != 1:
                    g2 = self._minlist[1] + 1
                    f2 = g2 + self._heuristic[x][y + o]
                    self._path.append([f2, g2, x, y + o])
                    self._board.explore(x, y+ o)

        del self._minlist[:]

        self._minlist = min(self._path)
        self._path.remove(self._minlist)
        if self._expanded[self._minlist[2]][self._minlist[3]] == -1:
            self._expanded[self._minlist[2]][self._minlist[3]] = self._val
        self._val += 1

    def running(self):
        return (self._minlist[2], self._minlist[3]) != self._end

    def build_heuristic(self):
        self._heuristic = [[sys.maxsize for _ in range(self._board.width())] for _ in range(self._board.height())]
        self._to_check = []

        self._heuristic[self._end[0]][self._end[1]] = 0
        self._evaluate_surrounding(self._end)

        while self._to_check:
            self._evaluate_surrounding(self._to_check.pop())


    def _evaluate_surrounding(self, loc):
        offsets = [-1, 1]

        for o in offsets:
            if 0 <= loc[0] + o < self._board.width():
                # will evaluate (loc[0] - 1, loc[1]) and (loc[0] + 1, loc[1])
                if self._board.state(loc[0] + o, loc[1]) != 1 and self._heuristic[loc[0]][loc[1]] + 1 < self._heuristic[loc[0] + o][loc[1]]:
                    self._heuristic[loc[0] + o][loc[1]] = self._heuristic[loc[0]][loc[1]] + 1
                    self._to_check.append((loc[0] + o, loc[1]))
            if 0 <= loc[1] + o < self._board.height(): 
                # will evaluate (loc[0], loc[1] - 1) and (loc[0], loc[1] + 1)
                if self._board.state(loc[0], loc[1] + o) != 1 and self._heuristic[loc[0]][loc[1]] + 1 < self._heuristic[loc[0]][loc[1] + o]:
                    self._heuristic[loc[0]][loc[1] + o] = self._heuristic[loc[0]][loc[1]] + 1
                    self._to_check.append((loc[0], loc[1] + o))

    def set_path(self):
        path = []
        
        for y, row in enumerate(self._expanded):
            for x, col in enumerate(row):
                if self._expanded[x][y] != -1:
                    path.append((x, y))
        
        self._board.set_path(path[1:-1])

