java
public class UncaughtExample1 {
    public static void main(String[] args) {
        int numerator = 10;
        int denominator = 0;
        int result = numerator / denominator; // This line throws ArithmeticException
        System.out.println("Result: " + result);
    }
}