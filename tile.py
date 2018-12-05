from processing_utils import draw_ellipse, draw_text
from constants import COLOR_BLACK, COLOR_WHITE, COLOR_HIGHLIGHT


class Tile:
    def __init__(self, x, y, width, height, color=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.number = 0

    def display(self):
        if self.color == COLOR_WHITE:
            draw_ellipse((255, 255, 255), 1, self.x, self.y, self.width, self.height)
        elif self.color == COLOR_BLACK:
            draw_ellipse((0, 0, 0), 1, self.x, self.y, self.width, self.height)
        elif self.color == COLOR_HIGHLIGHT:
            draw_ellipse((0, 0, 0), 0.3, self.x, self.y, self.width, self.height)
            draw_text((0, 0, 0), 25, self.x, self.y, str(self.number))

    def set_color(self, color):
        self.color = color

    def reset_color(self):
        self.color = None

    def has_color(self):
        return self.color in [COLOR_BLACK, COLOR_WHITE]

    def get_color(self):
        return self.color

    def set_number(self, number):
        self.number = number

    def clear_number(self):
        self.number = 0

    def __repr__(self):
        if self.color == COLOR_BLACK:
            return 'B'

        if self.color == COLOR_WHITE:
            return 'W'

        if self.color == COLOR_HIGHLIGHT:
            return str(self.number)

        return '-'
