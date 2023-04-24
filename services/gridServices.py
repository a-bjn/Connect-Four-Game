import math
import random
import copy


class GridService:

    def __init__(self, grid_repo):
        self.__grid_repo = grid_repo
        self.ROW_COUNT = 6
        self.COLUMN_COUNT = 7

    # placing pieces
    def get_next_open_row(self, grid, col):
        for r in range(self.ROW_COUNT):
            if grid[r][col].occupied == "":
                return r

    @staticmethod
    def drop_piece(grid, row, col, piece):
        grid[row][col].occupied = piece

    def is_valid_location(self, grid, col):
        return grid[self.ROW_COUNT - 1][col].occupied == ""

    # placing pieces

    def get_valid_locations(self, grid):
        valid_locations = []
        for col in range(self.COLUMN_COUNT):
            if self.is_valid_location(grid, col):
                valid_locations.append(col)

        return valid_locations

    def pick_best_move(self, grid, piece):
        valid_locations = self.get_valid_locations(grid)
        best_score = -10000
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = self.get_next_open_row(grid, col)
            temp_grid = copy.deepcopy(grid)
            self.drop_piece(temp_grid, row, col, piece)
            score = self.score_position(temp_grid, piece)
            if score > best_score:
                best_score = score
                best_col = col

        return best_col

    def is_terminal_node(self, grid):
        return self.winning_move(grid, "#") or self.winning_move(grid, "*") or len(self.get_valid_locations(grid)) == 0

    @staticmethod
    def evaluate_window(window, piece):
        score = 0
        opp_piece = "#"
        if piece == "#":
            opp_piece = "*"

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count("") == 1:
            score += 5
        elif window.count(piece) == 2 and window.count("") == 2:
            score += 2
        if window.count(opp_piece) == 3 and window.count("") == 1:
            score -= 4

        return score

    def score_position(self, grid, piece):
        score = 0

        # Score center
        center_array = list()
        for r in range(self.ROW_COUNT):
            center_array.append(grid[r][3].occupied)
            center_count = center_array.count(piece)
            score += center_count * 4

        # Score horizontal
        for r in range(self.ROW_COUNT):
            row_array = [i.occupied for i in list(grid[r][:])]
            for c in range(self.COLUMN_COUNT - 3):
                window = row_array[c:c + 4]
                score += self.evaluate_window(window, piece)

        # Score vertical
        for c in range(self.COLUMN_COUNT):
            col_array = []
            for row in range(self.ROW_COUNT):
                col_array.append(grid[row][c].occupied)
            for r in range(self.ROW_COUNT - 3):
                window = col_array[r:r + 4]
                score += self.evaluate_window(window, piece)

        # Score positive diagonal
        for r in range(self.ROW_COUNT - 3):
            for c in range(self.COLUMN_COUNT - 3):
                window = [grid[r+i][c+i].occupied for i in range(4)]
                score += self.evaluate_window(window, piece)

        # Score negative diagonal
        for r in range(self.ROW_COUNT - 3):
            for c in range(self.COLUMN_COUNT - 3):
                window = [grid[r+3-i][c+i].occupied for i in range(4)]
                score += self.evaluate_window(window, piece)

        return score

    def winning_move(self, grid, piece):
        # Check horizontal
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(self.ROW_COUNT):
                if grid[r][c].occupied == piece and grid[r][c + 1].occupied == piece and \
                        grid[r][c + 2].occupied == piece and grid[r][c + 3].occupied == piece:
                    return True

        # Check vertical
        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT - 3):
                if grid[r][c].occupied == piece and grid[r + 1][c].occupied == piece and \
                        grid[r + 2][c].occupied == piece and grid[r + 3][c].occupied == piece:
                    return True

        # Check positively slope
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(self.ROW_COUNT - 3):
                if grid[r][c].occupied == piece and grid[r + 1][c + 1].occupied == piece and \
                        grid[r + 2][c + 2].occupied == piece and grid[r + 3][c + 3].occupied == piece:
                    return True

        # Check negatively sloped
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(3, self.ROW_COUNT):
                if grid[r][c].occupied == piece and grid[r - 1][c + 1].occupied == piece and \
                        grid[r - 2][c + 2].occupied == piece and grid[r - 3][c + 3].occupied == piece:
                    return True

    def minimax(self, grid, depth, alpha, beta, maximizing_player):
        valid_locations = self.get_valid_locations(grid)
        is_terminal = self.is_terminal_node(grid)
        if depth == 0 or is_terminal:
            if is_terminal:
                if self.winning_move(grid, "*"):
                    return None, 1000000000000
                elif self.winning_move(grid, "#"):
                    return None, -1000000000000
                else:  # game over
                    return None, 0
            else:
                return None, self.score_position(grid, "*")
        if maximizing_player:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.get_next_open_row(grid, col)
                grid_copy = copy.deepcopy(grid)
                self.drop_piece(grid_copy, row, col, "*")
                new_score = self.minimax(grid_copy, depth-1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value
        else:
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.get_next_open_row(grid, col)
                grid_copy = copy.deepcopy(grid)
                self.drop_piece(grid_copy, row, col, "#")
                new_score = self.minimax(grid_copy, depth-1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

    def get_grid(self):
        return self.__grid_repo.grid()

    @staticmethod
    def coin_flip_turn():
        words = ["PLAYER", "COMPUTER"]
        pick = random.choice(words)
        return pick
