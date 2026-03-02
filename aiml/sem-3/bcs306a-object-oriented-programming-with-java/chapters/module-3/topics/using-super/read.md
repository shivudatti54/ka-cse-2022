java
class Vehicle {
    private int maxSpeed;

    // Parameterized constructor in superclass
    public Vehicle(int maxSpeed) {
        this.maxSpeed = maxSpeed;
    }

    public void display() {
        System.out.println("Max Speed: " + maxSpeed + " km/h");
    }
}

class Car extends Vehicle {
    private String fuelType;

    // Subclass constructor
    public Car(int maxSpeed, String fuelType) {
        super(maxSpeed); // MUST be first. Calls Vehicle(int maxSpeed)
        this.fuelType = fuelType;
    }

    @Override
    public void display() {
        super.display(); // Calls the overridden method from Vehicle
        System.out.println("Fuel Type: " + fuelType);
    }
}

public class Main {
    public static void main(String[] args) {
        Car myCar = new Car(180, "Petrol");
        myCar.display();
    }
}