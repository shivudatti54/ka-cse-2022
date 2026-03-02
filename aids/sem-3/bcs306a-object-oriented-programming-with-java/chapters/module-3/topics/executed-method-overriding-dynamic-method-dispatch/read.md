# **Object Oriented Programming with JAVA**

## **Module: Inheritance: Inheritance Basics, Using super, Creating a Multilevel Hierarchy, When Constructors Are Executed**

### Inheritance Basics

Inheritance is a fundamental concept in Object Oriented Programming (OOP) that allows one class to inherit the properties and behavior of another class. The class that is being inherited from is called the **parent** or **superclass**, while the class that is doing the inheriting is called the **child** or **subclass**.

#### Definition

Inheritance is a mechanism by which one class can inherit the attributes and methods of another class. The child class inherits all the fields and methods of the parent class and can also add new fields and methods or override the ones inherited from the parent class.

#### Benefits

- Encapsulation: Inheritance helps to encapsulate data and behavior, making it easier to modify and extend.
- Code Reusability: Inheritance promotes code reusability by allowing the child class to inherit the implementation of the parent class.
- Easier Maintenance: Inheritance makes it easier to modify and extend the behavior of the parent class without affecting the child class.

### Using the `super` Keyword

The `super` keyword is used to access the members of the superclass from a subclass. It is used to call the constructor of the superclass, override methods, and access fields.

#### Example

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
        super.sound(); // calls the sound method of the Animal class
    }
}
```

### Creating a Multilevel Hierarchy

A multilevel hierarchy is a class hierarchy that has multiple levels of inheritance. A class can inherit from another class, and that class can also inherit from another class.

#### Example

```java
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound.");
    }
}

public class Mammal extends Animal {
    public void eat() {
        System.out.println("The mammal eats.");
    }
}

public class Cat extends Mammal {
    public void play() {
        System.out.println("The cat plays.");
    }
}
```

### When Constructors Are Executed

When a class is instantiated, the constructor of the class is executed. If the child class has a constructor that is different from the constructor of the parent class, it is called before the constructor of the parent class.

#### Example

```java
public class Animal {
    public Animal() {
        System.out.println("The animal constructor is called.");
    }
}

public class Dog extends Animal {
    public Dog() {
        System.out.println("The dog constructor is called.");
    }
}
```

### Executed, Method Overriding, Dynamic Method Dispatch, Using Abstract Classes, Using final with Inheritance, Local Variable Type Inference and Inherita

#### Executed

- The constructor of the parent class is executed before the constructor of the child class.
- The constructor of the child class is executed after the constructor of the parent class.

#### Method Overriding

- Method overriding is a feature of OOP that allows a subclass to provide a specific implementation of a method that is already defined in its superclass.
- The method in the subclass has the same signature as the method in the superclass.

#### Dynamic Method Dispatch

- Dynamic method dispatch is a feature of OOP that allows the correct method to be called based on the actual type of the object, rather than its declared type.
- This is achieved through the use of polymorphism.

#### Using Abstract Classes

- An abstract class is a class that cannot be instantiated and is used to provide a common implementation for a group of related classes.
- An abstract class can have both abstract and non-abstract methods.

#### Using final with Inheritance

- The `final` keyword is used to indicate that a method cannot be overridden in a subclass.
- A class can be declared `final` and cannot be subclassed.

#### Local Variable Type Inference

- Local variable type inference is a feature of Java that allows the type of a local variable to be inferred from its initializer.
- This feature was introduced in Java 5.

#### Inherita

- Inherita is not a valid Java term.
- It is possible that this term is being used incorrectly or is a typo.

### Key Concepts

- Inheritance: a mechanism by which one class can inherit the attributes and methods of another class.
- Superclass: the class that is being inherited from.
- Child class: the class that is doing the inheriting.
- Constructor: a special method that is used to initialize objects.
- Method overriding: a feature of OOP that allows a subclass to provide a specific implementation of a method that is already defined in its superclass.
- Polymorphism: the ability of an object to take on multiple forms.
- Abstract class: a class that cannot be instantiated and is used to provide a common implementation for a group of related classes.
- Final: a keyword that is used to indicate that a method cannot be overridden in a subclass.
- Local variable type inference: a feature of Java that allows the type of a local variable to be inferred from its initializer.
