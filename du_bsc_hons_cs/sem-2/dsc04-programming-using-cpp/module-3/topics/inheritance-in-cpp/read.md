# Inheritance in C++
## Introduction

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows one class to inherit the properties and behavior of another class. In C++, inheritance is implemented using the `:` keyword, where a derived class inherits the members of a base class. Inheritance helps promote code reuse, facilitates the creation of a hierarchy of related classes, and supports the "is-a" relationship between classes.

Inheritance is essential in C++ because it enables programmers to create a new class based on an existing class, inheriting its attributes and methods. This helps reduce code duplication, improves code organization, and makes it easier to maintain and modify existing code.

## Key Concepts

### Types of Inheritance

C++ supports several types of inheritance:

1.  **Single Inheritance**: A derived class inherits from a single base class.
2.  **Multiple Inheritance**: A derived class inherits from multiple base classes.
3.  **Multilevel Inheritance**: A derived class inherits from a base class that itself inherits from another base class.
4.  **Hierarchical Inheritance**: Multiple derived classes inherit from a single base class.
5.  **Hybrid Inheritance**: A combination of multiple inheritance types.

### Access Modifiers

Access modifiers control the accessibility of inherited members:

1.  **Public**: Members are accessible from anywhere.
2.  **Private**: Members are accessible only within the class.
3.  **Protected**: Members are accessible within the class and its derived classes.

### Inheritance Syntax

The syntax for inheritance in C++ is as follows:
```cpp
class DerivedClass : public BaseClass {
    // Derived class members
};
```
### Constructors and Destructors

When a derived class object is created or destroyed, the following sequence occurs:

1.  Base class constructor is called.
2.  Derived class constructor is called.
3.  Derived class destructor is called.
4.  Base class destructor is called.

## Examples

### Example 1: Single Inheritance

```cpp
class Animal {
public:
    void eat() { cout << "Eating..." << endl; }
};

class Dog : public Animal {
public:
    void bark() { cout << "Barking..." << endl; }
};

int main() {
    Dog myDog;
    myDog.eat();   // Output: Eating...
    myDog.bark();  // Output: Barking...
    return 0;
}
```
### Example 2: Multiple Inheritance

```cpp
class Animal {
public:
    void eat() { cout << "Eating..." << endl; }
};

class Mammal {
public:
    void walk() { cout << "Walking..." << endl; }
};

class Dog : public Animal, public Mammal {
public:
    void bark() { cout << "Barking..." << endl; }
};

int main() {
    Dog myDog;
    myDog.eat();   // Output: Eating...
    myDog.walk();  // Output: Walking...
    myDog.bark();  // Output: Barking...
    return 0;
}
```
### Example 3: Multilevel Inheritance

```cpp
class Animal {
public:
    void eat() { cout << "Eating..." << endl; }
};

class Mammal : public Animal {
public:
    void walk() { cout << "Walking..." << endl; }
};

class Dog : public Mammal {
public:
    void bark() { cout << "Barking..." << endl; }
};

int main() {
    Dog myDog;
    myDog.eat();   // Output: Eating...
    myDog.walk();  // Output: Walking...
    myDog.bark();  // Output: Barking...
    return 0;
}
```
## Exam Tips

1.  Understand the different types of inheritance in C++.
2.  Learn how to use access modifiers to control member accessibility.
3.  Familiarize yourself with the inheritance syntax.
4.  Know the order of constructor and destructor calls in a derived class.
5.  Practice creating and using derived classes.
6.  Understand how to resolve ambiguity in multiple inheritance.
7.  Learn how to use the `virtual` keyword to resolve function overriding issues.