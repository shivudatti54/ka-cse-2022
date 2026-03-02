java
public class CaseConversionExample {
public static void main(String[] args) {
String originalString = "Hello, World! 123";

        // Convert to uppercase
        String upperCaseString = originalString.toUpperCase();
        System.out.println("Uppercase: " + upperCaseString); // Output: "HELLO, WORLD! 123"

        // Convert to lowercase
        String lowerCaseString = originalString.toLowerCase();
        System.out.println("Lowercase: " + lowerCaseString); // Output: "hello, world! 123"

        // The original string remains unchanged (immutability)
        System.out.println("Original: " + originalString); // Output: "Hello, World! 123"
    }

}
