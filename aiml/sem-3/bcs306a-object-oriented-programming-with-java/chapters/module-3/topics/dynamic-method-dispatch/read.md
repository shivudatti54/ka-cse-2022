java
class Animal {
    void makeSound() {
        System.out.println("Some generic animal sound");
    }
}

class Dog extends Animal {
    @Override
    void makeSound() {
        System.out.println("Woof! Woof!");
    }
}

public class Test {
    public static void main(String[] args) {
        // Upcasting: Animal reference pointing to a Dog object
        Animal myAnimal = new Dog(); // This is upcasting
    }
}