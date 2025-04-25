from Controllers.Controller import Controller
from GameObjects.Pawn import Player
import arcade

class PlayerController(Controller):
    '''Controller spécifique au joueur.'''
    __player: Player

    def __init__(self, player: Player) -> None:
        super().__init__([player])
        self.__player = player

        # ajoute touche ici avec état initial
        self._input_state = {
            arcade.key.D: False,
            arcade.key.A: False,
            arcade.key.W: False,
        }

        # on lie les actions aux touches pressées ici
        self._key_pressed = { 
            arcade.key.D: [self.__move_right],
            arcade.key.A: [self.__move_left],
            arcade.key.W: [self.__jump],
        }

        # on lie les actions aux touches relachées ici
        self._key_released = {
            arcade.key.D: [self.__move_left],
            arcade.key.A: [self.__move_right],
        }

    # logique du joueur
    def __move_right(self) -> None: 
        self.__player.move_right()
    def __move_left(self) -> None: 
        self.__player.move_left()
    def __jump(self) -> None:
        self.__player.jump()

    def add_pawns(self, pawns): pass # on ne peut pas ajouter plus d'un joueur