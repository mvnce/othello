from board import Board
from player import Player
from constants import COLOR_BLACK, COLOR_WHITE
from draw_utils import draw_text


class Controller:
    def __init__(self, length, size, offset, player_name="Yogurt"):

        self.length = length
        self.size = size
        self.offset = offset
        self.side = (self.length - (self.offset * (self.size - 1))) // self.size
        self.turn_index = 0
        self.players = [Player(COLOR_BLACK, player_name), Player(COLOR_WHITE, None)]

        self.board = Board(length, size, self.side, offset)
        # evaluate possible moves for player for the first time
        self.board.evaluate_board_moves(COLOR_BLACK, True)

        self.tile_cnt = 4
        self.tile_max = self.size ** 2

        self.is_saved = False

        print("Controller:", self.length)
        print("Controller:", self.size)
        print("Controller:", self.offset)
        print("Controller:", self.side)

    def display(self):
        self.board.display()
        self.draw_score()
        self.draw_turn(self.players[self.turn_index].color)
        self.update()

    def update(self):
        if self.tile_cnt == self.tile_max:
            self.board.end_game()
            if self.is_saved is False:
                self.save_score_to_file()
                self.is_saved = not self.is_saved

    def mouse_event_handler(self, mouse_x, mouse_y):
        row, col = self.convert_coordinate_to_position(mouse_x, mouse_y)

        if row is None or col is None:
            return

        is_success = self.board.play(row, col, self.players[self.turn_index].color)
        print("Controller CLICKED:", row, col, is_success)

        if is_success:
            self.tile_cnt += 1  # increase played tile counter
            self.next_player()

    def convert_coordinate_to_position(self, mouse_x, mouse_y):
        row, col = None, None

        for i in range(self.size):
            max_y_length = (i + 1) * self.offset + (i + 1) * self.side
            if mouse_y < max_y_length:
                row = i
                break

        for j in range(self.size):
            max_x_length = (j + 1) * self.offset + (j + 1) * self.side
            if mouse_x < max_x_length:
                col = j
                break

        return row, col

    def next_player(self):
        print('SET NEXT PLAYER')
        self.turn_index = 0 if self.turn_index == 1 else 1
        print(self.turn_index)
        is_playable = self.board.evaluate_board_moves(self.players[self.turn_index].color, True)
        if is_playable is False:
            self.tile_cnt = self.tile_max

    def draw_score(self):
        b_count, w_count = self.board.get_counts()
        text = "{0} {1} - {2} {3}".format(COLOR_BLACK, b_count, w_count, COLOR_WHITE)
        draw_text((255, 255, 255), 25, self.length / 11 * 3, self.length + 30, text)

    def draw_turn(self, color):
        text = "Turn: {0}".format(color)
        draw_text((255, 255, 255), 25, self.length / 11 * 9, self.length + 30, text)

    def save_score_to_file(self):
        b_count, w_count = self.board.get_counts()
        scores = []

        # try read existing scores
        try:
            existing_file = open("scores.txt", "r")
            lines = [line.strip() for line in existing_file.readlines()]
            for line in lines:
                parts = line.split(" ")
                name = " ".join(parts[0: -1])
                score = int(parts[-1])
                scores.append((name, score))
        except:
            print("file doesn't exist")

        # add new scores
        if len(scores) != 0 and b_count > scores[0][1]:
            scores.insert(0, (self.players[0].name, b_count))
        else:
            scores.append((self.players[0].name, b_count))

        # write to files
        score_file = open("scores.txt", "w")
        for score in scores:
            score_file.write("{0} {1}\n".format(score[0], score[1]))
        score_file.close()
