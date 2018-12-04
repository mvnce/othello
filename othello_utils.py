# constants
COLOR_BLACK = 'B'
COLOR_WHITE = 'W'


#  parameters: color: (0, 0, 0), center_x, center_y, width_x, height)
def draw_ellipse(color, center_x, center_y, width, height):
    fill(color[0], color[1], color[2])
    ellipse(center_x, center_y, width, height)


def draw_line(x1, y1, x2, y2):
    line(x1, y1, x2, y2)


def draw_rect(red, green, blue, alpha, corner_x, corner_y, width, height):
    fill(red, green, blue, alpha)
    rectMode(CORNER)
    rect(corner_x, corner_y, width, height)


def draw_text(red, green, blue, size, x, y, text_content):
    fill(red, green, blue)
    textSize(size)
    textAlign(CENTER, CENTER)
    text(text_content, x, y)
