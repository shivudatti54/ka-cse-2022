java
interface Shape {
    // Abstract method (the core contract)
    double calculateArea();

    // Static utility method
    static boolean isShapeValid(double dimension) {
        return dimension > 0;
    }
}

class Circle implements Shape {
    private double radius;

    public Circle(double radius) {
        if (!Shape.isShapeValid(radius)) { // Calling the static method
            throw new IllegalArgumentException("Radius must be positive");
        }
        this.radius = radius;
    }

    @Override
    public double calculateArea() {
        return Math.PI * radius * radius;
    }
}

public class Main {
    public static void main(String[] args) {
        // Calling the static method directly on the Interface
        System.out.println("Is 5.0 a valid dimension? " + Shape.isShapeValid(5.0));

        Circle c = new Circle(7.5);
        System.out.println("Area: " + c.calculateArea());

        // This will cause a compilation error:
        // c.isShapeValid(10); // Invalid call on an instance
    }
}