from MapSystem.MapLoader import MapLoader, MapData
import re

class MapValidator:
    '''validateur de base, verifie qu'un MapData contient des données valides'''
    REQUIRED_KEYS = {"width", "height"}
    KEY_TYPES = {
        "width": int,
        "height": int
    }

    def validate(self, data: MapData) -> None:
        '''passe tous les check de la classe'''
        self.__check_required_keys(data.keys)
        self.__check_keys_type(data.keys)
        self.__check_grid_dimension(data)
        self.__check_start_count(data)

    def __check_required_keys(self, keys: dict[str, str]) -> None:
        '''vérifie existence clés obligatoires. Lève exception si pas vérifié.'''
        missing = self.REQUIRED_KEYS - keys.keys() # on prend l'intersection des sets
        if missing:
            raise Exception(f"ERREUR: clés manquantes {missing}")
    
    def __check_keys_type(self, keys: dict[str, str]) -> None:
        '''vérifie que les clés sont connues et ont les type attendu. Lève exception si pas vérifié.'''
        for key, val in keys.items():
            if key not in self.KEY_TYPES:
                raise Exception(f"ERREUR: clé inconnue {key}")

            try:
                casted_value = self.KEY_TYPES[key](val) # tente une conversion si ne fonctionne pas TypeError
                if not isinstance(casted_value, self.KEY_TYPES[key]): # puis compare avec le type attendu
                    raise ValueError(f"ERREUR: {casted_value} n'est pas instance de {self.KEY_TYPES[key].__name__}")
            except (ValueError, TypeError):
                # l'erreur est levée si les types ne match pas ou si la conversion échoue
                raise Exception(f"ERREUR: la valeur {val} pour la clé {key} n'est pas du type {self.KEY_TYPES[key]}")
    
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
        width = int(data.keys["width"])
        data.grid = [line.ljust(width) for line in data.grid]
   
    def __check_start_count(self, data: MapData) -> None:
        '''vérifie que le point de départ du joueur est unique'''
        count = sum(len(re.findall("S", line)) for line in data.grid)
        if count != 1:
            raise Exception(f"ERREUR: compte de start incorrect {count}")
        
# on peut faire des validateurs dérivés si niveaux speciaux par exemple