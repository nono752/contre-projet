import arcade
from TileSystem.Tile import Category, Tile

class Pawn(Tile):
    '''Classe de base pour tous les objets controllables'''
    def kill(self) -> None: pass
    def on_hit(self) -> None: pass
    
class Player(Pawn): 
    speed: int
    jump_speed: int
    jump_sound: arcade.Sound
    is_killed: bool

    def __init__(self, path_or_texture=None, scale=1, center_x=0, center_y=0, angle=0, category = Category.WALL, **kwargs):
        super().__init__(path_or_texture, scale, center_x, center_y, angle, category, **kwargs)
        self.speed = 5
        self.jump_speed = 15
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        self.is_killed = False

    @property
    def physic(self) -> arcade.PhysicsEnginePlatformer:
        return self.physics_engines[0]
    
    def move_right(self) -> None:
        self.change_x += self.speed

    def move_left(self) -> None:
        self.change_x -= self.speed

    def jump(self) -> None: 
        if self.physic.can_jump():
            arcade.play_sound(self.jump_sound)
            self.physic.jump(self.jump_speed)
    
    def kill(self) -> None:
        self.is_killed = True
