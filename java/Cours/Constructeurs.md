Constructeur par défaut

Constructeur pas chainage

Constructeur par héritage

...



```java
1  public class Feuille
2  {
3      // Constructeur
4      public Feuille(int taille, float poids, Couleur couleur, Position3D position) {
5          this.taille = taille;
6          this.poids = poids;
7          this.couleur = couleur;
8          this.position = position;
9      }
10     // Attributs
11     public int taille;
12     public float poids;
13     public Couleur couleur;
14     public Position3D position;
15     
16     // Méthodes
17     public afficher() {}
18     public tomber() {}      
19 }
```

D'ailleurs pour construire tous ces objets, tu as remarqué la présence d'un constructeur:

```java
3      // Constructeur
4      public Feuille(int taille, float poids, Couleur couleur, Position3D position) {
5          this.taille = taille;
6          this.poids = poids;
7          this.couleur = couleur;
8          this.position = position;
9      }
```

C'est une méthode de classe un peu particulière, puisque l'action qu'elle propose c'est de construire un objet. Si tu n'es pas familier avec ce qu'est une méthode, ou communément appelée une fonction, ce n'est pas bien grave, c'est l'objet de la fiche "Variables et fonctions" que tu pourras lire à la suite de cette fiche. On a pas besoin de comprendre exactement cette méthode, seulement de savoir qu'elle existe et qu'elle nous permet d'obtenir un objet avec des paramètres à lui donner. On voit par ailleurs le mot clé *public* qui signifie que la méthode du constructeur peut être appelée par n'importe qui dans le code (fiche "Visibilité").