from __future__ import annotations
import arcade
from TileSystem.Tile import Category, Tile
import time

class Pawn(Tile):
    _speed: int
    _hp: int
    _damage: int
    _invincible_time: float
    _is_invincible: bool
    _last_hit_time: float
    '''Classe de base pour tous les objets controllables'''
    def kill(self) -> None: pass
    def on_hit(self, pawn: Pawn) -> None: pass
    
    @property
    def is_invincible(self) -> bool:
        return self._is_invincible
    @property
    def hp(self) -> int:
        return self._hp
    @hp.setter
    def hp(self, new: int) -> None:
        if self._is_invincible == True:
            return
        self._hp = new
        self._is_invincible = True
        self._last_hit_time = time.time()
        if self._hp <= 0:
            self.kill()

class Player(Pawn): 
    is_killed: bool
    jump_speed: int
    jump_sound: arcade.Sound
    def __init__(self, path_or_texture=None, scale=1, center_x=0, center_y=0, angle=0, category = Category.WALL, **kwargs):
        super().__init__(path_or_texture, scale, center_x, center_y, angle, category, **kwargs)
        self._speed = 5
        self._hp = 100
        self._is_invincible = False
        self._invincible_time = 1.5
        self.jump_speed = 15
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        self.is_killed = False

    def update(self, delta_time = 1 / 60, *args, **kwargs):
        if self._is_invincible and (time.time() - self._last_hit_time > self._invincible_time):
            self._is_invincible = False

    @property
    def physic(self) -> arcade.PhysicsEnginePlatformer:
        return self.physics_engines[0]
    
    def move_right(self) -> None:
        self.change_x += self._speed

    def move_left(self) -> None:
        self.change_x -= self._speed

    def jump(self) -> None: 
        if self.physic.can_jump():
            arcade.play_sound(self.jump_sound)
            self.physic.jump(self.jump_speed)
    
    def kill(self) -> None:
        self.visible = False
        self.is_killed = True
