# When Constructors and Destructors Are Executed

## Introduction

In Object-Oriented Programming with C++, constructors and destructors play a fundamental role in object lifecycle management. Constructors are special member functions that are automatically called when an object is created, initializing the object's data members. Destructors, conversely, are called when an object goes out of scope or is explicitly deleted, performing cleanup operations such as releasing memory, closing files, or releasing resources. Understanding when exactly these functions are executed is crucial for writing robust C++ programs and is a frequently tested topic in university examinations.

The execution order of constructors and destructors follows well-defined rules in C++. These rules ensure proper initialization and cleanup of objects, preventing resource leaks and undefined behavior. Whether dealing with local objects, global objects, static objects, or dynamically allocated objects, the compiler follows specific sequences that every C++ programmer must master. This knowledge becomes particularly important when dealing with complex class hierarchies, resource management, and memory allocation patterns.

## Key Concepts

### Constructor Execution Order

**1. Global Objects**
Global objects are declared outside any function and are constructed before the `main()` function begins execution. Their destructors are called after `main()` completes. Global objects are constructed in the order of their declaration within a single translation unit, and destructors are called in reverse order of construction.

```cpp
#include <iostream>
using namespace std;

class MyClass {
public:
 MyClass() { cout << "Constructor: MyClass\n"; }
 ~MyClass() { cout << "Destructor: MyClass\n"; }
};

MyClass globalObj; // Constructor called before main()

int main() {
 cout << "Inside main()\n";
 return 0;
}
// Destructor called after main() ends
```

**2. Local (Automatic) Objects**
Local objects are created within a function and are constructed when program execution reaches their declaration. They are destroyed when the function returns or when the block in which they are defined exits. Local objects are constructed in the order of their declaration and destroyed in reverse order.

```cpp
void function() {
 cout << "Function starts\n";
 MyClass obj1; // Constructor called here
 MyClass obj2; // Constructor called here
 cout << "Function ends\n";
} // obj2 destructor, then obj1 destructor (reverse order)
```

**3. Static Objects**
Static local objects (inside functions) are constructed only once, the first time the function is called. Their destructors are called when `main()` terminates or when `exit()` is called. Static objects at file scope (global static) follow the same rules as global objects.

```cpp
void demo() {
 static MyClass staticObj; // Constructed only once on first call
 cout << "Function called\n";
}

int main() {
 demo();
 demo();
 return 0;
} // staticObj destructor called here at program end
```

**4. Dynamic Objects**
Dynamically allocated objects using `new` are constructed when `new` expression is executed. They persist until explicitly destroyed with `delete`, which calls the destructor. If `delete` is not called, destructors are not executed (memory leak).

```cpp
int main() {
 MyClass* ptr = new MyClass(); // Constructor called
 delete ptr; // Destructor called
 return 0;
}
```

### Constructor Execution in Inheritance

When dealing with inheritance, base class constructors are executed before derived class constructors. The execution follows a specific hierarchy: virtual base classes first (in depth-first left-to-right order), then direct base classes, and finally the most derived class.

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

Note that destructors are called in the exact reverse order of constructors - derived class destructor first, then base class destructor. This ensures proper cleanup of the derived portion before the base portion.

### Virtual Base Classes

In multiple inheritance with virtual base classes, the virtual base class constructor is called before the non-virtual base class constructors, and only once regardless of how many paths exist in the inheritance hierarchy.

```cpp
class A { public: A() { cout << "A "; } };
class B : virtual public A { public: B() { cout << "B "; } };
class C : virtual public A { public: C() { cout << "C "; } };
class D : public B, public C { public: D() { cout << "D "; } };

int main() {
 D obj;
 return 0;
}
```

**Output:** `A B C D` (constructor), `D C B A` (destructor)

### Member Object Construction

Member objects (composition) are constructed before the enclosing class's constructor, in the order of their declaration in the class. They are destructed in reverse order after the class's destructor completes.

```cpp
class Member {
public:
 Member() { cout << "Member "; }
 ~Member() { cout << "~Member "; }
};

class Container {
 Member m1;
 Member m2;
public:
 Container() { cout << "Container "; }
 ~Container() { cout << "~Container "; }
};

int main() {
 Container obj;
 return 0;
}
```

**Output:** `Member Member Container ~Container ~Member ~Member`

## Examples

### Example 1: Nested Local Objects

```cpp
#include <iostream>
using namespace std;

class Alpha {
 char id;
public:
 Alpha(char c) : id(c) {
 cout << "Constructor Alpha(" << id << ")\n";
 }
 ~Alpha() {
 cout << "Destructor Alpha(" << id << ")\n";
 }
};

void test() {
 cout << "Entering test()\n";
 Alpha a('X'); // First object
 {
 Alpha b('Y'); // Second object in inner block
 cout << "Inside inner block\n";
 } // b destroyed here
 cout << "Leaving test()\n";
} // a destroyed here

int main() {
 test();
 return 0;
}
```

**Output:**

```
Entering test()
Constructor Alpha(X)
Constructor Alpha(Y)
Inside inner block
Destructor Alpha(Y)
Leaving test()
Destructor Alpha(X)
```

**Explanation:** Objects are constructed in order of declaration and destroyed in reverse order. The inner block's object `b` is destroyed when exiting the block, while `a` is destroyed when `test()` returns.

### Example 2: Constructor Chaining in Inheritance

```cpp
#include <iostream>
using namespace std;

class Parent {
public:
 Parent() { cout << "Parent Constructor\n"; }
 Parent(int x) { cout << "Parent Parameterized Constructor: " << x << "\n"; }
 ~Parent() { cout << "Parent Destructor\n"; }
};

class Child : public Parent {
public:
 Child() { cout << "Child Constructor\n"; }
 Child(int x) : Parent(x * 2) {
 cout << "Child Parameterized Constructor: " << x << "\n";
 }
 ~Child() { cout << "Child Destructor\n"; }
};

int main() {
 cout << "--- Creating obj1 ---\n";
 Child obj1;

 cout << "\n--- Creating obj2 ---\n";
 Child obj2(10);

 cout << "\n--- Exiting main ---\n";
 return 0;
}
```

**Output:**

```
--- Creating obj1 ---
Parent Constructor
Child Constructor
Child Destructor
Parent Destructor

--- Creating obj2 ---
Parent Parameterized Constructor: 20
Child Parameterized Constructor: 10
Child Destructor
Parent Destructor
```

**Explanation:** Base class constructor is always called before derived class constructor. If a parameterized constructor is called, we can explicitly invoke a specific base constructor using the initializer list.

### Example 3: Dynamic Memory and Array of Objects

```cpp
#include <iostream>
using namespace std;

class Widget {
 int id;
public:
 Widget(int i) : id(i) {
 cout << "Constructing Widget " << id << "\n";
 }
 ~Widget() {
 cout << "Destructing Widget " << id << "\n";
 }
};

int main() {
 cout << "=== Single object ===\n";
 Widget* w1 = new Widget(1);
 delete w1;

 cout << "\n=== Array of objects ===\n";
 Widget* w2 = new Widget[3]; // Calls default constructor for each

 cout << "\n=== Deleting array ===\n";
 delete[] w2;

 return 0;
}
```

**Output:**

```
=== Single object ===
Constructing Widget 1
Destructing Widget 1

=== Array of objects ===
Constructing Widget 0
Constructing Widget 1
Constructing Widget 2

=== Deleting array ===
Destructing Widget 2
Destructing Widget 1
Destructing Widget 0
```

**Important Note:** When deleting arrays of objects, always use `delete[]` to ensure each object's destructor is called. Using `delete` instead of `delete[]` leads to undefined behavior.

## Exam Tips

1. **Order Reversal Rule:** Remember that destructors are always called in the exact reverse order of constructors - LIFO (Last In First Out) principle.

2. **Base Before Derived:** In inheritance, base class constructor executes before derived class constructor; destructor executes in reverse order.

3. **Global vs Local:** Global objects are constructed before `main()` and destroyed after `main()` ends. Local objects are destroyed when they go out of scope.

4. **Virtual Destructors:** Always use virtual destructors when dealing with polymorphism to ensure proper cleanup of derived class objects through base class pointers.

5. **Member Objects Order:** Member objects are constructed in the order of their declaration in the class, not in the order of the initializer list.

6. **Virtual Base Classes:** Virtual base class constructors are called before non-virtual base class constructors and only once regardless of inheritance paths.

7. **Dynamic Memory:** Always pair `new` with `delete` and `new[]` with `delete[]` to ensure destructors are called properly.

8. **Static Local Objects:** These are constructed only once and destroyed when `main()` terminates.
