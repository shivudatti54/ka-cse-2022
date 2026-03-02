# Inheritance and Polymorphism in C++

## Comprehensive Study Material for BSc Physical Science (CS) - Delhi University NEP 2024

---

## Table of Contents
1. [Introduction and Real-World Relevance](#introduction)
2. [Inheritance in C++](#inheritance)
3. [Types of Inheritance](#types-of-inheritance)
4. [Polymorphism in C++](#polymorphism)
5. [Runtime Polymorphism and Virtual Functions](#runtime-polymorphism)
6. [Pure Virtual Functions and Abstract Classes](#pure-virtual)
7. [Virtual Destructors](#virtual-destructors)
8. [The Diamond Problem and Virtual Inheritance](#diamond-problem)
9. [VTable and VPointer Mechanism](#vtable)
10. [Code Examples](#code-examples)
11. [Key Takeaways](#key-takeaways)
12. [Challenging MCQs](#mcqs)
13. [Flashcards](#flashcards)

---

## 1. Introduction and Real-World Relevance {#introduction}

### What is Inheritance and Polymorphism?

**Inheritance** and **polymorphism** are two fundamental pillars of Object-Oriented Programming (OOP) that enable code reusability, extensibility, and flexibility in software design. These concepts form the backbone of modern software development and are essential for creating scalable and maintainable applications.

In the context of the Delhi University BSc Physical Science (CS) curriculum under NEP 2024, these topics carry significant weight as they form the foundation for understanding advanced C++ programming concepts and are frequently tested in university examinations.

### Real-World Relevance

Consider a real-world scenario: A university management system needs to handle different types of members—students, teachers, and administrators. Each member type shares common attributes (like name, ID, contact information) but also has unique characteristics. Using **inheritance**, we can create a base class `Person` with common attributes and derive `Student`, `Teacher`, and `Administrator` classes from it. 

Now, imagine the system needs to calculate fees for different categories. A **polymorphic** function `calculateFees()` can be defined in the base class and overridden in derived classes to provide appropriate implementations for each member type. This allows the system to call the appropriate function based on the actual object type at runtime, making the code flexible and extensible.

Other real-world applications include:
- **Game Development**: Different enemy types (zombies, vampires, demons) inheriting from a base `Enemy` class, each with unique attack behaviors
- **GUI Systems**: Buttons, text boxes, and checkboxes inheriting from a base `Widget` class with common rendering methods
- **Banking Systems**: Different account types (savings, checking, fixed deposit) with varying interest calculation methods

---

## 2. Inheritance in C++ {#inheritance}

### What is Inheritance?

**Inheritance** is a mechanism in C++ that allows a class (called a **derived class** or **child class**) to acquire properties and behaviors (data members and member functions) of another class (called a **base class** or **parent class**). This promotes code reusability and establishes a natural hierarchy between classes.

### Syntax of Inheritance

```cpp
// Base class
class BaseClass {
public:
    int baseData;
    void baseFunction() {
        cout << "Base class function" << endl;
    }
};

// Derived class
class DerivedClass : public BaseClass {
public:
    int derivedData;
    void derivedFunction() {
        cout << "Derived class function" << endl;
    }
};
```

### Why Use Inheritance?

1. **Code Reusability**: Common attributes and behaviors need not be rewritten for each class
2. **Extensibility**: New classes can be added with minimal changes to existing code
3. **Maintainability**: Changes in base class automatically reflect in derived classes
4. **Logical Hierarchy**: Reflects real-world relationships naturally

### Access Specifiers and Inheritance

C++ provides three types of inheritance, determined by the access specifier used:

| Inheritance Type | Private Members | Protected Members | Public Members |
|-----------------|-----------------|-------------------|-----------------|
| **Public** | Inaccessible | Protected | Public |
| **Protected** | Inaccessible | Protected | Protected |
| **Private** | Inaccessible | Private | Private |

---

## 3. Types of Inheritance {#types-of-inheritance}

### 3.1 Single Inheritance
A derived class inherits from only one base class.

```cpp
class Animal {
public:
    void eat() { cout << "Eating..." << endl; }
};

class Dog : public Animal {
public:
    void bark() { cout << "Barking..." << endl; }
};
```

### 3.2 Multiple Inheritance
A derived class inherits from more than one base class.

```cpp
class Flyable {
public:
    void fly() { cout << "Flying..." << endl; }
};

class Swimmable {
public:
    void swim() { cout << "Swimming..." << endl; }
};

class Duck : public Flyable, public Swimmable {
public:
    void quack() { cout << "Quacking..." << endl; }
};
```

### 3.3 Multilevel Inheritance
A class inherits from a class that is already a derived class.

```cpp
class Vehicle {
public:
    void start() { cout << "Vehicle started" << endl; }
};

class Car : public Vehicle {
public:
    void drive() { cout << "Car driving" << endl; }
};

class SportsCar : public Car {
public:
    void race() { cout << "Sports car racing" << endl; }
};
```

### 3.4 Hierarchical Inheritance
Multiple derived classes inherit from a single base class.

```cpp
class Shape {
public:
    void display() { cout << "Displaying shape" << endl; }
};

class Circle : public Shape {
public:
    void drawCircle() { cout << "Drawing circle" << endl; }
};

class Rectangle : public Shape {
public:
    void drawRectangle() { cout << "Drawing rectangle" << endl; }
};
```

### 3.5 Hybrid Inheritance
A combination of two or more types of inheritance.

---

## 4. Constructor and Destructor Order in Inheritance

Understanding the order of constructor and destructor calls is crucial for proper resource management:

### Constructor Execution Order
1. **Base class constructors** are executed before derived class constructors
2. If there are multiple base classes, they are executed in the order of inheritance declaration
3. For multilevel inheritance, constructors execute from top to bottom

```cpp
class A {
public:
    A() { cout << "Constructor A" << endl; }
    ~A() { cout << "Destructor A" << endl; }
};

class B : public A {
public:
    B() { cout << "Constructor B" << endl; }
    ~B() { cout << "Destructor B" << endl; }
};

class C : public B {
public:
    C() { cout << "Constructor C" << endl; }
    ~C() { cout << "Destructor C" << endl; }
};

int main() {
    C obj;
    return 0;
}
```

**Output:**
```
Constructor A
Constructor B
Constructor C
Destructor C
Destructor B
Destructor A
```

### Key Points:
- **Constructors** are called in the order of inheritance (base → derived)
- **Destructors** are called in reverse order (derived → base)
- This ensures proper initialization and cleanup of resources

---

## 5. Polymorphism in C++ {#polymorphism}

### What is Polymorphism?

**Polymorphism** (from Greek: "many forms") allows a single interface to be used for different data types or classes. In C++, polymorphism enables one function to behave differently based on the type of object that is calling it.

### Types of Polymorphism

#### 5.1 Compile-Time Polymorphism (Static Binding)
- **Function Overloading**: Multiple functions with the same name but different parameters
- **Operator Overloading**: Redefining operators for user-defined types

```cpp
class Calculator {
public:
    int add(int a, int b) { return a + b; }
    double add(double a, double b) { return a + b; }
    int add(int a, int b, int c) { return a + b + c; }
};
```

#### 5.2 Runtime Polymorphism (Dynamic Binding)
- Achieved through **virtual functions**
- Function call is resolved at runtime based on the actual object type
- Requires inheritance and base class pointers/references

---

## 6. Runtime Polymorphism and Virtual Functions {#runtime-polymorphism}

### Virtual Functions

A **virtual function** is a member function in a base class that you expect to override in derived classes. The key characteristic is that the function to be called is determined at runtime based on the actual object type, not the pointer/reference type.

### Syntax and Usage

```cpp
class Base {
public:
    virtual void show() {
        cout << "Base class show()" << endl;
    }
};

class Derived : public Base {
public:
    void show() override {
        cout << "Derived class show()" << endl;
    }
};

int main() {
    Base* ptr;
    Derived d;
    
    ptr = &d;
    ptr->show();  // Calls Derived class show()
    
    return 0;
}
```

**Output:**
```
Derived class show()
```

### Key Characteristics of Virtual Functions:

1. **Virtual keyword**: Used to declare a virtual function in the base class
2. **Override keyword** (C++11): Optional but recommended in derived class to explicitly indicate overriding
3. **Pure virtual functions**: Virtual functions with `= 0` declaration that must be overridden
4. **Cannot be static**: Virtual functions cannot be static members
5. **Can be friend functions**: Virtual functions can be friend functions of other classes

### Virtual Function Rules:
- Virtual functions cannot be constructor but can be destructor
- If a function is virtual in base class, all derived classes override it by default (even without virtual keyword)
- The most derived implementation is always called

---

## 7. Pure Virtual Functions and Abstract Classes {#pure-virtual}

### Pure Virtual Function

A **pure virtual function** is a virtual function that has no implementation in the base class and must be overridden by derived classes. It is declared using `= 0`:

```cpp
class Shape {
public:
    virtual void draw() = 0;  // Pure virtual function
    virtual double area() = 0;  // Pure virtual function
};
```

### Abstract Classes

A class that contains at least one pure virtual function is called an **abstract class**. 

**Characteristics of Abstract Classes:**

1. **Cannot be instantiated**: You cannot create objects of an abstract class
2. **Can have constructors**: Abstract classes can have constructors that derived classes can call
3. **Can have normal functions**: Can contain regular member functions with implementations
4. **Can have data members**: Can have member variables with various access specifiers
5. **Pointer/references**: Can have pointers and references to abstract class types

```cpp
class Animal {
protected:
    string name;
public:
    Animal(string n) : name(n) {}
    
    // Pure virtual function
    virtual void speak() = 0;
    
    // Regular function
    void displayName() {
        cout << "Name: " << name << endl;
    }
};

class Dog : public Animal {
public:
    Dog(string n) : Animal(n) {}
    
    void speak() override {
        cout << name << " says: Woof!" << endl;
    }
};

int main() {
    // Animal a;  // ERROR: Cannot instantiate abstract class
    // Animal* ptr = new Animal();  // ERROR
    
    Animal* ptr = new Dog("Buddy");
    ptr->speak();  // Outputs: Buddy says: Woof!
    ptr->displayName();
    
    return 0;
}
```

---

## 8. Virtual Destructors {#virtual-destructors}

### Why Virtual Destructors?

When deleting a derived class object through a base class pointer, only the base class destructor gets called if the destructor is not virtual. This leads to **memory leaks** because the derived class destructor never executes.

```cpp
class Base {
public:
    ~Base() {
        cout << "Base destructor" << endl;
    }
};

class Derived : public Base {
public:
    ~Derived() {
        cout << "Derived destructor" << endl;
    }
};

int main() {
    Base* ptr = new Derived();
    delete ptr;
    return 0;
}
```

**Output (without virtual destructor):**
```
Base destructor
```

### Solution: Virtual Destructor

```cpp
class Base {
public:
    virtual ~Base() {
        cout << "Base destructor" << endl;
    }
};

class Derived : public Base {
public:
    ~Derived() {
        cout << "Derived destructor" << endl;
    }
};

int main() {
    Base* ptr = new Derived();
    delete ptr;
    return 0;
}
```

**Output (with virtual destructor):**
```
Derived destructor
Base destructor
```

### Key Rules:
- **Always make base class destructors virtual** when you have inheritance and plan to delete derived objects through base pointers
- Virtual destructors ensure proper cleanup of all resources in the inheritance hierarchy

---

## 9. The Diamond Problem and Virtual Inheritance {#diamond-problem}

### The Diamond Problem

The diamond problem occurs in multiple inheritance when a class inherits from two classes that both inherit from a common base class. This creates ambiguity because the derived class has two copies of the base class members.

```cpp
class Animal {
public:
    int age;
};

class Mammal : public Animal {};
class Bird : public Animal {};

class Bat : public Mammal, public Bird {};  // Diamond problem!
```

In this case, `Bat` has two separate `age` members—one from `Mammal` and one from `Bird`.

### Solution: Virtual Inheritance

**Virtual inheritance** ensures that only one copy of the base class members exists in the derived class.

```cpp
#include <iostream>
using namespace std;

class Animal {
public:
    int age;
    Animal() { age = 0; cout << "Animal constructor" << endl; }
};

class Mammal : virtual public Animal {
public:
    Mammal() { cout << "Mammal constructor" << endl; }
};

class Bird : virtual public Animal {
public:
    Bird() { cout << "Bird constructor" << endl; }
};

class Bat : public Mammal, public Bird {
public:
    Bat() { cout << "Bat constructor" << endl; }
};

int main() {
    Bat b;
    b.age = 5;
    cout << "Age: " << b.age << endl;
    return 0;
}
```

**Output:**
```
Animal constructor
Mammal constructor
Bird constructor
Bat constructor
Age: 5
```

Now there's only one `age` member, and the `Animal` constructor is called only once.

---

## 10. VTable and VPointer Mechanism {#vtable}

### How Virtual Functions Work: VTable and VPointer

Understanding the internal mechanism of virtual functions is essential for advanced C++ programming.

### VTable (Virtual Table)

The **VTable** is a lookup table of function pointers used to resolve virtual function calls dynamically at runtime. Every class that has at least one virtual function has its own VTable.

### VPointer (VPTR)

The **VPointer** (or VTable Pointer) is a hidden pointer added by the compiler to each object of a class that has virtual functions. This pointer points to the class's VTable.

### How It Works:

1. When a class defines a virtual function, the compiler creates a VTable for that class
2. Each object of that class contains a VPointer that points to its class's VTable
3. When a virtual function is called through a base pointer, the runtime uses the VPointer to access the correct VTable and then the correct function implementation

```cpp
class Base {
public:
    virtual void func1() { cout << "Base::func1" << endl; }
    virtual void func2() { cout << "Base::func2" << endl; }
};

class Derived : public Base {
public:
    void func1() override { cout << "Derived::func1" << endl; }
    virtual void func3() { cout << "Derived::func3" << endl; }
};
```

In this case:
- **Base's VTable**: [func1 → Base::func1, func2 → Base::func2]
- **Derived's VTable**: [func1 → Derived::func1, func2 → Base::func2, func3 → Derived::func3]

### Memory Layout:

```
Base Object:
┌─────────────────┐
│    VPTR         │ ──────► Base VTable
└─────────────────┘
    [Other data]

Derived Object:
┌─────────────────┐
│    VPTR         │ ──────► Derived VTable
└─────────────────┘
    [Other data]
```

### Performance Implications:
- Virtual functions have a small runtime overhead due to indirect function call
- The VTable lookup happens at runtime, adding indirection
- However, modern compilers optimize this effectively

---

## 11. Code Examples {#code-examples}

### Example 1: Runtime Polymorphism with Shapes

```cpp
#include <iostream>
using namespace std;

// Abstract base class
class Shape {
protected:
    string color;
public:
    Shape(string c) : color(c) {}
    
    // Pure virtual function
    virtual double area() = 0;
    
    // Virtual function with default implementation
    virtual void display() {
        cout << "Color: " << color << endl;
    }
    
    virtual ~Shape() {}
};

class Circle : public Shape {
private:
    double radius;
public:
    Circle(string c, double r) : Shape(c), radius(r) {}
    
    double area() override {
        return 3.14159 * radius * radius;
    }
    
    void display() override {
        cout << "Circle - ";
        Shape::display();
        cout << "Radius: " << radius << ", Area: " << area() << endl;
    }
};

class Rectangle : public Shape {
private:
    double length, width;
public:
    Rectangle(string c, double l, double w) : Shape(c), length(l), width(w) {}
    
    double area() override {
        return length * width;
    }
    
    void display() override {
        cout << "Rectangle - ";
        Shape::display();
        cout << "Length: " << length << ", Width: " << width 
             << ", Area: " << area() << endl;
    }
};

class Triangle : public Shape {
private:
    double base, height;
public:
    Triangle(string c, double b, double h) : Shape(c), base(b), height(h) {}
    
    double area() override {
        return 0.5 * base * height;
    }
    
    void display() override {
        cout << "Triangle - ";
        Shape::display();
        cout << "Base: " << base << ", Height: " << height 
             << ", Area: " << area() << endl;
    }
};

int main() {
    // Create array of shape pointers
    Shape* shapes[3];
    
    shapes[0] = new Circle("Red", 5.0);
    shapes[1] = new Rectangle("Blue", 4.0, 6.0);
    shapes[2] = new Triangle("Green", 3.0, 4.0);
    
    cout << "=== Using Base Class Pointer ===" << endl;
    for (int i = 0; i < 3; i++) {
        shapes[i]->display();
        cout << endl;
    }
    
    cout << "=== Total Area Calculation ===" << endl;
    double totalArea = 0;
    for (int i = 0; i < 3; i++) {
        totalArea += shapes[i]->area();
    }
    cout << "Total Area: " << totalArea << endl;
    
    // Clean up
    for (int i = 0; i < 3; i++) {
        delete shapes[i];
    }
    
    return 0;
}
```

### Example 2: Employee Management System with Polymorphism

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Abstract base class
class Employee {
protected:
    string name;
    int id;
    double baseSalary;
    
public:
    Employee(string n, int i, double sal) : name(n), id(i), baseSalary(sal) {}
    
    // Pure virtual function
    virtual double calculateSalary() = 0;
    
    // Virtual function
    virtual void displayInfo() {
        cout << "ID: " << id << ", Name: " << name 
             << ", Base Salary: " << baseSalary << endl;
    }
    
    virtual ~Employee() {}
};

class Manager : public Employee {
private:
    double bonus;
    int teamSize;
    
public:
    Manager(string n, int i, double sal, double b, int ts) 
        : Employee(n, i, sal), bonus(b), teamSize(ts) {}
    
    double calculateSalary() override {
        return baseSalary + bonus + (teamSize * 100);
    }
    
    void displayInfo() override {
        cout << "=== Manager ===" << endl;
        Employee::displayInfo();
        cout << "Bonus: " << bonus << ", Team Size: " << teamSize 
             << ", Total Salary: " << calculateSalary() << endl;
    }
};

class Developer : public Employee {
private:
    string programmingLanguage;
    int overtimeHours;
    
public:
    Developer(string n, int i, double sal, string lang, int ot) 
        : Employee(n, i, sal), programmingLanguage(lang), overtimeHours(ot) {}
    
    double calculateSalary() override {
        return baseSalary + (overtimeHours * 500);
    }
    
    void displayInfo() override {
        cout << "=== Developer ===" << endl;
        Employee::displayInfo();
        cout << "Language: " << programmingLanguage 
             << ", Overtime Hours: " << overtimeHours 
             << ", Total Salary: " << calculateSalary() << endl;
    }
};

class Intern : public Employee {
private:
    string college;
    int hoursWorked;
    
public:
    Intern(string n, int i, double sal, string col, int hw) 
        : Employee(n, i, sal), college(col), hoursWorked(hw) {}
    
    double calculateSalary() override {
        return baseSalary + (hoursWorked * 100);
    }
    
    void displayInfo() override {
        cout << "=== Intern ===" << endl;
        Employee::displayInfo();
        cout << "College: " << college << ", Hours Worked: " << hoursWorked 
             << ", Total Salary: " << calculateSalary() << endl;
    }
};

int main() {
    vector<Employee*> employees;
    
    employees.push_back(new Manager("John Smith", 101, 50000, 10000, 5));
    employees.push_back(new Developer("Alice Johnson", 102, 40000, "C++", 20));
    employees.push_back(new Developer("Bob Williams", 103, 45000, "Python", 15));
    employees.push_back(new Intern("Charlie Brown", 104, 10000, "Delhi University", 80));
    
    cout << "=== Employee Information ===" << endl;
    for (const auto& emp : employees) {
        emp->displayInfo();
        cout << endl;
    }
    
    cout << "=== Total Salary Expenditure ===" << endl;
    double totalSalary = 0;
    for (const auto& emp : employees) {
        totalSalary += emp->calculateSalary();
    }
    cout << "Total: " << totalSalary << endl;
    
    // Cleanup
    for (auto& emp : employees) {
        delete emp;
    }
    
    return 0;
}
```

---

## 12. Key Takeaways {#key-takeaways}

### Inheritance:
- **Inheritance** enables code reusability by allowing derived classes to acquire base class properties
- Five types: Single, Multiple, Multilevel, Hierarchical, and Hybrid
- Access specifiers (public, protected, private) control member visibility in derived classes
- Constructor execution: Base → Derived | Destructor execution: Derived → Base

### Polymorphism:
- **Polymorphism** allows a single interface to represent different forms
- **Runtime polymorphism** is achieved through virtual functions
- **Virtual functions** enable dynamic method resolution based on actual object type
- **Pure virtual functions** (`= 0`) create abstract classes that cannot be instantiated
- **Virtual destructors** ensure proper cleanup when deleting derived objects through base pointers

### Diamond Problem:
- Occurs in multiple inheritance with common base class
- **Virtual inheritance** (`virtual` keyword) solves the diamond problem by ensuring single base class copy

### VTable/VPointer:
- **VTable** is a lookup table of virtual function pointers
- **VPointer** in each object points to class's VTable
- Runtime polymorphism uses VTable lookup for function resolution

### Best Practices:
1. Always use `virtual` destructor in base classes with inheritance
2. Use `override` keyword for clarity and compiler error detection
3. Prefer composition over inheritance when possible
4. Use abstract classes to define interfaces
5. Keep destructors virtual in polymorphic hierarchies

---

## 13. Challenging MCQs {#mcqs}

### Level: University Examination Standard

**Q1. What is the output of the following code?**

```cpp
class A {
public:
    virtual void show() { cout << "A::show" << endl; }
};

class B : public A {
public:
    void show() { cout << "B::show" << endl; }
};

int main() {
    A* ptr = new B();
    ptr->show();
    delete ptr;
    return 0;
}
```
- a) A::show
- b) B::show
- c) Compilation Error
- d) Runtime Error

**Answer: b) B::show**

---

**Q2. Which of the following is TRUE about pure virtual functions?**

- a) They must have implementation in the base class
- b) They make a class abstract
- c) They cannot be destructors
- d) They cannot be overloaded

**Answer: b) They make a class abstract**

---

**Q3. What will be the output?**

```cpp
class Base {
public:
    virtual ~Base() { cout << "Base Destructor" << endl; }
};

class Derived : public Base {
public:
    ~Derived() { cout << "Derived Destructor" << endl; }
};

int main() {
    Base* ptr = new Derived();
    delete ptr;
    return 0;
}
```
- a) Base Destructor
- b) Derived Destructor
- c) Derived Destructor\nBase Destructor
- d) Base Destructor\nDerived Destructor

**Answer: c) Derived Destructor\nBase Destructor**

---

**Q4. In the diamond problem, which keyword is used to resolve it?**

- a) static
- b) virtual
- c) abstract
- d) override

**Answer: b) virtual**

---

**Q5. Which of the following CANNOT be virtual in C++?**

- a) Destructor
- b) Constructor
- c) Static member function
- d) Both b and c

**Answer: d) Both b and c**

---

**Q6. What is the VTable?**

- a) A table of virtual function pointers
- b) A memory allocation table
- c) A lookup table for static functions
- d) A debugging table

**Answer: a) A table of virtual function pointers**

---

**Q7. How many times is the constructor of the base class called in the following?**

```cpp
class A { public: A() { } };
class B : virtual public A { };
class C : virtual public A { };
class D : public B, public C { };

int main() {
    D obj;
    return 0;
}
```
- a) 1
- b) 2
- c) 3
- d) 4

**Answer: a) 1**

---

**Q8. What is an abstract class?**

- a) A class with all pure virtual functions
- b) A class with at least one pure virtual function
- c) A class with no member functions
- d) A class with private constructor

**Answer: b) A class with at least one pure virtual function**

---

**Q9. Which access specifier in inheritance makes private members of base class accessible in derived class?**

- a) Public
- b) Protected
- c) Private
- d) None of the above

**Answer: d) None of the above**

---

**Q10. What does the following declaration mean? `virtual void display() = 0;`**

- a) Display function with no return value
- b) Pure virtual function
- c) Function with default implementation
- d) Static function

**Answer: b) Pure virtual function**

---

## 14. Flashcards for Quick Revision {#flashcards}

### Flashcard Set: Inheritance and Polymorphism

| Term | Definition |
|------|------------|
| **Inheritance** | Mechanism where a derived class acquires properties of a base class |
| **Polymorphism** | Ability of different classes to respond to the same message differently |
| **Virtual Function** | A member function declared with `virtual` keyword, resolved at runtime |
| **Pure Virtual Function** | Virtual function with `= 0`, must be overridden by derived classes |
| **Abstract Class** | Class containing at least one pure virtual function; cannot be instantiated |
| **VTable** | Virtual table - lookup table of function pointers for runtime polymorphism |
| **VPointer** | Hidden pointer in objects pointing to class's VTable |
| **Diamond Problem** | Ambiguity in multiple inheritance when two paths lead to same base class |
| **Virtual Inheritance** | Using `virtual` keyword in inheritance to solve diamond problem |
| **Virtual Destructor** | Destructor marked virtual to ensure proper cleanup of derived objects |

### Quick Reference: Constructor/Destructor Order

```
Constructor Order (for multilevel inheritance A → B → C):
A() → B() → C()

Destructor Order (reverse of constructor):
~C() → ~B() → ~A()

With virtual inheritance (Diamond):
Most derived class constructor calls base class constructor only once
```

### Access Specifiers Quick Reference

| Base Member | Public Derivation | Protected Derivation | Private Derivation |
|-------------|------------------|---------------------|-------------------|
| Public      | Public           | Protected           | Private           |
| Protected   | Protected        | Protected           | Private           |
| Private     | Inaccessible     | Inaccessible        | Inaccessible      |

---

*Study Material prepared for Delhi University BSc Physical Science (CS) - NEP 2024*
*Subject: GE1B - Programming Using C++*
*Topic: Inheritance and Polymorphism*