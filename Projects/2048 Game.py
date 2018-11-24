"""
Clone of 2048 game.
"""

import poc_2048_gui
#import Test2048
import random
#import my_module as tools

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # replace with your code from the previous mini-project
    res = []
    index = 0
    for num in line:
        res.append(0)
        if num != 0:
            res[index] = num
            index += 1
    
    for dummy_num in range(len(res)-1):
        if res[dummy_num] == res[dummy_num+1]:
            res[dummy_num] *= 2
            res.append(0)
            res.pop(dummy_num+1)
    return res

# helper function
def make_2d_grid(a_list, width, height, side=None):
    """
    create a 2D grid (rows and columns)
    """
    result = "["
    for row in range(height):
        result += "["
        if side is not None:
            result += str(side[row])+": "
        for colum in range(width):
            result += str(a_list[row][colum])
            if colum < width-1:
                result += ", "
        result += "]"
        if row < height-1:
            result += "\n"
    result += "]"
    return result

# main class
class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._height = grid_height
        self._width = grid_width
        self.reset()

        # dictionary
        self._tiles_up = [(0, col) for col in range(self._width)]
        self._tiles_down = [(self._height-1, col) for col in range(self._width)]
        self._tiles_left = [(row, 0) for row in range(self._height)]
        self._tiles_right = [(row, self._width-1) for row in range(self._height)]

        # arrows
        self._arrows = {UP: self._tiles_up,
                        DOWN: self._tiles_down,
                        LEFT: self._tiles_left,
                        RIGHT: self._tiles_right}

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        # create a new grid
        self._grid = [[0 for dummy_i in range(self._width)] for dummy_j in range(self._height)]

        # add two cards
        self.new_tile()
        self.new_tile()


    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        self._print_list = make_2d_grid(self._grid,self.get_grid_width(),self.get_grid_height())
        return self._print_list

    def get_grid(self):
        """
        get grid value as a list for debuging
        """
        return self._grid

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return len(self._grid)

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return len(self._grid[0])

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        length = 0
        self._is_changed = False
        if OFFSETS[direction][1] == 0:
            length = len(self._grid)
        else:
            length = len(self._grid[0])

        for element in range(len(self._arrows[direction])):
            t_list = []
            for step in range(length):
                row = self._arrows[direction][element][0] + step * OFFSETS[direction][0]
                col = self._arrows[direction][element][1] + step * OFFSETS[direction][1]
                t_list.append(self._grid[row][col])
            t_list = merge(t_list)

            for back in range(len(t_list)):
                row = self._arrows[direction][element][0] + back * OFFSETS[direction][0]
                col = self._arrows[direction][element][1] + back * OFFSETS[direction][1]
                temp = self._grid[row][col]
                self._grid[row][col] = t_list[back]
                if self._grid[row][col] != temp:
                    self._is_changed = True
        if self._is_changed:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        rand = 2
        if random.randint(0, 10) == 1:
            rand = 4
        first_pass = True
        r_row = 0
        r_col = 0
        while first_pass or self._grid[r_row][r_col] != 0:
            first_pass = False
            r_row = random.randrange(0, self._height)
            r_col = random.randrange(0, self._width)
        self._grid[r_row][r_col] = rand

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))


#print "below arrows thing"
#print game._arrows[UP][2][1]
# ===== Tests =====
#Test2048.run_suite(TwentyFortyEight)