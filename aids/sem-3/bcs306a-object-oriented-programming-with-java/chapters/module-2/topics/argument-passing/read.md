java
public class PrimitivePassDemo {
    public static void modifyValue(int number) {
        number = number * 2; // Modifies the copy
        System.out.println("Inside method, number is: " + number); // Output: 20
    }

    public static void main(String[] args) {
        int originalValue = 10;
        System.out.println("Before method call: " + originalValue); // Output: 10
        modifyValue(originalValue); // Passes a copy of the value 10
        System.out.println("After method call: " + originalValue); // Output: 10 (unchanged)
    }
}