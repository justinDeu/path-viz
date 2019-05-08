from board import Board 
import pygame as pg
from pygame.locals import *
from algo import Algo
from cheat import Cheat
from brute import BruteForce
from astar2 import AStar2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (169, 169, 169)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
RUST = (139, 64, 0)

COLORS = {
    0: WHITE,
    1: GREEN,
    2: BLUE,
    3: RED,
    4: ORANGE,
    5: RUST
}

BACKGROUND_COLOR = GREY
GRID_BACKGROUND_COLOR = BLACK
CELL_COLOR = WHITE

MARGIN = 5

TIME_DELAY = 100

class PathUI():

    def __init__(self, board, width, height, cell_size):
        self.board = board
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self._running = True
        self._display_surf = pg.display.set_mode((self.width + 300, self.height), pg.HWSURFACE)

        pg.init()

        pg.display.set_caption('Path Visualizer')
        self.init_rects()
        self.render()
        self._running = True


    def init_rects(self):
        rects = []
        for row in range(self.board.height()):
            rects.append([])
            for col in range(self.board.width()):
                rect = pg.Rect((self.cell_size + MARGIN) * col + MARGIN,
                               (self.cell_size + MARGIN) * row + MARGIN, 
                                self.cell_size,
                                self.cell_size)
                rects[row].append(rect)
        self.rects = rects
        

    def draw_grid(self):
        for i, row in enumerate(self.rects):
            for j, rect in enumerate(row):
                pg.draw.rect(self._display_surf, self._color(self.board.state(i, j)), rect)


    def handle_event(self, event):
        if event.type == pg.QUIT:
            self._running = False
            return
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.run_btn.collidepoint(event.pos):
                    self.run_button_clicked()
                    return
                if self.reset_btn.collidepoint(event.pos):
                    self.reset()
                    return
                for i, row in enumerate(self.rects):
                    for j, rect in enumerate(row):
                        if rect.collidepoint(event.pos):
                            self.board.toggle_wall(i, j)
                            self.render()
                            return
            elif event.button == 3:
                for i, row in enumerate(self.rects):
                    for j, rect in enumerate(row):
                        if rect.collidepoint(event.pos):
                            self.board.set_start_end(i, j)
                            self.render()
                            return
            return

        elif event.type == pg.MOUSEMOTION and pg.mouse.get_pressed()[0]:
            for i, row in enumerate(self.rects):
                for j, rect in enumerate(row):
                    if rect.collidepoint(event.pos) and self.board.state(i, j) != 1:
                        self.board.toggle_wall(i, j)
                        self.render()
                        return

            return

    def _color(self, val):
        return COLORS[val]

    def render(self):
        self._display_surf.fill(BACKGROUND_COLOR)
        pg.draw.rect(self._display_surf, GRID_BACKGROUND_COLOR,
            pg.Rect(0, 0, (self.board.width() * (self.cell_size + MARGIN)) + MARGIN, 
                (self.board.height() * (self.cell_size + MARGIN)) + MARGIN))
        self.draw_grid()
        self.run_btn = self.draw_button("Run Search", (self.width+200, self.height // 2))
        self.reset_btn = self.draw_button("Reset", (self.width + 200, (self.height // 2) + 80))
        pg.display.flip()

    def on_cleanup(self):
        pg.quit()

    def execute(self):
        while self._running:
            pg.event.pump()
            for event in pg.event.get():
                self.handle_event(event) 
        self.on_cleanup()

    def draw_button(self, txt, location, size=(80, 50)):
        text = pg.font.SysFont('Arial', 15)
        txt_surf = text.render(txt, False, BLACK)
        btn = pg.Rect(location[0], location[1], size[0], size[1])
        pg.draw.rect(self._display_surf, RED, btn)
        self._display_surf.blit(txt_surf, location)
        return btn
    
    def run_button_clicked(self):
        algo = AStar2(self.board)
        while(algo.running()):
            algo.step()
            self.render()
            pg.time.delay(TIME_DELAY)
        
        algo.set_path()
        self.render()
    
    def reset(self):
        self.board = Board(self.width // self.cell_size, self.height // self.cell_size)
        self.render()
