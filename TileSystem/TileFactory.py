from Core.config import *
from MapSystem.MapLoader import MapData
from TileSystem.Tile import Tile

from GameObjects.Interactable import *

class TileFactory:
    '''Gère la création des objets du jeu'''
    
    def create_map_tiles(self, validData: MapData) -> list[Tile]:
        '''Retourne la liste des sprites crées avec les symbols d'une MapData valide déjà à la bonne position'''
        tiles = self.__get_tiles(validData) 
        tiles = self.__convert_walls_to_platform(tiles, validData)
        return tiles

    def __create_tile(self, symbol: str, x: int, y: int) -> Tile:
        '''crée un sprite à partir d'un symbol et de coordonnées. Les symboles doivent etre déjà vérifiés'''
        value = SYMBOL_MAPPING[symbol]
        tile_type = value.obj_type
        return tile_type(path_or_texture=value.texture, center_x=x, center_y=y, scale=SCALE, category=value.category)
    
    def __get_tiles(self, validData: MapData) -> list[Tile]: 
        '''récupère les tiles de la carte'''
        tiles: list[Tile] = []
        grid = validData.grid

        for line in range(len(grid)):
            reversed_index = len(grid) - 1 - line
            pos_y = int((reversed_index + 0.5)*TILE_SIZE)
            for column in range(len(grid[line])):
                symbol = grid[line][column]
                if symbol not in SYMBOLS: # si le symbole n'est associé à aucune texture
                    continue 
                pos_x = int((column + 0.5)*TILE_SIZE)
                tiles.append(self.__create_tile(symbol, pos_x, pos_y))

        return tiles
    
    def __convert_walls_to_platform(self, tiles: list[Tile], validData: MapData) -> list[Tile]:
        '''Trouve les murs qui sont mobiles change leur category en PLATFORM et leur donne les bonnes borne de déplacement'''
        ## reflechir a un algo
        ## surement qqch de recursif
        ## ajouter bornes elem du groupe en fonction distance fleche
        ## utiliser set 
        return tiles