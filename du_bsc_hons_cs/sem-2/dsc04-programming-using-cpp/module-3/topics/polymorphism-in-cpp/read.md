# Polymorphism in C++

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction to Polymorphism

### 1.1 What is Polymorphism?

The word **polymorphism** is derived from Greek words: *poly* (many) and *morphos* (forms). In programming, polymorphism refers to the ability of objects to take on many forms. More specifically, it allows the same interface to be used for different underlying data types or forms. This is one of the core pillars of Object-Oriented Programming (OOP), alongside encapsulation, inheritance, and abstraction.

### 1.2 Real-World Relevance

Polymorphism is everywhere in the real world. Consider a **smartphone**: the same "touch" interface works for making calls, taking photos, browsing the internet, and playing games. The action (touch) remains the same, but the response varies based on the context. Similarly, in software development:

- **GUI frameworks** use polymorphism to handle different UI elements (buttons, text boxes, menus) through a common interface
- **Payment processing systems** use a single `processPayment()` method that behaves differently for credit cards, PayPal, UPI, etc.
- **Shape drawing applications** use a common `draw()` method that behaves differently for circles, rectangles, and triangles
- **Game development** employs polymorphism for handling different enemy types, player characters, and game objects

### 1.3 Types of Polymorphism in C++

C++ supports two major types of polymorphism:

| Type | Also Known As | When Resolved | Implementation |
|------|---------------|---------------|----------------|
| Compile-time Polymorphism | Static Binding | At compile time | Function overloading, Operator overloading |
| Runtime Polymorphism | Dynamic Binding | At runtime | Virtual functions, Inheritance |

---

## 2. Compile-Time Polymorphism (Static Binding)

Compile-time polymorphism is achieved when the compiler determines which function to call during compilation. This is also called **early binding**.

### 2.1 Function Overloading

Function overloading allows multiple functions with the **same name** but **different parameters** within the same scope.

```cpp
#include <iostream>
using namespace std;

// Function overloading examples
class Calculator {
public:
    // Overloaded functions with different parameter types
    int add(int a, int b) {
        return a + b;
    }
    
    double add(double a, double b) {
        return a + b;
    }
    
    int add(int a, int b, int c) {
        return a + b + c;
    }
    
    string add(string a, string b) {
        return a + b;
    }
};

int main() {
    Calculator calc;
    cout << calc.add(5, 3) << endl;          // Output: 8
    cout << calc.add(2.5, 3.7) << endl;      // Output: 6.2
    cout << calc.add(1, 2, 3) << endl;       // Output: 6
    cout << calc.add("Hello, ", "World!") << endl; // Output: Hello, World!
    return 0;
}
```

**Key Points:**
- Function overloading is resolved based on the number, type, or order of arguments
- Return type alone is **not sufficient** for function overloading
- It improves code readability by using descriptive function names for similar operations

### 2.2 Operator Overloading

C++ allows operators to be overloaded to work with user-defined data types.

```cpp
#include <iostream>
using namespace std;

class Complex {
private:
    int real;
    int imag;
    
public:
    Complex(int r = 0, int i = 0) : real(r), imag(i) {}
    
    // Operator overloading for addition
    Complex operator + (const Complex& obj) {
        Complex temp;
        temp.real = real + obj.real;
        temp.imag = imag + obj.imag;
        return temp;
    }
    
    void display() {
        cout << real << " + " << imag << "i" << endl;
    }
};

int main() {
    Complex c1(3, 4), c2(1, 2);
    Complex c3 = c1 + c2;  // Uses overloaded + operator
    c3.display();          // Output: 4 + 6i
    return 0;
}
```

**Commonly Overloadable Operators:** +, -, *, /, ==, !=, <<, >>, [], ()

**Operators That Cannot Be Overloaded:** :: (scope resolution), . (member access), .* (pointer-to-member), ? : (ternary)

---

## 3. Runtime Polymorphism (Dynamic Binding)

Runtime polymorphism is achieved through **virtual functions** and inheritance. The decision about which function to call is made at runtime based on the actual object type (not the pointer/reference type).

### 3.1 Virtual Functions

A **virtual function** is a member function in a base class that you expect to override in derived classes. The key feature is that the function to be called is determined at runtime based on the actual object type.

```cpp
#include <iostream>
using namespace std;

// Base class
class Animal {
public:
    // Virtual function
    virtual void speak() {
        cout << "Animal speaks" << endl;
    }
    
    // Virtual destructor (important for proper cleanup)
    virtual ~Animal() {
        cout << "Animal destructor called" << endl;
    }
};

// Derived class 1
class Dog : public Animal {
public:
    void speak() override {  // Override keyword (C++11)
        cout << "Dog barks: Woof! Woof!" << endl;
    }
    
    ~Dog() {
        cout << "Dog destructor called" << endl;
    }
};

// Derived class 2
class Cat : public Animal {
public:
    void speak() override {
        cout << "Cat meows: Meow! Meow!" << endl;
    }
    
    ~Cat() {
        cout << "Cat destructor called" << endl;
    }
};

int main() {
    // Base pointer to derived objects
    Animal* ptr;
    
    Dog d;
    Cat c;
    
    ptr = &d;
    ptr->speak();  // Calls Dog's speak() - Runtime polymorphism
    
    ptr = &c;
    ptr->speak();  // Calls Cat's speak() - Runtime polymorphism
    
    return 0;
}
```

**Output:**
```
Dog barks: Woof! Woof!
Cat meows: Meow! Meow!
Dog destructor called
Animal destructor called
Cat destructor called
Animal destructor called
```

### 3.2 Pure Virtual Functions and Abstract Classes

A **pure virtual function** is a virtual function that has no implementation in the base class. It is declared by assigning `0` to the function declaration.

```cpp
#include <iostream>
using namespace std;

// Abstract class (cannot be instantiated)
class Shape {
public:
    // Pure virtual function
    virtual void draw() = 0;
    
    // Virtual function with default implementation
    virtual void description() {
        cout << "This is a shape" << endl;
    }
    
    // Virtual destructor (necessary for proper cleanup)
    virtual ~Shape() {}
};

// Concrete class 1
class Circle : public Shape {
public:
    void draw() override {
        cout << "Drawing a Circle" << endl;
    }
};

// Concrete class 2
class Rectangle : public Shape {
public:
    void draw() override {
        cout << "Drawing a Rectangle" << endl;
    }
};

int main() {
    // Shape s;  // ERROR: Cannot instantiate abstract class
    
    Circle c;
    Rectangle r;
    
    Shape* shapes[] = {&c, &r};
    
    for (int i = 0; i < 2; i++) {
        shapes[i]->draw();
        shapes[i]->description();
    }
    
    return 0;
}
```

**Key Points:**
- A class containing at least one pure virtual function is called an **abstract class**
- Abstract classes **cannot be instantiated** (cannot create objects of that type)
- Derived classes **must override** all pure virtual functions or they become abstract too
- Abstract classes are used to define interfaces and enforce contracts

---

## 4. The vtable and vptr: Under the Hood

Understanding how polymorphism works internally helps in debugging and writing efficient code.

### 4.1 How Virtual Functions Work

When a class contains at least one virtual function, the compiler creates a **vtable** (virtual table) for that class. The vtable is an array of function pointers. Each object of that class contains a hidden **vptr** (virtual table pointer) that points to the class's vtable.

```
Memory Layout for an Object with Virtual Functions:
┌─────────────────────────────────┐
│         vptr (hidden)          │ ───► Points to vtable
├─────────────────────────────────┤
│     Member Variables           │
└─────────────────────────────────┘

vtable for Animal class:
┌─────────────────────────────────┐
│  Index 0: Animal::speak()       │
│  Index 1: Animal::~Animal()     │
└─────────────────────────────────┘

vtable for Dog class (after override):
┌─────────────────────────────────┐
│  Index 0: Dog::speak()         │  ◄─── Overridden!
│  Index 1: Dog::~Dog()          │  ◄─── Overridden!
└─────────────────────────────────┘
```

### 4.2 Runtime Resolution Process

1. When a virtual function is called through a base class pointer
2. The pointer's vptr is accessed
3. The vtable is consulted to find the correct function address
4. The function is called through that address

**Performance Implication:** Virtual function calls have a small runtime overhead compared to regular function calls due to the indirection through vtable.

---

## 5. Virtual Destructors

Virtual destructors are crucial for proper resource cleanup when dealing with polymorphism.

### 5.1 The Problem Without Virtual Destructors

```cpp
#include <iostream>
using namespace std;

class Base {
public:
    Base() {
        cout << "Base constructor" << endl;
    }
    
    // Non-virtual destructor
    ~Base() {
        cout << "Base destructor" << endl;
    }
};

class Derived : public Base {
public:
    Derived() {
        cout << "Derived constructor" << endl;
        data = new int[100];  // Dynamic allocation
    }
    
    ~Derived() {
        cout << "Derived destructor" << endl;
        delete[] data;  // This will NOT be called if base destructor is not virtual!
    }
    
private:
    int* data;
};

int main() {
    Base* ptr = new Derived();
    delete ptr;  // Only Base destructor called - MEMORY LEAK!
    return 0;
}
```

**Output (INCORRECT BEHAVIOR):**
```
Base constructor
Derived constructor
Base destructor
```

### 5.2 The Solution: Virtual Destructors

```cpp
#include <iostream>
using namespace std;

class Base {
public:
    Base() {
        cout << "Base constructor" << endl;
    }
    
    // Virtual destructor - ALWAYS use this in polymorphic base classes
    virtual ~Base() {
        cout << "Base destructor" << endl;
    }
};

class Derived : public Base {
public:
    Derived() {
        cout << "Derived constructor" << endl;
        data = new int[100];
    }
    
    ~Derived() {
        cout << "Derived destructor" << endl;
        delete[] data;
    }
    
private:
    int* data;
};

int main() {
    Base* ptr = new Derived();
    delete ptr;  // Now calls both destructors in correct order
    return 0;
}
```

**Output (CORRECT BEHAVIOR):**
```
Base constructor
Derived constructor
Derived destructor
Base destructor
```

**Rule:** If a class has any virtual functions, **always make the destructor virtual**.

---

## 6. The Slicing Problem

Object slicing occurs when a derived class object is assigned to a base class object, resulting in the loss of derived class-specific information.

### 6.1 Understanding Slicing

```cpp
#include <iostream>
using namespace std;

class Base {
public:
    int baseData;
    virtual void show() {
        cout << "Base::show()" << endl;
    }
};

class Derived : public Base {
public:
    int derivedData;
    void show() override {
        cout << "Derived::show() - " << derivedData << endl;
    }
};

int main() {
    Derived d;
    d.baseData = 10;
    d.derivedData = 20;
    
    // Slicing: Assigning derived object to base object
    Base b = d;  // Slicing happens here!
    
    b.show();    // Calls Base::show()
    
    // The derived part is "sliced off"
    // cout << b.derivedData;  // ERROR: No such member
    
    return 0;
}
```

### 6.2 Avoiding Slicing

**Method 1: Use Pointers or References**

```cpp
#include <iostream>
using namespace std;

class Base {
public:
    int baseData;
    virtual void show() {
        cout << "Base::show()" << endl;
    }
};

class Derived : public Base {
public:
    int derivedData;
    void show() override {
        cout << "Derived::show() - " << derivedData << endl;
    }
};

int main() {
    Derived d;
    d.baseData = 10;
    d.derivedData = 20;
    
    // Using reference - no slicing
    Base& ref = d;
    ref.show();  // Calls Derived::show()
    
    // Using pointer - no slicing
    Base* ptr = &d;
    ptr->show();  // Calls Derived::show()
    
    return 0;
}
```

**Output (both methods):**
```
Derived::show() - 20
Derived::show() - 20
```

---

## 7. The override Keyword (C++11)

The `override` keyword explicitly indicates that a virtual function is intended to override a base class function. It helps prevent subtle bugs.

### 7.1 Without override (Potential Error)

```cpp
class Base {
public:
    virtual void display(int x) {
        cout << "Base::display" << endl;
    }
};

class Derived : public Base {
public:
    // Oops! Different parameter - this is OVERLOADING, not overriding
    void display() {
        cout << "Derived::display" << endl;
    }
};
```

### 7.2 With override (Compiler Checks)

```cpp
class Base {
public:
    virtual void display(int x) {
        cout << "Base::display" << endl;
    }
};

class Derived : public Base {
public:
    // Compiler error: does not override any base class method
    void display(int x) override {
        cout << "Derived::display" << endl;
    }
};
```

**Benefits of using `override`:**
- Catches typos in function signatures
- Ensures the base class function is actually virtual
- Makes code more readable and maintainable

---

## 8. The dynamic_cast Operator

`dynamic_cast` is a runtime-safe type conversion operator used for polymorphic types. It checks if the conversion is valid at runtime.

### 8.1 Syntax and Usage

```cpp
#include <iostream>
using namespace std;

class Base {
public:
    virtual void show() {}  // Must have at least one virtual function
};

class Derived1 : public Base {
public:
    void show() override {
        cout << "Derived1::show()" << endl;
    }
    void derived1Method() {
        cout << "Derived1 specific method" << endl;
    }
};

class Derived2 : public Base {
public:
    void show() override {
        cout << "Derived2::show()" << endl;
    }
    void derived2Method() {
        cout << "Derived2 specific method" << endl;
    }
};

int main() {
    Base* basePtr = new Derived1();
    
    // Attempt to downcast to Derived1
    Derived1* d1 = dynamic_cast<Derived1*>(basePtr);
    if (d1) {
        d1->derived1Method();  // Works!
    }
    
    // Attempt to downcast to Derived2 - will fail (returns nullptr)
    Derived2* d2 = dynamic_cast<Derived2*>(basePtr);
    if (d2) {
        d2->derived2Method();  // This won't execute
    } else {
        cout << "Cannot cast Derived1* to Derived2*" << endl;
    }
    
    delete basePtr;
    return 0;
}
```

### 8.2 dynamic_cast with References

```cpp
#include <iostream>
#include <typeinfo>
using namespace std;

class Base {
public:
    virtual void show() {}
};

class Derived : public Base {
public:
    void show() override {
        cout << "Derived::show()" << endl;
    }
};

int main() {
    Base* basePtr = new Derived();
    
    try {
        Derived& derivedRef = dynamic_cast<Derived&>(*basePtr);
        derivedRef.show();  // Works!
    } catch (bad_cast& e) {
        cout << "bad_cast exception: " << e.what() << endl;
    }
    
    delete basePtr;
    return 0;
}
```

**Note:** `dynamic_cast` only works with polymorphic types (classes with at least one virtual function).

---

## 9. Real-World Use Cases

### 9.1 Payment Processing System

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Abstract base class for payment methods
class Payment {
public:
    virtual bool processPayment(double amount) = 0;
    virtual string getPaymentType() = 0;
    virtual ~Payment() {}
};

// Credit Card Payment
class CreditCardPayment : public Payment {
private:
    string cardNumber;
public:
    CreditCardPayment(string num) : cardNumber(num) {}
    
    bool processPayment(double amount) override {
        cout << "Processing Credit Card payment of $" << amount << endl;
        cout << "Card: " << cardNumber << endl;
        return true;
    }
    
    string getPaymentType() override {
        return "Credit Card";
    }
};

// PayPal Payment
class PayPalPayment : public Payment {
private:
    string email;
public:
    PayPalPayment(string e) : email(e) {}
    
    bool processPayment(double amount) override {
        cout << "Processing PayPal payment of $" << amount << endl;
        cout << "Email: " << email << endl;
        return true;
    }
    
    string getPaymentType() override {
        return "PayPal";
    }
};

// UPI Payment
class UPIPayment : public Payment {
private:
    string upiId;
public:
    UPIPayment(string id) : upiId(id) {}
    
    bool processPayment(double amount) override {
        cout << "Processing UPI payment of $" << amount << endl;
        cout << "UPI ID: " << upiId << endl;
        return true;
    }
    
    string getPaymentType() override {
        return "UPI";
    }
};

int main() {
    vector<Payment*> paymentMethods;
    
    paymentMethods.push_back(new CreditCardPayment("4532-XXXX-XXXX-1234"));
    paymentMethods.push_back(new PayPalPayment("user@paypal.com"));
    paymentMethods.push_back(new UPIPayment("user@upi"));
    
    double totalAmount = 1500.00;
    
    for (Payment* p : paymentMethods) {
        cout << "Payment Type: " << p->getPaymentType() << endl;
        p->processPayment(totalAmount);
        cout << "-------------------" << endl;
    }
    
    // Clean up
    for (Payment* p : paymentMethods) {
        delete p;
    }
    
    return 0;
}
```

### 9.2 Shape Drawing Application

```cpp
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

const double PI = 3.14159;

// Abstract base class
class Shape {
public:
    virtual double area() const = 0;
    virtual double perimeter() const = 0;
    virtual void draw() const = 0;
    virtual ~Shape() {}
};

class Circle : public Shape {
private:
    double radius;
public:
    Circle(double r) : radius(r) {}
    
    double area() const override {
        return PI * radius * radius;
    }
    
    double perimeter() const override {
        return 2 * PI * radius;
    }
    
    void draw() const override {
        cout << "Drawing Circle with radius " << radius << endl;
    }
};

class Rectangle : public Shape {
private:
    double length, width;
public:
    Rectangle(double l, double w) : length(l), width(w) {}
    
    double area() const override {
        return length * width;
    }
    
    double perimeter() const override {
        return 2 * (length + width);
    }
    
    void draw() const override {
        cout << "Drawing Rectangle " << length << "x" << width << endl;
    }
};

class Triangle : public Shape {
private:
    double a, b, c;
public:
    Triangle(double side1, double side2, double side3) : a(side1), b(side2), c(side3) {}
    
    double area() const override {
        // Heron's formula
        double s = (a + b + c) / 2;
        return sqrt(s * (s - a) * (s - b) * (s - c));
    }
    
    double perimeter() const override {
        return a + b + c;
    }
    
    void draw() const override {
        cout << "Drawing Triangle with sides " << a << ", " << b << ", " << c << endl;
    }
};

int main() {
    vector<Shape*> shapes = {
        new Circle(5.0),
        new Rectangle(4.0, 6.0),
        new Triangle(3.0, 4.0, 5.0)
    };
    
    cout << "=== Shape Information ===" << endl;
    for (const Shape* s : shapes) {
        s->draw();
        cout << "  Area: " << s->area() << endl;
        cout << "  Perimeter: " << s->perimeter() << endl;
        cout << endl;
    }
    
    // Clean up
    for (Shape* s : shapes) {
        delete s;
    }
    
    return 0;
}
```

---

## 10. Key Takeaways

1. **Polymorphism** enables a single interface to represent different underlying forms (data types or behaviors)

2. **Compile-time Polymorphism** (Static Binding):
   - Achieved through function overloading and operator overloading
   - Resolved by the compiler at compile time
   - No runtime overhead

3. **Runtime Polymorphism** (Dynamic Binding):
   - Achieved through virtual functions and inheritance
   - Resolved at runtime using vtable/vptr mechanism
   - Requires at least one virtual function in the class

4. **Virtual Functions** allow derived classes to override base class methods, enabling runtime polymorphic behavior

5. **Pure Virtual Functions** (= 0) make a class abstract—useful for defining interfaces and enforcing contracts

6. **Virtual Destructors** are essential in polymorphic base classes to ensure proper cleanup of derived class resources

7. **Object Slicing** occurs when a derived object is assigned to a base object by value; avoid using pointers/references

8. **The override keyword** (C++11) helps catch errors when overriding virtual functions

9. **dynamic_cast** provides safe runtime type checking for polymorphic types

10. **Performance Consideration**: Virtual functions have slight overhead due to vtable lookup; use judiciously

---

## 11. Multiple Choice Questions

### Easy Level

1. What is polymorphism?
   - A) Creating multiple objects of the same class
   - B) The ability of objects to take many forms
   - C) Hiding data within a class
   D) Inheriting from multiple classes
   - **Answer: B**

2. Which keyword is used to define a virtual function in C++?
   - A) abstract
   - B) virtual
   - C) override
   - D) static
   - **Answer: B**

3. What is required for runtime polymorphism?
   - A) Function overloading
   - B) Operator overloading
   - C) Virtual functions
   - D) Templates
   - **Answer: C**

### Medium Level

4. What is a pure virtual function?
   - A) A function that cannot be overridden
   - B) A virtual function with default implementation
   - C) A virtual function with no implementation (= 0)
   - D) A static virtual function
   - **Answer: C**

5. What is the slicing problem?
   - A) Memory being freed incorrectly
   - B) Loss of derived class information when assigned to base object
   - C) Deleting a virtual object twice
   - D) Compiling errors in virtual functions
   - **Answer: B**

6. What does vtable contain?
   - A) Object data members
   - B) Virtual function pointers
   - C) Constructor addresses
   - D) Static members
   - **Answer: B**

### Hard Level

7. What is the output of the following code?

```cpp
#include <iostream>
using namespace std;

class A {
public:
    virtual void show() { cout << "A::show" << endl; }
};

class B : public A {
public:
    void show() override { cout << "B::show" << endl; }
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
   - C) Compilation error
   - D) Runtime error
   - **Answer: B**

8. Why should destructors in polymorphic classes be virtual?
   - A) To allow early binding
   - B) To ensure proper cleanup of derived class resources
   - C) To increase performance
   - D) To prevent memory leaks only in base class
   - **Answer: B**

9. Which cast operator is used for safe downcasting in polymorphic types?
   - A) static_cast
   - B) reinterpret_cast
   - C) const_cast
   - D) dynamic_cast
   - **Answer: D**

10. What happens when you try to instantiate an abstract class?
    - A) Object is created with default values
    - B) Compilation error occurs
    - C) Runtime error occurs
    - D) It behaves like a normal class
    - **Answer: B**

---

## 12. Flashcards

### Flashcard 1
**Q: What is Polymorphism in C++?**  
**A:** The ability of objects to take on many forms, allowing the same interface to be used for different underlying data types or behaviors.

---

### Flashcard 2
**Q: What is the difference between compile-time and runtime polymorphism?**  
**A:** Compile-time polymorphism (static binding) is resolved at compile time through function/operator overloading. Runtime polymorphism (dynamic binding) is resolved at runtime through virtual functions and inheritance.

---

### Flashcard 3
**Q: What is a virtual function?**  
**A:** A member function in a base class declared with the `virtual` keyword that can be overridden in derived classes, enabling runtime polymorphic behavior.

---

### Flashcard 4
**Q: What is a pure virtual function?**  
**A:** A virtual function with no implementation, declared as `virtual void func() = 0;`. It makes the class abstract and must be overridden by derived classes.

---

### Flashcard 5
**Q: What is the slicing problem?**  
**A:** When a derived class object is assigned to a base class object by value, the derived portion is "sliced off," losing all derived-specific data and behaviors.

---

### Flashcard 6
**Q: Why are virtual destructors important?**  
**A:** Virtual destructors ensure that when a derived class object is deleted through a base class pointer, the derived class destructor is called first, followed by the base class destructor, properly cleaning up all resources.

---

### Flashcard 7
**Q: What is the purpose of the `override` keyword?**  
**A:** The `override` keyword (C++11) explicitly indicates that a function is intended to override a base class virtual function, allowing the compiler to catch errors if the override doesn't actually override anything.

---

### Flashcard 8
**Q: What is `dynamic_cast` used for?**  
**A:** `dynamic_cast` is a runtime-safe type conversion operator for polymorphic types that checks if the conversion is valid at runtime, returning nullptr (for pointers) or throwing `bad_cast` (for references) if unsuccessful.

---

### Flashcard 9
**Q: What is a vtable?**  
**A:** A vtable (virtual table) is a lookup table created by the compiler for each class with virtual functions, containing function pointers to the most-derived implementations of virtual functions.

---

### Flashcard 10
**Q: What is an abstract class?**  
**A:** An abstract class is a class that contains at least one pure virtual function. It cannot be instantiated and is used to define interfaces that derived classes must implement.

---

## References and Further Reading

1. **Textbook:** "The Complete Reference C++" by Herbert Schildt
2. **Delhi University Syllabus:** BSc (Hons) Computer Science, NEP 2024 UGCF - Programming Using C++
3. **C++ Standard:** ISO/IEC 14882:2017 (C++17)
4. **Online Resources:** cppreference.com, cplusplus.com

---

*This study material is prepared for BSc (Hons) Computer Science students at Delhi University as part of the NEP 2024 UGCF curriculum.*