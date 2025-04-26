import arcade

from Core.GameScene import GameScene
from Core.Managers.ControllerManager import ControllerManager
from Core.Managers.PhysicManager import PhysicManager

from typing import Sequence

class GameView(arcade.View):
    """Main in-game view."""
    scene: GameScene

    physic_mng: PhysicManager
    controller_mng: ControllerManager

    camera: arcade.camera.Camera2D

    def __init__(self) -> None:
        # Magical incantion: initialize the Arcade view
        super().__init__()

        # Choose a nice comfy background color
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE

        # Setup our game
        self.setup("maps/map1.txt")

        # Init camera
        self.camera = arcade.camera.Camera2D()

    def setup(self, path_file: str) -> None:
        """Set up the game here."""
        # initialise la scène
        self.scene = GameScene(path_file)

        # initialise les managers
        self.physic_mng = PhysicManager(self.scene, gravity_constant=1)
        self.controller_mng = ControllerManager(self.scene)

    def on_update(self, delta_time: float) -> None:
        self.update_camera()
        if self.scene.player.is_killed == True:
            self.setup(self.scene.current_path)

        self.physic_mng.update()
        self.scene.update(delta_time)
        self.controller_mng.update(delta_time)

    def on_draw(self) -> None:
        """Render the screen."""
        self.clear() # always start with self.clear()

        with self.camera.activate():
            self.scene.draw()
    
    def on_key_press(self, key: int, modifiers: int) -> bool | None:
        self.controller_mng.update_from_key(key, True)
        return super().on_key_release(key, modifiers)
    
    def on_key_release(self, key: int, modifiers: int) -> bool | None:
        self.controller_mng.update_from_key(key, False)
        return super().on_key_release(key, modifiers)
    
    ###########################################################################################################

    def update_camera(self) -> None:
        player = self.scene.player
        current_x = self.camera.position[0]
        current_y = self.camera.position[1]
        pos_min_y = self.camera.height/2 ## ATTENTION NE FONCTIONNE QUE SI LA CARTE EST CONSTRUITE AU DESSUS DE 0

        target_x = player.center_x
        target_y = max(player.center_y, pos_min_y) # max entre la position du joueur et la position minimale de la camera sur y

        new_pos_x = arcade.math.lerp(current_x, target_x, 0.02)
        new_pos_y = arcade.math.lerp(current_y, target_y, 0.1)

        self.camera.position = arcade.Vec2(new_pos_x, new_pos_y)
        
