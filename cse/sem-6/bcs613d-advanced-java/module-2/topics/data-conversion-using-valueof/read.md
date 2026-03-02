java
public class ValueOfDemo {
public static void main(String[] args) {
// Converting a String to an Integer object
String numberStr = "456";
Integer intObj = Integer.valueOf(numberStr);
System.out.println("Integer Object: " + intObj); // Output: 456

// Demonstrating the radix parameter (parsing a binary string)
String binaryStr = "1111";
Integer fromBinary = Integer.valueOf(binaryStr, 2); // Base 2 (binary)
System.out.println("Value of binary '1111': " + fromBinary); // Output: 15
}

}
