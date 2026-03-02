# Arrays of Objects in C++

## Introduction

Arrays of objects represent one of the fundamental data structures in object-oriented programming, combining the power of arrays with the encapsulation features of classes. In C++, an array of objects allows programmers to store multiple instances of a class in a contiguous memory locations, enabling efficient management of related objects. This concept becomes particularly valuable when dealing with collections of similar entities such as students in a class, employees in an organization, or products in an inventory system.

The importance of arrays of objects extends beyond mere data storage. They provide a structured approach to handling groups of related objects while maintaining the object-oriented principles of data hiding and encapsulation. Each element in an array of objects is a complete object with its own set of data members and member functions. This enables programmers to perform operations on collections of objects using loops and array indexing, making code more concise and maintainable.

In the context of the university's Object-Oriented Programming with C++ course, understanding arrays of objects is essential for grasping more advanced concepts such as dynamic memory management, file handling with objects, and standard template library containers. This topic serves as a bridge between basic array concepts and complex object-oriented design patterns.

## Key Concepts

### Declaration and Definition of Arrays of Objects

When declaring an array of objects, the syntax follows the same pattern as declaring an array of primitive types, but with the class name serving as the data type. The general syntax is:

```cpp
ClassName arrayName[arraySize];
```

For example, to create an array of 10 Student objects:

```cpp
class Student {
private:
 int rollNo;
 char name[50];
 float marks;
public:
 void getData();
 void displayData();
};

Student s[10]; // Array of 10 Student objects
```

When objects are created as array elements, the default constructor of the class is automatically invoked for each object. If the class does not have a default constructor, the compilation will fail. Therefore, it is mandatory to define a default constructor when working with arrays of objects, or use parameterized constructor with default arguments.

### Initialization Using Constructors

Arrays of objects can be initialized at the time of declaration using constructors. There are two primary approaches:

**Using Default Constructor:**

```cpp
Student s[5]; // Calls default constructor 5 times
```

**Using Parameterized Constructor:**

```cpp
Student s[3] = {Student(1, "Alice", 85.5),
 Student(2, "Bob", 90.0),
 Student(3, "Charlie", 78.5)};
```

Alternatively, if the class has a parameterized constructor, C++ allows a more concise initialization:

```cpp
Student s[3] = {Student(1, "Alice", 85.5),
 Student(2, "Bob", 90.0),
 Student(3, "Charlie", 78.5)};
```

### Accessing Members of Objects in Array

Individual objects within an array are accessed using subscript notation (index). Once a specific object is accessed, its members can be manipulated using the dot operator (.) or arrow operator (->) depending on whether the array contains objects or pointers to objects.

```cpp
s[0].getData(); // Access getData() for first object
s[0].displayData(); // Access displayData() for first object
s[4].marks = 95.5; // Access data member directly (if public)
```

To process all objects in an array, loops are commonly used:

```cpp
for (int i = 0; i < 10; i++) {
 s[i].displayData();
}
```

### Array of Objects and Member Functions

Each object in the array has its own copy of data members, but all objects share the same member functions. When a member function is called through a specific object, the function operates on that particular object's data members. This is achieved through the implicit 'this' pointer that C++ provides.

```cpp
class Rectangle {
 int length, breadth;
public:
 void setDimensions(int l, int b) {
 length = l;
 breadth = b;
 }
 int calculateArea() {
 return length * breadth;
 }
};

Rectangle r[5];
r[0].setDimensions(10, 5);
r[1].setDimensions(7, 3);
cout << "Area: " << r[0].calculateArea(); // Output: 50
```

### Passing Arrays of Objects to Functions

Arrays of objects can be passed to functions either by value or by reference. When passed by value, a copy of each object is created using the copy constructor. When passed by reference, the function works with the original objects.

**Pass by Value:**

```cpp
void displayStudent(Student s) {
 s.displayData();
}

// Calling
displayStudent(s[0]); // Creates a copy
```

**Pass by Reference:**

```cpp
void displayStudent(Student &s) {
 s.displayData();
}

// Calling
displayStudent(s[0]); // Works with original object
```

**Passing Entire Array:**

```cpp
void displayAll(Student s[], int n) {
 for (int i = 0; i < n; i++) {
 s[i].displayData();
 }
}

// Calling
displayAll(s, 10);
```

### Dynamic Arrays of Objects

C++ allows creation of dynamic arrays of objects using the 'new' keyword. This is particularly useful when the number of objects is not known at compile time.

```cpp
int n;
cout << "Enter number of students: ";
cin >> n;

Student *s = new Student[n]; // Dynamic array of n objects

// Accessing elements
s[0].getData();
s[0].displayData();

delete[] s; // Deallocate memory
```

For dynamic arrays with pointers to objects:

```cpp
Student *s = new Student[n];
// Each element is a pointer
s[0] = new Student(1, "Alice", 85.5);
```

### Destructors and Arrays of Objects

When an array of objects goes out of scope or is explicitly deleted, the destructor is called for each object in the array. This is particularly important when dealing with dynamically allocated arrays of objects that contain pointers to dynamically allocated memory.

```cpp
class String {
 char *name;
public:
 String() {
 name = new char[50];
 }
 ~String() {
 delete[] name; // Called for each object
 }
};

String s[5]; // Destructor called for each when array goes out of scope
```

## Examples

### Example 1: Employee Management System

**Problem:** Create a class Employee with empId, name, and salary. Create an array of 5 employees, accept data, and display those with salary above 50000.

```cpp
#include <iostream>
#include <string.h>
using namespace std;

class Employee {
 int empId;
 char name[30];
 float salary;
public:
 Employee() {
 empId = 0;
 name[0] = '\0';
 salary = 0.0;
 }

 void getData() {
 cout << "Enter Employee ID: ";
 cin >> empId;
 cout << "Enter Name: ";
 cin >> name;
 cout << "Enter Salary: ";
 cin >> salary;
 }

 void displayData() {
 cout << "ID: " << empId << endl;
 cout << "Name: " << name << endl;
 cout << "Salary: " << salary << endl;
 }

 float getSalary() {
 return salary;
 }
};

int main() {
 Employee emp[5];
 int n = 5;

 cout << "Enter details of " << n << " employees:" << endl;
 for (int i = 0; i < n; i++) {
 cout << "\nEmployee " << i + 1 << ":" << endl;
 emp[i].getData();
 }

 cout << "\nEmployees with salary > 50000:" << endl;
 for (int i = 0; i < n; i++) {
 if (emp[i].getSalary() > 50000) {
 emp[i].displayData();
 cout << "-------------------" << endl;
 }
 }

 return 0;
}
```

**Step-by-step Solution:**

1. Define the Employee class with appropriate data members and member functions
2. Create an array of 5 Employee objects in main()
3. Use a for loop to accept data for each employee using getData()
4. Use another for loop to check salary condition and display qualifying employees

### Example 2: Complex Number Operations

**Problem:** Create a class Complex with real and imaginary parts. Store 3 complex numbers in an array and find their sum.

```cpp
#include <iostream>
using namespace std;

class Complex {
 float real, imag;
public:
 Complex() {
 real = imag = 0;
 }

 Complex(float r, float i) {
 real = r;
 imag = i;
 }

 void getData() {
 cout << "Enter real part: ";
 cin >> real;
 cout << "Enter imaginary part: ";
 cin >> imag;
 }

 void displayData() {
 cout << real;
 if (imag >= 0)
 cout << " + " << imag << "i" << endl;
 else
 cout << " - " << (-imag) << "i" << endl;
 }

 Complex add(Complex c) {
 Complex temp;
 temp.real = real + c.real;
 temp.imag = imag + c.imag;
 return temp;
 }
};

int main() {
 Complex c[3], sum;

 cout << "Enter 3 complex numbers:" << endl;
 for (int i = 0; i < 3; i++) {
 c[i].getData();
 }

 // Initialize sum with first element
 sum = c[0];

 // Add remaining elements
 for (int i = 1; i < 3; i++) {
 sum = sum.add(c[i]);
 }

 cout << "\nSum of complex numbers: ";
 sum.displayData();

 return 0;
}
```

### Example 3: Dynamic Array of Objects with Constructor Arguments

**Problem:** Create a dynamic array of Box objects with specified dimensions at runtime.

```cpp
#include <iostream>
using namespace std;

class Box {
 int length, width, height;
public:
 Box() {
 length = width = height = 0;
 }

 Box(int l, int w, int h) {
 length = l;
 width = w;
 height = h;
 }

 int volume() {
 return length * width * height;
 }

 void display() {
 cout << "Dimensions: " << length << " x " << width
 << " x " << height << endl;
 cout << "Volume: " << volume() << endl;
 }
};

int main() {
 int n;
 cout << "Enter number of boxes: ";
 cin >> n;

 // Dynamic array of objects
 Box *boxes = new Box[n];

 int l, w, h;
 for (int i = 0; i < n; i++) {
 cout << "Enter dimensions for box " << i + 1 << ": ";
 cin >> l >> w >> h;
 boxes[i] = Box(l, w, h); // Using parameterized constructor
 }

 cout << "\nBox Details:" << endl;
 for (int i = 0; i < n; i++) {
 boxes[i].display();
 cout << "-------------------" << endl;
 }

 delete[] boxes;
 return 0;
}
```

## Exam Tips

1. **Remember Default Constructor Requirement:** For arrays of objects, ensure your class has a default constructor. If you define a parameterized constructor without a default constructor, the compilation will fail.

2. **Constructor Call Sequence:** When creating an array of objects, the default constructor is called n times (where n is the array size). For dynamic arrays, this also applies.

3. **Accessing Members:** Use array subscript with dot operator: `objectArray[index].memberFunction()`. Parentheses are essential when calling member functions.

4. **Destructor Execution:** Destructors are called in reverse order when an array of objects is destroyed. Always ensure proper memory management for dynamic arrays.

5. **Pass by Reference vs Value:** When passing arrays of objects to functions, prefer pass by reference to avoid overhead of calling copy constructor for each object.

6. **Initialization Syntax:** For arrays of objects with parameterized constructors, use the explicit initialization form: `ClassName obj[2] = {ClassName(args1), ClassName(args2)}`.

7. **'this' Pointer Concept:** Understand that each member function has access to a 'this' pointer that points to the specific object being operated on.

8. **Memory Leak Prevention:** When using dynamic arrays of objects with pointer data members, ensure proper deallocation in destructors to prevent memory leaks.

9. **Static Data Members:** Remember that static data members are shared among all objects in an array - there is only one copy of the static member.

10. **Practice Code Tracing:** Be prepared to trace code that accesses arrays of objects in loops and function calls, as this is commonly tested in university exams.
