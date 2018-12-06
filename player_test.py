from player import Player
from constants import COLOR_BLACK


def test_constructor():
    player = Player(COLOR_BLACK, "PIZZA")
    assert player.color == COLOR_BLACK
    assert player.name == "PIZZA"


def test_get_color():
    player = Player(COLOR_BLACK, "FRIES")
    assert player.get_color() == COLOR_BLACK


def test_get_name():
    player = Player(COLOR_BLACK, "COKE")
    assert player.get_name() == "COKE"
