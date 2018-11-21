from piece import Piece


class Pieces:
    def __init__(self, length, size, line_weight):
        self.length = length
        self.size = size
        self.line_weight = line_weight

        # initialize all pieces
        self.pieces = []

        available_length = self.length - (self.line_weight * (self.size - 1))
        block_length = available_length // self.size
        # ellipse width and height
        ellipse_length = block_length
        center_offset = block_length // 2

        for i in range(size):
            initial_y = (i * block_length) + (i + 1) * line_weight
            row = []
            for j in range(size):
                # TODO: need to handle x, y and r calculation
                x_position = ((j + 1) * self.line_weight) + (j * block_length) + center_offset - 1
                y_position = initial_y + center_offset
                print(x_position, y_position)
                row.append(Piece(x_position, y_position, ellipse_length))
            self.pieces.append(row)

    def display(self):
        for row in self.pieces:
            for piece in row:
                piece.display()
