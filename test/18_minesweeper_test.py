import minesweeper
import unittest


class TestGrid(unittest.TestCase):

    def test_generating_empty_grid(self):
        grid = minesweeper.Grid(2, 1)
        print(grid)
        self.assertFalse(True)
        # self.assertEqual()


if __name__ == '__main__':
    unittest.main()
#
# def test_generating_empty_grid():
#     grid = minesweeper.Grid(2, 1)
#     print(grid)
#     unittest.ass
