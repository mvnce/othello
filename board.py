from pieces import Pieces


class Board:
    def __init__(self, length, size, line_weight=2):
        self.length = length
        self.size = size
        self.line_weight = line_weight
        self.pieces = Pieces(self.length, self.size, self.line_weight)

    def display(self):
        # calculation for drawing lines
        stroke(0, 0, 0)
        strokeWeight(self.line_weight)
        available_length = self.length - (self.line_weight * (self.size - 1))
        block_length = available_length // self.size

        # draw horizontal lines
        for i in range(1, self.size):
            x1 = 0
            y1 = i * block_length + i * self.line_weight
            x2 = self.length
            y2 = y1
            line(x1, y1, x2, y2)

        # draw vertical lines
        for i in range(1, self.size):
            x1 = i * block_length + i * self.line_weight
            y1 = 0
            x2 = x1
            y2 = self.length
            line(x1, y1, x2, y2)

        self.pieces.display()
