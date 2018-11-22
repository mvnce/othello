from piece import Piece


class Pieces:
    def __init__(self, length, size, offset):
        self.length = length
        self.size = size
        self.offset = offset
        self.pieces = []

        available_length = self.length - (self.offset * (self.size - 1))
        block_length = available_length // self.size
        # ellipse width and height
        ellipse_length = block_length - self.offset
        center_offset = block_length // 2

        self.block_length = block_length

        # initialize all pieces
        for i in range(size):
            initial_y = (i * block_length) + (i + 1) * offset
            row = []
            for j in range(size):
                x_position = ((j + 1) * self.offset) + \
                    (j * block_length) + center_offset - self.offset // 2
                y_position = initial_y + center_offset - self.offset // 2

                row.append(Piece(x_position, y_position,
                                 ellipse_length - offset * 2))

            self.pieces.append(row)

        # set initial four pieces
        self.pieces[size // 2 - 1][size // 2 - 1].setOwner('WHITE')
        self.pieces[size // 2][size // 2].setOwner('WHITE')
        self.pieces[size // 2 - 1][size // 2].setOwner('BLACK')
        self.pieces[size // 2][size // 2 - 1].setOwner('BLACK')

    def display(self):
        for row in self.pieces:
            for piece in row:
                piece.display()

    # return true for handling click correctly
    # return false when tile already has a piece
    def click_handler(self, mouse_x, mouse_y, turn):
        row, col = None, None

        # decide which piece need to be updated
        # handle row and column seperately
        for i in range(self.size):
            max_x_length = (i + 1) * self.offset + \
                (i + 1) * self.block_length
            if mouse_x < max_x_length:
                col = i
                break

        for i in range(self.size):
            max_y_length = (i + 1) * self.offset + \
                (i + 1) * self.block_length
            if mouse_y < max_y_length:
                row = i
                break

        if row != None and col != None:
            if self.pieces[row][col].hasOwner():
                return False

            if turn:
                self.pieces[row][col].setOwner('BLACK')
                return True
            else:
                self.pieces[row][col].setOwner('WHITE')
                return True

        return False

    def getCounts(self):
        black = 0
        white = 0

        for row in self.pieces:
            for item in row:
                if item.getOwner() == 'BLACK':
                    black += 1
                elif item.getOwner() == 'WHITE':
                    white += 1
                else:
                    raise AttributeError("Piece has unexpected value")

        return black, white
