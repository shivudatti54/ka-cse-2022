# **Virtual Functions and Polymorphism: Virtual Functions, The Virtual Attribute is Inherited, Virtual Functions are Hierarchical, Pure Virtual Functions**

## **Introduction to Virtual Functions**

In object-oriented programming (OOP), virtual functions are a key concept that allows for runtime polymorphism. In this study material, we will explore the concept of virtual functions, how the virtual attribute is inherited, how virtual functions are hierarchical, and what pure virtual functions are.

## **What are Virtual Functions?**

A virtual function is a member function that can be overridden by a derived class. It is declared using the `virtual` keyword in the base class. Virtual functions are used to achieve runtime polymorphism, which allows objects of different classes to be treated as objects of a common superclass.

**Key Concepts:**

- A virtual function is a member function that can be overridden by a derived class.
- The `virtual` keyword is used to declare a virtual function.
- A virtual function can be overridden by a derived class.

## **The Virtual Attribute is Inherited**

When a derived class inherits from a base class with a virtual function, it inherits the virtual attribute, allowing it to override the function.

**Example:**

```cpp
class Shape {
public:
    virtual void draw() {
        std::cout << "Drawing a shape." << std::endl;
    }
};

class Circle : public Shape {
public:
    void draw() override {
        std::cout << "Drawing a circle." << std::endl;
    }
};

int main() {
    Shape* shape = new Circle();
    shape->draw();  // Output: Drawing a circle.
    return 0;
}
```

## **Virtual Functions are Hierarchical**

In an object-oriented hierarchy, a derived class can inherit virtual functions from its base classes. These functions can then be overridden by the derived class.

**Example:**

```cpp
class Animal {
public:
    virtual void sound() {
        std::cout << "The animal makes a sound." << std::endl;
    }
};

class Dog : public Animal {
public:
    void sound() override {
        std::cout << "The dog barks." << std::endl;
    }
};

class Cat : public Animal {
public:
    void sound() override {
        std::cout << "The cat meows." << std::endl;
    }
};

int main() {
    Animal* animal = new Dog();
    animal->sound();  // Output: The dog barks.
    return 0;
}
```

## **Pure Virtual Functions**

A pure virtual function is a virtual function that has no implementation in the base class. It is declared using the `= 0` syntax and must be implemented by any derived class.

**Example:**

```cpp
class Shape {
public:
    virtual void draw() = 0;
};

class Circle : public Shape {
public:
    void draw() override {
        std::cout << "Drawing a circle." << std::endl;
    }
};

int main() {
    Shape* shape = new Circle();
    shape->draw();  // Output: Drawing a circle.
    return 0;
}
```

**Key Concepts:**

- A pure virtual function is a virtual function with no implementation in the base class.
- It is declared using the `= 0` syntax.
- It must be implemented by any derived class.
- A class that contains a pure virtual function is an abstract class and cannot be instantiated directly.

By understanding the concept of virtual functions, you can achieve runtime polymorphism in C++ and write more flexible and maintainable code.
