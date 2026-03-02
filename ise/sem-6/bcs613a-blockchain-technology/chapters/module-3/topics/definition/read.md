# Class Definition and Access Specifiers in C++

## Introduction to Classes and Objects

Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to design applications and computer programs. These objects are organized around data, in the form of fields (often known as attributes or properties), and code, in the form of procedures (often known as methods).

In C++, a **class** is a user-defined data type that serves as a blueprint for creating objects. An **object** is an instance of a class. Think of a class as a cookie cutter and objects as the cookies made from it.

## What is a Class?

A class is a collection of related data (member variables) and functions (member functions) that operate on that data. It encapsulates data and behavior into a single logical unit.

### Basic Class Syntax

```cpp
class ClassName {
    // Access specifier
    // Member variables (data members)
    // Member functions (methods)
};
```

### Example: Simple Class Definition

```cpp
class Rectangle {
public:
    double length;
    double width;
    
    double calculateArea() {
        return length * width;
    }
    
    double calculatePerimeter() {
        return 2 * (length + width);
    }
};
```

## Access Specifiers: Controlling Visibility

Access specifiers determine how the members (attributes and methods) of a class can be accessed. C++ provides three access specifiers:

### 1. Public Access Specifier (`public:`)

Members declared as public are accessible from anywhere in the program where the class object is visible.

```cpp
class Student {
public:
    string name;        // Public attribute
    void display() {    // Public method
        cout << "Name: " << name;
    }
};

int main() {
    Student s1;
    s1.name = "Alice";  // Direct access allowed
    s1.display();       // Direct access allowed
    return 0;
}
```

### 2. Private Access Specifier (`private:`)

Members declared as private are accessible only within the class itself. This is the default access level for class members.

```cpp
class BankAccount {
private:
    double balance;      // Private attribute
    
public:
    void deposit(double amount) {
        balance += amount;  // Accessible within class
    }
    
    double getBalance() {
        return balance;     // Accessible within class
    }
};

int main() {
    BankAccount acc;
    // acc.balance = 1000;  // Error: private member
    acc.deposit(1000);      // OK: public method
    cout << acc.getBalance(); // OK: public method
    return 0;
}
```

### 3. Protected Access Specifier (`protected:`)

Members declared as protected are accessible within the class and by derived classes (through inheritance). We'll explore this more in the inheritance module.

```cpp
class Vehicle {
protected:
    int speed;          // Protected attribute
    
public:
    void setSpeed(int s) {
        speed = s;      // Accessible within class
    }
};

class Car : public Vehicle {
public:
    void displaySpeed() {
        cout << "Speed: " << speed; // Accessible in derived class
    }
};
```

## Class Declaration vs. Definition

### Class Declaration
Declares the class name and its members without implementation.

```cpp
class Calculator;  // Forward declaration

class Calculator {
public:
    double add(double a, double b);
    double subtract(double a, double b);
    // ... other member function declarations
};
```

### Class Definition
Includes the implementation of member functions.

```cpp
// Definition outside class using scope resolution operator ::
double Calculator::add(double a, double b) {
    return a + b;
}

double Calculator::subtract(double a, double b) {
    return a - b;
}
```

## Data Hiding and Encapsulation

Encapsulation is one of the fundamental OOP concepts that binds together the data and functions that manipulate the data, keeping both safe from outside interference and misuse.

### Benefits of Encapsulation:
- **Data Hiding**: Internal implementation is hidden from users
- **Increased Flexibility**: Can change implementation without affecting users
- **Reusability**: Encapsulated code can be reused across programs
- **Testing**: Easier to test and debug

### Example: Encapsulated Class

```cpp
class Temperature {
private:
    double celsius;     // Private data member
    
public:
    // Public interface to access private data
    void setCelsius(double c) {
        celsius = c;
    }
    
    void setFahrenheit(double f) {
        celsius = (f - 32) * 5/9;
    }
    
    double getCelsius() {
        return celsius;
    }
    
    double getFahrenheit() {
        return (celsius * 9/5) + 32;
    }
};
```

## Struct vs. Class Comparison

| Feature | struct | class |
|---------|--------|-------|
| Default Access | public | private |
| Inheritance | public by default | private by default |
| Usage | Simple data containers | Complex objects with behavior |
| Memory Layout | Same as class | Same as struct |

```cpp
// Struct example (public by default)
struct Point {
    int x, y;  // Public by default
};

// Class example (private by default)
class PointClass {
    int x, y;  // Private by default
public:
    PointClass(int a, int b) : x(a), y(b) {}
};
```

## Inline Member Functions

Member functions can be defined inside the class definition, making them inline by default.

```cpp
class MathOperations {
public:
    // Inline function defined inside class
    int square(int x) {
        return x * x;
    }
    
    // Function declaration only
    int cube(int x);
};

// Outside definition (not inline by default)
int MathOperations::cube(int x) {
    return x * x * x;
}
```

## Constant Member Functions

Member functions that don't modify object state should be declared as const.

```cpp
class Circle {
private:
    double radius;
    
public:
    Circle(double r) : radius(r) {}
    
    // Const member function - doesn't modify object
    double getArea() const {
        return 3.14159 * radius * radius;
    }
    
    // Non-const member function - modifies object
    void setRadius(double r) {
        radius = r;
    }
};
```

## Best Practices for Class Design

1. **Use meaningful names**: Class names should be nouns, method names should be verbs
2. **Keep classes focused**: Each class should have a single responsibility
3. **Use access specifiers appropriately**: Make data members private by default
4. **Provide constructors**: Initialize objects to valid states
5. **Use const correctness**: Mark methods that don't modify state as const
6. **Prefer composition over inheritance**: When possible, use has-a relationships

## ASCII Diagram: Class Structure

```
+-----------------------+
|       Class Name      |
+-----------------------+
|   - private members   |
|   + public members    |
|   # protected members |
+-----------------------+
        ^
        |
        | instantiation
        |
+-----------------------+
|       Object          |
+-----------------------+
|   State (data)        |
|   Behavior (methods)   |
+-----------------------+
```

## Exam Tips

1. **Remember default access**: Class members are private by default, struct members are public by default
2. **Understand encapsulation**: Be able to explain why data hiding is important
3. **Know the difference**: Between class declaration and definition
4. **Practice syntax**: Be comfortable with scope resolution operator (::)
5. **Identify errors**: Common mistakes include accessing private members directly
6. **Think about design**: When to use public vs private vs protected access