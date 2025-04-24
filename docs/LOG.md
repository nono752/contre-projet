# Journal

## À faire (prochaine étape)

Mettez ici ce que vous pensez devoir être la ou les 2 prochaines étapes pour chacune/chacun.

- **semaine 2**  
  * Est-ce qu'aucun test sont vraiment nécessaire pour la semaine 2 ? Si non les faire !
- **semaine 3**  
  * Est-ce que les les tests sont suffisants pour loader et validator ? Devrait-on vérifier affichage des exceptions ?  
  * peut-on faire un type special d'exception pour les cartes ?  
  * on ne vérifie pas que le width/heigth soient unsigned. Cela se verifie dans la verif de taille carte car fera forcement une erreur. OK ?  
  * Probleme mapdata est modifiable.  
  * Probleme pour l'instant la carte ne peut avoir que deux sections c'est un peu du bidouillage  

## Sommaire
- [Semaine 2](#Semaine-2)
- [Semaine 3](#Semaine-3)
- [Semaine 4](#Semaine-4)
- [Semaine 5](#Semaine-5)
- [Semaine 6 à 9 - refactoring](#Semaine-6-à-9---refactoring)
- [Semaine 10](#Semaine-10)
- [Semaine 11](#Semaine-11)
- [Semaine 12](#Semaine-12)
- [Semaine 13](#Semaine-13)
- [Semaine 14](#Semaine-14)

---

## Semaine 2
### taches
* [x] Créer le LOG.md                                                 
* [x] S'inscrire en binôme                                            
* [x] Découverte d'Arcade                                             
* [x] Meilleure gestion du clavier                                   
* [x] Meilleure gestion de la caméra                                  
* [x] `README.md` à jour, expliquant comment jouer   

### LOG
- **Gestion calvier**  
Au lieu d'assigner directement `change_x = velocity`, on ajoute/soustrait la vitesse lors de l'appui/relachement. 
L'opposé est appliqué à la touche de déplacement en sens contraire.    
Pour le saut, on utilise les methodes:
  ```python
  def enable_multi_jump(allowed_jumps: int) -> None:
  def can_jump(y_distance: float = 5) -> bool:
  ```  
de la classe `arcade.PhysicsEnginePlatformer` pour: en fonction du nombre de saut donné savoir si le joueur peut sauter

- **Gestion caméra**  
On utilise une interpolation linéaire`pour suivre le joueur tant qu'il ne se trouve pas à un point ou le suivre ferait sortir
la camera de la carte:
  ```python
   def update_camera(self) -> None:
          current_x = self.camera.position[0]
          current_y = self.camera.position[1]
          pos_min_y = self.camera.height/2 ## ATTENTION NE FONCTIONNE QUE SI LA CARTE EST CONSTRUITE AU DESSUS DE 0
  
          target_x = self.player.center_x
          target_y = max(self.player.center_y, pos_min_y) # max entre la position du joueur et la position minimale de la camera sur y
  
          new_pos_x = arcade.math.lerp(current_x, target_x, 0.03)
          new_pos_y = arcade.math.lerp(current_y, target_y, 0.3)
  
          self.camera.position = (new_pos_x, new_pos_y)
  ```

- **Ajout readme.md**  
Ajout premiere version readme qui décrit le programme de manière générale et explique:
  1. comment cloner et lancer
  2. les autres commandes uv utiles pour le projet
  3. le but du jeu, les mécaniques principales et les commandes

- **Tests**  
Pour l'instant hormis les test du tutoriel, aucun ajout ne semble nécessaire.



## Semaine 3
### taches
* [ ] Mettre le LOG à jour                                        
* [ ] Mettre le ANSWER à jour                                        
* [X] Pouvoir récuperer carte depuis txt                                    
* [X] Pouvoir vérifier la carte
* [X] pouvoir lire la carte et ajouter à la scene les bon sprites
 
### LOG
- **Décodage de la carte**  
Le décodage se fait comme suit:
  1. `MapLoader` charge les données de la carte sans vérification dans `MapData`:
    ```python
    @dataclass
    class MapData:
        '''contient les données de la carte'''
        keys: dict[str, str]
        grid: list[str]
    ```
  2. `MapValidator` valide ou lance un exception.
    Les vérifications sont: un seul point de départ, bonnes dimensions, clés obligatoires et types correspondent.
  3. On fait le lien entre symbole et objet à créer dans `config.py` les constantes utiles à la création de la carte sont conservées ici.
  4. `TileFactory` crée des `Tile` en fonction du symbole.
    ```python
    class Category(Enum):
        WALL = "Walls"
        LADDER = "Ladders"
        INTERACTABLE = "Interactables"
        PAWN = "Pawns"
        PLAYER = "Players"
  
    class Tile(arcade.Sprite):
        category: Final[Category]
        def __init__(self, path_or_texture = None, scale = 1, center_x = 0, center_y = 0, angle = 0, category: Category = Category.WALL, **kwargs) -> None:
            super().__init__(path_or_texture, scale, center_x, center_y, angle, **kwargs)
            self.category = category
    ```
  5. `GameScene` utilise les points précédents charger des cartes en placant les Tiles dans les bonnes `SpriteList` et aux bonnes coordonnées.  
  Il contient tous les sprites du jeu et peut les mettre à jour et les dessiner.

- **organisation des fichiers**  
  Core/ : Contient les fonctionnalités principales
    - `GameScene.py`
    - `GameView.py`
    - `config.py`

  MapSystem/ : Contient les fonctionnalités de décodage de carte
    - `MapLoader.py`
    - `MapValidatorView.py`

  TileSystem/ : Contient les fonctionnalités permettant de créer des Tiles
    - `Tile.py`
    - `TileFactory.py`



## Semaine 4

## Semaine 5

## Semaine 6 à 9 - refactoring

## Semaine 10

## Semaine 11

## Semaine 12

## Semaine 13

## Semaine 14