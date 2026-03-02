java
interface Shape {
    double calculateArea(); // Abstract instance method

    // Static utility method
    static double calculateCircleArea(double radius) {
        return Math.PI * radius * radius;
    }
}

class Circle implements Shape {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public double calculateArea() {
        // We can use the interface's static method internally
        return Shape.calculateCircleArea(this.radius);
    }
}

public class Main {
    public static void main(String[] args) {
        // Calling the static method using the Interface name
        double area = Shape.calculateCircleArea(5.0);
        System.out.println("Area of circle: " + area); // Output: Area of circle: 78.539...

        Circle myCircle = new Circle(5.0);
        System.out.println("Area from Circle object: " + myCircle.calculateArea());

        // myCircle.calculateCircleArea(5); // ERROR - This will not compile
        // Circle.calculateCircleArea(5);   // ERROR - This will also not compile
    }
}