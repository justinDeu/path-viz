from board import Board 
import pygame as pg
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

BACKGROUND_COLOR = BLACK
CELL_COLOR = WHITE
ACTIVE_CELL_COLOR = GREEN

class PathUI():

    WIDTH, HEIGHT = 505, 505
    CELL_SIZE = 15
    MARGIN = 5

    def __init__(self):
        self._running = True
        self._display_surf = pg.display.set_mode((self.WIDTH, self.HEIGHT), pg.HWSURFACE)
        self.board = Board(100, 100)

        pg.init()

        pg.display.set_caption('Path Visualizer')
        self.init_rects()
        self.render()
        self._running = True

    def init_rects(self):
        rects = []
        for row in range(self.HEIGHT // self.CELL_SIZE):
            rects.append([])
            for col in range(self.WIDTH // self.CELL_SIZE):
                rect = pg.Rect((self.CELL_SIZE + self.MARGIN) * col + self.MARGIN, (self.CELL_SIZE + self.MARGIN) * row + self.MARGIN, self.CELL_SIZE, self.CELL_SIZE)
                rects[row].append([rect, CELL_COLOR])
        self.rects = rects
        

    def draw_grid(self):
        for row in self.rects:
            for item in row:
                pg.draw.rect(self._display_surf, item[1], item[0])


    def handle_event(self, event):
        if event.type == pg.QUIT:
            self._running = False
            return
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            for row in self.rects:
                for item in row:
                    rect = item[0]
                    if rect.collidepoint(event.pos):
                        item[1] = ACTIVE_CELL_COLOR
                        self.render()
                        return
            return
        elif event.type == pg.MOUSEMOTION and pg.mouse.get_pressed()[0]:
            for row in self.rects:
                for item in row:
                    rect = item[0]
                    if rect.collidepoint(event.pos):
                        item[1] = ACTIVE_CELL_COLOR
                        self.render()
                        return

            return

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
    
