import arcade
from Core.config import *
from MapSystem.MapLoader import MapLoader, MapData
from MapSystem.MapValidator import MapValidator
from TileSystem.TileFactory import TileFactory
from TileSystem.Tile import *
<<<<<<< HEAD
from GameObjects.Player import Player
=======
from GameObjects.Pawn import Player
>>>>>>> 56eb9ecb8e7cbe85daeee55129d4e62ef5beafb0

class GameScene(arcade.Scene):
    '''
    Gère la scene principale du jeu, dérivé de arcade.Scene. 
    Stock les tous les sprites, les met à jour et définit comment on les affiche.
    '''
    __mapData: MapData

    def __init__(self, file_path: str) -> None:
        '''Initialise les listes et charge la carte avec file_path'''
        super().__init__()
        self.add_sprite_list(Category.WALL.value, use_spatial_hash=True)
<<<<<<< HEAD
        self.add_sprite_list(Category.PLATFORM.value, use_spatial_hash=False)
=======
>>>>>>> 56eb9ecb8e7cbe85daeee55129d4e62ef5beafb0
        self.add_sprite_list(Category.LADDER.value, use_spatial_hash=True)
        self.add_sprite_list(Category.INTERACTABLE.value, use_spatial_hash=True)
        self.add_sprite_list(Category.PAWN.value, use_spatial_hash=False)
        self.add_sprite_list(Category.PLAYER.value, use_spatial_hash=False) # ne devrait jamais contenir plus d'un element alors pourquoi une liste

        self.load_map(file_path)

    def reset(self) -> None:
        '''supprime tous les sprites de la scene sauf le joueur'''
        self.get_sprite_list(Category.WALL.value).clear()
        self.get_sprite_list(Category.LADDER.value).clear()
        self.get_sprite_list(Category.INTERACTABLE.value).clear()
        self.get_sprite_list(Category.PAWN.value).clear()

    def load_map(self, file_path: str) -> None:
        '''Reset la scene et charge une nouvelle carte via le chemin donné'''
        self.reset()

        loader = MapLoader()
        validator = MapValidator()
        self.__mapData = loader.load_from_file(file_path)
        try:
            validator.validate(self.__mapData) ## que faire si la carte donnée n'est pas bonne
        except Exception as err:
            print(err)
            self.__mapData = loader.load_from_file("maps/default.txt")

        factory = TileFactory()
        tiles = factory.create_map_tiles(self.__mapData)
        self.__store_tiles(tiles)
        
    def next_map(self) -> None: ## devrait se faire dans gameview normalement
        '''Change de carte.'''
        to_load = self.__mapData.keys.get("next", "maps/default.txt")
        print(to_load)
        self.load_map(to_load)
        self.player.kill()

    def __store_tiles(self, tiles: list[Tile]) -> None:
        '''met les tiles dans les bonnes sprites listes'''
        for tile in tiles:
            category = tile.category.value
            if not isinstance(category, str):
                continue
            self.add_sprite(category, tile)

    @property
    def data(self) -> MapData: return self.__mapData
    @property
    def player(self) -> Player: return self.get_sprite_list(Category.PLAYER.value)[0]
    @property
    def walls(self) -> arcade.SpriteList: return self.get_sprite_list(Category.WALL.value)
    @property
<<<<<<< HEAD
    def platforms(self) -> arcade.SpriteList: return self.get_sprite_list(Category.PLATFORM.value)
    @property
=======
>>>>>>> 56eb9ecb8e7cbe85daeee55129d4e62ef5beafb0
    def ladders(self) -> arcade.SpriteList: return self.get_sprite_list(Category.LADDER.value)
    @property 
    def interactables(self) -> arcade.SpriteList: return self.get_sprite_list(Category.INTERACTABLE.value)
    @property 
    def pawns(self) -> arcade.SpriteList: return self.get_sprite_list(Category.PAWN.value)