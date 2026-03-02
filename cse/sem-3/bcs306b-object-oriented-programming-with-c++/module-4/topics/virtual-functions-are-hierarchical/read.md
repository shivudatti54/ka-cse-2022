# Virtual Functions are Hierarchical

## Introduction

Virtual functions form the backbone of runtime polymorphism in C++ and represent one of the most powerful features of object-oriented programming. When we say "virtual functions are hierarchical," we mean that virtual function behavior is determined by the most derived class (the actual object type) rather than the pointer or reference type used to refer to it. This hierarchical behavior allows a program to dispatch function calls at runtime based on the actual object type, enabling flexible and extensible code design.

In the context of the university's BCS306B course, understanding virtual functions is crucial because they form the foundation for implementing polymorphism, which is one of the three pillars of object-oriented programming alongside encapsulation and inheritance. The hierarchical nature of virtual functions means that when a derived class overrides a virtual function from its base class, the override takes precedence in the inheritance hierarchy, creating a chain of function implementations that can be traversed at runtime.

This topic becomes particularly important when designing systems that require dynamic behavior, such as shape drawing applications, game engines, file processing systems, and any scenario where different object types need to be handled uniformly through base class pointers while maintaining their specific behaviors.

## Key Concepts

### What Makes Virtual Functions Hierarchical

A virtual function is a member function declared in a base class with the keyword `virtual` and redefined (overridden) in derived classes. The key characteristic that makes virtual functions hierarchical is the presence of a virtual function table (VTABLE) and a virtual pointer (VPTR) in each object that contains virtual functions.

When a class contains at least one virtual function, the compiler creates a VTABLE for that class. This table contains function pointers to the most appropriate implementation of each virtual function for that class. Each object of such a class contains a hidden VPTR that points to the class's VTABLE. At runtime, when a virtual function is called through a base class pointer or reference, the VPTR is used to look up the correct function implementation based on the actual object type.

### Virtual Function Declaration and Override

Consider a base class `Shape` with a virtual function `draw()`:

```cpp
class Shape {
public:
 virtual void draw() {
 cout << "Drawing a generic shape" << endl;
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
```

In this hierarchy, `draw()` is virtual in the base class and overridden in derived classes. When we call `draw()` through a base class pointer pointing to a derived class object, the hierarchical nature of virtual functions ensures that the derived class version is called.

### The VTABLE-VPTR Mechanism

The hierarchical behavior of virtual functions is implemented through:

1. **VTABLE (Virtual Function Table)**: A static array created by the compiler for each class that contains virtual functions. Each entry in the table is a pointer to the most derived implementation of that virtual function accessible from that class.

2. **VPTR (Virtual Pointer)**: A hidden pointer embedded in each object of a class that has virtual functions. This pointer points to the class's VTABLE.

When a virtual function is called, the runtime system:

- Uses the VPTR in the object to access the VTABLE
- Looks up the function pointer at the appropriate offset
- Calls the function through that pointer

This mechanism ensures that the correct function is called based on the actual object type, not the pointer type.

### Pure Virtual Functions and Abstract Classes

A pure virtual function is declared by assigning 0 to it in the base class:

```cpp
class AbstractShape {
public:
 virtual void draw() = 0; // Pure virtual function
};
```

Classes containing pure virtual functions become abstract classes and cannot be instantiated. They only serve as base classes in a hierarchy. This is another manifestation of the hierarchical nature - the abstract base class defines an interface that derived classes must implement.

### Virtual Destructors

Virtual destructors are crucial in hierarchical inheritance when dealing with polymorphism. When deleting a derived class object through a base class pointer, only the base destructor is called if the destructor is not virtual, leading to resource leaks:

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
```

With a virtual destructor, both destructors are called in the correct order (derived first, then base), demonstrating proper cleanup in the inheritance hierarchy.

### The Override Specifier

C++11 introduced the `override` specifier, which explicitly indicates that a function is intended to override a virtual function in a base class. This helps prevent accidental overloadings due to mismatched function signatures:

```cpp
class Base {
public:
 virtual void func(int x) { }
};

class Derived : public Base {
public:
 void func(int x) override { } // Correct override
 // void func(double x) override { } // Error: doesn't override any base function
};
```

### Object Slicing Problem

When a derived class object is assigned to a base class object (by value), the derived portion is "sliced off," and only the base portion remains. This removes the polymorphic behavior:

```cpp
Derived d;
Base b = d; // Object slicing occurs - no polymorphism
b.draw(); // Calls Base::draw(), not Derived::draw()
```

To preserve polymorphism, we must use pointers or references.

### Virtual Functions in Multiple Inheritance

Virtual functions work with multiple inheritance, but care must be taken when a class inherits from multiple base classes that have virtual functions:

```cpp
class A {
public:
 virtual void func() { }
};

class B {
public:
 virtual void func() { }
};

class C : public A, public B {
public:
 void func() override { } // Ambiguous - needs scope resolution
};
```

In such cases, we need to explicitly specify which base class function we are overriding.

## Examples

### Example 1: Banking System with Polymorphic Interest Calculation

**Problem**: Create a hierarchy where different account types calculate interest differently.

**Solution**:

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

class FixedDepositAccount : public BankAccount {
private:
 int tenure;
public:
 FixedDepositAccount(double b, int t) : BankAccount(b), tenure(t) {}

 double calculateInterest() override {
 return balance * 0.075 * (tenure / 12.0);
 }
};

int main() {
 BankAccount* accounts[3];

 accounts[0] = new BankAccount(10000);
 accounts[1] = new SavingsAccount(10000, 0.06);
 accounts[2] = new FixedDepositAccount(10000, 24);

 for (int i = 0; i < 3; i++) {
 accounts[i]->display();
 cout << "-------------------" << endl;
 }

 // Clean up
 for (int i = 0; i < 3; i++) {
 delete accounts[i];
 }

 return 0;
}
```

**Output**:

```
Balance: 10000
Interest: 400
-------------------
Balance: 10000
Interest: 600
-------------------
Balance: 10000
Interest: 1500
-------------------
```

This example demonstrates how virtual functions create a hierarchical behavior where each derived class provides its own implementation of interest calculation.

### Example 2: Document Processing System

**Problem**: Implement a document processing system where different document types require different processing methods.

**Solution**:

```cpp
#include <iostream>
#include <string>
using namespace std;

class Document {
protected:
 string filename;
public:
 Document(string name) : filename(name) {}

 virtual void open() {
 cout << "Opening document: " << filename << endl;
 }

 virtual void process() {
 cout << "Processing generic document" << endl;
 }

 virtual void save() {
 cout << "Saving document: " << filename << endl;
 }

 virtual ~Document() {}
};

class TextDocument : public Document {
public:
 TextDocument(string name) : Document(name) {}

 void process() override {
 cout << "Performing word count and spell check" << endl;
 }
};

class ImageDocument : public Document {
public:
 ImageDocument(string name) : Document(name) {}

 void process() override {
 cout << "Applying filters and resizing image" << endl;
 }

 void save() override {
 cout << "Compressing and saving image: " << filename << endl;
 }
};

class PDFDocument : public Document {
public:
 PDFDocument(string name) : Document(name) {}

 void process() override {
 cout << "Extracting text and generating thumbnails" << endl;
 }
};

void processDocument(Document* doc) {
 doc->open();
 doc->process();
 doc->save();
 cout << endl;
}

int main() {
 TextDocument textDoc("report.txt");
 ImageDocument imageDoc("photo.jpg");
 PDFDocument pdfDoc("ebook.pdf");

 processDocument(&textDoc);
 processDocument(&imageDoc);
 processDocument(&pdfDoc);

 return 0;
}
```

**Output**:

```
Opening document: report.txt
Performing word count and spell check
Saving document: report.txt

Opening document: photo.jpg
Applying filters and resizing image
Compressing and saving image: photo.jpg

Opening document: ebook.pdf
Extracting text and generating thumbnails
Saving document: ebook.pdf
```

This example shows how the hierarchical nature of virtual functions allows uniform treatment of different document types while maintaining type-specific behavior.

### Example 3: Demonstrating the Slicing Problem

**Problem**: Show how object slicing destroys polymorphism and how to prevent it.

**Solution**:

```cpp
#include <iostream>
using namespace std;

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

 void display() {
 cout << "Derived class display()" << endl;
 }
};

int main() {
 Derived d;
 Base b = d; // Object slicing - derived part is sliced off

 cout << "Calling through sliced object:" << endl;
 b.show(); // Calls Base::show()

 cout << "\nUsing pointer to preserve polymorphism:" << endl;
 Base* ptr = &d;
 ptr->show(); // Calls Derived::show()

 cout << "\nUsing reference to preserve polymorphism:" << endl;
 Base& ref = d;
 ref.show(); // Calls Derived::show()

 return 0;
}
```

**Output**:

```
Calling through sliced object:
Base class show()

Using pointer to preserve polymorphism:
Derived class show()

Using reference to preserve polymorphism:
Derived class show()
```

This example demonstrates that the hierarchical behavior of virtual functions only works through pointers or references, not through value objects.

## Exam Tips

1. **Remember the Virtual Function Rule**: A base class pointer or reference calling a virtual function will always invoke the most derived class implementation, not the base class version.

2. **Virtual Destructor is Mandatory**: Always make destructors virtual when dealing with polymorphic base classes to ensure proper cleanup of derived class resources.

3. **Pure Virtual Functions Create Abstract Classes**: Classes with pure virtual functions (assigned 0) cannot be instantiated and serve as interfaces for derived classes.

4. **Override Keyword Prevents Errors**: Always use the C++11 `override` specifier when overriding virtual functions to catch signature mismatches at compile time.

5. **Slicing Destroys Polymorphism**: Passing objects by value to base class parameters causes slicing, removing the polymorphic behavior. Always use pointers or references.

6. **VTABLE is Class-Specific, Not Object-Specific**: Each class with virtual functions has one VTABLE, shared by all objects of that class. The VPTR is what makes each object point to its class's VTABLE.

7. **Constructors Cannot Be Virtual**: Virtual functions rely on the VPTR, which is not set up until after the constructor runs. Therefore, constructors cannot be virtual.

8. **Default Arguments Use Static Binding**: Virtual functions use dynamic binding for the function implementation, but default arguments use static binding (based on the pointer type, not object type).

9. **Private Virtual Functions Can Still Be Overridden**: A virtual function can be private in the base class but still be overridden and called polymorphically in derived classes.

10. **Destructors Call in Reverse Order**: When a derived object is destroyed through a base pointer with virtual destructor, the derived destructor runs first, then the base destructor.
