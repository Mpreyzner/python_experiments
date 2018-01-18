import random
import numpy
import pprint
from math import *

grid_size = 10
number_of_mines = 3


class Grid:
    def __init__(self, size, number_of_mines):
        self.size = size
        self.number_of_mines = number_of_mines
        self.grid = []
        self.covered_grid = []

    def generate_empty(self):
        grid = [[0 for x in range(self.size)] for y in range(self.size)]
        return grid

    def generate_random_coordinates(self, limit):
        return random.randint(0, limit), random.randint(0, limit)

    def generate_mines(self, number_of_mines):
        mines = []
        # it can generate same mines ;D
        for i in range(number_of_mines):
            x, y = self.generate_random_coordinates(self.size - 1)
            if (x, y) in mines:
                # what if it generates the same number n times?
                x, y = self.generate_random_coordinates(self.size - 1)
            mines.append((x, y))
        return mines

    def add_mines(self, mines, grid):
        for i in range(len(mines)):
            x, y = mines[i][0], mines[i][1]
            grid[x][y] = -1
        return grid

    def add_distance_to_mines(self, grid, mines):
        for x in range(self.size):
            for y in range(self.size):
                for mine in mines:
                    distance = sqrt((x - mine[0]) ** 2 + (y - mine[1]) ** 2)
                    if 2 > distance >= 1 and grid[x][y] != -1:
                        grid[x][y] = grid[x][y] + 1
                        # 1 for adjacent and 1.4ish for slant
        return grid

    def cover_grid(self):
        covered_grid = [['*' for x in range(self.size)] for y in range(self.size)]
        return covered_grid

    def render(self):
        grid = self.generate_empty()
        mines = self.generate_mines(self.number_of_mines)
        grid_with_mines = self.add_mines(mines, grid)
        grid_with_distances = self.add_distance_to_mines(grid_with_mines, mines)
        covered_grid = self.cover(grid_with_distances)
        return covered_grid




# the player is initially presented with a grid of undifferentiated squares.
# Some randomly selected squares, unknown to the player, are designated to contain mines.
# Typically, the size of the grid and the number of mines are set in advance by the user
# The game is played by revealing squares of the grid by indicating each coordinates square.
# If a square containing a mine is revealed, the player loses the game. I
# f no mine is revealed, a digit is instead displayed in the square, indicating how many adjacent squares contain mines;
#  if no mines are adjacent, the square becomes blank, and all adjacent squares will be recursively revealed.
# The player uses this information to deduce the contents of other squares, and may either safely reveal each square or mark the square as containing a mine.

# In some versions, a question mark may be placed in an unrevealed square to serve as an aid to logical deduction. Implementations may also allow players to quickly "clear around" a revealed square once the correct number of mines have been flagged around it. The game is won when all mine-free squares are revealed, because all mines have been located.

# Some versions of Minesweeper will set up the board by never placing a mine on the first square revealed.[1] Minesweeper for versions of Windows protects the first square revealed; in Windows 7, players may elect to replay a board, in which case the first square may no longer be protected.
