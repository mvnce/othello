from tile import Tile


class Tiles:
    def __init__(self, length, size, offset):
        self.length = length
        self.size = size
        self.offset = offset
        self.tiles = []

        available_length = self.length - (self.offset * (self.size - 1))
        block_length = available_length // self.size
        # ellipse width and height
        ellipse_length = block_length - self.offset
        center_offset = block_length // 2

        self.block_length = block_length

        # initialize all tiles
        for i in range(size):
            initial_y = (i * block_length) + (i + 1) * offset
            row = []
            for j in range(size):
                x_position = ((j + 1) * self.offset) + \
                    (j * block_length) + center_offset - self.offset // 2
                y_position = initial_y + center_offset - self.offset // 2

                row.append(Tile(x_position, y_position,
                                ellipse_length - offset * 2))

            self.tiles.append(row)

        # set initial four tiles
        self.tiles[size // 2 - 1][size // 2 - 1].setOwner('WHITE')
        self.tiles[size // 2][size // 2].setOwner('WHITE')
        self.tiles[size // 2 - 1][size // 2].setOwner('BLACK')
        self.tiles[size // 2][size // 2 - 1].setOwner('BLACK')

    def display(self):
        for row in self.tiles:
            for tile in row:
                tile.display()

    # return true for handling click correctly
    # return false when tile already has a tile
    def click_handler(self, mouse_x, mouse_y, turn):
        row, col = None, None

        # decide which tile need to be updated
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

        if row != None or col != None:
            if self.tiles[row][col].hasOwner():
                return False

            self.tiles[row][col].setOwner(turn)
            return True

        return False

    def get_counts(self):
        black = 0
        white = 0

        for row in self.tiles:
            for item in row:
                if item.getOwner() == 'BLACK':
                    black += 1
                elif item.getOwner() == 'WHITE':
                    white += 1

        return black, white
