# **Object Oriented Programming with JAVA**

## **Module: Inheritance: Inheritance Basics, Using super, Creating a Multilevel Hierarchy, When Constructors Are Executed**

### Table of Contents

1. [Executed, Method Overriding, Dynamic Method Dispatch](#executed-method-overriding-dynamic-method-dispatch)
2. [Using Abstract Classes](#using-abstract-classes)
3. [Using final with Inheritance](#using-final-with-inheritance)
4. [Local Variable Type Inference](#local-variable-type-inference)
5. [Inherita](#inherita)

### Executed, Method Overriding, Dynamic Method Dispatch

---

Inheritance and polymorphism are two fundamental concepts in object-oriented programming (OOP). Inheritance allows one class to inherit the properties and behavior of another class, while polymorphism enables objects of different classes to be treated as if they were of the same class.

#### Executed

The concept of "executed" in the context of OOP refers to the fact that when a subclass is instantiated, its constructor is executed first. This is followed by the execution of the superclass's constructor. The superclass's constructor is executed before the subclass's constructor, and it provides the necessary initialization for the superclass.

```java
public class Animal {
    public Animal() {
        System.out.println("Animal constructor executed");
    }

    public void sound() {
        System.out.println("Animal makes a sound");
    }
}

public class Dog extends Animal {
    public Dog() {
        System.out.println("Dog constructor executed");
    }

    public void sound() {
        System.out.println("Dog barks");
    }
}
```

In the above example, when a `Dog` object is instantiated, the `Dog` constructor is executed first, followed by the `Animal` constructor. This ensures that the `Dog` object has all the properties and behavior of the `Animal` class, as well as its own specific properties and behavior.

#### Method Overriding

Method overriding is a feature of OOP that allows a subclass to provide a different implementation of a method that is already defined in its superclass. The subclass method has the same name, return type, and parameter list as the superclass method, but it can have a different implementation.

```java
public class Animal {
    public void sound() {
        System.out.println("Animal makes a sound");
    }
}

public class Dog extends Animal {
    public void sound() {
        System.out.println("Dog barks");
    }
}
```

In the above example, the `Dog` class overrides the `sound()` method of the `Animal` class with its own implementation. When a `Dog` object is created, it calls the `Dog` implementation of the `sound()` method, rather than the `Animal` implementation.

#### Dynamic Method Dispatch

Dynamic method dispatch is a feature of OOP that allows the runtime environment to determine which method to call when a method is invoked on an object of a particular class. This is in contrast to static method dispatch, where the method to call is determined at compile time.

Dynamic method dispatch is achieved through the use of polymorphism, which allows objects of different classes to be treated as if they were of the same class. This is achieved through the use of interfaces, abstract classes, and method overriding.

```java
public class Animal {
    public void sound() {
        System.out.println("Animal makes a sound");
    }
}

public class Dog extends Animal {
    public void sound() {
        System.out.println("Dog barks");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal myAnimal = new Dog();
        myAnimal.sound();
    }
}
```

In the above example, the `Animal` object is created with a `Dog` object. When the `sound()` method is called on the `Animal` object, the runtime environment determines which method to call based on the actual class of the object. In this case, it calls the `Dog` implementation of the `sound()` method.

### Using Abstract Classes

---

Abstract classes are a type of class that cannot be instantiated on their own and are designed to be inherited by other classes. They are used to provide a common implementation for a group of related classes.

```java
public abstract class Animal {
    public abstract void sound();
}

public class Dog extends Animal {
    public void sound() {
        System.out.println("Dog barks");
    }
}

public class Cat extends Animal {
    public void sound() {
        System.out.println("Cat meows");
    }
}
```

In the above example, the `Animal` class is an abstract class that provides a common interface for all animals. The `Dog` and `Cat` classes inherit from the `Animal` class and provide their own implementation of the `sound()` method.

### Using final with Inheritance

---

The `final` keyword is used to prevent a class from being subclassed. When a class is declared as `final`, it cannot be inherited by any other class.

```java
public final class Animal {
    public void sound() {
        System.out.println("Animal makes a sound");
    }
}

public class Dog {
    public void sound() {
        System.out.println("Dog barks");
    }
}
```

In the above example, the `Animal` class is declared as `final`, which prevents the `Dog` class from inheriting from it.

### Local Variable Type Inference

---

Local variable type inference is a feature of Java that allows the compiler to infer the type of a local variable based on its initial value.

```java
public void myMethod() {
    int x = 10; // x is inferred to be an int
    double y = 10.5; // y is inferred to be a double
    String z = "hello"; // z is inferred to be a String
}
```

In the above example, the types of the local variables `x`, `y`, and `z` are inferred by the compiler based on their initial values.

### Inherita

---

Inherita is a null pointer exception that occurs when a subclass attempts to access a method or field of its superclass that has not been overridden.

```java
public class Animal {
    public void sound() {
        System.out.println("Animal makes a sound");
    }
}

public class Dog extends Animal {
    public void sound() {
        throw new RuntimeException("Method sound not overridden");
    }
}
```

In the above example, the `Dog` class attempts to override the `sound()` method of the `Animal` class, but it throws a `RuntimeException` instead. This is because the `Dog` class does not provide an implementation of the `sound()` method.

### Further Reading

---

- "Head First Design Patterns" by Kathy Sierra and Bert Bates
- "Design Patterns: Elements of Reusable Object-Oriented Software" by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides
- "Object-Oriented Programming in Java" by Herbert Schildt
- "Java: A Beginner's Guide" by Herbert Schildt

Note: The above examples and code snippets are for illustration purposes only and may not be complete or functional in all cases.
