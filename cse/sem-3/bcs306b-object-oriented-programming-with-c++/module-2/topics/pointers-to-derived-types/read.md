# Pointers to Derived Types in C++

## Introduction

Pointers to derived types represent one of the most powerful features of object-oriented programming in C++, enabling runtime polymorphism and dynamic binding. In the context of C++ inheritance hierarchies, pointers serve as the mechanism through which we can achieve polymorphic behavior, allowing a single pointer to refer to objects of different derived classes at runtime.

The concept of pointers to derived types is fundamental to understanding how C++ implements runtime polymorphism. When we create a base class pointer that can point to objects of derived classes, we unlock the ability to write flexible and extensible code. This becomes particularly important in scenarios where we need to work with collections of different object types through a common interface, such as in shape rendering systems, game development, or database management systems.

Understanding the relationship between base class pointers and derived class objects is crucial for every C++ programmer. the university's BCS306b curriculum emphasizes this topic because it forms the foundation for implementing design patterns, creating extensible software architectures, and understanding how modern C++ frameworks operate internally. The proper use of pointers to derived types allows developers to write code that can accommodate new derived classes without modifying existing code, adhering to the Open-Closed Principle of object-oriented design.

## Key Concepts

### Base Class Pointers and Derived Class Objects

In C++, a pointer to a base class can hold the address of any object of its derived classes. This is known as upcasting and is always safe because every derived class object contains a base class subobject. The syntax is straightforward:

```cpp
class Base {
public:
 virtual void display() { cout << "Base display"; }
};

class Derived : public Base {
public:
 void display() override { cout << "Derived display"; }
};

int main() {
 Base* ptr; // Pointer to base class
 Derived obj; // Object of derived class

 ptr = &obj; // Upcasting: derived to base
 ptr->display(); // Calls Derived::display() due to virtual function
}
```

The key insight here is that when a base class pointer points to a derived class object, the pointer can only access members that are declared in the base class, unless virtual functions are involved.

### Type Compatibility and Upcasting

C++ enforces strict type compatibility rules that govern pointer assignments in inheritance hierarchies. The implicit conversion from a derived class pointer to a base class pointer (upcasting) is always safe and does not require any explicit type casting. This is because every derived class "is-a" base class, making the inheritance relationship a type of subtype relationship.

However, the reverse is not true: a base class pointer cannot be implicitly converted to a derived class pointer. This is because the base class object may not contain all the additional members that the derived class defines. Attempting to force such a conversion without proper validation leads to undefined behavior.

### Virtual Functions and Dynamic Binding

The true power of pointers to derived types is realized through virtual functions. When a base class declares a function as virtual, and derived classes override it, the function that gets called depends on the actual type of the object being pointed to, not the pointer type. This mechanism is called dynamic binding or late binding, and it occurs at runtime.

```cpp
class Shape {
public:
 virtual void draw() = 0; // Pure virtual function
 virtual ~Shape() {} // Virtual destructor for proper cleanup
};

class Circle : public Shape {
public:
 void draw() override { cout << "Drawing Circle\n"; }
};

class Rectangle : public Shape {
public:
 void draw() override { cout << "Drawing Rectangle\n"; }
};
```

When we create an array of base class pointers pointing to different derived class objects, each call to `draw()` will invoke the appropriate derived class implementation based on the actual object type.

### Downcasting and Runtime Type Information

Sometimes we need to access derived-class-specific members through a base class pointer. This requires downcasting, which must be done explicitly in C++. The language provides two ways to perform downcasting: static_cast and dynamic_cast.

The dynamic_cast operator is the safer option as it performs runtime type checking. If the cast is invalid (the object is not of the requested type), it returns nullptr (for pointers) or throws an exception (for references).

```cpp
class Base {
public:
 virtual ~Base() = default;
};

class Derived1 : public Base {
public:
 void derived1Method() { cout << "Derived1 specific\n"; }
};

class Derived2 : public Base {
public:
 void derived2Method() { cout << "Derived2 specific\n"; }
};

void process(Base* ptr) {
 // Safe downcasting using dynamic_cast
 Derived1* d1 = dynamic_cast<Derived1*>(ptr);
 if (d1) {
 d1->derived1Method();
 }

 Derived2* d2 = dynamic_cast<Derived2*>(ptr);
 if (d2) {
 d2->derived2Method();
 }
}
```

### Virtual Destructors and Memory Management

One of the most critical aspects of using pointers to derived types is ensuring proper memory cleanup. When deleting a derived class object through a base class pointer, the base class destructor must be virtual. Otherwise, only the base class destructor gets called, leading to resource leaks and undefined behavior.

```cpp
class Base {
public:
 virtual ~Base() {
 cout << "Base destructor\n";
 }
};

class Derived : public Base {
public:
 ~Derived() override {
 cout << "Derived destructor\n";
 }
};

int main() {
 Base* ptr = new Derived();
 delete ptr; // Both destructors called due to virtual destructor
 return 0;
}
```

## Examples

### Example 1: Banking System Implementation

Consider a banking system where we have different account types:

```cpp
class Account {
protected:
 double balance;
public:
 Account(double bal) : balance(bal) {}
 virtual void calculateInterest() = 0;
 virtual void display() {
 cout << "Balance: " << balance << endl;
 }
 virtual ~Account() {}
};

class SavingsAccount : public Account {
private:
 double interestRate;
public:
 SavingsAccount(double bal, double rate) : Account(bal), interestRate(rate) {}

 void calculateInterest() override {
 double interest = balance * interestRate;
 balance += interest;
 cout << "Savings Interest Added: " << interest << endl;
 }
};

class CurrentAccount : public Account {
private:
 double overdraftLimit;
public:
 CurrentAccount(double bal, double limit) : Account(bal), overdraftLimit(limit) {}

 void calculateInterest() override {
 if (balance < 0) {
 double interest = abs(balance) * 0.02;
 balance -= interest;
 cout << "Overdraft Interest Charged: " << interest << endl;
 }
 }
};

int main() {
 Account* accounts[3];

 accounts[0] = new SavingsAccount(10000, 0.05);
 accounts[1] = new CurrentAccount(-5000, 10000);
 accounts[2] = new SavingsAccount(25000, 0.04);

 for (int i = 0; i < 3; i++) {
 accounts[i]->calculateInterest();
 accounts[i]->display();
 cout << "-------------------\n";
 delete accounts[i];
 }

 return 0;
}
```

This example demonstrates how base class pointers enable treating different account types uniformly while still invoking the appropriate interest calculation logic for each type.

### Example 2: Employee Management System

```cpp
class Employee {
protected:
 string name;
 int empId;
public:
 Employee(string n, int id) : name(n), empId(id) {}

 virtual double calculateSalary() = 0;
 virtual void displayDetails() {
 cout << "ID: " << empId << ", Name: " << name << endl;
 }
 virtual ~Employee() {}
};

class Manager : public Employee {
private:
 double baseSalary;
 double bonus;
public:
 Manager(string n, int id, double base, double bon)
 : Employee(n, id), baseSalary(base), bonus(bon) {}

 double calculateSalary() override {
 return baseSalary + bonus;
 }

 void displayDetails() override {
 cout << "Manager - ";
 Employee::displayDetails();
 cout << "Salary: " << calculateSalary() << endl;
 }
};

class Developer : public Employee {
private:
 double hourlyRate;
 int hoursWorked;
public:
 Developer(string n, int id, double rate, int hours)
 : Employee(n, id), hourlyRate(rate), hoursWorked(hours) {}

 double calculateSalary() override {
 return hourlyRate * hoursWorked;
 }

 void displayDetails() override {
 cout << "Developer - ";
 Employee::displayDetails();
 cout << "Salary: " << calculateSalary() << endl;
 }
};

int main() {
 Employee* emp[3];

 emp[0] = new Manager("John", 101, 50000, 10000);
 emp[1] = new Developer("Alice", 102, 500, 160);
 emp[2] = new Manager("Bob", 103, 45000, 8000);

 double totalSalary = 0;
 for (int i = 0; i < 3; i++) {
 emp[i]->displayDetails();
 totalSalary += emp[i]->calculateSalary();
 delete emp[i];
 }

 cout << "Total Salary Expenditure: " << totalSalary << endl;
 return 0;
}
```

### Example 3: Demonstrating Downcasting

```cpp
class Vehicle {
public:
 virtual void start() { cout << "Vehicle starting\n"; }
 virtual ~Vehicle() {}
};

class Car : public Vehicle {
public:
 void start() override { cout << "Car starting with key\n"; }
 void playMusic() { cout << "Playing music\n"; }
};

class Bike : public Vehicle {
public:
 void start() override { cout << "Bike kick-started\n"; }
 void doWheelie() { cout << "Doing wheelie\n"; }
};

void demonstrateDowncast(Vehicle* v) {
 // Attempt to cast to Car
 Car* c = dynamic_cast<Car*>(v);
 if (c) {
 cout << "Vehicle is a Car. ";
 c->playMusic();
 }

 // Attempt to cast to Bike
 Bike* b = dynamic_cast<Bike*>(v);
 if (b) {
 cout << "Vehicle is a Bike. ";
 b->doWheelie();
 }
}

int main() {
 Vehicle* vehicles[3];
 vehicles[0] = new Car();
 vehicles[1] = new Bike();
 vehicles[2] = new Car();

 for (int i = 0; i < 3; i++) {
 demonstrateDowncast(vehicles[i]);
 delete vehicles[i];
 }

 return 0;
}
```

## Exam Tips

1. **Virtual Function Requirement**: Remember that runtime polymorphism through base class pointers only works when the base class function is declared as virtual. Non-virtual functions exhibit static binding.

2. **Pure Virtual Functions**: Classes containing pure virtual functions become abstract classes and cannot be instantiated directly. However, pointers to abstract classes can still be created.

3. **Virtual Destructor Rule**: Always make base class destructors virtual when the class contains virtual functions. This ensures proper cleanup of derived class objects when deleted through base class pointers.

4. **Override Keyword**: Use the override specifier when overriding virtual functions in derived classes. This helps the compiler catch errors where the function signature doesn't match.

5. **Slicing Problem**: When passing derived class objects by value to functions expecting base class objects, object slicing occurs. Always pass objects by reference or pointer to preserve polymorphic behavior.

6. **dynamic_cast Safety**: Prefer dynamic_cast over static_cast for downcasting because it performs runtime type checking and returns nullptr for invalid casts.

7. **Memory Leaks Prevention**: Always delete dynamically allocated objects accessed through base class pointers. Using smart pointers (unique_ptr, shared_ptr) is the modern C++ approach to avoid memory leaks.

8. **Diamond Problem**: In multiple inheritance scenarios, use virtual base classes to avoid ambiguity in pointer calculations and duplicate base class subobjects.

9. **Pointer to Members**: Be aware that pointers to virtual member functions require the virtual function table (vtable) lookup at runtime, which has slight overhead compared to non-virtual calls.

10. **Understanding Object Layout**: Know that a derived class object contains a base class subobject, which is why upcasting always works implicitly. The derived class extends the base with additional data members and potentially overridden functions.
