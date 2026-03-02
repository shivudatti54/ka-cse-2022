# **Chapter 6: Introducing Classes**

## **6.1 Introduction to Classes**

In Object Oriented Programming (OOP), a class is a blueprint for creating objects that share similar characteristics and behavior. A class defines the properties and methods of an object, and provides a way to create multiple objects from a single class definition.

## **6.2 Class Fundamentals**

A class consists of:

- **Class Definition**: A statement that defines a new class.
- **Class Members**: The data and methods that are part of the class.
- **Instantiation**: The process of creating an object from a class.

**Key Concepts:**

- **Access Modifiers**: Modifiers that control access to class members (e.g. `public`, `private`, `protected`).
- **Inheritance**: The process by which one class can inherit the properties and methods of another class.
- **Polymorphism**: The ability of an object to take on multiple forms.

**Example:**

```java
public class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}
```

## **6.3 Declaring Objects**

An object is created from a class using the `new` keyword. The object reference variable is used to refer to the object.

**Key Concepts:**

- **Object Reference Variables**: Variables that hold a reference to an object.
- **Object Initialization**: The process of initializing an object's state using the class constructor.

**Example:**

```java
Person person = new Person("John Doe", 30);
person.displayInfo();
```

## **6.4 Assigning Object Reference Variables**

Object reference variables are used to refer to the object created from the class.

**Key Concepts:**

- **Assignment Operator**: The operator used to assign a value to a variable (e.g. `=`).
- **Object Reference Variable Assignment**: The process of assigning an object reference variable to a new object.

**Example:**

```java
Person person1 = new Person("John Doe", 30);
Person person2 = person1;
person1.displayInfo();
```

## **6.5 Key Takeaways**

- A class is a blueprint for creating objects that share similar characteristics and behavior.
- Class members include data and methods that are part of the class.
- Instantiation is the process of creating an object from a class.
- Object reference variables are used to refer to the object created from the class.
