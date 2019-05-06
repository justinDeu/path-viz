from pathUI import PathUI
from board import Board

WIDTH, HEIGHT = 505, 505
CELL_SIZE = 15
MARGIN = 5

if __name__ == "__main__":
    board = Board(WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE)
    ui = PathUI(board, WIDTH, HEIGHT, CELL_SIZE)
    ui.execute()
    