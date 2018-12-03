from tiles import Tiles
from othello_utils import COLOR_WHITE, COLOR_BLACK, draw_line, draw_rect, draw_text


class Board:
    def __init__(self, length, size, offset):
        self.length = length
        self.size = size
        self.offset = offset

        # calculate each tile length
        available_length = self.length - (self.offset * (self.size - 1))
        self.block_length = available_length // self.size

        self.tiles = Tiles(self.length, self.size, self.offset)
        self.turn = COLOR_BLACK
        self.all_tiles = self.size * self.size
        self.tile_counter = 4

    def click_handler(self, mouse_x, mouse_y):
        is_success = self.tiles.click_handler(mouse_x, mouse_y, self.turn)

        if is_success:
            self.tiles.make_computer_move(COLOR_WHITE)
            self.tile_counter += 2

    def display(self):
        self.draw_board()
        self.tiles.display()
        self.update()

    def update(self):
        # when board is full
        if self.tile_counter == self.all_tiles:
            b_count, w_count = self.tiles.get_counts()

            summary_text = "Black {0} - {1} White".format(b_count, w_count)
            result_text = 'Black Win!' if b_count > w_count else 'White Win!' if b_count < w_count else 'Tie Game'

            self.draw_text(result_text, summary_text)

    def draw_board(self):
        # draw horizontal lines
        for i in range(1, self.size):
            x1, y1 = 0, i * self.block_length + i * self.offset
            x2, y2 = self.length, y1
            draw_line(x1, y1, x2, y2)

        # draw vertical lines
        for i in range(1, self.size):
            x1, y1 = i * self.block_length + i * self.offset, 0
            x2, y2 = x1, self.length
            draw_line(x1, y1, x2, y2)

    def draw_text(self, result, summary):
        draw_rect(0, 0, 0, 0.75, 0, 0, self.length, self.length)
        draw_text(255, 255, 255, 30, self.length / 2, self.length / 5 * 2, result)
        draw_text(255, 255, 255, 30, self.length / 2, self.length / 5 * 3, summary)
