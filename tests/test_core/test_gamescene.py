from Core.GameScene import GameScene
from GameObjects.Interactable import Door, Coin
import pytest

def test_init_load() -> None:
    scene = GameScene("tests/test_core/maps/coin.txt")
    assert len(scene.ladders) == 0
    assert len(scene.walls) == 10
    assert len(scene.interactables) == 2

    with pytest.raises(Exception):
        scene2 = GameScene("invalid_path")

def test_reset() -> None:
    scene = GameScene("tests/test_core/maps/coin.txt")
    scene.reset()
    assert len(scene.walls) == 0

def test_change() -> None:
    # un seul interactable c'est la porte
    scene = GameScene("tests/test_core/maps/change_map.txt")
    assert len(scene.interactables) == 1
    assert isinstance(scene.interactables[0], Door)
    assert scene.current_path == "tests/test_core/maps/change_map.txt"

    # deux interactable pieces
    scene.next_map()
    assert len(scene.interactables) == 2
    assert isinstance(scene.interactables[0], Coin)
    assert scene.current_path == "tests/test_core/maps/coin.txt"