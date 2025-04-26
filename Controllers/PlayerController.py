from Controllers.Controller import Controller
from GameObjects.Pawn import Player
from Core.GameScene import GameScene
import arcade

class PlayerController(Controller):
    '''Controller spécifique au joueur.'''
    __player: Player

    def __init__(self, scene: GameScene) -> None:
        players = scene.get_sprite_list("Players")
        super().__init__(players)
        self.__player = scene.player

        # ajoute touche ici avec état initial
        self._input_state = {
            arcade.key.D: False,
            arcade.key.A: False,
            arcade.key.W: False,
        }

        # on lie les actions aux touches pressées ici
        self._key_pressed = { 
            arcade.key.D: [self.__player.move_right],
            arcade.key.A: [self.__player.move_left],
            arcade.key.W: [self.__player.jump],
        }

        # on lie les actions aux touches relachées ici
        self._key_released = {
            arcade.key.D: [self.__player.move_left],
            arcade.key.A: [self.__player.move_right],
        }