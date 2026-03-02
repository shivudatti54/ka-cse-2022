# Friend Classes in C++

## Introduction

In object-oriented programming, encapsulation is one of the fundamental pillars that promotes data hiding and information abstraction. C++ provides access specifiers (private, protected, and public) to control the visibility of class members. However, in certain scenarios, we need to grant special access to another class or function without violating the entire encapsulation model. This is where the **friend** mechanism in C++ becomes essential.

Friend classes and friend functions provide a controlled way to allow external entities to access private and protected members of a class. While traditional OOP principles emphasize strict encapsulation, the friend feature acknowledges that in real-world applications, certain classes are so closely related that they need to share implementation details. The friend mechanism in C++ was introduced to handle such scenarios elegantly, providing a balance between data hiding and practical programming needs.

This topic is crucial for CSE students as it forms the foundation for understanding advanced C++ concepts and design patterns. Friend classes are frequently used in implementing operator overloading, visitor patterns, and relationships between tightly coupled classes. Understanding when and how to use friend classes appropriately is essential for writing maintainable and efficient C++ code.

## Key Concepts

### 1. Declaration of Friend Classes

A friend class is declared using the `friend` keyword within another class. When class A declares class B as its friend, class B can access all private and protected members of class A. However, this access is not reciprocal unless class A also declares class B as its friend.

The syntax for declaring a friend class is:

```cpp
class ClassA {
 friend class ClassB; // ClassB can access private members of ClassA
private:
 int privateData;
protected:
 int protectedData;
public:
 ClassA() : privateData(0), protectedData(0) {}
};

class ClassB {
public:
 void accessClassA(ClassA& obj) {
 obj.privateData = 100; // Allowed - ClassB is a friend
 obj.protectedData = 200; // Allowed - ClassB is a friend
 }
};
```

### 2. Properties of Friend Classes

**Unidirectional Access**: The friend relationship is not mutual by default. If class A declares class B as a friend, only class B can access class A's private members, not vice versa.

**Non-Transitive**: Friendship is not inherited. If class A is a friend of class B, and class C inherits from class B, class C does not automatically become a friend of class A.

**Non-Symmetric**: If class A declares class B as a friend, it does not mean class B automatically considers class A as a friend. Friendship must be explicitly granted.

### 3. Friend Member Functions

Sometimes, we don't want to grant access to an entire class but only to specific member functions of another class. This is achieved by declaring specific member functions as friends:

```cpp
class Rectangle {
 friend void displayDimensions(const Rectangle& r);
private:
 double length;
 double width;
public:
 Rectangle(double l, double w) : length(l), width(w) {}
};

void displayDimensions(const Rectangle& r) {
 cout << "Length: " << r.length << endl; // Accessing private member
 cout << "Width: " << r.width << endl; // Accessing private member
}
```

### 4. Friend Function with Multiple Classes

A single function can be a friend to multiple classes. This is particularly useful when implementing operators that work with objects of different classes:

```cpp
class Matrix;

class Vector {
 int v[3];
public:
 Vector() { v[0] = v[1] = v[2] = 0; }
 Vector(int a, int b, int c) { v[0] = a; v[1] = b; v[2] = c; }
 friend int dotProduct(const Vector&, const Matrix&);
};

class Matrix {
 int m[3][3];
public:
 Matrix() { for(int i=0; i<3; i++) for(int j=0; j<3; j++) m[i][j] = 0; }
 Matrix(int arr[3][3]) { for(int i=0; i<3; i++) for(int j=0; j<3; j++) m[i][j] = arr[i][j]; }
 friend int dotProduct(const Vector&, const Matrix&);
};

int dotProduct(const Vector& vec, const Matrix& mat) {
 int result = 0;
 for(int i = 0; i < 3; i++) {
 result += vec.v[i] * mat.m[i][i]; // Accessing private members
 }
 return result;
}
```

### 5. Friend Classes and Operator Overloading

Friend classes are extensively used in operator overloading, especially for operators that need access to private members of multiple classes:

```cpp
class Complex {
 double real, imag;
public:
 Complex(double r = 0, double i = 0) : real(r), imag(i) {}

 friend class Calculator;
};

class Calculator {
public:
 Complex add(const Complex& c1, const Complex& c2) {
 return Complex(c1.real + c2.real, c1.imag + c2.imag);
 }

 Complex multiply(const Complex& c1, const Complex& c2) {
 return Complex(c1.real * c2.real - c1.imag * c2.imag,
 c1.real * c2.imag + c1.imag * c2.real);
 }
};
```

## Examples

### Example 1: Bank Account System

Consider a scenario where we have a `BankAccount` class and a `Transaction` class. The transaction class needs to modify the balance of bank accounts:

```cpp
#include <iostream>
using namespace std;

class BankAccount {
 string accountNumber;
 double balance;
public:
 BankAccount(string accNo, double bal) : accountNumber(accNo), balance(bal) {}

 void display() const {
 cout << "Account: " << accountNumber << ", Balance: $" << balance << endl;
 }

 friend class Transaction;
};

class Transaction {
public:
 void deposit(BankAccount& account, double amount) {
 if (amount > 0) {
 account.balance += amount; // Accessing private member
 cout << "Deposited $" << amount << endl;
 }
 }

 void withdraw(BankAccount& account, double amount) {
 if (amount > 0 && account.balance >= amount) {
 account.balance -= amount; // Accessing private member
 cout << "Withdrew $" << amount << endl;
 }
 }

 void transfer(BankAccount& from, BankAccount& to, double amount) {
 if (from.balance >= amount) {
 from.balance -= amount;
 to.balance += amount;
 cout << "Transferred $" << amount << endl;
 }
 }
};

int main() {
 BankAccount acc1("ACC001", 1000), acc2("ACC002", 500);
 Transaction t;

 acc1.display();
 acc2.display();

 t.deposit(acc1, 500);
 t.withdraw(acc1, 200);
 t.transfer(acc1, acc2, 300);

 acc1.display();
 acc2.display();

 return 0;
}
```

**Output**:

```
Account: ACC001, Balance: $1000
Account: ACC002, Balance: $500
Deposited $500
Withdrew $200
Transferred $300
Account: ACC001, Balance: $1000
Account: ACC002, Balance: $800
```

### Example 2: Stack and Queue Implementation

Let's implement a scenario where a `Queue` class needs to access private members of a `Stack` class to implement certain operations:

```cpp
#include <iostream>
using namespace std;

const int MAX = 5;

class Stack {
 int arr[MAX];
 int top;
public:
 Stack() : top(-1) {}

 void push(int value) {
 if (top < MAX - 1) {
 arr[++top] = value;
 }
 }

 int pop() {
 if (top >= 0) {
 return arr[top--];
 }
 return -1;
 }

 bool isEmpty() const { return top == -1; }
 bool isFull() const { return top == MAX - 1; }

 // Allow Queue to access private members
 friend class Queue;
};

class Queue {
 int arr[MAX];
 int front, rear;
public:
 Queue() : front(0), rear(-1) {}

 void enqueue(int value) {
 if (rear < MAX - 1) {
 arr[++rear] = value;
 }
 }

 int dequeue() {
 if (front <= rear) {
 return arr[front++];
 }
 return -1;
 }

 // Convert queue to stack using friend's access
 void convertToStack(Stack& s) {
 while (!s.isFull() && front <= rear) {
 s.push(arr[front++]);
 }
 }

 void display() const {
 for (int i = front; i <= rear; i++) {
 cout << arr[i] << " ";
 }
 cout << endl;
 }
};

int main() {
 Stack s;
 Queue q;

 q.enqueue(10);
 q.enqueue(20);
 q.enqueue(30);

 cout << "Queue: ";
 q.display();

 q.convertToStack(s);
 cout << "Stack from queue: ";
 while (!s.isEmpty()) {
 cout << s.pop() << " ";
 }
 cout << endl;

 return 0;
}
```

## Exam Tips

1. **Remember the syntax**: The `friend` keyword must be used inside the class that is granting access, followed by the class or function name.

2. **Understand unidirectional nature**: In exams, frequently asked questions test whether students understand that friendship is not mutual unless explicitly declared both ways.

3. **Friend functions vs Friend classes**: Know when to use each - friend functions are suitable for operators or specific functions, while friend classes are used when many functions need access.

4. **Encapsulation trade-off**: Be prepared to answer questions about when to use friend classes and the trade-offs involved between encapsulation and practicality.

5. **Common declarations**: Memorize the syntax for declaring friend classes, friend member functions, and friend global functions.

6. **Design patterns**: Friend classes are used in implemention of design patterns like Factory, Visitor, and Singleton. Understanding these helps in application-based questions.

7. **Code tracing**: Practice tracing code that uses friend classes to determine output and access privileges.

8. **Declaration order**: Remember that when Class A needs to declare Class B as a friend, Class B must be declared before Class A (forward declaration may be needed).
