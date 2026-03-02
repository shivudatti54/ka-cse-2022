# Virtual Functions in C++

## Introduction to Virtual Functions

Virtual functions are a fundamental feature of C++ that enables runtime polymorphism, a core concept in object-oriented programming. They allow a program to decide which function to call at runtime rather than compile time, based on the actual type of object being pointed to or referenced.

**Key Concept**: When a base class pointer points to a derived class object, and both classes have a function with the same signature, a virtual function ensures that the derived class's version is called.

## How Virtual Functions Work

Virtual functions are implemented through a mechanism called the **virtual function table (vtable)** and **virtual pointer (vptr)**.

### The vtable and vptr Mechanism

Every class that contains virtual functions has a hidden pointer member called vptr. This vptr points to a table of function pointers called the vtable. Each object of the class contains its own vptr.

```
+----------------+      +-----------------+
|    Base Class  |      |    vtable for   |
|    Object      |      |    Base Class    |
| +------------+ |      | +-------------+ |
| |   vptr     |----->  | | &Base::func | |
| +------------+ |      | +-------------+ |
| | data members| |      +-----------------+
| +------------+ |
+----------------+

+-----------------+     +------------------+
|   Derived Class |     |   vtable for     |
|   Object        |     |   Derived Class  |
| +-------------+ |     | +--------------+ |
| |   vptr      |-----> | | &Derived::func| |
| +-------------+ |     | +--------------+ |
| | data members| |     +------------------+
| +-------------+ |
+-----------------+
```

When a virtual function is called through a base class pointer, the compiler:

1. Follows the vptr to the vtable
2. Looks up the appropriate function pointer in the vtable
3. Calls the function through the pointer

## Declaring and Using Virtual Functions

### Basic Syntax

```cpp
class Base {
public:
    virtual void display() {  // Virtual function declaration
        cout << "Base class display" << endl;
    }
};

class Derived : public Base {
public:
    void display() override {  // Override keyword (C++11)
        cout << "Derived class display" << endl;
    }
};

int main() {
    Base* basePtr;
    Derived derivedObj;

    basePtr = &derivedObj;
    basePtr->display();  // Calls Derived::display() at runtime
    return 0;
}
```

### The override Keyword (C++11)

The `override` keyword helps prevent errors by ensuring you're actually overriding a virtual function from the base class. If the function signature doesn't match any virtual function in the base class, the compiler will generate an error.

## Virtual Destructors

### Why Virtual Destructors Are Essential

When dealing with polymorphism through base class pointers, it's crucial to declare the destructor as virtual to ensure proper cleanup of derived class objects.

```cpp
class Base {
public:
    virtual ~Base() {  // Virtual destructor
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
    delete ptr;  // Calls both Derived and Base destructors
    return 0;
}
```

**Without a virtual destructor**, only the base class destructor would be called, potentially leaving derived class resources undeleted.

## Pure Virtual Functions and Abstract Classes

### Pure Virtual Functions

A pure virtual function is a virtual function that has no implementation in the base class and must be overridden in derived classes.

```cpp
class Shape {
public:
    virtual double area() const = 0;  // Pure virtual function
};

class Circle : public Shape {
private:
    double radius;
public:
    Circle(double r) : radius(r) {}
    double area() const override {
        return 3.14159 * radius * radius;
    }
};
```

### Abstract Classes

A class containing at least one pure virtual function becomes an **abstract class**. You cannot create objects of an abstract class; it serves only as an interface for derived classes.

## Virtual Function Table Implementation Details

### How vtables Are Structured

Each class with virtual functions has its own vtable. The vtable contains:

- Pointers to virtual functions
- Possibly RTTI (Run-Time Type Information) data
- Entries for each virtual function in declaration order

```
Base Class vtable:
+-------------------+
| type_info for Base|
+-------------------+
| &Base::virtualFunc|
+-------------------+
| &Base::virtualFunc2|
+-------------------+

Derived Class vtable:
+---------------------+
| type_info for Derived|
+---------------------+
| &Derived::virtualFunc|
+---------------------+
| &Base::virtualFunc2  |
+---------------------+
```

## Performance Considerations

Virtual functions have some overhead compared to regular function calls:

1. **Indirection cost**: Extra pointer dereferencing
2. **Cache misses**: Vtable lookups may cause cache misses
3. **Inlining limitations**: Virtual functions generally cannot be inlined

However, for most applications, this overhead is negligible compared to the flexibility gained.

## Comparison: Virtual vs Non-Virtual Functions

| Aspect       | Virtual Functions             | Non-Virtual Functions   |
| ------------ | ----------------------------- | ----------------------- |
| Binding Time | Runtime (dynamic)             | Compile-time (static)   |
| Overhead     | Slight (vtable lookup)        | None                    |
| Polymorphism | Supports runtime polymorphism | No runtime polymorphism |
| Inlining     | Generally not possible        | Possible                |
| Memory Usage | Extra vptr per object         | No extra memory         |

## Common Use Cases

1. **Framework design**: Allowing user-defined behavior in frameworks
2. **Plugin architectures**: Enabling runtime extensibility
3. **GUI toolkits**: Handling events polymorphically
4. **Game development**: Different behaviors for game entities

## Best Practices

1. **Use virtual destructors** in base classes intended for polymorphism
2. **Prefer the override keyword** for clarity and error prevention
3. **Consider making base classes abstract** when appropriate
4. **Be mindful of performance** in performance-critical code
5. **Use final keyword** (C++11) to prevent further overriding

## Exam Tips

1. **Remember the vtable mechanism**: Understand how vtables enable runtime polymorphism
2. **Virtual destructors are crucial**: Always mention them when discussing polymorphism with dynamic allocation
3. **Know the difference**: Between early binding (non-virtual) and late binding (virtual)
4. **Abstract classes**: Remember that you cannot instantiate classes with pure virtual functions
5. **Override keyword**: Explain its benefits for code safety and clarity
6. **Performance implications**: Be prepared to discuss the trade-offs of virtual functions
