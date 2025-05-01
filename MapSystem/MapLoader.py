from dataclasses import dataclass
import re
import yaml
from typing import Any

## CHANGER EN RAWMAPDATA
@dataclass
class MapData:
    '''contient les données de la carte'''
    keys: Any
    grid: list[str]
    curr_path: str

class MapLoader:
    '''permet de charger la carte sans vérification dans MapData'''
    def load_from_file(self, path: str) -> MapData:
        """retourne les données de la carte sans vérifications"""
        with open(path, 'r', encoding="utf8") as f:
            content = f.read()

        sections = re.findall(r'(?:^|\n---\n)(.*?)(?=(?:\n---\n|\n---$|$))', content, re.DOTALL) # si jamais le fichier finit par \n--- ne le prend pas dans la carte
        keys = yaml.safe_load(sections[0])
        grid = sections[1].split("\n") if sections[1] else ""   
        return MapData(keys, [line.rstrip() for line in grid], path)