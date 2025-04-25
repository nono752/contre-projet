import arcade
from .Controller import AIController
from GameObjects.Pawn import Pawn
from GameObjects.Blob import Blob
from typing import Sequence
class BlobController(AIController):
    def __init__(self, blobs: Sequence[Blob], scene):
        self.i = 0
        super().__init__(blobs, scene)

        # ajoute touche ici avec état initial
        self._input_state = {}

        # on lie les actions aux touches pressées ici
        self._key_pressed = {}

        # on lie les actions aux touches relachées ici
        self._key_released = {}

    def pattern(self, pawn: Pawn) -> None: 
        '''Si a la prochaine position il touche un mur lateralement ou touche de la lave change de sens'''
        if not isinstance(pawn, Blob):
            return
        if self.i == 0:
            self.__move_right(pawn)
            self.i += 1
            print("once")
        
    def __move_right(self, pawn: Blob) -> None:
        pawn.move_right()
    def __move_left(self, pawn: Blob) -> None: pass
