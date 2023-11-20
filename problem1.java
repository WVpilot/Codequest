import java.io.File;
import java.util.Scanner;

public class problem1 
{
    public static void main(String[] args) 
    {
        try
        {    
            File inFile = new File("src/input.txt");
            Scanner input = new Scanner(inFile);
            
            String tIn = "";
            int cases = input.nextInt();
            input.nextLine();
            for (int i = 0; i < cases; i++)
            {
                tIn = input.nextLine();
                System.out.println(processString(tIn));
            }

            input.close();
        }

        catch (Exception err)
        {
            System.out.println(err);
        }
    }

    public static String processString(String in)
    {
        String out = "";

        for (int i = 0; i < in.length(); i++)
        {
            if (in.charAt(i) == 'a' || in.charAt(i) == 'e' || in.charAt(i) == 'i' || in.charAt(i) == 'o' || in.charAt(i) == 'u')
            {
                i++;
                out += in.substring(i, i + 1);
            }
        }

        return out;
    }
}
