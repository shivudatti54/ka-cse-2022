# Virtual Functions and Polymorphism: Virtual Functions, The Virtual Attribute is Inherited, Virtual Functions are Hierarchical, Pure Virtual Functions

### Overview

In object-oriented programming (OOP), virtual functions and polymorphism are crucial concepts that enable more flexibility and generic code. A virtual function is a member function of a class that can be overridden by a derived class. This allows for more flexibility in code and makes it easier to add new functionality without modifying existing code. In this module, we will delve into the world of virtual functions and polymorphism, exploring their history, definition, the virtual attribute, hierarchical virtual functions, pure virtual functions, and their applications.

### Historical Context

The concept of virtual functions dates back to the early 1980s, when C++ was first designed by Bjarne Stroustrup at Bell Labs. The first version of C++ (C++ 1.0) did not have virtual functions, but they were introduced in C++ 3 (1988). The introduction of virtual functions revolutionized the way C++ programmers wrote code, enabling more generic and flexible programs.

### Definition and Basics

A virtual function is a member function of a class that can be overridden by a derived class. The virtual function is declared using the `virtual` keyword in the base class and can be overridden by any derived class.

```cpp
// Base class with a virtual function
class Animal {
public:
    virtual void sound() {
        cout << "The animal makes a sound." << endl;
    }
};

// Derived class overriding the virtual function
class Dog : public Animal {
public:
    void sound() override {
        cout << "The dog barks." << endl;
    }
};
```

In the above example, the `sound()` function is a virtual function in the `Animal` class, and it is overridden by the `Dog` class.

### The Virtual Attribute is Inherited

When a derived class inherits from a base class, it automatically inherits the virtual attribute. This means that any virtual functions declared in the base class are also inherited by the derived class.

```cpp
// Base class with a virtual function
class Animal {
public:
    virtual void sound() {
        cout << "The animal makes a sound." << endl;
    }
};

// Derived class inheriting the virtual attribute
class Dog : public Animal {
public:
    void sound() {
        cout << "The dog barks." << endl;
    }
};

int main() {
    Dog myDog;
    myDog.sound();  // Outputs: The dog barks.
    return 0;
}
```

In the above example, the `Dog` class inherits the `sound()` function from the `Animal` class.

### Virtual Functions are Hierarchical

Virtual functions can be used to create hierarchical classes. Each class in the hierarchy can override the virtual function with its own implementation.

```cpp
// Base class with a virtual function
class Animal {
public:
    virtual void sound() {
        cout << "The animal makes a sound." << endl;
    }
};

// Derived class overriding the virtual function
class Dog : public Animal {
public:
    void sound() override {
        cout << "The dog barks." << endl;
    }
};

// Another derived class overriding the virtual function
class Cat : public Dog {
public:
    void sound() override {
        cout << "The cat meows." << endl;
    }
};

int main() {
    Cat myCat;
    myCat.sound();  // Outputs: The cat meows.
    return 0;
}
```

In the above example, the `Cat` class overrides the `sound()` function with its own implementation.

### Pure Virtual Functions

A pure virtual function is a virtual function that has no implementation in the base class and must be implemented by any derived class. Pure virtual functions are declared using the `virtual` keyword followed by `= 0` in the base class.

```cpp
// Base class with a pure virtual function
class Animal {
public:
    virtual void sound() = 0;
};

// Derived class implementing the pure virtual function
class Dog : public Animal {
public:
    void sound() {
        cout << "The dog barks." << endl;
    }
};

int main() {
    Dog myDog;
    myDog.sound();  // Outputs: The dog barks.
    return 0;
}
```

In the above example, the `sound()` function is a pure virtual function in the `Animal` class, and it is implemented by the `Dog` class.

### Applicability and Applications

Virtual functions and polymorphism are widely used in C++ programming. They enable more flexibility in code and make it easier to add new functionality without modifying existing code. Some common applications of virtual functions and polymorphism include:

- **Game Development**: Virtual functions are used to create complex game objects that can be easily extended or modified.
- **Graphical User Interfaces**: Virtual functions are used to create GUI components that can be easily customized or extended.
- **Database Systems**: Virtual functions are used to create database objects that can be easily extended or modified.

### Further Reading

- "The C++ Programming Language" by Bjarne Stroustrup
- "Effective C++" by Scott Meyers
- "C++ Templates: The Complete Guide" by Nicolai Josuttis
- "C++ Polymorphism: A Gentle Introduction" by Aleksey Gurtovoy and David Abrahams

This module has covered the basics of virtual functions and polymorphism in C++. It has provided a detailed explanation of virtual functions, the virtual attribute, hierarchical virtual functions, and pure virtual functions. It has also discussed the applicability and applications of virtual functions and polymorphism, and provided further reading suggestions.
