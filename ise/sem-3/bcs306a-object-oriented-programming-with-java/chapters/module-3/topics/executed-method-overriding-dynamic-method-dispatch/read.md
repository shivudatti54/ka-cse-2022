# **Object Oriented Programming with JAVA**

## **Inheritance Basics**

Inheritance is a fundamental concept in Object Oriented Programming (OOP) that allows one class to inherit the properties and behavior of another class. The class that is being inherited from is called the **superclass** or **parent class**, while the class that is doing the inheriting is called the **subclass** or **child class**.

**Key Concepts:**

- **Inheritance**: A class inherits the properties and behavior of another class.
- **Superclass**: The class being inherited from.
- **Subclass**: The class doing the inheriting.

## **Using super with Inheritance**

The `super` keyword is used to access the members of the superclass in a subclass.

**Example:**

```java
// Animal.java (Animal class)
public class Animal {
    public void sound() {
        System.out.println("Animal makes a sound");
    }
}

// Dog.java (Dog class that inherits from Animal)
public class Dog extends Animal {
    public void sound() {
        super.sound();
        System.out.println("Dog barks");
    }
}
```

In the above example, the `Dog` class inherits the `sound()` method from the `Animal` class and overrides it with its own implementation. The `super` keyword is used to call the `sound()` method of the superclass.

## **When Constructors Are Executed**

When a subclass is created, the constructor of the superclass is automatically executed before the constructor of the subclass.

**Example:**

```java
// Animal.java (Animal class)
public class Animal {
    public Animal() {
        System.out.println("Animal constructor executed");
    }
}

// Dog.java (Dog class that inherits from Animal)
public class Dog extends Animal {
    public Dog() {
        System.out.println("Dog constructor executed");
    }
}
```

In the above example, when a `Dog` object is created, the `Animal` constructor is executed first, followed by the `Dog` constructor.

## **Method Overriding**

Method overriding is a feature of OOP where a subclass provides a different implementation of a method that is already defined in its superclass.

**Key Concepts:**

- **Method overriding**: A subclass provides a different implementation of a method that is already defined in its superclass.
- **Polymorphism**: The ability of an object to take on multiple forms.

**Example:**

```java
// Animal.java (Animal class)
public class Animal {
    public void sound() {
        System.out.println("Animal makes a sound");
    }
}

// Dog.java (Dog class that overrides the sound() method of Animal)
public class Dog extends Animal {
    public void sound() {
        System.out.println("Dog barks");
    }
}
```

In the above example, the `Dog` class overrides the `sound()` method of the `Animal` class with its own implementation.

## **Dynamic Method Dispatch**

Dynamic method dispatch is a feature of OOP where the correct method to be executed is determined at runtime, rather than at compile time.

**Key Concepts:**

- **Dynamic method dispatch**: The correct method to be executed is determined at runtime.
- **Polymorphism**: The ability of an object to take on multiple forms.

**Example:**

```java
// Animal.java (Animal class)
public class Animal {
    public void sound() {
        System.out.println("Animal makes a sound");
    }
}

// Dog.java (Dog class that overrides the sound() method of Animal)
public class Dog extends Animal {
    public void sound() {
        System.out.println("Dog barks");
    }
}
```

In the above example, when we call the `sound()` method on an object of type `Dog`, the correct method to be executed is determined at runtime, based on the actual object type, rather than at compile time.

## **Using Abstract Classes**

Abstract classes are classes that cannot be instantiated and are used to provide a common implementation for a group of related classes.

**Key Concepts:**

- **Abstract classes**: Classes that cannot be instantiated and provide a common implementation for a group of related classes.
- **Abstract methods**: Methods that are declared in an abstract class but not implemented.

**Example:**

```java
// Animal.java (Animal.java becomes an abstract class)
public abstract class Animal {
    public abstract void sound();
}

// Dog.java (Dog class that extends Animal)
public class Dog extends Animal {
    public void sound() {
        System.out.println("Dog barks");
    }
}
```

In the above example, the `Animal` class is declared as an abstract class and contains an abstract method `sound()`. The `Dog` class extends the `Animal` class and implements the `sound()` method.

## **Using final with Inheritance**

The `final` keyword is used to declare a class, method, or variable that cannot be overridden or changed.

**Key Concepts:**

- **Final classes**: Classes that cannot be subclassed.
- **Final methods**: Methods that cannot be overridden.
- **Final variables**: Variables that cannot be changed.

**Example:**

```java
// Animal.java (Animal class becomes final)
public final class Animal {
    public final void sound() {
        System.out.println("Animal makes a sound");
    }
}

// Dog.java (Dog class extends Animal)
public class Dog extends Animal {
    // Dog.java is not allowed to add any new methods or fields
    // and override the sound() method of Animal
}
```

In the above example, the `Animal` class is declared as a `final` class, which means it cannot be subclassed. The `Dog` class is not allowed to add any new methods or fields and override the `sound()` method of `Animal`.

## **Local Variable Type Inference**

Local Variable Type Inference (LVTI) is a feature of Java that allows the compiler to infer the type of a local variable.

**Key Concepts:**

- **Local Variable Type Inference (LVTI)**: The compiler infers the type of a local variable.
- **Varargs**: Variables with a variable number of arguments.

**Example:**

```java
// MethodWithVarargs.java
public class MethodWithVarargs {
    public void printArray(int[] array) {
        for (int element : array) {
            System.out.println(element);
        }
    }

    public static void main(String[] args) {
        MethodWithVarargs method = new MethodWithVarargs();
        int[] array = {1, 2, 3, 4, 5};
        method.printArray(array);
    }
}
```

In the above example, the `printArray()` method is declared with a single parameter `array` of type `int[]`. However, when we call the method in the `main()` method, we pass an array of type `int[]`. The type `int[]` is inferred by the compiler, and the `printArray()` method is called with the correct type.
