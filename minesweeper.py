import random
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
        self.last_revealed = ()

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
        self.grid = grid
        return grid

    def cover_grid(self):
        covered_grid = [['*' for x in range(self.size)] for y in range(self.size)]
        self.covered_grid = covered_grid
        return covered_grid

    def render(self):
        grid = self.generate_empty()
        mines = self.generate_mines(self.number_of_mines)
        grid_with_mines = self.add_mines(mines, grid)
        grid_with_distances = self.add_distance_to_mines(grid_with_mines, mines)
        covered_grid = self.cover_grid()
        return covered_grid

    def reveal(self, x, y):
        self.covered_grid[x][y] = self.grid[x][y]
        self.last_revealed = self.covered_grid[x][y]
        return self.covered_grid

    def lost(self):
        if self.last_revealed == -1:
            return True
        else:
            return False

    def won(self):
        sum = []
        for i in range(len(self.covered_grid)):
            sum = sum + (self.covered_grid[i])

        won = (sum.count('*') == self.number_of_mines)
        # print(sum)
        # print(self.number_of_mines)
        return won


def print_grid(grid):
    for i in reversed(range(len(grid))):
        print(grid[i])


grid = Grid(3,3)
foo = grid.render()
print_grid(foo)
while True:
    x = int(input("Enter x coordinate of box you want to reveal \n"))
    y = int(input("Enter y coordinate of box you want to reveal \n"))
    res = grid.reveal(x, y)
    print_grid(res)
    if grid.lost():
        print('Ooops! Mine you lost')
        break
    if grid.won():
        print('You won. Congratulations')
        break


# add some better printing
# fix bug with generating mines with same coordinates
