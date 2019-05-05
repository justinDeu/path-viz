class Board():

    def __init__(self, width, height):
        self.height = height
        self.width = width

        self.board = [[0 for i in range(width)] for j in range(height)]

        self.startTracker = 1
        self.start = (0, 0)
        self.end = (0, 0)

    def toggle(self, x, y):
        if self.board[x][y] == 0:
            self.board[x][y] = 1
        elif self.board[x][y] == 1:
            self.board[x][y] = 0

        return self.board[x][y]

    def setStartEnd(self, x, y):
        if self.startTracker == 1:
            self.board[x][y] = 2
            self.board[self.start[0]][self.start[1]] = 0
            self.start = (x, y)
        else:
            self.board[x][y] = 3
            self.board[self.end[0]][self.end[1]] = 0
            self.end = (x, y)
        
        self.startTracker = self.startTracker * -1