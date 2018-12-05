from controller import Controller

BOARD_LENGTH = 550
BOARD_HEIGHT = 610
GAME_SIZE = 8
OFFSET = 3

controller = Controller(BOARD_LENGTH, GAME_SIZE, OFFSET)


def setup():
    while True:
        name = input('enter your name')
        if name:
            controller.set_player_name(name)
            break

    size(BOARD_LENGTH, BOARD_HEIGHT)
    colorMode(RGB, 1)


def draw():
    background("#006800")
    stroke(0, 0, 0)
    strokeWeight(OFFSET)
    controller.display()


def mousePressed():
    controller.mouse_event_handler(mouseX, mouseY)


def input(self, message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
