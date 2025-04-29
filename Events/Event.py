## juste quelques idée pour gérer evenements
import arcade
from GameObjects.Blob import Blob
from GameObjects.Interactable import Lava, Coin

# peut etre necessaire si besoin de passer un evenement avec des informations en plus
#class Event: pass
#
#class ControllerEvent(Event):
#    '''Contient les données utiles qu'on peut envoyer lorsqu'il y a evenement de controll'''
#    input_state: dict[int, bool]
#    interactable: list[arcade.Sprite] # revoir le type
#
####################################################################
class Flag:
    HIT = 0,
    INTERACT = 1,
class Event:
    HITBLOB = 0
    HITLAVA = 1
    COLLECTCOIN = 2
class EventDispatcher:
    selector: dict[tuple[int, type], int] # Associe un evenement representé par un int en fonction d'un flag(int) et du type du sender
    def __init__(self):
        self.selector = {
            (Flag.HIT, Blob): Event.HITBLOB,
            (Flag.HIT, Lava): Event.HITLAVA,
            (Flag.INTERACT, Coin): Event.COLLECTCOIN,
        }

    def dispatch(self, flag: int, sender: arcade.Sprite, listener: arcade.Sprite) -> None: pass
        # IF LISTENER IS A LISTENER INSTANCE OR HAS LISTENER COMPOSENT
        # create the right event with the selector
        # call listener.receiveEvent(event)

## dispatcher devrait par exemple etre appelé dans le physic/collision manager pour pouvoir appeler les bons copmortement chet les listeners