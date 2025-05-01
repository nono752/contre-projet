from TileSystem.Tile import *

## peut-etre se complexifie plus tard sinon enlever
def test_init() -> None:
    tile = Tile(
        path_or_texture=None, 
        center_x=0, 
        center_y=50, 
        scale=0.5, 
        category=Category.PLAYER
        )
    assert tile.category == Category.PLAYER