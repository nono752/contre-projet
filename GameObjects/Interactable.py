import arcade
from TileSystem.Tile import Tile, Category
from .Pawn import Pawn
from .Player import Player
from abc import abstractmethod

class Interactable(Tile):
    '''Classe de base pour les objets avec lesquels on peut interragir.'''
    @abstractmethod
    def on_hit(self, pawn: Pawn) ->None:
        '''A appeler lorsqu'il y a collision.''' 
        ...

    @abstractmethod
    def on_interact(self, player: Player) -> None:
        '''A appeler lorsqu'il y a interaction avec le joueur.'''
        ...

class Lava(Interactable):
    def on_hit(self, pawn):
        '''Tue le pawn instantanément.'''
        pawn.kill()
        return None

class Coin(Interactable):
    coin_sound: arcade.Sound

    def __init__(self, path_or_texture=None, scale=1, center_x=0, center_y=0, angle=0, category=Category.WALL, **kwargs) -> None:
        super().__init__(path_or_texture, scale, center_x, center_y, angle, category, **kwargs)
        self.coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
    
    def on_hit(self, pawn):
        '''Disparait fait un son et ajoute un point au joueur'''
        if isinstance(pawn, Player):
            arcade.play_sound(self.coin_sound)
            self.remove_from_sprite_lists()
            pawn.score += 1
        return None

class Door(Interactable):
    def __init__(self, path_or_texture=None, scale=1, center_x=0, center_y=0, angle=0, category = Category.WALL, **kwargs):
        super().__init__(path_or_texture, scale, center_x, center_y, angle, category, **kwargs)
        self.change_map_event = None

    def on_interact(self, player):
        return