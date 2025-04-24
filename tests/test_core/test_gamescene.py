from Core.GameScene import GameScene
import pytest

def test_init() -> None:
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