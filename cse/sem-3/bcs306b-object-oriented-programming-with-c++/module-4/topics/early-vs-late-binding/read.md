# Early Binding vs Late Binding in C++

## Introduction

In object-oriented programming with C++, understanding the difference between early binding and late binding is fundamental to grasping how polymorphism works at runtime. Binding refers to the process of associating a function call with the actual function implementation that gets executed. The timing of this association—whether it occurs during compilation (early binding) or during program execution (late binding)—has significant implications for code performance, flexibility, and maintainability.

Early binding, also known as static binding, occurs when the compiler determines which function to call at compile-time based on the type of the object. This is the default behavior in C++ for non-virtual functions and provides excellent performance since no runtime overhead is required. Late binding, or dynamic binding, defers the function resolution until runtime, allowing the program to decide which function to execute based on the actual object type, not the pointer or reference type. This mechanism is essential for achieving runtime polymorphism through virtual functions.

In the context of the university's BCS306B syllabus, this topic forms the foundation for understanding virtual functions, abstract classes, and runtime polymorphism—concepts that are frequently tested in university examinations and are crucial for developing flexible, extensible software systems.

## Key Concepts

### What is Binding?

Binding is the process where a function call is linked to the appropriate function implementation. The moment this linking occurs determines whether we have early binding or late binding. In C++, the type of the object determines which binding mechanism is used: static types lead to early binding, while virtual functions trigger late binding.

### Early Binding (Static Binding)

Early binding occurs at compile time. The compiler resolves the function call by examining the static type of the object or pointer. When you call a non-virtual function, the compiler knows exactly which function to call and can insert the direct memory address of that function into the call instruction.

**Characteristics of Early Binding:**

- Resolved at compile time
- No runtime overhead—excellent performance
- Compiler performs type checking
- Used for non-virtual functions, overloaded functions, and operators
- Function calls are resolved based on the declared type, not the actual object type

**Example of Early Binding:**

```cpp
class Base {
public:
 void display() {
 cout << "Base display" << endl;
 }
};

class Derived : public Base {
public:
 void display() {
 cout << "Derived display" << endl;
 }
};

int main() {
 Base* ptr = new Derived();
 ptr->display(); // Early binding: calls Base::display()
 return 0;
}
```

In this example, since `display()` is not declared as virtual, the compiler uses early binding and calls `Base::display()` regardless of whether `ptr` points to a `Derived` object.

### Late Binding (Dynamic Binding)

Late binding occurs at runtime. The compiler generates code that determines which function to call during program execution, typically through the use of virtual function tables (vtables). This enables runtime polymorphism, where the actual function executed depends on the runtime type of the object.

**Characteristics of Late Binding:**

- Resolved at runtime using the virtual function mechanism
- Small runtime overhead due to vtable lookup
- Enables true polymorphism
- Requires virtual keyword for member functions
- Supports runtime type identification (RTTI)

### Virtual Functions and Vtables

When a class contains virtual functions, the compiler creates a virtual function table (vtable) for that class. Each object of that class contains a hidden pointer (vptr) that points to its class's vtable. At runtime, the vptr is used to look up the correct function address.

**How Vtables Work:**

1. Each class with virtual functions has its own vtable
2. The vtable is an array of function pointers
3. Each object contains a vptr pointing to its class's vtable
4. Virtual function calls go through the vptr and vtable
5. Derived classes override virtual functions by replacing entries in their vtable

### Virtual Destructors

Virtual destructors are crucial when dealing with polymorphism. If a base class pointer points to a derived class object and the destructor is not virtual, only the base class destructor executes, causing resource leaks.

```cpp
class Base {
public:
 virtual ~Base() {
 cout << "Base destructor" << endl;
 }
};

class Derived : public Base {
public:
 ~Derived() {
 cout << "Derived destructor" << endl;
 }
};

int main() {
 Base* ptr = new Derived();
 delete ptr; // Calls both destructors due to virtual destructor
 return 0;
}
```

### Pure Virtual Functions and Abstract Classes

A pure virtual function is declared by assigning 0 in the declaration:

```cpp
virtual void display() = 0;
```

Classes containing pure virtual functions become abstract classes and cannot be instantiated. They define interfaces that derived classes must implement.

### Runtime Type Information (RTTI)

C++ provides RTTI through `dynamic_cast` and `typeid` operators for safe type checking at runtime. RTTI works only with polymorphic types (classes containing virtual functions).

```cpp
#include <typeinfo>

Base* ptr = new Derived();
if (Derived* dptr = dynamic_cast<Derived*>(ptr)) {
 cout << "Successfully cast to Derived" << endl;
}
```

## Examples

### Example 1: Demonstrating Early vs Late Binding

```cpp
#include <iostream>
using namespace std;

class Animal {
public:
 void speak() { // Non-virtual - Early binding
 cout << "Animal speaks" << endl;
 }

 virtual void eat() { // Virtual - Late binding
 cout << "Animal eats" << endl;
 }
};

class Dog : public Animal {
public:
 void speak() { // Hides base class function
 cout << "Dog barks" << endl;
 }

 void eat() override { // Overrides virtual function
 cout << "Dog eats bones" << endl;
 }
};

int main() {
 Animal* animal1 = new Animal();
 Animal* animal2 = new Dog();
 Dog* dog = new Dog();

 cout << "Early binding example:" << endl;
 animal1->speak(); // Early binding: Animal::speak()
 animal2->speak(); // Early binding: Animal::speak() - NOT Dog::speak()
 dog->speak(); // Early binding: Dog::speak()

 cout << "\nLate binding example:" << endl;
 animal1->eat(); // Late binding: Animal::eat()
 animal2->eat(); // Late binding: Dog::eat()
 dog->eat(); // Late binding: Dog::eat()

 return 0;
}
```

**Output:**

```
Early binding example:
Animal speaks
Animal speaks
Dog barks

Late binding example:
Animal eats
Dog eats bones
Dog eats bones
```

### Example 2: Abstract Class and Pure Virtual Function

```cpp
#include <iostream>
using namespace std;

class Shape {
protected:
 string color;
public:
 Shape(string c) : color(c) {}

 // Pure virtual function - makes Shape abstract
 virtual double area() = 0;

 void displayColor() {
 cout << "Color: " << color << endl;
 }
};

class Circle : public Shape {
 double radius;
public:
 Circle(string c, double r) : Shape(c), radius(r) {}

 double area() override {
 return 3.14159 * radius * radius;
 }
};

class Rectangle : public Shape {
 double length, breadth;
public:
 Rectangle(string c, double l, double b) : Shape(c), length(l), breadth(b) {}

 double area() override {
 return length * breadth;
 }
};

int main() {
 Circle c("Red", 5.0);
 Rectangle r("Blue", 4.0, 6.0);

 Shape* shapes[] = {&c, &r};

 for (int i = 0; i < 2; i++) {
 shapes[i]->displayColor();
 cout << "Area: " << shapes[i]->area() << endl << endl;
 }

 return 0;
}
```

### Example 3: Virtual Destructor for Proper Cleanup

```cpp
#include <iostream>
using namespace std;

class Base {
public:
 Base() {
 cout << "Base constructor" << endl;
 }

 virtual ~Base() { // Virtual destructor - ESSENTIAL for polymorphism
 cout << "Base destructor" << endl;
 }

 virtual void show() {
 cout << "Base show" << endl;
 }
};

class Derived : public Base {
private:
 int* data;
public:
 Derived() {
 data = new int[100]; // Dynamic memory allocation
 cout << "Derived constructor" << endl;
 }

 ~Derived() {
 delete[] data; // Cleanup dynamic memory
 cout << "Derived destructor" << endl;
 }

 void show() override {
 cout << "Derived show" << endl;
 }
};

int main() {
 Base* ptr = new Derived();
 ptr->show(); // Late binding: calls Derived::show()
 delete ptr; // Properly calls Derived then Base destructors
 return 0;
}
```

## Exam Tips

1. **Remember the Key Difference**: Early binding resolves function calls at compile-time, while late binding resolves them at runtime through virtual functions.

2. **Virtual Keyword is Essential**: Only member functions declared with `virtual` keyword use late binding. Without `virtual`, C++ uses early binding by default.

3. **Pointer/Reference Type Matters in Early Binding**: With early binding, the function called depends on the pointer or reference type, not the actual object type.

4. **Virtual Destructors**: Always make base class destructors virtual when using polymorphism to ensure proper cleanup of derived class objects.

5. **Pure Virtual Functions**: Functions declared as `virtual type function() = 0;` are pure virtual and make the class abstract (cannot be instantiated).

6. **Vtable Concept**: Understand that virtual functions use a vtable (virtual function table) at runtime for dynamic dispatch—each object with virtual functions has a hidden vptr.

7. **Performance Trade-off**: Early binding has no runtime overhead (faster), while late binding has small overhead due to vtable lookup (slightly slower but more flexible).

8. **RTTI Applications**: `dynamic_cast` and `typeid` work only with polymorphic types (classes having at least one virtual function).

9. **Slicing Problem**: When passing objects by value instead of pointers/references, the virtual mechanism is lost due to object slicing.

10. **Override Keyword**: Use C++11's `override` specifier to explicitly indicate that a derived class function is overriding a base class virtual function—helps catch errors at compile-time.
