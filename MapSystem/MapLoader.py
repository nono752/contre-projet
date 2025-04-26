from dataclasses import dataclass
import re

## CHANGER EN RAWMAPDATA
@dataclass
class MapData:
    '''contient les données de la carte'''
    keys: dict[str, str]
    grid: list[str]
    curr_path: str

class MapLoader:
    '''permet de charger la carte sans vérification dans MapData'''
    def load_from_file(self, path: str) -> MapData:
        """retourne les données de la carte sans vérifications"""
        with open(path, 'r', encoding="utf8") as f:
            content = f.read()
    
        sections = re.findall(r'(?:^|\n---\n)(.*?)(?=(?:\n---\n|\n---$|$))', content, re.DOTALL) # utiliser split ici ne fonctionne pas si ligne finit par ---\n
        keys = self.find_keys(sections[0]) if sections[0] else {}
        grid = sections[1].split("\n") if sections[1] else ""
        
        return MapData(keys, [line.rstrip() for line in grid], path)
    
    def find_keys(self, section: str) -> dict[str, str]:
        '''trouve toutes les lignes de la forme clé: valeur et la retourne sous les retourne sous la forme d'un dictionnaire'''
        return { match.group(1): match.group(2).strip() for match in re.finditer(r'^\s*(\w+)\s*:\s*(\S.*)$', section, re.MULTILINE) }