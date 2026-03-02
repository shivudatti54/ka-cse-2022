# Classes in C++

## Introduction

Classes form the cornerstone of Object-Oriented Programming (OOP) in C++ and represent one of the most significant advances in programming methodology. A class is a user-defined data type that encapsulates data members (attributes) and member functions (methods) into a single unit. Unlike structured programming approaches where data and functions are separate, classes enable the binding of data with the functions that manipulate it, promoting the principle of encapsulation.

The concept of classes in C++ builds upon the foundation of C structures but extends far beyond simple data aggregation. While C structures could only hold data members, C++ classes can contain both data and functions, along with sophisticated access control mechanisms, inheritance, polymorphism, and other OOP features. Understanding classes is essential for any programmer seeking to leverage the full power of C++ for developing modular, maintainable, and scalable software solutions.

In the context of the university's BCS306B course, this module establishes the fundamental building blocks that will be used throughout the subject. The concepts learned here serve as prerequisites for understanding more advanced topics such as inheritance, polymorphism, and template programming. Mastery of classes is critical for success in both theoretical examinations and practical programming assignments.

## Key Concepts

### Class Declaration and Definition

A class in C++ is declared using the `class` keyword followed by the class name and a pair of curly braces containing the class body. The class body contains declarations of data members and member functions, along with access specifiers that control the visibility of these members.

```cpp
class Rectangle {
private:
 int length;
 int breadth;

public:
 // Constructor declaration
 Rectangle(int l = 0, int b = 0);

 // Member function declarations
 int area();
 int perimeter();

 // Setter functions
 void setDimensions(int l, int b);
};
```

The class definition includes the implementation of member functions, which can be defined either inside the class declaration or outside it. When defined inside the class, they are automatically treated as inline functions by the compiler. When defined outside, the scope resolution operator (`::`) must be used to associate the function with the class.

```cpp
// Member function defined outside the class
int Rectangle::area() {
 return length * breadth;
}

int Rectangle::perimeter() {
 return 2 * (length + breadth);
}
```

### Access Specifiers

C++ provides three access specifiers that determine the visibility and accessibility of class members:

**Private (`private:`)**: Members declared as private are accessible only within the class itself and by friend functions. Private members form the internal implementation and are hidden from outside access, supporting encapsulation. By default, all members of a class are private when the `class` keyword is used.

**Public (`public:`)**: Public members are accessible from anywhere in the program where an object of the class is visible. These constitute the interface through which external code interacts with the class. Constructors, destructors, and major member functions are typically declared public.

**Protected (`protected:`)**: Protected members are similar to private members but become accessible in derived classes (classes that inherit from this class). This access specifier is particularly relevant in the context of inheritance, which is covered in subsequent modules.

The general practice is to make data members private (for encapsulation) and member functions public (for providing access to functionality), though there are exceptions based on design requirements.

### Data Members and Member Functions

**Data Members** (also called attributes or properties) are variables declared within the class body. They represent the state or characteristics of objects created from the class. Data members can be of any type, including primitive types, pointers, references, or even other class types.

**Member Functions** (also called methods) are functions declared within the class body. They define the behavior of objects and typically operate on the data members. Member functions have a special pointer called `this` that points to the object invoking the function, allowing them to access the object's members.

```cpp
class BankAccount {
private:
 int accountNumber;
 double balance;
 std::string holderName;

public:
 void deposit(double amount) {
 if (amount > 0) {
 balance += amount;
 }
 }

 void withdraw(double amount) {
 if (amount <= balance) {
 balance -= amount;
 }
 }

 double getBalance() const { // const member function
 return balance;
 }
};
```

Member functions can be declared as `const` using the `const` keyword, indicating that they do not modify any data members of the object. Such functions are called constant member functions and can be called on constant objects.

### Objects

An object is an instance of a class. While a class defines the blueprint or template, objects represent actual entities created based on that blueprint. Each object has its own copy of data members (unless declared as static), but all objects share the same member function code.

```cpp
Rectangle rect1(10, 5); // Object created using parameterized constructor
Rectangle rect2; // Object created using default constructor
Rectangle rect3 = rect1; // Object created using copy constructor
```

Objects can be created in several ways:

- **Stack allocation**: `Rectangle rect;`
- **Dynamic allocation**: `Rectangle* ptr = new Rectangle(10, 5);`

Accessing members of an object uses the dot operator (`.`) for objects and arrow operator (`->`) for pointers to objects.

```cpp
rect1.setDimensions(15, 10);
rect1.area(); // Returns 150
Rectangle* p = &rect1;
p->area(); // Also returns 150
```

### Constructors

Constructors are special member functions that are automatically invoked when an object is created. They have the same name as the class and do not have a return type. Constructors initialize objects and can be overloaded to provide multiple ways of creating objects.

**Default Constructor**: A constructor that can be called with no arguments. If no constructor is defined, the compiler provides a default constructor.

```cpp
class Box {
private:
 int width, height;
public:
 Box() { // Default constructor
 width = height = 0;
 }
};
```

**Parameterized Constructor**: Constructors that accept parameters to initialize objects with specific values.

```cpp
Box(int w, int h) {
 width = w;
 height = h;
}
```

**Copy Constructor**: A constructor that creates an object as a copy of another object. The compiler provides a default copy constructor that performs shallow copy.

```cpp
Box(const Box& b) {
 width = b.width;
 height = b.height;
}
```

**Constructor Initialization List**: A more efficient way to initialize data members, especially for const members and references.

```cpp
class Circle {
private:
 const double PI;
 double radius;
public:
 Circle(double r) : PI(3.14159), radius(r) { }
};
```

### Destructors

Destructors are special member functions that are invoked when an object is destroyed. They have the same name as the class prefixed with a tilde (`~`) and do not have a return type or parameters. Destructors are used to release resources acquired during the object's lifetime, such as dynamically allocated memory or file handles.

```cpp
class DynamicArray {
private:
 int* arr;
 int size;
public:
 DynamicArray(int s) {
 size = s;
 arr = new int[size];
 }

 ~DynamicArray() { // Destructor
 delete[] arr; // Release dynamically allocated memory
 }
};
```

If a class does not define a destructor, the compiler provides a default one. It is crucial to define a destructor when a class manages dynamic memory to prevent memory leaks.

### The this Pointer

The `this` pointer is an implicit pointer available within all non-static member functions. It points to the object for which the member function was called. The `this` pointer is particularly useful for distinguishing between parameter names and data members when they have the same name, and for returning the current object from member functions.

```cpp
class Employee {
private:
 int id;
 std::string name;
public:
 void setData(int id, std::string name) {
 this->id = id; // Using this to differentiate
 this->name = name;
 }

 Employee* getThis() {
 return this; // Returning pointer to current object
 }
};
```

### Static Members

Static data members and member functions belong to the class rather than any specific object. There is only one copy of a static member shared by all objects of the class. Static members are declared using the `static` keyword.

```cpp
class Student {
private:
 std::string name;
 int rollNo;
 static int count; // Shared by all objects

public:
 Student(std::string n) {
 name = n;
 rollNo = ++count;
 }

 static int getCount() { // Static member function
 return count;
 }
};

int Student::count = 0; // Definition outside class
```

Static member functions can only access static data members and other static member functions, as they do not have a `this` pointer.

### Friend Functions and Classes

A friend function is a function that is not a member of a class but has access to its private and protected members. Friend functions are declared within the class using the `friend` keyword.

```cpp
class Calculator {
private:
 int value;
public:
 Calculator(int v = 0) : value(v) { }

 friend int doubleValue(const Calculator& c); // Declaration
};

int doubleValue(const Calculator& c) {
 return c.value * 2; // Accessing private member
}
```

Friend relationships are not transitive, reciprocal, or inherited. They are granted explicitly and provide a controlled way to allow external functions or classes to access private members when necessary.

## Examples

### Example 1: Implementing a Simple Class

**Problem**: Create a class `Complex` to represent complex numbers with real and imaginary parts. Implement functions to add and display complex numbers.

```cpp
#include <iostream>
using namespace std;

class Complex {
private:
 int real;
 int imag;

public:
 // Constructor
 Complex(int r = 0, int i = 0) : real(r), imag(i) { }

 // Function to add complex numbers
 Complex add(Complex c) {
 Complex temp;
 temp.real = real + c.real;
 temp.imag = imag + c.imag;
 return temp;
 }

 // Function to display complex number
 void display() {
 if (imag >= 0)
 cout << real << " + " << imag << "i" << endl;
 else
 cout << real << " - " << (-imag) << "i" << endl;
 }
};

int main() {
 Complex c1(3, 4);
 Complex c2(1, -2);
 Complex c3;

 cout << "First complex number: ";
 c1.display();

 cout << "Second complex number: ";
 c2.display();

 c3 = c1.add(c2);
 cout << "Sum: ";
 c3.display();

 return 0;
}
```

**Output**:

```
First complex number: 3 + 4i
Second complex number: 1 - 2i
Sum: 4 + 2i
```

### Example 2: Constructor Overloading and Destructor

**Problem**: Create a class `String` that manages a dynamically allocated character array. Implement multiple constructors and a destructor to prevent memory leaks.

```cpp
#include <iostream>
#include <cstring>
using namespace std;

class String {
private:
 char* str;
 int length;

public:
 // Default constructor
 String() {
 str = nullptr;
 length = 0;
 }

 // Parameterized constructor
 String(const char* s) {
 length = strlen(s);
 str = new char[length + 1];
 strcpy(str, s);
 }

 // Copy constructor
 String(const String& s) {
 length = s.length;
 str = new char[length + 1];
 strcpy(str, s.str);
 }

 // Destructor
 ~String() {
 if (str != nullptr) {
 delete[] str;
 str = nullptr;
 }
 }

 // Function to display string
 void display() {
 if (str != nullptr)
 cout << str << endl;
 }

 // Function to get length
 int getLength() {
 return length;
 }
};

int main() {
 String s1("Hello World");
 cout << "s1: ";
 s1.display();
 cout << "Length: " << s1.getLength() << endl;

 String s2 = s1; // Uses copy constructor
 cout << "s2 (copy): ";
 s2.display();

 return 0;
}
```

**Explanation**: The copy constructor ensures deep copying of the string, which is essential when a class manages dynamic memory. Without it, both objects would point to the same memory location, leading to double deletion when destructors are called.

### Example 3: Static Members and this Pointer

**Problem**: Create a class `Item` that tracks the number of items created using a static counter. Use the `this` pointer to implement a function that compares two items.

```cpp
#include <iostream>
using namespace std;

class Item {
private:
 int code;
 float price;
 static int count; // Static counter

public:
 Item() {
 code = 0;
 price = 0.0;
 }

 Item(int c, float p) {
 code = c;
 price = p;
 count++;
 }

 // Using this pointer to compare items
 bool isSameAs(Item& other) {
 return (this->code == other.code && this->price == other.price);
 }

 // Static function to get count
 static int getCount() {
 return count;
 }

 void display() {
 cout << "Code: " << code << ", Price: " << price << endl;
 }
};

int Item::count = 0; // Initialize static member

int main() {
 Item i1(101, 250.50);
 Item i2(102, 150.75);
 Item i3(101, 250.50);

 cout << "Total items created: " << Item::getCount() << endl;

 i1.display();
 i2.display();
 i3.display();

 if (i1.isSameAs(i3)) {
 cout << "i1 and i3 have same code and price" << endl;
 } else {
 cout << "i1 and i3 are different" << endl;
 }

 return 0;
}
```

**Output**:

```
Total items created: 3
Code: 101, Price: 250.5
Code: 102, Price: 150.75
Code: 101, Price: 250.5
i1 and i3 have same code and price
```

## Exam Tips

1. **Understand the difference between class and structure**: In C++, the only difference is the default access specifier. Class members are private by default, while struct members are public by default.

2. **Remember constructor and destructor characteristics**: Constructors have the same name as the class, no return type, and are called automatically. Destructors have the same name prefixed with ~, no return type and no parameters, and are called automatically when objects are destroyed.

3. **Know when to use initialization lists**: Use initialization lists for initializing const members, reference members, and base class constructors. They are more efficient than assignment in the constructor body.

4. **Remember the order of execution**: Constructor is called before destructor. For local objects, destructor is called when the scope ends. For dynamically allocated objects, destructor is called when delete is used.

5. **Understand the this pointer**: The this pointer points to the object itself and is implicitly available in all non-static member functions. It cannot be modified.

6. **Static members require external definition**: Static data members must be defined outside the class (unless they are const integral types with initializers). This is a common source of linker errors.

7. **Friend functions violate encapsulation**: While useful, friend functions break the encapsulation principle. Use them sparingly and only when necessary for operator overloading or closely related classes.

8. **Copy constructor vs assignment operator**: Copy constructor is called when a new object is created from an existing object. Assignment operator is called when an existing object is assigned values from another existing object.

9. **Constant member functions**: A const member function promises not to modify any data members. Both const and non-const objects can call const member functions.

10. **Access specifiers in inheritance**: Remember that private members are never accessible directly in derived classes, regardless of the access specifier used during inheritance.
