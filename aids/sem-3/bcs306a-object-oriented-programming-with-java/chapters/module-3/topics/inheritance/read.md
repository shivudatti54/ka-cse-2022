# Types of Inheritance in C++

## Introduction to Inheritance

Inheritance is one of the four fundamental principles of Object-Oriented Programming (OOP), alongside encapsulation, polymorphism, and abstraction. It allows a new class (derived class) to inherit properties and behaviors (data members and member functions) from an existing class (base class). This mechanism promotes code reusability and establishes a natural hierarchical relationship between classes.

The basic syntax for inheritance in C++ is:
```cpp
class DerivedClass : access-specifier BaseClass {
    // members of derived class
};
```

## Access Specifiers in Inheritance

The access specifier (`public`, `protected`, or `private`) in the inheritance declaration determines how the inherited members are accessible in the derived class.

| Base Class Member Access | Inheritance Type | Access in Derived Class |
|--------------------------|------------------|-------------------------|
| private                  | Any              | Not accessible          |
| protected                | public           | protected               |
| protected                | protected        | protected               |
| protected                | private          | private                 |
| public                   | public           | public                  |
| public                   | protected        | protected               |
| public                   | private          | private                 |

## The Five Types of Inheritance

C++ supports five distinct types of inheritance, each serving different design purposes.

### 1. Single Inheritance

Single inheritance is the simplest form where a derived class inherits from only one base class. This creates a straightforward "is-a" relationship.

**Example:**
```cpp
#include <iostream>
using namespace std;

class Vehicle {          // Base class
  public:
    void start() {
        cout << "Vehicle started." << endl;
    }
};

class Car : public Vehicle {  // Derived class
  public:
    void drive() {
        cout << "Car is driving." << endl;
    }
};

int main() {
    Car myCar;
    myCar.start();  // Inherited from Vehicle
    myCar.drive();  // Defined in Car
    return 0;
}
```

**ASCII Diagram:**
```
    Vehicle (Base)
       ↑
       |
      Car (Derived)
```

### 2. Multiple Inheritance

Multiple inheritance allows a derived class to inherit from more than one base class. This enables a derived class to combine features from multiple sources.

**Example:**
```cpp
#include <iostream>
using namespace std;

class Engine {
  public:
    void startEngine() {
        cout << "Engine started." << endl;
    }
};

class MusicSystem {
  public:
    void playMusic() {
        cout << "Music playing." << endl;
    }
};

class Car : public Engine, public MusicSystem {  // Inherits from two base classes
  public:
    void drive() {
        cout << "Car is driving." << endl;
    }
};

int main() {
    Car myCar;
    myCar.startEngine();  // From Engine
    myCar.playMusic();    // From MusicSystem
    myCar.drive();        // From Car
    return 0;
}
```

**ASCII Diagram:**
```
Engine     MusicSystem
    \         /
     \       /
       Car (Derived)
```

### 3. Multilevel Inheritance

In multilevel inheritance, a class is derived from another derived class, creating a chain of inheritance.

**Example:**
```cpp
#include <iostream>
using namespace std;

class Vehicle {
  public:
    Vehicle() { cout << "Vehicle constructor" << endl; }
};

class FourWheeler : public Vehicle {
  public:
    FourWheeler() { cout << "FourWheeler constructor" << endl; }
};

class Car : public FourWheeler {
  public:
    Car() { cout << "Car constructor" << endl; }
};

int main() {
    Car myCar;  // Constructors called in order: Vehicle → FourWheeler → Car
    return 0;
}
```

**ASCII Diagram:**
```
    Vehicle (Base)
       ↑
       |
   FourWheeler (Intermediate Derived)
       ↑
       |
      Car (Derived)
```

### 4. Hierarchical Inheritance

In hierarchical inheritance, multiple derived classes inherit from a single base class. This is useful when modeling categories that share common characteristics.

**Example:**
```cpp
#include <iostream>
using namespace std;

class Shape {                 // Base class
  protected:
    double area;
  public:
    virtual void calculateArea() = 0; // Pure virtual function
    void displayArea() {
        cout << "Area: " << area << endl;
    }
};

class Circle : public Shape { // Derived class 1
  private:
    double radius;
  public:
    Circle(double r) : radius(r) {}
    void calculateArea() override {
        area = 3.14159 * radius * radius;
    }
};

class Rectangle : public Shape { // Derived class 2
  private:
    double length, width;
  public:
    Rectangle(double l, double w) : length(l), width(w) {}
    void calculateArea() override {
        area = length * width;
    }
};

int main() {
    Circle c(5.0);
    c.calculateArea();
    c.displayArea();
    
    Rectangle r(4.0, 6.0);
    r.calculateArea();
    r.displayArea();
    
    return 0;
}
```

**ASCII Diagram:**
```
        Shape (Base)
         /    \
        /      \
   Circle    Rectangle (Derived Classes)
```

### 5. Hybrid Inheritance

Hybrid inheritance is a combination of two or more types of inheritance. The most common form combines multiple and hierarchical inheritance.

**Example:**
```cpp
#include <iostream>
using namespace std;

class Vehicle {
  public:
    Vehicle() { cout << "Vehicle constructor" << endl; }
};

class Engine {
  public:
    Engine() { cout << "Engine constructor" << endl; }
};

class Car : public Vehicle, public Engine { // Multiple inheritance
  public:
    Car() { cout << "Car constructor" << endl; }
};

class SportsCar : public Car { // Multilevel inheritance
  public:
    SportsCar() { cout << "SportsCar constructor" << endl; }
};

int main() {
    SportsCar sc; // Constructors called: Vehicle → Engine → Car → SportsCar
    return 0;
}
```

**ASCII Diagram:**
```
Vehicle   Engine
   \       /
    \     /
      Car (Multiple Inheritance)
        ↑
        |
   SportsCar (Multilevel Inheritance)
```

## Special Inheritance Scenarios

### Virtual Base Classes

Virtual base classes solve the "diamond problem" in multiple inheritance where a derived class inherits from two classes that both inherit from the same base class, preventing duplicate copies of the base class members.

**Example without virtual inheritance (problematic):**
```cpp
class Animal {
  public:
    void breathe() { cout << "Breathing..." << endl; }
};

class LandAnimal : public Animal { };
class WaterAnimal : public Animal { };

class Amphibian : public LandAnimal, public WaterAnimal { }; 
// Amphibian has two copies of Animal members

int main() {
    Amphibian frog;
    // frog.breathe(); // Error: ambiguous call
    frog.LandAnimal::breathe(); // Need to specify which copy
    frog.WaterAnimal::breathe();
}
```

**Example with virtual inheritance (solution):**
```cpp
class Animal {
  public:
    void breathe() { cout << "Breathing..." << endl; }
};

class LandAnimal : virtual public Animal { }; // Virtual inheritance
class WaterAnimal : virtual public Animal { }; // Virtual inheritance

class Amphibian : public LandAnimal, public WaterAnimal { }; 
// Now only one copy of Animal members

int main() {
    Amphibian frog;
    frog.breathe(); // No longer ambiguous
    return 0;
}
```

**ASCII Diagram of Diamond Problem:**
```
        Animal
        /    \
       /      \
LandAnimal  WaterAnimal
       \      /
        \    /
       Amphibian
```

## Constructor Inheritance and Execution Order

Constructors are called in the order of inheritance, from the base class to the most derived class. Destructors are called in reverse order.

**Execution Order Example:**
```cpp
class Base1 {
  public:
    Base1() { cout << "Base1 constructor" << endl; }
    ~Base1() { cout << "Base1 destructor" << endl; }
};

class Base2 {
  public:
    Base2() { cout << "Base2 constructor" << endl; }
    ~Base2() { cout << "Base2 destructor" << endl; }
};

class Derived : public Base1, public Base2 {
  public:
    Derived() { cout << "Derived constructor" << endl; }
    ~Derived() { cout << "Derived destructor" << endl; }
};

int main() {
    Derived obj;
    return 0;
}
// Output:
// Base1 constructor
// Base2 constructor
// Derived constructor
// Derived destructor
// Base2 destructor
// Base1 destructor
```

## Comparison of Inheritance Types

| Type of Inheritance | Description | Use Case | Potential Issues |
|---------------------|-------------|----------|------------------|
| Single | One derived class from one base class | Simple "is-a" relationships | None |
| Multiple | One derived class from multiple base classes | Combining features from different sources | Ambiguity, Diamond problem |
| Multilevel | Derived class from another derived class | Creating specialization hierarchies | Deep hierarchies can become complex |
| Hierarchical | Multiple derived classes from one base class | Creating categories with shared features | None significant |
| Hybrid | Combination of multiple inheritance types | Complex modeling needs | Can combine issues of constituent types |

## Exam Tips

1. **Understand access specifiers**: Remember how public, protected, and private inheritance affect member accessibility in derived classes.

2. **Constructor order**: Constructors are called from base to derived, destructors in reverse order.

3. **Diamond problem**: Know how virtual base classes resolve the ambiguity in multiple inheritance.

4. **Code tracing**: Practice tracing through inheritance examples to predict output, especially with constructors/destructors.

5. **Design questions**: When asked to design a class hierarchy, consider which type of inheritance best models the relationship.

6. **Memory layout**: For advanced questions, understand how objects are laid out in memory with different inheritance types.

7. **Virtual functions**: Remember that inheritance is closely tied to polymorphism through virtual functions (covered in next module).