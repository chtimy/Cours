public class StringExample
{
     public static void main(String []args)
     {
        String myString = new String("je suis une tomate, et ouai!");

        System.out.println("La chaine de caractere est : " + myString);

        System.out.println("Second caractere : " + myString.charAt(1));

        System.out.println("Affichage de toute la chaine de caracteres avec une boucle for.");
        for(int i = 0; i < myString.length(); i++)
        {
            // Attention, on utilise la fonction print et non println
            // On ne revient pas à la ligne après l'affichage du caractère
            System.out.print(myString.charAt(i));
        }
        // On revient a la ligne
        System.out.println("");
     }
}