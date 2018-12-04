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
        elif self.color == 'VALID_OPTION':
            draw_ellipse((255, 255, 0), self.x, self.y, self.width, self.height)

    def set_color(self, color):
        self.color = color

    def reset_color(self):
        self.color = None

    def has_color(self):
        return self.color in [COLOR_BLACK, COLOR_WHITE]

    def get_color(self):
        return self.color

    def __repr__(self):
        if self.color == COLOR_BLACK:
            return 'B'

        if self.color == COLOR_WHITE:
            return 'W'

        if self.color == 'VALID_OPTION':
            return 'O'

        return '-'
