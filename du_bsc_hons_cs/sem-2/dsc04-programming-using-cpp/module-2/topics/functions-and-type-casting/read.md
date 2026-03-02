# Functions and Type Casting in C++

## Comprehensive Study Material for BSc (Hons) Computer Science - Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

Functions and type casting constitute fundamental pillars of C++ programming that every computer science student must master. Functions enable modular, reusable, and organized code structure, while type casting ensures proper data type handling during operations and conversions. These concepts are essential for developing efficient software solutions and form a critical part of the Delhi University BSc (Hons) Computer Science curriculum under the NEP 2024 UGCF framework.

In real-world software development, functions are ubiquitous—they implement algorithms, handle user interactions, perform calculations, and manage system resources. Type casting becomes necessary when working with different data types, inheritance hierarchies, and generic programming. This study material provides exhaustive coverage of these topics, addressing all concepts required for university examinations and practical programming competence.

---

## 2. Functions in C++: Foundation and Fundamentals

### 2.1 What is a Function?

A function is a self-contained block of code that performs a specific task and can be called from other parts of a program. Functions promote code reusability, modularity, and easier maintenance. Each function has a unique name, and when invoked, the program execution transfers to the function body.

### 2.2 Function Declaration (Prototype)

A function declaration informs the compiler about the function's name, return type, and parameters before its actual definition. This is also known as the function prototype.

```cpp
// Function prototypes
int add(int a, int b);           // Returns integer, takes two integers
double calculateArea(double radius);  // Returns double, takes double
void displayMessage();           // Returns nothing
```

### 2.3 Function Definition

The function definition contains the actual implementation—the code that executes when the function is called.

```cpp
// Function definition
int add(int a, int b) {
    return a + b;
}

// Main function - program entry point
int main() {
    int result = add(10, 20);
    std::cout << "Sum: " << result << std::endl;
    return 0;
}
```

### 2.4 Function Call and Return Values

Functions can return values using the `return` statement. The return type must match the declared return type.

```cpp
#include <iostream>
using namespace std;

// Function with return value
int multiply(int x, int y) {
    return x * y;
}

int main() {
    int product = multiply(6, 7);
    cout << "Product: " << product << endl;  // Output: Product: 42
    return 0;
}
```

---

## 3. Parameter Passing Mechanisms

Understanding how parameters are passed to functions is crucial for writing efficient C++ code. C++ supports three primary parameter passing mechanisms.

### 3.1 Pass-by-Value

In pass-by-value, a copy of the argument is made and passed to the function. Changes to the parameter inside the function do not affect the original argument.

```cpp
#include <iostream>
using namespace std;

void modifyValue(int num) {
    num = 100;  // Only modifies the local copy
    cout << "Inside function: " << num << endl;
}

int main() {
    int x = 50;
    modifyValue(x);
    cout << "After function call: " << x << endl;
    // Output:
    // Inside function: 100
    // After function call: 50
    return 0;
}
```

### 3.2 Pass-by-Reference

Pass-by-reference allows functions to modify the original arguments directly. This is achieved by passing references (&) or pointers to the variables.

```cpp
#include <iostream>
using namespace std;

void modifyReference(int &num) {
    num = 100;  // Modifies the original variable
    cout << "Inside function: " << num << endl;
}

int main() {
    int x = 50;
    modifyReference(x);
    cout << "After function call: " << x << endl;
    // Output:
    // Inside function: 100
    // After function call: 100
    return 0;
}
```

**Key Advantage**: Pass-by-reference is efficient for large data structures (like arrays, vectors, or objects) because it avoids copying.

### 3.3 Pass-by-Pointer

Pass-by-pointer involves passing the memory address of a variable. The function receives a pointer and can modify the original value through dereferencing.

```cpp
#include <iostream>
using namespace std;

void modifyPointer(int *ptr) {
    if (ptr != nullptr) {
        *ptr = 100;  // Dereference to modify original value
        cout << "Inside function: " << *ptr << endl;
    }
}

int main() {
    int x = 50;
    modifyPointer(&x);  // Pass address of x
    cout << "After function call: " << x << endl;
    // Output:
    // Inside function: 100
    // After function call: 100
    return 0;
}
```

### 3.4 Return by Reference

Functions can also return by reference, which is useful for returning large objects or when you need to modify the returned value in the calling scope.

```cpp
#include <iostream>
using namespace std;

int& findLarger(int &a, int &b) {
    return (a > b) ? a : b;
}

int main() {
    int x = 10, y = 20;
    int &ref = findLarger(x, y);
    ref = 100;  // Modifies y because y is larger
    cout << "x = " << x << ", y = " << y << endl;  // y is now 100
    return 0;
}
```

---

## 4. Default Arguments

C++ allows functions to have default argument values. If arguments are not provided during function call, default values are used.

```cpp
#include <iostream>
using namespace std;

int power(int base, int exponent = 2) {
    int result = 1;
    for (int i = 0; i < exponent; i++) {
        result *= base;
    }
    return result;
}

int main() {
    cout << power(3) << endl;      // Uses default exponent: 9
    cout << power(3, 3) << endl;   // Uses provided exponent: 27
    return 0;
}
```

**Important Rules**:
- Default arguments must be at the rightmost positions
- Default arguments should be defined in the prototype, not in the definition (for header files)

---

## 5. Function Overloading

Function overloading allows multiple functions with the same name but different parameter lists. The compiler determines which function to call based on the arguments provided.

```cpp
#include <iostream>
using namespace std;

// Overloaded functions - same name, different parameters
int add(int a, int b) {
    cout << "Integer addition" << endl;
    return a + b;
}

double add(double a, double b) {
    cout << "Double addition" << endl;
    return a + b;
}

int add(int a, int b, int c) {
    cout << "Three integer addition" << endl;
    return a + b + c;
}

int main() {
    cout << add(5, 3) << endl;          // Calls int version
    cout << add(5.5, 3.3) << endl;      // Calls double version
    cout << add(1, 2, 3) << endl;       // Calls three-parameter version
    return 0;
}
```

**Use Cases**:
- Performing similar operations on different data types
- Providing convenient interfaces with varying numbers of parameters
- Creating intuitive APIs for library users

---

## 6. Recursion

A recursive function is one that calls itself either directly or indirectly. Recursion is powerful for solving problems that can be broken down into smaller, similar subproblems.

### 6.1 Structure of Recursive Functions

```cpp
return_type function(parameters) {
    if (base_condition) {
        return base_value;  // Terminating condition
    }
    return function(smaller_problem);  // Recursive call
}
```

### 6.2 Example: Factorial Calculation

```cpp
#include <iostream>
using namespace std;

// Recursive function to calculate factorial
int factorial(int n) {
    if (n <= 1) {
        return 1;  // Base case
    }
    return n * factorial(n - 1);  // Recursive call
}

int main() {
    int num = 5;
    cout << "Factorial of " << num << " = " << factorial(num) << endl;
    // Output: Factorial of 5 = 120
    return 0;
}
```

### 6.3 Example: Fibonacci Sequence

```cpp
#include <iostream>
using namespace std;

// Recursive Fibonacci function
int fibonacci(int n) {
    if (n <= 1) {
        return n;  // Base cases: fib(0) = 0, fib(1) = 1
    }
    return fibonacci(n - 1) + fibonacci(n - 2);  // Two recursive calls
}

int main() {
    int n = 10;
    cout << "Fibonacci sequence up to " << n << ":" << endl;
    for (int i = 0; i < n; i++) {
        cout << fibonacci(i) << " ";
    }
    cout << endl;
    // Output: 0 1 1 2 3 5 8 13 21 34
    return 0;
}
```

### 6.4 Important Considerations

- **Base Case**: Always have a terminating condition to prevent infinite recursion
- **Stack Overflow**: Deep recursion can exhaust stack memory
- **Efficiency**: Consider using dynamic programming (memoization) for overlapping subproblems

---

## 7. Inline Functions

Inline functions are functions where the compiler attempts to insert the function's body at the point of call instead of performing a regular function call. This eliminates function call overhead.

```cpp
#include <iostream>
using namespace std;

inline int square(int x) {
    return x * x;
}

int main() {
    cout << "Square of 5: " << square(5) << endl;
    return 0;
}
```

**When to Use**:
- Small, simple functions (typically 1-3 lines)
- Frequently called functions
- Functions where call overhead exceeds execution time

**When Not to Use**:
- Large, complex functions
- Functions with loops, switches, or goto statements
- Recursive functions

---

## 8. Static and Const Parameters

### 8.1 Const Parameters

The `const` qualifier in function parameters ensures that the parameter cannot be modified inside the function. This is both a documentation tool and a safety mechanism.

```cpp
#include <iostream>
using namespace std;

void printArray(const int arr[], int size) {
    // arr[0] = 100;  // Error: cannot modify const parameter
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int numbers[] = {1, 2, 3, 4, 5};
    printArray(numbers, 5);
    return 0;
}
```

### 8.2 Const Reference Parameters

Combining `const` with references is a common and efficient practice, especially for passing large objects.

```cpp
#include <iostream>
#include <string>
using namespace std;

void displayInfo(const string &name, const int &age) {
    // name = "New Name";  // Error: cannot modify
    cout << "Name: " << name << ", Age: " << age << endl;
}
```

### 8.3 Static Variables in Functions

A static variable inside a function retains its value between function calls.

```cpp
#include <iostream>
using namespace std;

void counter() {
    static int count = 0;  // Initialized only once
    count++;
    cout << "Call count: " << count << endl;
}

int main() {
    counter();  // Call count: 1
    counter();  // Call count: 2
    counter();  // Call count: 3
    return 0;
}
```

---

## 9. Lambda Functions (Anonymous Functions)

Lambda functions (introduced in C++11) are inline, anonymous functions that can be defined at the point of use. They are particularly useful for STL algorithms and callbacks.

### 9.1 Lambda Syntax

```cpp
[capture_list](parameters) -> return_type {
    // function body
}
```

### 9.2 Examples

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    // Basic lambda
    auto greet = []() {
        cout << "Hello from lambda!" << endl;
    };
    greet();

    // Lambda with parameters
    auto add = [](int a, int b) {
        return a + b;
    };
    cout << "Sum: " << add(5, 3) << endl;

    // Lambda with capture
    int multiplier = 10;
    auto multiply = [multiplier](int x) {
        return x * multiplier;
    };
    cout << "Result: " << multiply(5) << endl;

    // Lambda with STL algorithm
    vector<int> numbers = {5, 2, 8, 1, 9};
    cout << "Original: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;

    sort(numbers.begin(), numbers.end(), [](int a, int b) {
        return a > b;  // Descending order
    });

    cout << "Sorted (desc): ";
    for (int n : numbers) cout << n << " ";
    cout << endl;

    return 0;
}
```

### 9.3 Capture Modes

| Capture Mode | Description |
|--------------|-------------|
| `[ ]` | No capture |
| `[=]` | Capture by value (copy) |
| `[&]` | Capture by reference |
| `[x]` | Capture specific variable by value |
| `[&x]` | Capture specific variable by reference |
| `[=, &x]` | Capture all by value, except x by reference |

---

## 10. Function Pointers

A function pointer stores the address of a function and allows functions to be passed as arguments and called dynamically.

### 10.1 Declaration and Usage

```cpp
#include <iostream>
using namespace std;

// Function to be pointed to
int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int main() {
    // Function pointer declaration
    int (*operation)(int, int);

    // Point to add function
    operation = add;
    cout << "Add: " << operation(10, 5) << endl;  // 15

    // Point to subtract function
    operation = subtract;
    cout << "Subtract: " << operation(10, 5) << endl;  // 5

    return 0;
}
```

### 10.2 Function Pointers as Parameters

```cpp
#include <iostream>
using namespace std;

int add(int a, int b) { return a + b; }
int multiply(int a, int b) { return a * b; }

// Function that takes a function pointer as parameter
int calculate(int x, int y, int (*func)(int, int)) {
    return func(x, y);
}

int main() {
    cout << "Using add: " << calculate(10, 5, add) << endl;
    cout << "Using multiply: " << calculate(10, 5, multiply) << endl;
    return 0;
}
```

---

## 11. Type Casting in C++

Type casting converts one data type to another. This is essential for arithmetic operations, object-oriented programming, and memory manipulation.

### 11.1 Implicit Type Casting (Automatic)

The compiler automatically performs implicit casting when there's no data loss.

```cpp
#include <iostream>
using namespace std;

int main() {
    int numInt = 100;
    double numDouble = numInt;  // Implicit: int to double
    cout << "Double value: " << numDouble << endl;  // 100

    char ch = 'A';
    int chInt = ch;  // Implicit: char to int (ASCII value)
    cout << "Integer value of 'A': " << chInt << endl;  // 65

    return 0;
}
```

### 11.2 Explicit Type Casting (C-Style)

C-style casting uses the `(type)value` syntax.

```cpp
#include <iostream>
using namespace std;

int main() {
    double numDouble = 9.8;
    int numInt = (int)numDouble;  // C-style cast
    cout << "Integer value: " << numInt << endl;  // 9 (truncation)

    int a = 10, b = 3;
    double result = (double)a / b;  // Cast to double for accurate division
    cout << "Result: " << result << endl;  // 3.333...

    return 0;
}
```

### 11.3 C++ Casting Operators

C++ provides four type-safe casting operators that offer better control and error detection than C-style casts.

#### 11.3.1 static_cast

Used for well-defined conversions, including numeric conversions, void*/any pointer conversions, and base-class to derived-class conversions.

```cpp
#include <iostream>
using namespace std;

int main() {
    // Numeric conversions
    double d = 9.8;
    int i = static_cast<int>(d);  // 9
    cout << "static_cast int: " << i << endl;

    // Enum to int
    enum Color { RED = 0, GREEN, BLUE };
    Color c = GREEN;
    int colorValue = static_cast<int>(c);  // 1
    cout << "Color value: " << colorValue << endl;

    // void* to typed pointer
    int num = 42;
    void* voidPtr = &num;
    int* intPtr = static_cast<int*>(voidPtr);
    cout << "Value through void*: " << *intPtr << endl;

    return 0;
}
```

#### 11.3.2 dynamic_cast

Used for safe downcasting in inheritance hierarchies. It performs runtime type checking and returns nullptr (for pointers) or throws an exception (for references) if the cast is invalid.

```cpp
#include <iostream>
using namespace std;

class Base {
public:
    virtual void display() {  // Virtual function for polymorphism
        cout << "Base class" << endl;
    }
    virtual ~Base() {}  // Virtual destructor
};

class Derived : public Base {
public:
    void display() override {
        cout << "Derived class" << endl;
    }
    void derivedMethod() {
        cout << "Derived specific method" << endl;
    }
};

int main() {
    Base* basePtr = new Derived();

    // Safe downcasting using dynamic_cast
    Derived* derivedPtr = dynamic_cast<Derived*>(basePtr);
    if (derivedPtr) {
        derivedPtr->display();  // Derived class
        derivedPtr->derivedMethod();
    } else {
        cout << "Cast failed" << endl;
    }

    // Failed cast example
    Base* basePtr2 = new Base();
    Derived* failedPtr = dynamic_cast<Derived*>(basePtr2);
    if (failedPtr == nullptr) {
        cout << "Cast failed: Not a Derived object" << endl;
    }

    delete basePtr;
    delete basePtr2;

    return 0;
}
```

#### 11.3.3 const_cast

Used to add or remove the const or volatile qualifiers from a variable.

```cpp
#include <iostream>
using namespace std;

void modifyValue(int* ptr) {
    *ptr = 100;
}

int main() {
    const int num = 50;
    // modifyValue(&num);  // Error: cannot convert const int* to int*

    // Use const_cast to remove const
    const_cast<int*>(&num);
    modifyValue(const_cast<int*>(&num));  // Undefined behavior!

    // Proper use: Adding const
    int value = 75;
    const int* ptr = &value;
    int* nonConstPtr = const_cast<int*>(ptr);
    *nonConstPtr = 100;
    cout << "Modified value: " << value << endl;

    return 0;
}
```

**Warning**: Using const_cast to modify originally const objects leads to undefined behavior.

#### 11.3.4 reinterpret_cast

The most dangerous cast, used for low-level, implementation-specific reinterpreting of bit patterns. It converts one pointer type to another unrelated pointer type or integer to pointer.

```cpp
#include <iostream>
using namespace std;

int main() {
    int num = 65;

    // Reinterpret integer as pointer
    int* intPtr = &num;
    char* charPtr = reinterpret_cast<char*>(intPtr);
    cout << "Reinterpreted as char: " << *charPtr << endl;  // 'A' (ASCII 65)

    // Pointer to function
    int (*funcPtr)() = nullptr;
    long addr = reinterpret_cast<long>(funcPtr);
    cout << "Function address: " << addr << endl;

    // Converting between unrelated pointer types
    struct A { int x; };
    struct B { int y; };
    A a = {10};
    B* bPtr = reinterpret_cast<B*>(&a);
    cout << "B's y (interpreted from A's x): " << bPtr->y << endl;

    return 0;
}
```

---

## 12. Key Takeaways

### Functions:
- **Modular Design**: Functions break code into manageable, reusable units
- **Pass-by-Reference**: Use `&` for efficient parameter passing without copying
- **Function Overloading**: Multiple functions with the same name but different parameters enable polymorphic behavior
- **Recursion**: Powerful technique for problems with self-similar subproblems; always define a base case
- **Lambda Functions**: Anonymous inline functions useful for callbacks and STL algorithms; master capture lists
- **Function Pointers**: Enable runtime function selection and callback mechanisms

### Type Casting:
- **Implicit Casting**: Automatic by compiler when no data loss occurs
- **static_cast**: Compile-time checked conversions for well-defined type changes
- **dynamic_cast**: Runtime-safe downcasting in inheritance with type checking
- **const_cast**: Add/remove const qualifier; avoid undefined behavior
- **reinterpret_cast**: Low-level bit reinterpretation; use sparingly and carefully

### Best Practices:
- Prefer pass-by-const-reference for large objects
- Use inline functions for small, frequently called functions
- Prefer C++ casts over C-style casts for type safety
- Use dynamic_cast with virtual functions for proper RTTI (Run-Time Type Information)

---

## 13. Assessment Questions

### Very Short Answer Questions (1 Mark)
1. What is the difference between pass-by-value and pass-by-reference?
2. Define a recursive function.
3. What is the purpose of the `inline` keyword?
4. Write the syntax of a lambda function.
5. What does `static_cast` do?

### Short Answer Questions (2-3 Marks)
6. Explain function overloading with an example.
7. What are default arguments in functions? State one restriction.
8. Differentiate between `static_cast` and `dynamic_cast`.
9. Explain the capture modes in lambda functions.
10. What is a function pointer? Give one use case.

### Long Answer Questions (5 Marks)
11. Write a C++ program to demonstrate recursion by calculating the factorial of a number.
12. Explain all four C++ casting operators with appropriate examples.
13. Discuss pass-by-value, pass-by-reference, and pass-by-pointer with suitable code examples.
14. What are lambda functions? Explain different capture modes with examples.
15. Explain function overloading and inline functions with suitable examples.

### Programming Problems
16. Write a function that swaps two integers using pass-by-reference.
17. Create an overloaded function to find the maximum of two integers, two floats, and three integers.
18. Write a C++ program using lambda functions to filter even numbers from a vector.
19. Implement a function template to find the maximum of two values.
20. Write a program demonstrating the use of function pointers to perform arithmetic operations.

---

*This study material is designed in accordance with the Delhi University BSc (Hons) Computer Science NEP 2024 UGCF syllabus, covering all essential concepts of Functions and Type Casting for comprehensive examination preparation.*