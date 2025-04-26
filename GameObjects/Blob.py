import arcade
from .Pawn import Pawn, Player
from TileSystem.Tile import Category

class Blob(Pawn):
    def __init__(self, path_or_texture=None, scale=1, center_x=0, center_y=0, angle=0, category = Category.WALL, **kwargs):
        super().__init__(path_or_texture, scale, center_x, center_y, angle, category, **kwargs)
        self._speed = 1
        self._damage = 50
        self.change_x = self._speed

    def move_right(self) -> None:
        self.change_x = self._speed
    def move_left(self) -> None:
        self.change_x = -self._speed
    def on_hit(self, pawn: Pawn) -> None:
        if not isinstance(pawn, Player):
            return
        if not pawn.is_invincible:
            pawn.hp -= self._damage
            pawn.change_y = 15

