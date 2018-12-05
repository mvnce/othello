from constants import COLOR_BLACK, COLOR_WHITE, COLOR_HIGHLIGHT
from tile import Tile


class Tiles:
    def __init__(self, length, size, side, offset):
        self.length = length
        self.size = size
        self.side = side
        self.offset = offset

        self.tiles = list()
        self.highlighted_coords = list()
        self.tile_flip_lookup = dict()

        # ellipse width and height
        ellipse_len = self.side - self.offset
        center_offset = self.side // 2

        # initialize all tiles
        for i in range(self.size):
            initial_y = (i * self.side) + (i + 1) * self.offset
            temp_row = []
            for j in range(self.size):
                x_position = ((j + 1) * self.offset) + (j * self.side) + center_offset - self.offset // 2
                y_position = initial_y + center_offset - self.offset // 2

                ellipse_width = ellipse_height = ellipse_len - self.offset * 2
                temp_row.append(Tile(x_position, y_position, ellipse_width, ellipse_height, self.offset))

            self.tiles.append(temp_row)

        # set initial four tiles
        a, b = self.size // 2, self.size // 2 - 1
        self.tiles[b][b].set_color(COLOR_WHITE)
        self.tiles[a][a].set_color(COLOR_WHITE)
        self.tiles[b][a].set_color(COLOR_BLACK)
        self.tiles[a][b].set_color(COLOR_BLACK)

    def display(self):
        for row in self.tiles:
            for tile in row:
                tile.display()

    # return true for handling click correctly
    # return false when tile already has a tile
    def play(self, row, col, color):
        # prevent override existing tile
        if self.tiles[row][col].has_color():
            return False

        # prevent illegal tile move
        if not (row, col) in self.tile_flip_lookup:
            return False

        self.put_tile(row, col, color)
        return True

    def computer_play(self, color):
        print('computer play: ', color)
        print('computer play: ', self.highlighted_coords)
        print('computer play: ', self.tile_flip_lookup)
        best_coord, best_cnt = self.highlighted_coords[0], 0
        for coord in self.highlighted_coords:
            if len(self.tile_flip_lookup[coord]) > best_cnt:
                best_coord, best_cnt = coord, len(self.tile_flip_lookup[coord])
        self.put_tile(best_coord[0], best_coord[1], color)

    def put_tile(self, row, col, color):
        self.tiles[row][col].set_color(color)
        flippables = self.tile_flip_lookup[(row, col)]
        self.flip_tiles(flippables, color)
        self.debug_print()

    def evaluate_valid_moves(self, color, highlight=False):
        for (row, col) in self.highlighted_coords:
            if self.tiles[row][col].get_color() == COLOR_HIGHLIGHT:
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
            del self.highlighted_coords[:]
            for (row, col) in coordinates_lookup.keys():
                # adding new highlighted coords
                self.highlighted_coords.append((row, col))
                self.tiles[row][col].set_color(COLOR_HIGHLIGHT)
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
        coordinates = list()
        coordinates += self.calculate_flips(row, column, 0, -1, 0, self.size - 1, color, self.tiles)  # left
        coordinates += self.calculate_flips(row, column, 0, 1, 0, self.size - 1, color, self.tiles)  # right
        coordinates += self.calculate_flips(row, column, -1, 0, 0, self.size - 1, color, self.tiles)  # up
        coordinates += self.calculate_flips(row, column, 1, 0, 0, self.size - 1, color, self.tiles)  # down

        coordinates += self.calculate_flips(row, column, -1, -1, 0, self.size - 1, color, self.tiles)  # up-left
        coordinates += self.calculate_flips(row, column, -1, 1, 0, self.size - 1, color, self.tiles)  # up-right
        coordinates += self.calculate_flips(row, column, 1, -1, 0, self.size - 1, color, self.tiles)  # down-left
        coordinates += self.calculate_flips(row, column, 1, 1, 0, self.size - 1, color, self.tiles)  # down-right
        return coordinates

    def calculate_flips(self, row, col, row_shf, col_shf, min_limit, max_limit, color, tiles):
        coordinates = []  # for storing flippable (row, col) pairs
        is_valid = False  # must find same color tile, then all found tiles are valid to be captured

        row, col = row + row_shf, col + col_shf  # it should NOT count itself

        while (row >= min_limit and row <= max_limit) and (col >= min_limit and col <= max_limit):
            tile_color = tiles[row][col].get_color()

            if tile_color is None or tile_color == COLOR_HIGHLIGHT:
                del coordinates[:]
                break
            elif tile_color == color:
                is_valid = True
                break
            elif tile_color != color:
                coordinates.append((row, col))

            row, col = row + row_shf, col + col_shf  # increments

        return coordinates if is_valid else []

    def flip_tiles(self, coordinates, new_color):
        for (row, column) in coordinates:
            self.tiles[row][column].set_color(new_color)

    def debug_print(self):
        print('\n++++++++++++++')
        for row in self.tiles:
            print(row)
        print('++++++++++++++\n')
