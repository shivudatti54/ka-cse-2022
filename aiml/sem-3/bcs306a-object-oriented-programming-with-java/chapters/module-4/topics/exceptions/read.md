java
public class BasicException {
    public static void main(String[] args) {
        try {
            int result = 10 / 0; // This will throw an ArithmeticException
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {
            System.out.println("Error: Cannot divide by zero!");
            // e.printStackTrace(); // Uncomment to print the full stack trace
        }
        System.out.println("Program continues after the exception...");
    }
}