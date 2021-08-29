public class LoopExample
{
     public static void main(String []args)
     {
        // Boucle for
        // 1er : Initialisation de la boucle 
        //      => ici la variable i est init à 0
        // 2nd : Condition vérifiée à chaque début de boucle pour rester dans la boucle 
        //      => On en sort pas tant que la variable i < 20
        // 3ème : Instruction exécuté à chaque fin de tour de boucle
        //      => Ici la variable i est incrémenté de 1 à chaque tour de boucle
        for(int i = 0 ; i < 20 ;  i++)
        {
            System.out.println(i);
        }
     }
}