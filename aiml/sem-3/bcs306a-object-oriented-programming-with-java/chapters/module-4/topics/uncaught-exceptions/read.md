java
public class UncaughtDemo {

    public static void main(String[] args) {
        System.out.println("Start of main()");
        methodA(); // Method A is called from main
        System.out.println("End of main()"); // This line will NOT execute
    }

    static void methodA() {
        System.out.println("Start of methodA()");
        methodB(); // Method B is called from A
        System.out.println("End of methodA()"); // This line will NOT execute
    }

    static void methodB() {
        System.out.println("Start of methodB()");
        int result = 10 / 0; // This line throws an ArithmeticException
        System.out.println("End of methodB()"); // This line will NOT execute
    }
}