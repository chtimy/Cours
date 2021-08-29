![](Images\title.png)

# Introduction

Tu te demandes comment passer de la page blanche dans ton éditeur de code préféré à l'image ci-dessus, et bien justement tu tombes au bon endroit pour apprendre! Ce projet a pour but d'apprendre les bases du java, mais pas que, parce que l'idée c'est aussi de comprendre des notions qui touchent à la programmation en général. Je pense notamment à la programmation orientée objet (ou POO c'est plus court) , je pense à des principes fondamentaux de la programmation comme S.O.L.I.D. ou enfin des designs patterns très utiles pour répondre à certaines problématiques de la vie courante d'un programmeur. Bref, beaucoup de choses à voir. Evidemment on va le faire de manière amusante, pédagogique et beaucoup axé sur la créativité, ta créativité! Parce que oui, je vais t'aider à programmer un petit jeu vidéo, mais c'est toi qui fera le plus gros du travail en choisissant vers quoi tu veux aller au fur et à mesure de l'aventure.

Bienvenue, installes-toi, et fais chauffer ton IDE, pour lui faire manger des milliers de lignes de code (enfin on va commencer doucement).

# Présentation du projet  

Le jeu que l'on va programmer ressemble fortement au petit jeu Zelda qui fréquentait nos salons sur la Super-Nes, mais nous, nous allons le faire à notre sauce. Je propose ici quelques éléments de base et je te laisserai ensuite faire tes propres choix. 

- Dessiner et gérer notre petit héro à travers son aventure à travers un monde 2D
- Lui mettre plein d'ennemis, afin qu'il ait un peu de challenge
- Interagir avec le décor et les autres personnage pour créer une épopée formidable
- Donner au moins une quête à faire, du genre sauves ton amour de toujours des mains du grand méchant (pas très original je sais)
- Réaliser une belle interface pour qu'on ait un peu de contact avec le jeu (l'immersif c'est bien mais parfois c'est pas bien)

Créer un jeu, c'est gérer :

- un moteur de rendu
- un moteur d'évènements
- un moteur de collisions
- un moteur d'intelligence artificielle
- un moteur pour les évènements

Et on va s'arrêter là, je pense que c'est déjà pas mal pour te faire peur. Mais ne t'inquiètes pas, tout va bien se passer.

# Au cœur de ce cours

Tout au long du projet on va intégrer différentes notions qui vont être expliquées chacune par des petites fiches de cours concises et je l'espère les plus claires possibles. Le but, cher lecteur, n'est pas de te gaver d'information, mais seulement t'en donner l'essentiel pour qu'ensuite tu puisses te débrouiller par toi-même pour comprendre tout le reste. Les importantes notions que nous allons voir sont les suivantes:

- Introduction à la POO et ses 3 piliers
- Classes et Objets
- Encapsulation
- Paquetages
- Héritage
- Exceptions
- Polymorphisme
- Abstraction et Interfaces
- Collections

A côté de ce cours je te propose aussi qu'on s'intéresse à des sujets qui vont te permettre d'avoir les outils nécessaires pour mieux comprendre les différentes approches autour de la POO mais même plus globalement autour de la programmation:

- UML, les diagrammes de classe
- Le principe S.O.L.I.D.
- Les design patterns
- Les Unit Tests
- D'autres paradigmes de programmation
- Java, la compilation, l'interprétation et l'exécution

Voilà pour la *short-list*. Ces fiches sont celles, un peu obligatoire pour bien comprendre les grandes lignes. Evidemment, afin d'améliorer ce cours et de l'enrichir, n'hésites pas à proposer des topics sur lesquels tu n'es pas à l'aise et qui mérite une fiche de cours, je suis preneur!

Avant que tu ne te jettes sur le contenu du cours, nous devons d'abord discuter des outils utilisés afin d'être le plus confortable possible pour la suite.

# Outils

- **CodeShare** est un outil pour partager du code. On s'en servira pour interagir ensemble sur un morceau de code. Ca me permet de t'aider lorsque tu es bloqué, mais aussi de te proposer des morceaux de code pour te faciliter la vie dans certains cas.
- **Git** est un outil de versionnage. Afin que je puisse avoir exactement le même projet que tu es en train de développer, c'est important de pouvoir se synchroniser au niveau du code. Je dois pouvoir le compiler et exécuter comme tu le ferais chez toi. On évitera de se passer des fichiers en durs par mail. En plus un outil git bien utilisé, c'est un développeur bien organisé.
- **GitHub** est un service en ligne permettant de stocker des répertoires de code et qui peut se synchroniser avec l'outil git justement. C'est sur cette plateforme que l'on va mettre ton projet de code.
- Pour **l'IDE**, c'est toi qui choisi. Il en existe des plus ou moins complets comme par exemple Intellij IDEA ou Eclipse qui ont un bon debugger, des snippets pour le code, des outils d'auto-complétions très sympas. Si tu préfères des outils plus proches du couteau et du silex, il existe Sublime Text (que j'utilise très souvent!), Notepad, voire même le bloc-note! Evidemment j'en oublie plein. Choisis celui qui te convient le mieux.
- Pour les **QCM** entre les cours, j'utilise généralement l'outil proposé par Framasoft. Mais parfois çà ne fonctionne pas, donc on avisera.

Nous voilà enfin prêt pour attaquer le JAVA!

<img src="Images\attack.png" alt="attack" style="zoom:100%;" />