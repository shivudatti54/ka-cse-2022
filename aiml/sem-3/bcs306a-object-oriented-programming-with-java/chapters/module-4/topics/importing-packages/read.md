java
public class FullyQualifiedExample {
    public static void main(String[] args) {
        java.util.Scanner myScanner = new java.util.Scanner(System.in); // Using FQN
        System.out.println("You entered: " + myScanner.nextLine());
    }
}