from board import Board

BOARD_LENGTH = 600

SIZE = 4

board = Board(BOARD_LENGTH, SIZE)


def setup():
    size(BOARD_LENGTH, BOARD_LENGTH)
    colorMode(RGB, 1)


def draw():
    background('#006800')
    board.display()
