from __future__ import annotations
import arcade
from TileSystem.Tile import Category, Tile
from abc import ABC

## revoir l'organisation pour composition
class Pawn(Tile, ABC):
    '''Classe de base pour tous les objets controllables'''
    iframe: IFrame
    _speed: float

    ##### mettre ceci dans une classe
    _hp: int
    _damage: int
    #####

    def kill(self) -> None: pass
    def on_hit(self, pawn: Pawn) -> None: pass
    
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
        self.iframe = IFrame(0.2)
        self.jump_speed = 15
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        self.is_killed = False
        self.score = 0

    def update(self, delta_time = 1 / 60, *args, **kwargs): pass

    @property
    def physic(self) -> arcade.PhysicsEnginePlatformer:
        return self.physics_engines[0]

    def move_right(self) -> None:
        self.change_x = self._speed
        
    def move_left(self) -> None:
        self.change_x = -self._speed

    def stop_moving_right(self) -> None:
        if self.change_x > 0:
            self.change_x = 0
    def stop_moving_left(self) -> None:
        if self.change_x < 0:
            self.change_x = 0

    def jump(self) -> None: 
        if self.physic.can_jump():
            arcade.play_sound(self.jump_sound)
            self.physic.jump(self.jump_speed)
    
    def take_damage(self, damage: int) -> None:
        if self.iframe.is_active == True:
            return
        
        self._hp -= damage
        if self._hp <= 0:
            self.kill()

        self.damage_animation()
        self.iframe.start()

    def kill(self) -> None:
        self.visible = False
        self.is_killed = True
        self.score = 0

    def damage_animation(self) -> None:
        self.color = arcade.color.RED
        arcade.schedule_once(lambda dt: setattr(self, "color", arcade.color.WHITE), 0.1)


class IFrame:
    duration: float
    is_active: bool

    def __init__(self, duration: float):
        self.duration = duration
        self.is_active = False
    
    def start(self) -> None:
        self.is_active = True
        arcade.schedule_once(lambda dt: setattr(self, "is_active", False), self.duration)
