java
// Superclass
class Vehicle {
    void start() {
        System.out.println("Vehicle is starting...");
    }
}

// Subclass inheriting from Vehicle
class Car extends Vehicle {
    // Overriding the parent's method
    @Override
    void start() {
        System.out.println("Car is starting with a key!");
    }

    // New method specific to Car
    void honk() {
        System.out.println("Beep Beep!");
    }
}