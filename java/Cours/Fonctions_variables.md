# Les variables

Durant la programmation, il est nécessaire de stocker des valeurs de différentes formes dans la mémoire afin de pouvoir les exploiter plus loin dans le code.

On peut catégoriser les variables en deux parties:

- les variables de type primitif ou *built-in types*
- les variables de type non primitif

## Types primitifs

Les types primitives sont des valeurs qui peuvent être écrites à même le code et qui sont directement interprétables par le langage de programmation. Un exemple avec un type primitif entier:

```java
int value = 5; // La valeur "5" est interprété par java comme un entier
```

En java, mais aussi communément dans de nombreux autres langages, il existe différentes catégories de types de variables que l'on peut rencontrer comme :

- Les **entiers**:

```java
byte value = 55; // (number, 1 byte) entre [-128, 127]
```

```java
short value = -15043; // (number, 2 bytes) entre [-32 768, 32 767]
```

```java
int value = 2e12; // (number, 4 bytes) entre [-2^31, 2^31-1]
```

```java
long value = -2e55; // (number, 8 bytes) entre [-2^63, 2^63-1]
```

- Les **flottants**:

```java
float value = 67.54543f; // (float number, 4 bytes) 
```

```java
double value = -9.439075473568486 // (float number, 8 bytes)
```

- Les **caractères** (pouvant être considéré comme un nombre strictement positif):

```java
char value = 't'; // (a character, 2 bytes) entre [0 , 65 535]
```

- Les **booléens:**

```java
boolean value = false;
```

## Conversion des types primitifs

Si on le souhaite on peut passer d'un type primitif à un autre, mais certaines règles sont à respecter pour éviter de se faire attraper par le compilateur. Par exemple, il n'est pas possible de transformer une valeur de type ``int`` en une valeur de type ``short`` puisqu'il existe un risque d'une perte d'information lors de la transformation. C'est comme essayer de mettre à l'intérieur d'une petit boite une plus grosse boite, çà rentre pas.

```java
int a = 5;
short b = a; // error: incompatible types: possible lossy conversion from int to short
```

Si on est vraiment sûr de ce que l'on fait et qu'on assume une perte de précision, il faut indiquer au compilateur qu'on force la transformation du type vers un autre quelque soit les conséquences. Ce type d'opération porte le nom de **cast**. Pour corriger l'exemple précédent, il faut donc caster la valeur de type `int` en type short avant de l'assigner à une valeur de type ``short``.

```java
int a = 5;
short b = (short)a;
```

A l'inverse, le cast dans l'autre sens n'est pas nécessaire puisque stocker une valeur de type `short` dans une variable de type `int` n'est pas un problème parce qu'il n'existe aucune perte d'information. Mettre une petite boite dans une plus grande boite devrait largement rentrer.

```java
short a = 5;
int b = a;
```

Cette règle s'applique également pour toutes les catégories.

> <img src="Images/question_guy.png" alt="question_guy" style="zoom:33%;" />Que se passe t-il lorsqu'on affecte un type d'une catégorie à un autre type d'une autre catégorie? 

Pour répondre à cette question, rien de mieux que d'expérimenter!

Essayons d'un entier vers un flottant.

```java
int a = 5;
float b = a; // L'exécution se passe bien
```

Ici, un entier peut tout à fait être considéré comme un flottant sans perte d'information (presque, ce ne fonctionne pas parfaitement pour des grands nombres). Voyons voir maintenant dans l'autre sens.

```java
float a = 3.5f;
int b = a; // error: incompatible types: possible lossy conversion from float to int
```

En effet, ici la conversion entrainerait une perte d'information, notamment toute la partie après la virgule du nombre flottant, puisque qu'un type `int` ne peut contenir que des nombres entiers.

> <img src="Images/question_guy.png" alt="question_guy" style="zoom:33%;" />Et si je force le *cast*, est-ce que çà fonctionne.

Voyons voir le résultat tout de suite.

```java
float a = 3.5;
int b = (int)a;
System.out.println(b); // Affiche 3
```

La conversion se passe bien, mais toute la partie après la virgule a disparu de la valeur stockée dans `b`. 

Attention de ne pas confondre le *cast* d'un flottant vers un entier comme une opération d'arrondie à l'entier le plus proche. Dans ce cas, la partie après la virgule est simplement supprimé. Que ce soit 3.1, 3.5 ou encore 3.9 le résultat sera la valeur 3.

> <img src="Images\exercise.png" alt="exercise" style="zoom:50%;" />
>
> Il ne faut surtout pas hésiter à ce moment là de faire des expérimentations autour des casts pour bien comprendre le mécanisme.

## Limite des variables

Vous avez probablement entendu l'incident en 1996 du vol de la fusée Arianne 5. Si c'est pas le cas, je le résume ici en copiant effrontément le résumé de la [page française Wikipédia](https://fr.wikipedia.org/wiki/Vol_501_d%27Ariane_5) (merci la communauté):

> Le **vol 501** est le vol inaugural du lanceur européen [Ariane 5](https://fr.wikipedia.org/wiki/Ariane_5), qui a eu lieu le 4 juin 1996. Il s'est soldé par un échec, causé par un dysfonctionnement informatique (appelé aussi bug), qui vit la fusée se briser et exploser en vol seulement 36,7 secondes après le décollage.

On en a conclut que la fusée a explosée à cause d'un bug informatique (et aussi à cause de négligence). Ce bug tient du fait que ceux qui ont programmé le code du système de navigation de la fusée n'ont pas prêté suffisamment d'attention à la taille des valeurs pouvant être attribuées aux variables, et plus précisément de la valeur représentant la vitesse latérale (ou l'accélération, je n'en suis pas sûr) de la fusée. 

Le type de variable utilisé avait une taille de 8 bits, soit une valeur entre -127 et 128, ce qui s'adaptait très bien pour la fusée précédente Arianne 4 puisque sa masse et autres attributs étaient bien moins importantes que la fusée Arianne 5. 

> <img src="Images/question_guy.png" alt="question_guy" style="zoom:33%;" />Ah je vois le truc venir. La valeur de la vitesse pour la fusée Arianne 5 pouvait dépasser la valeur 255?

Exactement, et c'est justement la cause du bug qui a provoqué l'explosion de la fusée, la valeur était bien trop grande pour être stockée dans ce type de variable, il aurait fallu une plus grande taille.

Faisons l'expérience avec du code java. On va tenter de dépasser les valeurs de bornes d'un type byte qui est [-128, 127].

```java
byte value = 127;
System.out.println(value); // Affiche "127"
value += 1;
System.out.println(value); // Affiche "-128"
value -= 1;
System.out.println(value); // Affiche "127"
```

On voit que lorsque la valeur dépasse la borne, la valeur devient la valeur de la borne opposée. On voit bien ici que le résultat est complètement aberrant par rapport à ce qui est attendu. Ce dépassement de valeur est appelée en terme technique une erreur *d'overflow* de la variable et le comportement dans ce cas est propre à chaque système.

C'est pour çà qu'il est judicieux de bien choisir le type adapté à la valeur que l'on veut manipuler. Aujourd'hui la taille du type est quasi insignifiante au vu des performances des systèmes. On utilisera par exemple quasi-systématiquement des `int` pour représenter des entiers plutôt que des types `short` ou `byte`, mais il faut quand même faire attention à ces choses là.

 > <img src="Images/question_guy.png" alt="question_guy" style="zoom:33%;" />Mais je comprend pas tout à fait le lien avec le dépassement de valeurs et l'explosion de la fusée Arianne 5?

Alors oui, pour finir l'histoire. Lorsque la fusée s'est envolée, du fait de ses propriétés différentes de celle de la fusée d'Arianne 4. La variable stockant la vitesse latérale de la fusée s'est retrouvée avec des valeurs probablement négatives et le système de pilotage automatique a pu considérer que la fusée allait vers le bas au lieu d'aller vers le haut. Le système de pilotage a donc essayer de remettre la fusée à l'endroit, alors qu'elle était déjà à l'endroit, ce qui a provoqué une explosion au final.  

## Les types non primitifs



Références:

https://www.learnjavaonline.org/en/Variables_and_Types
https://fr.wikipedia.org/wiki/Vol_501_d%27Ariane_5
https://fr.wikipedia.org/wiki/Ariane_5#%C3%89checs
