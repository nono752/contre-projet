import arcade
from Core.config import *
from MapSystem.MapLoader import MapLoader, MapData
from MapSystem.MapValidator import MapValidator
from TileSystem.TileFactory import TileFactory
from TileSystem.Tile import *
from GameObjects.Pawn import Player
import copy

class GameScene(arcade.Scene):
    '''
    Gère la scene principale du jeu, dérivé de arcade.Scene. 
    Stock les tous les sprites, les met à jour et définit comment on les affiche.
    '''
    __mapData: MapData

    def __init__(self, file_path: str) -> None:
        '''Initialise les listes et charge la carte avec file_path'''
        super().__init__()
        self.add_sprite_list("Walls", use_spatial_hash=True)
        self.add_sprite_list("Ladders", use_spatial_hash=True)
        self.add_sprite_list("Interactables", use_spatial_hash=True)
        self.add_sprite_list("Pawns", use_spatial_hash=False)
        self.add_sprite_list("Players", use_spatial_hash=False) # ne devrait jamais contenir plus d'un element alors pourquoi une liste

        self.load_map(file_path)

    def reset(self) -> None:
        '''supprime tous les sprites de la scene'''
        self.get_sprite_list("Walls").clear()
        self.get_sprite_list("Ladders").clear()
        self.get_sprite_list("Interactables").clear()
        self.get_sprite_list("Pawns").clear()
        self.get_sprite_list("Players").clear()

    def load_map(self, file_path: str) -> None:
        '''Reset la scene et charge une nouvelle carte via le chemin donné'''
        self.reset()

        loader = MapLoader()
        validator = MapValidator()
        self.__mapData = loader.load_from_file(file_path)
        validator.validate(self.__mapData) # ici faudrait attraper l'exception que faire si la carte donnée n'est pas bonne

        factory = TileFactory()
        tiles = factory.create_map_tiles(self.__mapData)
        self.__store_tiles(tiles)
        
    def next_map(self) -> None: ## devrait se faire dans gameview normalement
        '''Change de carte. Le joueur conserve ses statistiques'''
        score = self.player.score ## les stocker au fur et a mesure dans un objet jamais détruit
        hp = self.player.hp
        to_load = self.__mapData.keys.get("next", "maps/default.txt")
        print(to_load)
        self.load_map(to_load) ## pour l'instant crash si map suivant invalid faut attraper l'exception
        self.player.score = score
        self.player.hp = hp ## lecontroller n'est pas mis a jour

    def __store_tiles(self, tiles: list[Tile]) -> None:
        '''met les tiles dans les bonnes catégories'''
        for tile in tiles:
            category = tile.category.value
            if not isinstance(category, str):
                continue
            self.add_sprite(category, tile)

    @property
    def data(self) -> MapData:
        return self.__mapData
    @property
    def player(self) -> Player:
        return self.get_sprite_list("Players")[0]
    @property
    def walls(self) -> arcade.SpriteList:
        return self.get_sprite_list("Walls")
    @property
    def ladders(self) -> arcade.SpriteList:
        return self.get_sprite_list("Ladders")
    @property
    def interactables(self) -> arcade.SpriteList:
        return self.get_sprite_list("Interactables")
    @property
    def pawns(self) -> arcade.SpriteList:
        return self.get_sprite_list("Pawns")
