from dataclasses import dataclass
import re

@dataclass
class MapData:
    '''contient les données de la carte'''
    keys: dict[str, str]
    grid: list[str]

class MapLoader:
    '''permet de charger la carte sans vérification dans MapData'''
    def load_from_file(self, path: str) -> MapData:
        """retourne les données de la carte sans vérifications"""
        with open(path, 'r', encoding="utf8") as f:
            content = f.read()
            sections = content.split('---\n', maxsplit=1) # maxsplit pour eviter de separer la carte si elle contient une ligne separateur
        
        keys = self.find_keys(sections[0])
        grid = sections[1].split('\n') if len(sections) > 1 else []

        # supprime tout ce qu'il y a apres le dernier --- pour éviter problème nb lignes s'il y a lignes vides en fin de fichier
        for i in range(len(grid) - 1, 0, -1):  # Parcours inverse avec index
            if grid[i] == "---":
                break
        grid = grid[:i]

        return MapData(keys, [line.rstrip() for line in grid if line])
    
    def find_keys(self, section: str) -> dict[str, str]:
        '''trouve toutes les lignes de la forme clé: valeur et la retourne sous les retourne sous la forme d'un dictionnaire'''
        return { match.group(1): match.group(2).strip() for match in re.finditer(r'^\s*(\w+)\s*:\s*(\S.*)$', section, re.MULTILINE) }