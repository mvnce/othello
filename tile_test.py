from tile import Tile
from constants import COLOR_BLACK, COLOR_WHITE


def test_constructor():
    tile = Tile(100, 100, 800, 800, 3)
    assert tile.x == 100
    assert tile.y == 100
    assert tile.width == 800
    assert tile.height == 800
    assert tile.offset == 3
    assert tile.color is None


def test_set_color():
    tile = Tile(100, 100, 800, 800, 3)
    tile.set_color(COLOR_BLACK)
    assert tile.color == COLOR_BLACK
    tile.set_color(COLOR_WHITE)
    assert tile.color == COLOR_WHITE


def test_reset_color():
    tile = Tile(100, 100, 800, 800, 3)
    tile.reset_color()
    assert tile.color is None


def test_has_color():
    tile = Tile(100, 100, 800, 800, 3)
    assert tile.has_color() is False
    tile.set_color(COLOR_BLACK)
    assert tile.has_color() is True


def test_get_color():
    tile = Tile(100, 100, 800, 800, 3)
    assert tile.get_color() is None
    tile.set_color(COLOR_BLACK)
    assert tile.get_color() == COLOR_BLACK


def test_set_number():
    tile = Tile(100, 100, 800, 800, 3)
    assert tile.number == 0
    tile.set_number(8)
    assert tile.number == 8


def test_clear_number():
    tile = Tile(100, 100, 800, 800, 3)
    tile.set_number(8)
    assert tile.number == 8
    tile.clear_number()
    assert tile.number == 0
