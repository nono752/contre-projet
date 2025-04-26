import arcade

from Controllers.AIController import AIController
from Controllers.PlayerController import PlayerController

from GameObjects.Pawn import Pawn

from ..GameScene import GameScene

class ControllerManager:
    player_controller: PlayerController
    AI_controller: AIController

    def __init__(self, scene: GameScene) -> None:
        '''Met les composants de la scene dans les bons controller'''
        self.player_controller = PlayerController(scene)
        self.AI_controller = AIController(scene)

    def update(self, delta_time: float) -> None:
        self.player_controller.update(delta_time)
        self.AI_controller.update(delta_time)
    
    def update_from_key(self, key: int, state: bool) -> None:
        self.player_controller.update_from_key(key, state)
        self.AI_controller.update_from_key(key, state)
      