from __future__ import annotations
import arcade
from TileSystem.Tile import Category, Tile

## revoir l'organisation pour composition
class Pawn(Tile):
    '''Classe de base pour tous les objets controllables'''
    _speed: int
    ##### mettre ceci dans une classe
    _hp: int
    _damage: int
    _invincible_duration: float
    _is_invincible: bool
    #####

    def kill(self) -> None: pass
    def on_hit(self, pawn: Pawn) -> None: pass
    
    def flip(self) -> None:
        self.texture = self.texture.flip_horizontally()

    @property
    def is_invincible(self) -> bool:
        return self._is_invincible
    @property
    def hp(self) -> int:
        return self._hp
    @hp.setter
    def hp(self, hp: int) -> None:
        if hp > 0:
            self._hp = hp

class Player(Pawn): 
    is_killed: bool
    score: int
    jump_speed: int
    jump_sound: arcade.Sound
    def __init__(self, path_or_texture=None, scale=1, center_x=0, center_y=0, angle=0, category = Category.WALL, **kwargs):
        super().__init__(path_or_texture, scale, center_x, center_y, angle, category, **kwargs)
        self.flip() # commence en regardant à droite
        self._speed = 5
        self._hp = 100
        self._is_invincible = False
        self._invincible_duration = 0.2
        self.jump_speed = 15
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        self.is_killed = False
        self.score = 0

    def update(self, delta_time = 1 / 60, *args, **kwargs): pass

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
    
    def take_damage(self, damage: int) -> None:
        if self._is_invincible == True:
            return
        
        self._hp -= damage
        if self._hp <= 0:
            self.kill()

        self._is_invincible = True
        self.color = arcade.color.RED
        arcade.schedule_once(self.end_invicibility, self._invincible_duration)
        
    def end_invicibility(self, dt: float = 0) -> None:
        self._is_invincible = False
        self.color = arcade.color.WHITE

    def kill(self) -> None:
        self.visible = False
        self.is_killed = True
        self.score = 0
