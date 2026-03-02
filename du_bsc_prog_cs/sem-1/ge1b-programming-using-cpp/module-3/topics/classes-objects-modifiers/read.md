# Classes, Objects, and Modifiers in C++

## Comprehensive Study Material for GE1B Programming Using C++

---

## 1. Introduction

Object-Oriented Programming (OOP) is a fundamental paradigm in modern software development, and C++ was one of the first languages to introduce these powerful concepts. In the Delhi University BSc Physical Science (CS) curriculum under NEP 2024, understanding Classes, Objects, and Modifiers is essential for building robust, maintainable, and scalable applications.

In the real world, we model everything as objects—vehicles, employees, bank accounts, students. Classes serve as blueprints for creating such objects, while modifiers control the accessibility and behavior of class members. This chapter covers these core OOP concepts comprehensively, aligning with the DU syllabus requirements for GE1B.

---

## 2. Classes and Objects: The Foundation of OOP

### 2.1 What is a Class?

A **class** is a user-defined data type that acts as a blueprint for creating objects. It encapsulates data (attributes/properties) and functions (methods/behaviors) together. In C++, classes provide data hiding, inheritance, and polymorphism—key features of OOP.

**Syntax:**
```cpp
class ClassName {
    // Private members (by default)
    data_type member1;
    
public:
    // Public members
    data_type member2;
    
    // Member functions
    return_type functionName();
};
```

### 2.2 What is an Object?

An **object** is an instance of a class. When a class is defined, no memory is allocated until an object is created. Each object has its own copy of the data members (unless declared static) and can access the public members of the class.

**Syntax:**
```cpp
ClassName objectName;  // Object creation
```

### 2.3 Key Differences: Class vs Object

| Aspect | Class | Object |
|--------|-------|--------|
| Definition | Blueprint/Template | Instance of a class |
| Memory | No memory allocated | Memory allocated |
| Declaration | `class ClassName {};` | `ClassName obj;` |
| Existence | Logical abstraction | Physical reality |

---

## 3. Access Specifiers (Modifiers) in C++

Access specifiers (also called access modifiers) determine the visibility and accessibility of class members. C++ provides three access modifiers:

### 3.1 Private

- **Default access level** for class members
- Members are accessible only within the same class
- Cannot be accessed by objects or functions outside the class
- Used for data hiding and encapsulation

```cpp
class BankAccount {
private:
    double balance;  // Private data member
    
public:
    void deposit(double amount) {
        balance += amount;  // Accessible within class
    }
};

int main() {
    BankAccount acc;
    // acc.balance = 1000;  // ERROR: Private member
    acc.deposit(500);  // OK: Public member function
}
```

### 3.2 Public

- Members are accessible from anywhere in the program
- Forms the interface through which external code interacts with the class
- Used for member functions that provide services to users

```cpp
class Rectangle {
public:
    double width;
    double height;
    
    double area() {
        return width * height;
    }
};

int main() {
    Rectangle r;
    r.width = 5;
    r.height = 3;
    cout << "Area: " << r.area();  // OK: Public access
}
```

### 3.3 Protected

- Used primarily in the context of inheritance
- Members are accessible within the class and in derived (child) classes
- Not accessible from outside the class hierarchy

```cpp
class Vehicle {
protected:
    string fuelType;
    
public:
    void display() {
        cout << "Fuel: " << fuelType;
    }
};

class Car : public Vehicle {
public:
    void setFuel(string f) {
        fuelType = f;  // Accessible in derived class
    }
};

int main() {
    Car c;
    c.setFuel("Petrol");
    // c.fuelType = "Diesel";  // ERROR: Protected member
    c.display();  // OK
}
```

---

## 4. Constructors: Building Objects

A **constructor** is a special member function that is automatically called when an object is created. It initializes the object and has the same name as the class.

### 4.1 Types of Constructors

#### 4.1.1 Default Constructor

Takes no parameters and initializes members with default values.

```cpp
class Student {
public:
    string name;
    int age;
    
    // Default constructor
    Student() {
        name = "Unknown";
        age = 0;
    }
};

int main() {
    Student s1;  // Calls default constructor
    cout << s1.name << " " << s1.age;
}
```

#### 4.1.2 Parameterized Constructor

Accepts arguments to initialize members with specific values.

```cpp
class Student {
public:
    string name;
    int age;
    
    // Parameterized constructor
    Student(string n, int a) {
        name = n;
        age = a;
    }
};

int main() {
    Student s1("Amit", 20);  // Calls parameterized constructor
    cout << s1.name << " " << s1.age;
}
```

#### 4.1.3 Copy Constructor

Creates a new object as a copy of an existing object.

```cpp
class Student {
public:
    string name;
    int age;
    
    Student(string n, int a) {
        name = n;
        age = a;
    }
    
    // Copy constructor
    Student(const Student& s) {
        name = s.name;
        age = s.age;
    }
};

int main() {
    Student s1("Rahul", 21);
    Student s2 = s1;  // Calls copy constructor
    cout << s2.name << " " << s2.age;
}
```

### 4.2 Constructor Overloading

Multiple constructors can exist with different parameter lists (compile-time polymorphism).

```cpp
class Box {
public:
    double length, breadth, height;
    
    Box() {  // Default
        length = breadth = height = 1;
    }
    
    Box(double side) {  // Cube
        length = breadth = height = side;
    }
    
    Box(double l, double b, double h) {  // Rectangular
        length = l;
        breadth = b;
        height = h;
    }
};
```

---

## 5. Destructors: Cleaning Up Resources

A **destructor** is a special member function that is called when an object goes out of scope or is explicitly deleted. It releases resources allocated by the object.

**Characteristics:**
- Same name as class preceded by tilde (~)
- Cannot be overloaded
- Takes no parameters
- Automatically invoked

```cpp
class MemoryBlock {
private:
    int* data;
    int size;
    
public:
    MemoryBlock(int s) {
        size = s;
        data = new int[size];  // Dynamic memory allocation
        cout << "Memory allocated\n";
    }
    
    ~MemoryBlock() {  // Destructor
        delete[] data;  // Release memory
        cout << "Memory deallocated\n";
    }
};

int main() {
    MemoryBlock obj(10);
    // Destructor called automatically when obj goes out of scope
}
```

---

## 6. The 'this' Pointer

The **`this`** pointer is an implicit pointer available within all non-static member functions. It points to the object that invoked the function.

**Key Uses:**
- Differentiing between member variables and parameters with same name
- Returning the current object from a member function
- Chaining function calls

```cpp
class Student {
private:
    string name;
    int age;
    
public:
    void setData(string name, int age) {
        this->name = name;    // 'this' distinguishes member from parameter
        this->age = age;
    }
    
    // Returning current object for method chaining
    Student& getData() {
        return *this;  // Dereferencing 'this'
    }
    
    void display() {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
};

int main() {
    Student s;
    s.setData("Priya", 22);
    s.display();
}
```

---

## 7. Static Members

Static members belong to the class rather than any specific object. They are shared among all objects of the class.

### 7.1 Static Data Members

```cpp
class Counter {
private:
    int count;          // Instance variable
    static int total;   // Shared by all objects
    
public:
    Counter() {
        count = 0;
        total++;
    }
    
    static int getTotal() {  // Static member function
        return total;
    }
    
    void showCount() {
        cout << "Count: " << count << ", Total: " << total << endl;
    }
};

int Counter::total = 0;  // Definition outside class

int main() {
    Counter c1, c2, c3;
    c1.showCount();
    c2.showCount();
    c3.showCount();
    cout << "Total objects created: " << Counter::getTotal();
}
```

### 7.2 Static Member Functions

- Can access only static data members
- Can be called using class name without creating an object
- Do not have a 'this' pointer

---

## 8. Friend Functions and Friend Classes

A **friend function** is a non-member function that has access to private and protected members of a class. Similarly, a **friend class** can access private and protected members of another class.

### 8.1 Friend Function

```cpp
class Box {
private:
    double width;
    
public:
    Box(double w) : width(w) {}
    
    // Declaring friend function
    friend void displayWidth(Box b);
};

void displayWidth(Box b) {
    // Can access private member directly
    cout << "Width: " << b.width << endl;
}

int main() {
    Box b(10.5);
    displayWidth(b);  // No object.method() syntax
}
```

### 8.2 Friend Class

```cpp
class Teacher {
private:
    string name = "Dr. Sharma";
    
    // Granting access to Student class
    friend class Student;
};

class Student {
public:
    void revealTeacher(Teacher t) {
        // Can access private member of Teacher
        cout << "Teacher: " << t.name << endl;
    }
};
```

**Note:** Friendship is not transitive, not inherited, and not reciprocal unless explicitly granted.

---

## 9. Complete Working Examples

### Example 1: Student Management System

```cpp
#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    string name;
    int rollNo;
    float marks;
    
public:
    // Constructor
    Student(string n = "Unknown", int r = 0, float m = 0.0) {
        name = n;
        rollNo = r;
        marks = m;
    }
    
    // Copy constructor
    Student(const Student& s) {
        name = s.name;
        rollNo = s.rollNo;
        marks = s.marks;
    }
    
    // Member functions
    void setData(string n, int r, float m) {
        name = n;
        rollNo = r;
        marks = m;
    }
    
    void display() const {
        cout << "Name: " << name << ", Roll: " << rollNo 
             << ", Marks: " << marks << endl;
    }
    
    float getMarks() {
        return marks;
    }
    
    // Destructor
    ~Student() {
        // Cleanup if needed
    }
};

int main() {
    Student s1("Aman", 101, 85.5);
    Student s2("Priya", 102, 92.0);
    Student s3 = s1;  // Copy constructor
    
    cout << "Student Details:\n";
    s1.display();
    s2.display();
    s3.display();
    
    return 0;
}
```

### Example 2: Bank Account with Encapsulation

```cpp
#include <iostream>
using namespace std;

class BankAccount {
private:
    string accountHolder;
    long accountNumber;
    double balance;
    static double minimumBalance;  // Static member
    
public:
    // Constructor
    BankAccount(string name, long accNo, double bal) {
        accountHolder = name;
        accountNumber = accNo;
        balance = bal;
    }
    
    // Deposit money
    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            cout << "Deposited: " << amount << endl;
        } else {
            cout << "Invalid amount!\n";
        }
    }
    
    // Withdraw money
    void withdraw(double amount) {
        if (amount > 0 && (balance - amount) >= minimumBalance) {
            balance -= amount;
            cout << "Withdrawn: " << amount << endl;
        } else {
            cout << "Insufficient balance or below minimum!\n";
        }
    }
    
    // Display balance
    void displayBalance() const {
        cout << "Account Holder: " << accountHolder << endl;
        cout << "Account Number: " << accountNumber << endl;
        cout << "Current Balance: " << balance << endl;
    }
    
    static void setMinimumBalance(double mb) {
        minimumBalance = mb;
    }
};

double BankAccount::minimumBalance = 500.0;  // Initialize static member

int main() {
    BankAccount::setMinimumBalance(500.0);
    
    BankAccount acc1("Rahul Kumar", 1234567890, 5000.0);
    
    acc1.displayBalance();
    cout << "\n--- Transaction ---\n";
    acc1.deposit(1000);
    acc1.withdraw(2000);
    acc1.withdraw(4000);  // Should fail
    
    cout << "\n--- Final Balance ---\n";
    acc1.displayBalance();
    
    return 0;
}
```

---

## 10. Key Takeaways

1. **Classes and Objects**: Classes are blueprints; objects are instances with actual memory allocation.

2. **Access Modifiers**:
   - `private`: Accessible only within the class (default for class)
   - `public`: Accessible from anywhere
   - `protected`: Accessible within class and derived classes

3. **Constructors**: Special functions for object initialization; can be default, parameterized, or copy constructors; support overloading.

4. **Destructors**: Clean up resources; same name as class with ~ prefix; automatically invoked.

5. **this Pointer**: Points to current object; useful for distinguishing member variables from parameters.

6. **Static Members**: Shared across all objects; belong to class rather than instances; static functions can access only static members.

7. **Friend Functions**: Non-member functions with access to private/protected members; breaks encapsulation but useful for operator overloading and cooperative classes.

8. **Encapsulation**: Bundling data and methods together while restricting direct access to some components—fundamental OOP principle.

---

## 11. MCQ Bank

### Easy Level

1. **What is a class in C++?**
   - a) An instance of an object
   - b) A blueprint for creating objects
   - c) A function
   - d) A data type only
   
   **Answer: b**

2. **Which access specifier makes members accessible only within the class?**
   - a) public
   - b) private
   - c) protected
   - d) friend
   
   **Answer: b**

3. **What is the default access specifier for class members in C++?**
   - a) public
   - b) private
   - c) protected
   - d) default
   
   **Answer: b**

4. **Which function is called automatically when an object is created?**
   - a) Destructor
   - b) Constructor
   - c) Main function
   - d) Static function
   
   **Answer: b**

5. **What does the 'this' pointer point to?**
   - a) The class
   - b) The current object
   - c) The main function
   - d) None of the above
   
   **Answer: b**

### Medium Level

6. **Which of the following is NOT a valid access specifier in C++?**
   - a) private
   - b) public
   - c) protected
   - d) secure
   
   **Answer: d**

7. **Can a static member function access non-static data members directly?**
   - a) Yes, always
   - b) No, never
   - c) Only if declared const
   - d) Only in main function
   
   **Answer: b**

8. **What is the purpose of a copy constructor?**
   - a) To destroy an object
   - b) To create a copy of another object
   - c) To initialize static members
   - d) To overload operators
   
   **Answer: b**

9. **If no constructor is defined, which constructor does the compiler provide?**
   - a) Virtual constructor
   - b) Default constructor
   - c) Copy constructor
   - d) Parameterized constructor
   
   **Answer: b**

10. **Can a friend function access private members of a class?**
    - a) No, never
    - b) Yes, always
    - c) Only if declared in main
    - d) Only with special syntax
    
    **Answer: b**

### Hard Level

11. **Which statement is true about protected members in inheritance?**
    - a) Accessible only in the base class
    - b) Accessible in base class and derived classes
    - c) Accessible in all classes
    - d) Not accessible in inheritance
    
    **Answer: b**

12. **How many destructors can a class have?**
    - a) Multiple based on parameters
    - b) Only one
    - c) Zero (compiler provides)
    - d) Infinite
    
    **Answer: b**

13. **What is the output if we try to access a private member outside the class?**
    - a) Warning
    - b) Compilation error
    - c) Runtime error
    - d) No output
    
    **Answer: b**

14. **Which keyword is used to declare a friend function?**
    - a) friend
    - b) this
    - c) static
    - d) public
    
    **Answer: a**

15. **Static data members are:**
    - a) Created for each object
    - b) Shared among all objects of a class
    - c) Always private
    - d) Cannot be modified
    
    **Answer: b**

---

## 12. Flashcards

| # | Term | Definition |
|---|------|------------|
| 1 | Class | User-defined data type that serves as a blueprint for creating objects |
| 2 | Object | Instance of a class with actual memory allocation |
| 3 | Encapsulation | Bundling data and methods together while restricting access |
| 4 | Constructor | Special member function called automatically when an object is created |
| 5 | Destructor | Special member function called automatically when an object is destroyed |
| 6 | Access Specifiers | Keywords (private, public, protected) that define member accessibility |
| 7 | this Pointer | Implicit pointer pointing to the current object |
| 8 | Static Member | Member belonging to class rather than any object; shared across instances |
| 9 | Friend Function | Non-member function with access to private/protected members |
| 10 | Copy Constructor | Constructor that creates a new object as a copy of an existing one |
| 11 | Data Hiding | Principle of restricting access to certain class components |
| 12 | Parameterized Constructor | Constructor that accepts arguments for initialization |

---

*This study material is aligned with the Delhi University NEP 2024 syllabus for GE1B Programming Using C++, covering all essential concepts required for BSc Physical Science (CS) examinations.*