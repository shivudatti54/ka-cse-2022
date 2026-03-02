# Virtual Functions in C++

## Introduction

Virtual functions constitute one of the most powerful features of C++ that enables runtime polymorphism, a cornerstone of object-oriented programming. When working with inheritance hierarchies, virtual functions allow the program to determine which function to call at runtime based on the actual object type, rather than the pointer or reference type. This dynamic binding mechanism is essential for building flexible and extensible software systems.

In C++, by default, function calls are resolved at compile-time using static binding. However, when a function is declared as virtual in a base class and overridden in a derived class, the compiler sets up a mechanism to resolve the function call at runtime. This runtime polymorphism is crucial for implementing design patterns such as Strategy, Template Method, and Factory Method. Virtual functions enable developers to write code that works with base class pointers or references while actually executing the appropriate derived class implementations, making the code more generic, reusable, and maintainable.

Understanding virtual functions is essential for CSE students as it forms the foundation for advanced C++ programming and is frequently tested in university examinations. This topic also prepares students for understanding interfaces, abstract classes, and various design patterns used in real-world software development.

## Key Concepts

### Virtual Functions

A virtual function is a member function of a base class that is declared using the `virtual` keyword and is intended to be overridden by derived classes. When a virtual function is called through a pointer or reference to the base class, the program determines which version of the function to execute based on the actual object type at runtime, not the pointer type.

The syntax for declaring a virtual function is:

```cpp
class Base {
public:
 virtual void display() {
 cout << "Base class display" << endl;
 }
};
```

Any derived class can override this function using the same signature:

```cpp
class Derived : public Base {
public:
 void display() override {
 cout << "Derived class display" << endl;
 }
};
```

The `override` specifier (introduced in C++11) is highly recommended as it helps catch errors at compile-time if the function signature doesn't match any base class virtual function.

### Pure Virtual Functions

A pure virtual function is a virtual function that is declared in the base class but has no implementation. It is declared by assigning `0` to the function declaration. Classes containing pure virtual functions become abstract classes and cannot be instantiated directly.

```cpp
class Shape {
public:
 virtual void draw() = 0; // Pure virtual function
 virtual double area() = 0; // Another pure virtual function
};
```

Pure virtual functions define an interface that derived classes must implement. This is similar to interfaces in Java or abstract methods in other object-oriented languages.

### Abstract Classes

An abstract class is a class that contains at least one pure virtual function. Abstract classes cannot be instantiated, but pointers and references to abstract classes can be created. Abstract classes serve as base classes that define a contract for derived classes.

```cpp
class Animal {
public:
 virtual void sound() = 0;
 virtual void eat() = 0;

 // Can also have non-virtual functions
 void sleep() {
 cout << "Animal is sleeping" << endl;
 }
};

class Dog : public Animal {
public:
 void sound() override {
 cout << "Dog barks" << endl;
 }
 void eat() override {
 cout << "Dog eats meat" << endl;
 }
};
```

### Virtual Destructors

Virtual destructors are essential when dealing with polymorphism. If a base class pointer points to a derived class object and the object is deleted, only the base class destructor is called if the destructor is not virtual, leading to resource leaks.

```cpp
class Base {
public:
 virtual ~Base() {
 cout << "Base destructor" << endl;
 }
};

class Derived : public Base {
public:
 ~Derived() override {
 cout << "Derived destructor" << endl;
 }
};

int main() {
 Base* ptr = new Derived();
 delete ptr; // Both destructors are called
 return 0;
}
```

**Output:**

```
Derived destructor
Base destructor
```

### Virtual Table (vtable) and Virtual Pointer (vptr)

Internally, C++ implements virtual functions using a mechanism called vtable (virtual table). Each class that has virtual functions contains a vtable, which is an array of function pointers. Each object of such a class contains a hidden pointer called vptr that points to the class's vtable.

When a virtual function is called:

1. The program uses the vptr to access the vtable
2. The vtable contains pointers to the most derived class's implementation of the virtual functions
3. The appropriate function is called based on the actual object type

This mechanism incurs a small runtime overhead compared to non-virtual function calls, but provides the flexibility of runtime polymorphism.

### Virtual Function Rules

1. Virtual functions cannot be static members of a class
2. Virtual functions can be friend functions of another class
3. A virtual function in the base class must be defined unless it is declared pure virtual
4. Constructors cannot be virtual
5. Destructors can and should be virtual in polymorphic base classes
6. The return type of an overriding virtual function must be covariant in C++11 and later

## Examples

### Example 1: Basic Virtual Function Implementation

```cpp
#include <iostream>
using namespace std;

class Animal {
public:
 virtual void speak() {
 cout << "Animal speaks" << endl;
 }

 virtual ~Animal() {
 cout << "Animal destructor" << endl;
 }
};

class Dog : public Animal {
public:
 void speak() override {
 cout << "Dog barks: Woof! Woof!" << endl;
 }

 ~Dog() {
 cout << "Dog destructor" << endl;
 }
};

class Cat : public Animal {
public:
 void speak() override {
 cout << "Cat meows: Meow! Meow!" << endl;
 }

 ~Cat() {
 cout << "Cat destructor" << endl;
 }
};

int main() {
 Animal* animals[3];
 animals[0] = new Animal();
 animals[1] = new Dog();
 animals[2] = new Cat();

 for (int i = 0; i < 3; i++) {
 animals[i]->speak(); // Runtime polymorphism
 }

 for (int i = 0; i < 3; i++) {
 delete animals[i];
 }

 return 0;
}
```

**Output:**

```
Animal speaks
Dog barks: Woof! Woof!
Cat meows: Meow! Meow!
Animal destructor
Dog destructor
Animal destructor
Cat destructor
Animal destructor
```

### Example 2: Pure Virtual Function and Abstract Class

```cpp
#include <iostream>
using namespace std;

class Shape {
protected:
 string color;
public:
 Shape(string c = "white") : color(c) {}

 // Pure virtual function
 virtual double area() = 0;

 // Pure virtual function
 virtual void draw() = 0;

 void setColor(string c) {
 color = c;
 }

 void showColor() {
 cout << "Color: " << color << endl;
 }

 virtual ~Shape() {}
};

class Circle : public Shape {
private:
 double radius;
public:
 Circle(double r, string c = "red") : Shape(c), radius(r) {}

 double area() override {
 return 3.14159 * radius * radius;
 }

 void draw() override {
 cout << "Drawing a circle with radius " << radius << endl;
 }
};

class Rectangle : public Shape {
private:
 double length, width;
public:
 Rectangle(double l, double w, string c = "blue") : Shape(c), length(l), width(w) {}

 double area() override {
 return length * width;
 }

 void draw() override {
 cout << "Drawing a rectangle of " << length << " x " << width << endl;
 }
};

int main() {
 // Shape s; // ERROR: Cannot instantiate abstract class

 Shape* shapes[2];
 shapes[0] = new Circle(5.0);
 shapes[1] = new Rectangle(4.0, 6.0);

 for (int i = 0; i < 2; i++) {
 shapes[i]->draw();
 cout << "Area: " << shapes[i]->area() << endl;
 shapes[i]->showColor();
 cout << endl;
 }

 delete shapes[0];
 delete shapes[1];

 return 0;
}
```

**Output:**

```
Drawing a circle with radius 5
Area: 78.5397
Color: red

Drawing a rectangle of 4 x 6
Area: 24
Color: blue
```

### Example 3: Virtual Destructor Demonstration

```cpp
#include <iostream>
using namespace std;

class Base {
private:
 int* data;
public:
 Base() {
 data = new int(100);
 cout << "Base constructor: Allocated memory" << endl;
 }

 virtual ~Base() {
 cout << "Base destructor: Cleaning up" << endl;
 delete data;
 }

 virtual void show() {
 cout << "Base show()" << endl;
 }
};

class Derived : public Base {
private:
 int* moreData;
public:
 Derived() {
 moreData = new int(200);
 cout << "Derived constructor: Allocated more memory" << endl;
 }

 ~Derived() override {
 cout << "Derived destructor: Cleaning up" << endl;
 delete moreData;
 }

 void show() override {
 cout << "Derived show()" << endl;
 }
};

int main() {
 cout << "=== Using Base pointer to Derived object ===" << endl;
 Base* ptr = new Derived();
 ptr->show();
 delete ptr;

 cout << "\n=== Using Derived object directly ===" << endl;
 Derived d;
 d.show();

 return 0;
}
```

**Output:**

```
=== Using Base pointer to Derived object ===
Base constructor: Allocated memory
Derived constructor: Allocated more memory
Derived show()
Derived destructor: Cleaning up
Base destructor: Cleaning up

=== Using Base object directly ===
Base constructor: Allocated memory
Derived constructor: Allocated more memory
Derived show()
Derived destructor: Cleaning up
Base destructor: Cleaning up
```

## Exam Tips

1. **Remember the virtual keyword**: A function must be declared as virtual in the base class to enable runtime polymorphism. Without the virtual keyword, static binding occurs even if the derived class overrides the function.

2. **Pure virtual functions make abstract classes**: A class with at least one pure virtual function (= 0) becomes abstract and cannot be instantiated. This is a common exam question.

3. **Always use virtual destructors in polymorphic classes**: When a class contains virtual functions, always make the destructor virtual to ensure proper cleanup of derived class objects through base class pointers.

4. **The override specifier**: Use the C++11 `override` specifier when overriding virtual functions to catch signature mismatches at compile-time. This prevents subtle bugs.

5. **Virtual functions and constructors**: Constructors cannot be virtual. However, destructors should be virtual in polymorphic base classes.

6. **Runtime vs Compile-time**: Virtual functions provide runtime polymorphism (dynamic binding), while function overloading provides compile-time polymorphism (static binding).

7. **Abstract classes cannot be instantiated**: Remember that abstract classes can have constructors (for derived classes to call) but cannot create objects of the abstract class type directly.

8. **Default arguments and virtual functions**: Virtual functions use static binding for default arguments. The default argument value from the base class declaration is used, not from the derived class override.
