from algo import Algo

class BruteForce(Algo):
    """
    A brute force algorithm that will check all the surrounding cells
    to those in the list until it finds a path.

    Only can tell if a path exists between the start and end 
    """

    def __init__(self, board):
        super().__init__(board)
        self._nodes = [self._board.start()]    # list of tuples representing the points visited 

    def step(self):
        """Advances the algorithm one step closer to the end"""
        next = self._nodes.pop(0)
        self._add_nearby_cells(next)
        self._board.explore(next[0], next[1])

    def running(self):
        """Returns whether the algorithm has finished or not"""
        return self._next_step() != self._board.end()

    def _next_step(self):
        return self._nodes[0]

    def _add_nearby_cells(self, point):
        """
        Attempts to add the 4 surrounding points to the point given as a tuple
        to the list of nodes.

        Will not add if the point is already in the list or it is a wall
        """
        offsets = (-1, 1)
        (x_pos, y_pos) = point

        for x_off in offsets:
            for y_off in offsets:
                if x_pos + x_off >= 0 and x_pos + x_off < self._board.width() and y_pos + y_off >= 0 and y_pos + y_off < self._board.height():
                    self._add_cell((x_pos + x_off, y_pos + y_off))


    def _add_cell(self, cell):
        """
        Adds the cell, given as a tuple, to the list if it is not and it
        is not a wall.
        """
        if self._board.state(cell[0], cell[1]) != 1 and cell not in self._nodes:
            self._nodes.append(cell) 


    