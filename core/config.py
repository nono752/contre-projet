from TileSystem.Tile import TileProperty, Category

## constantes
TILE_SIZE = 64
SCALE = 0.5
SYMBOL_MAPPING = {
    "S": TileProperty(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", Category.PLAYER),
    "=": TileProperty(":resources:images/tiles/grassMid.png", Category.WALL),
    "-": TileProperty(":resources:/images/tiles/grassHalf_mid.png", Category.WALL),
    "x": TileProperty(":resources:/images/tiles/boxCrate_double.png", Category.WALL),
    "*": TileProperty(":resources:/images/items/coinGold.png", Category.INTERACTABLE),
    "o": TileProperty(":resources:/images/enemies/slimeBlue.png", Category.PAWN),
    "£": TileProperty(":resources:/images/tiles/lava.png", Category.INTERACTABLE),
}
