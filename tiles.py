from othello_utils import COLOR_BLACK, COLOR_WHITE
from tile import Tile
import datetime


class Tiles:
    def __init__(self, length, size, offset):
        self.length = length
        self.size = size
        self.offset = offset
        self.tiles = list()
        self.block_length = None
        self.valid_move_coordinates = set()

    def initialize(self):
        len_without_offset = self.length - (self.offset * (self.size - 1))
        block_len = len_without_offset // self.size
        # ellipse width and height
        ellipse_len = block_len - self.offset
        center_offset = block_len // 2

        self.block_length = block_len

        # initialize all tiles
        for i in range(self.size):
            initial_y = (i * block_len) + (i + 1) * self.offset
            temp_row = []
            for j in range(self.size):
                x_position = ((j + 1) * self.offset) + (j * block_len) + center_offset - self.offset // 2
                y_position = initial_y + center_offset - self.offset // 2

                ellipse_width = ellipse_height = ellipse_len - self.offset * 2
                temp_row.append(Tile(x_position, y_position, ellipse_width, ellipse_height))

            self.tiles.append(temp_row)

        # set initial four tiles
        a, b = self.size // 2, self.size // 2 - 1
        self.tiles[b][b].set_color(COLOR_WHITE)
        self.tiles[a][a].set_color(COLOR_WHITE)
        self.tiles[b][a].set_color(COLOR_BLACK)
        self.tiles[a][b].set_color(COLOR_BLACK)

        # self.find_possible_moves(COLOR_BLACK)
        self.debug_print()

    def display(self):
        for row in self.tiles:
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
            if self.tiles[row][column].has_color():
                return False

            self.tiles[row][column].set_color(turn)
            self.debug_print()
            return True
        else:
            return False

    def find_possible_moves(self, color):
        print('\n====== EXECUTE FIND POSSIBLE MOVES ======')
        print(str(color))
        available_move_dictionary = {}

        for row_index, row_tiles in enumerate(self.tiles):
            for col_index, tile in enumerate(row_tiles):
                if self.tiles[row_index][col_index].has_color():
                    continue
                flip_counts, flip_total = self.__can_flip_tiles(row_index, col_index, color)
                if flip_total == 0:
                    continue
                available_move_dictionary[(row_index, col_index)] = flip_counts

        # # reset color attribute to None
        # for (row, col) in self.valid_move_coordinates:
        #     self.tiles[row][col].reset_color()
        #     print('remove color for tile', row, col)
        #
        # # clear previous valid move coordinates
        # del self.valid_move_coordinates[:]
        #
        # # print(available_move_dictionary)
        # for (row, col) in available_move_dictionary.keys():
        #     if not self.tiles[row][col].has_color():
        #
        #         self.valid_move_coordinates.append((row, col))
        #         self.tiles[row][col].set_color('VALID_OPTION')
        #         print('setting valid option', row, col)
        #     else:
        #         print('The tile has color', row, col)

        # del self.valid_move_coordinates[:]
        self.valid_move_coordinates.clear()

        for (row, col) in available_move_dictionary.keys():
            self.valid_move_coordinates.add((row, col))

        self.debug_print()

        print('\n', datetime.datetime.now())
        print('=====================')
        for (row, col) in available_move_dictionary.keys():
            print((row, col))
        print('=====================\n')

        return available_move_dictionary

    def make_computer_move(self, turn):
        for row in self.tiles:
            for item in row:
                if not item.has_color():
                    item.set_color(turn)
                    return True
        return False

    def get_counts(self):
        b_count, w_count = 0, 0

        for row in self.tiles:
            for item in row:
                if item.get_color() == COLOR_BLACK:
                    b_count += 1
                elif item.get_color() == COLOR_WHITE:
                    w_count += 1

        return b_count, w_count

    def __can_flip_tiles(self, row_index, col_index, color):
        # check left
        l_flip_count = 0
        left_check_flag = False
        for iter_col in range(col_index - 1, -1, -1):
            if self.tiles[row_index][iter_col].get_color() is None:
                l_flip_count = 0
                break
            elif self.tiles[row_index][iter_col].get_color() == color:
                left_check_flag = True
                break
            elif self.tiles[row_index][iter_col].get_color() != color:
                l_flip_count += 1
        if left_check_flag is False:
            l_flip_count = 0

        # check right
        r_flip_count = 0
        r_check_flag = False
        for iter_col in range(col_index + 1, self.size):
            if self.tiles[row_index][iter_col].get_color() is None:
                right_flip_count = 0
                break
            elif self.tiles[row_index][iter_col].get_color() == color:
                r_check_flag = True
                break
            elif self.tiles[row_index][iter_col].get_color() != color:
                r_flip_count += 1
        if r_check_flag is False:
            r_flip_count = 0

        # check up
        u_flip_count = 0
        u_check_flag = False
        for iter_row in range(row_index - 1, -1, -1):
            if self.tiles[iter_row][col_index].get_color() is None:
                u_flip_count = 0
                break
            elif self.tiles[iter_row][col_index].get_color() == color:
                u_check_flag = True
                break
            elif self.tiles[iter_row][col_index].get_color() != color:
                u_flip_count += 1
        if u_check_flag is False:
            u_flip_count = 0

        # check down
        d_flip_count = 0
        d_check_flag = False
        for iter_row in range(row_index + 1, self.size):
            if self.tiles[iter_row][col_index].get_color() is None:
                d_flip_count = 0
                break
            elif self.tiles[iter_row][col_index].get_color() == color:
                d_check_flag = True
                break
            elif self.tiles[iter_row][col_index].get_color() != color:
                d_flip_count += 1
        if d_check_flag is False:
            d_flip_count = 0

        flip_total = l_flip_count + r_flip_count + u_flip_count + d_flip_count

        print("rowIndex and colIndex", row_index, col_index, 'TOTAL', flip_total)
        print("L:", l_flip_count, "R:", r_flip_count, "U:", u_flip_count, "D:", d_flip_count)

        return {'L': l_flip_count, 'R': r_flip_count, 'U': u_flip_count, 'D': d_flip_count}, flip_total

    def debug_print(self):

        print('\n', datetime.datetime.now())
        print('=====================')
        for row in self.tiles:
            print(row)

        print('=====================\n')
