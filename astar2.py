from algo import Algo
import sys

class AStar2(Algo):
    """
    Implements the A* search algorithm to be used in the ui.
    """
    def __init__(self, board):
        super().__init__(board)

        self._h_costs = self._cost_array(self._end[0], self._end[1])
        #self._g_costs = self._cost_array(self._start[0], self._start[1])

        self._closed = []   # The list of already visited nodes
        self._open = [Node(self._start, None, 0, self._h_costs[self._start[1]][self._start[0]])]

        self._curr = self._min_f()

    def step(self):

        # Finding the open node with he lowest f cost 
        self._curr = self._min_f()

        # Removing the current node from the open list and adding it to the closed list
        self._open.remove(self._curr)
        self._closed.append(self._curr)

        # Got to the end, all finished
        if self._curr.loc == self._end:
            return

        # Get the neighbors for current
        neighbors = self._neighbors(self._curr.loc)

        # Analyze each of the neighbors
        for neighbor in neighbors:

            # Neighbor in closed, don't do anything 
            if neighbor in [n.loc for n in self._closed]:
                continue
            
            # if neighbor isn't wall
            if self._board.state(neighbor[0], neighbor[1]) != 1:
                g_cost = self._curr.g + 1
                h_cost = self._h_costs[neighbor[1]][neighbor[0]]

                # Have not seen it before, add to open
                if neighbor not in [n.loc for n in self._open]:
                    self._open.append(Node(neighbor, self._curr, g_cost, h_cost))
                    self._board.explore(neighbor[0], neighbor[1])
                    continue
                
                # Check if the new path to it is shorter
                for node in self._open:
                    if node.loc == neighbor and g_cost + h_cost < node.f():
                        node.g = g_cost
                        node.h = h_cost          # shouldn't have to do because h costs are constant
                        node.parent = self._curr
            

    def set_path(self):
        path = []

        curr = self._curr

        while curr:
            path.append(curr.loc)
            curr = curr.parent
        
        self._board.set_path(path)

    def running(self):
        return self._curr.loc != self._end

    def _cost_array(self, x, y):
        costs = [[sys.maxsize for _ in range(self._board.width())] for _ in range(self._board.height())]
        to_check = []

        costs[y][x] = 0
        neighbors = self._neighbors((x, y))

        for n in neighbors:
            to_check.append(n)
            costs[n[1]][n[0]] = 1

        while to_check:
            curr = to_check.pop()
            val = costs[curr[1]][curr[0]]
            neighbors = self._neighbors(curr)

            for n in neighbors:
                if val + 1 < costs[n[1]][n[0]]:
                    costs[n[1]][n[0]] = val + 1
                    to_check.append(n)

        return costs


    def _neighbors(self, loc):
        """ Returns a list of neighboring locations that are available """
        offsets = [-1, 1]
        neighbors = []

        for o in offsets:
            if 0 <= loc[0] + o < self._board.width():
                neighbors.append((loc[0] + o, loc[1]))
                    
            if 0 <= loc[1] + o < self._board.height(): 
                neighbors.append((loc[0], loc[1] + o))

        return neighbors

    def _min_f(self):
        """
        Finds the node in the open list with the lowest f cost, in the case of ties,
        goes to h cost

        returns the node with minimum f and then h costs
        """
        lowest = self._open[0]
        for node in self._open:
            if node.f() < lowest.f():
                lowest = node
            elif node.f() == lowest.f() and node.h < lowest.h:
                lowest = node
        
        return lowest



class Node():
    """ A Node class for running the algorithm """

    def __init__(self, loc, parent, g, h):
        self.loc = loc      # Node's location as (x, y)
        self.parent = parent    # Node's parent node
        self.g = g      # Node's distance from start
        self.h = h      # Node's distance from en

    def f(self):
        """ The combined cost of the node """
        return self.g + self.h