import arcade

from gameview import GameView

INITIAL_COIN_COUNT = 2

def test_collect(window: arcade.Window) -> None:
    view = GameView()
    window.show_view(view)

    # Make sure we have the amount of coins we expect at the start
    assert len(view.collectables) == INITIAL_COIN_COUNT

    # Start moving right
    view.on_key_press(arcade.key.D, 0)

    # Let the game run for 1 second
    window.test(60)

    # We should have collected the first coin
    assert len(view.collectables) == INITIAL_COIN_COUNT - 1