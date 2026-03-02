# **Object Oriented Programming with JAVA**

## **Inheritance: Inheritance Basics, Using super, Creating a Multilevel Hierarchy, When Constructors Are Used**

## **Introduction**

Inheritance is a fundamental concept in Object Oriented Programming (OOP) that allows one class to inherit the properties and behavior of another class. The inheriting class is called the subclass or derived class, while the class being inherited from is called the superclass or base class. In this section, we will explore the basics of inheritance in Java, including using the `super` keyword, creating a multilevel hierarchy, and when constructors are used.

## **Historical Context**

The concept of inheritance dates back to the 1930s, when it was first introduced by Dr. Ludwig Wittgenstein in his Philosophical Investigations. However, it was not until the 1970s that object-oriented programming (OOP) gained popularity, and inheritance became a key feature of OOP languages such as Smalltalk and Simula. Java, developed in the mid-1990s, adopted inheritance as a core concept, and it has since become a fundamental aspect of Java programming.

## **Using the `super` Keyword**

The `super` keyword is used to access the members of the superclass from a subclass. When a subclass is instantiated, it calls the superclass's constructor using the `super()` method. The `super` keyword is used to call a superclass member, such as a method or a variable, from a subclass.

```java
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound.");
    }
}

public class Dog extends Animal {
    public void sound() {
        super.sound(); // Calls the Animal.sound() method
        System.out.println("The dog barks.");
    }
}
```

In the above example, the `Dog` class extends the `Animal` class and overrides the `sound()` method. However, it still calls the `Animal.sound()` method using the `super` keyword.

## **Creating a Multilevel Hierarchy**

A multilevel hierarchy is a class hierarchy where a subclass is itself a subclass of another subclass. This type of hierarchy is also known as a nested class hierarchy.

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
```

In the above example, the `Carnivore` class extends the `Mammal` class, which in turn extends the `Animal` class. This creates a multilevel hierarchy where `Carnivore` is a subclass of `Mammal`, and `Mammal` is a subclass of `Animal`.

## **When Constructors Are Used**

Constructors are special methods in Java that are used to initialize objects. When a subclass is instantiated, it calls the superclass's constructor using the `super()` method. However, if a subclass does not explicitly call the superclass's constructor using `super()`, the compiler will insert a call to the superclass's no-arg constructor.

```java
public class Animal {
    public Animal() {
        System.out.println("The animal is created.");
    }
}

public class Dog extends Animal {
    public Dog() {
        System.out.println("The dog is created.");
    }
}
```

In the above example, the `Dog` class extends the `Animal` class and does not explicitly call the superclass's constructor. However, the compiler will insert a call to the superclass's no-arg constructor, resulting in the following output:

```
The animal is created.
The dog is created.
```

## **Case Study: Creating a Multilevel Hierarchy for a University**

Suppose we want to create a multilevel hierarchy to represent the academic departments and faculty members of a university. We can create the following classes:

- `Department`: represents a university department
- `Faculty`: represents a faculty member
- `Professor`: represents a professor
- `Lecturer`: represents a lecturer

```java
public class Department {
    private String name;

    public Department(String name) {
        this.name = name;
    }

    public void displayDetails() {
        System.out.println("Department Name: " + name);
    }
}

public class Faculty {
    private String name;
    private Department department;

    public Faculty(String name, Department department) {
        this.name = name;
        this.department = department;
    }

    public void displayDetails() {
        System.out.println("Faculty Name: " + name);
        department.displayDetails();
    }
}

public class Professor extends Faculty {
    private String subject;

    public Professor(String name, Department department, String subject) {
        super(name, department);
        this.subject = subject;
    }

    public void displayDetails() {
        super.displayDetails();
        System.out.println("Subject: " + subject);
    }
}

public class Lecturer extends Faculty {
    private String subject;

    public Lecturer(String name, Department department, String subject) {
        super(name, department);
        this.subject = subject;
    }

    public void displayDetails() {
        super.displayDetails();
        System.out.println("Subject: " + subject);
    }
}
```

We can create an instance of the `Professor` class and display the details of the department, faculty, and professor:

```java
public class Main {
    public static void main(String[] args) {
        Department csDepartment = new Department("Computer Science");
        Faculty faculty = new Professor("John Doe", csDepartment, "Algorithms");
        faculty.displayDetails();
    }
}
```

This will output:

```
Department Name: Computer Science
Faculty Name: John Doe
Department Name: Computer Science
Subject: Algorithms
```

## **Conclusion**

Inheritance is a powerful feature in Object Oriented Programming that allows one class to inherit the properties and behavior of another class. In this section, we have explored the basics of inheritance in Java, including using the `super` keyword, creating a multilevel hierarchy, and when constructors are used. We have also created a case study to demonstrate the use of a multilevel hierarchy in a real-world scenario.
