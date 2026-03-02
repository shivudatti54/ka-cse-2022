# Inheritance and Protected Members in C++

## Introduction

Inheritance is one of the fundamental pillars of object-oriented programming (OOP) that enables the creation of new classes (derived classes) from existing classes (base classes). This powerful mechanism promotes code reusability, extensibility, and establishes a natural hierarchical relationship between classes. In the context of software development, inheritance allows programmers to model real-world relationships where specialized classes inherit properties and behaviors from more general classes.

The protected access specifier in C++ plays a crucial role in inheritance by providing a middle ground between public and private access. It allows derived classes to access base class members while still maintaining encapsulation from outside the class. Understanding how protected members work in conjunction with inheritance is essential for designing robust and maintainable C++ applications. This topic forms the foundation for understanding polymorphism and virtual functions, which are advanced OOP concepts heavily tested in university examinations.

## Key Concepts

### 1. Inheritance Basics

Inheritance enables a class to acquire the properties and behaviors of another class. The class that inherits is called the derived class (or subclass), and the class being inherited from is called the base class (or superclass). The syntax for inheritance involves specifying the base class name after a colon followed by the type of inheritance.

```cpp
class BaseClass {
 // base class members
};

class DerivedClass : public BaseClass {
 // derived class members
};
```

### 2. Types of Inheritance

**Single Inheritance**: A derived class inherits from only one base class. This is the simplest form where one class derives from another.

**Multiple Inheritance**: A derived class inherits from more than one base class. The syntax uses commas to separate base classes.

```cpp
class Derived : public Base1, public Base2 {
 // members
};
```

**Multilevel Inheritance**: A class is derived from a class that is itself derived from another class, creating a chain of inheritance.

**Hierarchical Inheritance**: Multiple derived classes inherit from a single base class.

**Hybrid Inheritance**: A combination of two or more types of inheritance, often requiring virtual base classes to avoid ambiguity.

### 3. Protected Access Specifier

The protected keyword creates members that are accessible within the class and its derived classes, but not from objects of the class outside the inheritance hierarchy. This makes it particularly useful for allowing subclasses to access implementation details while hiding them from other code.

```cpp
class Base {
protected:
 int protectedVar; // accessible in derived classes
private:
 int privateVar; // not accessible in derived classes
public:
 int publicVar; // accessible everywhere
};
```

### 4. Modes of Inheritance

**Public Inheritance**: Public and protected members of base class remain public and protected respectively in derived class. Private members remain private and are not directly accessible.

**Protected Inheritance**: Public and protected members become protected in derived class. This restricts accessibility to derived classes only.

**Private Inheritance**: Public and protected members become private in derived class. This is rarely used but useful for implementation inheritance.

### 5. Constructors and Destructors in Inheritance

When a derived class object is created, the base class constructor executes before the derived class constructor. Similarly, destructors execute in reverse order (derived first, then base). Derived class constructors can call base class constructors using an initializer list.

```cpp
class Base {
public:
 Base() { cout << "Base Constructor\n"; }
 ~Base() { cout << "Base Destructor\n"; }
};

class Derived : public Base {
public:
 Derived() { cout << "Derived Constructor\n"; }
 ~Derived() { cout << "Derived Destructor\n"; }
};
```

### 6. Access Control Summary

| Base Member | Public Inheritance | Protected Inheritance | Private Inheritance |
| ----------- | ------------------ | --------------------- | ------------------- |
| Private     | Not accessible     | Not accessible        | Not accessible      |
| Protected   | Protected          | Protected             | Private             |
| Public      | Public             | Protected             | Private             |

## Examples

### Example 1: Single Inheritance with Protected Members

**Problem**: Create a base class `Animal` with protected data members for name and age, and a derived class `Dog` that adds breed information.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Animal {
protected:
 string name;
 int age;
public:
 Animal(string n, int a) : name(n), age(a) {}
 void display() {
 cout << "Name: " << name << ", Age: " << age << endl;
 }
};

class Dog : public Animal {
private:
 string breed;
public:
 Dog(string n, int a, string b) : Animal(n, a), breed(b) {}
 void showDogDetails() {
 // Accessing protected members from base class
 cout << "Dog Name: " << name << endl;
 cout << "Dog Age: " << age << " years" << endl;
 cout << "Breed: " << breed << endl;
 }
};

int main() {
 Dog d("Buddy", 3, "Golden Retriever");
 d.showDogDetails();
 d.display(); // public method of base class
 return 0;
}
```

**Output**:

```
Dog Name: Buddy
Dog Age: 3 years
Breed: Golden Retriever
Name: Buddy, Age: 3
```

### Example 2: Multiple Inheritance

**Problem**: Create two base classes `Teacher` and `Student`, and a derived class `TeachingAssistant` that inherits from both.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Teacher {
protected:
 string subject;
public:
 Teacher(string s) : subject(s) {}
 void teach() { cout << "Teaching " << subject << endl; }
};

class Student {
protected:
 string course;
public:
 Student(string c) : course(c) {}
 void study() { cout << "Studying " << course << endl; }
};

class TeachingAssistant : public Teacher, public Student {
private:
 string name;
public:
 TeachingAssistant(string n, string s, string c)
 : Teacher(s), Student(c), name(n) {}
 void display() {
 cout << "TA Name: " << name << endl;
 teach();
 study();
 }
};

int main() {
 TeachingAssistant ta("John", "Mathematics", "Computer Science");
 ta.display();
 return 0;
}
```

### Example 3: Constructor Chaining in Inheritance

**Problem**: Demonstrate constructor and destructor call order in multilevel inheritance.

```cpp
#include <iostream>
using namespace std;

class GrandParent {
public:
 GrandParent() { cout << "GrandParent Constructor\n"; }
 ~GrandParent() { cout << "GrandParent Destructor\n"; }
};

class Parent : public GrandParent {
public:
 Parent() { cout << "Parent Constructor\n"; }
 ~Parent() { cout << "Parent Destructor\n"; }
};

class Child : public Parent {
public:
 Child() { cout << "Child Constructor\n"; }
 ~Child() { cout << "Child Destructor\n"; }
};

int main() {
 cout << "Creating object:\n";
 Child obj;
 cout << "\nDestroying object:\n";
 return 0;
}
```

**Output**:

```
Creating object:
GrandParent Constructor
Parent Constructor
Child Constructor

Destroying object:
Child Destructor
Parent Destructor
GrandParent Destructor
```

## Exam Tips

1. **Remember the order of constructor execution**: In inheritance, base class constructors execute before derived class constructors. Destructors execute in reverse order.

2. **Protected vs Private**: Protected members are accessible in derived classes, while private members are not directly accessible even in derived classes.

3. **Default inheritance type**: If no access specifier is mentioned during inheritance, classes default to private inheritance for classes and public inheritance for structures.

4. **Multiple inheritance ambiguity**: When using multiple inheritance, if two base classes have members with the same name, use scope resolution operator (::) to specify which member to use.

5. **Constructor initializer list**: Always use initializer list to call base class constructors, not assignment inside the constructor body.

6. **Virtual base classes**: In hybrid inheritance, use virtual keyword to avoid duplicate copies of base class. This is crucial for preventing ambiguity in diamond problem.

7. **Slicing problem**: When a derived class object is assigned to a base class object, only the base portion is copied (slicing), losing derived class-specific features.

8. **Protected access in main()**: Remember that protected members cannot be accessed directly in main() using object of derived class - only public members can be accessed.

9. **IS-A vs HAS-A**: Inheritance represents IS-A relationship (Dog IS-A Animal), while composition (having a member object) represents HAS-A relationship.

10. **university frequently asks**: Drawing inheritance hierarchies, predicting output based on constructor/destructor order, and identifying access specifier effects in various inheritance modes.
