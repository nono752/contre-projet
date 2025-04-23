import arcade

class GameView(arcade.View):
    """Main in-game view."""
    player: arcade.Sprite
    walls: arcade.SpriteList[arcade.Sprite]
    collectables: arcade.SpriteList[arcade.Sprite]

    coin_sound: arcade.Sound
    jump_sound: arcade.Sound

    physic: arcade.PhysicsEnginePlatformer
    camera: arcade.camera.Camera2D

    def __init__(self) -> None:
        # Magical incantion: initialize the Arcade view
        super().__init__()

        # Choose a nice comfy background color
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE

        # Init camera
        self.camera = arcade.camera.Camera2D()

        # Setup our game
        self.setup()

    def setup(self) -> None:
        """Set up the game here."""
        # initialise les membres
        self.player = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", center_x=64, center_y=128)
        self.walls = arcade.SpriteList(use_spatial_hash=True) # spatial hash pour objet immobiles
        self.collectables = arcade.SpriteList(use_spatial_hash=True)

        self.coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        
        # ajout de sprite
        for x in range(0, 1280, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", center_x=x, center_y=32, scale=0.5)
            self.walls.append(wall)
        for x in {256, 512, 768}:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", center_x=x, center_y=96, scale=0.5)
            self.walls.append(wall)
        for x in {128, 384}:
            coin = arcade.Sprite(":resources:images/items/coinGold.png", center_x=x, center_y=96, scale=0.5)
            self.collectables.append(coin)
        
        # parametre physique
        self.physic = arcade.PhysicsEnginePlatformer(self.player, walls=self.walls, gravity_constant=1) ## rm doit etre initialisé apres avoir créé tous les murs
        self.physic.enable_multi_jump(50)

    def on_update(self, delta_time) -> None:
        self.physic.update() # rm met aussi a jour la position du joueur par rapport a change x
        self.update_camera()

        # collecte supprime les objets collectés
        collected: list[arcade.Sprite] = arcade.check_for_collision_with_list(self.player, self.collectables)
        for c in collected:
            arcade.play_sound(self.coin_sound)
            c.remove_from_sprite_lists()

    def on_draw(self) -> None:
        """Render the screen."""
        self.clear() # always start with self.clear()

        # affiche les listes avec camera
        with self.camera.activate():
            arcade.draw_sprite(self.player)
            self.walls.draw()
            self.collectables.draw()
    
    def on_key_press(self, symbol, modifiers) -> bool | None:
        match symbol:
            case arcade.key.D:
                self.player.change_x += 5
            case arcade.key.A:
                self.player.change_x -= 5
            case arcade.key.W:
                if self.physic.can_jump():
                    self.physic.jump(15)
                    arcade.play_sound(self.jump_sound)
            case arcade.key.ESCAPE:
                self.setup()
        return super().on_key_press(symbol, modifiers)
    
    def on_key_release(self, symbol, modifiers) -> bool | None:
        match symbol:
            case arcade.key.D:
                self.player.change_x -= 5
            case arcade.key.A:
                self.player.change_x += 5
        return super().on_key_release(symbol, modifiers)
    
    ###########################################################################################################

    def update_camera(self) -> None:
        current_x = self.camera.position[0]
        current_y = self.camera.position[1]
        pos_min_y = self.camera.height/2 ## ATTENTION NE FONCTIONNE QUE SI LA CARTE EST CONSTRUITE AU DESSUS DE 0

        target_x = self.player.center_x
        target_y = max(self.player.center_y, pos_min_y) # max entre la position du joueur et la position minimale de la camera sur y

        new_pos_x = arcade.math.lerp(current_x, target_x, 0.03)
        new_pos_y = arcade.math.lerp(current_y, target_y, 0.3)

        self.camera.position = arcade.Vec2(new_pos_x, new_pos_y)
        
