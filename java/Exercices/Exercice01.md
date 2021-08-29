# Exercice 01 : Les premières bases dans java

## 1. Compiler son premier code java

Copier le morceau de code ci-dessous dans un nouveau fichier appelé "*HelloWorld.java*".

```java
public class HelloWorld
{
     public static void main(String []args)
     {
        System.out.println("Hello World");
     }
}
```

Ce code, très classique permet d'afficher à l'écran la chaîne de caractères "Hello World". Les mots clé "public", "class", "static" seront vu dans les cours suivants. Ce qu'il faut retenir ici, c'est que l'on souhaite créer un point d'entrée du programme grâce à la fonction *main*. Cette fonction spéciale est encapsulée dans la classe *HelloWorld*.

Il faut maintenant compiler ce code dans un langage intermédiaire seulement interprétable par une machine virtuelle java. Lorsqu'on veut exécuter un programme java sur son ordinateur, il faut toujours installer un environnement java incluant une machine virtuelle.

Pour compiler ce code, il faut lancer un terminal, se déplacer dans le dossier où se trouve le fichier source "*HelloWorld.java*" et lancer la commande suivante:

```bash
javac HelloWorld.java
```

Cette commande va créer un fichier appelé *HelloWorld.class* qui contient le langage interprétable java. Il ne reste plus qu'à exécuter la commande ci-dessous pour interpréter le code et l'exécuter:

```bash
java HelloWorld
```

On remarque ici que l'on écrit pas le suffixe *.class* car la commande n'a besoin que tu nom du fichier et sait ensuite quel fichier *.class* exécuter.

On doit normalement obtenir aucune erreur et voir le résultat s'afficher.

## 2. Calculatrice

On souhaite écrire une calculatrice permettant d'additionner, de soustraire, de multiplier et de diviser deux nombres en fonction de ce que demande l'utilisateur dans la console. Par exemple, je souhaite taper : 3+6
Le programme doit alors immédiatement me donner le résultat 9.

### 2.1 Ecrire les opérations

a. Ecrire une fonction "addition" dans la classe *HelloWorld* qui prend en entrée deux paramètres de type flottant et qui retourne le résultat de l'addition de ces deux nombres.

b. Faire de même avec les opération "soustraction", "multiplication" et "division".

c. Ecrire dans la fonction main un code qui teste chacune des 4 fonctions avec deux nombres. Vérifier que le résultat est bien celui attendu.

### 2.2 Lire et interpréter les inputs de l'utilisateur

a. Lire l'input de l'utilisateur en plaçant le contenu dans une chaine de caractères. Afficher la chaine dans le terminal pour vérifier que la lecture s'est bien réalisée.

b. Ecrire une fonction ***compute*** qui prend en entrée un chaine de caractères et qui retourne le résultat de l'opération c'est à dire un entier.
	b.1. Ecrire la première partie de la fonction qui va accéder à chaque caractère et qui va découper la chaine OPERANDE OPERATEUR OPERANDE. OPERANDE est un entier constitué d'un ou plusieurs chiffres. OPERATEUR peut être "+", "-", "/", "\*". 

> Une chaine de caractères "String" encapsule un tableau de caractères qui sont accessibles via la fonction ***charAt(int index)***.

​	b.2. Appeler la bonne fonction pour calculer le résultat à partir des OPERANDES et de l'OPERATEUR.

​	b.3. Retourner le résultat et l'afficher dans la fonction main. 

c. Faire des tests dans la fonction main en rentrant des inputs utilisateurs et qui teste chacun des opérateurs. 