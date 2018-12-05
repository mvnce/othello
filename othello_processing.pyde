from controller import Controller

BOARD_LENGTH = 550
BOARD_HEIGHT = 610
GAME_SIZE = 4
OFFSET = 3

controller = Controller(BOARD_LENGTH, GAME_SIZE, OFFSET)

def setup():
    size(BOARD_LENGTH, BOARD_HEIGHT)
    colorMode(RGB, 1)


def draw():
    background("#006800")
    stroke(0, 0, 0)
    strokeWeight(OFFSET)
    controller.display()


def mousePressed():
    controller.mouse_event_handler(mouseX, mouseY)
