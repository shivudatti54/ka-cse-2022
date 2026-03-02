# Using Virtual Functions in C++

## Introduction

Virtual functions constitute one of the most powerful features of C++ that enables runtime polymorphism, a cornerstone of object-oriented programming. In the context of software development, the ability to define functions in base classes that can be overridden by derived classes allows for flexible and extensible code design. Virtual functions enable the program to determine which function to call at runtime based on the actual object type, rather than the pointer or reference type. This dynamic binding mechanism is essential for implementing design patterns, creating extensible frameworks, and building scalable software systems.

The concept of virtual functions becomes particularly important when working with heterogeneous collections of objects, where different derived class instances need to be processed through base class pointers or references. Without virtual functions, C++ would only support compile-time polymorphism through function overloading and templates. The addition of virtual functions to the language transformed C++ into a truly object-oriented language capable of dynamic polymorphism. This topic is crucial for CSE students as it forms the foundation for understanding advanced OOP concepts and design patterns that are frequently tested in university examinations and are essential for professional software development.

## Key Concepts

### 1. Virtual Functions and Runtime Polymorphism

A virtual function is a member function in a base class that you expect to be overridden in derived classes. When a virtual function is called through a pointer or reference to a base class, the program determines at runtime which version of the function to invoke based on the actual object type. This mechanism is called dynamic binding or late binding, as opposed to static binding where the function call is resolved at compile time.

The syntax for declaring a virtual function uses the `virtual` keyword:

```cpp
class Base {
public:
 virtual void display() {
 cout << "Base class display" << endl;
 }
};

class Derived : public Base {
public:
 void display() override {
 cout << "Derived class display" << endl;
 }
};
```

When a derived class overrides a virtual function, it may optionally use the `override` keyword (introduced in C++11) to make the intention explicit and allow the compiler to catch errors if the function signature doesn't match.

### 2. Virtual Function Tables (vtable)

Every class that contains virtual functions has a hidden virtual function table (vtable) associated with it. The vtable is a static array of function pointers where each entry points to the most derived implementation of the virtual function accessible from that class. Each object of a class with virtual functions contains a hidden pointer called the virtual table pointer (vptr) that points to the class's vtable.

When a virtual function is called on an object, the compiler generates code that:

1. Follows the object's vptr to access its class's vtable
2. Looks up the function pointer at the appropriate offset in the vtable
3. Calls the function pointed to by that pointer

This mechanism allows the correct function to be called regardless of whether the program is accessing the object through a base class pointer or the actual derived class reference.

### 3. Pure Virtual Functions and Abstract Classes

A pure virtual function is a virtual function that is declared but not defined in the base class. It is declared by assigning 0 to the virtual function declaration:

```cpp
class Shape {
public:
 virtual void draw() = 0; // Pure virtual function
 virtual double area() = 0; // Pure virtual function
};
```

A class that contains at least one pure virtual function is called an abstract class. Abstract classes cannot be instantiated directly, meaning you cannot create objects of an abstract class. However, you can have pointers and references to abstract classes, which is precisely what enables polymorphism. Derived classes must provide implementations for all pure virtual functions; otherwise, they also become abstract classes.

Abstract classes serve as interfaces or contracts in software design, defining a set of operations that derived classes must implement. This is a powerful concept for creating flexible and extensible systems where the base class defines the protocol and derived classes provide specific implementations.

### 4. Virtual Destructors

Virtual destructors are crucial for proper cleanup of objects when they are deleted through base class pointers. If a base class destructor is not virtual and you delete a derived class object through a base class pointer, only the base class destructor will be called, leading to resource leaks and undefined behavior.

The rule of thumb is: if a class has any virtual functions, its destructor should also be virtual:

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
 Derived() { data = new int[100]; }
 virtual ~Derived() {
 delete[] data;
 cout << "Derived destructor" << endl;
 }
};
```

When the derived object is deleted through a base pointer, the derived destructor executes first (due to virtual dispatch), then the base destructor runs, ensuring proper resource cleanup.

### 5. Virtual Functions and Access Control

The access specifier in the derived class function declaration is independent of the access specifier in the base class. A public virtual function in the base class can be overridden by a private, protected, or public function in the derived class. The access control that applies is the one in the class through which the function is called. This can lead to surprising results if not understood correctly.

### 6. Virtual Functions in Multiple Inheritance

In multiple inheritance scenarios, virtual functions work similarly, but each base class that contains virtual functions will have its own vtable. The derived class object contains multiple vptrs, one for each virtual base class. The compiler generates code to navigate these vtables correctly when calling virtual functions.

## Examples

### Example 1: Basic Virtual Function Demonstration

Consider a banking system where different account types calculate interest differently:

```cpp
#include <iostream>
using namespace std;

class BankAccount {
protected:
 double balance;
public:
 BankAccount(double b) : balance(b) {}

 virtual double calculateInterest() {
 return balance * 0.04; // Default 4% interest
 }

 virtual void display() {
 cout << "Balance: " << balance << endl;
 cout << "Interest: " << calculateInterest() << endl;
 }

 virtual ~BankAccount() {}
};

class SavingsAccount : public BankAccount {
private:
 double interestRate;
public:
 SavingsAccount(double b, double r) : BankAccount(b), interestRate(r) {}

 double calculateInterest() override {
 return balance * interestRate;
 }
};

class CurrentAccount : public BankAccount {
public:
 CurrentAccount(double b) : BankAccount(b) {}

 double calculateInterest() override {
 return 0; // No interest for current account
 }
};

int main() {
 BankAccount* accounts[3];
 accounts[0] = new BankAccount(10000);
 accounts[1] = new SavingsAccount(10000, 0.06);
 accounts[2] = new CurrentAccount(10000);

 for(int i = 0; i < 3; i++) {
 accounts[i]->display();
 cout << "-------------------" << endl;
 }

 // Clean up
 for(int i = 0; i < 3; i++) {
 delete accounts[i];
 }

 return 0;
}
```

**Output:**

```
Balance: 10000
Interest: 400
-------------------
Balance: 10000
Interest: 600
-------------------
Balance: 10000
Interest: 0
-------------------
```

This example demonstrates how the same function call `calculateInterest()` produces different results based on the actual object type, demonstrating runtime polymorphism.

### Example 2: Pure Virtual Functions and Abstract Classes

Creating a shape hierarchy with area calculation:

```cpp
#include <iostream>
using namespace std;

class Shape {
public:
 virtual double area() = 0; // Pure virtual function
 virtual void display() = 0; // Pure virtual function
 virtual ~Shape() {}
};

class Circle : public Shape {
private:
 double radius;
public:
 Circle(double r) : radius(r) {}

 double area() override {
 return 3.14159 * radius * radius;
 }

 void display() override {
 cout << "Circle with radius " << radius
 << ", Area: " << area() << endl;
 }
};

class Rectangle : public Shape {
private:
 double length, breadth;
public:
 Rectangle(double l, double b) : length(l), breadth(b) {}

 double area() override {
 return length * breadth;
 }

 void display() override {
 cout << "Rectangle " << length << " x " << breadth
 << ", Area: " << area() << endl;
 }
};

int main() {
 // Shape s; // ERROR: Cannot instantiate abstract class

 Shape* shapes[] = {
 new Circle(5),
 new Rectangle(4, 6),
 new Circle(3)
 };

 for(int i = 0; i < 3; i++) {
 shapes[i]->display();
 }

 for(int i = 0; i < 3; i++) {
 delete shapes[i];
 }

 return 0;
}
```

### Example 3: Virtual Destructor for Proper Cleanup

Demonstrating the importance of virtual destructors:

```cpp
#include <iostream>
using namespace std;

class Base {
public:
 Base() { cout << "Base constructor" << endl; }
 virtual ~Base() { cout << "Base destructor" << endl; }
 virtual void show() { cout << "Base show" << endl; }
};

class Derived : public Base {
private:
 int* array;
public:
 Derived(int size) {
 array = new int[size];
 cout << "Derived constructor" << endl;
 }

 ~Derived() {
 delete[] array;
 cout << "Derived destructor" << endl;
 }

 void show() override { cout << "Derived show" << endl; }
};

int main() {
 Base* ptr = new Derived(10);
 ptr->show();
 delete ptr; // Without virtual destructor, only Base destructor called

 return 0;
}
```

**Output:**

```
Base constructor
Derived constructor
Derived show
Derived destructor
Base destructor
```

## Exam Tips

1. **Remember the virtual keyword**: A function must be declared as virtual in the base class to enable runtime polymorphism. Without it, static binding occurs.

2. **Pure virtual function syntax**: The syntax `virtual void func() = 0;` declares a pure virtual function. Remember that classes with pure virtual functions are abstract and cannot be instantiated.

3. **Override keyword**: Use the C++11 `override` specifier when overriding virtual functions to catch signature mismatches at compile time. This is a common source of errors in exams.

4. **Virtual destructor rule**: If your class contains virtual functions, always make the destructor virtual. This is a golden rule tested frequently in university exams.

5. **Vtable concept**: Understand that virtual functions are resolved at runtime using vtables. Each class with virtual functions has its own vtable, and objects contain vptrs pointing to these tables.

6. **Slicing problem**: When a derived class object is assigned to a base class object (not pointer/reference), object slicing occurs and virtual functions won't work. Always use pointers or references for polymorphism.

7. **Default arguments**: Virtual functions do not support default arguments in the expected way. The default argument value from the base class declaration is used, not the derived class's value.

8. **Constructor and virtual functions**: Never call virtual functions from constructors. At the time of base class construction, the derived class part doesn't exist yet, so virtual function calls resolve to the base class version.

9. **Abstract classes**: Remember that abstract classes can have constructors that derived classes can call. They can also have non-virtual functions and data members.

10. **vtbl and performance**: Virtual functions have a small runtime overhead due to indirection through vtable. However, this is usually negligible compared to the flexibility gained.
