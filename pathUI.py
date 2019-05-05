from board import Board 
import pygame as pg
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (169, 169, 169)
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

BACKGROUND_COLOR = GREY
GRID_BACKGROUND_COLOR = BLACK
CELL_COLOR = WHITE
ACTIVE_CELL_COLOR = GREEN

MARGIN = 5

def button_clicked():
    print("Clicked button")

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
        pg.draw.rect(self._display_surf, GRID_BACKGROUND_COLOR,
            pg.Rect(0, 0, (len(self.board.board) * (self.cell_size + MARGIN)) + MARGIN, 
                (len(self.board.board[0]) * (self.cell_size + MARGIN)) + MARGIN))
        self.draw_grid()
        self.draw_button("Find Path", (self.width+200, self.height // 2))
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
        self.button = pg.Rect(location[0], location[1], size[0], size[1])
        pg.draw.rect(self._display_surf, RED, self.button)


class Button():
    def __init__(self, txt, location, action, display, bg=RED, fg=BLUE, size=(80, 30), font_name="Segoe Print", font_size=16):
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size
        self.screen = display

        self.font = pg.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pg.surface.Surface(size)
        self.rect = pg.Rect(location[0], location[1], size[0], size[1])

        self.call_back_ = action

    def draw(self):

        self.screen.draw(self.rect)
        self.screen.draw(self.txt_rect)

        """ self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        self.screen.blit(self.surface, self.rect) """

    def call_back(self):
        self.call_back_()
    
