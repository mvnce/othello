#  parameters: color: (0, 0, 0), alpha, center_x, center_y, width_x, height)
def draw_ellipse(color, alpha, center_x, center_y, width, height, disable_stroke=False):
    if disable_stroke:
        noStroke()
    else:
        stroke(0, 0, 0)
    fill(color[0], color[1], color[2], alpha)
    ellipse(center_x, center_y, width, height)


def draw_line(x1, y1, x2, y2):
    line(x1, y1, x2, y2)


def draw_rect(color, alpha, corner_x, corner_y, width, height):
    fill(color[0], color[1], color[2], alpha)
    rectMode(CORNER)
    rect(corner_x, corner_y, width, height)


def draw_text(color, size, x, y, text_content):
    fill(color[0], color[1], color[2])
    textSize(size)
    textAlign(CENTER, CENTER)
    text(text_content, x, y)

# def input_handler(self, message=''):
#     from javax.swing import JOptionPane
#     return JOptionPane.showInputDialog(frame, message)
