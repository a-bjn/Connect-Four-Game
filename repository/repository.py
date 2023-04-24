from domain.grid import Grid


class GridRepository:

    def __init__(self):
        self.__grid = Grid()

    def grid(self):
        return self.__grid
