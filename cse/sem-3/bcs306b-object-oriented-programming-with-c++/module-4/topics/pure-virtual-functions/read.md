# Pure Virtual Functions in C++

## Introduction

Pure virtual functions are one of the most powerful features of object-oriented programming in C++, enabling the creation of abstract base classes that define interfaces without implementations. This concept is fundamental to achieving polymorphism and implementing design patterns such as the Strategy Pattern, Template Method Pattern, and Factory Pattern. In the context of the university's Object Oriented Programming with C++ curriculum, understanding pure virtual functions is essential for developing flexible and extensible software systems.

When we design class hierarchies, we often encounter situations where we want to define a common interface for a group of related classes while leaving the actual implementation to derived classes. Pure virtual functions provide exactly this mechanism - they declare a function in the base class with no implementation, forcing every derived class that wishes to be instantiated to provide its own implementation. This creates a contract between the base class and its derived classes, ensuring that certain methods are always implemented.

The concept of pure virtual functions leads to what is known as an abstract class - a class that cannot be instantiated directly but serves as a blueprint for derived classes. Abstract classes are extensively used in frameworks and libraries to define extensible systems where the framework provides the skeleton and user code fills in the specific details. This approach is central to many design patterns and is a hallmark of well-designed object-oriented systems.

## Key Concepts

### Syntax of Pure Virtual Functions

A pure virtual function is declared by assigning 0 to the function declaration. The syntax is:

```cpp
virtual return_type function_name(parameters) = 0;
```

The `= 0` syntax is called the pure specifier. It tells the compiler that this function has no implementation in this class and that the class is abstract. For example:

```cpp
class Shape {
public:
 virtual void draw() = 0; // Pure virtual function
 virtual double area() = 0; // Pure virtual function
};
```

It is important to note that you cannot create objects of an abstract class, but you can have pointers and references to abstract classes. This is the foundation for runtime polymorphism in C++.

### Abstract Classes

An abstract class in C++ is a class that contains at least one pure virtual function. While you cannot instantiate an abstract class directly, you can:

1. Declare pointers and references to the abstract class
2. Use abstract classes as base classes for derived classes
3. Implement some concrete methods in the abstract class alongside pure virtual functions

Consider this example:

```cpp
class Animal {
protected:
 string name;
public:
 Animal(string n) : name(n) {}

 // Pure virtual function - must be implemented by derived classes
 virtual void speak() = 0;

 // Concrete method - inherited by all derived classes
 void displayName() {
 cout << "Animal name: " << name << endl;
 }
};

class Dog : public Animal {
public:
 Dog(string n) : Animal(n) {}

 void speak() override {
 cout << name << " says: Woof!" << endl;
 }
};

class Cat : public Animal {
public:
 Cat(string n) : Animal(n) {}

 void speak() override {
 cout << name << " says: Meow!" << endl;
 }
};
```

In this example, `Animal` is an abstract class with a pure virtual function `speak()`. The derived classes `Dog` and `Cat` provide their own implementations of `speak()`, making them concrete classes that can be instantiated.

### Interface Classes

An interface in C++ is typically implemented as an abstract class with only pure virtual functions and no data members. Interfaces define a contract without any implementation details. This is similar to interfaces in languages like Java, though C++ does not have a dedicated interface keyword.

```cpp
// Interface for printable objects
class Printable {
public:
 virtual void print(ostream& out) const = 0;
 virtual ~Printable() {}
};

// Interface for comparable objects
class Comparable {
public:
 virtual bool operator<(const Comparable& other) const = 0;
 virtual bool operator>(const Comparable& other) const = 0;
 virtual ~Comparable() {}
};
```

Interface classes are particularly useful for:

- Defining capabilities that multiple unrelated classes can share
- Achieving multiple inheritance where a class can inherit from multiple interfaces
- Decoupling code through dependency injection

### Virtual Destructors and Pure Virtual Destructors

When dealing with polymorphic deletion through base class pointers, it is crucial to have a virtual destructor in the abstract class. A pure virtual destructor is a special case:

```cpp
class Base {
public:
 virtual ~Base() = 0; // Pure virtual destructor
};

// Must provide implementation for pure virtual destructor
Base::~Base() {
 // Cleanup code if needed
}
```

Even though the destructor is pure virtual, you must provide an implementation for it. This is because when derived class objects are destroyed, the compiler generates code to call the base class destructor, and an implementation must exist.

### Virtual Function Table (vtable) and Pure Virtual Functions

To understand how pure virtual functions work internally, we need to briefly discuss the virtual function table (vtable). Each class that has virtual functions (including abstract classes) has a vtable - a table of function pointers. For abstract classes, the entry for pure virtual functions typically points to a special "pure virtual function" handler that terminates the program if called directly.

When a derived class overrides a pure virtual function, the vtable entry is updated to point to the derived class's implementation. This mechanism enables runtime polymorphism - the correct function is called based on the actual object type, not the pointer type.

## Examples

### Example 1: Shape Hierarchy with Area Calculation

```cpp
#include <iostream>
using namespace std;

class Shape {
protected:
 string color;
public:
 Shape(string c) : color(c) {}

 // Pure virtual functions
 virtual double area() const = 0;
 virtual void draw() const = 0;

 virtual ~Shape() {}
};

class Circle : public Shape {
private:
 double radius;
public:
 Circle(string c, double r) : Shape(c), radius(r) {}

 double area() const override {
 return 3.14159 * radius * radius;
 }

 void draw() const override {
 cout << "Drawing a circle with radius " << radius
 << " in color " << color << endl;
 }
};

class Rectangle : public Shape {
private:
 double length, width;
public:
 Rectangle(string c, double l, double w) : Shape(c), length(l), width(w) {}

 double area() const override {
 return length * width;
 }

 void draw() const override {
 cout << "Drawing a rectangle " << length << "x" << width
 << " in color " << color << endl;
 }
};

class Triangle : public Shape {
private:
 double base, height;
public:
 Triangle(string c, double b, double h) : Shape(c), base(b), height(h) {}

 double area() const override {
 return 0.5 * base * height;
 }

 void draw() const override {
 cout << "Drawing a triangle with base " << base
 << " and height " << height << " in color " << color << endl;
 }
};

int main() {
 // Cannot create Shape objects - it's abstract
 // Shape s("red"); // Error!

 Shape* shapes[] = {
 new Circle("Red", 5.0),
 new Rectangle("Blue", 4.0, 6.0),
 new Triangle("Green", 3.0, 4.0)
 };

 double totalArea = 0.0;
 for (int i = 0; i < 3; i++) {
 shapes[i]->draw();
 totalArea += shapes[i]->area();
 }

 cout << "Total area: " << totalArea << endl;

 // Cleanup
 for (int i = 0; i < 3; i++) {
 delete shapes[i];
 }

 return 0;
}
```

This example demonstrates polymorphism where different derived classes implement the pure virtual functions differently, and we can treat them uniformly through base class pointers.

### Example 2: Payment Processing System

```cpp
#include <iostream>
#include <string>
using namespace std;

class PaymentProcessor {
protected:
 string merchantId;
public:
 PaymentProcessor(string mid) : merchantId(mid) {}

 // Pure virtual functions defining the payment interface
 virtual bool processPayment(double amount) = 0;
 virtual bool refundPayment(string transactionId) = 0;
 virtual string getPaymentType() const = 0;

 virtual ~PaymentProcessor() {}
};

class CreditCardProcessor : public PaymentProcessor {
private:
 string cardNumber;
public:
 CreditCardProcessor(string mid, string card)
 : PaymentProcessor(mid), cardNumber(card) {}

 bool processPayment(double amount) override {
 cout << "Processing credit card payment of $" << amount << endl;
 cout << "Card: " << cardNumber.substr(0, 4) << "****" << endl;
 return true;
 }

 bool refundPayment(string transactionId) override {
 cout << "Refunding credit card transaction: " << transactionId << endl;
 return true;
 }

 string getPaymentType() const override {
 return "Credit Card";
 }
};

class PayPalProcessor : public PaymentProcessor {
private:
 string email;
public:
 PayPalProcessor(string mid, string em)
 : PaymentProcessor(mid), email(em) {}

 bool processPayment(double amount) override {
 cout << "Processing PayPal payment of $" << amount << endl;
 cout << "Account: " << email << endl;
 return true;
 }

 bool refundPayment(string transactionId) override {
 cout << "Refunding PayPal transaction: " << transactionId << endl;
 return true;
 }

 string getPaymentType() const override {
 return "PayPal";
 }
};

class CryptoProcessor : public PaymentProcessor {
private:
 string walletAddress;
public:
 CryptoProcessor(string mid, string wallet)
 : PaymentProcessor(mid), walletAddress(wallet) {}

 bool processPayment(double amount) override {
 cout << "Processing cryptocurrency payment of $" << amount << endl;
 cout << "Wallet: " << walletAddress << endl;
 return true;
 }

 bool refundPayment(string transactionId) override {
 cout << "Cryptocurrency refunds not supported" << endl;
 return false;
 }

 string getPaymentType() const override {
 return "Cryptocurrency";
 }
};

void processOrder(PaymentProcessor& processor, double amount) {
 cout << "\n--- Processing with " << processor.getPaymentType() << " ---" << endl;
 processor.processPayment(amount);
}

int main() {
 CreditCardProcessor cc("MERCH001", "4111111111111111");
 PayPalProcessor pp("MERCH002", "user@example.com");
 CryptoProcessor crypto("MERCH003", "0x1234ABCD");

 processOrder(cc, 99.99);
 processOrder(pp, 149.99);
 processOrder(crypto, 199.99);

 return 0;
}
```

This example shows how pure virtual functions create a flexible payment processing system where new payment methods can be added by simply deriving from the abstract base class.

### Example 3: Document Processing with Interface

```cpp
#include <iostream>
#include <fstream>
using namespace std;

// Interface for serializable documents
class Serializable {
public:
 virtual void serialize(ofstream& file) const = 0;
 virtual void deserialize(ifstream& file) = 0;
 virtual ~Serializable() {}
};

// Interface for documents that can be displayed
class Displayable {
public:
 virtual void display() const = 0;
 virtual void preview() const = 0;
 virtual ~Displayable() {}
};

// Concrete implementation
class Report : public Serializable, public Displayable {
private:
 string title;
 string content;
 int pages;
public:
 Report(string t, string c, int p) : title(t), content(c), pages(p) {}

 // Serializable implementation
 void serialize(ofstream& file) const override {
 file << title << endl;
 file << content << endl;
 file << pages << endl;
 }

 void deserialize(ifstream& file) override {
 getline(file, title);
 getline(file, content);
 file >> pages;
 }

 // Displayable implementation
 void display() const override {
 cout << "=== " << title << " ===" << endl;
 cout << "Pages: " << pages << endl;
 cout << content << endl;
 }

 void preview() const override {
 cout << "[Preview] " << title << " (" << pages << " pages)" << endl;
 }
};

int main() {
 Report report("Annual Report", "This is the annual report content...", 50);

 // Use Displayable interface
 Displayable* displayable = &report;
 displayable->display();
 cout << endl;
 displayable->preview();

 return 0;
}
```

This demonstrates multiple inheritance with interfaces and how pure virtual functions enable a class to implement multiple contracts.

## Exam Tips

1. **Remember the syntax**: Pure virtual functions are declared using `virtual return_type function_name() = 0;`. The `= 0` is the pure specifier and is unique to C++.

2. **Abstract classes cannot be instantiated**: If a class has even one pure virtual function, you cannot create objects of that class. This is a common exam question.

3. **Derived classes must implement all pure virtual functions**: A derived class that does not implement all pure virtual functions remains abstract and cannot be instantiated.

4. **Virtual destructor is essential**: When using polymorphism with abstract classes, always make the destructor virtual to ensure proper cleanup of derived class objects through base class pointers.

5. **Can have concrete methods in abstract classes**: An abstract class can contain both pure virtual functions and regular concrete methods with implementations.

6. **Pointers and references work**: You can have pointers and references to abstract classes, which enables runtime polymorphism.

7. **Pure virtual functions can have implementations**: Since C++11, you can provide a default implementation for a pure virtual function, but the function still makes the class abstract.

8. **Interface vs Abstract Class**: An interface typically has only pure virtual functions and no data members, while an abstract class can have both.

9. **Multiple inheritance with interfaces**: C++ allows multiple inheritance from multiple abstract interface classes.

10. **Virtual function table concept**: Understand that pure virtual functions use the vtable mechanism for runtime polymorphism.
