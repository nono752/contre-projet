import arcade
from Core.GameScene import GameScene
from GameObjects.Interactable import *
from GameObjects.Pawn import Pawn
from GameObjects.Blob import Blob

class PhysicManager(arcade.PhysicsEnginePlatformer):
    '''Connait la scene. Doit gérer les collisions du jeu et la gravité du joueur'''
    scene: GameScene
    def __init__(self, scene: GameScene, g = 0.5) -> None:
        super().__init__(player_sprite=scene.player, walls=scene.walls, platforms=scene.platforms, gravity_constant=g, ladders=scene.ladders)
        self.scene = scene
        self.scene.player.physics_engines.append(self)

        # parametres physic engine
        self.enable_multi_jump(2)
    
    def update(self):
        self.__check_collision()
        return super().update()
    
    def __check_collision(self) -> None:
        # vérifie collisions joueur
        hit_interactable: list[Interactable] = arcade.check_for_collision_with_list(self.scene.player, self.scene.interactables)
        hit_pawns: list[Pawn] = arcade.check_for_collision_with_list(self.scene.player, self.scene.pawns)
        for target in hit_interactable or hit_pawns:
            target.on_hit(self.scene.player)
        
        #vérifie colisions BLOB
        ## TRES MAUVAIS CHANGER
        blobs = [blob for blob in self.scene.pawns if isinstance(blob, Blob)]
        for blob in blobs:
            # si colisionne lateralement
            if arcade.check_for_collision_with_lists(blob, [self.scene.pawns, self.scene.walls]):
                blob.change_direction()
                continue
            # si le point en bas à droite/gauche en colision avec mur
            collision_box = arcade.SpriteSolidColor(width=1, height=1)
            if  blob.change_x > 0:
                collision_box.position = (blob.right + 1, blob.bottom - 1)
            else:
                collision_box.position = (blob.left + blob.change_x, blob.bottom - 1)
            if not arcade.check_for_collision_with_list(collision_box, self.scene.walls):
                blob.change_direction()



    def interact(self) -> None:
        hit_interactable: list[Interactable] = arcade.check_for_collision_with_list(self.scene.player, self.scene.interactables)
        for target in hit_interactable:
            target.on_interact(self.scene.player) # devrait recup un event mais apres ?
            
            ## MAUVAIS CHANGER POUR EVENTSYSTEM
            if isinstance(target, Door):
                self.scene.next_map()
        