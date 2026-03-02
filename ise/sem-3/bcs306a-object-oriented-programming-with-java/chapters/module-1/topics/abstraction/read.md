java
// Abstract class
abstract class Vehicle {
    // Concrete method - has an implementation
    public void start() {
        System.out.println("Vehicle is starting...");
    }

    // Abstract method - no implementation, just a declaration
    public abstract void accelerate();
    public abstract void brake();
}

// Concrete subclass inheriting the abstract class
class Car extends Vehicle {
    // Must provide implementation for all abstract methods
    @Override
    public void accelerate() {
        System.out.println("Car is accelerating by pressing the gas pedal.");
    }

    @Override
    public void brake() {
        System.out.println("Car is braking by pressing the brake pedal.");
    }
}

// Main class
public class Main {
    public static void main(String[] args) {
        Vehicle myCar = new Car(); // Reference of abstract type, object of concrete type
        myCar.start();     // Inherited concrete method
        myCar.accelerate(); // Implemented abstract method
        myCar.brake();     // Implemented abstract method

        // Vehicle v = new Vehicle(); // This would be an ERROR! Cannot instantiate an abstract class.
    }
}