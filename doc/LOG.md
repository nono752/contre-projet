# Journal

## Progression

Format :

    * [fait/à faire] Tâche 

Ajoutez au fur et à mesure les tâches qui seront demandées chaque semaine.
Vous pouvez ajouter vos propres tâches si vous le jugez utile (p.ex. avec une décomposition plus fine).

---

## À faire (prochaine étape)

Mettez ici ce que vous pensez devoir être la ou les 2 prochaines étapes pour chacune/chacun.

* Est-ce qu'aucun test sont vraiment nécessaire pour la semaine 2 ? Si non les faire !

---

## Table
- [Semaine 2](#Semaine-2)
- [Semaine 3](#Semaine-3)

## Semaine 2
### taches
* [x] Créer le LOG.md                                                 
* [x] S'inscrire en binôme                                            
* [x] Découverte d'Arcade                                             
* [x] Meilleure gestion du clavier                                   
* [x] Meilleure gestion de la caméra                                  
* [x] `README.md` à jour, expliquant comment jouer   

### log
- **gestion calvier**  
Au lieu d'assigner directement `change_x = velocity`, on ajoute/soustrait la vitesse lors de l'appui/relachement. 
L'opposé est appliqué à la touche de déplacement en sens contraire.

Pour le saut, on utilise les methodes:
```python
def enable_multi_jump(allowed_jumps: int) -> None:
def can_jump(y_distance: float = 5) -> bool:
```
de la classe `arcade.PhysicsEnginePlatformer` pour: en fonction du nombre de saut donné savoir si le joueur peut sauter

- **gestion caméra**  
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

- **ajout readme.md**  
Ajout premiere version readme qui décrit le programme de manière générale et explique:
1. comment cloner et lancer
2. les autres commandes uv utiles pour le projet
3. le but du jeu, les mécaniques principales et les commandes

- **tests**  
Pour l'instant hormis les test du tutoriel, aucun ajout ne semble nécessaire.


### Semaine 3

### Semaine 4

### Semaine 5

### Semaine 6

### Semaine 7

### Semaine 8

### Semaine 9

### Semaine 10

### Semaine 11

### Semaine 12

### Semaine 13

### Semaine 14