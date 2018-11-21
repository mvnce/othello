from board import Board

WIDTH = 600
HEIGHT = 600

SIZE = 4

board = Board(WIDTH, HEIGHT, SIZE)


def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)


def draw():
    background('#006800')
    board.display()
