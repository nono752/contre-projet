from MapSystem.MapLoader import MapData
import re

class MapValidator:
    '''validateur de base, verifie qu'un MapData contient des données valides'''
    REQUIRED_KEYS = {"width", "height"}
    KEY_TYPES = {
        "width": int,
        "height": int,
        "next": str
    }

    def validate(self, data: MapData) -> None:
        '''passe tous les check de la classe'''
        self.__check_required_keys(data)
        self.__check_keys_type(data)
        self.__check_grid_dimension(data)
        self.__check_start(data)
        self.__check_exit(data)

    def __check_required_keys(self, data: MapData) -> None:
        '''vérifie existence clés obligatoires. Lève exception si pas vérifié.'''
        missing = self.REQUIRED_KEYS - data.keys.keys() # on prend l'intersection des sets
        if missing:
            raise Exception(f"ERREUR: clés manquantes {missing}")
    
    def __check_keys_type(self, data: MapData) -> None:
        '''vérifie que les clés sont connues et ont les type attendu. Lève exception si pas vérifié.'''
        for key, val in data.keys.items():
            if key not in self.KEY_TYPES:
                raise Exception(f"ERREUR: clé inconnue {key}")
            
            if not type(val) == self.KEY_TYPES[key]:
                raise Exception(f"ERREUR: type de {key} recu {type(val)}, attendu {self.KEY_TYPES[key]}")
    
    def __check_grid_dimension(self, data: MapData) -> None:
        '''
        vérifie les dimension de la grille par rapport à ses clé obligatoires width/height et complete la grille.
        Attention utiliser uniquement apres avoir vérifie l'existence des clé obligatoires et leur type.
        Lève exception si dimensions pas correctes.
        '''
        if len(data.grid) != int(data.keys["height"]):
            raise Exception(f"ERREUR: hauteur de carte incorrecte attendu:{int(data.keys["height"])}, recu:{len(data.grid)}")
        if any(len(line) > int(data.keys["width"]) for line in data.grid):
            raise Exception("ERREUR: largeur de carte dépassée")

        self.__complete_grid(data)

    def __complete_grid(self, data: MapData) -> None:
        '''
        Complete la grille avec des espaces si ligne trop est courte.
        Attention utiliser uniquement apres avoir vérifie l'existence des clé obligatoires et leur type.
        '''
        width = data.keys["width"]
        data.grid = [line.ljust(width) for line in data.grid]
   
    def __check_start(self, data: MapData) -> None:
        '''vérifie que le point de départ du joueur est unique'''
        count = sum(len(re.findall("S", line)) for line in data.grid)
        if count != 1:
            raise Exception(f"ERREUR: compte de start incorrect {count}")
    def __check_exit(self, data: MapData)  -> None:
        '''S'il y a une porte vérifie que la clé next existe'''
        count = sum(len(re.findall("E", line)) for line in data.grid)
        if count >= 1:
            key = data.keys.get("next")
            if key is None:
                raise Exception(f"ERREUR: {count} portes mais pas de clé next")

# on peut faire des validateurs dérivés si niveaux speciaux par exemple