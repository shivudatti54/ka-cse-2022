# Friend Functions in C++

## Introduction

Friend functions are a unique feature in C++ that provide a mechanism to access private and protected members of a class from outside the class, while still maintaining the principle of data encapsulation. In object-oriented programming, data hiding is one of the fundamental concepts where the internal data of a class is hidden from outside access. However, there are situations where certain functions or classes need privileged access to private members without breaking the encapsulation principle. This is where friend functions come into play.

The friend mechanism in C++ allows non-member functions or other classes to access private and protected members as if they were part of the class itself. This is particularly useful in operator overloading, implementing friendship between classes, and creating efficient utility functions that need direct access to class internals. It is important to note that friendship in C++ is not transitive, not inherited, and not mutual unless explicitly granted.

## Key Concepts

### Declaration of Friend Functions

A friend function is declared using the keyword 'friend' inside the class definition, but it is not a member function of the class. The friend function can be defined either inside the class or outside, but it must be declared with the friend keyword in the class whose private members it needs to access.

```cpp
class Box {
private:
 double width;
public:
 double length;
 friend void displayWidth(Box b); // Friend function declaration
};
```

### Characteristics of Friend Functions

1. A friend function is not a member of the class, so it cannot be called using the object dot operator.
2. It can be declared in the private or public section of the class without affecting its functionality.
3. It has access to all private and protected members of the class.
4. It can be a friend to multiple classes.
5. It does not have a 'this' pointer since it is not a member function.

### Friend Function vs Member Function

A key distinction exists between member functions and friend functions in C++. Member functions are called using the object of the class with the dot operator, while friend functions are regular functions that receive objects as arguments. Member functions have a 'this' pointer automatically, but friend functions do not have one. Additionally, only member functions can be declared as virtual in C++, whereas friend functions cannot be virtual. Friend functions can directly access private data without getters, whereas member functions must use the object to access them.

### Friend Classes

When one class wants to grant access to all its private and protected members to another class, it declares the second class as a friend class. This gives all member functions of the friend class access to the private members of the first class.

```cpp
class A {
 friend class B; // B is a friend class of A
private:
 int x;
};
```

In this example, all member functions of class B can access the private member 'x' of class A. However, this friendship is not mutual unless explicitly stated.

### Friend Function with Multiple Classes

A single function can be declared as a friend to multiple classes. This is particularly useful when we need to perform operations that involve data from different classes.

```cpp
class B; // Forward declaration

class A {
 int a;
public:
 friend void add(A, B);
};

class B {
 int b;
public:
 friend void add(A, B);
};

void add(A obj1, B obj2) {
 cout << "Sum: " << obj1.a + obj2.b;
}
```

## Examples

### Example 1: Basic Friend Function

Consider a program where we want to display the width of a box using a friend function.

```cpp
#include <iostream>
using namespace std;

class Box {
private:
 double width;
public:
 Box() : width(5.0) {} // Constructor
 friend void displayWidth(Box b); // Friend function declaration
};

void displayWidth(Box b) {
 // Can access private member width directly
 cout << "Width of box: " << b.width << endl;
}

int main() {
 Box b;
 displayWidth(b); // Calling friend function
 return 0;
}
```

**Output:**
Width of box: 5

### Example 2: Friend Function for Operator Overloading

Adding two complex numbers using a friend function:

```cpp
#include <iostream>
using namespace std;

class Complex {
private:
 int real, imag;
public:
 Complex(int r = 0, int i = 0) : real(r), imag(i) {}

 // Friend function for operator overloading
 friend Complex operator+(Complex c1, Complex c2);

 void display() {
 cout << real << " + " << imag << "i" << endl;
 }
};

Complex operator+(Complex c1, Complex c2) {
 Complex temp;
 temp.real = c1.real + c2.real;
 temp.imag = c1.imag + c2.imag;
 return temp;
}

int main() {
 Complex c1(3, 4), c2(5, 6), c3;
 c3 = c1 + c2; // Uses overloaded + operator
 c3.display();
 return 0;
}
```

**Output:**
8 + 10i

### Example 3: Friend Class

Creating a friend class to access private members:

```cpp
#include <iostream>
using namespace std;

class Student {
private:
 string name;
 int marks;
public:
 Student(string n, int m) : name(n), marks(m) {}
 friend class Result; // Result is a friend class
};

class Result {
public:
 void display(Student s) {
 cout << "Name: " << s.name << endl;
 cout << "Marks: " << s.marks << endl;
 }
};

int main() {
 Student s("John", 85);
 Result r;
 r.display(s);
 return 0;
}
```

**Output:**
Name: John
Marks: 85

## Exam Tips

1. Remember that friend functions are declared with the 'friend' keyword inside the class but are not member functions.
2. Friendship is not transitive - if A is friend of B and B is friend of C, A is not automatically friend of C.
3. Friendship is not inherited - derived classes do not inherit friendship.
4. A friend function can access private and protected members directly using the dot operator.
5. Friend functions are useful for operator overloading, especially when the left operand is not an object of the class.
6. The friend keyword can be used to declare an entire class as a friend using 'friend class ClassName'.
7. A function can be a friend to multiple classes, useful for operations involving multiple classes.
8. Friend functions do not have a 'this' pointer since they are not members of the class.
9. In university exams, questions often ask to differentiate between member functions and friend functions.
10. Always remember to use forward declaration when two classes need to be friends with each other.
