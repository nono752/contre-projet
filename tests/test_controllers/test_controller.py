import pytest
import arcade
from Controllers.Controller import Controller

# rm: du coup fait aussi office de test pour le playercontroller pour l'instant
def test_controller() -> None:

    def foo() -> None: raise Exception("foo")
    def bar() -> None: raise Exception("bar")

    class TestController(Controller):
        def __init__(self) -> None:
            super().__init__()

            # ajoute touche ici avec état initial
            self._input_state = {
                arcade.key.A: False,
            }

            # on lie les actions aux touches pressées ici
            self._key_pressed = { 
                arcade.key.A: [foo],
            }

            # on lie les actions aux touches relachées ici
            self._key_released = {
                arcade.key.A: [bar],
            }

    controller = TestController()

    # la touche A est pressée
    with pytest.raises(Exception) as msg:
        controller.update_from_key(arcade.key.A, True)
        assert msg == "foo"
    
    # la touche A est relachée
    with pytest.raises(Exception) as msg:
        controller.update_from_key(arcade.key.A, False)
        assert msg == "bar"
    
    # relache A alors qu'elle est considérée comme relachée
    controller.update_from_key(arcade.key.A, False) # ignore