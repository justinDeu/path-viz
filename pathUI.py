import tkinter as tk

WIDTH, HEIGHT = 500, 500
MARGIN = 0
SIDE = 20

class PathUI(tk.Frame):
    def __init__(self, parent, algo):
        self.algo = algo
        self.parent = parent
        tk.Frame.__init__(self, parent)

        self.row, self.col = 0, 0

        self.__initUI()

    def __initUI(self):
        self.parent.title("Path Vizualizer")
        self.pack(fill=tk.BOTH, expand=1)
        self.canvas = tk.Canvas(self,
                             width=WIDTH,
                             height=HEIGHT)
        self.canvas.pack(fill=tk.BOTH, side=tk.TOP)
        clear_button = tk.Button(self,
                              text="Clear Grid",
                              command=self.__clear_grid)
        clear_button.pack(fill=tk.BOTH, side=tk.LEFT)

        self.__draw_grid()
        
        self.canvas.bind("<Button-1>", self.__cell_clicked)

    def __clear_grid(self):
        print("Clear Grid clicked")

    def __cell_clicked(self, event):
        print("Canvas Clicked @ (%d, %d)" % (event.x , event.y))

    def __draw_grid(self):
        for i in range(25):
            color = "black"

            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)