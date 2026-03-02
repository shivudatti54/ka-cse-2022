java
// Level 1: The top-most superclass (Grandparent)
class Vehicle {
    String type;

    Vehicle(String type) {
        this.type = type;
        System.out.println("A " + type + " is created.");
    }

    void move() {
        System.out.println("The " + type + " is moving.");
    }
}

// Level 2: Inherits from Vehicle (Parent)
class LandVehicle extends Vehicle {
    int wheels;

    LandVehicle(String type, int wheels) {
        super(type); // Calls Vehicle(String type) constructor
        this.wheels = wheels;
        System.out.println("It has " + wheels + " wheels.");
    }

    @Override
    void move() {
        super.move(); // Calls Vehicle's move() method
        System.out.println("It is moving on land.");
    }
}

// Level 3: Inherits from LandVehicle (Child)
class Car extends LandVehicle {
    String brand;

    Car(String brand) {
        super("Car", 4); // Calls LandVehicle(String type, int wheels) constructor
        this.brand = brand;
        System.out.println("It is a " + brand + ".");
    }

    void honk() {
        System.out.println("The " + brand + " car is honking!");
    }
}

// Main class to test the hierarchy
public class TestMultilevel {
    public static void main(String[] args) {
        System.out.println("Creating a Car object:");
        Car myCar = new Car("Maruti");

        System.out.println("\nCalling overridden method:");
        myCar.move(); // Calls the most specific version (in LandVehicle)

        System.out.println("\nCalling child-specific method:");
        myCar.honk();
    }
}