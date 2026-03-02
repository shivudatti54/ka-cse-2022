# Runtime Polymorphism Using Pointers in C++

## Introduction

Runtime polymorphism is one of the most powerful features of object-oriented programming, enabling objects of different classes to be treated uniformly through a common interface. In C++, this is achieved primarily through virtual functions and base class pointers. Unlike compile-time polymorphism (which includes function overloading and operator overloading), runtime polymorphism resolves function calls at runtime, allowing for dynamic behavior based on the actual object type.

For DU students preparing for semester examinations, understanding runtime polymorphism is essential because it forms the foundation for designing flexible and extensible software systems. This topic becomes particularly important when working with inheritance hierarchies where you need to process different derived class objects through a common base class interface. Real-world applications include graphics rendering systems (where different shapes are drawn through a common interface), game development (where different enemy types respond to a common update method), and banking systems (where different account types calculate interest through a unified interface).

This module explores how runtime polymorphism works with pointers in C++, covering virtual functions, pure virtual functions, abstract classes, virtual destructors, and the underlying mechanism of virtual tables. Mastery of these concepts is crucial for both theoretical understanding and practical programming in C++.

## Key Concepts

### 1. Pointer to Base Class

In C++, a pointer to a base class can store addresses of objects from any derived class. This is the fundamental mechanism that enables runtime polymorphism. When you create a base class pointer and assign it the address of a derived class object, you establish an "is-a" relationship that allows the pointer to access the derived object through the base class interface.

```cpp
class Animal {
public:
    void eat() { cout << "Animal eats food" << endl; }
};

class Dog : public Animal {
public:
    void bark() { cout << "Dog barks" << endl; }
};

int main() {
    Dog d;
    Animal* ptr = &d;  // Base class pointer to derived object
    ptr->eat();        // Works - eat() is inherited
    // ptr->bark();    // Error - bark() not in base class
    return 0;
}
```

The key insight here is that the pointer type determines which members are accessible, not the object type. This is where virtual functions become essential.

### 2. Virtual Functions

A virtual function is a member function declared in a base class and redefined in derived classes. The key characteristic of virtual functions is that the correct function is called based on the actual object type at runtime, not the pointer type. This is achieved through a mechanism called dynamic dispatch or late binding.

To declare a function as virtual, use the `virtual` keyword in the base class declaration. Any derived class that overrides this function automatically becomes virtual (though it's good practice to include the `virtual` keyword for clarity).

```cpp
class Shape {
public:
    virtual void draw() {
        cout << "Drawing a shape" << endl;
    }
};

class Circle : public Shape {
public:
    void draw() override {
        cout << "Drawing a circle" << endl;
    }
};

class Rectangle : public Shape {
public:
    void draw() override {
        cout << "Drawing a rectangle" << endl;
    }
};

int main() {
    Shape* shapes[3];
    shapes[0] = new Circle();
    shapes[1] = new Rectangle();
    shapes[2] = new Shape();
    
    for(int i = 0; i < 3; i++) {
        shapes[i]->draw();  // Runtime polymorphism
    }
    return 0;
}
```

**Output:**
```
Drawing a circle
Drawing a rectangle
Drawing a shape
```

The `override` keyword (introduced in C++11) is highly recommended when overriding virtual functions. It ensures that the function actually overrides a virtual function in the base class, preventing subtle errors from misspelled function names or incorrect parameter types.

### 3. Pure Virtual Functions and Abstract Classes

A pure virtual function is a virtual function that is declared but not defined in the base class. It is declared by assigning 0 to the virtual function. Classes containing pure virtual functions are called abstract classes and cannot be instantiated (you cannot create objects of an abstract class).

```cpp
class Animal {
public:
    // Pure virtual function
    virtual void speak() = 0;
    
    // Concrete function - can be inherited as-is
    void sleep() {
        cout << "Animal is sleeping" << endl;
    }
};

// Cannot do: Animal a;  // Error - Animal is abstract

class Dog : public Animal {
public:
    void speak() override {
        cout << "Dog says: Woof!" << endl;
    }
};

int main() {
    Dog d;
    d.speak();    // Dog says: Woof!
    d.sleep();    // Animal is sleeping
    return 0;
}
```

Abstract classes serve as interfaces or contracts in C++. They define a set of behaviors that derived classes must implement. This is analogous to interfaces in Java or abstract classes in other OOP languages. In DU exams, understanding when to use abstract classes versus concrete base classes is a common question.

### 4. Virtual Destructors

When deleting a derived class object through a base class pointer, only the base class destructor gets called if the destructor is not virtual. This leads to resource leaks because derived class destructors never execute. To ensure proper cleanup, always make base class destructors virtual when the class contains virtual functions.

```cpp
class Base {
public:
    virtual ~Base() {
        cout << "Base destructor" << endl;
    }
};

class Derived : public Base {
public:
    Derived() { data = new int[100]; }
    ~Derived() {
        delete[] data;
        cout << "Derived destructor" << endl;
    }
private:
    int* data;
};

int main() {
    Base* ptr = new Derived();
    delete ptr;  // Calls both destructors in correct order
    return 0;
}
```

**Output:**
```
Derived destructor
Base destructor
```

Without the virtual destructor, only "Base destructor" would be printed, causing a memory leak. This is a critical concept that frequently appears in DU examinations as a "what goes wrong" question.

### 5. Virtual Function Table (vtable)

Understanding how virtual functions work internally helps deepen your conceptual understanding. Each class that contains virtual functions has a hidden virtual table (vtable) - a table of function pointers. Each object of such a class contains a hidden pointer to this vtable (called the vptr or vfptr).

When a virtual function is called through a base pointer:
1. The object's vptr is followed to find the class's vtable
2. The function pointer at the appropriate offset is retrieved
3. The function is called through that pointer

This mechanism adds a small runtime overhead (typically one pointer lookup), but provides the flexibility of runtime polymorphism. Understanding vtables helps explain why virtual functions cannot be inlined and why they have the behavior they do.

### 6. Runtime Type Information (RTTI) and Dynamic Cast

C++ provides RTTI (Runtime Type Information) to safely query and convert object types at runtime. The `dynamic_cast` operator performs safe downcasting (converting from base pointer to derived pointer) and returns nullptr if the conversion is invalid.

```cpp
class Base {
public:
    virtual void show() { cout << "Base" << endl; }
};

class Derived : public Base {
public:
    void show() override { cout << "Derived" << endl; }
    void derivedOnly() { cout << "Derived specific" << endl; }
};

int main() {
    Base* b = new Derived();
    
    // Safe downcasting using dynamic_cast
    Derived* d = dynamic_cast<Derived*>(b);
    if(d) {
        d->derivedOnly();  // Works safely
    }
    
    // Invalid cast returns nullptr
    Base* baseObj = new Base();
    Derived* badCast = dynamic_cast<Derived*>(baseObj);
    if(badCast == nullptr) {
        cout << "Invalid cast" << endl;
    }
    
    delete b;
    delete baseObj;
    return 0;
}
```

## Examples

### Example 1: Banking System with Account Types

Consider a banking system where different account types calculate interest differently:

```cpp
#include <iostream>
using namespace std;

class BankAccount {
protected:
    double balance;
public:
    BankAccount(double b) : balance(b) {}
    
    virtual void calculateInterest() = 0;  // Pure virtual
    
    virtual void display() {
        cout << "Balance: Rs. " << balance << endl;
    }
    
    virtual ~BankAccount() {}
};

class SavingsAccount : public BankAccount {
private:
    double interestRate;
public:
    SavingsAccount(double b, double r) : BankAccount(b), interestRate(r) {}
    
    void calculateInterest() override {
        double interest = balance * interestRate;
        balance += interest;
        cout << "Savings Interest: Rs. " << interest << endl;
    }
};

class CurrentAccount : public BankAccount {
private:
    double serviceCharge;
public:
    CurrentAccount(double b, double sc) : BankAccount(b), serviceCharge(sc) {}
    
    void calculateInterest() override {
        balance -= serviceCharge;
        cout << "Service Charge deducted: Rs. " << serviceCharge << endl;
    }
};

int main() {
    BankAccount* accounts[2];
    accounts[0] = new SavingsAccount(10000, 0.05);
    accounts[1] = new CurrentAccount(10000, 500);
    
    cout << "=== Before Interest Calculation ===" << endl;
    for(int i = 0; i < 2; i++) {
        accounts[i]->display();
    }
    
    cout << "\n=== After Interest Calculation ===" << endl;
    for(int i = 0; i < 2; i++) {
        accounts[i]->calculateInterest();
        accounts[i]->display();
    }
    
    for(int i = 0; i < 2; i++) {
        delete accounts[i];
    }
    return 0;
}
```

**Output:**
```
=== Before Interest Calculation ===
Balance: Rs. 10000
Balance: Rs. 10000

=== After Interest Calculation ===
Savings Interest: Rs. 500
Balance: Rs. 10500
Service Charge deducted: Rs. 500
Balance: Rs. 9500
```

### Example 2: Shape Drawing System

A classic example demonstrating polymorphism in graphics:

```cpp
#include <iostream>
using namespace std;

class Shape {
protected:
    string color;
public:
    Shape(string c) : color(c) {}
    
    virtual void draw() = 0;
    virtual double area() = 0;
    
    virtual ~Shape() {}
};

class Circle : public Shape {
private:
    double radius;
public:
    Circle(string c, double r) : Shape(c), radius(r) {}
    
    void draw() override {
        cout << "Drawing " << color << " Circle with radius " << radius << endl;
    }
    
    double area() override {
        return 3.14159 * radius * radius;
    }
};

class Rectangle : public Shape {
private:
    double length, width;
public:
    Rectangle(string c, double l, double w) : Shape(c), length(l), width(w) {}
    
    void draw() override {
        cout << "Drawing " << color << " Rectangle " << length << "x" << width << endl;
    }
    
    double area() override {
        return length * width;
    }
};

int main() {
    Shape* shapes[] = {
        new Circle("Red", 5.0),
        new Rectangle("Blue", 10.0, 6.0),
        new Circle("Green", 3.0)
    };
    
    double totalArea = 0;
    for(int i = 0; i < 3; i++) {
        shapes[i]->draw();
        totalArea += shapes[i]->area();
    }
    
    cout << "\nTotal Area: " << totalArea << endl;
    
    for(int i = 0; i < 3; i++) {
        delete shapes[i];
    }
    return 0;
}
```

### Example 3: Vehicle Management System

```cpp
#include <iostream>
using namespace std;

class Vehicle {
protected:
    string brand;
    int speed;
public:
    Vehicle(string b, int s) : brand(b), speed(s) {}
    
    virtual void start() {
        cout << brand << " vehicle started" << endl;
    }
    
    virtual void stop() {
        cout << brand << " vehicle stopped" << endl;
    }
    
    virtual void displayInfo() {
        cout << "Brand: " << brand << ", Max Speed: " << speed << " km/h" << endl;
    }
    
    virtual ~Vehicle() {}
};

class Car : public Vehicle {
private:
    int seats;
public:
    Car(string b, int s, int st) : Vehicle(b, s), seats(st) {}
    
    void displayInfo() override {
        Vehicle::displayInfo();
        cout << "Type: Car, Seats: " << seats << endl;
    }
};

class Bike : public Vehicle {
private:
    bool hasGear;
public:
    Bike(string b, int s, bool g) : Vehicle(b, s), hasGear(g) {}
    
    void start() override {
        cout << brand << " Bike engine started";
        if(hasGear) cout << " with kick start" << endl;
        else cout << " with self start" << endl;
    }
};

int main() {
    Vehicle* garage[3];
    garage[0] = new Car("Toyota", 180, 5);
    garage[1] = new Bike("Honda", 120, true);
    garage[2] = new Car("Ford", 200, 4);
    
    for(int i = 0; i < 3; i++) {
        garage[i]->start();
        garage[i]->displayInfo();
        garage[i]->stop();
        cout << endl;
    }
    
    for(int i = 0; i < 3; i++) {
        delete garage[i];
    }
    return 0;
}
```

## Exam Tips

1. **Virtual Function Resolution**: Remember that virtual functions are resolved at runtime using the actual object type, not the pointer type. This is the core concept of runtime polymorphism.

2. **Abstract Class Restrictions**: You cannot instantiate an abstract class, but you can have pointers and references to abstract classes. This is frequently tested in DU exams.

3. **Virtual Destructor Rule**: Always make destructors virtual when the class has virtual functions. Non-virtual destructors cause undefined behavior when deleting through base pointers.

4. **Slicing Problem**: When a derived class object is assigned to a base class object (not pointer), object slicing occurs and polymorphism is lost. Avoid this by using pointers or references.

5. **Override Keyword**: Use the `override` specifier (C++11) when overriding virtual functions. It catches errors at compile-time rather than creating a new virtual function accidentally.

6. **Default Arguments**: Virtual functions do not support default arguments in the way you might expect. The default argument used is based on the static type (pointer type), not the dynamic type.

7. **Pure Virtual Functions**: Classes with all pure virtual functions are called "interfaces" in C++. They define contracts that derived classes must implement.

8. **Virtual Functions in Constructors**: Calling virtual functions from constructors is dangerous - the derived class's virtual function won't be called because the derived part hasn't been constructed yet.

9. **sizeof() with Virtual Functions**: Classes with virtual functions have additional overhead (typically 8 bytes on 64-bit systems) for the vptr.

10. **Virtual Functions and Static Methods**: Static functions cannot be virtual because they are not associated with any object and don't have a this pointer.