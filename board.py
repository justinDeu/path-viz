class Board():

    def __init__(self, width, height):
        self.height = height
        self.widith = width

        self.board = [[0 for i in range(width)] for j in range(height)]

    def toggle(self, x, y):
        if self.board[x][y] == 0:
            self.board[x][y] == 1
        elif self.board[x][y] == 1:
            self.board[x][y] == 0