# Classes, Objects, and Modifiers in C++

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

Object-Oriented Programming (OOP) is a fundamental paradigm in modern software development, and C++ is one of the most powerful languages that fully supports OOP concepts. For students at Delhi University's BSc (Hons) Computer Science program, understanding **Classes**, **Objects**, and **Modifiers** is essential not only for academic success but also for building robust, maintainable software systems.

In the real world, OOP mirrors how we perceive real-world entities. Consider a banking system: a "Bank Account" is a class (a blueprint), while a specific customer's account (e.g., "John's Savings Account") is an object (an instance). The modifiers (access specifiers) control who can access the account balance—customers can view their own balance (public access to certain functions), but internal processing details remain hidden (private data).

This study material covers all components required for the Delhi University syllabus, including advanced topics often overlooked in basic tutorials.

---

## 2. Classes and Objects: The Foundation

### 2.1 What is a Class?

A **class** is a user-defined data type that serves as a blueprint for creating objects. It encapsulates data (attributes/properties) and functions (methods/behaviors) that operate on that data into a single unit.

**Syntax:**
```cpp
class ClassName {
    // Access specifier (public, private, protected)
    // Data members (variables)
    // Member functions (methods)
};
```

### 2.2 What is an Object?

An **object** is an instance of a class. When a class is defined, no memory is allocated until an object is created. Each object has its own copy of data members (unless declared static).

```cpp
class BankAccount {
public:
    string accountHolder;
    double balance;
    
    void display() {
        cout << "Holder: " << accountHolder << ", Balance: " << balance << endl;
    }
};

int main() {
    BankAccount johnAccount;  // Object creation
    johnAccount.accountHolder = "John Doe";
    johnAccount.balance = 5000.0;
    johnAccount.display();
    return 0;
}
```

---

## 3. Access Specifiers (Modifiers)

Access modifiers in C++ control the visibility and accessibility of class members. This is fundamental to **encapsulation**—the process of hiding internal details and exposing only necessary interfaces.

### 3.1 Types of Access Specifiers

| Specifier | Accessibility | Typical Use |
|-----------|---------------|-------------|
| **private** | Only within the class and friend functions | Data hiding—protecting internal state |
| **public** | Anywhere the object is accessible | Interface methods for external interaction |
| **protected** | Within class and derived classes | Inheritance—allowing subclasses access |

### 3.2 Deep Encapsulation Discussion

Encapsulation is not merely using `private` data members; it involves:

1. **Data Hiding**: Preventing direct external modification of internal state
2. **Interface Abstraction**: Providing controlled access through public methods
3. **Validation**: Ensuring data integrity through setter methods

**Example of Proper Encapsulation:**
```cpp
class Temperature {
private:
    double celsius;  // Hidden internal representation
    
public:
    // Setter with validation
    void setCelsius(double temp) {
        if (temp >= -273.15) {  // Absolute zero validation
            celsius = temp;
        }
    }
    
    // Getter with computation
    double getFahrenheit() const {
        return (celsius * 9.0 / 5.0) + 32.0;
    }
    
    double getCelsius() const {
        return celsius;
    }
};
```

This approach prevents invalid temperature values and allows the class to change its internal representation (e.g., storing in Kelvin instead) without affecting external code—a powerful principle called **implementation hiding**.

---

## 4. Constructors and Destructors

### 4.1 Constructors

A **constructor** is a special member function called automatically when an object is created. It initializes the object.

**Characteristics:**
- Same name as the class
- No return type (not even void)
- Can be overloaded (multiple constructors with different parameters)

```cpp
class Rectangle {
private:
    double width, height;
    
public:
    // Default constructor
    Rectangle() {
        width = height = 0;
    }
    
    // Parameterized constructor
    Rectangle(double w, double h) {
        width = w;
        height = h;
    }
    
    // Copy constructor
    Rectangle(const Rectangle& rect) {
        width = rect.width;
        height = rect.height;
    }
};
```

### 4.2 Copy Constructor

A **copy constructor** initializes an object using another object of the same class. It is invoked when:
- Passing an object by value to a function
- Returning an object by value from a function
- Initializing one object with another of the same type

```cpp
class Person {
private:
    string name;
    int* age;  // Dynamic memory
    
public:
    Person(string n, int a) {
        name = n;
        age = new int(a);
    }
    
    // Deep copy constructor (essential for dynamic memory)
    Person(const Person& p) {
        name = p.name;
        age = new int(*p.age);  // Allocate new memory
    }
    
    ~Person() {
        delete age;  // Destructor to free memory
    }
};
```

**Important**: Always implement a deep copy constructor when your class manages dynamic memory to avoid shallow copy problems.

### 4.3 Destructor

A **destructor** is called when an object goes out of scope or is explicitly deleted. It releases resources (like dynamic memory, file handles, network connections).

```cpp
class FileHandler {
private:
    ofstream file;
    
public:
    FileHandler(string filename) {
        file.open(filename);
    }
    
    ~FileHandler() {
        if (file.is_open()) {
            file.close();
        }
    }
};
```

---

## 5. Initializer Lists

Initializer lists provide a more efficient way to initialize class members, especially for:
- Reference members
- Const members
- Members without default constructors

```cpp
class Student {
private:
    const int rollNumber;      // Const member
    string& name;              // Reference member
    
public:
    // Using initializer list
    Student(int r, string& n) : rollNumber(r), name(n) {
        // Constructor body (minimal work needed here)
    }
};
```

**Without initializer list**, the above would not compile because `const` and reference members cannot be assigned after initialization.

---

## 6. Static Members

Static members belong to the class rather than any specific object. They are shared among all objects of the class.

### 6.1 Static Data Members

```cpp
class BankAccount {
private:
    static double interestRate;  // Shared by all accounts
    double balance;
    
public:
    static void setInterestRate(double rate) {
        interestRateRate = rate;
    }
    
    double calculateInterest() const {
        return balance * interestRate;
    }
};

// Definition outside class (required for static members)
double BankAccount::interestRate = 3.5;
```

### 6.2 Static Member Functions

Static member functions:
- Can only access static data members and other static member functions
- Can be called using the class name without creating an object
- Do not have a `this` pointer

```cpp
class Config {
private:
    static int objectCount;
    
public:
    Config() {
        objectCount++;
    }
    
    static int getObjectCount() {
        return objectCount;
    }
};

int Config::objectCount = 0;

int main() {
    Config c1, c2, c3;
    cout << Config::getObjectCount() << endl;  // Output: 3
    return 0;
}
```

---

## 7. Const Members

### 7.1 Const Objects

Once a const object is created, its data members cannot be modified.

```cpp
class Date {
private:
    int day, month, year;
    
public:
    Date(int d, int m, int y) : day(d), month(m), year(y) {}
    
    void display() const {  // Const member function
        cout << day << "/" << month << "/" << year << endl;
    }
};

int main() {
    const Date today(15, 1, 2024);
    today.display();  // OK - display is const
    // today.day = 20;  // ERROR - cannot modify const object
    return 0;
}
```

### 7.2 Const Member Functions

A const member function promises not to modify any data members of the object. This is essential for:
- Ensuring data integrity
- Allowing the function to be called on const objects
- Overloading based on const-ness

```cpp
class Vector {
private:
    double x, y;
    
public:
    Vector(double a, double b) : x(a), y(b) {}
    
    double magnitude() const {  // Cannot modify x or y
        return sqrt(x*x + y*y);
    }
    
    void scale(double factor) {  // Non-const: modifies state
        x *= factor;
        y *= factor;
    }
};
```

---

## 8. Operator Overloading

Operator overloading allows operators to work with user-defined types (classes). This makes code more intuitive and readable.

### 8.1 Overloading Arithmetic Operators

```cpp
class Complex {
private:
    double real, imag;
    
public:
    Complex(double r = 0, double i = 0) : real(r), imag(i) {}
    
    // Overload + operator
    Complex operator+(const Complex& other) const {
        return Complex(real + other.real, imag + other.imag);
    }
    
    // Overload << for output streaming
    friend ostream& operator<<(ostream& os, const Complex& c) {
        os << c.real << "+" << c.imag << "i";
        return os;
    }
};

int main() {
    Complex c1(3, 4), c2(1, 2);
    Complex c3 = c1 + c2;  // Uses overloaded +
    cout << c3 << endl;    // Output: 4+6i
    return 0;
}
```

### 8.2 Common Operators to Overload

- **Arithmetic**: `+`, `-`, `*`, `/`, `%`
- **Comparison**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Assignment**: `=`, `+=`, `-=`, `*=`, `/=`
- **Input/Output**: `<<`, `>>`
- **Subscript**: `[]`
- **Function Call**: `()`

---

## 9. Inheritance and Access Control

Inheritance allows a class (derived class) to inherit properties and behaviors from another class (base class). Access specifiers play a crucial role in inheritance.

### 9.1 Types of Inheritance

| Inheritance Type | Base public | Base protected | Base private |
|------------------|-------------|----------------|--------------|
| **public** | public → public | protected → protected | private → inaccessible |
| **protected** | public → protected | protected → protected | private → inaccessible |
| **private** | public → private | protected → private | private → inaccessible |

### 9.2 Example of Protected and Private Inheritance

```cpp
class Person {
protected:
    string name;
    int age;
    
public:
    Person(string n, int a) : name(n), age(a) {}
};

class Student : private Person {  // Private inheritance
private:
    int rollNo;
    
public:
    Student(string n, int a, int r) : Person(n, a), rollNo(r) {}
    // name and age are now private in Student
    // Only Student can access them
};

int main() {
    Student s("Alice", 20, 101);
    // s.name = "Bob";  // ERROR - name is private now
    return 0;
}
```

---

## 10. Comprehensive Example: Library Management System

This example demonstrates multiple OOP concepts in a cohesive application:

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Book {
private:
    string title;
    string author;
    int copies;
    static int totalBooks;  // Static member
    
public:
    // Constructor
    Book(string t, string a, int c) : title(t), author(a), copies(c) {
        totalBooks++;
    }
    
    // Copy constructor
    Book(const Book& b) : title(b.title), author(b.author), copies(b.copies) {
        totalBooks++;
    }
    
    // Destructor
    ~Book() {
        totalBooks--;
    }
    
    // Const member function - doesn't modify state
    void display() const {
        cout << "Title: " << title << ", Author: " << author 
             << ", Copies: " << copies << endl;
    }
    
    // Static member function
    static int getTotalBooks() {
        return totalBooks;
    }
    
    // Operator overloading
    bool operator==(const Book& other) const {
        return title == other.title && author == other.author;
    }
};

int Book::totalBooks = 0;

class Library {
private:
    vector<Book> collection;
    
public:
    void addBook(const Book& b) {
        collection.push_back(b);
    }
    
    void displayAll() const {
        for (const auto& book : collection) {
            book.display();
        }
    }
    
    int getCount() const {
        return collection.size();
    }
};

int main() {
    Library lib;
    
    Book b1("Data Structures", "Cormen", 5);
    Book b2("Algorithms", "Cormen", 3);
    Book b3("C++ Programming", "Stroustrup", 4);
    
    lib.addBook(b1);
    lib.addBook(b2);
    lib.addBook(b3);
    
    cout << "=== Library Collection ===" << endl;
    lib.displayAll();
    
    cout << "\nTotal books in library: " << lib.getCount() << endl;
    cout << "Total Book objects (static): " << Book::getTotalBooks() << endl;
    
    // Testing copy constructor
    Book b4(b1);
    cout << "\nAfter copy, total Book objects: " << Book::getTotalBooks() << endl;
    
    return 0;
}
```

---

## 11. Multiple Choice Questions (Advanced Level)

### Level 1: Basic Understanding

1. **What is the default access specifier for members of a class in C++?**
   - (a) public
   - (b) private
   - (c) protected
   - (d) None

2. **Which member function is called when an object goes out of scope?**
   - (a) Constructor
   - (b) Destructor
   - (c) Copy constructor
   - (d) Static function

### Level 2: Intermediate Concepts

3. **What is the output?**
   ```cpp
   class Test {
       static int count;
   public:
       Test() { count++; }
   };
   int Test::count = 0;
   
   int main() {
       Test t1, t2, t3;
       cout << Test::count;
       return 0;
   }
   ```
   - (a) 0
   - (b) 1
   - (c) 3
   - (d) Compilation error

4. **Which of the following is NOT a valid access specifier in C++?**
   - (a) public
   - (b) private
   - (c) protected
   - (d) hidden

5. **What does a const member function guarantee?**
   - (a) Returns a const value
   - (b) Does not modify any data members
   - (c) Cannot be called by non-const objects
   - (d) Cannot be overloaded

### Level 3: Advanced Concepts

6. **When is a copy constructor invoked?**
   - (a) Only when creating a new object
   - (b) When passing an object by value to a function
   - (c) When returning an object by value
   - (d) Both (b) and (c)

7. **In protected inheritance, public members of the base class become _____ in the derived class.**
   - (a) public
   - (b) private
   - (c) protected
   - (d) inaccessible

8. **Which is correct for initializer lists?**
   - (a) They are optional for all data members
   - (b) They are mandatory for const and reference members
   - (c) They improve performance only for built-in types
   - (d) They cannot be used with constructors

9. **What will happen if a class with dynamic memory members only has a default copy constructor?**
   - (a) Compilation error
   - (b) Shallow copy leading to double-free errors
   - (c) Deep copy automatically
   - (d) Memory leak

10. **Which operator cannot be overloaded in C++?**
    - (a) `+`
    - (b) `::`
    - (c) `[]`
    - (d) `=`

**Answer Key:** 1-(b), 2-(b), 3-(c), 4-(d), 5-(b), 6-(d), 7-(c), 8-(b), 9-(b), 10-(b)

---

## 12. Flashcards for Quick Review

### Card 1
**Q:** What is the difference between `public` and `private` access specifiers?

**A:** `public` members are accessible from anywhere; `private` members are only accessible within the class itself and by friend functions. Private members implement data hiding.

### Card 2
**Q:** When is a copy constructor called?

**A:** It is called when: (1) initializing an object with another object of the same type, (2) passing an object by value to a function, (3) returning an object by value from a function.

### Card 3
**Q:** Why use initializer lists?

**A:** Initializer lists are necessary for initializing const members, reference members, and members without default constructors. They also provide better performance by avoiding default initialization followed by assignment.

### Card 4
**Q:** What is the purpose of the `static` keyword in a class?

**A:** Static members (data or functions) belong to the class rather than any specific object. They are shared among all objects and can be accessed using the class name without creating an object.

### Card 5
**Q:** What guarantees does a `const` member function provide?

**A:** A const member function promises not to modify any non-static data members of the object. It can be called on both const and non-const objects, enabling function overloading based on const-ness.

### Card 6
**Q:** What is the difference between shallow copy and deep copy?

**A:** Shallow copy copies pointer values (address), so multiple objects share the same memory. Deep copy allocates new memory and copies the actual data, ensuring independent memory for each object.

### Card 7
**Q:** What is encapsulation?

**A:** Encapsulation is bundling data and methods that operate on that data into a single unit (class), while restricting direct access to some components to ensure data integrity and implementation hiding.

### Card 8
**Q:** What happens in private inheritance?

**A:** In private inheritance, all public and protected members of the base class become private in the derived class. This makes the derived class "has-a" relationship but hides the base class interface.

---

## 13. Key Takeaways

1. **Classes and Objects**: Classes are blueprints; objects are instances with their own memory for non-static members.

2. **Access Modifiers**: Use `private` for data hiding, `public` for interfaces, and `protected` for inheritance scenarios.

3. **Constructors**: Include default, parameterized, and copy constructors to handle different initialization scenarios. Always implement a deep copy constructor when your class manages dynamic memory.

4. **Destructors**: Essential for releasing resources (memory, files, network connections). Rule of Three: if you need to define destructor, copy constructor, or copy assignment, you likely need all three.

5. **Initializer Lists**: Mandatory for const members, reference members, and members requiring initialization without default constructors.

6. **Static Members**: Shared across all objects; accessed via class name. Static member functions can only access static members.

7. **Const Correctness**: Use const for objects and member functions to ensure data integrity and enable function overloading.

8. **Operator Overloading**: Makes user-defined types behave like built-in types, improving code readability and intuitiveness.

9. **Inheritance Access**: Choose inheritance type carefully—`public` for "is-a", `private` for "implemented in terms of", `protected` for limited inheritance.

10. **Encapsulation**: Beyond data hiding, it involves providing clean interfaces, validating inputs, and allowing implementation changes without affecting users.

---

*This study material aligns with the Delhi University BSc (Hons) Computer Science NEP 2024 UGCF syllabus, covering all essential topics for comprehensive understanding of Classes, Objects, and Modifiers in C++.*