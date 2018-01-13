import random

grid_size = 10
number_of_mines = 3

#if all fields are uncovered except mines user won


def generate_grid(size, number_of_mines):
    # grid = []
    grid = [[0 for x in range(size)] for y in range(size)]
    for i in range(number_of_mines):
        x, y = random.randint(0, size - 1), random.randint(0, size -1)
        grid[x][y] = -1

    return grid


def uncover_cell(x, y):
    return 1;


def mark_field_as_mine(x,y):
    return []


def print_current_grid(grid):
    return []


def reveal_field():
    x = input('Select x of field you want to uncover')
    y = input('Select y of field you want to uncover')
    uncover_cell(x, y)
    return []  # return grid with revealed field


grid = generate_grid(grid_size, number_of_mines)
print(grid)
#
# while True:
#     print_current_grid(grid)
#     grid = reveal_field()

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
