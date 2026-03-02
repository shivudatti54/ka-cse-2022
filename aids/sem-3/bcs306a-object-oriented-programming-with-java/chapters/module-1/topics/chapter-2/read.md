# **Object Oriented Programming with JAVA**

## **Chapter 2: An Overview of Java: Object-Oriented Programming (Two Paradigms, Abstraction, The Three OOP**

## **What is Object Oriented Programming (OOP)?**

Object Oriented Programming (OOP) is a programming paradigm that revolves around the concept of objects and classes. It's a way of designing, implementing, and writing code that's reusable, maintainable, and easy to understand.

### Two Paradigms of OOP

There are two main paradigms of OOP:

- **Class-Based Programming**: This paradigm is based on the concept of classes and objects. A class is a blueprint or a template that defines the properties and behavior of an object. An object is an instance of a class, and it has its own set of attributes (data) and methods (functions).
- **Prototype-Based Programming**: This paradigm is based on the concept of prototypes or blueprints. A prototype is a pre-existing object that can be used as a template to create new objects.

### Abstraction

Abstraction is a fundamental concept in OOP that allows us to hide the implementation details of an object and show only the necessary information to the outside world. Abstraction helps to reduce complexity and improve modularity.

**Abstraction Definition**: Abstraction is the process of showing only the necessary information to the outside world while hiding the implementation details.

**Example of Abstraction**:

```java
public class BankAccount {
    private double balance;

    public BankAccount(double balance) {
        this.balance = balance;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public void withdraw(double amount) {
        balance -= amount;
    }
}
```

In this example, the BankAccount class abstracts the implementation details of the account balance, deposits, and withdrawals. The outside world can only interact with the object through the provided methods, without knowing the internal implementation details.

### The Three OOP Principles

There are three fundamental principles of OOP:

- **Encapsulation**: Encapsulation is the concept of bundling data and methods that operate on that data within a single unit, called a class or object. It helps to hide the implementation details and show only the necessary information to the outside world.
- **Inheritance**: Inheritance is the concept of creating a new class based on an existing class. The new class inherits the properties and behavior of the existing class and can also add new properties and behavior.
- **Polymorphism**: Polymorphism is the concept of having multiple forms of a class or method. It allows an object of one class to be treated as an object of another class, and vice versa.

### Key Concepts

- **Class**: A blueprint or a template that defines the properties and behavior of an object.
- **Object**: An instance of a class, with its own set of attributes (data) and methods (functions).
- **Abstraction**: The process of showing only the necessary information to the outside world while hiding the implementation details.
- **Encapsulation**: Bundling data and methods that operate on that data within a single unit, called a class or object.
- **Inheritance**: Creating a new class based on an existing class, inheriting the properties and behavior of the existing class.
- **Polymorphism**: Having multiple forms of a class or method, allowing an object of one class to be treated as an object of another class, and vice versa.
