# Introducing C++ Classes

## Introduction

Object-Oriented Programming (OOP) represents a paradigm shift from procedural programming, focusing on objects rather than procedures. C++, developed by Bjarne Stroustrup at Bell Labs in 1979 as an extension of the C programming language, brought the power of object-oriented programming to systems programming. The class is the fundamental building block of object-oriented programming in C++, serving as a blueprint for creating objects that encapsulate data and behavior.

Understanding classes is crucial for any C++ programmer because they enable data abstraction, encapsulation, inheritance, and polymorphism—the four pillars of object-oriented programming. In the context of the university's BCS306B curriculum, this topic forms the foundation upon which more advanced OOP concepts are built. This module introduces the fundamental concepts of classes, including their structure, members, access specifiers, and the distinction between class and structure.

## Key Concepts

### What is a Class?

A class is a user-defined data type that combines data members (variables) and member functions (methods) into a single unit. It serves as a blueprint or template from which objects are created. Unlike primitive data types, classes allow programmers to create custom types that model real-world entities with both attributes and behaviors.

**Syntax for Class Definition:**

```cpp
class ClassName {
 // private members (by default)
 // public members
 // protected members
};
```

### Class vs Structure

In C++, both classes and structures can contain data members and member functions. The primary difference lies in default access specifiers: members of a class are private by default, while members of a struct are public by default. Additionally, inheritance defaults differ: private for classes, public for structures.

```cpp
class MyClass {
 int data; // private by default
};

struct MyStruct {
 int data; // public by default
};
```

### Access Specifiers

C++ provides three access specifiers that control the visibility and accessibility of class members:

1. **private**: Members are accessible only within the class and friend functions. This is the default access level for class members.

2. **public**: Members are accessible from anywhere the object is visible. Public members define the interface of the class.

3. **protected**: Similar to private, but accessible in derived classes (covered in later modules).

### Data Members and Member Functions

**Data Members** (also called attributes or properties) are variables declared within a class that store the state or characteristics of objects created from the class.

**Member Functions** (also called methods) are functions declared within a class that define the behavior or operations that can be performed on objects.

```cpp
class BankAccount {
private:
 double balance; // data member
 string accountHolder; // data member

public:
 void deposit(double amount); // member function
 void withdraw(double amount); // member function
 double getBalance(); // member function
};
```

### Creating Objects

An object is an instance of a class. Creating an object allocates memory for the data members and provides access to the member functions.

```cpp
BankAccount account1; // Object created on stack
BankAccount* account2 = new BankAccount(); // Object created on heap
```

### Constructors

A constructor is a special member function that is automatically called when an object is created. It initializes the object and has the same name as the class.

**Types of Constructors:**

1. **Default Constructor**: Takes no parameters
2. **Parameterized Constructor**: Takes one or more parameters
3. **Copy Constructor**: Creates an object as a copy of another object

```cpp
class Rectangle {
private:
 double length, breadth;

public:
 // Default constructor
 Rectangle() {
 length = breadth = 0;
 }

 // Parameterized constructor
 Rectangle(double l, double b) {
 length = l;
 breadth = b;
 }

 // Copy constructor
 Rectangle(const Rectangle& r) {
 length = r.length;
 breadth = r.breadth;
 }
};
```

### Destructor

A destructor is a special member function called when an object is destroyed. It has the same name as the class preceded by a tilde (~) and takes no parameters. Destructors are used to release resources allocated by the object.

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

### this Pointer

The `this` pointer is an implicit pointer available within member functions that points to the object for which the function was called. It is particularly useful for distinguishing between member variables and parameters with the same name.

```cpp
class Sample {
private:
 int data;

public:
 void setData(int data) {
 this->data = data; // this->data refers to member variable
 }
};
```

### Static Members

Static members belong to the class rather than any particular object. There is only one copy of a static member shared by all objects of the class.

```cpp
class Counter {
private:
 static int count; // Static data member

public:
 Counter() {
 count++;
 }

 static int getCount() { // Static member function
 return count;
 }
};

int Counter::count = 0; // Definition outside class
```

## Examples

### Example 1: Creating a Simple Student Class

**Problem:** Create a class named `Student` with private data members for name and roll number, and public member functions to set and display student information.

**Solution:**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Student {
private:
 string name;
 int rollNo;

public:
 // Member function to set student details
 void setDetails(string n, int r) {
 name = n;
 rollNo = r;
 }

 // Member function to display student details
 void display() {
 cout << "Name: " << name << endl;
 cout << "Roll Number: " << rollNo << endl;
 }
};

int main() {
 Student s1, s2;

 s1.setDetails("John Doe", 101);
 s2.setDetails("Jane Smith", 102);

 cout << "Student 1 Details:" << endl;
 s1.display();

 cout << "\nStudent 2 Details:" << endl;
 s2.display();

 return 0;
}
```

**Output:**

```
Student 1 Details:
Name: John Doe
Roll Number: 101

Student 2 Details:
Name: Jane Smith
Roll Number: 102
```

### Example 2: Implementing Constructor and Destructor

**Problem:** Create a class `Shape` with parameterized constructor to initialize dimensions and a destructor to display a message when object is destroyed.

**Solution:**

```cpp
#include <iostream>
using namespace std;

class Shape {
private:
 int width, height;

public:
 // Parameterized constructor
 Shape(int w, int h) {
 width = w;
 height = h;
 cout << "Constructor: Shape created with dimensions "
 << width << " x " << height << endl;
 }

 // Destructor
 ~Shape() {
 cout << "Destructor: Shape with dimensions "
 << width << " x " << height << " is being destroyed" << endl;
 }

 int area() {
 return width * height;
 }
};

int main() {
 cout << "Creating first shape..." << endl;
 Shape s1(5, 3);
 cout << "Area: " << s1.area() << endl;

 cout << "\nCreating second shape..." << endl;
 Shape s2(10, 7);
 cout << "Area: " << s2.area() << endl;

 cout << "\nExiting main function..." << endl;
 return 0;
}
```

**Output:**

```
Creating first shape...
Constructor: Shape created with dimensions 5 x 3
Area: 15

Creating second shape...
Constructor: Shape created with dimensions 10 x 7
Area: 70

Exiting main function...
Destructor: Shape with dimensions 10 x 7 is being destroyed
Destructor: Shape with dimensions 5 x 3 is being destroyed
```

### Example 3: Using Static Members

**Problem:** Create a class `Employee` that keeps track of the total number of employees using a static data member.

**Solution:**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Employee {
private:
 string name;
 int empID;
 static int empCount; // Static data member

public:
 Employee(string n, int id) {
 name = n;
 empID = id;
 empCount++; // Increment count when new employee is created
 cout << "Employee " << name << " added. ";
 cout << "Total employees: " << empCount << endl;
 }

 ~Employee() {
 empCount--; // Decrement when employee is removed
 cout << "Employee " << name << " removed. ";
 cout << "Total employees: " << empCount << endl;
 }

 static int getCount() { // Static member function
 return empCount;
 }

 void display() {
 cout << "ID: " << empID << ", Name: " << name << endl;
 }
};

// Definition and initialization of static member
int Employee::empCount = 0;

int main() {
 cout << "Initial employee count: " << Employee::getCount() << endl;

 Employee e1("Alice", 1001);
 Employee e2("Bob", 1002);
 Employee e3("Charlie", 1003);

 cout << "\nFinal employee count: " << Employee::getCount() << endl;

 cout << "\n--- Employees leaving ---" << endl;
 return 0;
}
```

## Exam Tips

1. **Remember Default Access Specifiers**: Class members are private by default, while struct members are public by default. This is a frequently tested concept in university exams.

2. **Constructor vs Destructor**: Constructors have the same name as the class and can be overloaded; destructors have a tilde (~) prefix, cannot be overloaded, and take no parameters.

3. **this Pointer Usage**: The `this` pointer is implicitly available in all non-static member functions and points to the current object.

4. **Static Members Need Definition**: Static data members must be defined outside the class (usually in a .cpp file) to allocate memory. This is a common mistake students make.

5. **Access Specifier Flow**: Private members cannot be accessed directly from main() or other functions; they can only be accessed through public member functions.

6. **Memory Allocation**: Objects created on the stack are automatically destroyed when they go out of scope, calling the destructor automatically. For heap-allocated objects, you must use `delete` to trigger the destructor.

7. **Copy Constructor**: The copy constructor is invoked when passing an object by value to a function, returning an object by value, or initializing a new object from an existing one.

8. **Practice Syntax**: Be thorough with class definition syntax, including the use of semicolons after the closing brace—missing semicolons is a common compilation error.

9. **Const Member Functions**: Member functions that do not modify any data members should be declared as `const` for correctness and to allow calling on const objects.

10. **Object Size**: The size of an object includes the size of all its data members. Member functions are not stored in each object—they exist in a single location and are shared.
