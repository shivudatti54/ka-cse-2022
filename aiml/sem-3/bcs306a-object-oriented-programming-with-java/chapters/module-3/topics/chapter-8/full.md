# Chapter 8: Inheritance Basics, Using Super, Creating a Multilevel Hierarchy, When Constructors Are Involved

## 8.1 Introduction to Inheritance

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows one class to inherit the properties and behavior of another class. The inheriting class, also known as the subclass or derived class, inherits all the fields and methods of the superclass or base class. Inheritance enables code reuse, facilitates the creation of a hierarchy of classes, and promotes modularity and flexibility in software design.

## 8.2 Historical Context

The concept of inheritance dates back to the early days of programming, when it was known as "subroutine inheritance" or "function inheritance." However, it wasn't until the 1970s and 1980s, with the advent of object-oriented programming (OOP), that inheritance became a central aspect of OOP.

In the 1970s, languages like Simula and Smalltalk introduced the concept of classes and objects, which laid the foundation for modern OOP. Inheritance was also introduced in these languages, allowing programmers to create a hierarchy of classes that inherited the properties and behavior of their superclasses.

## 8.3 Using Super

In Java, the `super` keyword is used to access the members of the superclass. When a subclass is created, it can use the `super` keyword to call the constructor of the superclass, access its fields, and use its methods.

Here's an example of using the `super` keyword:

```java
public class Animal {
    public Animal() {
        System.out.println("Animal constructor");
    }

    public void sounds() {
        System.out.println("Animal makes a sound");
    }
}

public class Dog extends Animal {
    public Dog() {
        super(); // calls Animal constructor
        System.out.println("Dog constructor");
    }

    public void sounds() {
        super.sounds(); // calls Animal.sounds() method
        System.out.println("Dog barks");
    }
}
```

In this example, the `Dog` class extends the `Animal` class and uses the `super` keyword to call the `Animal` constructor and access its `sounds()` method.

## 8.4 Creating a Multilevel Hierarchy

A multilevel hierarchy of classes is created when a class extends another class, and that class extends another class. This creates a tree-like structure of classes, where each class is a subclass of its parent class.

Here's an example of a multilevel hierarchy:

```java
public class Animal {
    public Animal() {
        System.out.println("Animal constructor");
    }

    public void sounds() {
        System.out.println("Animal makes a sound");
    }
}

public class Mammal extends Animal {
    public Mammal() {
        super();
        System.out.println("Mammal constructor");
    }

    public void eats() {
        System.out.println("Mammal eats");
    }
}

public class Dog extends Mammal {
    public Dog() {
        super();
        System.out.println("Dog constructor");
    }

    public void barks() {
        System.out.println("Dog barks");
    }
}
```

In this example, the `Dog` class extends the `Mammal` class, which extends the `Animal` class. This creates a multilevel hierarchy of classes, where each class is a subclass of its parent class.

## 8.5 When Constructors Are Involved

When a subclass is created, it can use the `super` keyword to call the constructor of its superclass. However, if the subclass has its own constructor, it must call the superclass constructor using the `super` keyword.

Here's an example of when constructors are involved:

```java
public class Animal {
    public Animal() {
        System.out.println("Animal constructor");
    }

    public void sounds() {
        System.out.println("Animal makes a sound");
    }
}

public class Dog extends Animal {
    public Dog() {
        super(); // calls Animal constructor
        System.out.println("Dog constructor");
    }

    public Dog(String name) {
        super();
        this.name = name;
        System.out.println("Dog constructor with name");
    }
}
```

In this example, the `Dog` class has two constructors: one that calls the `Animal` constructor, and another that takes a `name` parameter. The second constructor must call the `Animal` constructor using the `super` keyword.

## 8.6 Overriding Methods

Inheritance allows for method overriding, where a subclass can provide a different implementation of a method that is already defined in its superclass.

Here's an example of overriding methods:

```java
public class Animal {
    public void sounds() {
        System.out.println("Animal makes a sound");
    }
}

public class Dog extends Animal {
    public void sounds() {
        System.out.println("Dog barks");
    }
}
```

In this example, the `Dog` class overrides the `sounds()` method of the `Animal` class, providing a different implementation that is specific to dogs.

## 8.7 Polymorphism

Polymorphism is the ability of an object to take on multiple forms, depending on the context in which it is used. Inheritance allows for polymorphism, as a subclass can be treated as its superclass.

Here's an example of polymorphism:

```java
public class Animal {
    public void sounds() {
        System.out.println("Animal makes a sound");
    }
}

public class Dog extends Animal {
    public void sounds() {
        System.out.println("Dog barks");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal animal = new Animal();
        Dog dog = new Dog();

        animal.sounds(); // outputs "Animal makes a sound"
        dog.sounds(); // outputs "Dog barks"
    }
}
```

In this example, the `animal` and `dog` variables are of type `Animal`, but they point to objects of type `Dog`. The `sounds()` method is called on both variables, and the correct output is produced.

## 8.8 Case Study: Designing a Family Tree

Suppose we want to design a family tree that includes people, their parents, and their children. We can use inheritance to create a `Person` class that has a `parent` field, and a `Child` class that extends `Person` and has a `parent` field.

Here's an example of how we can design the family tree:

```java
public class Person {
    public Person() {
        System.out.println("Person constructor");
    }

    public void parents() {
        System.out.println("Person has parents");
    }
}

public class Child extends Person {
    public Child(Person parent) {
        super();
        this.parent = parent;
        System.out.println("Child constructor");
    }

    public void getParents() {
        parent.parents(); // calls Person.parents() method
        System.out.println("Child has a parent");
    }
}
```

In this example, the `Child` class extends the `Person` class and has a `parent` field. The `Child` class also overrides the `parents()` method to provide a different implementation that is specific to children.

## 8.9 Applications of Inheritance

Inheritance has many applications in software design, including:

- Modeling real-world objects and systems
- Creating a hierarchy of classes
- Code reuse
- Polymorphism
- Object-oriented programming

## 8.10 Further Reading

- "Head First Design Patterns" by Kathy Sierra and Bert Bates
- "Design Patterns: Elements of Reusable Object-Oriented Software" by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides
- "Object-Oriented Programming: A Concise Introduction" by Ralf Hildebrandt
- "Inheritance: A Programming Concept" by Andrew Koenig

## 8.11 Diagrams

Here are some diagrams that illustrate the concepts of inheritance:

- UML Class Diagram:
  ```markdown
  +---------------+
  | Animal |
  +---------------+
  | - constructor |
  | - sounds() |
  +---------------+
  +---------------+
  | Mammal |
  +---------------+
  | - constructor |
  | - eats() |
  | - extends Animal |
  +---------------+
  +---------------+
  | Dog |
  +---------------+
  | - constructor |
  | - barks() |
  | - extends Mammal |
  | - extends Animal |
  +---------------+

````
*   Object Diagram:
    ```markdown
+---------------+
|  Animal     |
|  - object    |
+---------------+
|  Mammal      |
|  - object    |
+---------------+
|  Dog         |
|  - object    |
+---------------+
````

- Inheritance Graph:
  ```markdown
  +---------------+
  | Animal |
  +---------------+
  | |
  | +---- Mammal |
  | | |
  | +---- Dog |
  | | |
  +---------------+

```
Note: The diagrams are not exhaustive and are just a few examples of how inheritance can be represented visually.
```
