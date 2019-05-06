class Board():
    """Represents a board with a start, end, and walls on it. Provides public functions
    To manipulate the board while solving the path from start to end.

    Notation:
        0 - a clear spot
        1 - a wall 
        2 - the start point
        3 - the end point 
        4 - an explored location
    """

    def __init__(self, width, height):
        """Creates a new Board with the given dimensions"""
        self._height = height
        self._width = width

        self._board = [[0 for i in range(width)] for j in range(height)]

        self._startTracker = 1
        self._start = (0, 0)
        self._end = (0, 0)

    def toggle_wall(self, x, y):
        """Toggles a wall on and off at a given position
        
        Returns the new state of the cell
        """
        if self._board[x][y] == 0:
            self._board[x][y] = 1
        elif self._board[x][y] == 1:
            self._board[x][y] = 0

        return self._board[x][y]

    def set_start_end(self, x, y):
        """Toggles the given location as the new start/end point"""
        if self._startTracker == 1:
            self._board[x][y] = 2
            self._board[self._start[0]][self._start[1]] = 0
            self._start = (x, y)
        else:
            self._board[x][y] = 3
            self._board[self._end[0]][self._end[1]] = 0
            self._end = (x, y)
        
        self._startTracker = self._startTracker * -1
    
    def state(self, x, y):
        """Returns the current state of the given location"""
        return self._board[x][y]

    def explore(self, x, y):
        """Markes the given location as explored"""
        self._board[x][y] = 4

    def width(self):
        """Returns the board's width"""
        return self._width
    
    def height(self):
        """Returns the board's height"""
        return self._height