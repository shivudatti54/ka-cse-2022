# Abstract Classes and Pure Virtual Functions

## Introduction to Abstract Classes

In object-oriented programming, an **abstract class** is a class that cannot be instantiated on its own. It serves as a blueprint for other classes and is designed to be inherited by derived classes. Abstract classes are used to define common interfaces and behaviors that subclasses must implement.

The key characteristic of an abstract class is that it contains at least one **pure virtual function**. This makes the class incomplete, requiring derived classes to provide implementations for these pure virtual functions before they can be instantiated.

## What are Pure Virtual Functions?

A **pure virtual function** is a virtual function that has no implementation in the base class. It is declared by assigning 0 to the function declaration:

```cpp
virtual returnType functionName(parameters) = 0;
```

The `= 0` syntax indicates that the function is pure virtual, meaning it must be overridden by any concrete (non-abstract) derived class.

## Why Use Abstract Classes?

Abstract classes serve several important purposes in OOP:

1. **Define Common Interface**: They establish a common protocol that all derived classes must follow
2. **Enforce Implementation**: They force derived classes to implement specific behaviors
3. **Prevent Instantiation**: They prevent creating objects of incomplete classes
4. **Support Polymorphism**: They enable runtime polymorphism through base class pointers/references

## Creating Abstract Classes

### Basic Syntax

```cpp
class Shape {  // Abstract base class
public:
    // Pure virtual function
    virtual double area() const = 0;

    // Pure virtual function
    virtual double perimeter() const = 0;

    // Regular virtual function with implementation
    virtual void display() const {
        std::cout << "This is a shape" << std::endl;
    }

    // Regular member function
    void setColor(const std::string& color) {
        this->color = color;
    }

    // Virtual destructor (important!)
    virtual ~Shape() {}

private:
    std::string color;
};
```

### Key Characteristics

- Contains at least one pure virtual function
- Cannot be instantiated: `Shape s;` would cause a compilation error
- Can contain data members, regular member functions, and virtual functions with implementations
- Should always have a virtual destructor

## Implementing Derived Classes

### Concrete Derived Classes

```cpp
class Circle : public Shape {
private:
    double radius;

public:
    Circle(double r) : radius(r) {}

    // Must implement all pure virtual functions
    double area() const override {
        return 3.14159 * radius * radius;
    }

    double perimeter() const override {
        return 2 * 3.14159 * radius;
    }

    // Can override regular virtual functions (optional)
    void display() const override {
        std::cout << "Circle with radius: " << radius << std::endl;
    }
};

class Rectangle : public Shape {
private:
    double width, height;

public:
    Rectangle(double w, double h) : width(w), height(h) {}

    // Must implement pure virtual functions
    double area() const override {
        return width * height;
    }

    double perimeter() const override {
        return 2 * (width + height);
    }
};
```

### Using Abstract Classes Polymorphically

```cpp
int main() {
    // Shape shape; // Error: cannot instantiate abstract class

    Circle circle(5.0);
    Rectangle rectangle(4.0, 6.0);

    // Using objects directly
    std::cout << "Circle area: " << circle.area() << std::endl;
    std::cout << "Rectangle perimeter: " << rectangle.perimeter() << std::endl;

    // Using base class pointers (polymorphism)
    Shape* shapes[2];
    shapes[0] = new Circle(3.0);
    shapes[1] = new Rectangle(2.0, 4.0);

    for (int i = 0; i < 2; i++) {
        std::cout << "Area: " << shapes[i]->area() << std::endl;
        shapes[i]->display(); // Calls appropriate derived class implementation
    }

    // Cleanup
    for (int i = 0; i < 2; i++) {
        delete shapes[i];
    }

    return 0;
}
```

## Interface vs Implementation Inheritance

### Interface Inheritance (Abstract Classes)

```cpp
class Drawable {
public:
    virtual void draw() const = 0; // Interface only
    virtual ~Drawable() {}
};
```

### Implementation Inheritance (Regular Classes)

```cpp
class Base {
public:
    virtual void doSomething() {
        // Default implementation
    }
};
```

### Combined Approach

```cpp
class Animal {
public:
    virtual void makeSound() const = 0; // Pure virtual - interface

    virtual void sleep() const {        // Virtual with implementation
        std::cout << "Zzz..." << std::endl;
    }

    void breathe() const {              // Regular function - implementation
        std::cout << "Breathing..." << std::endl;
    }

    virtual ~Animal() {}
};
```

## Advanced Concepts

### Abstract Classes with Constructors

Abstract classes can have constructors, which are called when derived class objects are created:

```cpp
class Vehicle {
protected:
    int wheels;
    std::string fuelType;

public:
    Vehicle(int w, const std::string& fuel) : wheels(w), fuelType(fuel) {}

    virtual void start() const = 0;
    virtual void stop() const = 0;

    void displaySpecs() const {
        std::cout << "Wheels: " << wheels << ", Fuel: " << fuelType << std::endl;
    }

    virtual ~Vehicle() {}
};

class Car : public Vehicle {
public:
    Car(const std::string& fuel) : Vehicle(4, fuel) {}

    void start() const override {
        std::cout << "Car starting..." << std::endl;
    }

    void stop() const override {
        std::cout << "Car stopping..." << std::endl;
    }
};
```

### Multiple Pure Virtual Functions

Abstract classes can have multiple pure virtual functions:

```cpp
class DatabaseConnection {
public:
    virtual bool connect() = 0;
    virtual bool disconnect() = 0;
    virtual bool executeQuery(const std::string& query) = 0;
    virtual std::vector<std::string> getResults() = 0;
    virtual ~DatabaseConnection() {}
};
```

### Pure Virtual Destructors

A destructor can be made pure virtual, but it must still be implemented:

```cpp
class Base {
public:
    virtual ~Base() = 0; // Pure virtual destructor
};

// Must provide implementation
Base::~Base() {
    // Cleanup code
}

class Derived : public Base {
public:
    ~Derived() override {
        // Derived class cleanup
    }
};
```

## Real-World Examples

### GUI Framework Example

```cpp
class Widget {
public:
    virtual void draw() const = 0;
    virtual void handleEvent(const Event& event) = 0;
    virtual Dimension getSize() const = 0;

    void setPosition(int x, int y) {
        positionX = x;
        positionY = y;
    }

    virtual ~Widget() {}

protected:
    int positionX, positionY;
};

class Button : public Widget {
public:
    void draw() const override {
        // Draw button implementation
    }

    void handleEvent(const Event& event) override {
        // Handle button events
    }

    Dimension getSize() const override {
        return Dimension{100, 30};
    }
};
```

### Payment Processing Example

```cpp
class PaymentProcessor {
public:
    virtual bool processPayment(double amount) = 0;
    virtual bool refundPayment(const std::string& transactionId) = 0;
    virtual std::string getProcessorName() const = 0;

    virtual bool validateCard(const std::string& cardNumber) {
        // Common validation logic
        return cardNumber.length() == 16;
    }

    virtual ~PaymentProcessor() {}
};

class CreditCardProcessor : public PaymentProcessor {
public:
    bool processPayment(double amount) override {
        // Credit card specific processing
        return true;
    }

    bool refundPayment(const std::string& transactionId) override {
        // Credit card specific refund
        return true;
    }

    std::string getProcessorName() const override {
        return "Credit Card Processor";
    }
};
```

## Comparison with Interfaces in Other Languages

| Feature               | C++ Abstract Class                                 | Java Interface            | C# Interface       |
| --------------------- | -------------------------------------------------- | ------------------------- | ------------------ |
| Multiple Inheritance  | Limited (multiple interfaces via abstract classes) | Yes                       | Yes                |
| Method Implementation | Yes                                                | No (until Java 8)         | No                 |
| Fields                | Can have data members                              | Only constants            | No instance fields |
| Constructors          | Yes                                                | No                        | No                 |
| Access Specifiers     | Various levels                                     | Public only               | Public only        |
| Default Methods       | Regular virtual methods                            | Default methods (Java 8+) | No                 |

## Common Patterns and Best Practices

### 1. The Template Method Pattern

```cpp
class DataProcessor {
public:
    // Template method
    void process() {
        loadData();
        transformData();
        saveData();
    }

    virtual ~DataProcessor() {}

protected:
    virtual void loadData() = 0;     // Primitive operation
    virtual void transformData() = 0; // Primitive operation

    void saveData() {                // Concrete operation
        std::cout << "Saving processed data..." << std::endl;
    }
};

class CSVProcessor : public DataProcessor {
protected:
    void loadData() override {
        std::cout << "Loading CSV data..." << std::endl;
    }

    void transformData() override {
        std::cout << "Transforming CSV data..." << std::endl;
    }
};
```

### 2. Factory Method Pattern

```cpp
class Document {
public:
    virtual void open() = 0;
    virtual void save() = 0;
    virtual void close() = 0;
    virtual ~Document() {}
};

class Application {
public:
    virtual Document* createDocument() = 0; // Factory method

    void newDocument() {
        Document* doc = createDocument();
        doc->open();
        // ... use document
        doc->close();
        delete doc;
    }

    virtual ~Application() {}
};

class TextApplication : public Application {
public:
    Document* createDocument() override {
        return new TextDocument();
    }
};
```

## Common Mistakes and Pitfalls

1. **Forgetting to implement pure virtual functions**: Results in derived class also being abstract
2. **Not providing virtual destructor**: Can cause memory leaks
3. **Trying to instantiate abstract class**: Compilation error
4. **Incorrect access specifiers**: Pure virtual functions should typically be public
5. **Not using override keyword**: Makes code less readable and error-prone

## ASCII Diagram: Class Hierarchy

```
         Abstract Base Class
        +-------------------+
        |    Shape          |
        +-------------------+
        | + area() = 0      |
        | + perimeter() = 0 |
        | + display()       |
        +-------------------+
                 ^
                 | implements
                 |
    +------------+------------+
    |                         |
+---+-----+             +-----+---+
| Circle  |             | Rectangle|
+---------+             +----------+
| - radius|             | - width  |
+---------+             | - height |
| + area()|             +----------+
| + perimeter()         | + area()|
| + display()           | + perimeter()
+---------+             +----------+
```

## Exam Tips

1. **Remember the syntax**: `virtual returnType function() = 0;` declares a pure virtual function
2. **Abstract classes cannot be instantiated**: Any attempt will result in a compilation error
3. **Derived classes must implement**: All pure virtual functions, or they remain abstract
4. **Virtual destructors are crucial**: Always declare a virtual destructor in abstract base classes
5. **Polymorphism works**: Base class pointers/references can point to derived class objects
6. **Abstract classes can have implementation**: They're not just interfaces; they can contain data and implemented methods
7. **Watch for access specifiers**: Pure virtual functions are typically public, but can be protected if needed for internal use
