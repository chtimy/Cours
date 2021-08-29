

![TP](images\TP.png)

# TP01 - Préparation du projet

Pour ce TP, on va avoir deux projets Java distincts:

- Lab
- Javos (le nom du jeu)

Le projet Lab est déjà créé de mon côté, il faudra le synchroniser de ton côté avec l'outil Git si ce n'est pas déjà fait. Dans ce projet tu retrouveras des morceaux de code que j'aurais codés pour te donner des exemples de différents concepts. Tu y trouveras aussi des exercices à faire ou des exercices corrigées.  

Pour le projet Javos, c'est à toi de créer ton propre projet. Il faudra créer un repo avec git et pousser le repo sur le serveur Github afin que je puisse suivre ton travail. C'est dans ce projet que tu vas travailler à travers tout une série de TP qui va te développer pas à pas le jeu Javos. 

> Notes : Si jamais tu ne sais pas encore te servir de git, une fiche sera bientôt disponible sur l'utilisation de l'outil Git.

# TP01 - Création de notre première classe

Dans **Javos**, chaque personnage, chaque objet, chaque bâtiment, **quasiment tout doit pouvoir avoir une position 2D** afin de placer les objets les uns par rapport aux autre. L'idée c'est donc de pouvoir créer une première classe définissant une position 2D et qui sera ensuite utilisée par d'autres objets. 

**Consignes**:

- Créer une nouvelle classe appelée **Position2D** (visibilité *public*)
- Ajouter deux attributs ***\_x*** et ***\_y*** de type *float*(visibilité *public*)
- Créer un **constructeur** qui prend en paramètre deux *float* qui seront ensuite affectés à *\_x* et *\_y* (visibilité *public*)
- Créer un **constructeur** qui ne prend aucun paramètre et qui définit *\_x* et *\_y* par défaut, c'est à dire la valeur 0. (visibilité *public*)
- Créer une méthode ***translate*** qui prend en entrée deux paramètres *dx* et *dy* de type *float* et qui effectue une translation sur les attributs *\_x* et *\_y* (visibilité *public*)
- Créer une méthode ***distance*** qui prend en entrée un autre objet de type Position2D et qui retourne la distance entre les deux positions (visibilité *public*)

> Rappel : La distance entre deux points est 
> $$
> \sqrt{(x'-x)^2+(y'-y)^2}
> $$
> Il faut utiliser la méthode *sqrt* de la librairie Math de java pour pouvoir calculer la racine carré d'un nombre 

Chaque nouvelle classe doit normalement être testée pour vérifier son bon fonctionnement, surtout sur les cas extrêmes. Pour le moment nous n'utilisons pas le Framework JUnit pour effectuer des tests de manière automatique, donc nous allons le faire à la main. 

**Consignes pour les Unit Tests**:

- Créer une méthode **main** dans la classe Position2D
  - Pour chaque test, il faut ajouter un court commentaire en disant ce que fait le test
  - Pour chaque test, il faut afficher si le test a réussi ou non
- **1er cas de test** : 
  - Créer un objet de type Position2D 
  - Appeler le constructeur vide
  - Vérifier que les attributs _x et _y sont bien égaux à 0
- **2nd cas de test** : 
  - Créer un objet de type Position2D 
  - Appeler le constructeur avec paramètres 
  - Vérifier que les attributs _x et _y sont bien égaux aux valeurs envoyées en entrée du constructeur
- **3ème cas de test** : 
  - Créer un objet de type Position2D avec des valeurs non nulles
  - Appeler la méthode *translate* de cet objet avec des valeurs non nulles
  -  Vérifier que les attributs _x et _y de l'objet correspondent bien aux valeurs attendues
- **4ème cas de test** : 
  - Créer un objet *p1* de type Position2D avec des valeurs non nulles
  - Créer un autre objet *p2* de type Position2D avec des valeurs non nulles
  - Appeler la méthode *distance* de p1 avec p2 en paramètre 
  -  Vérifier que la valeur retournée par la méthode correspond bien à ce qui est attendu  

# TP01 - On peut enfin placer notre héro!

Maintenant que la classe Position2D existe, on va pouvoir s'en servir pour notre nouveau héro et le déplacer où l'on veut sur la carte.

**Consignes:**

- Créer une nouvelle classe appelée **Hero** (visibilité public)
- Créer un attribut de type String  appelé ***\_name*** (visibilité *private*)
- Créer un attribut de type Position2D appelé ***\_position*** (visibilité *private*)
- Créer un **constructeur**  prenant en entrée un nom, une position et qui définit les attributs (visibilité *public*)
- Créer un **constructeur** prenant en entrée un nom et qui définit *\_name* et qui donne une position par défaut à *\_position* (position à l'origine (0,0) ) (visibilité *public*)
- Créer une méthode ***setPosition***, qui prend entrée une valeur x et y et qui redéfinit la position du héro (visibilité *public*)
- Créer une méthode ***getPosition*** qui retourne la position du héro (visibilité *public*)
- Créer une méthode ***getName*** qui retourne le nom du héro (visibilité *public*)

**Consignes pour les unit tests**:

- Créer une méthode **main** dans la classe Hero
- **1er cas de test** : 
  - Créer un objet de type Hero
  - Appeler le constructeur en envoyant un nom et une position x,y
  - Vérifier que les attributs correspondent aux paramètres d'entrée 
- **2nd cas de test** : 
  - Créer un objet de type Hero
  - Appeler le constructeur en envoyant seulement un nom 
  - Vérifier que les attributs correspondent aux paramètres d'entrée 
- **3ème cas de test** : 
  - Créer un objet de type Hero en appelant n'importe quel constructeur
  - Appeler la méthode **setPosition** avec des valeurs x et y
  - Vérifier que les attributs correspondent aux paramètres d'entrée 