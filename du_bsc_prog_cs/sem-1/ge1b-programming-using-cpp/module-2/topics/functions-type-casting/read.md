# Functions and Type Casting in C++

## Introduction

Functions and type casting constitute the fundamental building blocks of structured programming in C++. While functions enable code modularity, reusability, and organization by allowing programmers to decompose complex problems into smaller, manageable sub-problems, type casting provides mechanisms for converting data between different types. Together, these concepts form an essential part of the DU Computer Science curriculum under the NEP 2024 framework.

In real-world software development, functions are everywhere—from small utility programs to large-scale enterprise applications. Consider a banking application where functions handle transactions, calculate interest, validate user inputs, and generate reports. Type casting becomes critical when dealing with mixed-type arithmetic operations, file I/O operations, and when working with legacy codebases. For DU students preparing for semester examinations, a thorough understanding of these concepts is not merely academic—it forms the practical foundation for advanced topics like object-oriented programming, data structures, and algorithm design.

This module explores function fundamentals including declaration, definition, and invocation, along with parameter passing mechanisms such as pass-by-value, pass-by-reference, and pass-by-pointer. We also examine function overloading, default arguments, and recursion. The second half of this module covers type casting—both implicit conversions performed by the compiler and explicit conversions using C-style casts and modern C++ casting operators.

## Key Concepts

### Functions in C++

A function is a self-contained block of code that performs a specific task and can be called from other parts of a program. Functions promote code reusability, reduce code duplication, and improve program organization through modular design.

#### Function Declaration and Definition

A function declaration (prototype) tells the compiler about the function's name, return type, and parameters. A function definition contains the actual implementation.

```cpp
// Function Declaration
int add(int a, int b);

// Function Definition
int add(int a, int b) {
    return a + b;
}
```

The function signature consists of the function name and parameter types (not the return type). Two functions in the same scope cannot have identical signatures.

#### Parameter Passing Mechanisms

**Pass-by-Value:** The actual value is copied into the function. Changes to the parameter inside the function do not affect the original argument.

```cpp
void modify(int x) {
    x = x + 10;  // Only the local copy changes
}

int main() {
    int num = 5;
    modify(num);  // num remains 5
}
```

**Pass-by-Reference:** The function receives a reference (alias) to the original variable. Modifications affect the original data.

```cpp
void modify(int &x) {
    x = x + 10;  // Original variable changes
}

int main() {
    int num = 5;
    modify(num);  // num becomes 15
}
```

**Pass-by-Pointer:** The function receives the memory address of the variable. The function can modify the original value through dereferencing.

```cpp
void modify(int *x) {
    *x = *x + 10;  // Dereference to modify original
}

int main() {
    int num = 5;
    modify(&num);  // num becomes 15
}
```

#### Function Overloading

C++ supports function overloading—multiple functions can have the same name if their parameter lists differ (either in number or type of parameters).

```cpp
// Overloaded functions for different data types
int add(int a, int b) {
    return a + b;
}

double add(double a, double b) {
    return a + b;
}

int add(int a, int b, int c) {
    return a + b + c;
}
```

The compiler determines which function to call based on the argument types—a process called name mangling.

#### Default Arguments

Functions can have default parameter values that are used when arguments are omitted during the function call.

```cpp
void display(int count = 10, char ch = '*') {
    for(int i = 0; i < count; i++)
        cout << ch;
}

int main() {
    display();        // Prints 10 asterisks
    display(5);       // Prints 5 asterisks
    display(3, '#');  // Prints 3 hash symbols
}
```

Default arguments must be specified from right to left—once a default argument is used, all subsequent parameters must also have defaults.

#### Recursion

A function that calls itself is called a recursive function. Each recursive call creates a new stack frame until a base case terminates the recursion.

```cpp
// Factorial calculation using recursion
int factorial(int n) {
    if (n <= 1)  // Base case
        return 1;
    return n * factorial(n - 1);  // Recursive call
}
```

Understanding the call stack is crucial for recursive functions. DU students should remember that excessive recursion can lead to stack overflow.

### Type Casting in C++

Type casting converts a value from one data type to another. C++ supports both implicit (automatic) and explicit (manual) conversions.

#### Implicit Type Conversion (Coercion)

The C++ compiler automatically performs implicit conversions when:
- Arithmetic operations involve mixed types (e.g., int + float)
- Assignment operations have different types
- Function calls pass arguments that don't match parameter types

```cpp
int a = 10;
double b = 5.5;
double result = a + b;  // 'a' implicitly converted to 10.0
```

The conversion follows a hierarchy: `bool` → `char` → `short` → `int` → `long` → `float` → `double` (promotion/demotion). Demotions may cause data loss.

#### Explicit Type Conversion (C-Style)

C-style casts use the cast operator syntax: `(type)expression`

```cpp
double x = 9.8;
int y = (int)x;  // y = 9, decimal truncated

int a = 10, b = 3;
double c = (double)a / b;  // Forces floating-point division: 3.333...
```

While C-style casts are concise, they provide no type safety checking and can be dangerous.

#### C++ Casting Operators

C++ provides four type-safe casting operators:

**static_cast:** Used for well-defined conversions, including numeric conversions and pointer upcasts/downcasts within class hierarchies.

```cpp
double d = 3.14159;
int i = static_cast<int>(d);  // Truncates to 3

char c = 'A';
int ascii = static_cast<int>(c);  // 65
```

**const_cast:** Removes or adds const/volatile qualifiers. Used primarily to interface with legacy code.

```cpp
void print(char *str) {
    cout << str << endl;
}

int main() {
    const char *msg = "Hello";
    // print(msg);  // Error: const char* to char*
    print(const_cast<char*>(msg));  // Works but risky
}
```

**reinterpret_cast:** Converts between unrelated types by reinterpreting the bit pattern. Highly unsafe and implementation-dependent.

```cpp
int *ptr = new int(65);
char *cptr = reinterpret_cast<char*>(ptr);
cout << *cptr;  // Prints 'A' (ASCII 65)
```

**dynamic_cast:** Used for safe downcasting in polymorphic class hierarchies. Returns nullptr (for pointers) or throws bad_cast (for references) on failure.

```cpp
class Base { virtual void dummy() {} };
class Derived : public Base { int d; };

Base *basePtr = new Derived;
Derived *derivedPtr = dynamic_cast<Derived*>(basePtr);  // Succeeds
```

## Examples

### Example 1: Pass-by-Value vs Pass-by-Reference

**Problem:** Write a function to swap two numbers. Demonstrate both pass-by-value (using pointers) and pass-by-reference approaches.

**Solution:**

```cpp
#include <iostream>
using namespace std;

// Pass-by-pointer (C-style approach)
void swapPointer(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Pass-by-reference (C++ approach)
void swapReference(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    int x = 10, y = 20;
    
    cout << "Before swap: x = " << x << ", y = " << y << endl;
    
    swapPointer(&x, &y);  // Passing addresses
    cout << "After swapPointer: x = " << x << ", y = " << y << endl;
    
    swapReference(x, y);  // Passing references
    cout << "After swapReference: x = " << x << ", y = " << y << endl;
    
    return 0;
}
```

**Output:**
```
Before swap: x = 10, y = 20
After swapPointer: x = 20, y = 10
After swapReference: x = 10, y = 20
```

### Example 2: Function Overloading with Type Conversion

**Problem:** Create overloaded functions to calculate the area of different shapes: circle (radius), rectangle (length, breadth), and square (side).

**Solution:**

```cpp
#include <iostream>
#include <cmath>
using namespace std;

const double PI = 3.14159;

// Area of circle
double area(double radius) {
    return PI * radius * radius;
}

// Area of rectangle
double area(double length, double breadth) {
    return length * breadth;
}

// Area of square (uses rectangle function)
double area(double side) {
    return area(side, side);  // Calls rectangle function
}

int main() {
    cout << "Circle (r=5): " << area(5.0) << endl;
    cout << "Rectangle (l=4, b=6): " << area(4.0, 6.0) << endl;
    cout << "Square (s=3): " << area(3.0) << endl;
    
    // Demonstration of implicit conversion
    cout << "Circle (r=5): " << area(5) << endl;  // int to double
    
    return 0;
}
```

### Example 3: Type Casting in Mixed Expressions

**Problem:** Demonstrate the difference between integer division and floating-point division, and show proper type casting.

**Solution:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 7, b = 2;
    
    // Integer division (truncates decimal)
    int result1 = a / b;
    cout << "Integer division: " << a << "/" << b << " = " << result1 << endl;
    
    // Cast numerator to double
    double result2 = (double)a / b;
    cout << "Cast numerator: (double)" << a << "/" << b << " = " << result2 << endl;
    
    // Cast using static_cast
    double result3 = static_cast<double>(a) / b;
    cout << "static_cast: " << result3 << endl;
    
    // Cast entire expression
    double result4 = static_cast<double>(a / b);
    cout << "Cast result: " << result4 << " (incorrect!)" << endl;
    
    return 0;
}
```

**Output:**
```
Integer division: 7/2 = 3
Cast numerator: (double)7/2 = 3.5
static_cast: 3.5
Cast result: 3 (incorrect!)
```

**Key Insight:** Notice that `static_cast<double>(a / b)` performs integer division first (getting 3), then converts 3 to 3.0—this is a common mistake to avoid.

## Exam Tips

1. **Understand Function Signature:** Remember that function signature includes only the function name and parameter types, not the return type. Function overloading is based on signatures, not return types.

2. **Pass-by-Reference vs Pass-by-Pointer:** For DU exams, be clear when to use each. Pass-by-reference is more idiomatic in C++, while pass-by-pointer is useful when you need to pass optional parameters or when NULL is a valid argument.

3. **Default Arguments Placement:** Default arguments must appear in the function declaration (prototype) and should be at the end of the parameter list. In the definition, do not repeat default values.

4. **Avoid Data Loss in Type Casting:** When casting from higher to lower precision types (double to int), be aware of potential data loss. The `static_cast` operator makes intentions explicit and is preferred over C-style casts.

5. **Recursion Base Case:** Always identify the base case in recursive functions. Without a base case, the function will cause infinite recursion and stack overflow.

6. **sizeof and Type Casting:** Remember that `sizeof(char)` is always 1 byte, but `sizeof(int)` varies by system. When calculating memory offsets or buffer sizes, consider type casting carefully.

7. **const Correctness:** Use `const` with reference parameters when the function should not modify the argument. This prevents accidental modifications and enables passing of temporary objects.

8. **dynamic_cast Safety:** Remember that `dynamic_cast` only works with polymorphic classes (having at least one virtual function). For failed pointer casts, it returns nullptr rather than causing undefined behavior.