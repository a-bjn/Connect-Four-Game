import math
import sys
import pygame
from domain.grid import Grid


class Ui:

    def __init__(self, grid_service):
        self.__grid_service = grid_service
        self.__grid_domain = Grid()

    def start(self):
        grid = self.__grid_service.get_grid()
        grid.turn = self.__grid_service.coin_flip_turn()
        game_over = False

        command = input("Would you like to play the game with gui?(y/n)")

        if command == "n":
            while not game_over:
                if grid.turn == "PLAYER":
                    col = int(input("Player: "))
                    if self.__grid_service.is_valid_location(grid.map, col):
                        row = self.__grid_service.get_next_open_row(grid.map, col)
                        self.__grid_service.drop_piece(grid.map, row, col, grid.player_piece)
                        if self.__grid_service.winning_move(grid.map, grid.player_piece):
                            print("Player Win!")
                            game_over = True
                    grid.turn = "COMPUTER"
                elif grid.turn == "COMPUTER":
                    col, minimax_score = self.__grid_service.minimax(grid.map, 5, -math.inf, math.inf, True)
                    if self.__grid_service.is_valid_location(grid.map, col):
                        row = self.__grid_service.get_next_open_row(grid.map, col)
                        self.__grid_service.drop_piece(grid.map, row, col, grid.computer_piece)
                        if self.__grid_service.winning_move(grid.map, grid.computer_piece):
                            game_over = True
                        grid.turn = "PLAYER"
                if game_over:
                    pygame.time.wait(3000)
                print(grid)
        elif command == "y":
            pygame.init()
            square_size = 75
            width = 7 * square_size
            height = 7 * square_size
            size = (width, height)
            screen = pygame.display.set_mode(size)
            self.__grid_domain.draw_board(grid.map, screen, square_size, height)
            pygame.display.update()
            while not game_over:
                if grid.turn == "PLAYER":
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        if event.type == pygame.MOUSEMOTION:
                            pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, square_size))
                            pos_of_x = event.pos[0]
                            if grid.turn == "PLAYER":
                                pygame.draw.circle(screen, (255, 0, 0), (pos_of_x, int(square_size / 2)),
                                                   int(square_size / 2 - 5))
                        pygame.display.update()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if grid.turn == "PLAYER":
                                pos_of_x = event.pos[0]
                                col = int(math.floor(pos_of_x / square_size))
                                if self.__grid_service.is_valid_location(grid.map, col):
                                    pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, square_size))
                                    row = self.__grid_service.get_next_open_row(grid.map, col)
                                    self.__grid_service.drop_piece(grid.map, row, col, grid.player_piece)
                                    if self.__grid_service.winning_move(grid.map, grid.player_piece):
                                        pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, square_size))
                                        label = pygame.font.SysFont("monospace", 75).render("YOU WIN!", True,
                                                                                            (255, 0, 0))
                                        screen.blit(label, (40, 10))
                                        game_over = True
                                    grid.turn = "COMPUTER"
                                    self.__grid_domain.draw_board(grid.map, screen, square_size, height)
                elif grid.turn == "COMPUTER" and not game_over:
                    col, minimax_score = self.__grid_service.minimax(grid.map, 5, -math.inf, math.inf, True)
                    if self.__grid_service.is_valid_location(grid.map, col):
                        row = self.__grid_service.get_next_open_row(grid.map, col)
                        self.__grid_service.drop_piece(grid.map, row, col, grid.computer_piece)
                        if self.__grid_service.winning_move(grid.map, grid.computer_piece):
                            pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, square_size))
                            label = pygame.font.SysFont("monospace", 75).render("COMPUTER WIN!", True, (255, 0, 0))
                            screen.blit(label, (40, 10))
                            game_over = True
                        grid.turn = "PLAYER"
                        self.__grid_domain.draw_board(grid.map, screen, square_size, height)
                if game_over:
                    pygame.time.wait(3000)
