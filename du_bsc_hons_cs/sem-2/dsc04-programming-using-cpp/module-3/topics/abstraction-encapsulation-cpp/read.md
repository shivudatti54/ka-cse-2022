# Abstraction and Encapsulation in C++
## Introduction

Abstraction and encapsulation are two fundamental concepts in object-oriented programming (OOP) that help in designing robust, maintainable, and scalable software systems. Abstraction is the process of exposing only the necessary information to the outside world while hiding the implementation details. Encapsulation is the concept of bundling data and its associated methods that operate on that data within a single unit, making it harder for other parts of the program to access or modify the data directly.

In C++, abstraction and encapsulation are achieved using classes and objects. A class is a blueprint or a template that defines the properties and behavior of an object. An object is an instance of a class, and it has its own set of attributes (data) and methods (functions).

## Key Concepts

### Classes and Objects

In C++, a class is defined using the `class` keyword followed by the name of the class. The class definition includes the data members (attributes) and member functions (methods). An object is created by instantiating a class.

```cpp
class Car {
    private:
        string brand;
        string model;
        int year;

    public:
        void setBrand(string b) {
            brand = b;
        }

        void setModel(string m) {
            model = m;
        }

        void setYear(int y) {
            year = y;
        }

        void printDetails() {
            cout << "Brand: " << brand << endl;
            cout << "Model: " << model << endl;
            cout << "Year: " << year << endl;
        }
};
```

### Access Modifiers

Access modifiers are used to control access to the members of a class. C++ provides three access modifiers:

*   `public`: Members declared as `public` are accessible from anywhere in the program.
*   `private`: Members declared as `private` are accessible only within the class itself.
*   `protected`: Members declared as `protected` are accessible within the class itself and within any class derived from that class.

### Abstraction

Abstraction is achieved by exposing only the necessary information to the outside world while hiding the implementation details. In C++, abstraction is achieved using abstract classes and interfaces.

```cpp
class Shape {
    public:
        virtual void draw() = 0;
};

class Circle : public Shape {
    public:
        void draw() {
            cout << "Drawing a circle." << endl;
        }
};

class Rectangle : public Shape {
    public:
        void draw() {
            cout << "Drawing a rectangle." << endl;
        }
};
```

### Encapsulation

Encapsulation is achieved by bundling data and its associated methods that operate on that data within a single unit. In C++, encapsulation is achieved using classes and objects.

```cpp
class BankAccount {
    private:
        double balance;

    public:
        void deposit(double amount) {
            balance += amount;
        }

        void withdraw(double amount) {
            if (balance >= amount) {
                balance -= amount;
            } else {
                cout << "Insufficient balance." << endl;
            }
        }

        double getBalance() {
            return balance;
        }
};
```

## Examples

### Example 1: Abstraction

```cpp
class Animal {
    public:
        virtual void sound() = 0;
};

class Dog : public Animal {
    public:
        void sound() {
            cout << "The dog barks." << endl;
        }
};

class Cat : public Animal {
    public:
        void sound() {
            cout << "The cat meows." << endl;
        }
};

int main() {
    Animal* dog = new Dog();
    Animal* cat = new Cat();

    dog->sound();
    cat->sound();

    return 0;
}
```

### Example 2: Encapsulation

```cpp
class Student {
    private:
        string name;
        int age;

    public:
        void setName(string n) {
            name = n;
        }

        void setAge(int a) {
            age = a;
        }

        void printDetails() {
            cout << "Name: " << name << endl;
            cout << "Age: " << age << endl;
        }
};

int main() {
    Student student;
    student.setName("John Doe");
    student.setAge(20);
    student.printDetails();

    return 0;
}
```

## Exam Tips

1.  Understand the concepts of abstraction and encapsulation.
2.  Learn how to implement abstraction using abstract classes and interfaces.
3.  Learn how to implement encapsulation using classes and objects.
4.  Understand the use of access modifiers to control access to class members.
5.  Practice creating classes and objects to solve real-world problems.
6.  Learn how to use inheritance to create a hierarchy of classes.
7.  Understand the concept of polymorphism and how to achieve it using function overriding and function overloading.