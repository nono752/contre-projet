from Controllers.Controller import Controller
from GameObjects.Pawn import Player
from Core.Managers.PhysicManager import PhysicManager
import arcade

class PlayerController(Controller):
    '''Controller spécifique au joueur.'''
    __player: Player
    __physic: PhysicManager

    def __init__(self, physic: PhysicManager) -> None:
        super().__init__()
        self.__player = physic.scene.player
        self.__physic = physic

        # ajoute touche ici avec état initial
        self._input_state = {
            arcade.key.D: False,
            arcade.key.A: False,
            arcade.key.W: False,
            arcade.key.E: False,
        }

        # on lie les actions aux touches pressées ici
        self._key_pressed = { 
            arcade.key.D: [self.__player.move_right, self.__player.flip],
            arcade.key.A: [self.__player.move_left, self.__player.flip],
            arcade.key.W: [self.__player.jump],
            arcade.key.E: [self.__physic.interact],
        }

        # on lie les actions aux touches relachées ici
        self._key_released = {
            arcade.key.D: [self.__player.stop_moving_right],
            arcade.key.A: [self.__player.stop_moving_left],
        }