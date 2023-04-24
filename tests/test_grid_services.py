import unittest
import math
from services.gridServices import GridService
from repository.repository import GridRepository
from domain.grid import Grid


class ServiceGridTest(unittest.TestCase):

    @staticmethod
    def test_grid_service_minimax():
        grid_repo = GridRepository()
        grid_service = GridService(grid_repo)
        grid = Grid
        grid_service.minimax(grid.map, 3, -math.inf, math.inf, True)
