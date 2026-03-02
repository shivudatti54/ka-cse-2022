# Chapter 6: Declaring Objects and Assigning Object Reference Variables

### 6.1 Introduction to Classes and Objects

A class is a blueprint or a template that defines the properties and behavior of an object. In object-oriented programming, an object is an instance of a class. It represents a real-world entity or concept, and it has its own set of attributes (data) and methods (functions).

### 6.2 Declaring Classes

A class is declared in Java using the `class` keyword, followed by the name of the class. The class name should be a valid Java identifier, which means it should start with a letter or underscore, and it should not contain any special characters.

```java
public class Car {
    // class body
}
```

### 6.3 Access Modifiers

Access modifiers are used to specify the accessibility of a class, its members (methods and variables), and its constructors. There are four access modifiers in Java:

- `public`: Accessible from anywhere in the program.
- `private`: Accessible only within the class.
- `protected`: Accessible within the class and its subclasses.
- `default` (no modifier): Accessible within the package.

### 6.4 Class Members

Class members are the components of a class, including:

- **Variables** (data members): Store data.
- **Methods** (functions): Perform actions.
- **Constructors**: Initialize objects when they are created.

### 6.5 Declaring Objects

A class can have multiple objects, each representing an instance of the class. An object is declared using an object reference variable, which is a reference to the object.

```java
Car myCar; // declares an object reference variable
myCar = new Car(); // creates a new object and assigns it to the variable
```

### 6.6 Assigning Object Reference Variables

Object reference variables can be reassigned to point to different objects.

```java
Car myCar; // declares an object reference variable
myCar = new Car(); // creates a new object and assigns it to the variable

Car otherCar = new Car(); // creates another object and assigns it to a new variable
myCar = otherCar; // reassigns the object reference variable to point to the other object
```

### 6.7 Key Concepts

- A class is a blueprint or a template that defines the properties and behavior of an object.
- An object is an instance of a class and represents a real-world entity or concept.
- Access modifiers are used to specify the accessibility of a class, its members, and its constructors.
- Class members include variables, methods, and constructors.
- An object reference variable is a reference to an object, and it can be reassigned to point to different objects.

### 6.8 Example

```java
public class Car {
    private String color;
    private int speed;

    public Car(String color, int speed) {
        this.color = color;
        this.speed = speed;
    }

    public void accelerate() {
        speed++;
    }

    public void brake() {
        speed--;
    }

    public String getColor() {
        return color;
    }

    public int getSpeed() {
        return speed;
    }
}

public class Main {
    public static void main(String[] args) {
        Car myCar = new Car("red", 60);
        System.out.println(myCar.getColor()); // prints "red"
        System.out.println(myCar.getSpeed()); // prints 60

        myCar.accelerate();
        System.out.println(myCar.getSpeed()); // prints 61

        Car otherCar = new Car("blue", 80);
        myCar = otherCar; // reassigns the object reference variable
        System.out.println(myCar.getColor()); // prints "blue"
    }
}
```

This example demonstrates the declaration of a class, its members, and the creation of objects. It also shows how object reference variables can be reassigned to point to different objects.
