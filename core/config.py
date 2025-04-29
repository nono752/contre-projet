from TileSystem.Tile import TileProperty, Category, Tile
from GameObjects.Interactable import *
from GameObjects.Player import Player
from GameObjects.Blob import Blob

## paremètres des tiles
TILE_SIZE = 64
SCALE = 0.5

SYMBOL_MAPPING = {
    "S": TileProperty(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", Category.PLAYER, Player),
    "=": TileProperty(":resources:images/tiles/grassMid.png", Category.WALL, Tile),
    "-": TileProperty(":resources:/images/tiles/grassHalf_mid.png", Category.WALL, Tile),
    "x": TileProperty(":resources:/images/tiles/boxCrate_double.png", Category.WALL, Tile),
    "*": TileProperty(":resources:/images/items/coinGold.png", Category.INTERACTABLE, Coin),
    "o": TileProperty(":resources:/images/enemies/slimeBlue.png", Category.PAWN, Blob),
    "£": TileProperty(":resources:/images/tiles/lava.png", Category.INTERACTABLE, Lava),
    "E": TileProperty(":resources:/images/tiles/signExit.png", Category.INTERACTABLE, Door),
}

SYMBOLS = [key for key in SYMBOL_MAPPING]
