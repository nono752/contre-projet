import arcade
from GameObjects.Pawn import Pawn
from collections.abc import Callable
from typing import Sequence

class Controller:
    _pawns: list[Pawn]
    _input_state: dict[int, bool]
    _key_pressed: dict[int, list[Callable[[],None]]]
    _key_released: dict[int, list[Callable[[],None]]]

    def __init__(self, pawns: Sequence[Pawn]) -> None: ## tout ce mic mac de sequence est dû à la co-variance
        self._pawns = list(pawns)
        self._input_state = {}
        self._key_pressed = {}
        self._key_released = {}
    
    def update(self) -> None: pass

    def update_from_key(self, key: int, state: bool) -> None:
        '''Met à jour le controller via des clés en principe appelé dans on_key_pressed/released'''
        for pawn in self._pawns:
            if key not in self._input_state.keys(): return # vérifie que la clé est connue
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
        '''Ajoute une liste de pawns au controller'''
        self._pawns += pawns
    def remove_pawns(self, pawns: list[Pawn]) -> None:
        for pawn in pawns:
            if pawn in self._pawns:
                self._pawns.remove(pawn)

class AIController(Controller):
    _scene: arcade.Scene
    def __init__(self, pawns: Sequence[Pawn], scene: arcade.Scene) -> None:
        super().__init__(pawns)
        self._scene = scene
    
    def update(self) -> None:
        for pawn in self._pawns:
            self.pattern(pawn)
    
    def pattern(self, pawn: Pawn) -> None:
        '''Definit les patten de mouvement indépendant des entrées joueur'''
        pass




    