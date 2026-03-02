java
public class PrimitiveExample {
    public static void modifyValue(int x) {
        x = x + 10; // Modifies the copy
        System.out.println("Inside method: " + x); // Output: 15
    }

    public static void main(String[] args) {
        int originalValue = 5;
        modifyValue(originalValue);
        System.out.println("Outside method: " + originalValue); // Output: 5
    }
}