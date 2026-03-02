# Base Class Access Control in C++

## Introduction

In Object-Oriented Programming with C++, inheritance is a fundamental mechanism that allows a new class (derived class) to inherit properties and behaviors from an existing class (base class). However, C++ provides sophisticated access control mechanisms that determine how members of a base class are accessible to the derived class and to the outside world. Understanding base class access control is crucial for designing robust class hierarchies and implementing proper encapsulation.

The access control system in C++ distinguishes between three access specifiers: **private**, **protected**, and **public**. Each specifier defines a different level of visibility and accessibility for class members. When inheritance is involved, the type of inheritance (public, private, or protected) further modifies how base class members are accessible in the derived class. This topic forms a critical component of the the syllabus for Object-Oriented Programming with C++ and frequently appears in university examinations.

## Key Concepts

### 1. Access Specifiers in Classes

**Private Members:**

- Accessible only within the same class
- Not accessible to derived classes or outside functions
- Used for internal implementation details that should be hidden

**Protected Members:**

- Accessible within the same class
- Accessible to derived classes
- Not accessible to outside functions or objects
- Provides a middle ground between private and public

**Public Members:**

- Accessible everywhere - within the class, to derived classes, and outside the class
- Form the external interface of the class

### 2. Types of Inheritance

When a class inherits from a base class, the inheritance can be of three types:

**Public Inheritance:**

```cpp
class Base {
public:
 int publicVar;
protected:
 int protectedVar;
private:
 int privateVar;
};

class Derived : public Base {
 // publicVar becomes public
 // protectedVar becomes protected
 // privateVar is not accessible
};
```

In public inheritance:

- Public members of Base become public in Derived
- Protected members of Base become protected in Derived
- Private members of Base remain private (inaccessible directly)

**Protected Inheritance:**

```cpp
class Derived : protected Base {
 // publicVar becomes protected
 // protectedVar becomes protected
 // privateVar is not accessible
};
```

In protected inheritance:

- Public and protected members of Base become protected in Derived
- The outside world cannot access any inherited members

**Private Inheritance:**

```cpp
class Derived : private Base {
 // publicVar becomes private
 // protectedVar becomes private
 // privateVar is not accessible
};
```

In private inheritance:

- All inherited members become private in Derived
- Derived class acts as if Base is an implementation detail

### 3. Access Control and Member Visibility

| Base Class Member | Public Derivation | Protected Derivation | Private Derivation |
| ----------------- | ----------------- | -------------------- | ------------------ |
| Public            | Public            | Protected            | Private            |
| Protected         | Protected         | Protected            | Private            |
| Private           | Inaccessible      | Inaccessible         | Inaccessible       |

### 4. Using 'using' Declaration

C++ allows modifying access levels in derived classes using the 'using' declaration:

```cpp
class Base {
public:
 int x;
protected:
 int y;
};

class Derived : private Base {
public:
 using Base::x; // x becomes public
protected:
 using Base::y; // y becomes protected
};
```

### 5. Constructors and Destructors in Inheritance

- Base class constructors are called before derived class constructors
- Destructors are called in reverse order (derived first, then base)
- Derived class constructors can call base class constructors
- Access specifiers affect which constructors are callable

### 6. Multiple Inheritance and Access Control

In multiple inheritance, each base class can have different access specifiers:

```cpp
class A { public: int a; };
class B { public: int b; };

class C : public A, public B {
 // Both a and b are public
};
```

## Examples

### Example 1: Public Inheritance

```cpp
#include <iostream>
using namespace std;

class Vehicle {
public:
 int wheels;
 void display() {
 cout << "Vehicle with " << wheels << " wheels" << endl;
 }
protected:
 int speed;
 void setSpeed(int s) { speed = s; }
private:
 int fuelLevel;
};

class Car : public Vehicle {
public:
 void carFunction() {
 wheels = 4; // OK: public in derived
 display(); // OK: public function accessible
 setSpeed(60); // OK: protected function accessible
 // fuelLevel = 50; // ERROR: private not accessible
 }
};

int main() {
 Car c;
 c.wheels = 4; // OK: public
 c.display(); // OK: public
 // c.setSpeed(60); // ERROR: protected not accessible
 return 0;
}
```

### Example 2: Protected Inheritance

```cpp
#include <iostream>
using namespace std;

class BankAccount {
public:
 void deposit(int amount) { balance += amount; }
protected:
 int balance = 1000;
private:
 int accountNumber;
};

class SavingsAccount : protected BankAccount {
public:
 void withdraw(int amount) {
 if (balance >= amount)
 balance -= amount;
 }
 void showBalance() {
 cout << "Balance: " << balance << endl;
 }
 // deposit() becomes protected - not accessible outside
};

int main() {
 SavingsAccount sa;
 // sa.deposit(500); // ERROR: deposit is protected now
 // sa.balance // ERROR: balance is protected
 sa.withdraw(200); // OK: public function
 sa.showBalance(); // OK: public function
 return 0;
}
```

### Example 3: Private Inheritance

```cpp
#include <iostream>
using namespace std;

class Person {
public:
 string name;
protected:
 int age;
private:
 int salary;
};

class Employee : private Person {
public:
 void setData(string n, int a) {
 name = n; // OK: name becomes private, accessible here
 age = a; // OK: age becomes private, accessible here
 // salary = 50000; // ERROR: never accessible
 }
 void display() {
 cout << "Name: " << name << ", Age: " << age << endl;
 }
};

int main() {
 Employee emp;
 emp.setData("John", 25);
 emp.display();
 // emp.name = "Mike"; // ERROR: name is private in Employee
 // emp.age = 30; // ERROR: age is private in Employee
 return 0;
}
```

## Exam Tips

1. **Remember the Access Specifier Hierarchy**: Public > Protected > Private. When in doubt, the more restrictive access specifier applies.

2. **Key Difference**: Protected members are accessible in derived classes but not outside, while private members are never accessible in derived classes.

3. **Inheritance Type Effect**: Public inheritance keeps the access levels, protected reduces public to protected, private reduces everything to private.

4. **Common Mistake**: Students often think private members become accessible in derived classes - they do not. Only protected and public members are accessible.

5. **Constructor Call Order**: In multiple inheritance, base class constructors are called in the order of declaration, not in the order in the initializer list.

6. **Virtual Functions and Access Control**: A derived class can override a virtual function but cannot increase its visibility (cannot make a protected virtual function public in derived class).

7. **Diamond Problem**: In multiple inheritance with shared base class, virtual inheritance solves ambiguity but access control still applies to the virtually inherited base.

8. **Slicing**: When a derived class object is assigned to a base class object, only the base portion is copied - this is called slicing and is different from polymorphism using pointers/references.

9. **Use 'using' Declaration**: Remember this technique to restore or change access levels of inherited members in derived classes.

10. **university Exam Pattern**: Expect questions on determining the type of access (public/protected/private) for members after inheritance, and coding questions on implementing specific inheritance types.
