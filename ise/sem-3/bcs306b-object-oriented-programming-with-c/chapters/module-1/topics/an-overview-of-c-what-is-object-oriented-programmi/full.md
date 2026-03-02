# **An Overview of C++: What is Object-Oriented Programming? Introducing C++ Classes**

## **Module 5: 5 Hours**

### Table of Contents

1. [Introduction to Object-Oriented Programming](#introduction-to-object-oriented-programming)
   - [History of Object-Oriented Programming](#history-of-object-oriented-programming)
   - [Key Concepts](#key-concepts)
   - [Benefits of Object-Oriented Programming](#benefits-of-object-oriented-programming)
2. [What is Object-Oriented Programming in C++?](#what-is-object-oriented-programming-in-c++)
   - [Class Definition in C++](#class-definition-in-c++)
   - [Inheritance in C++](#inheritance-in-c++)
   - [Polymorphism in C++](#polymorphism-in-c++)
   - [Encapsulation in C++](#encapsulation-in-c++)
3. [Introducing C++ Classes](#introducing-c++-classes)
   - [Class Declaration](#class-declaration)
   - [Member Variables](#member-variables)
   - [Member Functions](#member-functions)
   - [Constructors](#constructors)
   - [Destructors](#destructors)
4. [Example: Simple C++ Class](#example-simple-c++-class)
5. [Case Study: Real-World Application of Object-Oriented Programming in C++](#case-study-real-world-application-of-object-oriented-programming-in-c++)
6. [Applications of Object-Oriented Programming in C++](#applications-of-object-oriented-programming-in-c++)
7. [Historical Context and Modern Developments](#historical-context-and-modern-developments)
8. [Conclusion](#conclusion)
9. [Further Reading](#further-reading)

### Introduction to Object-Oriented Programming

---

Object-Oriented Programming (OOP) is a programming paradigm that revolves around the concept of objects and classes. It was first introduced in the 1960s by Alan Kay and later popularized by C++.

#### History of Object-Oriented Programming

The concept of OOP was first introduced in 1965 by Alan Kay, a computer scientist who worked at Xerox PARC. At that time, Kay was designing a new programming language called Simula, which was the first language to support object-oriented programming. However, it was C++ that popularized OOP and made it accessible to a wider audience.

#### Key Concepts

Object-Oriented Programming is based on the following key concepts:

- **Classes**: These are blueprints or templates that define the characteristics and behavior of an object.
- **Objects**: These are instances of classes and have their own set of attributes and methods.
- **Inheritance**: This is the process of creating a new class based on an existing class.
- **Polymorphism**: This is the ability of an object to take on multiple forms.
- **Encapsulation**: This is the process of hiding the implementation details of an object from the outside world.

#### Benefits of Object-Oriented Programming

Object-Oriented Programming has several benefits:

- **Modularity**: OOP promotes modularity, which means that code is organized into smaller, independent units that can be easily modified or replaced.
- **Reusability**: OOP promotes reusability, which means that code can be reused in multiple contexts.
- **Flexibility**: OOP promotes flexibility, which means that code can be easily modified or extended to meet changing requirements.

### What is Object-Oriented Programming in C++?

---

In C++, object-oriented programming is implemented using classes. A class is a blueprint or template that defines the characteristics and behavior of an object.

#### Class Definition in C++

A class is defined using the `class` keyword followed by the name of the class and the members of the class.

```cpp
class MyClass {
public:
    // Member variables
    int x;
    double y;

    // Member functions
    void printValues();
};
```

#### Inheritance in C++

Inheritance is the process of creating a new class based on an existing class. The new class inherits the members of the existing class and can also add new members or override the members of the existing class.

```cpp
class Animal {
public:
    void eat();
};

class Dog : public Animal {
public:
    void bark();
};

int main() {
    Dog dog;
    dog.eat();  // Calls the eat() function from the Animal class
    dog.bark(); // Calls the bark() function from the Dog class
    return 0;
}
```

#### Polymorphism in C++

Polymorphism is the ability of an object to take on multiple forms. This can be achieved using function overloading or function overriding.

```cpp
class Shape {
public:
    virtual void draw() = 0;
};

class Circle : public Shape {
public:
    void draw() {
        std::cout << "Drawing a circle." << std::endl;
    }
};

class Rectangle : public Shape {
public:
    void draw() {
        std::cout << "Drawing a rectangle." << std::endl;
    }
};

int main() {
    Shape* shape = new Circle();
    shape->draw(); // Outputs: Drawing a circle.
    shape = new Rectangle();
    shape->draw(); // Outputs: Drawing a rectangle.
    return 0;
}
```

#### Encapsulation in C++

Encapsulation is the process of hiding the implementation details of an object from the outside world. This can be achieved using access specifiers (public, private, protected).

```cpp
class BankAccount {
private:
    double balance;

public:
    BankAccount(double initialBalance) : balance(initialBalance) {}

    void deposit(double amount) {
        balance += amount;
    }

    double getBalance() {
        return balance;
    }
};
```

### Introducing C++ Classes

---

A C++ class is a blueprint or template that defines the characteristics and behavior of an object. It consists of member variables and member functions.

#### Class Declaration

A class declaration starts with the `class` keyword followed by the name of the class.

```cpp
class MyClass {
public:
    // Member variables
    int x;
    double y;

    // Member functions
    void printValues();
};
```

#### Member Variables

Member variables are the data members of a class. They are declared inside the class declaration.

```cpp
class MyClass {
public:
    int x;
    double y;

    // Member functions
    void printValues();
};
```

#### Member Functions

Member functions are the behavior members of a class. They are declared inside the class declaration.

```cpp
class MyClass {
public:
    int x;
    double y;

    void printValues() {
        std::cout << "x = " << x << std::endl;
        std::cout << "y = " << y << std::endl;
    }
};
```

#### Constructors

Constructors are special member functions that are called when an object is created. They are used to initialize the member variables of a class.

```cpp
class MyClass {
public:
    MyClass(int x, double y) : x(x), y(y) {}

    void printValues() {
        std::cout << "x = " << x << std::endl;
        std::cout << "y = " << y << std::endl;
    }
};
```

#### Destructors

Destructors are special member functions that are called when an object is destroyed. They are used to release the resources held by an object.

```cpp
class MyClass {
public:
    ~MyClass() {
        std::cout << "Destruction of MyClass." << std::endl;
    }

    MyClass(int x, double y) : x(x), y(y) {}

    void printValues() {
        std::cout << "x = " << x << std::endl;
        std::cout << "y = " << y << std::endl;
    }
};
```

### Example: Simple C++ Class

---

In this example, we create a simple C++ class called `MyClass` with member variables `x` and `y`, and member functions `printValues`.

```cpp
class MyClass {
public:
    int x;
    double y;

    void printValues() {
        std::cout << "x = " << x << std::endl;
        std::cout << "y = " << y << std::endl;
    }
};

int main() {
    MyClass obj;
    obj.x = 10;
    obj.y = 20.5;
    obj.printValues();
    return 0;
}
```

### Case Study: Real-World Application of Object-Oriented Programming in C++

---

In this case study, we consider a real-world application of object-oriented programming in C++.

Suppose we are designing a system to manage a university's student database. We can create a class called `Student` to represent a student with attributes such as name, age, and course.

```cpp
class Student {
public:
    std::string name;
    int age;
    std::string course;

    void displayDetails() {
        std::cout << "Name: " << name << std::endl;
        std::cout << "Age: " << age << std::endl;
        std::cout << "Course: " << course << std::endl;
    }
};
```

We can then create a class called `University` to manage the student database.

```cpp
class University {
public:
    std::list<Student> students;

    void addStudent(Student student) {
        students.push_back(student);
    }

    void removeStudent(Student student) {
        students.erase(std::remove(students.begin(), students.end(), student), students.end());
    }
};
```

We can then create objects of the `Student` and `University` classes and use them to manage the student database.

```cpp
int main() {
    University university;
    Student student1;
    student1.name = "John Doe";
    student1.age = 20;
    student1.course = "Computer Science";
    university.addStudent(student1);

    Student student2;
    student2.name = "Jane Doe";
    student2.age = 22;
    student2.course = "Mathematics";
    university.addStudent(student2);

    university.displayStudents();
    return 0;
}
```

### Applications of Object-Oriented Programming in C++

---

Object-oriented programming has numerous applications in C++.

- **Game Development**: OOP is widely used in game development to create 3D models and animate characters.
- **Database Management**: OOP is used to manage complex database systems and ensure data integrity.
- **Network Programming**: OOP is used to create network applications that can handle multiple connections and communication protocols.
- **Web Development**: OOP is used to create web applications that can handle user interactions and dynamic content.

### Historical Context and Modern Developments

---

Object-oriented programming has a rich history that spans several decades.

- **1960s**: The concept of OOP was first introduced by Alan Kay and his team at Xerox PARC.
- **1970s**: The first OOP languages, such as Simula and Smalltalk, were developed.
- **1980s**: C++ was developed, which popularized OOP and made it accessible to a wider audience.
- **1990s**: OOP became widely adopted in industry and academia.

In recent years, there has been a resurgence of interest in OOP, driven by the rise of cloud computing and big data.

- **Cloud Computing**: OOP is used to create scalable and modular cloud applications.
- **Big Data**: OOP is used to analyze and process large datasets using complex algorithms.

### Conclusion

---

In conclusion, object-oriented programming is a powerful paradigm that has numerous applications in C++. It has a rich history that spans several decades, and its popularity continues to grow in industry and academia.

By understanding the key concepts, benefits, and applications of OOP, you can create more efficient, scalable, and maintainable software systems.

### Further Reading

---

- "The C++ Programming Language" by Bjarne Stroustrup
- "Object-Oriented Software Construction" by Bertrand Meyer
- "Design Patterns: Elements of Reusable Object-Oriented Software" by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides
