java
public class PassByValueDemo {
    public static void modifyValue(int x) {
        x = x + 10; // Modifies the copy
        System.out.println("Value inside method: " + x); // Output: 20
    }

    public static void main(String[] args) {
        int num = 10;
        System.out.println("Value before method call: " + num); // Output: 10
        modifyValue(num); // Passes the value 10 (a copy)
        System.out.println("Value after method call: " + num); // Output: 10 (unchanged)
    }
}