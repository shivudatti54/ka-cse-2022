# **Chapter 8: Inheritance Basics**

## **Introduction**

Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows one class to inherit the properties and behavior of another class. In this chapter, we will explore the basics of inheritance, including using the `super` keyword, creating a multilevel hierarchy, and understanding when constructors are involved.

## **What is Inheritance?**

Inheritance is a mechanism that enables a class to inherit the attributes and methods of another class. The class that is being inherited from is called the **superclass** or **parent class**, while the class that is doing the inheriting is called the **subclass** or **child class**.

## **Benefits of Inheritance**

- Promotes code reuse: Inheritance allows us to reuse code from the superclass, reducing the amount of code we need to write.
- Encapsulates data and behavior: Inheritance helps us to encapsulate data and behavior, making it easier to manage and maintain complex systems.

## **Using the `super` Keyword**

The `super` keyword is used to access the superclass's members, such as attributes and methods. When we use the `super` keyword, we can access the superclass's members without having to prefix them with the superclass's name.

**Example: Using `super` Keyword**

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

In this example, the `Dog` class extends the `Animal` class and overrides the `sound()` method. However, the `Dog` class still calls the `Animal` class's `sound()` method using the `super` keyword.

## **Multilevel Hierarchy**

A multilevel hierarchy is a class hierarchy where a subclass inherits from another subclass. This is also known as a nested inheritance.

**Example: Multilevel Hierarchy**

```java
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound.");
    }
}

public class Mammal extends Animal {
    public void drink() {
        System.out.println("The mammal drinks.");
    }
}

public class Dog extends Mammal {
    public void bark() {
        System.out.println("The dog barks.");
    }
}
```

In this example, the `Dog` class extends the `Mammal` class, which in turn extends the `Animal` class. This creates a multilevel hierarchy.

## **Constructors and Inheritance**

When a subclass is created, the constructor of the superclass is automatically called before the constructor of the subclass. This is known as constructor chaining.

**Example: Constructors and Inheritance**

```java
public class Animal {
    public Animal() {
        System.out.println("Animal constructor called.");
    }
}

public class Dog extends Animal {
    public Dog() {
        System.out.println("Dog constructor called.");
    }
}
```

In this example, the `Dog` class extends the `Animal` class and overrides the constructor. However, the `Dog` class's constructor still calls the `Animal` class's constructor.

## **Key Concepts**

- **Superclass**: The class that is being inherited from.
- **Subclass**: The class that is doing the inheriting.
- **`super` keyword**: Used to access the superclass's members.
- **Multilevel hierarchy**: A class hierarchy where a subclass inherits from another subclass.
- **Constructor chaining**: The constructor of the superclass is called before the constructor of the subclass.

## **Practice Problems**

1.  Create a subclass that inherits from a superclass.
2.  Use the `super` keyword to access the superclass's members.
3.  Create a multilevel hierarchy and demonstrate it.

## **Conclusion**

Inheritance is a powerful concept in OOP that allows us to reuse code and promote modularity. By understanding the basics of inheritance, including using the `super` keyword, creating a multilevel hierarchy, and understanding when constructors are involved, we can write more efficient and effective code.
