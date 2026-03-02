# Object-Oriented Programming with JAVA

### Principles)

Object-oriented programming (OOP) is a programming paradigm that revolves around the concept of objects and classes. The principles of OOP provide the foundation for designing and developing robust, maintainable, and scalable software systems. In this section, we will delve into the key principles of OOP.

#### 1. Abstraction

Abstraction is the process of hiding the implementation details of an object from the user and exposing only the necessary information through public interfaces. This helps to reduce complexity, improve modularity, and increase reusability.

```java
// Example of abstraction in Java
public class Car {
    private Engine engine;

    public Car(Engine engine) {
        this.engine = engine;
    }

    public void accelerate() {
        engine.accelerate();
    }

    public void brake() {
        engine.brake();
    }
}

public class Engine {
    public void accelerate() {
        System.out.println("Accelerating...");
    }

    public void brake() {
        System.out.println("Braking...");
    }
}
```

In this example, the `Car` class abstracts the `Engine` class, hiding its implementation details and exposing only the necessary methods through the public interface.

#### 2. Encapsulation

Encapsulation is the process of bundling data and methods that operate on that data within a single unit, called a class. This helps to hide the internal state of an object from the outside world and ensures data integrity.

```java
// Example of encapsulation in Java
public class BankAccount {
    private double balance;

    public BankAccount(double balance) {
        this.balance = balance;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public void withdraw(double amount) {
        balance -= amount;
    }

    public double getBalance() {
        return balance;
    }
}
```

In this example, the `BankAccount` class encapsulates the `balance` data, providing controlled access through the `deposit`, `withdraw`, and `getBalance` methods.

#### 3. Inheritance

Inheritance is the process of creating a new class based on an existing class. The new class, called the subclass or derived class, inherits the properties and behavior of the existing class, called the superclass or base class.

```java
// Example of inheritance in Java
public class Animal {
    public void eat() {
        System.out.println("Eating...");
    }
}

public class Dog extends Animal {
    public void bark() {
        System.out.println("Barking...");
    }
}
```

In this example, the `Dog` class inherits the `eat` method from the `Animal` class and adds its own `bark` method.

#### 4. Polymorphism

Polymorphism is the ability of an object to take on multiple forms. This can be achieved through method overriding or method overloading.

```java
// Example of polymorphism in Java
public class Shape {
    public void area() {
        System.out.println("Area...");
    }
}

public class Circle extends Shape {
    public void area() {
        System.out.println("Circle area...");
    }
}

public class Rectangle extends Shape {
    public void area() {
        System.out.println("Rectangle area...");
    }
}
```

In this example, the `Circle` and `Rectangle` classes override the `area` method of the `Shape` class, demonstrating polymorphism.

### Using Blocks of Code

Blocks of code are used to group related statements together. They can be used to improve code readability, maintainability, and reusability.

#### 1. If-Else Statements

If-else statements are used to execute different blocks of code based on conditions.

```java
// Example of if-else statements in Java
public class Example {
    public static void main(String[] args) {
        int age = 25;
        if (age >= 18) {
            System.out.println("Adult");
        } else {
            System.out.println("Minor");
        }
    }
}
```

#### 2. Loops

Loops are used to execute a block of code repeatedly.

```java
// Example of loops in Java
public class Example {
    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            System.out.println("Hello, World!");
        }
    }
}
```

#### 3. Switch Statements

Switch statements are used to execute different blocks of code based on a variable.

```java
// Example of switch statements in Java
public class Example {
    public static void main(String[] args) {
        int day = 3;
        switch (day) {
            case 1:
                System.out.println("Monday");
                break;
            case 2:
                System.out.println("Tuesday");
                break;
            case 3:
                System.out.println("Wednesday");
                break;
        }
    }
}
```

### Lexical Issues

Lexical issues refer to problems related to the syntax and structure of programming languages, particularly in Java.

#### 1. Whitespace

Whitespace in Java refers to the space characters used to separate tokens.

```java
// Example of whitespace in Java
public class Example {
    public static void main(String[] args) {
        System.out.println("Hello World");
        System.out.println("   Hello   World");
    }
}
```

In this example, the first line of code is valid, while the second line is invalid due to excessive whitespace.

#### 2. Identifiers

Identifiers in Java refer to names given to variables, methods, and classes.

```java
// Example of identifiers in Java
public class Example {
    public static void main(String[] args) {
        int x = 5; // valid identifier
        5x = 10; // invalid identifier (variable name must start with a letter)
    }
}
```

In this example, the variable name `x` is a valid identifier, while `5x` is not.

#### 3. Literals

Literals in Java refer to values that are represented directly in source code.

```java
// Example of literals in Java
public class Example {
    public static void main(String[] args) {
        int x = 5; // literal
        String y = "Hello"; // literal
    }
}
```

In this example, `5` and `"Hello"` are literals.

#### 4. Comments

Comments in Java refer to notes added to source code to provide additional information or explain the code.

```java
// Example of comments in Java
public class Example {
    public static void main(String[] args) {
        // This is a comment
        System.out.println("Hello World");
    }
}
```

In this example, the line `// This is a comment` is a comment.

#### 5. Separators

Separators in Java refer to special characters used to separate tokens.

```java
// Example of separators in Java
public class Example {
    public static void main(String[] args) {
        int x = 5; // valid token
        // x = 5; // invalid separator (assignment operator is not a separator)
    }
}
```

In this example, the `=` character is a separator, while `x = 5` is invalid due to excessive whitespace.

#### 6. Java Keywords

Java keywords refer to reserved words that have specific meanings in the Java programming language.

```java
// Example of Java keywords
public class Example {
    public static void main(String[] args) {
        int x = 5; // keyword: int
        String y = "Hello"; // keyword: String
    }
}
```

In this example, `int` and `String` are Java keywords.

### Further Reading

- "Head First Java" by Kathy Sierra and Bert Bates
- "Java: A Beginner's Guide" by Herbert Schildt
- "Effective Java" by Joshua Bloch

Note: This is a comprehensive guide to the principles, blocks of code, lexical issues, and Java keywords. It is designed to be a detailed resource for learning Java programming.
