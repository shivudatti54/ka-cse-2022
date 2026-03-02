java
public class ValueOfDemo {
public static void main(String[] args) {
String numberStr = "450";
String decimalStr = "98.76";

        // Converting String to Integer object
        Integer intObj = Integer.valueOf(numberStr);
        System.out.println("Integer Object: " + intObj); // Output: 450

        // Converting String to Double object
        Double doubleObj = Double.valueOf(decimalStr);
        System.out.println("Double Object: " + doubleObj); // Output: 98.76

        // Demonstrating radix (base) - Converting binary "1111" to decimal
        Integer fromBinary = Integer.valueOf("1111", 2);
        System.out.println("Binary '1111' to Decimal: " + fromBinary); // Output: 15
    }

}
