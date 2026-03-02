# The Virtual Attribute is Inherited

## Introduction

In Object-Oriented Programming with C++, the virtual attribute represents one of the most powerful mechanisms for achieving runtime polymorphism. The fundamental principle that makes this possible is the concept of virtual function inheritance. When a base class declares a function as virtual, that virtual attribute is automatically inherited by all derived classes that override this function. This inheritance of the virtual attribute enables dynamic binding, where the appropriate function implementation is determined at runtime based on the actual object type, not the pointer or reference type.

Understanding how the virtual attribute is inherited is crucial for writing flexible and extensible C++ code. Without virtual functions, C++ would be limited to static binding, where function calls are resolved at compile-time. The virtual attribute transforms this behavior, allowing the same piece of code to behave differently depending on the actual object it operates on. This mechanism forms the foundation for many design patterns, frameworks, and polymorphic behaviors in C++ applications.

This topic explores the intricacies of virtual function inheritance, including pure virtual functions, the override specifier, virtual destructors, and the rules governing how the virtual attribute propagates through class hierarchies. Mastery of these concepts is essential for any C++ developer seeking to leverage the full power of object-oriented programming.

## Key Concepts

### 1. Virtual Functions and Virtual Attribute Inheritance

When a base class declares a member function with the `virtual` keyword, it establishes a virtual function. The most critical aspect to understand is that once a function is declared virtual in a base class, it remains virtual in all derived classes regardless of whether the `virtual` keyword is explicitly used in the derived class declaration. Consider the following example:

```cpp
class Base {
public:
 virtual void display() {
 cout << "Base display" << endl;
 }
};

class Derived : public Base {
public:
 void display() { // Virtual attribute is inherited implicitly
 cout << "Derived display" << endl;
 }
};
```

In the `Derived` class, the `display()` function implicitly inherits the virtual attribute from the base class. The function is still virtual, even though the `virtual` keyword is not repeated. This is known as implicit virtual inheritance.

### 2. Pure Virtual Functions and Abstract Classes

A pure virtual function is declared by assigning `= 0` in its declaration. This makes the function abstract, meaning it has no implementation in the base class and must be overridden by all concrete derived classes. When a class contains at least one pure virtual function, it becomes an abstract class and cannot be instantiated directly.

```cpp
class Shape {
public:
 virtual void draw() = 0; // Pure virtual function
 virtual double area() = 0; // Another pure virtual function
 virtual ~Shape() {} // Virtual destructor for proper cleanup
};

class Circle : public Shape {
private:
 double radius;
public:
 Circle(double r) : radius(r) {}
 void draw() override {
 cout << "Drawing Circle" << endl;
 }
 double area() override {
 return 3.14159 * radius * radius;
 }
};
```

The pure virtual function establishes a contract that derived classes must fulfill by providing their own implementations. This is a fundamental mechanism for achieving abstraction and defining interfaces in C++.

### 3. The Override Specifier (C++11)

Modern C++ provides the `override` specifier to explicitly indicate that a function is intended to override a virtual function from a base class. While not strictly required, using `override` is highly recommended because it enables the compiler to catch errors where a derived class function fails to properly override a base class virtual function.

```cpp
class Base {
public:
 virtual void process(int value) {
 cout << "Base processing: " << value << endl;
 }
};

class Derived : public Base {
public:
 void process(int value) override { // Explicitly states intention to override
 cout << "Derived processing: " << value * 2 << endl;
 }
 // void process(double) override; // ERROR: Cannot override non-virtual function
};
```

If you accidentally misspell the function name or change the parameter types, the compiler will generate an error when `override` is specified, preventing subtle bugs.

### 4. Virtual Destructors

One of the most important aspects of virtual attribute inheritance involves destructors. When a base class pointer points to a derived class object and delete is called, only the base class destructor executes if the destructor is not virtual, leading to resource leaks and undefined behavior. Therefore, base classes with virtual functions should always have virtual destructors.

```cpp
class Base {
public:
 virtual ~Base() {
 cout << "Base destructor" << endl;
 }
};

class Derived : public Base {
private:
 int* data;
public:
 Derived() {
 data = new int[100];
 }
 virtual ~Derived() {
 delete[] data;
 cout << "Derived destructor" << endl;
 }
};

// Usage
Base* ptr = new Derived();
delete ptr; // Properly calls both destructors in correct order
```

The virtual destructor is inherited just like any other virtual function, ensuring proper cleanup of derived class resources.

### 5. Covariant Return Types

When overriding a virtual function, the derived class can specify a different return type if it is a pointer or reference to a class type. This is called a covariant return type. The derived class's return type must be more derived than the base class's return type.

```cpp
class Base {
public:
 virtual Base* clone() {
 return new Base(*this);
 }
};

class Derived : public Base {
public:
 Derived* clone() override { // Covariant return type
 return new Derived(*this);
 }
};
```

This feature allows for more specific return types in derived classes while maintaining polymorphism.

### 6. Virtual Function Accessibility

The virtual attribute is independent of access specifiers. A function can be virtual and public, protected, or private. However, note that you cannot override a private virtual function with a public function in the derived class. The accessibility of the overriding function can be different from the original.

```cpp
class Base {
protected:
 virtual void internalProcess() {
 cout << "Base internal process" << endl;
 }
public:
 void process() {
 internalProcess(); // Calls derived implementation if overridden
 }
};

class Derived : public Base {
public:
 void internalProcess() override {
 cout << "Derived internal process" << endl;
 }
};
```

### 7. Virtual Functions and Multiple Inheritance

In multiple inheritance scenarios, virtual functions from different base classes can be overridden independently. The virtual attribute inheritance works normally across each inheritance path.

```cpp
class Interface1 {
public:
 virtual void method1() = 0;
};

class Interface2 {
public:
 virtual void method2() = 0;
};

class Concrete : public Interface1, public Interface2 {
public:
 void method1() override {
 cout << "Method1 implementation" << endl;
 }
 void method2() override {
 cout << "Method2 implementation" << endl;
 }
};
```

## Examples

### Example 1: Demonstrating Virtual Attribute Inheritance

```cpp
#include <iostream>
using namespace std;

class Animal {
public:
 virtual void speak() {
 cout << "Animal speaks" << endl;
 }
 virtual ~Animal() {}
};

class Dog : public Animal {
public:
 void speak() { // Virtual attribute inherited implicitly
 cout << "Dog barks: Woof! Woof!" << endl;
 }
};

class Cat : public Animal {
public:
 void speak() { // Virtual attribute inherited implicitly
 cout << "Cat meows: Meow! Meow!" << endl;
 }
};

int main() {
 Animal* ptr;

 Dog d;
 Cat c;

 ptr = &d;
 ptr->speak(); // Runtime polymorphism: calls Dog::speak()

 ptr = &c;
 ptr->speak(); // Runtime polymorphism: calls Cat::speak()

 return 0;
}
```

**Output:**

```
Dog barks: Woof! Woof!
Cat meows: Meow! Meow!
```

### Example 2: Pure Virtual Function Implementation

```cpp
#include <iostream>
using namespace std;

class Shape {
protected:
 string name;
public:
 Shape(string n) : name(n) {}
 virtual void draw() = 0; // Pure virtual function
 virtual double getArea() = 0; // Pure virtual function
 virtual ~Shape() {}
};

class Rectangle : public Shape {
private:
 double length, width;
public:
 Rectangle(double l, double w) : Shape("Rectangle"), length(l), width(w) {}
 void draw() override {
 cout << "Drawing Rectangle with length " << length
 << " and width " << width << endl;
 }
 double getArea() override {
 return length * width;
 }
};

class Triangle : public Shape {
private:
 double base, height;
public:
 Triangle(double b, double h) : Shape("Triangle"), base(b), height(h) {}
 void draw() override {
 cout << "Drawing Triangle with base " << base
 << " and height " << height << endl;
 }
 double getArea() override {
 return 0.5 * base * height;
 }
};

int main() {
 Shape* shapes[2];
 shapes[0] = new Rectangle(5, 3);
 shapes[1] = new Triangle(4, 6);

 for (int i = 0; i < 2; i++) {
 shapes[i]->draw();
 cout << "Area: " << shapes[i]->getArea() << endl;
 }

 for (int i = 0; i < 2; i++) {
 delete shapes[i];
 }

 return 0;
}
```

### Example 3: Virtual Destructor Demonstration

```cpp
#include <iostream>
using namespace std;

class Base {
public:
 Base() {
 cout << "Base constructor" << endl;
 }
 virtual ~Base() { // Virtual destructor
 cout << "Base destructor" << endl;
 }
};

class Derived : public Base {
private:
 int* array;
public:
 Derived(int size) {
 array = new int[size];
 cout << "Derived constructor - allocated array" << endl;
 }
 ~Derived() {
 delete[] array;
 cout << "Derived destructor - deallocated array" << endl;
 }
};

int main() {
 Base* ptr = new Derived(10);
 cout << "--- Deleting pointer ---" << endl;
 delete ptr;
 return 0;
}
```

**Output:**

```
Base constructor
Derived constructor - allocated array
--- Deleting pointer ---
Derived destructor - deallocated array
Base destructor
```

## Exam Tips

1. **Remember the Rule**: If a base class declares a function as virtual, all overriding functions in derived classes are automatically virtual - you don't need to repeat the virtual keyword.

2. **Pure Virtual Functions**: A pure virtual function is declared with `= 0` and makes the class abstract. Abstract classes cannot be instantiated.

3. **Virtual Destructors**: Always make destructors virtual in classes that have virtual functions to ensure proper cleanup through base class pointers.

4. **Override Specifier**: Use the C++11 `override` specifier to catch override errors at compile-time rather than runtime.

5. **Object Slicing**: When passing objects by value instead of pointers or references, virtual functions are not invoked - the object gets sliced.

6. **Virtual Functions and Constructors**: Virtual functions are not called dynamically during construction - the base class version runs because the derived part hasn't been constructed yet.

7. **Covariant Returns**: Remember that overriding functions can have covariant return types (derived class pointers/references).

8. **Default Arguments**: Virtual functions use static binding for default arguments - the base class default is used, not the derived class default.
