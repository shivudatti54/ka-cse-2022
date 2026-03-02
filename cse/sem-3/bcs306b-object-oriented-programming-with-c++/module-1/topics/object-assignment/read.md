# Object Assignment in C++

## Introduction

Object assignment is a fundamental operation in object-oriented programming that allows one object to be copied into another using the assignment operator (=). In C++, when we assign one object to another, a member-wise copy is performed by default, where each data member of the source object is copied to the corresponding member of the destination object. This concept forms the backbone of object management in C++ and is essential for understanding memory management, shallow vs. deep copying, and the Rule of Three/Five in C++.

Understanding object assignment is crucial for CSE students because it directly impacts how objects behave in memory, how resources are managed, and how programs handle complex data structures. improper understanding of object assignment can lead to subtle bugs such as double-free errors, memory leaks, or dangling pointers. This topic becomes particularly important when dealing with classes that manage dynamic memory or other resources, where default assignment behavior may not be sufficient.

In this module, we will explore the intricacies of object assignment in C++, including the default assignment operator, the differences between shallow and deep copying, copy constructors versus assignment operators, and the advanced concepts of move semantics. These concepts are not only theoretically important but also have significant practical applications in software development.

## Key Concepts

### 1. The Assignment Operator

In C++, the assignment operator is a binary operator that assigns values from one object to another. For user-defined classes, C++ provides a default assignment operator that performs member-wise copy. The signature of the assignment operator is typically:

```cpp
ClassName& operator=(const ClassName& other);
```

The default assignment operator works similarly to the default copy constructor - it performs a shallow copy of all non-static data members. If the class contains pointers, only the pointer addresses are copied, not the actual data they point to.

Example demonstrating default assignment:

```cpp
#include <iostream>
using namespace std;

class Student {
private:
 int id;
 char* name;

public:
 Student(int i, const char* n) {
 id = i;
 name = new char[strlen(n) + 1];
 strcpy(name, n);
 }

 void display() {
 cout << "ID: " << id << ", Name: " << name << endl;
 }

 ~Student() {
 delete[] name;
 }
};

int main() {
 Student s1(101, "John");
 Student s2(102, "Alice");

 s2 = s1; // Default assignment - shallow copy

 s1.display();
 s2.display();

 return 0;
}
```

In this example, after `s2 = s1`, both objects' name pointers point to the same memory location, which can cause problems when destructors are called.

### 2. Copy Constructor vs Assignment Operator

Understanding the difference between copy constructor and assignment operator is crucial:

- **Copy Constructor**: Called when a new object is being created from an existing object
- **Assignment Operator**: Called when an already existing object is assigned a new value

```cpp
class Box {
 int width, height;
public:
 Box(int w, int h) : width(w), height(h) {}

 // Copy Constructor
 Box(const Box& b) : width(b.width), height(b.height) {
 cout << "Copy Constructor Called" << endl;
 }

 // Assignment Operator
 Box& operator=(const Box& b) {
 cout << "Assignment Operator Called" << endl;
 if (this != &b) { // Check for self-assignment
 width = b.width;
 height = b.height;
 }
 return *this;
 }
};

int main() {
 Box b1(10, 20);
 Box b2(30, 40);

 Box b3 = b1; // Copy Constructor (new object)
 b2 = b1; // Assignment Operator (existing object)

 return 0;
}
```

### 3. Shallow Copy vs Deep Copy

**Shallow Copy**: The default copy mechanism where pointer members copy the address, not the actual data. Both objects end up pointing to the same memory location.

**Deep Copy**: A custom copy where new memory is allocated and actual data is copied, ensuring each object has its own independent copy of the data.

```cpp
class DeepCopy {
private:
 int size;
 int* data;

public:
 DeepCopy(int s) : size(s) {
 data = new int[size];
 }

 // Deep Copy Constructor
 DeepCopy(const DeepCopy& obj) : size(obj.size) {
 data = new int[size];
 for (int i = 0; i < size; i++) {
 data[i] = obj.data[i];
 }
 }

 // Deep Copy Assignment Operator
 DeepCopy& operator=(const DeepCopy& obj) {
 if (this != &obj) {
 delete[] data; // Free existing memory
 size = obj.size;
 data = new int[size];
 for (int i = 0; i < size; i++) {
 data[i] = obj.data[i];
 }
 }
 return *this;
 }

 void setData(int index, int value) {
 if (index >= 0 && index < size) {
 data[index] = value;
 }
 }

 void display() {
 for (int i = 0; i < size; i++) {
 cout << data[i] << " ";
 }
 cout << endl;
 }

 ~DeepCopy() {
 delete[] data;
 }
};
```

### 4. The Rule of Three

In C++, if a class requires a custom destructor, copy constructor, or copy assignment operator, it likely requires all three. This is known as the Rule of Three.

```cpp
class Resource {
private:
 int* ptr;
 int size;

public:
 Resource(int s) : size(s) {
 ptr = new int[size];
 }

 // Destructor
 ~Resource() {
 delete[] ptr;
 }

 // Copy Constructor
 Resource(const Resource& obj) : size(obj.size) {
 ptr = new int[size];
 for (int i = 0; i < size; i++) {
 ptr[i] = obj.ptr[i];
 }
 }

 // Assignment Operator
 Resource& operator=(const Resource& obj) {
 if (this != &obj) {
 delete[] ptr;
 size = obj.size;
 ptr = new int[size];
 for (int i = 0; i < size; i++) {
 ptr[i] = obj.ptr[i];
 }
 }
 return *this;
 }
};
```

### 5. Self-Assignment Check

When implementing the assignment operator, it is essential to check for self-assignment. This prevents unnecessary work and potential issues when deleting and reallocating memory.

```cpp
Box& operator=(const Box& other) {
 // Check for self-assignment
 if (this != &other) {
 width = other.width;
 height = other.height;
 }
 return *this;
}
```

Without this check, assigning an object to itself could lead to data corruption, especially when dealing with dynamically allocated memory.

## Examples

### Example 1: Simple Class Assignment

**Problem**: Create a class `Complex` with real and imaginary parts. Demonstrate assignment between two Complex objects.

```cpp
#include <iostream>
using namespace std;

class Complex {
private:
 float real;
 float imag;

public:
 Complex(float r = 0, float i = 0) : real(r), imag(i) {}

 void display() {
 cout << real << " + " << imag << "i" << endl;
 }

 // Getter functions
 float getReal() const { return real; }
 float getImag() const { return imag; }
};

int main() {
 Complex c1(5.5, 3.2);
 Complex c2(2.1, 4.7);

 cout << "Before assignment:" << endl;
 cout << "c1: ";
 c1.display();
 cout << "c2: ";
 c2.display();

 c2 = c1; // Assignment operation

 cout << "\nAfter assignment:" << endl;
 cout << "c1: ";
 c1.display();
 cout << "c2: ";
 c2.display();

 return 0;
}
```

**Output**:

```
Before assignment:
c1: 5.5 + 3.2i
c2: 2.1 + 4.7i

After assignment:
c1: 5.5 + 3.2i
c2: 5.5 + 3.2i
```

### Example 2: Deep Copy Assignment with Dynamic Memory

**Problem**: Implement a class `String` that manages character arrays and demonstrate proper deep copy assignment.

```cpp
#include <iostream>
#include <cstring>
using namespace std;

class String {
private:
 char* str;
 int length;

public:
 String(const char* s = "") {
 length = strlen(s);
 str = new char[length + 1];
 strcpy(str, s);
 }

 // Copy Constructor (Deep Copy)
 String(const String& s) : length(s.length) {
 str = new char[length + 1];
 strcpy(str, s.str);
 }

 // Assignment Operator (Deep Copy)
 String& operator=(const String& s) {
 if (this != &s) {
 delete[] str;
 length = s.length;
 str = new char[length + 1];
 strcpy(str, s.str);
 }
 return *this;
 }

 void display() {
 cout << str << endl;
 }

 ~String() {
 delete[] str;
 }
};

int main() {
 String s1("Hello World");
 String s2("Temporary");

 cout << "Before assignment:" << endl;
 cout << "s1: ";
 s1.display();
 cout << "s2: ";
 s2.display();

 s2 = s1; // Deep copy assignment

 cout << "\nAfter assignment:" << endl;
 cout << "s1: ";
 s1.display();
 cout << "s2: ";
 s2.display();

 return 0;
}
```

### Example 3: Chained Assignment

**Problem**: Demonstrate that assignment operators can be chained in C++.

```cpp
#include <iostream>
using namespace std;

class Number {
private:
 int value;

public:
 Number(int v = 0) : value(v) {}

 Number& operator=(const Number& n) {
 value = n.value;
 cout << "Assignment performed: " << value << endl;
 return *this; // Enable chaining
 }

 int getValue() const { return value; }
};

int main() {
 Number n1(10), n2(20), n3(30);

 // Chained assignment: right to left
 n3 = n2 = n1;

 cout << "\nFinal values:" << endl;
 cout << "n1: " << n1.getValue() << endl;
 cout << "n2: " << n2.getValue() << endl;
 cout << "n3: " << n3.getValue() << endl;

 return 0;
}
```

**Output**:

```
Assignment performed: 10
Assignment performed: 10

Final values:
n1: 10
n2: 10
n3: 10
```

## Exam Tips

1. **Remember the Rule of Three**: If your class has a custom destructor, you likely need custom copy constructor and assignment operator. This is a frequently examined concept in university exams.

2. **Always check for self-assignment** in overloaded assignment operators to avoid unnecessary work and potential memory corruption.

3. **Distinguish between copy constructor and assignment operator**: Copy constructor creates a new object; assignment operator modifies an existing object.

4. **Understand shallow vs deep copy**: Default operations perform shallow copies, which can cause problems with pointer members.

5. **Return \*this** from assignment operators to enable chained assignments like `a = b = c`.

6. **The assignment operator should return a reference**: This follows the convention and allows chaining.

7. **Always delete old memory before allocating new memory** in assignment operators to prevent memory leaks.

8. **Use initializer list in copy constructor** for better performance when possible.
