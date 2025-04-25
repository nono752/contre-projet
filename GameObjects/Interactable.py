import arcade
from TileSystem.Tile import Tile, Category
from .Pawn import Pawn

class Interactable(Tile):
    '''Classe de base pour les objets avec lesquels on peut interragir.'''
    def on_hit(self, pawn: Pawn) -> None:
        '''A appeler lorsqu'il y a collision.'''
        pass

    def on_interact(self, pawn: Pawn) -> None:
        '''A appeler lorsqu'il y a interaction.'''
        pass

class Lava(Interactable):
    def on_hit(self, pawn) -> None:
        '''Tue le joueur instantanément.'''
        pawn.kill()

class Coin(Interactable):
    coin_sound: arcade.Sound

    def __init__(self, path_or_texture=None, scale=1, center_x=0, center_y=0, angle=0, category=Category.WALL, **kwargs) -> None:
        super().__init__(path_or_texture, scale, center_x, center_y, angle, category, **kwargs)
        self.coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
    
    def on_hit(self, pawn) -> None:
        '''Disparait fait un son et ajoute un point au joueur'''
        arcade.play_sound(self.coin_sound)
        self.remove_from_sprite_lists()