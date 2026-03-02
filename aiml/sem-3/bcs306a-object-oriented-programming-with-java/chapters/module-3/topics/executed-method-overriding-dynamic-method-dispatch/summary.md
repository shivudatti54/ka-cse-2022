# **Inheritance Basics: Key Points**

## **I. Executed Methods**

- In Java, the order of execution for methods is:
  - Constructors
  - Instance initialization block
  - Instance methods
  - Static methods
- Example:
  ```java
  public class Parent {
  public void executeMethod() {
  System.out.println("Parent method executed");
  }

      public static void main(String[] args) {
          Parent parent = new Parent();
          parent.executeMethod(); // Output: Parent method executed
      }

  }

````

**II. Method Overriding**
-------------------------

*   Method overriding:
    *   A method in a subclass with the same method signature as in the superclass.
    *   The method in the subclass may have a different return type or throw different exceptions.
*   Example:
    ```java
public class Parent {
    public void method() {
        System.out.println("Parent method");
    }
}

public class Child extends Parent {
    @Override
    public void method() {
        System.out.println("Child method");
    }
}
````

## **III. Dynamic Method Dispatch**

- Dynamic method dispatch:
  - The Java Virtual Machine (JVM) resolves the method call at runtime.
  - The JVM uses the `hashCode()` and `equals()` methods to determine the method to call.
- Example:
  ```java
  public class Animal {
  public void sound() {
  System.out.println("Animal makes a sound");
  }
  }

public class Dog extends Animal {
@Override
public void sound() {
System.out.println("Dog barks");
}
}

public class Main {
public static void main(String[] args) {
Animal animal = new Dog();
animal.sound(); // Output: Dog barks
}
}

````

**IV. Using Abstract Classes**
-----------------------------

*   Abstract classes:
    *   A class that cannot be instantiated.
    *   A class that provides a partial implementation of a class.
*   Example:
    ```java
public abstract class Animal {
    public abstract void sound();
}

public class Dog extends Animal {
    @Override
    public void sound() {
        System.out.println("Dog barks");
    }
}
````

## **V. Using final with Inheritance**

- The `final` keyword:
  - Used to declare a constant.
  - Used to declare a class with no subclasses.
- Example:
  ```java
  public final class Animal {
  // ...
  }

public class Dog extends Animal {
// Error: Cannot inherit from final class Animal
}

````

**VI. Local Variable Type Inference (var keyword)**
------------------------------------------------

*   Introduced in Java 10:
    *   Allows the compiler to infer the type of a local variable.
*   Example:
    ```java
public class Main {
    public static void main(String[] args) {
        var animal = new Animal();
        animal.sound(); // No explicit type required
    }
}
````

## **VII. Inheritance**

- Inheritance:
  - A mechanism to build new classes from existing classes.
  - The subclass inherits the properties and behavior of the superclass.
- Example:
  ```java
  public class Parent {
  public void method() {
  System.out.println("Parent method");
  }
  }

public class Child extends Parent {
// Inheritance example
}

```

```
