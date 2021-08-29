import java.util.Scanner;  // Import the Scanner class
public class ScannerExample
{
     public static void main(String []args)
     {
        Scanner myObj = new Scanner(System.in);
        System.out.println("Enter username");
        String userName = myObj.nextLine();  // Read user input
        System.out.println("Your name is : " + userName);
     }
}