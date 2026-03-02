java
// Abstract class
abstract class Vehicle {
    // Abstract method (no body)
    public abstract void start();

    // Concrete method
    public void stop() {
        System.out.println("Vehicle stopped.");
    }
}

// Concrete subclass inheriting the abstract class
class Car extends Vehicle {
    // Providing the implementation for the abstract method
    @Override
    public void start() {
        System.out.println("Car starts with a key.");
    }
}

class Bike extends Vehicle {
    @Override
    public void start() {
        System.out.println("Bike starts with a kick.");
    }
}

public class Main {
    public static void main(String[] args) {
        Vehicle myCar = new Car();
        Vehicle myBike = new Bike();

        myCar.start(); // Output: Car starts with a key.
        myCar.stop();  // Output: Vehicle stopped.

        myBike.start(); // Output: Bike starts with a kick.
    }
}