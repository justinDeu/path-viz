from board import Board 
import pygame as pg
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

COLORS = {
    0: WHITE,
    1: GREEN,
    2: BLUE,
    3: RED,
    4: ORANGE
}

BACKGROUND_COLOR = BLACK
CELL_COLOR = WHITE
ACTIVE_CELL_COLOR = GREEN

MARGIN = 5

class PathUI():

    def __init__(self, board, width, height, cell_size):
        self.board = board
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self._running = True
        self._display_surf = pg.display.set_mode((self.width, self.height), pg.HWSURFACE)

        pg.init()

        pg.display.set_caption('Path Visualizer')
        self.init_rects()
        self.render()
        self._running = True

    def init_rects(self):
        rects = []
        for row in range(self.board.height):
            rects.append([])
            for col in range(self.board.width):
                rect = pg.Rect((self.cell_size + MARGIN) * col + MARGIN,
                               (self.cell_size + MARGIN) * row + MARGIN, 
                                self.cell_size,
                                self.cell_size)
                rects[row].append(rect)
        self.rects = rects
        

    def draw_grid(self):
        for i, row in enumerate(self.rects):
            for j, rect in enumerate(row):
                pg.draw.rect(self._display_surf, self._color(self.board.board[i][j]), rect)


    def handle_event(self, event):
        if event.type == pg.QUIT:
            self._running = False
            return
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, row in enumerate(self.rects):
                    for j, rect in enumerate(row):
                        if rect.collidepoint(event.pos):
                            self.board.toggle(i, j)
                            self.render()
                            return
            elif event.button == 3:
                for i, row in enumerate(self.rects):
                    for j, rect in enumerate(row):
                        if rect.collidepoint(event.pos):
                            self.board.setStartEnd(i, j)
                            self.render()
                            return
            return

        elif event.type == pg.MOUSEMOTION and pg.mouse.get_pressed()[0]:
            for i, row in enumerate(self.rects):
                for j, rect in enumerate(row):
                    if rect.collidepoint(event.pos) and self.board.board[i][j] != 1:
                        self.board.toggle(i, j)
                        self.render()
                        return

            return

    def _color(self, val):
        return COLORS[val]

    def render(self):
        self._display_surf.fill(BACKGROUND_COLOR)
        self.draw_grid()
        pg.display.flip()

    def on_cleanup(self):
        pg.quit()

    def execute(self):
        while self._running:
            pg.event.pump()
            for event in pg.event.get():
                self.handle_event(event) 
        self.on_cleanup()
    
