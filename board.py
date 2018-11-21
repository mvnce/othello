class Board:
    def __init__(self, width, height, size, line_weight=2):
        self.width = width
        self.height = height
        self.size = size
        self.line_weight = line_weight

    def display(self):
        # Draw the maze walls
        stroke(0, 104, 0)
        strokeWeight(5)
        fill('#006800')
        # rectMode(CORNER)

        # calculation for drawing lines
        stroke(0, 0, 0)
        strokeWeight(self.line_weight)
        available_height = self.height - (self.line_weight * (self.size - 1))
        each_height = available_height // self.size

        # draw horizontal lines
        for i in range(1, self.size):
            x1 = 0
            y1 = i * each_height + i * self.line_weight
            x2 = self.height
            y2 = y1
            line(x1, y1, x2, y2)

        # draw vertical lines
        for i in range(1, self.size):
            x1 = i * each_height + i * self.line_weight
            y1 = 0
            x2 = x1
            y2 = self.height
            line(x1, y1, x2, y2)
