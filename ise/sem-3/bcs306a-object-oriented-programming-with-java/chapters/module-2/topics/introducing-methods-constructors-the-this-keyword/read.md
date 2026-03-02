# **Introducing Methods, Constructors, The this Keyword, Garbage Collection**

## **Table of Contents**

- [Introducing Methods](#introducing-methods)
- [Constructors](#constructors)
- [The this Keyword](#the-this-keyword)
- [Garbage Collection](#garbage-collection)

## **Introducing Methods**

- **Definition:** A method is a block of code that can be executed multiple times from different parts of a program.
- **Purpose:** Methods help organize code, reduce duplication, and improve code readability.
- **Types of Methods:**
  - **Instance Methods:** Access and modify instance variables.
  - **Static Methods:** Shared by all instances of a class.
  - **Abstract Methods:** Declared but not implemented.
- **Method Syntax:**

      ```java

  public static void main(String[] args) {
  // Method declaration (return type, method name, parameters)
  void printMessage(String message) {
  // Method body
  System.out.println(message);
  }
  }

````

**Constructors**
----------------

*   **Definition:** A constructor is a special method that is used to initialize objects when they are created.
*   **Purpose:** Constructors set the initial state of an object.
*   **Types of Constructors:**
    *   **Parameterized Constructors:** Take arguments when called.
    *   **No-Argument Constructors:** Take no arguments when called.
*   **Constructor Syntax:**

    ```java
public class Person {
    // No-argument constructor
    public Person() {
        // Initialize object state
    }

    // Parameterized constructor
    public Person(String name) {
        // Initialize object state with name
    }
}
````

## **The this Keyword**

- **Definition:** The `this` keyword is used to refer to the current object.
- **Purpose:** The `this` keyword provides access to the current object's state.
- **Example:**

      ```java

  public class Person {
  private String name;

      public Person(String name) {
          this.name = name; // Use this to set the name
      }

      public void printName() {
          System.out.println(this.name); // Use this to access the name
      }

  }

````

**Garbage Collection**
---------------------

*   **Definition:** Garbage collection is a process that automatically frees memory occupied by objects that are no longer needed.
*   **Purpose:** Garbage collection reduces memory leaks and improves program performance.
*   **How Garbage Collection Works:**
    *   **Reference Counting:** Keep track of object references.
    *   **Mark-and-Sweep:** Mark reachable objects and sweep away unreachable objects.

Note: Java uses a generational approach to garbage collection, dividing objects into three generations based on their lifetimes.

```java
public class GarbageCollection {
    public static void main(String[] args) {
        // Create an object
        Object obj = new Object();

        // Allow the object to be garbage collected
        obj = null;

        // Force garbage collection
        System.gc();
    }
}
````

## **Key Concepts Summary**

- **Methods:** Organize code, reduce duplication, and improve code readability.
- **Constructors:** Initialize objects when created.
- **The `this` Keyword:** Access the current object's state.
- **Garbage Collection:** Automatically free memory occupied by objects that are no longer needed.
