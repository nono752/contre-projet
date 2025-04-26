# Journal

## À faire (prochaine étape)

Mettez ici ce que vous pensez devoir être la ou les 2 prochaines étapes pour chacune/chacun.
- **Plus généralement**  
  * LOG doit être plus concis, déplacer partie sur conception dans DESIGN.
- **semaine 2**  
  * Est-ce qu'aucun test sont vraiment nécessaire pour la semaine 2 ? Si non les faire !
- **semaine 3**  
  * Est-ce que les les tests sont suffisants pour loader et validator ? Devrait-on vérifier affichage des exceptions ?  
  * peut-on faire un type special d'exception pour les cartes ?  
  * on ne vérifie pas que le width/heigth soient unsigned. Cela se verifie dans la verif de taille carte car fera forcement une erreur. OK ?  
  * Probleme mapdata est modifiable. De manière générale encapsulation est a revoir.
  * Probleme pour l'instant la carte ne peut avoir que deux sections c'est un peu du bidouillage.
  * Ce serait sympa d'ajouter des methodes __repr__ ou __str__.

  * Revoir le AIController et la logique de behavior est-ce que pawn ne devrait pas avoir un membre behavior ?
  * Peut-on généraliser le point précédent et faire des composition de system par exemple un membre interactable ?

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
### Taches
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
  1. Comment cloner et lancer.
  2. Les autres commandes uv utiles pour le projet.
  3. Le but du jeu, les mécaniques principales et les commandes.

- **Tests**  
  Pour l'instant hormis les test du tutoriel, aucun ajout ne semble nécessaire.



## Semaine 3
### Taches
* [x] Mettre le LOG à jour                                        
* [x] Mettre le ANSWER à jour                                        
* [X] Pouvoir récuperer carte depuis txt                                    
* [X] Pouvoir vérifier la carte
* [X] pouvoir lire la carte et ajouter à la scene les bon sprites
* [x] Ajout blob
* [x] Ajout lave
* [x] Séparation logique du joueur dans une classe `Player`
* [x] Récupération entrées clavier dans une classe `Controller`
* [ ] Création d'un classe Behavior générale pour les comportements
* [ ] Faire les tests de : Controllers, ControllerManager, GameObjects, Behaviors

rm voir si change structure avant de faire des tests
 
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
        path: str
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

- **Lave et Interactable**  
  La classe de base pour tous les objets du jeu est `Tile`qui est juste un sprite avec une catégorie `Category`.
  La `Lava` et les `Coin` sont tous deux sous-types de `Interactable`:
  ```python
  class Interactable(Tile):
      '''Classe de base pour les objets avec lesquels on peut interragir.'''
      def on_hit(self, pawn: Pawn) -> None: 
          '''A appeler lorsqu'il y a collision.'''
          pass
  
      def on_interact(self, pawn: Pawn) -> None:
          '''A appeler lorsqu'il y a interaction.'''
          pass
  ```
  Par exemple s'il y a collision avec joueur on peut simplement appeler `on_hit` sur tous les Interactable:
  ```python
  hit: list[Interactable] = arcade.check_for_collision_with_list(self.scene.player, self.scene.interactables)
      # Récupère actuellement les pièces touchées et tue le joueur s'il touche la lave
      for target in hit:
          target.on_hit(self.scene.player)
  ```
  La lave peut alors appeler quelque chose comme : `player.kill()` dans sa méthode on_hit.  
  Le joueur contient sa propre logique, pour l'instant lorsqu'il meurt on assigne `player.is_killed=True` et dans `gameview.update()`:
    ```python
  if self.scene.player.is_killed == True:
    # Recharge le niveau actuel
      self.setup(self.scene.current_path)
  ```

- **Blob**  
  Quant à l'organisation des entités, elle sont toutes dérivées de `Pawn` qui est un Tile.
  Création d'une classe behavior qui associe un comportement à une liste de pawn.
  le AIcontroller garde une liste des comportements les executes sur leurs cibles respectives.
  Le blob peut aussi interagir avec le joueur mais il n'hérite pas de interactable car hérite de pawn et je préfère eviter heritage multiple.
  
  Pour que le blob reste sur le sol on met un bloc à la position future de son bord droit/gazche décalé vers le bas et on verifie collision.
  les pawns ont une methode on_hit la verification de colision avec joueur se fait dans le physic manager. Comme pour la lave et les pieces
  Une collision avec le joueur lui enlève de la vie et le rend invincible pendant un temps donné et lui donne une vélocité verticale.

  j'ai pensé a faire un système de composants qui ressemblent un peu à behavior i.e. behavior serait un composant de toutes ses cibles.
  On pourrait avoir comme ca blob qui a un composant blobbehavior et un composant interactable. Voir si c'est compliqué à faire.


- **Sons**  
  Pour l'instant les sons sont contenus dans les classes qui les utilisent.
  C'est sûrement mieux de les centraliser dans un gestionnaire qui les appelle quand nécessaire.

## Semaine 4
### Taches
* [ ] Faire un système d'affichage pour score, hp, ...
* [ ] Ajouter Interactable Door
* [x] Modifier playercontroller pour pouvoir interagir
* [x] Modifier validateur pour tester nouvelle clé `next`
* [x] Modifier scene pour pouvoir changer de scene en gardant les stat du joueur
* [ ] Evenements souris
* [ ] Classe Weapon et Sword
* [ ] Tests

### LOG

## Semaine 5

## Semaine 6 à 9 - refactoring

## Semaine 10

## Semaine 11

## Semaine 12

## Semaine 13

## Semaine 14