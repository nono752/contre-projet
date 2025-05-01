from Core.config import *
from MapSystem.MapLoader import MapData
from TileSystem.Tile import Tile

from GameObjects.Interactable import *

class TileFactory:
    '''Gère la création des objets du jeu'''
    
    def create_map_tiles(self, validData: MapData) -> list[Tile]:
        '''Retourne la liste des sprites crées avec les symbols d'une MapData valide déjà à la bonne position'''
        tiles = self.__create_tile_list(validData)

        return tiles
    
    def __create_tile(self, symbol: str, x: int, y: int) -> Tile:
        '''crée un sprite à partir d'un symbol et de coordonnées'''
        value = SYMBOL_MAPPING[symbol] 
        tile_type = value.obj_type
        return tile_type(path_or_texture=value.texture, center_x=x, center_y=y, scale=SCALE, category=value.category)
    
    def __create_tile_list(self, validData: MapData) -> list[Tile]:
        tiles: list[Tile] = []
        grid = validData.grid

        for line in range(len(grid)):
            reversed_index = len(grid) - 1 - line
            pos_y = int((reversed_index + 0.5)*TILE_SIZE)
            for column in range(len(grid[line])):
                symbol = grid[line][column]
                if symbol not in SYMBOLS:
                    continue # si pas dans symbol ne crée pas de sprite
                pos_x = int((column + 0.5)*TILE_SIZE)
                tiles.append(self.__create_tile(symbol, pos_x, pos_y))

        return tiles
    
    def __is_in_a_platform(self) -> bool: 
        return False
    
