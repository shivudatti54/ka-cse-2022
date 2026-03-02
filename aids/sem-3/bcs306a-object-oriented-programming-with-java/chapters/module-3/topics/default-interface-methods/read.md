java
public interface Vehicle {
    // Traditional abstract method
    void start();

    // Default method with an implementation
    default void honk() {
        System.out.println("Beep Beep!");
    }
}