class Board():

    def __init__(self, width, height):
        self.height = height
        self.widith = width

        self.board = [[None for i in range(width)] for j in range(height)]
        print(self.board)