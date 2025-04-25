import arcade
from .Pawn import Pawn
from TileSystem.Tile import Category

class Blob(Pawn):
    speed: int
    def __init__(self, path_or_texture=None, scale=1, center_x=0, center_y=0, angle=0, category = Category.WALL, **kwargs):
        super().__init__(path_or_texture, scale, center_x, center_y, angle, category, **kwargs)
        self.speed = 3

    def move_right(self) -> None:
        self.change_x = self.speed
    def move_left(self) -> None:
        self.change_x = -self.speed
