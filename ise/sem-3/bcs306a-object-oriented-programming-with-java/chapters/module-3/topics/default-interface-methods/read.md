java
public interface Vehicle {
// Traditional abstract method
void start();

    // Default method (new in Java 8)
    default void honk() {
        System.out.println("Vehicle is honking!");
    }

}
