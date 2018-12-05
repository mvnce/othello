from tiles import Tiles
from draw_utils import draw_line, draw_rect, draw_text


class Board:
    def __init__(self, length, size, side, offset):
        self.length = length
        self.side = side
        self.size = size  # side length for each cube
        self.offset = offset

        self.tiles = Tiles(self.length, self.size, self.side, self.offset)

        # tracking valid moves for current player
        self.valid_moves = []

    def display(self):
        self.draw_board()
        self.tiles.display()

    def play(self, row, col, color):
        return self.tiles.play(row, col, color)

    def computer_play(self, color):
        return self.tiles.computer_play(color)

    def evaluate_board_moves(self, color, highlight=False):
        return self.tiles.evaluate_valid_moves(color, highlight)

    def draw_board(self):
        # draw horizontal lines
        for i in range(1, self.size + 1):
            x1, y1 = 0, i * self.side + i * self.offset
            x2, y2 = self.length, y1
            draw_line(x1, y1, x2, y2)

        # draw vertical lines
        for i in range(1, self.size):
            x1, y1 = i * self.side + i * self.offset, 0
            x2, y2 = x1, self.length
            draw_line(x1, y1, x2, y2)

    def end_game(self):
        b_count, w_count = self.tiles.get_counts()
        text = 'Black Win!' if b_count > w_count else 'White Win!' if b_count < w_count else 'Tie Game'

        draw_rect((0, 0, 0), 0.75, 0, 0, self.length, self.length)
        draw_text((255, 255, 255), 30, self.length / 2, self.length / 2, text)

    def get_counts(self):
        return self.tiles.get_counts()
