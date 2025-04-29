import arcade
from .Pawn import Pawn, Player
from TileSystem.Tile import Category

class Blob(Pawn):
    def __init__(self, path_or_texture=None, scale=1, center_x=0, center_y=0, angle=0, category = Category.WALL, **kwargs):
        super().__init__(path_or_texture, scale, center_x, center_y, angle, category, **kwargs)
        self.change_x = -1 ## utliser speed mais comprendre fonctions possibles arcade reverse? strafe?
        self._damage = 50

    def change_direction(self) -> None:
        self.texture = self.texture.flip_horizontally()
        self.change_x *= -1
        
    def on_hit(self, pawn: Pawn) -> None:
        if not isinstance(pawn, Player):
            return
        if not pawn.is_invincible:
            pawn.take_damage(self._damage)
            pawn.change_y = 15

