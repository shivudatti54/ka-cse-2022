java
public class NestedTryDemo {
public static void main(String[] args) {
try { // Outer try block
int[] numbers = {10, 20, 30};

            try { // Inner try block
                int result = numbers[3] / 0; // This line throws an ArrayIndexOutOfBoundsException
                System.out.println("Result: " + result);
            }
            catch (ArithmeticException e) {
                System.out.println("Inner Catch: Cannot divide by zero!");
            }
            // The ArrayIndexOutOfBoundsException propagates to the outer block

            System.out.println("This line inside the outer try will not be executed.");
        }
        catch (ArrayIndexOutOfBoundsException e) { // Outer catch handles the propagated exception
            System.out.println("Outer Catch: Array index is out of bounds!");
        }
        System.out.println("Program continues normally after the outer catch.");
    }

}
