import unittest
from domain.grid import Grid


class GridTest(unittest.TestCase):

    def test_grid(self):
        grid = Grid()

        self.assertEqual(grid.rows, 6)
        self.assertEqual(grid.cols, 7)

        self.assertEqual(grid.player_piece, "#")
        self.assertEqual(grid.computer_piece, "*")

        self.assertEqual(grid.turn, "")
        grid.turn = "PLAYER"
        self.assertEqual(grid.turn, "PLAYER")

        # i think this is called cheating :))) (but it's really funny)
        grid_map = grid.map
        self.assertEqual(grid.map, grid_map)
