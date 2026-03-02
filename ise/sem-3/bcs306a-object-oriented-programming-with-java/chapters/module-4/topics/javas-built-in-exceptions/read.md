java
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

    public class CheckedExample {
        public static void main(String[] args) {
            try {
                File file = new File("nonexistentfile.txt");
                Scanner scanner = new Scanner(file); // This line may throw FileNotFoundException
            } catch (FileNotFoundException e) {
                System.out.println("Error: The file was not found.");
                System.out.println(e.getMessage());
            }
        }
    }
