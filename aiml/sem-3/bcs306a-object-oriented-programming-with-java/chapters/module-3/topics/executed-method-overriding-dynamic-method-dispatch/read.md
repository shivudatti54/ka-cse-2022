# **Inheritance Basics in Object Oriented Programming with JAVA**

## **Introduction**

Inheritance is a fundamental concept in Object Oriented Programming (OOP) that allows one class to inherit the properties and behavior of another class. In this study material, we will explore the basics of inheritance in JAVA, including executing constructors, method overriding, dynamic method dispatch, using abstract classes, using final with inheritance, local variable type inference, and polymorphism.

## **Executing Constructors**

When a subclass object is created, the subclass constructor is executed first. This is followed by the execution of the superclass constructor. If the superclass constructor does not have any parameters, it is invoked implicitly by the subclass constructor.

**Example:**

```java
public class Animal {
    public Animal() {
        System.out.println("Animal constructor executed");
    }
}

public class Dog extends Animal {
    public Dog() {
        System.out.println("Dog constructor executed");
        super(); // invokes Animal constructor
    }
}

public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog();
    }
}
```

Output:

```
Dog constructor executed
Animal constructor executed
```

## **Method Overriding**

Method overriding is a feature of inheritance where a subclass provides a different implementation of a method that is already present in its superclass. The method in the subclass has the same name, return type, and parameter list as the method in the superclass.

**Example:**

```java
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound");
    }
}

public class Dog extends Animal {
    public void sound() {
        System.out.println("The dog barks");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal animal = new Animal();
        Dog dog = new Dog();

        animal.sound(); // prints "The animal makes a sound"
        dog.sound(); // prints "The dog barks"
    }
}
```

## **Dynamic Method Dispatch**

Dynamic method dispatch is the process of resolving the method to be invoked at runtime, based on the actual object being referred to, rather than the static type of the reference variable.

**Example:**

```java
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound");
    }
}

public class Dog extends Animal {
    public void sound() {
        System.out.println("The dog barks");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal animal = new Animal();
        Animal dog = new Dog();

        animal.sound(); // prints "The animal makes a sound"
        dog.sound(); // prints "The dog barks"
    }
}
```

## **Using Abstract Classes**

An abstract class is a class that cannot be instantiated and is designed to be inherited by other classes. Abstract classes can have both abstract and non-abstract methods.

**Example:**

```java
public abstract class Animal {
    public abstract void sound();
    public void eat() {
        System.out.println("The animal eats");
    }
}

public class Dog extends Animal {
    public void sound() {
        System.out.println("The dog barks");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.sound(); // prints "The dog barks"
        dog.eat(); // prints "The animal eats"
    }
}
```

## **Using Final with Inheritance**

The `final` keyword can be used to restrict inheritance in two ways:

1.  Final classes cannot be inherited from.
2.  Final methods cannot be overridden.

**Example:**

```java
public class Animal {
    public final void sound() {
        System.out.println("The animal makes a sound");
    }
}

public class Dog extends Animal {
    // cannot override the final method
    // public void sound() {
    //     System.out.println("The dog barks");
    // }
}

public class Main {
    public static void main(String[] args) {
        Animal animal = new Animal();
        animal.sound(); // prints "The animal makes a sound"
    }
}
```

## **Local Variable Type Inference**

In JAVA, local variable type inference (LVTI) is a feature that allows the compiler to infer the type of a local variable based on its assignment.

**Example:**

```java
public class Main {
    public static void main(String[] args) {
        var name = "John"; // the type of name is inferred as String
        var age = 30; // the type of age is inferred as int
    }
}
```

## **Polymorphism**

Polymorphism is the ability of an object to take on multiple forms. In JAVA, polymorphism can be achieved through method overriding, method overloading, and duck typing.

**Example:**

```java
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound");
    }
}

public class Dog extends Animal {
    public void sound() {
        System.out.println("The dog barks");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal animal = new Dog();
        animal.sound(); // prints "The dog barks"
    }
}
```

This concludes our study material on inheritance basics in Object Oriented Programming with JAVA.
