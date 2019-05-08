from board import Board

class Algo():
    """Defines an algorithm to find a path from a start to an end point.
    
    The algorithm will be run against a 2D array where different values 
    signify some state in the path. The values are as follows:
        0 - a free cell
        1 - a blocked cell (cannot take)
        2 - the start point
        3 - the end point
        4 - an explored point 

    All algorithms will expose 3 public functions: a constructor, the step function,
    and a boolean solved function.
    """

    def __init__(self, board: Board):
        self._board = board
        self._start = board.start()
        self._end = board.end()
        self._path = []
    
    def step(self) -> (int, int):
        """Advances the algorithm through one iteration exploring one 
        more position on the board

        Returns a tuple of the position explored 
        """
        pass
    
    def running(self) -> bool:
        """
        Returns a boolean value of whether the algorith has found a
        
            True - path has been found/no possible path
            False - path has not been found 
        """
        pass

    def set_path(self):
        """
        Sets the path found on the board, should call board.set_path
        """
        pass