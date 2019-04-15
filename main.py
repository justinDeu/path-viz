from pathUI import PathUI
from board import Board
from tkinter import Tk

WIDTH, HEIGHT = 500, 500


if __name__ == "__main__":
    algo = None
    root = Tk()
    root.geometry("%dx%d" % (WIDTH, HEIGHT + 50))
    PathUI(root, algo)
    root.mainloop()