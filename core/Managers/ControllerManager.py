import arcade

from Controllers.AIController import AIController
from Controllers.PlayerController import PlayerController

from GameObjects.Pawn import Pawn

from .PhysicManager import PhysicManager

class ControllerManager:
    player_controller: PlayerController
    AI_controller: AIController

    def __init__(self, physic: PhysicManager) -> None:
        '''Met les composants de la scene dans les bons controller'''
        self.player_controller = PlayerController(physic)
        self.AI_controller = AIController(physic)
    
    def update_from_key(self, key: int, state: bool) -> None:
        self.player_controller.update_from_key(key, state)
        self.AI_controller.update_from_key(key, state)
      