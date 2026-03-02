java
public class NestedTryExample {
    public static void main(String[] args) {
        try { // Outer try block
            int[] numbers = new int[5]; // Array of size 5

            try { // Inner try block
                int result = numbers[5] / 0; // This will cause an exception
                System.out.println("Result: " + result);
            }
            catch (ArithmeticException e) {
                System.out.println("Inner Catch: Cannot divide by zero!");
            }
            // The inner catch handles ArithmeticException, but not ArrayIndexOutOfBounds

            System.out.println("This statement is after the inner try-catch.");
        }
        catch (ArrayIndexOutOfBoundsException e) { // Outer catch block
            System.out.println("Outer Catch: Array index is out of bounds!");
        }
        catch (Exception e) { // General outer catch block
            System.out.println("Outer Catch: Some other error occurred - " + e.getMessage());
        }
        System.out.println("Program continues normally...");
    }
}