from algo import Algo

class Cheat(Algo):
    """
    Defines an algorithm to find the shortest path that cheats. This
    algorithm will ignore walls and take the most direct path possible.
    """

    def __init__(self):
        """
        Sets up the cheating algorithm with its current position as the
        start position.
        """
        super().__init__()
        self._curr = self._start

    def step(self) -> (int, int):
        """
        Advances the current position in the most direct path possible
        to the end point and explores the next position in the sequence

        Returns the position explored
        """

        x_offset = 0
        y_offset = 0

        if (self._curr[0] < self._end[0]):
            x_offset = 1
        elif (self._curr[0] > self._end[0]):
            x_offset = -1

        if (self._curr[1] < self._end[1]):
            y_offset = 1
        elif (self._curr[1] > self._end[1]):
            y_offset = -1
        
        self._update_curr(x_offset, y_offset)
        self._board.explore(self._curr[0], self._curr[1])
        return self._curr
            
            

    def running(self) -> bool:
        """
        Returns true once the algorithm has reached the end position
        in its cheating manner 
        """
        return self._curr == self._end 

    def _update_curr(self, x, y):
        """
        Updates the current position by the amounts specified in the 
        x and y directions
        """
        self._curr = (self._curr[0] + x, self._curr[1] + y)