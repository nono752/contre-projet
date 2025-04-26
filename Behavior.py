from GameObjects.Pawn import Pawn
from GameObjects.Blob import Blob
from Core.GameScene import GameScene
from Core.config import TILE_SIZE
from abc import abstractmethod
import arcade

##class Behavior[T:Pawn]:
##    _match: list[T]
##    _scene: GameScene
##    def __init__(self, scene: GameScene) -> None:
##        self.__match = [match for match in scene.pawns if isinstance(match, T)]
##
##    def update(self) -> None:
##        for sprite in self._match:
##            self.pattern(sprite, self._scene)
##
##    def pattern(self, target: T, scene: GameScene) -> None:
##        pass
##
##class BlobBehavior(Behavior[Blob]):
##    def __init__(self, scene: GameScene) -> None:
##        self._match = [match for match in scene.pawns if isinstance(match, Blob)]
##    def pattern(self, target: Blob, scene: GameScene) -> None:
##        target.change_x = 1

# Tant que le generique ne fonctionne pas
class BlobBehavior:
    _match: list[Blob]
    _scene: GameScene
    def __init__(self, scene: GameScene) -> None:
        self._match = [match for match in scene.pawns if isinstance(match, Blob)]
        self._scene = scene

    def update(self) -> None:
        for sprite in self._match:
            self.pattern(sprite)

    def pattern(self, target: Blob) -> None:
        # si colisionne lateralement
        if arcade.check_for_collision_with_lists(target, [self._scene.pawns, self._scene.walls]):
            target.change_x *= -1
            return
        # si le point en bas à droite/gauche en colision avec mur
        collision_box = arcade.SpriteSolidColor(width=1, height=1)
        if  target.change_x > 0:
            collision_box.position = (target.right + 1, target.bottom - 1)
        else:
            collision_box.position = (target.left + target.change_x, target.bottom - 1)
        if not arcade.check_for_collision_with_list(collision_box, self._scene.walls):
            target.change_x *= -1



    