java
class Animal {
void makeSound() {
System.out.println("Some generic animal sound");
}
}

class Dog extends Animal {
@Override
void makeSound() { // Overriding the parent method
System.out.println("Bark Bark!");
}
}

class Cat extends Animal {
@Override
void makeSound() { // Overriding the parent method
System.out.println("Meow!");
}
}

public class TestDispatch {
public static void main(String[] args) {
Animal myAnimal; // Superclass reference variable

        myAnimal = new Animal(); // Refers to an Animal object
        myAnimal.makeSound(); // Output: Some generic animal sound

        myAnimal = new Dog(); // Same reference now points to a Dog object
        myAnimal.makeSound(); // Output: Bark Bark! (Dog's version is called)

        myAnimal = new Cat(); // Same reference now points to a Cat object
        myAnimal.makeSound(); // Output: Meow! (Cat's version is called)
    }

}
