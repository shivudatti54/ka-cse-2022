java
public class UncaughtDemo {
public static void main(String[] args) {
System.out.println("Program started.");

        int numerator = 10;
        int denominator = 0;
        int result = numerator / denominator; // This line throws ArithmeticException

        System.out.println("Result is: " + result); // This line never executes
        System.out.println("Program ended.");       // This line never executes
    }

}
