import arcade
from Core.GameScene import GameScene
from GameObjects.Interactable import Interactable
from GameObjects.Pawn import Pawn

class PhysicManager(arcade.PhysicsEnginePlatformer):
    scene: GameScene
    def __init__(self, scene: GameScene, gravity_constant = 0.5, ladders = None, walls = None):
        super().__init__(scene.player, scene.walls, gravity_constant, ladders, walls)
        self.scene = scene
        self.scene.player.physics_engines.append(self)

        # parametres d'initialisation
        self.enable_multi_jump(2)
    
    def update(self):
        self.__check_collision()
        self.scene.player.update()
        return super().update()
    
    def __check_collision(self) -> None:
        hit_interactable = arcade.check_for_collision_with_list(self.scene.player, self.scene.interactables)
        hit_pawns = arcade.check_for_collision_with_list(self.scene.player, self.scene.pawns)
        for target in hit_interactable or hit_pawns:
            target.on_hit(self.scene.player)
        