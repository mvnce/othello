from othello_utils import COLOR_BLACK, COLOR_WHITE, draw_ellipse


class Tile:
    def __init__(self, x, y, width, height, color=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def display(self):
        if self.color == COLOR_WHITE:
            draw_ellipse((255, 255, 255), self.x, self.y, self.width, self.height)
        elif self.color == COLOR_BLACK:
            draw_ellipse((0, 0, 0), self.x, self.y, self.width, self.height)

    def set_color(self, color):
        self.color = color

    def has_color(self):
        return self.color is not None

    def get_color(self):
        return self.color
