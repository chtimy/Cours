![POO_title](Images\POO_title.png)

# Introduction à la POO

La POO (Programmation Orientée Objet) ou OOP en anglais (Object-Oriented Programming) est un paradigme de programmation aujourd'hui bien connu et très utilisé. On en trouve dans ne nombreux domaines comme l'animation, le  jeux-vidéo, du cinéma, la banque, la sécurité, le web, partout!

> <img src="Images\question_guy.png" alt="question_guy" style="zoom:33%;" /> Mais attends, d'abord c'est quoi la programmation et qu'est-ce que çà veut dire orienté objet?

**La programmation** c'est effectivement un bien grand mot pour désigner quelqu'un qui va écrire des instructions à une machine pour que cette dernière les exécute. Il existe une grande panoplie de langages permettant de communiquer avec la machine, tous, avec un niveau d'abstraction plus ou moins élevé. Si on veut être très proche de la machine comme le langage assembleur, on peut demander à la machine de faire des opérations les plus simples possibles en lui disant de faire une addition, une soustraction, de stocker une valeur dans un registre (mémoire très rapide d'un processeur), etc... Mais ces langages sont de moins en moins utilisés, car on a beaucoup évolué depuis l'émergence de l'informatique et des langages de programmation à beaucoup plus haut niveau d'abstraction nous permettent de faire des choses bien plus intéressantes en beaucoup moins de temps. Va programmer un jeu comme Mario Galaxy en disant à la machine "Alors d'abord additionnes-moi ces deux nombres s'il te plaît, ensuite quand tu auras fini, tu me stockeras le résultat dans ce registre pour faire après une soustraction, etc ...".  Evidemment, ce n'est plus possible et heureusement, une multitude de langages existent aujourd'hui en partant de langages génériques comme le langage C, Python, Java à des langages accessibles aux plus débutants voire même pour des très jeunes comme Scratch (exemple ci-dessous), Livecode et j'en passe. 

<img src="Images\scratch.PNG" style="zoom:20%;" />



> <img src="Images\question_guy.png" alt="question_guy" style="zoom:33%;" />  Ok, et pour l'orientée objet?

**Orientée objet** est un paradigme de programmation qui a émergé dans les années 80. L'idée est de fabriquer ton programme en découpant ton code en petits morceaux de codes appelés des objets qui intéragissent entre eux. On va voir que c'est un concept au final très intuitif, et facile à enseigner si on commence par les bonnes ficelles. En plus de cela c'est un paradigme est décorrélé de n'importe quel langage, on peut parler, écrire, chanter (tout ce que vous voulez)  de la POO sans toucher à un seul langage de programmation. Il paraît même que dans un futur proche on pourra programmer sans écrire une seule ligne de code avec un outil de modélisation très puissant appelé UML (*Unified Modeling Language*) où on modélise nos objets, leur comportement et leurs intéractions avec les autres. Voici un exemple ci-dessous. On reviendra sur ce langage dans une autre fiche de cours, si jamais çà t'intéresse.  

<img src="Images\uml.png" style="zoom:55%;" />

# Tout est objet

> <img src="Images\question_guy.png" alt="question_guy" style="zoom:33%;" />  Bon c'est très bien tout çà, mais c'est quoi un objet concrètement?

Patience, on y arrive! Pour expliquer un peu plus en détail ce qu'est un objet, on prend l'exemple d'un beau squelette guerrier ci-dessous. Il a l'air de porter beaucoup de choses sur lui qui pourraient facilement être décrits. 

> <img src="Images\exercise.png" alt="exercise" style="zoom:50%;" />
>
> Et pour la peine, je vais te faire travailler un peu. Peux-tu me faire la liste de tous les objets que tu voies sur l'image et le possible lien qu'ils ont entre eux?

<img src="Images\squeleton.png" alt="squeleton" style="zoom:25%;" />

<details>
<summary>Proposition de correction</summary>
<p>
    Sur ce squelette on peut voir comme objet :
    <ul>
    <li>un casque</li>
    <li>des épaulettes</li>
    <li>une épée</li>
    <li>un bouclier</li>
    <li>des bottes</li>
    <li>un pagne</li>
    <li>un plastron</li>
    </ul>
</p>
<p>
    Mais ce n'est pas tout. Le squelette lui-même est un objet (sans lui faire offense). D'ailleurs on peut tout de suite dire que l'objet squelette est en lien avec tous les équipements précédemment cités puisqu'il les porte. Par contre, on voit bien que l'épée et le bouclier n'ont pas de lien entre eux. Je peux tout à fait enlever l'épée, le bouclier va très bien se porter sans lui et inversement.
</p>
<p>
    On pourrait aller encore plus loin en décomposant le casque par exemple. Il a un casque composé de deux cornes et de je ne sais pas combien de petites pics. Il a une épaulette constituée elle aussi de petites pics. Il a un bouclier comportant une poignée, et surement un motif sur le devant. Et pourquoi pas même dire que les bottes sont composées d'un cuir de qualité qu'on pourrait changer en fer ou en tissus en fonction des besoins du joueur. On peut continuer et dire que la matière du cuir elle-même contient un alliage de matières premières qui elles-même contiennent des molécules (dont je ne connais pas les noms) et qui elles-même contiennent des atomes! Bon je vais m'arrêter là, de toute façon je n'avais plus d'idée.
</p>
<p>
     On voit bien que la description peut aller très loin et donc c'est à toi de décider jusqu'à où tu veux t'arrêter. Dans un jeu de combat, savoir que les bottes sont en cuir, en fer ou en tissus pour calculer des points de défense est amplement suffisant, on se fiche complètement d'en savoir plus.
</p>
</details>

On a fait la liste d'objets et des liens qu'ils ont entre eux (un objet casque contient un objet corne par exemple), ce qui est très bien jusqu'ici, mais pas suffisant pour commencer à programmer quoi que ce soit. Le squelette doit pouvoir, en plus de porter des objets, intéragir avec chacun de ses objets. Par exemple, il doit être capable de découper son adversaire grâce à son épée! **Et là on vient de mettre l'accent sur un deuxième point très important à propos des objets, ils peuvent effectuer des actions**. Mon objet squelette pourrait réaliser une action "attaquer" qui se déroulerait de la manière suivante:

```
Action attaquer :
	Est-ce que j'ai une épée?
	Oui : 
		Je réalise un coup vers l'avant avec mon épée
		Est-ce qu'un ennemi est à ma portée?
		Oui :
			Je lui enlève 5 points de vie grâce à la qualité de mon épée + 5 points de vie
			grâce à la caractéristique force du squelette
		Non : 
			Affiche "Manqué"
	Non :
		Affiche "Pas d'arme"
```

On voit dans cet algorithme, qu'on vérifie d'abord si le squelette a un objet de type épée sur lui, ensuite on vérifie si un ennemi est à proximité et enfin on enlève des points de vie en fonction des caractéristiques de l'épée et du squelette. Je vous donne un petit aperçu de cet algorithme en Java, mais fais attention il n'est pas complet!

**<u>Java :</u>**

```java
void Squelette::attack(Enemi [] enemis) {
    // Est-ce que j'ai une épée?
    if(_sword != null)
    {
        // Je réalise un coup vers l'avant avec mon épée
        attack_animation();
        // Est-ce qu'un ennemi est à ma portée?
        for(Enemi enemi in enemis) {
            if(_position.distance_to(enemi.get_position()) < _range_attack) {
                // Je lui enlève 5 points de vie grâce à la qualité de mon épée + 5 points de vie grâce à la caractéristique force du squelette
                enemi.hurt(_sword.getDamage() + _strength.convertToDamage());
            }
            else {
                System.out.println("Missed");
            }
        }
    }
    else {
		System.out.println("No weapon");
    }
}
```

Si tu ne comprends pas tout le code, c'est normal, c'est justement le but du cours que de t'apporter toutes les réponses dont tu as besoin, donc ne t'inquiètes pas! 

Je pense que l'on a fait un petit tour de ce qu'est un objet. On verra que d'autres notions sont utiles comme les constructeurs  qui permettent de construire un objet, mais laissons çà de côté pour le moment.

# Les langages qui font/sont de la POO

On peut citer les langages les plus connus qui permettent de faire la POO comme:

- Java
- C++
- C#
- Python
- PHP
- JavaScript
- Scala
- ...

Dans ce cours, on ne s'intéressera qu'à Java qui est entièrement conçu pour la POO. Quand je dis entièrement, c'est qu'il est impossible d'écrire en java des choses qui ne seront pas des objets.

> <img src="Images\question_guy.png" alt="question_guy" style="zoom:33%;" />  Ah d'accord, pourquoi apprendre le java et pas un autre langage du coup?

Et je te répondrais que pourquoi pas Java plutôt qu'un autre langage? Non bien évidemment je vais donner certains arguments qui font que Java est un très bon langage pour ceux qui souhaitent commencer la programmation. Il faut savoir que Java est utilisé très abondamment aujourd'hui, je pense notamment au jeu Minecraft, qui a l'origine, a tout été codé en Java; à l'outil MATLAB qui est en Java (un outil pour faire plein de choses compliquées en mathématiques); mais aussi dans nos smartphones Android où Java est utilisé un peu partout. 

Je vais donner 3 gros atouts qui, je l'espère, vont te convaincre que Java, c'est pas de la menthe à l'eau! 

- Comme on a dit, **Java est pensé POO**, donc il permet de faire les choses bien dès le départ. On ne peut pas programmer n'importe comment, il y a des règles à respecter, ce qui permet d'être rigoureux dans la programmation.
- Java, contrairement au C++ par exemple **propose de gérer toute la mémoire pour toi**. Tu n'as pas besoin de t'embêter à demander à la mémoire : "Peux tu me réserver tant de place pour que je créé cet objet. Ah au fait t'oubliera pas de le supprimer à ce moment là quand j'en aurai plus besoin?". Ce qui est appréciable et surtout permet de beaucoup stabiliser les logiciels. 
- Un programme en Java **peut être executé sur n'importe quelle machine** (ordinateur, carte embarquée, téléphone, ...) ayant une machine virtuelle Java. Ce sera l'objet de la fiche "Java, la compilation, l'interprétation et l'exécution". On peut déjà dire que Java compile du code intermédiaire qui est ensuite interprétée ensuite par la machine virtuelle qui va produire du code natif à la machine (natif signifie ici, un langage propre à l'architecture du processeur).

J'aurais un argument bonus, Java a une petite mascotte! Et oui, regardez comme elle est (pas) mignonne.

<img src="Images\java.png" alt="java" style="zoom:5%;" />

# Les 3 piliers de la POO

La POO s'appuie sur 3 grands principes :

- **Encapsulation**
- **Héritage**
- **Polymorphisme**

<u>Encapsulation:</u> C'est le fait de cloisonner des données/objets dans un objet et de ne laisser aucun autre objet venir les modifier. La responsabilité est entièrement donné à l'objet afin qu'il gère ses propres données.

<img src="Images\encapsulation.png" alt="encapsulation" style="zoom:70%;" />

<u>Héritage</u> : Si une souris est un animal et qu'un éléphant est un animal, alors une souris est un éléphant? Hmm pas tout à fait mais on a quelque chose! Un éléphant n'est pas une souris et inversement, par contre les deux ont bien çà en commun, c'est que ce sont des animaux. On sait qu'un animal doit manger et dormir pour continuer à vivre, on sait aussi qu'un animal a un poids et une taille. Par contre, un éléphant a des défenses, ce que n'a pas la souris, inversement, la souris à des moustaches que n'a pas l'éléphant. En POO, on est tout a fait capable de modéliser une telle situation en créant un type d'objet "Animal" et deux autres types d'objet "Elephant" et "Souris" qui vont hériter des attributs et actions du type d'objet "Animal". Le shéma ci-dessous illustre l'exemple, au passage on montre avec ce shéma des bribes de ce qu'est un shéma UML.

<img src="Images\moyen_locomotion.png" alt="moyen_locomotion" style="zoom:50%;" />

> <img src="Images\question_guy.png" alt="question_guy" style="zoom:33%;" />  Hey! Pourquoi manger et dormir se trouvent dans tous les types d'objet ? Ouah je comprend plus!

Oui, bien sûr, c'est normal. Tu mets le point sur un autre grand concept qui est le polymorphisme. Et comme par hasard, c'est le point suivant!

<u>Polymorphisme:</u> 

Intuitivement, et j'espère que tu es d'accord, un éléphant ne mange pas de la même façon qu'une souris que ce soit en quantité qu'en variété de nourriture. Donc l'action manger sera différent pour les deux animaux souris et éléphant. L'idée est donc d'écrire un morceau de code différent de l'action manger pour la souris et pour l'élephant. Dans le cas plus général du type Animal, on pourrait écrire un troisième bout de code qui serait commune à tous les animaux, mais parfois ce n'est pas possible, on laissera donc vide en indiquant que l'action manger n'est décrite que dans les classes plus spécifiques comme Souris ou Elephant. Maintenant, imaginons que nous souhaitons donner à manger à l'ensemble des animaux d'un parc naturel.

> <img src="Images\question_guy.png" alt="question_guy" style="zoom:33%;" />  Mais attends, donner à manger aux souris dans un parc na...

Chuuuut, imagines, imagines! Fais un effort. 

On ne veut pas s'embêter à savoir à quel est le type d'animal on a à faire, on veut simplement qu'il mange comme tous les autres. On pourrait donc gérer une collection d'animaux et appeler l'action "manger()" pour chaque animal. 

> <img src="Images\question_guy.png" alt="question_guy" style="zoom:33%;" />  Et du coup, comment on sait que c'est l'action manger de éléphant ou souris qui est réalisée?

Et bien, c'est tout simplement le programme qui décidera au moment de l'exécution si l'objet de type Animal est plus spécifiquement un éléphant ou une souris et appeler l'action manger de l'un ou l'autre en conséquence. Voilà un shéma un peu plus visuel ci-dessous.

<img src="Images\POLYMORPHISME.png" alt="POLYMORPHISME" style="zoom: 50%;" />

Evidemment, en si peu de lignes ces 3 concepts peuvent paraître encore obscur, mais ils font l'objet d'une fiche de cours chacun, et je donnerai plein d'exemples pour être sûr que tu saisisses tout.

# Résumé

- La programmation est le fait d'écriture des instructions à la machine pour qu'elle les exécute
- La POO est un paradigme de programmation où tout est considéré comme objet
- Chaque objet peut contenir d'autres objets, mais aussi des actions. On verra que ces termes ne sont pas tout à fait ceux empruntés à la POO. 
- Java est un langage propre à la POO, tout commence par l'écriture d'un type d'objet
- Les trois principaux principes de la POO sont l'encapsulation, l'héritage et le polymorphisme