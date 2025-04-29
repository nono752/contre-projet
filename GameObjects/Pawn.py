from __future__ import annotations
from TileSystem.Tile import Tile
from abc import ABC
from Components.IFrame import IFrame

## revoir l'organisation pour composition
class Pawn(Tile, ABC):
    '''Classe de base pour tous les objets controllables'''
    iframe: IFrame
    _speed: float

    ##### mettre dans un component ?
    _hp: int
    _damage: int
    #####

    def kill(self) -> None: ...
    def on_hit(self, pawn: Pawn) -> None: ...
    
    def flip(self) -> None:
        self.texture = self.texture.flip_horizontally()

    @property
    def is_invincible(self) -> bool:
        return self.iframe.is_active
    @property
    def hp(self) -> int:
        return self._hp
    @hp.setter
    def hp(self, hp: int) -> None:
        if hp > 0:
            self._hp = hp