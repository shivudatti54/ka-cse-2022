java
import java.util.InputMismatchException;
import java.util.Scanner;

public class ResumingExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = 0;
        boolean validInput = false;

        // The loop continues until we get valid input
        while (!validInput) {
            try {
                System.out.print("Please enter a valid integer: ");
                number = scanner.nextInt(); // This line might throw an exception
                validInput = true; // This line only executes if no exception was thrown
            } catch (InputMismatchException e) {
                System.out.println("Invalid input. That was not an integer.");
                scanner.next(); // Crucial: Clear the invalid input from the scanner buffer
            }
        }

        System.out.println("Thank you! You entered: " + number);
        scanner.close();
    }
}