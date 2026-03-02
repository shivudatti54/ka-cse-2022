java
public class TryCatchExample {
    public static void main(String[] args) {
        int a = 10;
        int b = 0;
        int result;

        try {
            // This line is likely to throw an ArithmeticException
            result = a / b;
            System.out.println("Result is: " + result); // This line won't execute if exception occurs
        }
        catch (ArithmeticException e) {
            // This block handles the specific exception
            System.out.println("Error: Cannot divide by zero!");
            // e.printStackTrace(); // Optional: to print the full exception trace
        }

        System.out.println("Program continues after try-catch.");
    }
}