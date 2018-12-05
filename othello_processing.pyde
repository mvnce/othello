from board import Board

BOARD_LENGTH = 550
BOARD_HEIGHT = 610
SIZE = 8
WEIGHT = 3

board = Board(BOARD_LENGTH, SIZE, WEIGHT)


def setup():
    size(BOARD_LENGTH, BOARD_HEIGHT)
    colorMode(RGB, 1)


def draw():
    # update(mouseX, mouseY)
    background("#006800")
    stroke(0, 0, 0)
    strokeWeight(WEIGHT)
    board.display()


def mousePressed():
    board.click_handler(mouseX, mouseY)
