import arcade
from GameObjects.Pawn import Pawn
from TileSystem.Tile import Category
from Components.IFrame import IFrame

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
        self.change_x += self._speed  
    def move_left(self) -> None: self.change_x -= self._speed

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

    def damage_animation(self) -> None:
        self.color = arcade.color.RED
        arcade.schedule_once(lambda dt: setattr(self, "color", arcade.color.WHITE), 0.1)