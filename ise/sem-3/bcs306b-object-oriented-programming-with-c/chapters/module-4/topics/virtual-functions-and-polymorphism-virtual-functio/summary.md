# **Virtual Functions and Polymorphism: Quick Revision Notes**

### Overview

---

- Virtual functions and polymorphism are key concepts in Object-Oriented Programming (OOP) with C++.
- Virtual functions allow objects of different classes to be treated as if they were of the same class, enabling polymorphism.

### Key Points

---

#### Virtual Functions

- A virtual function is declared in a base class using the `virtual` keyword.
- A virtual function is a member function that can be overridden by a derived class.
- A virtual function is resolved at runtime, based on the actual object being referred to.

#### The Virtual Attribute is Inherited

- The `virtual` attribute is inherited by derived classes from their base classes.
- This allows derived classes to override virtual functions of their base classes.

#### Virtual Functions are Hierarchical

- Virtual functions can be used to create a hierarchy of related classes.
- Each class in the hierarchy can override the virtual function with its own implementation.

#### Pure Virtual Functions

- A pure virtual function is declared in a base class using the `= 0` syntax.
- A pure virtual function must be overridden by any derived classes.
- A class with a pure virtual function is considered abstract and cannot be instantiated directly.

### Important Formulas, Definitions, and Theorems

---

- **Polymorphism**: The ability of an object to take on multiple forms, depending on the context in which it is used.
- **Virtual Dispatch**: The process of resolving a virtual function call at runtime, based on the actual object being referred to.
- **Run-Time Polymorphism**: The ability of an object to behave differently depending on the context in which it is used, at runtime.

### Example

---

```cpp
class Shape {
public:
    virtual void draw() = 0; // Pure Virtual Function
};

class Circle : public Shape {
public:
    void draw() {
        std::cout << "Drawing a circle." << std::endl;
    }
};

int main() {
    Shape* shape = new Circle();
    shape->draw(); // Outputs: Drawing a circle.
    return 0;
}
```

In this example, the `Shape` class has a pure virtual function `draw()`, which is overridden by the `Circle` class. The `Shape` pointer is used to call the `draw()` function, which is resolved at runtime based on the actual object being referred to.
