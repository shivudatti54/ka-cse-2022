# Chapter 6: Introducing Classes

==============================

In this chapter, we will delve into the world of object-oriented programming (OOP) with Java, focusing on the fundamentals of classes. We will explore what classes are, how to declare them, and how to assign object reference variables. By the end of this chapter, you will have a solid understanding of the basics of OOP in Java.

## What is a Class?

---

A class in Java is a blueprint or a template that defines the characteristics and behavior of an object. It is a user-defined data type that encapsulates data and provides methods to manipulate that data. Think of a class as a design pattern or a template that you can reuse to create multiple objects with similar properties and behaviors.

### Characteristics of a Class

- A class is a abstract concept that represents a real-world entity or a concept.
- A class has a name, which is used to identify it.
- A class has attributes, which are also known as data members or fields.
- A class has methods, which are also known as functions or procedures.

### Benefits of Using Classes

- Reusability: Classes can be reused to create multiple objects with similar properties and behaviors.
- Encapsulation: Classes encapsulate data and behavior, making it easier to modify and extend.
- Abstraction: Classes provide a level of abstraction, hiding the implementation details and exposing only the necessary information.

## Declaring Classes

---

In Java, you declare a class using the `class` keyword followed by the name of the class. The name of a class should be a valid Java identifier, which means it should start with a letter, underscore, or dollar sign, and can contain letters, digits, underscores, or dollar signs.

### Example of Declaring a Class

```java
public class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}
```

In the above example, we declare a class named `Person` with two private attributes: `name` and `age`. We also provide a constructor to initialize these attributes and two getter methods to access them.

## Assigning Object Reference Variables

---

Once you have declared a class, you can create objects from it and assign them to object reference variables. An object reference variable is a variable that holds the memory address of an object.

### Example of Assigning Object Reference Variables

```java
public class Main {
    public static void main(String[] args) {
        // Declare an object reference variable
        Person person;

        // Create an object from the Person class
        person = new Person("John Doe", 30);

        // Access the attributes of the object
        System.out.println("Name: " + person.getName());
        System.out.println("Age: " + person.getAge());
    }
}
```

In the above example, we declare an object reference variable `person` and assign it the memory address of an object created from the `Person` class. We then access the attributes of the object using the getter methods.

## Constructors

---

A constructor is a special method that is called when an object is created from a class. It is used to initialize the attributes of the object.

### Example of Constructors

```java
public class Person {
    private String name;
    private int age;

    // Constructor with two parameters
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Constructor with two parameters and default values
    public Person(String name, int age, String address) {
        this.name = name;
        this.age = age;
        this.address = address;
    }
}
```

In the above example, we declare two constructors for the `Person` class. The first constructor takes two parameters: `name` and `age`. The second constructor takes three parameters: `name`, `age`, and `address`.

## Methods

---

A method is a block of code that performs a specific task. It can take arguments and return values.

### Example of Methods

```java
public class Person {
    private String name;
    private int age;

    // Method to display the person's information
    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }

    // Method to increment the person's age
    public void incrementAge() {
        age++;
    }
}
```

In the above example, we declare two methods for the `Person` class: `displayInfo` and `incrementAge`. The `displayInfo` method prints the person's information, while the `incrementAge` method increments the person's age.

## Case Study: Bank Account Management System

---

Suppose we want to create a bank account management system using classes. We can create a `BankAccount` class with attributes like account number, account holder's name, and balance. We can also create methods to deposit, withdraw, and display the account information.

### Example Code

```java
public class BankAccount {
    private int accountNumber;
    private String accountHolderName;
    private double balance;

    public BankAccount(int accountNumber, String accountHolderName, double balance) {
        this.accountNumber = accountNumber;
        this.accountHolderName = accountHolderName;
        this.balance = balance;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public void withdraw(double amount) {
        if (balance >= amount) {
            balance -= amount;
        } else {
            System.out.println("Insufficient funds");
        }
    }

    public void displayInfo() {
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Account Holder's Name: " + accountHolderName);
        System.out.println("Balance: " + balance);
    }
}
```

In the above example, we declare a `BankAccount` class with attributes like `accountNumber`, `accountHolderName`, and `balance`. We also create methods to deposit, withdraw, and display the account information.

## Application: Employee Management System

---

Suppose we want to create an employee management system using classes. We can create an `Employee` class with attributes like employee ID, name, and salary. We can also create methods to display the employee information, increment the salary, and deduct taxes.

### Example Code

```java
public class Employee {
    private int employeeId;
    private String name;
    private double salary;

    public Employee(int employeeId, String name, double salary) {
        this.employeeId = employeeId;
        this.name = name;
        this.salary = salary;
    }

    public void displayInfo() {
        System.out.println("Employee ID: " + employeeId);
        System.out.println("Name: " + name);
        System.out.println("Salary: " + salary);
    }

    public void incrementSalary(double amount) {
        salary += amount;
    }

    public void deductTaxes(double amount) {
        salary -= amount;
    }
}
```

In the above example, we declare an `Employee` class with attributes like `employeeId`, `name`, and `salary`. We also create methods to display the employee information, increment the salary, and deduct taxes.

## Further Reading

---

- "Head First Java" by Kathy Sierra and Bert Bates
- "Java: A Beginner's Guide" by Herbert Schildt
- "Java Programming: From Problem Analysis" by Herbert Schildt
- "Java: The Complete Reference" by Herbert Schildt
- "Java Tutorial" by Oracle Corporation

By following this chapter, you should now have a solid understanding of classes and object-oriented programming in Java. Remember to practice writing classes and objects to reinforce your learning.
