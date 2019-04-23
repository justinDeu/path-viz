class Board():

    def __init__(self, width, height):
        self.height = height
        self.widith = width

        self.board = [[0 for i in range(width)] for j in range(height)]