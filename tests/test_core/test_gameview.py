import arcade

from Core.GameView import GameView

INITIAL_COIN_COUNT = 2

def test_collect_coin(window: arcade.Window) -> None:
    view = GameView()
    window.show_view(view)
    
    # charge une carte qui n'a bien que 2 interactables uniquement des pieces
    view.setup("tests/test_core/maps/coin.txt")

    # commence bien avec 2 interactables
    assert len(view.scene.interactables) == INITIAL_COIN_COUNT

    # Start moving right
    view.on_key_press(arcade.key.D, 0)

    # Let the game run for 1 second
    window.test(60)

    # reste une piece
    assert len(view.scene.interactables) == INITIAL_COIN_COUNT - 1