from board import Board

BOARD_LENGTH = 400
SIZE = 4
WEIGHT = 3

board = Board(BOARD_LENGTH, SIZE, WEIGHT)


def setup():
    size(BOARD_LENGTH, BOARD_LENGTH)
    colorMode(RGB, 1)


def draw():
    # update(mouseX, mouseY)
    background("#006800")
    strokeWeight(WEIGHT)
    board.display()


def mousePressed():
    board.click_handler(mouseX, mouseY)
