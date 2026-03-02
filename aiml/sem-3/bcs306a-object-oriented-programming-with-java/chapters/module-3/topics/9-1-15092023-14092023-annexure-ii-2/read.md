# **Inheritance Basics in Java**

### What is Inheritance?

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows one class to inherit the properties and behavior of another class. The class that is being inherited from is called the **parent class** or **superclass**, while the class that does the inheriting is called the **child class** or **subclass**.

### Benefits of Inheritance

- Encapsulates code and reduces redundancy
- Promotes code reuse
- Improves code modularity and maintainability
- Enhances code flexibility and extensibility

### Types of Inheritance

- **Single Inheritance**: A child class inherits from a single parent class.
- **Multiple Inheritance**: A child class inherits from multiple parent classes.
- **Multilevel Inheritance**: A child class inherits from a parent class, which in turn inherits from another parent class.
- **Hierarchical Inheritance**: A child class inherits from a parent class, and the child class can have multiple child classes.
- **Hybrid Inheritance**: A combination of multiple inheritance.

### Super Keyword

The `super` keyword is used to access the members of the parent class from the child class. It can be used to call methods, access variables, or inherit constructors.

#### Example

```java
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound.");
    }
}

public class Dog extends Animal {
    public void sound() {
        super.sound();
        System.out.println("The dog barks.");
    }
}
```

In this example, the `Dog` class inherits from the `Animal` class and overrides the `sound()` method. The `super` keyword is used to call the `sound()` method of the `Animal` class.

### Constructors

Constructors are special methods that are used to initialize objects when they are created. Inheritance allows constructors to be inherited and accessed from child classes.

#### Example

```java
public class Animal {
    public Animal(String name) {
        this.name = name;
    }
    private String name;
}

public class Dog extends Animal {
    public Dog(String name, int age) {
        super(name); // calls the Animal constructor
        this.age = age;
    }
    private int age;
}
```

In this example, the `Animal` class has a constructor that takes a `name` parameter, and the `Dog` class has a constructor that takes an `age` parameter. The `super` keyword is used to call the `Animal` constructor from the `Dog` constructor.

### Multilevel Hierarchy

A multilevel hierarchy is a type of inheritance where a child class inherits from a parent class, and the parent class also inherits from another parent class.

#### Example

```java
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound.");
    }
}

public class Mammal extends Animal {
    public void giveMilk() {
        System.out.println("The mammal gives milk.");
    }
}

public class Dog extends Mammal {
    public void bark() {
        System.out.println("The dog barks.");
    }
}
```

In this example, the `Dog` class inherits from the `Mammal` class, which in turn inherits from the `Animal` class. The `Dog` class can access the members of the `Mammal` and `Animal` classes using the `super` keyword.

### Key Concepts

- **Inheritance**: A fundamental concept in object-oriented programming that allows one class to inherit the properties and behavior of another class.
- **Super keyword**: Used to access the members of the parent class from the child class.
- **Constructors**: Special methods that are used to initialize objects when they are created.
- **Multilevel hierarchy**: A type of inheritance where a child class inherits from a parent class, and the parent class also inherits from another parent class.
