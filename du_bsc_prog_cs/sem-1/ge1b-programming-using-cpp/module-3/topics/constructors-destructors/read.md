# Constructors and Destructors in C++

## Comprehensive Study Material for BSc Physical Science (CS) - Delhi University NEP 2024

---

## 1. Introduction

In object-oriented programming, **constructors** and **destructors** are special member functions that manage the lifecycle of objects. When an object is created, the constructor is automatically invoked to initialize its member variables and allocate necessary resources. Conversely, when an object goes out of scope or is explicitly deleted, the destructor is called to perform cleanup operations, release resources, and prevent memory leaks.

**Real-World Relevance:**
Consider a banking application where each account object needs to open a database connection when created and close that connection when the account is closed. Constructors handle the resource acquisition (opening the connection), while destructors ensure proper cleanup (closing the connection). Without proper constructor/destructor implementation, applications would suffer from resource leaks, corrupted data, and system instability.

This topic is fundamental to the **Ge1B Programming Using Cpp** course under Delhi University's NEP 2024 syllabus for BSc Physical Science (CS). Understanding these concepts is essential for developing robust, memory-efficient C++ applications—a core competency for Tier-3/4 CS courses at DU.

---

## 2. Constructors

A **constructor** is a special member function with the same name as the class, no return type (not even void), and is automatically invoked when an object is created. Constructors are used to initialize objects and allocate resources.

### 2.1 Types of Constructors

#### 2.1.1 Default Constructor

A constructor that accepts no parameters (or all parameters have default values) is called a **default constructor**.

```cpp
#include <iostream>
using namespace std;

class BankAccount {
private:
    string accountHolder;
    double balance;
    
public:
    // Default Constructor
    BankAccount() {
        accountHolder = "Unknown";
        balance = 0.0;
        cout << "Default constructor called!" << endl;
    }
    
    void display() {
        cout << "Account Holder: " << accountHolder << endl;
        cout << "Balance: $" << balance << endl;
    }
};

int main() {
    BankAccount acc1;  // Default constructor invoked
    acc1.display();
    return 0;
}
```

**Output:**
```
Default constructor called!
Account Holder: Unknown
Balance: $0
```

#### 2.1.2 Parameterized Constructor

Constructors that accept arguments to initialize member variables with specific values are called **parameterized constructors**.

```cpp
#include <iostream>
using namespace std;

class BankAccount {
private:
    string accountHolder;
    double balance;
    
public:
    // Parameterized Constructor
    BankAccount(string name, double amount) {
        accountHolder = name;
        balance = amount;
        cout << "Parameterized constructor called for " << accountHolder << endl;
    }
    
    void display() {
        cout << "Account Holder: " << accountHolder << endl;
        cout << "Balance: $" << balance << endl;
    }
};

int main() {
    BankAccount acc1("Rahul Sharma", 5000.0);
    BankAccount acc2("Priya Singh", 10000.0);
    
    acc1.display();
    cout << endl;
    acc2.display();
    
    return 0;
}
```

#### 2.1.3 Copy Constructor

A **copy constructor** creates a new object as a copy of an existing object. It is invoked when:
- A new object is initialized with an existing object
- An object is passed by value to a function
- An object is returned by value from a function

```cpp
#include <iostream>
using namespace std;

class Point {
private:
    int x, y;
    
public:
    // Parameterized Constructor
    Point(int xCoord, int yCoord) {
        x = xCoord;
        y = yCoord;
    }
    
    // Copy Constructor
    Point(const Point &p) {
        x = p.x;
        y = p.y;
        cout << "Copy constructor called!" << endl;
    }
    
    void display() {
        cout << "Point: (" << x << ", " << y << ")" << endl;
    }
};

int main() {
    Point p1(10, 20);
    Point p2(p1);    // Copy constructor invoked
    Point p3 = p1;   // Copy constructor invoked
    
    p1.display();
    p2.display();
    p3.display();
    
    return 0;
}
```

**Output:**
```
Copy constructor called!
Copy constructor called!
Point: (10, 20)
Point: (10, 20)
Point: (10, 20)
```

#### 2.1.4 Conversion Constructor

A constructor that can be called with a single argument acts as a **conversion constructor**, allowing implicit conversion from another type to the class type.

```cpp
#include <iostream>
using namespace std;

class Integer {
private:
    int value;
    
public:
    // Conversion Constructor - converts int to Integer
    Integer(int v) {
        value = v;
        cout << "Conversion constructor called with value: " << value << endl;
    }
    
    void display() {
        cout << "Value: " << value << endl;
    }
};

int main() {
    Integer obj1 = 100;  // Implicit conversion
    Integer obj2(200);    // Explicit call
    
    obj1.display();
    obj2.display();
    
    return 0;
}
```

---

## 3. Destructors

A **destructor** is a special member function that is automatically called when an object is destroyed or goes out of scope. It is used to release resources, close files, free memory, and perform cleanup operations.

### 3.1 Characteristics of Destructors

- Same name as the class, preceded by a tilde (~)
- No return type and no parameters
- Only one destructor per class
- Cannot be overloaded
- Called automatically when object is destroyed

### 3.2 Basic Destructor Example

```cpp
#include <iostream>
using namespace std;

class FileHandler {
private:
    string filename;
    
public:
    FileHandler(string name) {
        filename = name;
        cout << "Opening file: " << filename << endl;
    }
    
    // Destructor
    ~FileHandler() {
        cout << "Closing file: " << filename << endl;
    }
    
    void readData() {
        cout << "Reading data from " << filename << endl;
    }
};

int main() {
    FileHandler file1("data.txt");
    file1.readData();
    
    {
        FileHandler file2("temp.txt");
        file2.readData();
    }  // file2 destructor called here
    
    cout << "Exiting main" << endl;
    return 0;
}  // file1 destructor called here
```

**Output:**
```
Opening file: data.txt
Reading data from data.txt
Opening file: temp.txt
Reading data from temp.txt
Closing file: temp.txt
Exiting main
Closing file: data.txt
```

---

## 4. Initializer Lists

**Initializer lists** provide a more efficient way to initialize member variables, especially for:
- Reference members
- Const members
- Member objects without default constructors
- Base class constructors

### 4.1 Why Use Initializer Lists?

```cpp
#include <iostream>
using namespace std;

class Student {
private:
    const int rollNumber;      // Const member
    string name;
    int &referenceId;          // Reference member
    
public:
    // Using Initializer List
    Student(string n, int r, int &ref) : rollNumber(r), name(n), referenceId(ref) {
        cout << "Constructor with initializer list executed!" << endl;
    }
    
    void display() {
        cout << "Roll Number: " << rollNumber << endl;
        cout << "Name: " << name << endl;
        cout << "Reference ID: " << referenceId << endl;
    }
};

int main() {
    int refId = 1001;
    Student s("Amit Kumar", 42, refId);
    s.display();
    
    return 0;
}
```

### 4.2 Initializer List for Base Class and Member Objects

```cpp
#include <iostream>
using namespace std;

class Base {
protected:
    int baseValue;
public:
    Base(int val) : baseValue(val) {
        cout << "Base constructor called with value: " << baseValue << endl;
    }
};

class Derived : public Base {
private:
    int derivedValue;
    Base baseObj;  // Member object
    
public:
    // Initializer list for base class and member objects
    Derived(int b, int d, int m) : Base(b), baseObj(b * 2), derivedValue(d) {
        cout << "Derived constructor called!" << endl;
    }
    
    void display() {
        cout << "Base Value: " << baseValue << endl;
        cout << "Derived Value: " << derivedValue << endl;
    }
};

int main() {
    Derived obj(10, 20, 30);
    obj.display();
    return 0;
}
```

---

## 5. Copy Assignment Operator

The **copy assignment operator** (`operator=`) is used to assign one object to another when both objects already exist. It is different from the copy constructor, which initializes a new object.

### 5.1 When is Copy Assignment Operator Called?

```cpp
#include <iostream>
using namespace std;

class Box {
private:
    int width, height;
    
public:
    // Parameterized Constructor
    Box(int w, int h) : width(w), height(h) {
        cout << "Constructor called" << endl;
    }
    
    // Copy Assignment Operator
    Box& operator=(const Box &b) {
        cout << "Copy Assignment Operator called" << endl;
        if (this != &b) {  // Check for self-assignment
            width = b.width;
            height = b.height;
        }
        return *this;
    }
    
    void display() {
        cout << "Width: " << width << ", Height: " << height << endl;
    }
};

int main() {
    Box b1(10, 20);
    Box b2(30, 40);
    
    b1 = b2;  // Copy assignment operator called (not copy constructor)
    
    b1.display();
    
    Box b3 = b1;  // This calls COPY CONSTRUCTOR, not assignment operator
    b3.display();
    
    return 0;
}
```

### 5.2 Rule of Three

In C++, if a class manages resources (like dynamic memory), you must explicitly define:
1. **Destructor** - to release resources
2. **Copy Constructor** - to properly copy the resource
3. **Copy Assignment Operator** - to properly assign the resource

This is known as the **Rule of Three**.

```cpp
#include <iostream>
using namespace std;

class MyString {
private:
    char *str;
    int length;
    
public:
    MyString(const char *s = "") {
        length = strlen(s);
        str = new char[length + 1];
        strcpy(str, s);
    }
    
    // Destructor
    ~MyString() {
        delete[] str;
    }
    
    // Copy Constructor
    MyString(const MyString &s) {
        length = s.length;
        str = new char[length + 1];
        strcpy(str, s.str);
    }
    
    // Copy Assignment Operator
    MyString& operator=(const MyString &s) {
        if (this != &s) {
            delete[] str;
            length = s.length;
            str = new char[length + 1];
            strcpy(str, s.str);
        }
        return *this;
    }
    
    void display() {
        cout << "String: " << str << ", Length: " << length << endl;
    }
};

int main() {
    MyString s1("Hello");
    MyString s2("World");
    
    MyString s3 = s1;  // Copy constructor
    s2 = s1;           // Copy assignment operator
    
    s1.display();
    s2.display();
    s3.display();
    
    return 0;
}
```

---

## 6. Virtual Destructors

**Virtual destructors** are essential for proper cleanup in polymorphic scenarios. When a base class pointer points to a derived class object, deleting the pointer should call the derived class destructor followed by the base class destructor.

### 6.1 Problem Without Virtual Destructor

```cpp
#include <iostream>
using namespace std;

class Base {
public:
    Base() {
        cout << "Base constructor" << endl;
    }
    ~Base() {
        cout << "Base destructor" << endl;
    }
};

class Derived : public Base {
private:
    int *arr;
public:
    Derived() {
        arr = new int[100];
        cout << "Derived constructor" << endl;
    }
    ~Derived() {
        delete[] arr;
        cout << "Derived destructor" << endl;
    }
};

int main() {
    Base *ptr = new Derived();
    delete ptr;  // Only Base destructor called! Memory leak!
    return 0;
}
```

**Output (without virtual destructor):**
```
Base constructor
Derived constructor
Base destructor
```

### 6.2 Solution: Virtual Destructor

```cpp
#include <iostream>
using namespace std;

class Base {
public:
    Base() {
        cout << "Base constructor" << endl;
    }
    virtual ~Base() {  // Virtual destructor
        cout << "Base destructor" << endl;
    }
};

class Derived : public Base {
private:
    int *arr;
public:
    Derived() {
        arr = new int[100];
        cout << "Derived constructor" << endl;
    }
    ~Derived() {
        delete[] arr;
        cout << "Derived destructor" << endl;
    }
};

int main() {
    Base *ptr = new Derived();
    delete ptr;  // Now both destructors are called properly
    return 0;
}
```

**Output (with virtual destructor):**
```
Base constructor
Derived constructor
Derived destructor
Base destructor
```

**Key Rule:** Always make base class destructors virtual when dealing with inheritance and polymorphism.

---

## 7. Delegating Constructors

**Delegating constructors** allow a constructor to call another constructor of the same class, reducing code duplication. This feature was introduced in C++11.

### 7.1 Without Delegating Constructors (Code Duplication)

```cpp
#include <iostream>
using namespace std;

class Rectangle {
private:
    int width, height;
    
public:
    Rectangle() {
        width = 0;
        height = 0;
    }
    
    Rectangle(int w, int h) {
        width = w;
        height = h;
    }
    
    Rectangle(int size) {
        width = size;
        height = size;
    }
    
    void display() {
        cout << "Width: " << width << ", Height: " << height << endl;
    }
};
```

### 7.2 With Delegating Constructors

```cpp
#include <iostream>
using namespace std;

class Rectangle {
private:
    int width, height;
    
public:
    // Primary constructor
    Rectangle(int w, int h) : width(w), height(h) {
        cout << "Primary constructor called" << endl;
    }
    
    // Delegating constructor - delegates to primary constructor
    Rectangle() : Rectangle(0, 0) {
        cout << "Default constructor delegating..." << endl;
    }
    
    // Delegating constructor - delegates to primary constructor
    Rectangle(int size) : Rectangle(size, size) {
        cout << "Square constructor delegating..." << endl;
    }
    
    void display() {
        cout << "Width: " << width << ", Height: " << height << endl;
    }
};

int main() {
    Rectangle r1;
    cout << endl;
    Rectangle r2(10, 20);
    cout << endl;
    Rectangle r3(15);
    
    r1.display();
    r2.display();
    r3.display();
    
    return 0;
}
```

---

## 8. Destructor Order in Inheritance

Understanding the order of destructor calls is crucial for proper resource management in inheritance hierarchies.

### 8.1 Destructor Call Order

```cpp
#include <iostream>
using namespace std;

class Base {
public:
    Base() {
        cout << "Base constructor" << endl;
    }
    virtual ~Base() {
        cout << "Base destructor" << endl;
    }
};

class Derived : public Base {
public:
    Derived() {
        cout << "Derived constructor" << endl;
    }
    ~Derived() {
        cout << "Derived destructor" << endl;
    }
};

class MoreDerived : public Derived {
public:
    MoreDerived() {
        cout << "MoreDerived constructor" << endl;
    }
    ~MoreDerived() {
        cout << "MoreDerived destructor" << endl;
    }
};

int main() {
    MoreDerived *obj = new MoreDerived();
    delete obj;
    return 0;
}
```

**Output:**
```
Base constructor
Derived constructor
MoreDerived constructor
MoreDerived destructor
Derived destructor
Base destructor
```

**Order of Destructor Execution:**
- Constructors are called from base to derived (top-down)
- Destructors are called from derived to base (bottom-up)
- This ensures that derived class resources are cleaned up before base class resources

### 8.2 Local Objects and Destructor Order

```cpp
#include <iostream>
using namespace std;

class Sample {
    string name;
public:
    Sample(string n) : name(n) {
        cout << "Constructor: " << name << endl;
    }
    ~Sample() {
        cout << "Destructor: " << name << endl;
    }
};

int main() {
    cout << "=== Creating objects ===" << endl;
    Sample obj1("First");
    Sample obj2("Second");
    Sample obj3("Third");
    
    cout << "=== Exiting main (objects will be destroyed) ===" << endl;
    return 0;
}
```

**Output:**
```
=== Creating objects ===
Constructor: First
Constructor: Second
Constructor: Third
=== Exiting main (objects will be destroyed) ===
Destructor: Third
Destructor: Second
Destructor: First
```

**Note:** Local objects are destroyed in reverse order of their creation (LIFO - Last In First Out).

---

## 9. Practical Example: Complete Class Implementation

```cpp
#include <iostream>
#include <cstring>
using namespace std;

// Class demonstrating all constructor/destructor concepts
class Employee {
private:
    int id;
    string name;
    double salary;
    static int employeeCount;  // Static member
    
public:
    // Default Constructor
    Employee() : id(0), name("Unknown"), salary(0.0) {
        employeeCount++;
    }
    
    // Parameterized Constructor
    Employee(int empId, string empName, double empSalary) 
        : id(empId), name(empName), salary(empSalary) {
        employeeCount++;
    }
    
    // Copy Constructor
    Employee(const Employee &emp) : id(emp.id), name(emp.name), salary(emp.salary) {
        employeeCount++;
        cout << "Copy constructor called for: " << name << endl;
    }
    
    // Copy Assignment Operator
    Employee& operator=(const Employee &emp) {
        if (this != &emp) {
            id = emp.id;
            name = emp.name;
            salary = emp.salary;
        }
        return *this;
    }
    
    // Destructor
    ~Employee() {
        employeeCount--;
        cout << "Destructor called for: " << name << endl;
    }
    
    // Member functions
    void display() const {
        cout << "ID: " << id << ", Name: " << name 
             << ", Salary: $" << salary << endl;
    }
    
    static int getCount() {
        return employeeCount;
    }
};

int Employee::employeeCount = 0;

int main() {
    cout << "=== Creating Employees ===" << endl;
    Employee e1(101, "Rahul Sharma", 50000.0);
    Employee e2(102, "Priya Gupta", 55000.0);
    Employee e3;  // Default constructor
    
    cout << "\nTotal Employees: " << Employee::getCount() << endl;
    
    cout << "\n=== Copy Constructor Demo ===" << endl;
    Employee e4 = e1;  // Copy constructor
    
    cout << "\n=== Assignment Operator Demo ===" << endl;
    e3 = e1;  // Assignment operator
    
    cout << "\n=== Employee Details ===" << endl;
    e1.display();
    e2.display();
    e3.display();
    e4.display();
    
    cout << "\n=== Exiting main ===" << endl;
    return 0;
}
```

---

## 10. Multiple Choice Questions

### Easy Level

**Q1.** What is the name of the special member function that is automatically called when an object is created?
- A) Destructor
- B) Constructor
- C) Main function
- D) Copy constructor

**Q2.** Which of the following is NOT a type of constructor?
- A) Default constructor
- B) Parameterized constructor
- C) Virtual constructor
- D) Copy constructor

**Q3.** What is the return type of a destructor?
- A) int
- B) void
- C) No return type (not even void)
- D) bool

### Medium Level

**Q4.** Which constructor is called when: `ClassName obj2 = obj1;` where obj1 already exists?
- A) Default constructor
- B) Parameterized constructor
- C) Copy constructor
- D) Assignment operator

**Q5.** What is the purpose of a virtual destructor?
- A) To improve performance
- B) To enable polymorphism and proper cleanup in inheritance
- C) To allow function overloading
- D) To initialize virtual members

**Q6.** In C++, which rule states that if you define a destructor, you should also define copy constructor and copy assignment operator?
- A) Rule of Five
- B) Rule of Three
- C) Liskov Substitution Principle
- D) Open-Closed Principle

**Q7.** What is the correct order of destructor calls in a class hierarchy (derived → base)?
- A) Random order
- B) Derived then Base
- C) Base then Derived
- D) Depends on compiler

### Hard Level

**Q8.** Consider the following code:
```cpp
class Base {
public:
    virtual ~Base() {}
};
class Derived : public Base {
    ~Derived() {}
};
Base* ptr = new Derived();
delete ptr;
```
How many destructors will be called?
- A) 0
- B) 1 (only Base destructor)
- C) 2 (Derived then Base)
- D) Undefined behavior

**Q9.** Which of the following is TRUE about initializer lists?
- A) They are optional for all constructors
- B) They are mandatory for initializing const and reference members
- C) They cannot be used with default arguments
- D) They execute before the constructor body

**Q10.** What is the output?
```cpp
class A {
public:
    A() { cout << "1"; }
    ~A() { cout << "4"; }
};
class B : public A {
public:
    B() { cout << "2"; }
    ~B() { cout << "3"; }
};
int main() { B obj; return 0; }
```
- A) 1234
- B) 4321
- C) 12
- D) 1243

**Q11.** Which constructor concept allows one constructor to call another constructor of the same class?
- A) Static constructors
- B) Delegating constructors
- C) Private constructors
- D) Explicit constructors

**Q12.** What happens if a class has a const member but no initializer list is used in the constructor?
- A) Compilation error
- B) Runtime error
- C) The const member remains uninitialized
- D) The const member is automatically set to zero

---

## 11. Flashcards

| Term | Definition |
|------|------------|
| **Constructor** | Special member function called automatically when an object is created to initialize member variables |
| **Destructor** | Special member function called automatically when an object is destroyed to perform cleanup operations |
| **Default Constructor** | Constructor with no parameters or all parameters having default values |
| **Parameterized Constructor** | Constructor that accepts arguments to initialize members with specific values |
| **Copy Constructor** | Constructor that creates a new object as a copy of an existing object |
| **Copy Assignment Operator** | Operator used to assign one existing object to another existing object |
| **Virtual Destructor** | Destructor declared with `virtual` keyword to ensure proper cleanup in inheritance/polymorphism |
| **Initializer List** | Syntax using colon after constructor parameters to initialize member variables directly |
| **Delegating Constructor** | Feature (C++11) allowing a constructor to call another constructor of the same class |
| **Rule of Three** | Rule stating that classes managing resources should define destructor, copy constructor, and copy assignment operator |
| **Object Lifecycle** | Sequence of object creation → usage → destruction in a program |
| **Resource Acquisition Initialization (RAII)** | Programming idiom where resource acquisition is done in constructor and release in destructor |

---

## 12. Key Takeaways

1. **Constructors** are special member functions with the same name as the class, no return type, and are automatically invoked during object creation to initialize member variables.

2. **Types of Constructors**: Default, Parameterized, Copy, and Conversion constructors serve different initialization purposes.

3. **Destructors** have the same name prefixed with (~), take no parameters, and are automatically called when objects are destroyed to release resources.

4. **Initializer Lists** are essential for initializing const members, reference members, and member objects without default constructors—they provide direct initialization rather than assignment.

5. **Copy Assignment Operator** is distinct from copy constructor—it's used when assigning to an existing object, while copy constructor initializes a new object.

6. **Virtual Destructors** are critical in polymorphic scenarios (base class pointers pointing to derived objects) to ensure proper cleanup of derived class resources.

7. **Destructor Order**: Constructors run from base to derived; destructors run from derived to base (reverse order).

8. **Delegating Constructors** (C++11) reduce code duplication by allowing constructors to call other constructors of the same class.

9. **Rule of Three/Five**: Classes managing resources (like dynamic memory) must define destructor, copy constructor, and copy assignment operator (Rule of Three); with move semantics, it's the Rule of Five.

10. **Delhi University Context**: These concepts form the foundation for understanding object-oriented design and memory management, which are essential for advanced C++ programming courses and practical software development.

---

## 13. References

- Delhi University NEP 2024 Syllabus: Ge1B Programming Using Cpp
- Bjarne Stroustrup, "The C++ Programming Language"
- Scott Meyers, "Effective C++"
- ISO C++11/C++14/C++17 Standards Documentation

---

*Study Material prepared for BSc Physical Science (CS) - Delhi University NEP 2024*