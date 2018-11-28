from othello_utils import COLOR_BLACK, COLOR_WHITE
from tile import Tile


class Tiles:
    def __init__(self, length, size, offset):
        self.length = length
        self.size = size
        self.offset = offset
        self.tile_matrix = []

        available_length = self.length - (self.offset * (self.size - 1))
        block_length = available_length // self.size
        # ellipse width and height
        ellipse_length = block_length - self.offset
        center_offset = block_length // 2

        self.block_length = block_length

        # initialize all tiles
        for i in range(size):
            initial_y = (i * block_length) + (i + 1) * offset
            row = []
            for j in range(size):
                x_position = ((j + 1) * self.offset) + (j * block_length) + center_offset - self.offset // 2
                y_position = initial_y + center_offset - self.offset // 2

                ellipse_width = ellipse_height = ellipse_length - offset * 2
                row.append(Tile(x_position, y_position, ellipse_width, ellipse_height))

            self.tile_matrix.append(row)

        # set initial four tiles
        self.tile_matrix[size // 2 - 1][size // 2 - 1].set_color(COLOR_WHITE)
        self.tile_matrix[size // 2][size // 2].set_color(COLOR_WHITE)
        self.tile_matrix[size // 2 - 1][size // 2].set_color(COLOR_BLACK)
        self.tile_matrix[size // 2][size // 2 - 1].set_color(COLOR_BLACK)

    def display(self):
        for row in self.tile_matrix:
            for tile in row:
                tile.display()

    # return true for handling click correctly
    # return false when tile already has a tile
    def click_handler(self, mouse_x, mouse_y, turn):
        row, column = None, None

        # decide which tile need to be updated
        # handle row and column separately
        for i in range(self.size):
            max_y_length = (i + 1) * self.offset + (i + 1) * self.block_length
            if mouse_y < max_y_length:
                row = i
                break

        for i in range(self.size):
            max_x_length = (i + 1) * self.offset + (i + 1) * self.block_length
            if mouse_x < max_x_length:
                column = i
                break

        if row is not None and column is not None:
            if self.tile_matrix[row][column].has_color():
                return False

            self.tile_matrix[row][column].set_color(turn)
            return True
        else:
            return False

    def make_computer_move(self, turn):
        print('computer move')
        for row in self.tile_matrix:
            for item in row:
                if not item.has_color():
                    item.set_color(turn)
                    return True
        return False

    def get_counts(self):
        b_count, w_count = 0, 0

        for row in self.tile_matrix:
            for item in row:
                if item.get_color() == COLOR_BLACK:
                    b_count += 1
                elif item.get_color() == COLOR_WHITE:
                    w_count += 1

        return b_count, w_count
