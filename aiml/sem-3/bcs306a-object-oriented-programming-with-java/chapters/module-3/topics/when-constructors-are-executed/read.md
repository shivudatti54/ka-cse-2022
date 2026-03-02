java
class Vehicle {
    private String type;

    // Superclass No-argument Constructor
    public Vehicle() {
        System.out.println("Vehicle Constructor: Setting type to 'Generic'");
        this.type = "Generic";
    }

    // Superclass Parameterized Constructor
    public Vehicle(String type) {
        System.out.println("Vehicle Constructor: Setting type to " + type);
        this.type = type;
    }
}

class Car extends Vehicle {
    private String model;

    // Subclass Constructor
    public Car(String model) {
        // super() is implicitly called here by the compiler!
        System.out.println("Car Constructor: Initializing model");
        this.model = model;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Creating Car object...");
        Car myCar = new Car("Swift");
    }
}