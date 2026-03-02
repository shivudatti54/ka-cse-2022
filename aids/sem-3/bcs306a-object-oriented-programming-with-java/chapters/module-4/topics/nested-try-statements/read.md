java
public class NestedTryExample {
    public static void main(String[] args) {
        try { // Outer try block
            int[] numbers = new int[5];
            
            try { // Inner try block
                String numStr = "abc";
                int num = Integer.parseInt(numStr); // This line throws NumberFormatException
                numbers[10] = num; // This line would throw ArrayIndexOutOfBoundsException
            }
            catch (NumberFormatException e) {
                System.out.println("Inner Catch: Number format error! " + e.getMessage());
            }
            // The inner catch handles the exception, so the outer try continues.

            System.out.println("Outer try continues...");
            numbers[0] = 100; // This is safe
        }
        catch (ArrayIndexOutOfBoundsException e) { // Outer catch block
            System.out.println("Outer Catch: Array index is out of bounds! " + e.getMessage());
        }
        catch (Exception e) { // General outer catch block
            System.out.println("Outer Catch: A general exception occurred.");
        }
        System.out.println("Program continues after try-catch.");
    }
}