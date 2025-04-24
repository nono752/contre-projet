import arcade
from Core.GameScene import GameScene

class GameView(arcade.View):
    """Main in-game view."""
    scene: GameScene

    coin_sound: arcade.Sound
    jump_sound: arcade.Sound

    physic: arcade.PhysicsEnginePlatformer
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
        # initialise les membres
        self.scene = GameScene(path_file)
        
        self.coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")

        # parametre physique
        self.physic = arcade.PhysicsEnginePlatformer(self.scene.player, walls=self.scene.walls, gravity_constant=1) ## rm doit etre initialisé apres avoir créé tous les murs
        self.physic.enable_multi_jump(2)

    def on_update(self, delta_time) -> None:
        self.physic.update() # rm met aussi a jour la position du joueur par rapport a change x
        self.update_camera()
        #self.scene.update(delta_time)

        # collecte supprime les objets collectés
        collected: list[arcade.Sprite] = arcade.check_for_collision_with_list(self.scene.player, self.scene.interactables)
        for c in collected:
            arcade.play_sound(self.coin_sound)
            c.remove_from_sprite_lists()

    def on_draw(self) -> None:
        """Render the screen."""
        self.clear() # always start with self.clear()

        # affiche les listes avec camera
        with self.camera.activate():
            self.scene.draw()
    
    def on_key_press(self, symbol, modifiers) -> bool | None:
        match symbol:
            case arcade.key.D:
                self.scene.player.change_x += 5
            case arcade.key.A:
                self.scene.player.change_x -= 5
            case arcade.key.W:
                if self.physic.can_jump():
                    self.physic.jump(15)
                    arcade.play_sound(self.jump_sound)
            case arcade.key.ESCAPE:
                self.setup("maps/map1.txt")
        return super().on_key_press(symbol, modifiers)
    
    def on_key_release(self, symbol, modifiers) -> bool | None:
        match symbol:
            case arcade.key.D:
                self.scene.player.change_x -= 5
            case arcade.key.A:
                self.scene.player.change_x += 5
        return super().on_key_release(symbol, modifiers)
    
    ###########################################################################################################

    def update_camera(self) -> None:
        player = self.scene.player
        current_x = self.camera.position[0]
        current_y = self.camera.position[1]
        pos_min_y = self.camera.height/2 ## ATTENTION NE FONCTIONNE QUE SI LA CARTE EST CONSTRUITE AU DESSUS DE 0

        target_x = player.center_x
        target_y = max(player.center_y, pos_min_y) # max entre la position du joueur et la position minimale de la camera sur y

        new_pos_x = arcade.math.lerp(current_x, target_x, 0.03)
        new_pos_y = arcade.math.lerp(current_y, target_y, 0.1)

        self.camera.position = arcade.Vec2(new_pos_x, new_pos_y)
        
