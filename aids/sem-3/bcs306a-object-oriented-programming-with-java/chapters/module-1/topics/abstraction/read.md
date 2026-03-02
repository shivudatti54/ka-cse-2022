java
// Abstract class
abstract class Vehicle {
    // Abstract method (no implementation)
    public abstract void startEngine();

    // Concrete method (with implementation)
    public void honk() {
        System.out.println("Beep Beep!");
    }
}

// Concrete subclass inheriting the abstract class
class Car extends Vehicle {
    // Must provide implementation for the abstract method
    @Override
    public void startEngine() {
        System.out.println("Car engine started with a key.");
    }
}

class Bike extends Vehicle {
    @Override
    public void startEngine() {
        System.out.println("Bike engine started with a kick.");
    }
}

// Main class
public class Main {
    public static void main(String[] args) {
        Vehicle myCar = new Car();
        Vehicle myBike = new Bike();

        myCar.startEngine(); // Output: Car engine started with a key.
        myCar.honk();        // Output: Beep Beep!

        myBike.startEngine(); // Output: Bike engine started with a kick.
    }
}