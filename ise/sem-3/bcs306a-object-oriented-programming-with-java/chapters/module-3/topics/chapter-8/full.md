# **Chapter 8: Inheritance Basics, Using super, Creating a Multilevel Hierarchy, When Constructors Are Invoked**

## **Introduction**

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows one class to inherit the properties and behavior of another class. This chapter will delve into the basics of inheritance, its applications, and its usage in Java.

## **Historical Context**

The concept of inheritance dates back to the early days of programming, with languages like Simula (1966) and Smalltalk (1972) introducing the idea. However, it was not until the introduction of C++ (1985) that inheritance became a mainstream feature in programming languages. Java, which was designed by James Gosling and his team at Sun Microsystems in the mid-1990s, inherited this concept and made it an integral part of its design.

## **Inheritance Basics**

Inheritance is a mechanism that allows one class to inherit the properties and behavior of another class. The class that inherits is called the subclass or derived class, while the class being inherited from is called the superclass or base class.

### UML Diagram of Inheritance

The following UML (Unified Modeling Language) diagram illustrates the relationship between a subclass and its superclass:

```markdown
+---------------+
| Superclass |
+---------------+
|
|
v
+---------------+
| Subclass |
+---------------+
```

## **Using the `super` Keyword**

In Java, the `super` keyword is used to access the members of the superclass from a subclass. This is particularly useful for overriding methods and accessing superclass fields.

### Example

```java
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound.");
    }
}

public class Dog extends Animal {
    @Override
    public void sound() {
        System.out.println("The dog barks.");
        super.sound(); // Calls the sound() method of the Animal class
    }
}
```

## **Creating a Multilevel Hierarchy**

A multilevel hierarchy occurs when a subclass inherits from another subclass. This allows for a more complex inheritance structure, where a class can inherit properties and behavior from multiple levels of superclasses.

### Example

```java
public class Mammal {
    public void eat() {
        System.out.println("The mammal eats.");
    }
}

public class Carnivore extends Mammal {
    public void hunt() {
        System.out.println("The carnivore hunts.");
    }
}

public class Dog extends Carnivore {
    @Override
    public void eat() {
        System.out.println("The dog eats dog food.");
    }
}
```

## **When Constructors Are Invoked**

In Java, constructors are used to initialize objects when they are created. When a subclass inherits from a superclass, the constructor of the subclass is invoked before the constructor of the superclass. However, if the superclass has a constructor, it must be called explicitly using the `super` keyword.

### Example

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

To call the superclass constructor explicitly, use the `super` keyword:

```java
public class Dog extends Animal {
    public Dog() {
        super();
        System.out.println("Dog constructor called.");
    }
}
```

## **Case Study: A Real-World Example**

Suppose we want to model a university with different types of students, such as undergraduate and graduate students. We can create a `Student` class as the superclass and then create subclasses for undergraduate and graduate students.

```java
public class Student {
    public void study() {
        System.out.println("The student studies.");
    }
}

public class UndergraduateStudent extends Student {
    public void attendLectures() {
        System.out.println("The undergraduate student attends lectures.");
    }
}

public class GraduateStudent extends Student {
    public void conductResearch() {
        System.out.println("The graduate student conducts research.");
    }
}
```

## **Applications of Inheritance**

Inheritance has numerous applications in software development, including:

- Modeling real-world entities with complex relationships
- Creating a hierarchy of classes to represent a complex system
- Reducing code duplication by inheriting properties and behavior from a superclass

## **Conclusion**

In this chapter, we have explored the basics of inheritance in object-oriented programming, including its history, usage, and applications. We have also discussed the importance of using the `super` keyword to access superclass members from a subclass. Additionally, we have provided examples of creating a multilevel hierarchy and when constructors are invoked.

## **Further Reading**

- "Head First Design Patterns" by Kathy Sierra and Bert Bates
- "Design Patterns: Elements of Reusable Object-Oriented Software" by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides
- "Java: A Beginner's Guide" by Herbert Schildt

Note: The above content is a detailed and comprehensive deep-dive into the topic of "Chapter 8" as per your requirements.
