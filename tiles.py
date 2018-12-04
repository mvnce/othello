from othello_utils import COLOR_BLACK, COLOR_WHITE, HIGHLIGHT, COLUMN, ROW
from tile import Tile


class Tiles:
    def __init__(self, length, size, offset):
        self.length = length
        self.size = size
        self.offset = offset
        self.tiles = list()
        self.block_length = None
        self.highlighted_coords = list()
        self.tile_flip_lookup = dict()

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
    def move_handler(self, mouse_x, mouse_y, turn):
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
            # prevent override existing tile
            if self.tiles[row][column].has_color():
                return False

            # prevent illegal tile move
            if not (row, column) in self.tile_flip_lookup:
                return False

            self.tiles[row][column].set_color(turn)
            flippables = self.tile_flip_lookup[(row, column)]
            self.flip_tiles_handler(flippables, turn)
            self.debug_print()
            return True

        return False

    def find_possible_moves(self, color, highlight=False):
        for (row, col) in self.highlighted_coords:
            if self.tiles[row][col].get_color() == HIGHLIGHT:
                print("resetting tile", row, col)
                self.tiles[row][col].reset_color()

        print('\n====== EXECUTE FIND POSSIBLE MOVES ======')
        print('current player:', str(color))
        coordinates_lookup = dict()

        for row_index, row_tiles in enumerate(self.tiles):
            for col_index, tile in enumerate(row_tiles):
                # only evaluate move for empty tile
                if self.tiles[row_index][col_index].has_color():
                    continue

                # evaluate flips for current tile
                coords = self.__can_flip_tiles(row_index, col_index, color)

                # no flip move is invalid and should not be counted
                if len(coords) == 0:
                    continue

                # store flippable tiles into a lookup dictionary by using original tile coord as key
                coordinates_lookup[(row_index, col_index)] = coords
                print((row_index, col_index), coords)

        if highlight:
            for (row, col) in coordinates_lookup.keys():
                # adding new highlighted coords
                self.highlighted_coords.append((row, col))
                self.tiles[row][col].set_color(HIGHLIGHT)
                self.tiles[row][col].set_number(len(coordinates_lookup[(row, col)]))

        self.tile_flip_lookup = coordinates_lookup

        # TODO: NEED TO REMOVE THIS DEBUGGING CODE BLOCK
        self.debug_print()
        for (row, col) in coordinates_lookup.keys():
            print((row, col))
        print('========================================\n')
        # TODO: END DEBUGGING CODE BLOCK

        return len(coordinates_lookup) > 0

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

    def __can_flip_tiles(self, row, column, color):
        # TODO: need to remove this block, keep it for debugging only
        # l_flippables = self.__loop_handler(column - 1, -1, -1, row, COLUMN, color)
        # r_flippables = self.__loop_handler(column + 1, self.size, 1, row, COLUMN, color)
        # u_flippables = self.__loop_handler(row - 1, -1, -1, column, ROW, color)
        # d_flippables = self.__loop_handler(row + 1, self.size, 1, column, ROW, color)

        all_coords = []
        all_coords += self.loop_handler(column - 1, -1, -1, row, COLUMN, color)
        all_coords += self.loop_handler(column + 1, self.size, 1, row, COLUMN, color)
        all_coords += self.loop_handler(row - 1, -1, -1, column, ROW, color)
        all_coords += self.loop_handler(row + 1, self.size, 1, column, ROW, color)

        # flip_total = len(l_flippables) + len(r_flippables) + len(u_flippables) + len(d_flippables)
        print("rowIndex and colIndex", row, column, 'TOTAL:', len(all_coords))
        # print("L:", len(l_flippables), "R:", len(r_flippables), "U:", len(u_flippables), "D:", len(d_flippables))

        # return {'L': l_flippables, 'R': r_flippables, 'U': u_flippables, 'D': d_flippables}, flip_total
        return all_coords

    def loop_handler(self, start, end, iter_order, fixed_index, row_or_column, color):
        coords, flag = list(), False
        if row_or_column == 'COLUMN':
            for iterator in range(start, end, iter_order):
                if self.tiles[fixed_index][iterator].get_color() is None:
                    del coords[:]
                    break
                elif self.tiles[fixed_index][iterator].get_color() == color:
                    flag = True
                    break
                elif self.tiles[fixed_index][iterator].get_color() != color:
                    coords.append((fixed_index, iterator))
            if flag is False:
                del coords[:]

        elif row_or_column == 'ROW':
            for iterator in range(start, end, iter_order):
                if self.tiles[iterator][fixed_index].get_color() is None:
                    del coords[:]
                    break
                elif self.tiles[iterator][fixed_index].get_color() == color:
                    flag = True
                    break
                elif self.tiles[iterator][fixed_index].get_color() != color:
                    coords.append((iterator, fixed_index))
            if flag is False:
                del coords[:]
        return coords

    def flip_tiles_handler(self, coordinates, new_color):
        for (row, column) in coordinates:
            self.tiles[row][column].set_color(new_color)

    def debug_print(self):
        print('\n++++++++++++++')
        for row in self.tiles:
            print(row)
        print('++++++++++++++\n')
