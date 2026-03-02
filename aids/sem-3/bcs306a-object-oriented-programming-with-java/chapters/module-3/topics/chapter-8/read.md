# **Chapter 8: Inheritance Basics**

## **Introduction**

Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows one class to inherit the properties and behavior of another class. In Java, inheritance is achieved using the `extends` keyword. In this chapter, we will explore the basics of inheritance, including using the `super` keyword, creating a multilevel hierarchy, and understanding when constructors are used.

## **What is Inheritance?**

Inheritance is a mechanism that allows a child class to inherit the properties and behavior of a parent class. The child class inherits all the fields and methods of the parent class and can also add new fields and methods or override the ones inherited from the parent class.

## **Types of Inheritance**

There are two types of inheritance in Java:

- **Single Inheritance**: A child class inherits from a single parent class.
- **Multiple Inheritance**: A child class inherits from multiple parent classes.

Java does not support multiple inheritance.

## **Using the `super` Keyword**

The `super` keyword is used to access the members of the parent class from the child class. There are two ways to use the `super` keyword:

- **Upcasting**: When a child class is assigned to a parent class reference variable, the `super` keyword is used to access the members of the parent class.
- **Downcasting**: When a parent class reference variable is assigned to a child class reference variable, the `super` keyword is used to access the members of the child class.

## **Example**

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

public class Main {
    public static void main(String[] args) {
        Animal animal = new Animal();
        Dog dog = new Dog();
        animal.sound();  // Output: The animal makes a sound.
        dog.sound();    // Output: The animal makes a sound. The dog barks.
    }
}
```

## **Creating a Multilevel Hierarchy**

A multilevel hierarchy is a class that inherits from another class, which in turn inherits from another class. This is also known as a nested class.

## **Example**

```java
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound.");
    }
}

public class Mammal extends Animal {
    public void walk() {
        System.out.println("The mammal walks.");
    }
}

public class Dog extends Mammal {
    public void sound() {
        super.sound();
        System.out.println("The dog barks.");
    }
}
```

## **Constructors**

Constructors are special methods that are used to initialize objects when they are created. In Java, constructors have the same name as the class and do not have a return type.

## **Example**

```java
public class Animal {
    public Animal(String name) {
        System.out.println("The animal is " + name + ".");
    }
}

public class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }
}
```

## **Key Concepts**

- Inheritance: A mechanism that allows one class to inherit the properties and behavior of another class.
- `super` keyword: Used to access the members of the parent class from the child class.
- Multilevel hierarchy: A class that inherits from another class, which in turn inherits from another class.
- Constructors: Special methods that are used to initialize objects when they are created.
