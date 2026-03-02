# Parameterized Constructors in C++

## Introduction

Parameterized constructors are a fundamental concept in object-oriented programming with C++. They represent a special member function of a class that is automatically invoked when an object is created, with the ability to accept arguments for initializing data members. Unlike default constructors that take no parameters, parameterized constructors provide flexibility in initializing objects with specific values at the time of instantiation.

In the context of the university's BCS306B Object Oriented Programming with C++ curriculum, parameterized constructors form the backbone of proper object initialization. They enable encapsulation by ensuring that objects are always created in a valid state. The ability to pass initial values during object creation eliminates the need for separate setter functions in many scenarios, leading to cleaner and more maintainable code. Understanding parameterized constructors is essential for implementing classes that model real-world entities effectively.

This topic builds upon the basic understanding of classes and objects, introducing the mechanism through which programmers can control how objects are initialized. The concept becomes particularly important when dealing with complex data structures, resource allocation, and establishing invariants within classes.

## Key Concepts

### Definition and Syntax of Parameterized Constructors

A parameterized constructor is a constructor that accepts one or more parameters. The syntax follows the same rules as regular member functions, with the constructor having the same name as the class and no return type (not even void).

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
};
```

The constructor is invoked automatically when an object is created with arguments:

```cpp
Rectangle r1(10, 5); // Calls Rectangle(int, int)
```

### Constructor Overloading

C++ supports constructor overloading, meaning a class can have multiple constructors with different parameter lists. This provides flexibility in object creation, allowing users to initialize objects in various ways.

```cpp
class Box {
private:
 int width, height, depth;
public:
 // Default constructor
 Box() {
 width = height = depth = 1;
 }

 // Parameterized constructor with one parameter (cube)
 Box(int side) {
 width = height = depth = side;
 }

 // Parameterized constructor with three parameters
 Box(int w, int h, int d) {
 width = w;
 height = h;
 depth = d;
 }

 void display() {
 cout << "Dimensions: " << width << " x " << height << " x " << depth << endl;
 }
};
```

The compiler differentiates between overloaded constructors based on the number and types of arguments passed during object creation.

### Default Arguments in Constructors

Parameterized constructors can use default argument values, which simplifies object creation by allowing fewer arguments to be specified.

```cpp
class Employee {
private:
 string name;
 int salary;
 string department;
public:
 Employee(string n, int s = 50000, string d = "IT") {
 name = n;
 salary = s;
 department = d;
 }
 void display() {
 cout << "Name: " << name << ", Salary: " << salary
 << ", Department: " << department << endl;
 }
};

// Usage
Employee e1("John"); // Uses default salary and department
Employee e2("Alice", 75000); // Uses default department
Employee e3("Bob", 60000, "HR"); // Uses all provided values
```

### Initialization Lists

Constructor initialization lists provide a more efficient way to initialize data members, especially for const members and references. This is the preferred method in C++ for initializing members.

```cpp
class Point {
private:
 const int x, y; // const members must be initialized
 int &ref; // reference must be initialized
public:
 // Using initialization list
 Point(int a, int b, int &r) : x(a), y(b), ref(r) {
 // Constructor body can be empty
 }
};
```

The initialization list is more efficient because it directly initializes members rather than default-initializing them first and then assigning values.

### Copy Constructors

A copy constructor is a special parameterized constructor that takes a reference to another object of the same class as its parameter. It is used to create a new object as a copy of an existing object.

```cpp
class String {
private:
 char *str;
 int length;
public:
 // Parameterized constructor
 String(const char *s) {
 length = strlen(s);
 str = new char[length + 1];
 strcpy(str, s);
 }

 // Copy constructor
 String(const String &s) {
 length = s.length;
 str = new char[length + 1];
 strcpy(str, s.str);
 }

 void display() {
 cout << str << endl;
 }
};
```

The copy constructor is called in the following scenarios:

- When an object is initialized with another object of the same class
- When an object is passed by value to a function
- When an object is returned by value from a function

### Explicit Constructors

The `explicit` keyword prevents implicit conversions and copy initialization, which can sometimes lead to unexpected behavior.

```cpp
class Stack {
private:
 int size;
public:
 explicit Stack(int s) {
 size = s;
 }
};

// Stack s1 = 10; // Error: implicit conversion not allowed
Stack s2(10); // OK: direct initialization
Stack s3{10}; // OK: list initialization
```

## Examples

### Example 1: Bank Account Class

**Problem:** Create a BankAccount class with parameterized constructor to initialize account holder name and initial balance.

```cpp
#include <iostream>
#include <string>
using namespace std;

class BankAccount {
private:
 string holderName;
 double balance;
 int accountNumber;
 static int nextAccNo;
public:
 // Parameterized constructor
 BankAccount(string name, double initialBalance) {
 holderName = name;
 balance = initialBalance;
 accountNumber = nextAccNo++;
 }

 void deposit(double amount) {
 if (amount > 0) {
 balance += amount;
 cout << "Deposited: " << amount << endl;
 } else {
 cout << "Invalid amount!" << endl;
 }
 }

 void withdraw(double amount) {
 if (amount > 0 && amount <= balance) {
 balance -= amount;
 cout << "Withdrawn: " << amount << endl;
 } else {
 cout << "Insufficient funds or invalid amount!" << endl;
 }
 }

 void display() {
 cout << "Account Number: " << accountNumber << endl;
 cout << "Holder Name: " << holderName << endl;
 cout << "Balance: Rs. " << balance << endl;
 }
};

int BankAccount::nextAccNo = 1001;

int main() {
 BankAccount acc1("John Doe", 5000);
 BankAccount acc2("Jane Smith", 10000);

 cout << "=== Account 1 ===" << endl;
 acc1.display();
 acc1.deposit(2000);
 acc1.withdraw(1500);
 acc1.display();

 cout << "\n=== Account 2 ===" << endl;
 acc2.display();

 return 0;
}
```

**Output:**

```
=== Account 1 ===
Account Number: 1001
Holder Name: John Doe
Balance: Rs. 5000
Deposited: 2000
Withdrawn: 1500
Account Number: 1001
Holder Name: John Doe
Balance: Rs. 5500

=== Account 2 ===
Account Number: 1002
Holder Name: Jane Smith
Balance: Rs. 10000
```

### Example 2: Constructor Overloading

**Problem:** Implement a Complex class demonstrating constructor overloading.

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

 // Parameterized constructor with one parameter (real only)
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
 if (imag >= 0)
 cout << real << " + " << imag << "i" << endl;
 else
 cout << real << " - " << -imag << "i" << endl;
 }
};

int main() {
 Complex c1; // Calls default constructor
 Complex c2(5); // Calls Complex(int)
 Complex c3(3, 4); // Calls Complex(int, int)
 Complex c4 = 7; // Calls Complex(int)

 cout << "c1 = ";
 c1.display();

 cout << "c2 = ";
 c2.display();

 cout << "c3 = ";
 c3.display();

 cout << "c4 = ";
 c4.display();

 return 0;
}
```

**Output:**

```
c1 = 0 + 0i
c2 = 5 + 0i
c3 = 3 + 4i
c4 = 7 + 0i
```

### Example 3: Copy Constructor and Deep Copy

**Problem:** Implement a String class with proper deep copy using copy constructor.

```cpp
#include <iostream>
#include <string.h>
using namespace std;

class String {
private:
 char *str;
 int len;
public:
 // Parameterized constructor
 String(const char *s) {
 len = strlen(s);
 str = new char[len + 1];
 strcpy(str, s);
 }

 // Copy constructor (Deep Copy)
 String(const String &s) {
 len = s.len;
 str = new char[len + 1];
 strcpy(str, s.str);
 cout << "Copy constructor called" << endl;
 }

 // Destructor
 ~String() {
 delete[] str;
 }

 void display() {
 cout << str << endl;
 }

 // Concatenation function
 String concat(String &s) {
 char *temp = new char[len + s.len + 1];
 strcpy(temp, str);
 strcat(temp, s.str);
 String result(temp);
 delete[] temp;
 return result;
 }
};

int main() {
 String s1("Hello ");
 String s2("World");

 cout << "s1 = ";
 s1.display();

 cout << "s2 = ";
 s2.display();

 cout << "\nCreating s3 using copy constructor:" << endl;
 String s3(s1); // Copy constructor called

 cout << "s3 = ";
 s3.display();

 cout << "\nPassing object to function:" << endl;
 String s4(s2);

 return 0;
}
```

## Exam Tips

1. **Remember constructor characteristics**: Constructors have the same name as the class, no return type, and are automatically invoked during object creation.

2. **Constructor overloading distinguishes by parameter list**: The compiler differentiates overloaded constructors based on the number, type, and order of parameters, not the return type.

3. **Use initialization lists for const and reference members**: Const data members and reference members must be initialized using initialization lists; they cannot be assigned values in the constructor body.

4. **Copy constructor is called in specific scenarios**: Understand when the copy constructor is invoked—when initializing from another object, passing by value, and returning by value.

5. **Default arguments reduce constructor overloads**: Using default arguments in parameterized constructors can reduce the number of constructor definitions needed.

6. **Shallow vs Deep Copy**: In university exams, if a class contains pointer members, always implement a custom copy constructor for deep copy; otherwise, both objects will share the same memory leading to double deletion.

7. **Explicit keyword prevents unintended conversions**: Remember to use explicit for constructors that should not participate in implicit type conversions.

8. **Constructor cannot be virtual**: Unlike member functions, constructors cannot be declared virtual in C++.

9. **Initialization order matters**: Data members are initialized in the order they are declared in the class, not the order in the initialization list. Always match the order to avoid confusion.

10. **Destructors and constructors**: Always pair dynamic memory allocation in constructors with appropriate deallocation in destructors to prevent memory leaks.
