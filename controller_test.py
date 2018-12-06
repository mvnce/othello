from controller import Controller


def test_constructor():
    controller = Controller(800, 8, 0, "dog")

    assert controller.length == 800
    assert controller.size == 8
    assert controller.offset == 0
    assert controller.side == 100
    assert controller.turn_index == 0
    assert len(controller.players) == 2

    assert controller.board is not None

    assert controller.tile_cnt == 4
    assert controller.tile_max == 64

    assert controller.is_saved is False


def test_set_player_name():
    controller = Controller(800, 8, 0, "dog")
    assert controller.players[0].name == "dog"

    controller.set_player_name("cat")
    assert controller.players[0].name == "cat"


def test_convert_coordinate_to_position():
    controller = Controller(800, 8, 0, "dog")
    row, col = controller.convert_coordinate_to_position(350, 450)
    assert (row, col) == (4, 3)
