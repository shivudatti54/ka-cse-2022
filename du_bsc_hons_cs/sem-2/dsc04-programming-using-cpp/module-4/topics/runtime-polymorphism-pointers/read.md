# Runtime Polymorphism Using Pointers in C++

## Comprehensive Study Material for BSc (Hons) Computer Science - Delhi University (NEP 2024 UGCF)

---

## Table of Contents
1. [Introduction and Real-World Relevance](#introduction-and-real-world-relevance)
2. [Understanding Polymorphism](#understanding-polymorphism)
3. [Key Concepts in Runtime Polymorphism](#key-concepts-in-runtime-polymorphism)
4. [Virtual Tables (vtables) - The Hidden Mechanism](#virtual-tables-vtables---the-hidden-mechanism)
5. [Virtual Destructors - Critical for Proper Cleanup](#virtual-destructors---critical-for-proper-cleanup)
6. [The Slicing Problem](#the-slicing-problem)
7. [Comprehensive Code Examples](#comprehensive-code-examples)
8. [Multiple Choice Questions](#multiple-choice-questions)
9. [Flashcards for Quick Revision](#flashcards-for-quick-revision)
10. [Key Takeaways](#key-takeaways)

---

## Introduction and Real-World Relevance

### What is Runtime Polymorphism?

**Runtime polymorphism** (also known as **dynamic polymorphism**) is a core object-oriented programming concept that allows the program to determine which function to execute at **runtime** rather than at compile time. In C++, this is achieved through the use of **virtual functions** and **pointers/references** to base classes.

### Real-World Analogy

Consider a **smartphone charging system**: You have a common charging port (the base class interface), but different phone models (derived classes) implement their own specific charging logic. When you plug in a charger (base class pointer), the phone's actual model determines the charging speed and protocol at runtime—this is analogous to runtime polymorphism!

### Why This Topic Matters for Delhi University Students

This topic is a **core component** of the BSc (Hons) Computer Science syllabus under "Programming Using C++" (Paper III: Object-Oriented Programming). Understanding runtime polymorphism is essential for:
- Building extensible and maintainable software
- Understanding design patterns (Strategy, Factory, Template Method)
- Developing game engines, GUI frameworks, and simulation systems
- Acing university examinations and practical exams

---

## Understanding Polymorphism

### Compile-Time vs Runtime Polymorphism

| Aspect | Compile-Time (Static) | Runtime (Dynamic) |
|--------|----------------------|-------------------|
| **Binding Time** | Compile time | Runtime |
| **Mechanism** | Function overloading, templates | Virtual functions |
| **Performance** | Faster (no lookup) | Slightly slower (vtable lookup) |
| **Flexibility** | Less flexible | Highly flexible |

### The Need for Runtime Polymorphism

```cpp
// Without polymorphism - rigid code
class Dog { public: void speak() { cout << "Woof"; } };
class Cat { public: void speak() { cout << "Meow"; } };

void makeSpeak(Dog d) { d.speak(); }  // Must have separate functions
void makeSpeak(Cat c) { c.speak(); }  // for each type!
```

```cpp
// With polymorphism - flexible code
class Animal {
public:
    virtual void speak() = 0;  // Pure virtual function
    virtual ~Animal() {}       // Virtual destructor
};

class Dog : public Animal {
public:
    void speak() override { cout << "Woof"; }
};

class Cat : public Animal {
public:
    void speak() override { cout << "Meow"; }
};

void makeSpeak(Animal* a) {  // Single function handles all types!
    a->speak();  // Resolved at runtime based on actual object type
}
```

---

## Key Concepts in Runtime Polymorphism

### 1. Virtual Functions

A **virtual function** is a member function that is declared in a base class and **redefined** in derived classes. The function to be called is determined at runtime based on the actual object type (not the pointer type).

**Syntax:**
```cpp
class Base {
public:
    virtual void display() {  // 'virtual' keyword is essential
        cout << "Base display";
    }
};

class Derived : public Base {
public:
    void display() override {  // 'override' is optional but recommended
        cout << "Derived display";
    }
};
```

### 2. Key Virtual Function Rules

- Virtual functions cannot be static
- Virtual functions can be friend functions of another class
- A virtual function in base class may or may not have implementation
- Constructors cannot be virtual (but destructors can and should be)
- If a derived class doesn't override a virtual function, it uses the base implementation

### 3. Pure Virtual Functions and Abstract Classes

A **pure virtual function** makes a class **abstract** (cannot be instantiated):

```cpp
class Shape {
public:
    virtual void draw() = 0;  // Pure virtual function (abstract)
    virtual double area() = 0;
};

class Circle : public Shape {
    double radius;
public:
    void draw() override { /* drawing code */ }
    double area() override { return 3.14 * radius * radius; }
};
```

---

## Virtual Tables (vtables) - The Hidden Mechanism

### How vtables Work

Every class with virtual functions has a hidden **vtable** (virtual table) created by the compiler. This is a **static array of function pointers**.

### vtable Structure Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    MEMORY LAYOUT EXPLANATION                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  For Base Class:                                                │
│  ┌──────────────────┐                                           │
│  │    Base Object   │                                           │
│  ├──────────────────┤                                           │
│  │ vptr (pointer) ──┼──► ┌─────────────────────────┐           │
│  │ other members    │    │  Base vtable            │           │
│  └──────────────────┘    │  ─────────────────────  │           │
│                          │  &Base::show()          │           │
│                          └─────────────────────────┘           │
│                                                                 │
│  For Derived Class:                                             │
│  ┌──────────────────┐                                           │
│  │   Derived Object │                                           │
│  ├──────────────────┤                                           │
│  │ vptr (pointer) ──┼──► ┌─────────────────────────┐           │
│  │ other members    │    │  Derived vtable         │           │
│  └──────────────────┘    │  ─────────────────────  │           │
│                          │  &Derived::show() ◄─────┘           │
│                          └─────────────────────────┘           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Code Demonstration of vtable Concept

```cpp
#include <iostream>
using namespace std;

class Base {
public:
    virtual void func1() { cout << "Base::func1\n"; }
    virtual void func2() { cout << "Base::func2\n"; }
    virtual ~Base() {}  // Virtual destructor
};

class Derived : public Base {
public:
    void func1() override { cout << "Derived::func1 (overridden)\n"; }
    virtual void func3() { cout << "Derived::func3\n"; }
};

int main() {
    Base* ptr = new Derived();  // Base pointer to Derived object
    
    // Runtime polymorphism - vtable lookup happens here
    ptr->func1();   // Calls Derived::func1 (not Base::func1!)
    ptr->func2();   // Calls Base::func2 (not overridden)
    // ptr->func3(); // ERROR: Base doesn't know about func3
    
    delete ptr;  // Properly calls Derived destructor via vtable
    
    return 0;
}
```

**Output:**
```
Derived::func1 (overridden)
Base::func2
```

---

## Virtual Destructors - Critical for Proper Cleanup

### The Problem Without Virtual Destructors

```cpp
#include <iostream>
using namespace std;

class Base {
public:
    Base() { cout << "Base constructor\n"; }
    ~Base() { cout << "Base destructor\n"; }  // NOT virtual!
};

class Derived : public Base {
public:
    Derived() { cout << "Derived constructor\n"; }
    ~Derived() { cout << "Derived destructor\n"; }  // Never called!
};

int main() {
    Base* ptr = new Derived();
    delete ptr;  // Only Base destructor called - MEMORY LEAK!
    return 0;
}
```

**Output (INCORRECT):**
```
Base constructor
Derived constructor
Base destructor    // Derived destructor was NEVER called!
```

### The Solution: Virtual Destructors

```cpp
#include <iostream>
using namespace std;

class Base {
public:
    Base() { cout << "Base constructor\n"; }
    virtual ~Base() { cout << "Base destructor\n"; }  // VIRTUAL!
};

class Derived : public Base {
public:
    Derived() { cout << "Derived constructor\n"; }
    ~Derived() { cout << "Derived destructor\n"; }  // Now called!
};

int main() {
    Base* ptr = new Derived();
    delete ptr;  // Correctly calls both destructors
    return 0;
}
```

**Output (CORRECT):**
```
Base constructor
Derived constructor
Derived destructor
Base destructor
```

### When to Use Virtual Destructors

✅ **Always use virtual destructors** when:
- A class contains at least one virtual function
- The class is intended to be a base class
- Objects of derived classes will be deleted through base class pointers

---

## The Slicing Problem

### What is Object Slicing?

**Slicing** occurs when a derived class object is assigned to a base class object, **losing all derived-class-specific information** (the "sliced" parts).

### Code Demonstration of Slicing

```cpp
#include <iostream>
using namespace std;

class Base {
public:
    int baseData;
    virtual void show() { cout << "Base show\n"; }
};

class Derived : public Base {
public:
    int derivedData;
    void show() override { cout << "Derived show\n"; }
};

int main() {
    Derived d;
    d.baseData = 10;
    d.derivedData = 20;
    
    // SLICING: Object is "sliced" when assigned to base object
    Base b = d;  // Slicing happens here!
    
    b.show();    // Calls Base::show (not virtual - no vtable involved)
    cout << "b.baseData: " << b.baseData << endl;
    // cout << b.derivedData; // ERROR: derivedData is sliced off!
    
    // Preventing Slicing: Use pointers or references
    Base* ptr = &d;  // No slicing - pointer to original object
    ptr->show();     // Calls Derived::show (polymorphism works!)
    
    Base& ref = d;   // No slicing - reference to original object
    ref.show();      // Calls Derived::show (polymorphism works!)
    
    return 0;
}
```

### How to Prevent Slicing

1. **Use pointers** (`Base* ptr = &derivedObj;`)
2. **Use references** (`Base& ref = derivedObj;`)
3. **Use smart pointers** (`std::unique_ptr<Base>`)

---

## Comprehensive Code Examples

### Example 1: Banking System with Polymorphism

```cpp
#include <iostream>
#include <string>
using namespace std;

// Abstract base class
class Account {
protected:
    string accountHolder;
    double balance;
    int accountNumber;

public:
    Account(string name, double bal, int accNo) 
        : accountHolder(name), balance(bal), accountNumber(accNo) {}
    
    // Pure virtual function - makes Account abstract
    virtual void calculateInterest() = 0;
    
    // Virtual destructor for proper cleanup
    virtual ~Account() {
        cout << "Account " << accountNumber << " destroyed\n";
    }
    
    // Common function
    void display() {
        cout << "Account #: " << accountNumber 
             << ", Holder: " << accountHolder 
             << ", Balance: $" << balance << endl;
    }
    
    // Getter
    double getBalance() { return balance; }
};

// Savings Account - earns compound interest
class SavingsAccount : public Account {
private:
    double interestRate;

public:
    SavingsAccount(string name, double bal, int accNo, double rate)
        : Account(name, bal, accNo), interestRate(rate) {}
    
    void calculateInterest() override {
        double interest = balance * interestRate;
        balance += interest;
        cout << "Savings Interest: $" << interest << endl;
    }
    
    ~SavingsAccount() {
        cout << "Savings Account destroyed\n";
    }
};

// Checking Account - earns simple interest
class CheckingAccount : public Account {
private:
    double fee;

public:
    CheckingAccount(string name, double bal, int accNo, double fee)
        : Account(name, bal, accNo), fee(fee) {}
    
    void calculateInterest() override {
        double interest = balance * 0.02;  // 2% simple interest
        balance = balance + interest - fee;
        cout << "Checking Interest (less fee): $" << interest - fee << endl;
    }
    
    ~CheckingAccount() {
        cout << "Checking Account destroyed\n";
    }
};

// Function that demonstrates runtime polymorphism
void processAccount(Account* acc) {
    acc->display();
    acc->calculateInterest();
    acc->display();
    cout << "------------------------\n";
}

int main() {
    // Array of base class pointers - demonstrates polymorphism
    Account* accounts[3];
    
    accounts[0] = new SavingsAccount("Alice", 1000.0, 1001, 0.05);
    accounts[1] = new CheckingAccount("Bob", 2000.0, 1002, 25.0);
    accounts[2] = new SavingsAccount("Charlie", 5000.0, 1003, 0.07);
    
    // Process each account polymorphically
    for (int i = 0; i < 3; i++) {
        processAccount(accounts[i]);
    }
    
    // Proper cleanup - virtual destructor ensures derived destructors called
    for (int i = 0; i < 3; i++) {
        delete accounts[i];
    }
    
    return 0;
}
```

### Example 2: Shape Drawing System with Override Keyword

```cpp
#include <iostream>
#include <cmath>
using namespace std;

// Abstract base class for all shapes
class Shape {
protected:
    string color;
    
public:
    Shape(string c = "white") : color(c) {}
    
    // Pure virtual functions
    virtual double area() = 0;
    virtual double perimeter() = 0;
    
    // Virtual destructor
    virtual ~Shape() {}
    
    // Non-virtual function - not overridden
    void setColor(string c) { color = c; }
    string getColor() { return color; }
};

class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(double r, string c = "red") : Shape(c), radius(r) {}
    
    // Override keyword ensures we're actually overriding
    double area() override {
        return M_PI * radius * radius;
    }
    
    double perimeter() override {
        return 2 * M_PI * radius;
    }
    
    // Specific to Circle
    double getRadius() { return radius; }
};

class Rectangle : public Shape {
private:
    double width, height;
    
public:
    Rectangle(double w, double h, string c = "blue") 
        : Shape(c), width(w), height(h) {}
    
    double area() override {
        return width * height;
    }
    
    double perimeter() override {
        return 2 * (width + height);
    }
};

class Triangle : public Shape {
private:
    double a, b, c;  // three sides
    
public:
    Triangle(double side1, double side2, double side3, string c = "green")
        : Shape(c), a(side1), b(side2), c(side3) {}
    
    double area() override {
        // Heron's formula
        double s = (a + b + c) / 2;
        return sqrt(s * (s - a) * (s - b) * (s - c));
    }
    
    double perimeter() override {
        return a + b + c;
    }
};

// Function demonstrating polymorphism with array of pointers
void printShapeInfo(Shape* s) {
    cout << "Color: " << s->getColor() << endl;
    cout << "Area: " << s->area() << endl;
    cout << "Perimeter: " << s->perimeter() << endl;
    cout << endl;
}

int main() {
    // Array of base class pointers - polymorphism in action
    Shape* shapes[3];
    
    shapes[0] = new Circle(5.0);
    shapes[1] = new Rectangle(4.0, 6.0);
    shapes[2] = new Triangle(3.0, 4.0, 5.0);
    
    cout << "=== Shape Information (via base class pointers) ===\n\n";
    
    for (int i = 0; i < 3; i++) {
        printShapeInfo(shapes[i]);
    }
    
    // Demonstrate override keyword usage
    cout << "=== Using override keyword ===\n";
    Circle* c = new Circle(10.0, "yellow");
    c->setColor("orange");
    cout << "Modified circle color: " << c->getColor() << endl;
    
    // Cleanup
    for (int i = 0; i < 3; i++) {
        delete shapes[i];
    }
    delete c;
    
    return 0;
}
```

---

## Multiple Choice Questions

### Basic Level

**Question 1:** What keyword is used to declare a virtual function in C++?
- A) `abstract`
- B) `virtual`
- C) `override`
- D) `polymorphic`

**Question 2:** Which of the following is required for runtime polymorphism?
- A) Static binding
- B) Function overloading
- C) Virtual functions and base class pointers
- D) Template functions

### Intermediate Level

**Question 3:** What is the output of the following code?

```cpp
class A {
public:
    virtual void show() { cout << "A::show"; }
};

class B : public A {
public:
    void show() { cout << "B::show"; }
};

int main() {
    A* p = new B();
    p->show();
    delete p;
    return 0;
}
```
- A) A::show
- B) B::show
- C) Compiler Error
- D) Runtime Error

**Question 4:** What problem does object slicing cause?
- A) Loss of virtual function behavior
- B) Loss of derived class data members
- C) Memory leak
- D) Both B and loss of polymorphic behavior

### Advanced Level (Scenario-Based)

**Question 5:** Consider a game development scenario where you have a base class `Enemy` with virtual function `attack()`, and derived classes `Dragon`, `Goblin`, and `Orc` override this function. If you store pointers to different enemy types in a `std::vector<Enemy*>`, what is the primary advantage of using virtual functions?

- A) Faster compilation time
- B) Each enemy type's specific attack behavior is executed at runtime
- C) Memory consumption is reduced
- D) The code becomes harder to maintain

**Question 6 (Code Tracing):**

```cpp
#include <iostream>
using namespace std;

class Base {
    int x;
public:
    Base(int i = 0) : x(i) { cout << "Base " << x << " "; }
    virtual ~Base() { cout << "~Base "; }
};

class Derived : public Base {
    int y;
public:
    Derived(int i = 0, int j = 1) : Base(i), y(j) { cout << "Derived " << y << " "; }
    ~Derived() { cout << "~Derived "; }
};

int main() {
    Base* ptr = new Derived(5, 10);
    delete ptr;
    return 0;
}
```

What is the correct output?
- A) Base 5 Derived 10 ~Derived ~Base
- B) Base 5 Derived 10 ~Base
- C) Base 5 Derived 10 ~Base ~Derived
- D) Derived 10 Base 5 ~Base ~Derived

**Question 7 (Scenario-Based):** You are designing a library management system with a base class `Resource` and derived classes `Book`, `DVD`, and `Magazine`. The base class has a virtual function `calculateLateFee()` that returns 0 by default. Which of the following is the MOST appropriate design choice?

- A) Make `calculateLateFee()` a non-virtual function
- B) Make `calculateLateFee()` a pure virtual function
- C) Remove the function from the base class
- D) Make `calculateLateFee()` private

### Expert Level

**Question 8:** Which statement is TRUE about vtables?
- A) Every class has a vtable whether or not it has virtual functions
- B) The vtable is created at runtime when virtual functions are called
- C) Each object with virtual functions contains a vptr pointing to its class's vtable
- D) vtables are stored in the stack segment

**Question 9 (Code Tracing):**

```cpp
class Parent {
public:
    virtual void method() { cout << "Parent"; }
};

class Child : public Parent {
public:
    void method() override { cout << "Child"; }
};

class GrandChild : public Child {
public:
    void method() override { cout << "GrandChild"; }
};

int main() {
    Parent* p = new GrandChild();
    p->method();
    delete p;
    return 0;
}
```
What is the output?
- A) Parent
- B) Child
- C) GrandChild
- D) Compiler Error

**Question 10 (Debugging Scenario):** A developer creates a base class `Employee` with a virtual function `calculateBonus()` and derives `Manager` and `Developer` from it. The program crashes when deleting objects through base class pointers. What is the MOST likely issue?

- A) Missing `override` keyword
- B) Non-virtual destructor in base class
- C) Private virtual function
- D) Using `new` incorrectly

---

### Answer Key

| Question | Answer | Explanation |
|----------|--------|--------------|
| 1 | B | `virtual` keyword declares virtual functions |
| 2 | C | Runtime polymorphism requires virtual functions + pointers/references |
| 3 | B | Virtual function calls resolved at runtime → B::show |
| 4 | D | Slicing loses derived data AND polymorphic behavior |
| 5 | B | Runtime polymorphism allows each enemy type to use its specific attack |
| 6 | A | Virtual destructor ensures proper cleanup order: Derived then Base |
| 7 | B | Pure virtual forces derived classes to implement their own late fee calculation |
| 8 | C | Each object with virtual functions has a vptr to its class's vtable |
| 9 | C | Three-level inheritance: GrandChild's override is called |
| 10 | B | Non-virtual destructor causes undefined behavior when deleting through base pointer |

---

## Flashcards for Quick Revision

### Flashcard 1
**Term:** Runtime Polymorphism
**Definition:** A programming concept where function calls are resolved at runtime based on the actual object type (not the pointer type), enabling dynamic behavior.

### Flashcard 2
**Term:** Virtual Function
**Definition:** A member function declared in a base class with the `virtual` keyword, which can be overridden in derived classes. The correct version is called at runtime through the vtable.

### Flashcard 3
**Term:** Pure Virtual Function
**Definition:** A virtual function with `= 0` syntax that has no implementation in the base class. Makes the class abstract (cannot instantiate objects).

### Flashcard 4
**Term:** Virtual Destructor
**Definition:** A destructor declared as `virtual` in the base class. Ensures proper cleanup of derived class resources when objects are deleted through base class pointers.

### Flashcard 5
**Term:** vtable (Virtual Table)
**Definition:** A compiler-generated data structure (array of function pointers) for classes with virtual functions. Each object contains a vptr pointing to this table, enabling runtime function resolution.

### Flashcard 6
**Term:** Object Slicing
**Definition:** The problem where assigning a derived class object to a base class object (by value) loses the derived class data and behavior. Prevent by using pointers or references.

### Flashcard 7
**Term:** Abstract Class
**Definition:** A class containing at least one pure virtual function. Cannot be instantiated but can serve as a base class for derived classes.

### Flashcard 8
**Term:** override Keyword
**Definition:** A C++11 keyword used in derived classes to explicitly indicate that a function overrides a virtual function from the base class. Compiler checks for correct override.

### Flashcard 9
**Term:** Diamond Problem (Multiple Inheritance)
**Definition:** An ambiguity issue when a class inherits from two classes that share a common base. Resolved using virtual inheritance.

### Flashcard 10
**Term:** vptr (Virtual Pointer)
**Definition:** A hidden pointer added by the compiler to each object of a class with virtual functions. Points to the class's vtable.

---

## Key Takeaways

### Core Concepts to Remember

1. **Runtime polymorphism requires THREE elements:**
   - Base class with virtual function(s)
   - Derived class(es) overriding those functions
   - Base class pointer (or reference) pointing to derived class object

2. **Virtual functions enable dynamic dispatch** through the vtable mechanism at runtime

3. **Always use virtual destructors** in base classes intended for polymorphic deletion

4. **Object slicing** occurs when derived objects are copied by value into base objects—prevent it with pointers/references

5. **Pure virtual functions** create abstract classes that serve as interfaces

6. **The `override` keyword** helps catch errors at compile-time when overriding functions

### Delhi University Examination Tips

- **Question patterns:** Expect questions on identifying output, finding errors, and explaining the difference between compile-time and runtime polymorphism
- **Code tracing:** Practice identifying which function gets called through base class pointers
- **vtable understanding:** Know how vptr and vtable work together for virtual function resolution
- **Slicing problem:** Be prepared to explain what slicing is and how to prevent it

### Practical Applications

- **Design patterns:** Strategy, Factory, Template Method all rely on runtime polymorphism
- **Framework development:** GUI frameworks (Qt, wxWidgets), game engines, and plugin systems
- **API design:** Creating extensible libraries where users can provide custom implementations

---

*Study Material prepared for BSc (Hons) Computer Science - Delhi University (NEP 2024 UGCF)*