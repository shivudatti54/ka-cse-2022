# Inheritance Basics in Java

=====================================

### Key Points

- Inheritance is a mechanism in Java where one class can inherit the properties and behavior of another class.
- The class that is being inherited is called the **Superclass** or **Parent Class**, while the class that is doing the inheriting is called the **Subclass** or **Child Class**.
- The keyword used to inherit a class is `extends`.
- The `super` keyword is used to access the members of the superclass.
- A subclass can have its own constructor, which is called when an object of the subclass is created.

### Super and Subclass Relationship

|     | Superclass (Parent)                           | Subclass (Child)                                                                             |
| --- | --------------------------------------------- | -------------------------------------------------------------------------------------------- |
| 1   | Can have its own properties and methods       | Can have its own properties and methods, inherits properties and methods from the superclass |
| 2   | Can have its own constructor                  | Can have its own constructor, also inherits the constructor of the superclass                |
| 3   | Can be modified or overridden by the subclass | Cannot be modified or overridden by the subclass                                             |

### Important Formulas and Definitions

- **Inheritance**: When a new class is derived from an existing class, it is said to have inherited the properties and behavior of the existing class.
- **Superclass**: The class that is being inherited, also known as the parent class.
- **Subclass**: The class that is doing the inheriting, also known as the child class.
- **Extends**: The keyword used to inherit a class.

### Theorem: Liskov Substitution Principle (LSP)

- **If** S is a subtype of T**, then for every application of T**, the same expression should be valid for S\*\*.

### Example

```java
// Superclass (Parent)
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound.");
    }
}

// Subclass (Child)
public class Dog extends Animal {
    public void sound() {
        System.out.println("The dog barks.");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog myDog = new Dog();
        myDog.sound();  // Output: The dog barks.
    }
}
```
