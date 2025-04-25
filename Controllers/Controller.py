from GameObjects.Pawn import Pawn
from collections.abc import Callable

class Controller:
    _pawns: list[Pawn]
    _input_state: dict[int, bool]
    _key_pressed: dict[int, list[Callable[[],None]]]
    _key_released: dict[int, list[Callable[[],None]]]

    def __init__(self, pawns: list[Pawn]) -> None:
        self._pawns = pawns
        self._input_state = {}
        self._key_pressed = {}
        self._key_released = {}
    
    def update(self, key: int, state: bool) -> None:
        '''Met à jour le controller'''
        if key not in self._input_state.keys(): return
        if self.__invalid_input(key, state): return
        self.__bind_input(key, state)
        self._input_state[key] = state

    def __bind_input(self, key: int, state: bool) -> None:
        '''Appelle les actions de la touche en fonction de si elle est pressée ou relachée'''
        if state == True:
            actions = self._key_pressed.get(key)
        elif state == False:
            actions = self._key_released.get(key)
        if actions is None:
            return
        for action in actions:
            action()
    
    def __invalid_input(self, valid_key: int, new_state: bool) -> bool:
        '''Vérifie qu'une touche n'est pas relachée avant d'être pressée et inversement. Suppose que la clé entrée est connue du controller.'''
        key_last_state = self._input_state[valid_key]
        if key_last_state == new_state:
            return True
        return False

    def add_pawns(self, pawns: list[Pawn]) -> None:
        self._pawns += pawns



    