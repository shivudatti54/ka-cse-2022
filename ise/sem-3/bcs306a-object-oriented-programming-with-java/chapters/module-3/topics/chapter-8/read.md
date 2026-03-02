# Chapter 8: Inheritance Basics, Using super, Creating a Multilevel Hierarchy, and Constructors

=====================================================

## 8.1 Introduction to Inheritance

---

Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows one class to inherit the properties and behavior of another class. The class that is being inherited from is called the **superclass** or **parent class**, while the class that is doing the inheriting is called the **subclass** or **child class**.

### Why Inheritance?

Inheritance allows for code reuse, which makes it easier to create a hierarchy of related classes. It also enables you to modify or extend the behavior of the superclass without modifying the original code.

## 8.2 Defining a Class with Inheritance

---

To define a class that inherits from another class, you use the `extends` keyword followed by the name of the superclass.

### Example

```java
public class Animal {
    private String name;

    public Animal(String name) {
        this.name = name;
    }

    public void eat() {
        System.out.println(name + " is eating");
    }
}

public class Dog extends Animal {
    public Dog(String name) {
        super(name); // calls the constructor of the superclass
    }

    public void bark() {
        System.out.println(name + " says Woof!");
    }
}
```

In this example, the `Dog` class inherits from the `Animal` class and adds its own behavior (the `bark()` method).

### Using the `super` Keyword

---

The `super` keyword is used to access the superclass's members, such as constructors, fields, and methods.

### Example

```java
public class Dog extends Animal {
    public Dog(String name) {
        super(name); // calls the constructor of the Animal class
    }

    public void bark() {
        System.out.println("Woof!");
    }
}
```

In this example, the `Dog` class calls the constructor of the `Animal` class using the `super` keyword.

## 8.3 Multilevel Inheritance

---

Multilevel inheritance occurs when a class inherits from another class, which itself inherits from a third class.

### Example

```java
public class Animal {
    private String name;

    public Animal(String name) {
        this.name = name;
    }

    public void eat() {
        System.out.println(name + " is eating");
    }
}

public class Mammal extends Animal {
    public Mammal(String name) {
        super(name);
    }

    public void walk() {
        System.out.println(name + " is walking");
    }
}

public class Dog extends Mammal {
    public Dog(String name) {
        super(name);
    }

    public void bark() {
        System.out.println(name + " says Woof!");
    }
}
```

In this example, the `Dog` class inherits from the `Mammal` class, which itself inherits from the `Animal` class.

## 8.4 Constructor Overloading and Call Super

---

When a subclass has its own constructor that calls the superclass's constructor using the `super` keyword, it's called constructor overloading.

### Example

```java
public class Animal {
    private String name;

    public Animal(String name) {
        this.name = name;
    }

    public Animal(String name, int age) {
        this.name = name;
        this.age = age; // not shown in this example
    }
}

public class Dog extends Animal {
    private int age;

    public Dog(String name, int age) {
        super(name); // calls the constructor of the Animal class
        this.age = age;
    }

    public void bark() {
        System.out.println(name + " says Woof!");
    }
}
```

In this example, the `Dog` class has its own constructor that calls the superclass's constructor using the `super` keyword.

### Key Concepts

---

- Inheritance allows code reuse and helps create a hierarchy of related classes.
- The `extends` keyword is used to define a class that inherits from another class.
- The `super` keyword is used to access the superclass's members.
- Constructor overloading can be used to call the superclass's constructor.
- Multilevel inheritance occurs when a class inherits from another class, which itself inherits from a third class.
