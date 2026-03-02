java
// Level 1: The Root Superclass
class Vehicle {
    String brand;
    int year;

    void start() {
        System.out.println("The vehicle is starting.");
    }
}

// Level 2: Intermediate Subclass (inherits from Vehicle, acts as superclass for Car)
class LandVehicle extends Vehicle {
    int numWheels;

    void drive() {
        System.out.println("The land vehicle is driving on " + numWheels + " wheels.");
    }
}

// Level 3: Leaf Subclass (inherits from LandVehicle, and indirectly from Vehicle)
class Car extends LandVehicle {
    String model;
    boolean isConvertible;

    void honk() {
        System.out.println("Honk! Honk!");
    }

    // A method using inherited members
    void displayInfo() {
        System.out.println("This is a " + year + " " + brand + " " + model + ".");
        System.out.println("It has " + numWheels + " wheels.");
        if (isConvertible) {
            System.out.println("And it's a convertible!");
        }
    }
}

// Main class to test the hierarchy
public class MultilevelInheritanceDemo {
    public static void main(String[] args) {
        Car myCar = new Car();
        
        // Fields from Vehicle (Level 1)
        myCar.brand = "Ford";
        myCar.year = 2023;
        
        // Field from LandVehicle (Level 2)
        myCar.numWheels = 4;
        
        // Fields from Car (Level 3)
        myCar.model = "Mustang";
        myCar.isConvertible = true;

        // Methods from all levels
        myCar.start();   // From Vehicle
        myCar.drive();   // From LandVehicle
        myCar.honk();    // From Car
        myCar.displayInfo(); // From Car
    }
}