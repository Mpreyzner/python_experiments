import minesweeper
import unittest
import pprint


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

    def test_adding_distance_to_mines(self):
        grid = minesweeper.Grid(2, 1)
        empty_grid = grid.generate_empty()
        temp = next(self.data_provider())
        mines = temp[0]
        result = temp[1]
        grid_with_mines = grid.add_mines(mines, empty_grid)
        complete_grid = grid.add_distance_to_mines(grid_with_mines, mines)
        self.assertEqual(result, complete_grid)

    def test_adding(self):
        mines_number = 3
        grid = minesweeper.Grid(3, 3)
        empty_grid = grid.generate_empty()
        mines = grid.generate_mines(mines_number)
        # result = temp[1]
        # print(mines)
        # print(result)

        grid_with_mines = grid.add_mines(mines, empty_grid)
        # print(grid_with_mines)
        complete_grid = grid.add_distance_to_mines(grid_with_mines, mines)
        sum = []
        for i in range(len(complete_grid)):
            sum = sum + (complete_grid[i])

        self.assertEqual(3, sum.count(-1))

    def test_covering_grid(self):
        grid = minesweeper.Grid(2, 1)
        covered_grid = grid.cover_grid()
        sum = []
        for i in range(len(covered_grid)):
            sum = sum + (covered_grid[i])
        self.assertEqual(4, sum.count('*'))

    def test_rendering_grid(self):
        grid = minesweeper.Grid(2, 1)
        result = grid.render()
        self.assertEqual(['*', '*'], ['*', '*'], result)

    def test_uncover_field(self):
        grid = minesweeper.Grid(2, 1)
        grid.render()
        uncovered = grid.reveal(0,0)
        self.assertNotEqual([['*', '*'], ['*', '*']], uncovered)


if __name__ == '__main__':
    unittest.main()
