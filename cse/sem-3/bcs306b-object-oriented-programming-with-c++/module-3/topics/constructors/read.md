# Constructors in C++

## Introduction

Constructors are special member functions in C++ that are automatically invoked when an object of a class is created. They play a fundamental role in object-oriented programming by ensuring that objects are properly initialized before they are used. The constructor's name must exactly match the class name, and it does not have any return type, not even void.

In the context of C++ programming, constructors serve as the foundation for proper object initialization and memory management. They are essential for encapsulation as they control how objects obtain their initial state. Without constructors, objects might contain garbage values, leading to undefined behavior and difficult-to-debug errors. The C++ Standard Library and user-defined classes rely heavily on constructors to establish invariants and ensure class integrity.

Understanding constructors is crucial for the university's BCS306B examination as it forms the backbone of object-oriented design patterns and memory management concepts. This module covers various types of constructors, their implementation, and their appropriate use cases in real-world applications.

## Key Concepts

### Default Constructor

A default constructor is a constructor that can be called without any arguments. It is automatically provided by the compiler if no user-defined constructors exist in the class. The default constructor initializes member variables using default initialization rules.

```cpp
class Student {
private:
 int rollNo;
 char name[50];
 float marks;
public:
 // Default constructor
 Student() {
 rollNo = 0;
 marks = 0.0;
 }
};
```

When the compiler generates a default constructor, it performs member-wise initialization. For fundamental types, they remain uninitialized, while for class types with constructors, those constructors are called.

### Parameterized Constructor

Parameterized constructors accept arguments to initialize objects with specific values. They enable the creation of objects with custom initial states and support function overloading.

```cpp
class Rectangle {
private:
 int length;
 int breadth;
public:
 // Parameterized constructor
 Rectangle(int l, int b) {
 length = l;
 breadth = b;
 }

 int area() {
 return length * breadth;
 }
};

// Usage
Rectangle r1(10, 5);
Rectangle r2(20, 10);
```

Parameterized constructors are particularly useful for enforcing invariants by validating input parameters during object creation.

### Copy Constructor

A copy constructor creates a new object as a copy of an existing object. It is invoked when:

- Passing an object by value to a function
- Returning an object by value from a function
- Initializing one object with another of the same type
- Explicitly creating a copy using the copy constructor

```cpp
class Box {
private:
 int width;
 int height;
public:
 Box(int w, int h) : width(w), height(h) {}

 // Copy constructor
 Box(const Box& b) {
 width = b.width;
 height = b.height;
 }
};

Box b1(10, 20);
Box b2(b1); // Copy constructor invoked
Box b3 = b1; // Copy constructor invoked
```

The copy constructor takes a const reference to the source object. If not explicitly defined, the compiler generates a default copy constructor that performs shallow copy (member-wise copy).

### Move Constructor

Introduced in C++11, the move constructor transfers ownership of resources from a temporary object to a new object. It avoids expensive deep copy operations by moving the internal pointer or resource handle.

```cpp
class Buffer {
private:
 int* data;
 int size;
public:
 Buffer(int s) : size(s) {
 data = new int[size];
 }

 // Move constructor
 Buffer(Buffer&& other) noexcept {
 data = other.data;
 size = other.size;
 other.data = nullptr;
 other.size = 0;
 }

 ~Buffer() { delete[] data; }
};
```

The move constructor takes an rvalue reference (&&) and should be marked noexcept to enable optimal performance in standard library containers.

### Constructor Initializer List

Constructor initializer lists provide an efficient way to initialize member variables, especially for:

- Reference members
- const members
- Member objects without default constructors
- Base class initialization

```cpp
class Point {
private:
 int x, y;
public:
 Point(int a, int b) : x(a), y(b) {}
};

class Line {
private:
 Point p1, p2; // Objects without default constructor
public:
 Line(Point a, Point b) : p1(a), p2(b) {}
};
```

The initializer list is more efficient than assignment inside the constructor body because it initializes members directly rather than default-constructing them first and then assigning values.

### Explicit Constructor

The `explicit` keyword prevents implicit conversions and copy initialization. It is particularly useful for single-parameter constructors to avoid unintended type conversions.

```cpp
class Integer {
private:
 int value;
public:
 explicit Integer(int v) : value(v) {}
};

void display(Integer obj) {
 // Function expects Integer object
}

int main() {
 Integer obj(10);
 display(obj); // OK - explicit call

 // display(10); // ERROR - implicit conversion not allowed
 // Integer obj2 = 20; // ERROR - copy initialization not allowed
}
```

### Private Constructor

Private constructors restrict object creation, enabling:

- Singleton design pattern implementation
- Factory method patterns
- Preventing direct instantiation of utility classes

```cpp
class Singleton {
private:
 static Singleton* instance;
 Singleton() {} // Private constructor

public:
 static Singleton* getInstance() {
 if (instance == nullptr) {
 instance = new Singleton();
 }
 return instance;
 }
};

Singleton* Singleton::instance = nullptr;
```

## Examples

### Example 1: Constructor Overloading

```cpp
#include <iostream>
using namespace std;

class Complex {
private:
 int real, imag;
public:
 // Default constructor
 Complex() {
 real = 0;
 imag = 0;
 }

 // Parameterized constructor with one parameter
 Complex(int r) {
 real = r;
 imag = 0;
 }

 // Parameterized constructor with two parameters
 Complex(int r, int i) {
 real = r;
 imag = i;
 }

 void display() {
 cout << real << " + " << imag << "i" << endl;
 }
};

int main() {
 Complex c1; // Calls default constructor
 Complex c2(5); // Calls single-parameter constructor
 Complex c3(3, 4); // Calls two-parameter constructor

 c1.display(); // Output: 0 + 0i
 c2.display(); // Output: 5 + 0i
 c3.display(); // Output: 3 + 4i

 return 0;
}
```

### Example 2: Copy Constructor for Deep Copy

```cpp
#include <iostream>
#include <cstring>
using namespace std;

class String {
private:
 char* str;
 int length;
public:
 String(const char* s) {
 length = strlen(s);
 str = new char[length + 1];
 strcpy(str, s);
 }

 // Deep copy constructor
 String(const String& s) {
 length = s.length;
 str = new char[length + 1];
 strcpy(str, s.str);
 }

 void display() {
 cout << str << endl;
 }

 ~String() {
 delete[] str;
 }
};

int main() {
 String s1("Hello");
 String s2 = s1; // Deep copy

 cout << "s1: ";
 s1.display();
 cout << "s2: ";
 s2.display();

 return 0;
}
```

### Example 3: Constructor Initializer List with const and reference members

```cpp
#include <iostream>
using namespace std;

class Date {
private:
 int day, month, year;
public:
 Date(int d, int m, int y) : day(d), month(m), year(y) {}

 void display() {
 cout << day << "/" << month << "/" << year << endl;
 }
};

class Person {
private:
 const int id; // const member - must be initialized
 string name;
 Date& birthDate; // reference member - must be initialized
public:
 Person(string n, Date& d, int i) : name(n), birthDate(d), id(i) {}

 void display() {
 cout << "ID: " << id << endl;
 cout << "Name: " << name << endl;
 cout << "Birth Date: ";
 birthDate.display();
 }
};

int main() {
 Date d(15, 8, 2002);
 Person p("John", d, 101);

 p.display();

 return 0;
}
```

## Exam Tips

1. **Remember Constructor Characteristics**: Constructors have the same name as the class, no return type (not even void), and are automatically called when objects are created.

2. **Copy Constructor Invocation**: Be able to identify all four scenarios where copy constructor is invoked: passing by value, returning by value, initialization, and explicit copying.

3. **Shallow vs Deep Copy**: The default copy constructor performs shallow copy (copies address). For classes with pointer members, implement deep copy to avoid dangling pointers and memory leaks.

4. **Constructor Initializer List Order**: Although members are initialized in the order they are declared in the class, not the order in the initializer list. Always match the declaration order to avoid confusion.

5. **explicit Keyword Usage**: Use `explicit` for single-parameter constructors to prevent unintended implicit conversions, especially for classes that represent fundamental types.

6. **Virtual Constructors**: Remember that constructors cannot be virtual in C++. Use factory method pattern if polymorphic object creation is needed.

7. **Default Arguments**: Parameterized constructors can use default arguments to serve as both parameterized and default constructors, but be careful about ambiguity.

8. **Destructor Relationship**: If a class has a custom copy constructor, it likely needs a custom destructor as well (Rule of Three in pre-C++11).

9. **Move Semantics**: In C++11 and later, understand when move constructor is called (rvalue references, std::move) and its efficiency benefits over copy constructor.

10. **Constructor Execution Order**: For inheritance, base class constructors execute before derived class constructors. Member objects are constructed in the order of their declaration.
