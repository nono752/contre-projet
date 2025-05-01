from TileSystem.TileFactory import TileFactory
from MapSystem.MapLoader import MapLoader
from GameObjects.Blob import Blob
from GameObjects.Interactable import Coin
from GameObjects.Player import Player

def test_create_map_tiles() -> None:
    factory = TileFactory()
    loader = MapLoader()
    data = loader.load_from_file("tests/test_tile_system/maps/test_creation.yaml") # suppose que le fichier est valide

    tiles = factory.create_map_tiles(data)
    assert len(tiles) == 13
    assert len([tile for tile in tiles if isinstance(tile, Blob)]) == 4
    assert len([tile for tile in tiles if isinstance(tile, Coin)]) == 3
    assert len([tile for tile in tiles if isinstance(tile, Player)]) == 1