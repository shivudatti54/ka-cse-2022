# Passing Objects to Functions in C++

## Introduction

In object-oriented programming with C++, one of the most fundamental and frequently used concepts is passing objects to functions. This mechanism allows functions to operate on class objects, enabling data encapsulation, code reusability, and efficient memory management. Understanding how objects are passed to functions is crucial for writing efficient and maintainable C++ programs, and this topic forms a foundational concept in the BCS306B syllabus.

When we pass objects to functions in C++, we have multiple mechanisms available: pass by value, pass by reference, and pass by pointer. Each method has its own implications for performance, data integrity, and functionality. The choice of passing mechanism affects whether a copy of the object is made, whether modifications to the object inside the function affect the original object, and how memory is managed during function calls.

In real-world C++ applications, passing objects to functions is ubiquitous. Consider a scenario where you have a `Student` class with attributes like name, USN, and marks. You might need to create functions to calculate grades, display student information, or validate marks. Each of these operations requires passing Student objects to functions. The way you choose to pass these objects determines the efficiency and correctness of your program.

This module explores all three methods of passing objects, their advantages, disadvantages, and appropriate use cases. We will also discuss important considerations such as const correctness and the implications of copy constructors when passing objects by value.

## Key Concepts

### 1. Pass by Value

When an object is passed by value to a function, a copy of the object is created using the copy constructor. The function works with this copy, and any modifications made to the object inside the function do not affect the original object. This provides complete isolation between the original object and the function's local copy.

The syntax for pass by value is straightforward: you simply specify the object type and parameter name in the function declaration. For example:

```cpp
void displayStudent(Student s) {
 s.display();
}
```

In this case, when `displayStudent` is called with a Student object, the copy constructor is invoked to create a new Student object. This process involves copying all member variables from the original object to the new object. If the class contains pointers or dynamically allocated memory, you need to be careful about shallow versus deep copying.

The advantages of pass by value include complete isolation, which prevents unintended modifications to the original object. However, the disadvantages are significant: the copy constructor is called, which can be expensive for large objects, and additional memory is consumed for the copy.

### 2. Pass by Reference

Passing objects by reference means the function receives a reference (alias) to the original object rather than a copy. No copy is made, and any modifications to the object inside the function affect the original object directly. This is achieved using the reference operator (&) in the parameter declaration.

```cpp
void updateMarks(Student &s, int newMarks) {
 s.setMarks(newMarks);
}
```

The advantages of pass by reference are efficiency (no copy is made) and the ability to modify the original object. However, you must be careful about unintended modifications. If you want to allow reading but not modifying the object, you should use const reference, discussed in the next section.

Pass by reference is particularly useful when you need to modify multiple member variables of an object or when you want to avoid the overhead of copying large objects. In competitive programming and university exams, pass by reference is often the preferred method for passing large objects to functions.

### 3. Pass by Pointer

Passing objects by pointer involves passing the memory address of the object. The function receives a pointer to the original object and can modify it through dereferencing. This method provides explicit control over memory addresses and is useful in scenarios involving dynamic memory allocation or when NULL values need to be handled.

```cpp
void updateMarks(Student *s, int newMarks) {
 if (s != NULL) {
 s->setMarks(newMarks);
 }
}
```

The advantages of pass by pointer include the ability to pass NULL (indicating no valid object), explicit memory address manipulation, and compatibility with C-style code. The disadvantages include the need for NULL checks, the use of pointer syntax (-> operator), and the potential for dangling pointers if not handled carefully.

### 4. Const Correctness

Const correctness is an essential concept when passing objects to functions. Using `const` with reference parameters ensures that the function cannot modify the object. This provides both safety and optimization opportunities for the compiler.

```cpp
void displayStudent(const Student &s) {
 // s.setMarks(100); // This would cause a compilation error
 s.display(); // Only const member functions can be called
}
```

The `const` keyword before the reference parameter tells the compiler that the function promises not to modify the object. This allows the compiler to make optimizations and also serves as documentation for other developers. Any attempt to modify the object inside the function will result in a compilation error.

For pass-by-value parameters, const is not typically used since a copy is being made anyway. However, const can be used with pointers in two ways: `const Student*` (pointer to const) and `Student* const` (const pointer to Student).

### 5. Returning Objects from Functions

Similar to passing objects, functions can also return objects by value, by reference, or by pointer. Each method has specific use cases and potential pitfalls.

When returning by value, a copy of the object is returned (or move semantics may apply in C++11 and later). Returning by reference is efficient but you must ensure the object being referenced continues to exist after the function returns. Returning by pointer requires careful management to avoid memory leaks.

```cpp
// Return by value
Student createStudent(string name, string usn) {
 Student s(name, usn);
 return s; // Returns a copy (or uses move constructor)
}

// Return by reference (use with caution)
Student& getStudent() {
 static Student s("John", "1BT22CS001");
 return s; // Returns reference to static object
}

// Return by pointer
Student* createNewStudent(string name, string usn) {
 Student *s = new Student(name, usn);
 return s; // Caller responsible for deletion
}
```

### 6. Copy Constructor and Pass by Value

When objects are passed by value, the copy constructor is invoked to create a copy. If the copy constructor is not explicitly defined, the compiler generates a default copy constructor that performs member-wise copy (shallow copy). For classes with pointer members, this can lead to problems like double deletion or shared state between objects.

In university exams, you should understand when the copy constructor is called:

- When an object is passed by value to a function
- When an object is returned by value from a function
- When an object is created from another object of the same class

## Examples

### Example 1: Pass by Value

```cpp
#include <iostream>
#include <string>
using namespace std;

class Rectangle {
private:
 int length, breadth;
public:
 Rectangle(int l = 0, int b = 0) {
 length = l;
 breadth = b;
 }

 void setDimensions(int l, int b) {
 length = l;
 breadth = b;
 }

 int area() {
 return length * breadth;
 }

 void display() {
 cout << "Length: " << length << ", Breadth: " << breadth << endl;
 }
};

void displayArea(Rectangle r) {
 // r is a copy of the original Rectangle
 cout << "Area inside function: " << r.area() << endl;
 r.setDimensions(100, 100); // Only modifies the copy
 cout << "Modified copy area: " << r.area() << endl;
}

int main() {
 Rectangle rect(10, 5);
 cout << "Original rectangle: ";
 rect.display();

 displayArea(rect);

 cout << "Original after function call: ";
 rect.display(); // Still 10x5, not affected

 return 0;
}
```

**Output:**

```
Original rectangle: Length: 10, Breadth: 5
Area inside function: 50
Modified copy area: 10000
Original after function call: Length: 10, Breadth: 5
```

This example demonstrates that pass by value creates a copy, and modifications to the copy do not affect the original object.

### Example 2: Pass by Reference

```cpp
#include <iostream>
using namespace std;

class Counter {
private:
 int count;
public:
 Counter(int c = 0) {
 count = c;
 }

 void increment() {
 count++;
 }

 int getCount() {
 return count;
 }

 void display() {
 cout << "Count: " << count << endl;
 }
};

void incrementCounter(Counter &c) {
 c.increment();
 c.increment();
 c.increment(); // Increments 3 times
}

int main() {
 Counter c(10);
 cout << "Before: ";
 c.display();

 incrementCounter(c); // Pass by reference

 cout << "After: ";
 c.display(); // Count is now 13

 return 0;
}
```

**Output:**

```
Before: Count: 10
After: Count: 13
```

This example shows that pass by reference allows the function to modify the original object directly.

### Example 3: Const Reference with Display Function

```cpp
#include <iostream>
#include <string>
using namespace std;

class BankAccount {
private:
 string accountHolder;
 string accountNumber;
 double balance;
public:
 BankAccount(string holder, string number, double bal) {
 accountHolder = holder;
 accountNumber = number;
 balance = bal;
 }

 // Const member function - can be called on const objects
 void display() const {
 cout << "Account Holder: " << accountHolder << endl;
 cout << "Account Number: " << accountNumber << endl;
 cout << "Balance: Rs. " << balance << endl;
 }

 void deposit(double amount) {
 balance += amount;
 }

 double getBalance() const {
 return balance;
 }
};

void printAccountDetails(const BankAccount &acc) {
 // Cannot modify acc - it's const
 // acc.deposit(1000); // Error!
 acc.display(); // OK - display() is const
}

int main() {
 BankAccount account("John Doe", "SBIN0012345", 50000);

 cout << "Account Details:" << endl;
 printAccountDetails(account);

 return 0;
}
```

**Output:**

```
Account Details:
Account Holder: John Doe
Account Number: SBIN0012345
Balance: Rs. 50000
```

This example demonstrates const correctness: the function receives a const reference and can only call const member functions on the object.

## Exam Tips

1. **Understand the difference between pass by value, reference, and pointer**: This is frequently tested in university exams. Remember that pass by value creates a copy, pass by reference uses the original object, and pass by pointer passes the address.

2. **Remember when copy constructor is called**: The copy constructor is invoked when objects are passed by value to functions, returned by value, or initialized from another object.

3. **Use const reference for read-only parameters**: When a function only needs to read an object without modifying it, always pass by const reference for efficiency and safety.

4. **Know the syntax differences**: Pass by value uses simple type name, pass by reference uses (&), and pass by pointer uses (\*).

5. **Remember const member functions**: When using const reference parameters, you can only call const member functions on the object.

6. **Understand the implications of modifications**: Pass by value protects the original, pass by reference/pointer allows modification. Choose based on whether you need to modify the object.

7. **Avoid returning references to local variables**: This creates dangling references and is undefined behavior. Remember that local variables are destroyed when the function returns.

8. **Pointer vs Reference**: Use pointers when you need to pass NULL or do arithmetic, use references for simple aliasing. References cannot be null and must be initialized.
