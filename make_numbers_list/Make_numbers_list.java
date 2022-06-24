/*
 * Creates a text file "inventory.txt" in an existing folder "inventory" in
 * the user's home directory if this file does not already exist and fills it
 * with numbers "1:", "2:", ..., "10:", each separated by two newlines.
 */
import java.util.Scanner;
import java.io.File;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class Make_numbers_list {

    public static void main(String... args) throws IOException{
        String user_file_path = System.getProperty("user.home");
        String dirname = "inventory";
        String filename = "inventory.txt";
        String absolute_filename = user_file_path + File.separator + dirname + File.separator + filename;
        int number = 10;
        
        File inv_file = new File(absolute_filename);
        if(inv_file.exists() && inv_file.isFile()) {
            System.out.print("The file " + absolute_filename + " already exists. Do you want to override it [y|n]?");
            char answer = new Scanner(System.in).next().charAt(0);
            if(answer != 'y' && answer != 'Y')
                return;
        }
        
        new FileWriter(absolute_filename, false).close();
        BufferedWriter out = null;
            out = new BufferedWriter(new FileWriter(absolute_filename, true));
            out.write("\n");
            for(int i = 1; i <= number; i++)
                out.write(i + ":\n\n\n");
        if(out != null)
            out.close();
    }
}
