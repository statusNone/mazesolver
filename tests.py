import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Check the total number of cells
        self.assertEqual(
            len(m1._cells),
            num_cols * num_rows,
        )

        # Check if specific keys exist
        self.assertIn((0, 0), m1._cells)
        self.assertIn((num_cols - 1, num_rows - 1), m1._cells)

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Check the total number of cells
        self.assertEqual(
            len(m1._cells),
            num_cols * num_rows,
        )

        # Check if specific keys exist
        self.assertIn((0, 0), m1._cells)
        self.assertIn((num_cols - 1, num_rows - 1), m1._cells)

if __name__ == "__main__":
    unittest.main()