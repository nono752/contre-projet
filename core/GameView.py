import arcade

from Core.config import TILE_SIZE
from Core.GameScene import GameScene
from Core.Managers.ControllerManager import ControllerManager
from Core.Managers.PhysicManager import PhysicManager

import math

class GameView(arcade.View): ## devrait etre un listener
    """Main in-game view."""
    scene: GameScene
    persistentData: arcade.Sprite ## pour l'instant on ne conserve que le joueur
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
        self.camera.zoom = 1.5
    
    def setup(self, path_file: str) -> None:
        """Set up the game here."""
        # initialise la scène
        self.scene = GameScene(path_file)

        # initialise les managers
        self.physic_mng = PhysicManager(self.scene, gravity_constant=1)
        self.controller_mng = ControllerManager(self.physic_mng)

    def on_update(self, delta_time: float) -> None:
        self.update_camera(delta_time)
        if self.scene.player.is_killed == True: ## déplacer dans un evenement
            self.setup(self.scene.data.curr_path)

        self.physic_mng.update()
        self.scene.update(delta_time)

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

    # fair un composant camerea mettre dans joueur
    def update_camera(self, dt: float) -> None:
        player = self.scene.player
        pos_min_y = self.camera.height/2 # ATTENTION NE FONCTIONNE QUE SI LA CARTE EST CONSTRUITE AU DESSUS DE 0
        pos_min_x = self.camera.width/2 # PAREIL
        pos_max_x = int(self.scene.data.keys["width"])*TILE_SIZE - self.camera.width/2

        current_x = self.camera.position[0]
        current_y = self.camera.position[1]
        target_x = max(player.center_x, pos_min_x)
        target_x = min(target_x, pos_max_x)
        target_y = max(player.center_y, pos_min_y)

        new_pos_x = arcade.math.smerp(current_x, target_x, dt, -1/math.log2(0.25)) #0.5 ko
        new_pos_y = arcade.math.smerp(current_y, target_y, dt, -1/math.log2(0.1)) #0.2 ok

        self.camera.position = arcade.Vec2(new_pos_x, new_pos_y)
        
