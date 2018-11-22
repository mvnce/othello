from tiles import Tiles


class Board:
    def __init__(self, length, size, offset):
        self.length = length
        self.size = size
        self.offset = offset

        # calculate each tile length
        available_length = self.length - (self.offset * (self.size - 1))
        self.block_length = available_length // self.size

        self.tiles = Tiles(self.length, self.size, self.offset)
        self.turn = "BLACK"
        self.total_tiles = int(pow(self.size, 2))
        self.tile_counter = 4

    def click_handler(self, mouse_x, mouse_y):
        is_success = self.tiles.click_handler(mouse_x, mouse_y, self.turn)

        if is_success:
            self.tile_counter += 1
            if self.turn == "BLACK":
                self.turn = "WHITE"
            else:
                self.turn = "BLACK"

    def display(self):
        # draw lines
        self.draw_board_lines()
        # draw tiles
        self.tiles.display()
        # handle game result display on top of everything
        self.update()

    def update(self):
        # when board is full
        if self.tile_counter == self.total_tiles:
            count_black, count_white = self.tiles.getCounts()
            summary_text = "Black {0} - {1} White".format(
                count_black, count_white)

            result_text = ""
            if count_black > count_white:
                result_text = "Black Win!"
            elif count_black < count_white:
                result_text = "White Win!"
            else:
                result_text = "Tie!"

            self.draw_text(result_text, summary_text)

    def draw_board_lines(self):
        stroke(0, 0, 0)
        # draw horizontal lines
        for i in range(1, self.size):
            x1, y1 = 0, i * self.block_length + i * self.offset
            x2, y2 = self.length, y1
            line(x1, y1, x2, y2)

        # draw vertical lines
        for i in range(1, self.size):
            x1, y1 = i * self.block_length + i * self.offset, 0
            x2, y2 = x1, self.length
            line(x1, y1, x2, y2)

    def draw_text(self, result, summary):
        # draw transparent background
        fill(0, 0, 0, 0.75)
        rectMode(CORNER)
        rect(0, 0, self.length, self.length)

        # draw text
        fill(255, 255, 255)
        textSize(30)
        textAlign(CENTER, CENTER)
        text(result, self.length/2, self.length/5 * 2)
        text(summary, self.length/2, self.length/5 * 3)
