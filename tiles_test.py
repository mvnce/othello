from tiles import Tiles
from constants import COLOR_BLACK, COLOR_WHITE


def test_constructor():
    tiles = Tiles(800, 8, 100, 0)
    assert tiles.length == 800
    assert tiles.size == 8
    assert tiles.side == 100
    assert tiles.offset == 0

    assert len(tiles.tiles) == 8
    assert tiles.highlighted_coords is not None
    assert tiles.tile_flip_lookup is not None


def test_human_play():
    tiles = Tiles(800, 8, 100, 0)
    # fulfill tile flip lookup dictionary
    tiles.evaluate_valid_moves(COLOR_BLACK)

    # test play on colored tile
    row, col = 4, 3
    assert tiles.human_play(row, col, COLOR_BLACK) is False

    # test illegal move
    row, col = 5, 3
    assert tiles.human_play(row, col, COLOR_BLACK) is False

    row, col = 3, 2
    assert tiles.human_play(row, col, COLOR_BLACK) is True


def test_computer_play():
    tiles = Tiles(800, 8, 100, 0)

    # test if there is no valid move
    assert tiles.computer_play(COLOR_BLACK) is False

    # fulfill tile flip lookup dictionary
    tiles.evaluate_valid_moves(COLOR_BLACK)

    # test valid move
    prev_count = count_tiles(tiles.tiles)
    assert tiles.computer_play(COLOR_BLACK) is True
    curr_count = count_tiles(tiles.tiles)
    assert curr_count == prev_count + 1


def test_put_tile():
    tiles = Tiles(800, 8, 100, 0)

    # fulfill tile flip lookup dictionary
    tiles.evaluate_valid_moves(COLOR_BLACK)

    # use first row, col pair
    row, col = list(tiles.tile_flip_lookup.keys())[0]
    prev_count = count_tiles(tiles.tiles)
    tiles.put_tile(row, col, COLOR_BLACK)
    curr_count = count_tiles(tiles.tiles)
    assert curr_count == prev_count + 1


def test_evaluate_valid_moves():
    tiles = Tiles(800, 8, 100, 0)

    assert len(tiles.tile_flip_lookup) == 0

    # fulfill tile flip lookup dictionary
    tiles.evaluate_valid_moves(COLOR_BLACK)

    assert len(tiles.tile_flip_lookup) == 4


def test_get_counts():
    tiles = Tiles(800, 8, 100, 0)

    assert tiles.get_counts() == (2, 2)

    # fulfill tile flip lookup dictionary
    tiles.evaluate_valid_moves(COLOR_BLACK)

    assert len(tiles.tile_flip_lookup) == 4

    row, col = 3, 2
    assert tiles.human_play(row, col, COLOR_BLACK) is True
    assert tiles.get_counts() == (4, 1)


def test_can_flip_tiles():
    tiles = Tiles(800, 8, 100, 0)

    # [-, -, -, -, -, -, -, -]
    # [-, -, -, -, -, -, -, -]
    # [-, -, -, -, W, -, -, -]
    # [-, -, -, W, W, -, -, -]
    # [-, -, -, W, W, B, -, -]
    # [-, -, -, B, W, W, -, -]
    # [-, -, B, -, -, -, -, -]
    # [-, -, -, -, -, -, -, -]
    tiles.tiles[2][4].set_color(COLOR_WHITE)
    tiles.tiles[3][3].set_color(COLOR_WHITE)
    tiles.tiles[3][4].set_color(COLOR_WHITE)
    tiles.tiles[4][3].set_color(COLOR_WHITE)
    tiles.tiles[4][4].set_color(COLOR_WHITE)
    tiles.tiles[4][5].set_color(COLOR_BLACK)
    tiles.tiles[5][3].set_color(COLOR_BLACK)
    tiles.tiles[5][4].set_color(COLOR_WHITE)
    tiles.tiles[5][5].set_color(COLOR_WHITE)
    tiles.tiles[6][2].set_color(COLOR_BLACK)

    row, col = 0, 0
    coordinates = tiles.can_flip_tiles(row, col, COLOR_BLACK)
    assert len(coordinates) == 0

    row, col = 2, 3
    coordinates = tiles.can_flip_tiles(row, col, COLOR_BLACK)
    assert len(coordinates) == 3


def test_calculate_flips():
    tiles = Tiles(800, 8, 100, 0)

    row, col = 5, 3
    coordinates = tiles.can_flip_tiles(row, col, COLOR_BLACK)
    assert len(coordinates) == 0

    row, col = 3, 2
    coordinates = tiles.can_flip_tiles(row, col, COLOR_BLACK)
    assert len(coordinates) == 1


def test_flip_tiles():
    tiles = Tiles(800, 8, 100, 0)

    coordinates = [(0, 0), (0, 1), (0, 2)]

    prev_count = count_tiles(tiles.tiles)
    tiles.flip_tiles(coordinates, COLOR_BLACK)
    curr_count = count_tiles(tiles.tiles)
    assert curr_count == prev_count + 3


def count_tiles(tile_matrix):
    counter = 0
    for row in tile_matrix:
        for tile in row:
            if tile.has_color():
                counter += 1
    return counter
