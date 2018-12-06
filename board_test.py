from board import Board
from constants import COLOR_BLACK


def test_constructor():
    board = Board(800, 8, 100, 0)
    assert board.length == 800
    assert board.size == 8
    assert board.side == 100
    assert board.offset == 0
    assert board.tiles is not None


def test_human_play():
    board = Board(800, 8, 100, 0)
    board.evaluate_board_moves(COLOR_BLACK)

    row, col = 5, 3
    assert board.human_play(row, col, COLOR_BLACK) is False
    row, col = 3, 2
    assert board.human_play(row, col, COLOR_BLACK) is True


def test_computer_play():
    board = Board(800, 8, 100, 0)
    board.evaluate_board_moves(COLOR_BLACK)

    assert board.computer_play(COLOR_BLACK) is True


def test_evaluate_board_moves():
    board = Board(800, 8, 100, 0)
    assert board.evaluate_board_moves(COLOR_BLACK) is True

    board = Board(800, 8, 100, 0)
    board.tiles.tiles[3][3].set_color(COLOR_BLACK)
    board.tiles.tiles[4][4].set_color(COLOR_BLACK)

    assert board.evaluate_board_moves(COLOR_BLACK) is False


def test_get_counts():
    board = Board(800, 8, 100, 0)
    assert board.get_counts() == (2, 2)

    board.evaluate_board_moves(COLOR_BLACK)
    row, col = 3, 2
    board.human_play(row, col, COLOR_BLACK)

    assert board.get_counts() == (4, 1)
