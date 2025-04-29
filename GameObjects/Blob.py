import arcade
from .Pawn import Pawn
from .Player import Player
from TileSystem.Tile import Category

class Blob(Pawn):
    def __init__(self, path_or_texture=None, scale=1, center_x=0, center_y=0, angle=0, category = Category.WALL, **kwargs):
        super().__init__(path_or_texture, scale, center_x, center_y, angle, category, **kwargs)
        self.change_x = -1 ## utliser speed mais comprendre fonctions possibles arcade reverse? strafe?
        self._damage = 50

    def change_direction(self) -> None:
        self.texture = self.texture.flip_horizontally()
        self.change_x *= -1
        
    def on_hit(self, target: Pawn) -> None:
        if not isinstance(target, Player):
            return
        if not target.is_invincible:
            target.take_damage(self._damage)
            target.change_y = 15

