import arcade
from .Controller import Controller
from Core.Managers.PhysicManager import PhysicManager

## revoir structure intégrer eventsystem
## le penser comme aieventdispatcher
class AIController(Controller):
    __physic: PhysicManager

    def __init__(self, physic: PhysicManager) -> None:
        super().__init__()
        self.__physic = physic

    def update_from_key(self, key, state) -> None: pass