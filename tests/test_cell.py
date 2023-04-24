import unittest
from domain.cell import Cell


class CellTest(unittest.TestCase):

    def test_cell(self):
        cell = Cell()

        cell.occupied = "#"
        self.assertEqual(cell.occupied, "#")
        self.assertEqual(cell.__str__(), "#")
        cell.occupied = "*"
        self.assertEqual(cell.occupied, "*")
        self.assertEqual(cell.__str__(), "*")

        cell.occupied = ""
        self.assertEqual(cell.occupied, "")
        self.assertEqual(cell.__str__(), "")
