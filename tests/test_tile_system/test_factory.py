import pytest
from TileSystem.TileFactory import TileFactory
from MapSystem.MapLoader import MapLoader, MapData
from TileSystem.Tile import Tile, Category

factory = TileFactory()

def test_create_tile() -> None:
    tile = factory.create_tile("=",10,20)
    assert tile.category == Category.WALL
    assert tile.center_x == 10
    assert tile.center_y == 20

    with pytest.raises(ValueError):
        failed = factory.create_tile("K",0,0)

def test_create_map_tiles() -> None:
    loader = MapLoader()
    data = loader.load_from_file("tests/test_tile_system/maps/valid_map.txt") # pas de verif le fichier est valide

    tiles = factory.create_map_tiles(data)
    assert len(tiles) == 21