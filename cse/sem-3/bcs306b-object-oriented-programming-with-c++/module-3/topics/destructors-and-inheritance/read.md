# Destructors and Inheritance in C++

## Introduction

Destructors are special member functions in C++ that perform cleanup operations when an object goes out of scope or is explicitly deleted. They play a crucial role in resource management, ensuring proper release of dynamically allocated memory, file handles, network connections, and other system resources. In object-oriented programming with C++, understanding destructors becomes particularly important when working with inheritance, as the order of destructor execution and the use of virtual destructors significantly impact program behavior and memory management.

Inheritance, one of the fundamental pillars of object-oriented programming, allows creating new classes (derived classes) from existing classes (base classes). When destructors are involved in an inheritance hierarchy, special considerations must be made to ensure that base class cleanup occurs properly after derived class cleanup. This topic explores the intricacies of destructors in the context of inheritance, including virtual destructors, order of destructor calls, and common pitfalls that developers must avoid to write robust C++ code.

For university examinations, this topic carries significant weight as it tests the student's understanding of object lifecycle management and polymorphism - essential concepts for any C++ developer.

## Key Concepts

### Destructors: Definition and Characteristics

A destructor is a special member function that has the same name as the class preceded by a tilde (~) symbol. It is automatically called when an object is destroyed. Unlike constructors, destructors do not take any parameters and cannot be overloaded - each class can have at most one destructor.

**Characteristics of Destructors:**

- Same name as class preceded by ~
- No return type (not even void)
- Cannot be overloaded (only one per class)
- Automatically invoked when object goes out of scope
- If no destructor is defined, compiler generates a default destructor
- Should be declared public for automatic invocation

```cpp
class Student {
private:
 char* name;
 int age;
public:
 // Constructor
 Student(const char* n, int a) {
 name = new char[strlen(n) + 1];
 strcpy(name, n);
 age = a;
 }

 // Destructor
 ~Student() {
 delete[] name; // Release dynamically allocated memory
 }
};
```

### Need for Destructors

Destructors are essential for:

1. **Memory Deallocation**: Releasing dynamically allocated memory using `delete` or `delete[]`
2. **Resource Cleanup**: Closing file handles, database connections, network sockets
3. **Logging**: Recording object destruction for debugging or audit purposes
4. **Releasing Locks**: In multithreaded applications, releasing acquired locks

Without proper destructor implementation, programs suffer from memory leaks and resource exhaustion.

### Destructors in Inheritance

When a class hierarchy exists, understanding the order of destructor calls is critical. In C++, destructors are called in the reverse order of construction - derived class destructor executes first, followed by base class destructor. This ensures that derived class resources are cleaned up before base class resources.

**Order of Destructor Execution:**

1. Derived class destructor executes
2. Members of derived class are destroyed in reverse order of declaration
3. Base class destructor executes
4. Members of base class are destroyed in reverse order of declaration

```cpp
#include <iostream>
using namespace std;

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

int main() {
 Derived obj;
 return 0;
}
```

**Output:**

```
Base Constructor
Derived Constructor
Derived Destructor
Base Destructor
```

### Virtual Destructors

When a base class pointer points to a derived class object and we delete through the base pointer, only the base class destructor gets called if destructors are not virtual. This leads to undefined behavior and resource leaks in derived classes.

**The Problem Without Virtual Destructors:**

```cpp
class Base {
public:
 ~Base() { cout << "Base Destructor\n"; }
};

class Derived : public Base {
 int* arr;
public:
 Derived() { arr = new int[100]; }
 ~Derived() {
 delete[] arr;
 cout << "Derived Destructor\n";
 }
};

int main() {
 Base* ptr = new Derived();
 delete ptr; // Only Base destructor called - MEMORY LEAK!
 return 0;
}
```

**Solution - Virtual Destructors:**

```cpp
class Base {
public:
 virtual ~Base() { cout << "Base Destructor\n"; }
};

class Derived : public Base {
 int* arr;
public:
 Derived() { arr = new int[100]; }
 ~Derived() {
 delete[] arr;
 cout << "Derived Destructor\n";
 }
};

int main() {
 Base* ptr = new Derived();
 delete ptr; // Both destructors called correctly
 return 0;
}
```

**Output with Virtual Destructor:**

```
Derived Destructor
Base Destructor
```

### Pure Virtual Destructors

A class with a pure virtual destructor must still provide a function body for the destructor. This is because derived classes inherit the pure virtual destructor's implementation. Pure virtual destructors are useful when you want to create an abstract base class that serves as an interface.

```cpp
class AbstractBase {
public:
 virtual ~AbstractBase() = 0; // Pure virtual destructor
};

// Must provide implementation for pure virtual destructor
AbstractBase::~AbstractBase() {
 cout << "AbstractBase Destructor\n";
}

class ConcreteClass : public AbstractBase {
public:
 ~ConcreteClass() { cout << "ConcreteClass Destructor\n"; }
};

int main() {
 ConcreteClass obj;
 return 0;
}
```

### Virtual Destructor Rules and Guidelines

1. **Always use virtual destructors in polymorphic base classes**: When a class is designed to be inherited and objects of derived classes are deleted through base class pointers, the base class destructor must be virtual.

2. **Virtual destructor adds small runtime overhead**: Virtual destructors introduce virtual table (vtable) lookup overhead, but this is necessary for correct behavior.

3. **Not all classes need virtual destructors**: Classes not designed for inheritance or not used polymorphically don't require virtual destructors.

4. **Destructor of derived class automatically becomes virtual**: If base class destructor is virtual, derived class destructor is also virtual regardless of whether it's explicitly marked.

## Examples

### Example 1: Demonstrating Destructor Order in Inheritance

```cpp
#include <iostream>
using namespace std;

class Vehicle {
 string brand;
public:
 Vehicle(string b) : brand(b) {
 cout << "Vehicle constructor: " << brand << endl;
 }
 virtual ~Vehicle() {
 cout << "Vehicle destructor: " << brand << endl;
 }
};

class Car : public Vehicle {
 int seats;
public:
 Car(string b, int s) : Vehicle(b), seats(s) {
 cout << "Car constructor: " << seats << " seater" << endl;
 }
 ~Car() {
 cout << "Car destructor" << endl;
 }
};

class SportsCar : public Car {
 int topSpeed;
public:
 SportsCar(string b, int s, int speed) : Car(b, s), topSpeed(speed) {
 cout << "SportsCar constructor: " << topSpeed << " km/h" << endl;
 }
 ~SportsCar() {
 cout << "SportsCar destructor" << endl;
 }
};

int main() {
 SportsCar* obj = new SportsCar("Ferrari", 2, 350);
 delete obj;
 return 0;
}
```

**Output:**

```
Vehicle constructor: Ferrari
Car constructor: 2 seater
SportsCar constructor: 350 km/h
SportsCar destructor
Car destructor
Vehicle destructor: Ferrari
```

### Example 2: Polymorphic Deletion Without Virtual Destructor (INCORRECT)

```cpp
#include <iostream>
using namespace std;

class Animal {
public:
 Animal() { cout << "Animal created\n"; }
 ~Animal() { cout << "Animal destroyed\n"; }
};

class Dog : public Animal {
 string* name;
public:
 Dog(string n) {
 name = new string(n);
 cout << "Dog created: " << *name << endl;
 }
 ~Dog() {
 cout << "Dog destroyed" << endl;
 delete name; // This never gets called!
 }
};

int main() {
 Animal* ptr = new Dog("Buddy");
 cout << "--- Deleting through base pointer ---\n";
 delete ptr;
 return 0;
}
```

**Output:**

```
Animal created
Dog created: Buddy
--- Deleting through base pointer ---
Animal destroyed
```

Notice that "Dog destroyed" never prints, causing a memory leak!

### Example 3: Fixing with Virtual Destructor

```cpp
#include <iostream>
using namespace std;

class Animal {
public:
 Animal() { cout << "Animal created\n"; }
 virtual ~Animal() { cout << "Animal destroyed\n"; }
};

class Dog : public Animal {
 string* name;
public:
 Dog(string n) {
 name = new string(n);
 cout << "Dog created: " << *name << endl;
 }
 ~Dog() {
 delete name;
 cout << "Dog destroyed" << endl;
 }
};

int main() {
 Animal* ptr = new Dog("Buddy");
 cout << "--- Deleting through base pointer ---\n";
 delete ptr;
 return 0;
}
```

**Output:**

```
Animal created
Dog created: Buddy
--- Deleting through base pointer ---
Dog destroyed
Animal destroyed
```

Both destructors are called in correct order!

## Exam Tips

1. **Remember the order**: Constructors execute from base to derived, destructors execute from derived to base (reverse order of construction).

2. **Virtual destructor is mandatory for polymorphic deletion**: If a base pointer points to derived object and is deleted, base destructor must be virtual.

3. **Destructors cannot be overloaded**: Each class can have only one destructor, and it takes no arguments.

4. **Pure virtual destructor needs implementation**: Unlike pure virtual functions, a pure virtual destructor must have a function body.

5. **Default destructor is provided by compiler**: If no destructor is defined, compiler generates one that calls member destructors.

6. **Virtual keyword inheritance**: If base destructor is virtual, derived destructors automatically become virtual.

7. **Memory leak occurs without virtual destructor**: In polymorphic scenarios, non-virtual destructors cause resource leaks in derived classes.

8. **Time of destructor invocation**: Automatic storage objects are destroyed when they go out of scope; dynamically allocated objects when delete is called.

9. **Static objects destruction**: Static objects are destroyed after main() function ends, in reverse order of construction.

10. **Array deletion**: Always use delete[] for arrays, delete for single objects - mixing these causes undefined behavior.
