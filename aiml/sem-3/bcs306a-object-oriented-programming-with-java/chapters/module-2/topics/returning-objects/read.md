java
class Box {
    double width, height, depth;

    // A method that returns a new Box object
    Box createNewBox(double w, double h, double d) {
        Box newBox = new Box(); // Create a new object
        newBox.width = w;
        newBox.height = h;
        newBox.depth = d;
        return newBox; // Return a reference to the new object
    }
}

public class Main {
    public static void main(String[] args) {
        Box myBox = new Box();
        Box anotherBox = myBox.createNewBox(10, 20, 15);
        // 'anotherBox' now holds a reference to the Box object returned by the method
        System.out.println("Volume of new box: " + (anotherBox.width * anotherBox.height * anotherBox.depth));
    }
}