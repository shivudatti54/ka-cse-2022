# What is Object-Oriented Programming

## Introduction

Object-Oriented Programming (OOP) is a programming paradigm that revolutionized software development by organizing code around "objects" rather than "functions" or "procedures." This approach models real-world entities as software objects that contain both data (attributes/properties) and behavior (methods/functions). Originally conceived in the 1960s with Simula language, OOP gained mainstream prominence with Smalltalk in the 1970s and became industry-standard through C++ in the 1980s, Java in the 1990s, and continues to influence modern languages like Python, C#, and Ruby.

For the university's BCS306B course, understanding OOP is fundamental because C++ is a hybrid language that supports both procedural and object-oriented programming. The module introduces you to the core principles that form the foundation of modern software engineering. Companies worldwide use OOP principles to build scalable, maintainable, and reusable software systems. Whether you're developing desktop applications, embedded systems, or enterprise software, OOP concepts will be your primary tool for structuring code effectively.

This topic examines the fundamental question: "What is Object-Oriented Programming?" We will explore its defining characteristics, compare it with procedural programming, understand the terminologies, and appreciate why this paradigm has become the dominant approach in software development. By the end of this module, you will possess a clear conceptual framework that will support your learning of C++ object-oriented features in subsequent modules.

## Key Concepts

### 1. Objects and Classes

**Object** is the core building block of OOP. An object represents a real-world entity or concept and consists of:

- **State (Data/Attributes)**: Properties that describe the object (e.g., a BankAccount object has balance, account number)
- **Behavior (Methods/Functions)**: Operations that the object can perform (e.g., deposit(), withdraw())

**Class** is the blueprint or template for creating objects. It defines the structure and behavior that all objects of that type will have. Think of a class as a blueprint and objects as the actual houses built from that blueprint.

For example:

```cpp
class BankAccount {
 // Data members (attributes)
 int accountNumber;
 string holderName;
 double balance;

public:
 // Member functions (methods)
 void deposit(double amount) {
 balance += amount;
 }

 void withdraw(double amount) {
 if(amount <= balance)
 balance -= amount;
 }

 double getBalance() {
 return balance;
 }
};
```

### 2. Encapsulation

Encapsulation is the bundling of data and methods that operate on that data into a single unit (class). It also restricts direct access to some of an object's components, which is a mechanism for preventing interference and misuse of data.

In C++, encapsulation is implemented using **access specifiers**:

- **private**: Accessible only within the class (data hiding)
- **public**: Accessible from anywhere
- **protected**: Accessible within class and derived classes

The primary benefits are:

- Data security through information hiding
- Ease of maintenance and modification
- Reduced complexity through modularity

### 3. Abstraction

Abstraction means showing only the essential features while hiding the complex implementation details. It helps in reducing programming complexity and effort.

In C++, abstraction is achieved through:

- **Abstract classes** (classes with pure virtual functions)
- **Interfaces** (conceptually, though C++ doesn't have explicit interface keyword)
- **Header files** that expose function declarations without implementation details

Example showing abstraction:

```cpp
class Shape {
public:
 virtual void draw() = 0; // Abstract method
 virtual double area() = 0; // Abstract method
};

class Circle : public Shape {
 double radius;
public:
 Circle(double r) : radius(r) {}
 void draw() override {
 // Complex drawing logic hidden
 }
 double area() override {
 return 3.14159 * radius * radius;
 }
};
```

### 4. Inheritance

Inheritance is the mechanism by which a class acquires the properties and behaviors of another class. It promotes code reusability and establishes a natural hierarchy.

**Key terminology:**

- **Base class (Parent/Super class)**: The class whose properties are inherited
- **Derived class (Child/Sub class)**: The class that inherits properties
- **Single inheritance**: One base class → one derived class
- **Multiple inheritance**: Multiple base classes → one derived class
- **Multilevel inheritance**: A → B → C hierarchy
- **Hierarchical inheritance**: One base → multiple derived classes
- **Hybrid inheritance**: Combination of above types

```cpp
class Vehicle {
protected:
 int wheels;
public:
 void start() { cout << "Vehicle started"; }
};

class Car : public Vehicle {
 int seats;
public:
 Car() { wheels = 4; seats = 5; }
};
```

### 5. Polymorphism

Polymorphism allows one interface to be used for a general class of actions. The specific action is determined by the exact nature of the situation. In C++, polymorphism is achieved through:

**Compile-time (Static) Polymorphism:**

- Function overloading (multiple functions with same name, different parameters)
- Operator overloading (redefining operators for user-defined types)

**Runtime (Dynamic) Polymorphism:**

- Virtual functions and function overriding
- Achieved through base class pointers/references

```cpp
class Animal {
public:
 virtual void sound() {
 cout << "Animal makes sound";
 }
};

class Dog : public Animal {
public:
 void sound() override {
 cout << "Dog barks";
 }
};

class Cat : public Animal {
public:
 void sound() override {
 cout << "Cat meows";
 }
};
```

### 6. Message Passing

Objects communicate with each other through message passing. When an object wants another object to perform an operation, it sends a message (calls a method). This message contains:

- The receiver object
- The method to be invoked
- Any required parameters

### 7. OOP vs Procedural Programming

| Aspect           | Procedural Programming | Object-Oriented Programming |
| ---------------- | ---------------------- | --------------------------- |
| Approach         | Top-down decomposition | Bottom-up design            |
| Data Security    | Limited (global data)  | High (encapsulation)        |
| Code Reuse       | Through functions      | Through inheritance         |
| Data & Functions | Separate               | Bundled in objects          |
| Problem Solving  | Algorithm-centered     | Data-centered               |
| Examples         | C, Pascal              | C++, Java, Python           |

## Examples

### Example 1: Student Information System

**Problem**: Create a system to manage student records with basic operations.

**Solution using OOP principles:**

```cpp
#include <iostream>
using namespace std;

class Student {
private:
 int rollNo;
 string name;
 float marks[3];

public:
 // Constructor
 Student(int r, string n) {
 rollNo = r;
 name = n;
 for(int i = 0; i < 3; i++)
 marks[i] = 0;
 }

 // Set marks (encapsulation)
 void setMarks(int subject, float m) {
 if(subject >= 0 && subject < 3)
 marks[subject] = m;
 }

 // Calculate average (abstraction - hides calculation logic)
 float getAverage() {
 float sum = 0;
 for(int i = 0; i < 3; i++)
 sum += marks[i];
 return sum / 3;
 }

 // Display student info
 void display() {
 cout << "Roll No: " << rollNo << endl;
 cout << "Name: " << name << endl;
 cout << "Average Marks: " << getAverage() << endl;
 }
};

int main() {
 Student s1(101, "Rahul");
 s1.setMarks(0, 85.5);
 s1.setMarks(1, 90.0);
 s1.setMarks(2, 78.5);
 s1.display();
 return 0;
}
```

**Step-by-step explanation:**

1. `Student` class encapsulates roll number, name, and marks as private data
2. Public methods provide controlled access to private data
3. `getAverage()` abstracts the calculation logic
4. Objects (s1) are created from the Student class blueprint

### Example 2: Shape Hierarchy with Polymorphism

**Problem**: Calculate area of different shapes using polymorphism.

```cpp
#include <iostream>
using namespace std;

class Shape {
public:
 virtual double area() = 0; // Pure virtual function
};

class Rectangle : public Shape {
 double length, breadth;
public:
 Rectangle(double l, double b) : length(l), breadth(b) {}
 double area() override {
 return length * breadth;
 }
};

class Circle : public Shape {
 double radius;
public:
 Circle(double r) : radius(r) {}
 double area() override {
 return 3.14159 * radius * radius;
 }
};

int main() {
 Shape *ptr[2];
 ptr[0] = new Rectangle(10, 5);
 ptr[1] = new Circle(7);

 cout << "Rectangle Area: " << ptr[0]->area() << endl;
 cout << "Circle Area: " << ptr[1]->area() << endl;

 return 0;
}
```

**Output:**

```
Rectangle Area: 50
Circle Area: 153.917
```

**Key concepts demonstrated:**

- Abstraction: `Shape` is an abstract class with pure virtual function
- Inheritance: `Rectangle` and `Circle` inherit from `Shape`
- Polymorphism: Same interface (area()) gives different results

### Example 3: Employee Inheritance Hierarchy

```cpp
#include <iostream>
using namespace std;

class Employee {
protected:
 string name;
 int empId;
 float salary;

public:
 Employee(string n, int id, float s) {
 name = n;
 empId = id;
 salary = s;
 }

 virtual void display() {
 cout << "ID: " << empId << ", Name: " << name
 << ", Salary: " << salary << endl;
 }

 virtual float calculateBonus() = 0; // Pure virtual
};

class Manager : public Employee {
 float bonusRate;
public:
 Manager(string n, int id, float s, float br)
 : Employee(n, id, s), bonusRate(br) {}

 float calculateBonus() override {
 return salary * bonusRate;
 }

 void display() override {
 Employee::display();
 cout << "Bonus: " << calculateBonus() << endl;
 }
};

int main() {
 Employee *emp;
 Manager m("Priya", 201, 50000, 0.15);
 emp = &m;
 emp->display();
 return 0;
}
```

## Exam Tips

1. **Know the Four Pillars**: Remember the four fundamental OOP principles - Encapsulation, Inheritance, Polymorphism, and Abstraction. Questions asking to "explain OOP" always expect these four.

2. **Difference between Class and Object**: In exams, students often confuse these. Class is the blueprint; object is the instance. One class creates multiple objects.

3. **Access Specifiers Priority**: Remember the order of restriction: private < protected < public. Private members are not accessible even to derived classes.

4. **Pure Virtual Functions**: When a base class has `virtual function() = 0;`, it becomes abstract and cannot be instantiated. This is frequently tested in university exams.

5. **Types of Inheritance**: Be thorough with single, multiple, multilevel, hierarchical, and hybrid inheritance. university often asks to differentiate or give examples.

6. **Runtime vs Compile-time Polymorphism**: Function overloading is compile-time (static), virtual functions are runtime (dynamic). Remember this distinction clearly.

7. **Constructors and Destructors**: Constructor has same name as class, no return type. Destructor has ~ prefix. Constructor called automatically when object created; destructor when object destroyed.

8. **Code Reusability**: The primary advantage of OOP is code reusability achieved through inheritance. This is a common short-answer question.

9. **Message Passing**: Remember that objects communicate through method calls (message passing), not direct access to internal data (due to encapsulation).

10. **university Previous Year Questions**: Review questions on defining OOP, explaining OOP principles, and differences between OOP and procedural programming from past papers.
