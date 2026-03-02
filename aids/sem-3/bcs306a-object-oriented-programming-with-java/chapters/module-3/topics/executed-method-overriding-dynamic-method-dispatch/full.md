# **Object Oriented Programming with JAVA**

## **Module: Inheritance: Inheritance Basics, Using super, Creating a Multilevel Hierarchy, When Constructors Are Called**

### Introduction

Inheritance is a fundamental concept in Object Oriented Programming (OOP) that allows one class to inherit the properties and behavior of another class. This module will delve into the basics of inheritance, including using the `super` keyword, creating a multilevel hierarchy, and understanding when constructors are called.

### Historical Context

Inheritance was first introduced in the late 19th century by Charles Babbage, an English mathematician and computer scientist. However, it wasn't until the 1960s and 1970s that inheritance became a core concept in OOP, with the development of languages such as Simula and Smalltalk.

### Executed, Method Overriding, Dynamic Method Dispatch

#### Executed

In Java, when a method is called on an object, the following sequence of events occurs:

1.  **Method lookup**: The Java Virtual Machine (JVM) searches for the method implementation in the following order:
    - The class's own method implementation
    - The superclass's method implementation
    - The superclass's superclass's method implementation
    - And so on
2.  **Method invocation**: If the method is found, the JVM invokes the method implementation.
3.  **Method execution**: The method implementation is executed, and the program flows accordingly.

#### Method Overriding

Method overriding occurs when a subclass provides a different implementation of a method that is already defined in its superclass. The subclass method has the same name, return type, and parameter list as the superclass method, but it can have a different implementation.

Here's an example of method overriding in Java:

```java
// Animal class
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound.");
    }
}

// Dog class
public class Dog extends Animal {
    public void sound() {
        System.out.println("The dog barks.");
    }
}

// Usage
public class Main {
    public static void main(String[] args) {
        Animal animal = new Dog();
        animal.sound(); // Output: The dog barks.
    }
}
```

#### Dynamic Method Dispatch

Dynamic method dispatch is the process of determining the method implementation to invoke at runtime. This is necessary because method overriding allows multiple subclasses to provide different implementations of the same method.

In Java, dynamic method dispatch occurs when the JVM uses the ` invokeDynamic` instruction to invoke a method implementation. This instruction uses the method handle, which is a unique identifier for the method implementation.

Here's an example of dynamic method dispatch in Java:

```java
// Animal class
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound.");
    }
}

// Dog class
public class Dog extends Animal {
    @Override
    public void sound() {
        System.out.println("The dog barks.");
    }
}

// Cat class
public class Cat extends Animal {
    @Override
    public void sound() {
        System.out.println("The cat meows.");
    }
}

// Usage
public class Main {
    public static void main(String[] args) {
        Animal animal = new Dog();
        animal.sound(); // Output: The dog barks.
    }
}
```

### Using Abstract Classes

Abstract classes are classes that cannot be instantiated and are designed to be inherited by other classes. Abstract classes can contain both abstract methods and concrete methods.

Here's an example of an abstract class in Java:

```java
// AbstractAnimal class
public abstract class AbstractAnimal {
    public abstract void sound();
    public void eat() {
        System.out.println("The animal eats.");
    }
}

// Dog class
public class Dog extends AbstractAnimal {
    @Override
    public void sound() {
        System.out.println("The dog barks.");
    }
}

// Cat class
public class Cat extends AbstractAnimal {
    @Override
    public void sound() {
        System.out.println("The cat meows.");
    }
}

// Usage
public class Main {
    public static void main(String[] args) {
        AbstractAnimal animal = new Dog();
        animal.sound(); // Output: The dog barks.
        animal.eat(); // Output: The animal eats.
    }
}
```

### Using Final with Inheritance

The `final` keyword is used to declare a class, method, or variable that cannot be overridden or modified. When a class inherits from a `final` class, it cannot be subclassed further.

Here's an example of using `final` with inheritance in Java:

```java
// finalAnimal class
public final class finalAnimal {
    private final String name;

    public finalAnimal(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}

// Dog class
public class Dog extends finalAnimal {
    public Dog(String name) {
        super(name);
    }
}

// Usage
public class Main {
    public static void main(String[] args) {
        finalAnimal animal = new Dog("Fido");
        System.out.println(animal.getName()); // Output: Fido
    }
}
```

### Local Variable Type Inference

Local variable type inference (LVTI) is a feature introduced in Java 10 that allows the compiler to infer the type of a local variable based on its assignment.

Here's an example of LVTI in Java:

```java
// LVTI example
public class Main {
    public static void main(String[] args) {
        String name = "John";
        int age = 30;
        System.out.println(name.toUpperCase()); // Output: JOHN
        System.out.println(age); // Output: 30
    }
}
```

### Inheritance

Inheritance is a fundamental concept in Object Oriented Programming (OOP) that allows one class to inherit the properties and behavior of another class. This module has covered the basics of inheritance, including using the `super` keyword, creating a multilevel hierarchy, and understanding when constructors are called.

### Further Reading

- "Head First Design Patterns" by Kathy Sierra and Bert Bates
- "Design Patterns: Elements of Reusable Object-Oriented Software" by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides
- "Java: A Beginner's Guide" by Herbert Schildt
- "Java: The Complete Reference" by Herbert Schildt

### Conclusion

Inheritance is a powerful tool in Object Oriented Programming (OOP) that allows one class to inherit the properties and behavior of another class. By understanding how to use `super`, create a multilevel hierarchy, and use `final` with inheritance, developers can write more efficient and effective code.

In the next module, we will explore the concept of polymorphism, which is the ability of an object to take on multiple forms.
