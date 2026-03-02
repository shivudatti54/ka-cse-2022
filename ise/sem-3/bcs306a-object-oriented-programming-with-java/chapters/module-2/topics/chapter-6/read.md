# **Chapter 6: Introducing Classes**

## **6.1 Introduction to Classes**

In Object-Oriented Programming (OOP), a class is a blueprint or a template that defines the properties and behavior of an object. A class is essentially a design pattern or a template that defines the characteristics of an object, such as its attributes (data) and methods (functions).

## **6.2 Defining a Class**

To define a class, we use the `class` keyword followed by the name of the class. The class definition typically includes:

- **Class Header**: The class header includes the `class` keyword, the name of the class, and the `extends` keyword (if the class inherits from another class).
- **Class Body**: The class body includes the attributes (data) and methods (functions) of the class.

**Example:**

```java
public class Car {
    // class header
    public class Car {
        // class body
        private String color;
        private int speed;

        public Car(String color, int speed) {
            this.color = color;
            this.speed = speed;
        }

        public void accelerate() {
            System.out.println("Accelerating...");
        }

        public void brake() {
            System.out.println("Braking...");
        }
    }
}
```

## **6.3 Declaring an Object**

To declare an object, we use the `new` keyword followed by the class name and parentheses containing the required parameters.

- **Constructors**: A constructor is a special method that is used to initialize an object when it is created. Constructors have the same name as the class and do not have a return type.
- **Instance Variables**: Instance variables are variables that are defined inside the class and are associated with an instance of the class.
- **Access Modifiers**: Access modifiers are used to control access to the attributes and methods of a class.

**Example:**

```java
public class Car {
    private String color;
    private int speed;

    public Car(String color, int speed) {
        this.color = color;
        this.speed = speed;
    }

    public void accelerate() {
        System.out.println("Accelerating...");
    }

    public void brake() {
        System.out.println("Braking...");
    }
}

public class Main {
    public static void main(String[] args) {
        Car myCar = new Car("Red", 60);
        System.out.println(myCar.color);  // prints "Red"
        myCar.accelerate();  // prints "Accelerating..."
        myCar.brake();  // prints "Braking..."
    }
}
```

**Key Concepts:**

- **Class**: A blueprint or a template that defines the properties and behavior of an object.
- **Object**: An instance of a class.
- **Constructor**: A special method that is used to initialize an object when it is created.
- **Instance Variables**: Variables that are defined inside the class and are associated with an instance of the class.
- **Access Modifiers**: Used to control access to the attributes and methods of a class.

## **6.4 Inheritance**

Inheritance is a fundamental concept in OOP that allows one class to inherit the properties and behavior of another class.

**Example:**

```java
public class Animal {
    public void eat() {
        System.out.println("Eating...");
    }
}

public class Dog extends Animal {
    public void bark() {
        System.out.println("Barking...");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog myDog = new Dog();
        myDog.eat();  // prints "Eating..."
        myDog.bark();  // prints "Barking..."
    }
}
```

**Key Concepts:**

- **Inheritance**: A fundamental concept in OOP that allows one class to inherit the properties and behavior of another class.
- **Superclass**: The class that is being inherited from.
- **Subclass**: The class that is doing the inheriting.
- **Access Modifiers**: Used to control access to the attributes and methods of a superclass or subclass.
