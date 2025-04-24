import arcade
from enum import Enum
from dataclasses import dataclass
from typing import Final

class Category(Enum):
    WALL = "Walls"
    LADDER = "Ladders"
    INTERACTABLE = "Interactables"
    PAWN = "Pawns"
    PLAYER = "Players"

@dataclass(frozen=True)
class TileProperty:
    texture: str
    category: Category

class Tile(arcade.Sprite):
    category: Final[Category]
    def __init__(self, path_or_texture = None, scale = 1, center_x = 0, center_y = 0, angle = 0, category: Category = Category.WALL, **kwargs) -> None:
        super().__init__(path_or_texture, scale, center_x, center_y, angle, **kwargs)
        self.category = category
    
