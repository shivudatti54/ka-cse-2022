java
public class LiteralsDemo {
    public static void main(String[] args) {
        // Integer Literals
        int decimal = 99;
        long bigNumber = 9999999999L; // Note the 'L'
        int hex = 0xFace; // Hexadecimal
        int binary = 0b1101; // Binary

        // Floating-Point Literals
        float pi = 3.14F; // Note the 'F'
        double scientific = 1.234e-5; // Scientific notation

        // Character and String Literals
        char letter = 'J';
        char escape = '\t'; // Tab character
        String greeting = "Hello, World!\n";

        // Boolean Literal
        boolean isJavaFun = true;

        // Null Literal
        String emptyString = null;

        System.out.println(greeting + "Is Java fun? " + isJavaFun);
    }
}