import arcade
from .Controller import Controller
from Core.GameScene import GameScene

from GameObjects.Pawn import Pawn
from GameObjects.Blob import Blob

from Behavior import *

## peut etre remplacer par un IASystem du coup plus besoin controllermanager
## vraiment besoin d'heriter de controller
class AIController(Controller):
    __scene: GameScene
    ##behaviors: list[Behavior]  
    behavblob: BlobBehavior

    def __init__(self, scene: GameScene) -> None:
        super().__init__(scene.pawns)
        self.__scene = scene
        self.init_behaviors()
    
    def update(self, delta_time: float) -> None:
        ##for behavior in self.behaviors:
        ##    behavior.update()
        self.behavblob.update()

    def init_behaviors(self) -> None:
        ## self.behaviors = []
        ## self.behaviors.append(BlobBehavior(self.__scene))
        self.behavblob = BlobBehavior(self.__scene)

    def update_from_key(self, key, state) -> None: pass