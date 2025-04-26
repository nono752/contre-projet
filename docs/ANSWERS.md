# Reponses

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
Pas de questions

## Semaine 3
### Conception fichier  
La lecture du fichier est séparé en trois parties chacun ayant une responsabilité:
  1. Récupération du fichier dans une structure spécifique.
  2. Vérification de ce qui a été récupéré.
  3. Chargement des objets du jeu à partir de la structure vérifiée.

Ainsi les tests sont simples un fichier test par responsabilité.

### Tests
Dans chaque dossier test, on a des cartes spécifiques pour chacun des tests.
En chargeant la bonne carte, on peut garder les tests déjà présents et en ajouter sans difficultés.

### Lave
La lave est plus proche des pieces. 
Ce sont tous deux des objets statiques avec lesquels le joueur peut interagir.

### Blob  
- Pour détecter chute ou lave  
  Selon la direction du blob signe de `change_x` on place un petit `SpriteSolidColor` sur le bord droit ou gauche du blob `blob.right + 1`et
  a hauteur `blob.bottom - 1`. On peut vérifier comme cela si lors du déplacement suivant le bord sera au dessus d'un `WALL`.
  La vérification se fait avec `arcade.check_collision_list`.
  S'il n'y a plus de sols `change_x *= -1`.

- Pour détecter obstacles latéraux
  C'est une simple détection de collision entre le blob et les autres blobs et les WALL.
