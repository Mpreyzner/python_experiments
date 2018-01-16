import minesweeper
import unittest
import pprint
from unittest_data_provider import data_provider

class TestGrid(unittest.TestCase):

    def test_generating_empty_grid(self):
        grid = minesweeper.Grid(3, 1)
        empty_grid = grid.generate_empty()

        self.assertEqual([[0, 0, 0], [0, 0, 0], [0, 0, 0]], empty_grid)

    def test_generating_mines(self):
        grid = minesweeper.Grid(3, 1)
        mines = grid.generate_mines(2)

        self.assertEqual(2, len(mines))

    def test_adding_mines(self):
        grid = minesweeper.Grid(2, 1)
        empty_grid = grid.generate_empty()
        mines = grid.generate_mines(2)

        grid_with_mines = grid.add_mines(mines, empty_grid)

        self.assertEqual(2, (grid_with_mines[0] + grid_with_mines[1]).count(-1))

    def data_provider(self):

        yield [[(0, 0)], [[-1, 1], [1, 1]]]
        yield [[(0, 1)], [[1, -1], [1, 1]]]
        yield [[(1, 0)], [[1, 1], [-1, 1]]]
        yield [[(1, 1)], [[1, 1], [1, -1]]]

        # for i in len(3):
        #     self.adding_distance_to_mines(test_data[i][0], test_data[i][1])

    def test_adding_distance_to_mines(self):
        grid = minesweeper.Grid(2, 1)
        empty_grid = grid.generate_empty()
        temp = next(self.foo())
        mines = temp[0]
        result = temp[1]
        # print(mines)
        print(result)
        grid_with_mines = grid.add_mines(mines, empty_grid)
        # print(grid_with_mines)
        complete_grid = grid.add_distance_to_mines(grid_with_mines, mines)
        # print(complete_grid)
        self.assertEqual(result, complete_grid)


if __name__ == '__main__':
    unittest.main()
