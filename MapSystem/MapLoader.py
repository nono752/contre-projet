from dataclasses import dataclass
import re
import yaml
from typing import Any

@dataclass
class MapData:
    '''contient les données de la carte'''
    keys: dict[str, Any]
    grid: list[str]
    curr_path: str

class MapLoader:
    '''permet de charger la carte sans vérification dans MapData'''
    def load_from_file(self, path: str) -> MapData:
        """retourne les données de la carte sans vérifications"""
        with open(path, 'r', encoding="utf8") as f:
            content = f.read()

        sections = re.findall(r'(?:^|\n---\n)(.*?)(?=(?:\n---\n|\n---$|$))', content, re.DOTALL) # si jamais le fichier finit par \n--- ne le prend pas dans la carte
        keys = self.__load_keys(sections[0])
        grid = sections[1].split("\n") if sections[1] else ""   
        return MapData(keys, [line.rstrip() for line in grid], path)
    
    def __find_dict(self, section) -> str:
        '''Enlève tout ce qui n'est pas du format key: value'''
        pattern = r'^\s*(\w+\s*:\s*\S+)'
        return '\n'.join(match.group(1) for match in re.finditer(pattern, section, re.MULTILINE))
     
    def __load_keys(self, section: str) -> dict[str, Any]:
        dict_str = self.__find_dict(section)
        print(dict_str)
        data: dict[str, Any] = yaml.safe_load(dict_str)
        return data