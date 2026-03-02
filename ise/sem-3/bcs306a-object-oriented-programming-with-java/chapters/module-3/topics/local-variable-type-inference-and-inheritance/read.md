java
// Superclass
class Vehicle {
String type;

    void start() {
        System.out.println("Vehicle is starting.");
    }

}

// Subclass inheriting from Vehicle
class Car extends Vehicle {
int numOfDoors;

    // Method Overriding
    @Override
    void start() {
        super.start(); // Using 'super' to call parent method
        System.out.println("Car engine ignited.");
    }

    void honk() {
        System.out.println("Beep Beep!");
    }

}
