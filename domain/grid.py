from texttable import Texttable
from domain.cell import Cell
import pygame


class Grid:

    def __init__(self):
        self.__rows = 6
        self.__cols = 7
        self.__map = [[Cell() for i in range(self.__cols)] for j in range(self.__rows)]
        self.__turn = ""
        self.__player_piece = "#"
        self.__computer_piece = "*"

    @property
    def rows(self):
        return self.__rows

    @property
    def cols(self):
        return self.__cols

    @property
    def map(self):
        return self.__map

    @property
    def turn(self):
        return self.__turn

    @property
    def player_piece(self):
        return self.__player_piece

    @property
    def computer_piece(self):
        return self.__computer_piece

    @turn.setter
    def turn(self, value):
        self.__turn = value

    def draw_board(self, grid, screen, square_size, height):
        for c in range(self.__cols):
            for r in range(self.__rows):
                pygame.draw.rect(screen, (0, 0, 255),
                                 (c * square_size, r * square_size + square_size, square_size, square_size))
                pygame.draw.circle(screen, (0, 0, 0), (int(c * square_size + square_size / 2),
                                   int(r * square_size + square_size + square_size / 2)),
                                   int(square_size / 2 - 5))
        for c in range(self.__cols):
            for r in range(self.__rows):
                if grid[r][c].occupied == "#":
                    pygame.draw.circle(screen, (255, 0, 0), (int(c * square_size + square_size / 2),
                                       height - int(r * square_size + square_size / 2)),
                                       int(square_size / 2 - 5))
                elif grid[r][c].occupied == "*":
                    pygame.draw.circle(screen, (255, 255, 0),
                                       (int(c * square_size + square_size / 2),
                                        height - int(r * square_size + square_size / 2)), int(square_size / 2 - 5))
        pygame.display.update()

    def __str__(self):
        tab = Texttable()
        header = list()

        for col in range(self.__cols):
            aux = col
            header.append(str(aux))

        tab.header(["/"] + header)

        for row in range(self.__rows - 1, -1, -1):
            tab.add_row([str(row)] + self.__map[row])

        return tab.draw()
