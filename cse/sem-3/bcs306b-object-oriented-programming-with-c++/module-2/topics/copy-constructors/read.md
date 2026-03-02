# Copy Constructors in C++

## Introduction

Copy constructors are a fundamental concept in C++ object-oriented programming that enables the creation of new objects as exact copies of existing objects. This mechanism is essential for understanding memory management, object initialization, and proper resource handling in C++ programs. The copy constructor is a special constructor that initializes a new object using an existing object of the same class.

In modern C++ programming, copy constructors play a critical role in various scenarios, including passing objects to functions by value, returning objects from functions, and creating objects from existing objects. Without proper understanding of copy constructors, programmers often encounter subtle bugs related to shallow copying, double deletion of resources, and unexpected behavior. This topic is particularly important for CSE students as it forms the foundation for understanding move semantics, rule of three/five/zero, and modern C++ best practices.

The copy constructor becomes even more significant when dealing with classes that manage dynamic memory, file handles, network connections, or other system resources. Understanding when and how to implement copy constructors properly distinguishes competent C++ programmers from beginners.

## Key Concepts

### Definition and Declaration

A copy constructor is a special constructor that takes a reference to an object of the same class as its parameter and creates a new object that is a copy of the existing one. The parameter must be a reference (preferably const reference) to avoid infinite recursion.

The general syntax for a copy constructor is:

```cpp
class ClassName {
public:
 ClassName(const ClassName& obj); // Copy constructor declaration
};
```

The copy constructor can be defined inside the class or declared as a friend function. It is always called when a new object is created from an existing object of the same class.

### Default Copy Constructor

If no copy constructor is explicitly defined in a class, the compiler provides a default copy constructor. The default copy constructor performs a **memberwise copy** (also called shallow copy), where each member variable is copied from the source object to the new object. For primitive types (int, float, char, etc.), this works perfectly. However, for pointer members that point to dynamically allocated memory, shallow copy can lead to serious problems.

Consider this example:

```cpp
class Student {
private:
 char* name;
 int age;
public:
 Student(const char* n, int a) {
 age = a;
 name = new char[strlen(n) + 1];
 strcpy(name, n);
 }
 // No copy constructor defined - compiler provides default
};

int main() {
 Student s1("John", 20);
 Student s2 = s1; // Default copy constructor called - shallow copy
 return 0;
}
```

In this case, both `s1.name` and `s2.name` will point to the same memory location, causing potential double deletion issues.

### Shallow Copy vs Deep Copy

**Shallow Copy**: The default copy constructor performs shallow copy, where only the pointer values are copied, not the actual data they point to. This means multiple objects may end up sharing the same dynamically allocated memory.

**Deep Copy**: A user-defined copy constructor that allocates new memory and copies the actual data content is called deep copy. This ensures each object has its own independent copy of the data.

Example demonstrating deep copy:

```cpp
class Student {
private:
 char* name;
 int age;
public:
 Student(const char* n, int a) {
 age = a;
 name = new char[strlen(n) + 1];
 strcpy(name, n);
 }

 // User-defined copy constructor (Deep Copy)
 Student(const Student& obj) {
 age = obj.age;
 name = new char[strlen(obj.name) + 1];
 strcpy(name, obj.name);
 }

 ~Student() {
 delete[] name;
 }
};
```

### When Copy Constructor is Called

The copy constructor is invoked in the following scenarios:

1. **Object Initialization**: When a new object is created from an existing object using the copy initialization syntax

```cpp
MyClass obj2 = obj1; // Copy constructor called
MyClass obj3(obj1); // Copy constructor called
```

2. **Passing Objects by Value**: When an object is passed to a function by value

```cpp
void display(MyClass obj) {
// obj is a copy created using copy constructor
}
```

3. **Returning Objects by Value**: When a function returns an object by value

```cpp
MyClass createObject() {
MyClass temp;
return temp; // Copy constructor may be called
}
```

4. **Array Initialization**: When initializing an array of class objects

```cpp
MyClass arr[3] = {obj1, obj2, obj3};
```

### Copy Constructor vs Assignment Operator

It is crucial to distinguish between copy constructor and assignment operator:

- **Copy Constructor**: Creates a new object from an existing object (initialization)
- **Assignment Operator**: Assigns value to an already existing object

```cpp
MyClass obj1;
MyClass obj2 = obj1; // Copy constructor (initialization)

MyClass obj3;
obj3 = obj1; // Assignment operator (obj3 already exists)
```

### Copy Constructor and const Correctness

The parameter of a copy constructor should be a const reference. This allows copying from both const and non-const objects while ensuring the source object is not modified:

```cpp
class MyClass {
public:
 MyClass(const MyClass& obj); // Recommended form
};
```

The const qualifier is important because:

- It allows copying from const objects
- It prevents accidental modification of the source object
- It enables binding to temporary objects

### Copy Constructor and Inheritance

When a class inherits from another class, the derived class's copy constructor must properly copy both the base class members and its own members. This requires explicitly calling the base class copy constructor:

```cpp
class Base {
protected:
 int value;
public:
 Base(const Base& obj) : value(obj.value) {}
};

class Derived : public Base {
private:
 int extra;
public:
 Derived(const Derived& obj) : Base(obj), extra(obj.extra) {}
};
```

### Private Copy Constructor

Sometimes we want to prevent copying of objects. This can be achieved by making the copy constructor private:

```cpp
class NonCopyable {
private:
 NonCopyable(const NonCopyable&); // Private and not defined
public:
 NonCopyable() {}
};

int main() {
 NonCopyable obj1;
 // NonCopyable obj2 = obj1; // Compilation error
 return 0;
}
```

## Examples

### Example 1: Simple Copy Constructor with Deep Copy

```cpp
#include <iostream>
#include <cstring>
using namespace std;

class String {
private:
 char* str;
 int length;
public:
 // Constructor
 String(const char* s) {
 length = strlen(s);
 str = new char[length + 1];
 strcpy(str, s);
 }

 // Copy Constructor (Deep Copy)
 String(const String& obj) {
 length = obj.length;
 str = new char[length + 1];
 strcpy(str, obj.str);
 cout << "Copy constructor called" << endl;
 }

 // Destructor
 ~String() {
 delete[] str;
 }

 void display() {
 cout << str << endl;
 }
};

int main() {
 String s1("Hello World");
 cout << "Original string: ";
 s1.display();

 String s2 = s1; // Copy constructor invoked
 cout << "Copied string: ";
 s2.display();

 return 0;
}
```

**Output:**

```
Original string: Hello World
Copy constructor called
Copied string: Hello World
```

### Example 2: Copy Constructor with Dynamic Memory Allocation

```cpp
#include <iostream>
using namespace std;

class Matrix {
private:
 int** data;
 int rows, cols;
public:
 Matrix(int r, int c) : rows(r), cols(c) {
 data = new int*[rows];
 for (int i = 0; i < rows; i++) {
 data[i] = new int[cols];
 for (int j = 0; j < cols; j++)
 data[i][j] = 0;
 }
 }

 // Copy Constructor - Deep Copy
 Matrix(const Matrix& obj) : rows(obj.rows), cols(obj.cols) {
 data = new int*[rows];
 for (int i = 0; i < rows; i++) {
 data[i] = new int[cols];
 for (int j = 0; j < cols; j++)
 data[i][j] = obj.data[i][j]; // Copy content
 }
 cout << "Deep copy performed" << endl;
 }

 void setElement(int r, int c, int val) {
 if (r >= 0 && r < rows && c >= 0 && c < cols)
 data[r][c] = val;
 }

 void display() {
 for (int i = 0; i < rows; i++) {
 for (int j = 0; j < cols; j++)
 cout << data[i][j] << " ";
 cout << endl;
 }
 }

 ~Matrix() {
 for (int i = 0; i < rows; i++)
 delete[] data[i];
 delete[] data;
 }
};

int main() {
 Matrix m1(2, 3);
 m1.setElement(0, 0, 1);
 m1.setElement(1, 2, 5);

 cout << "Matrix m1:" << endl;
 m1.display();

 Matrix m2 = m1; // Copy constructor called
 cout << "Matrix m2 (copy of m1):" << endl;
 m2.display();

 return 0;
}
```

### Example 3: Copy Constructor in Function Parameters

```cpp
#include <iostream>
using namespace std;

class Box {
private:
 int width, height;
 static int copyCount;

public:
 Box(int w, int h) : width(w), height(h) {
 cout << "Constructor called" << endl;
 }

 // Copy Constructor
 Box(const Box& obj) : width(obj.width), height(obj.height) {
 copyCount++;
 cout << "Copy constructor called (Count: " << copyCount << ")" << endl;
 }

 void displayDimensions() {
 cout << "Width: " << width << ", Height: " << height << endl;
 }

 static int getCopyCount() {
 return copyCount;
 }
};

int Box::copyCount = 0;

// Function that takes object by value
void processBox(Box b) {
 cout << "Inside processBox function" << endl;
 b.displayDimensions();
}

// Function that takes object by reference
void processBoxRef(const Box& b) {
 cout << "Inside processBoxRef function" << endl;
 b.displayDimensions();
}

int main() {
 Box b1(10, 20);
 cout << "---" << endl;

 cout << "Passing to function by value:" << endl;
 processBox(b1); // Copy constructor called

 cout << "---" << endl;

 cout << "Passing to function by reference:" << endl;
 processBoxRef(b1); // No copy constructor called

 cout << "---" << endl;

 Box b2 = b1; // Copy constructor called
 Box b3(b1); // Copy constructor called

 cout << "Total copies made: " << Box::getCopyCount() << endl;

 return 0;
}
```

## Exam Tips

1. **Remember the signature**: The copy constructor always takes a reference to the same class type as its parameter (preferably const reference).

2. **Distinguish shallow vs deep copy**: Know when each is needed. Deep copy is essential for classes with pointer members pointing to dynamically allocated memory.

3. **Know when copy constructor is called**: Initialization with another object, passing by value, returning by value, and array initialization.

4. **Copy constructor vs assignment operator**: Remember that copy constructor creates new objects, while assignment operator modifies existing objects.

5. **Default copy constructor performs memberwise shallow copy**: This is the key point that causes problems with pointer members.

6. **Rule of Three**: If you define any of destructor, copy constructor, or assignment operator, you should define all three.

7. **Const correctness**: Always use const reference parameter to allow copying from both const and non-const objects.

8. **Virtual copy constructors**: Not directly possible in C++, but can be achieved using clone() pattern for polymorphic copying.

9. **Pass-by-value creates copies**: Remember that when objects are passed to functions by value, the copy constructor is invoked.

10. **Prevent copying**: Make copy constructor private to prevent object copying when not desired.
