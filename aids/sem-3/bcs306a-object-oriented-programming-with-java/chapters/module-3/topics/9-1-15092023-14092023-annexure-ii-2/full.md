# **Object Oriented Programming with JAVA**

## **Module: Inheritance: Inheritance Basics, Using super, Creating a Multilevel Hierarchy, When Constructors Are Used**

### Table of Contents

1. [Introduction to Inheritance](#introduction-to-inheritance)
2. [Historical Context of Inheritance](#historical-context-of-inheritance)
3. [Types of Inheritance](#types-of-inheritance)
4. [Using `super` Keyword](#using_super_keyword)
5. [Creating a Multilevel Hierarchy](#creating-a-multilevel-hierarchy)
6. [When Constructors Are Used](#when_constructors-are-used)
7. [Example of Multilevel Inheritance](#example-of-multilevel-inheritance)
8. [Case Study: Inheritance in Real-World Scenario](#case-study-inheritance-in-real-world-scenario)

### Introduction to Inheritance

---

Inheritance is a fundamental concept in Object Oriented Programming (OOP) that allows one class to inherit the properties and behavior of another class. This allows for code reuse and facilitates the creation of a hierarchy of classes.

Inheritance is based on the idea of "is-a" relationship between classes, where a subclass is a specialization of its superclass.

### Historical Context of Inheritance

---

The concept of inheritance was first introduced by Béraldi in 1865 and later developed by Parnas in 1972. However, it was not until the 1980s that inheritance became a widely accepted concept in the development of object-oriented languages.

The first object-oriented language, Simula 67, was released in 1966 and introduced the concept of inheritance. However, it was not until the release of Smalltalk in 1972 that inheritance became a central concept in the language.

### Types of Inheritance

---

There are several types of inheritance:

- **Single Inheritance**: A subclass inherits from a single superclass.
- **Multiple Inheritance**: A subclass inherits from multiple superclasses.
- **Multilevel Inheritance**: A subclass inherits from a superclass, which in turn inherits from another superclass.
- **Hierarchical Inheritance**: A subclass inherits from a superclass, but the superclass does not inherit from any other superclass.
- **Hybrid Inheritance**: A combination of multiple inheritance and multilevel inheritance.

### Using `super` Keyword

---

The `super` keyword is used to access the members of the superclass from a subclass.

```java
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound.");
    }
}

public class Dog extends Animal {
    public void sound() {
        System.out.println("The dog barks.");
        super.sound(); // Accessing the sound method from the Animal class
    }
}
```

In the above example, the `Dog` class extends the `Animal` class and overrides the `sound()` method. However, it also calls the `sound()` method from the `Animal` class using the `super` keyword.

### Creating a Multilevel Hierarchy

---

A multilevel hierarchy is a type of inheritance where a subclass inherits from a superclass, which in turn inherits from another superclass.

```java
public class Animal {
    public void eat() {
        System.out.println("The animal eats.");
    }
}

public class Mammal extends Animal {
    public void nurse() {
        System.out.println("The mammal nurses.");
    }
}

public class Dog extends Mammal {
    public void bark() {
        System.out.println("The dog barks.");
    }
}
```

In the above example, the `Dog` class extends the `Mammal` class, which in turn extends the `Animal` class.

### When Constructors Are Used

---

Constructors are used to initialize objects when they are created. When using inheritance, constructors are used to initialize objects in the subclass.

```java
public class Animal {
    public Animal(String name) {
        this.name = name;
    }
    String name;
}

public class Dog extends Animal {
    public Dog(String name) {
        super(name); // Calling the constructor from the Animal class
    }
}
```

In the above example, the `Dog` class extends the `Animal` class and calls the constructor from the `Animal` class using the `super` keyword.

### Example of Multilevel Inheritance

---

```java
public class Animal {
    public void eat() {
        System.out.println("The animal eats.");
    }
}

public class Mammal extends Animal {
    public void nurse() {
        System.out.println("The mammal nurses.");
    }
}

public class Carnivore extends Mammal {
    public void hunt() {
        System.out.println("The carnivore hunts.");
    }
}

public class Dog extends Carnivore {
    public void bark() {
        System.out.println("The dog barks.");
    }
}
```

In the above example, the `Dog` class extends the `Carnivore` class, which in turn extends the `Mammal` class, which in turn extends the `Animal` class.

### Case Study: Inheritance in Real-World Scenario

---

Suppose we want to create a system to manage employees in a company. We can create a class `Employee` that has attributes such as `name`, `age`, and `salary`. We can then create subclasses such as `Manager`, `Developer`, and `Designer` that inherit from the `Employee` class and add additional attributes and methods specific to each role.

```java
public class Employee {
    public String name;
    public int age;
    public double salary;

    public Employee(String name, int age, double salary) {
        this.name = name;
        this.age = age;
        this.salary = salary;
    }

    public void displayDetails() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Salary: " + salary);
    }
}

public class Manager extends Employee {
    public String department;

    public Manager(String name, int age, double salary, String department) {
        super(name, age, salary);
        this.department = department;
    }

    public void displayDetails() {
        super.displayDetails();
        System.out.println("Department: " + department);
    }
}

public class Developer extends Employee {
    public String programmingLanguage;

    public Developer(String name, int age, double salary, String programmingLanguage) {
        super(name, age, salary);
        this.programmingLanguage = programmingLanguage;
    }

    public void displayDetails() {
        super.displayDetails();
        System.out.println("Programming Language: " + programmingLanguage);
    }
}
```

In the above example, the `Manager` and `Developer` classes extend the `Employee` class and add additional attributes and methods specific to each role.

### Further Reading

---

- "Head First Design Patterns" by Kathy Sierra and Bert Bates
- "Design Patterns: Elements of Reusable Object-Oriented Software" by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlisides
- "Object-Oriented Software Construction" by Bertrand Meyer
