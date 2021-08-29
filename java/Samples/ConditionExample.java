public class ConditionExample
{
     public static void main(String []args)
     {
        // if
        String vehicle = "Velo";

        System.out.println("Mon vehicle est un : " + vehicle);

        if(vehicle == "Velo")
        {
            System.out.println("C'est parti pour le tour de france!");
        }

        // if - else
        vehicle = "Moto";

        System.out.println("Mon vehicle est un : " + vehicle);

        if(vehicle == "Velo")
        {
            System.out.println("C'est parti pour le tout de france!");
        }
        else
        {
            System.out.println("Hey, mais vous voulez tricher?");
        }


        //if - if else - else
        vehicle = "Helicoptere";

        System.out.println("Mon vehicle est un : " + vehicle);

        if(vehicle == "Velo")
        {
            System.out.println("C'est parti pour le tout de france!");
        }
        else if(vehicle == "Moto")
        {
            System.out.println("C'est pour tricher ou pour filmer la course?");
        }
        else if(vehicle == "Helicoptere")
        {
            System.out.println("Ok, c'est seulement pour filmer depuis la haut je suppose?");
        }
        else
        {
            System.out.println("Hey, mais vous voulez tricher?");
        }
     }
}