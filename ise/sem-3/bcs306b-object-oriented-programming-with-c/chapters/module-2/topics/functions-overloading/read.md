# Functions and Overloading in C++

## Introduction to Functions

Functions are fundamental building blocks in C++ programming that allow you to organize code into reusable, logical units. A function is a self-contained block of code that performs a specific task when called.

### Function Components

A typical function consists of:

- **Function declaration/prototype**: Specifies the function's interface
- **Function definition**: Contains the actual implementation
- **Function call**: Invokes the function to execute its code

```cpp
// Function declaration
int add(int a, int b);

// Function definition
int add(int a, int b) {
    return a + b;
}

// Function call
int result = add(5, 3);
```

### Function Syntax

```
return_type function_name(parameter_list) {
    // function body
    return value; // if return_type is not void
}
```

### Types of Functions

1. **Standard functions**: Regular functions with parameters and return values
2. **Void functions**: Functions that don't return any value
3. **Inline functions**: Functions expanded at compile time for performance
4. **Recursive functions**: Functions that call themselves

## Function Parameters and Arguments

### Parameter Passing Mechanisms

| Mechanism         | Description                                  | Effect on Original Variable |
| ----------------- | -------------------------------------------- | --------------------------- |
| Pass by Value     | Creates a copy of the argument               | No effect on original       |
| Pass by Reference | Uses the original variable's memory location | Changes affect original     |
| Pass by Pointer   | Uses memory address of the variable          | Changes affect original     |

```cpp
// Pass by value
void modifyValue(int x) {
    x = x * 2; // Changes local copy only
}

// Pass by reference
void modifyReference(int &x) {
    x = x * 2; // Changes original variable
}

// Pass by pointer
void modifyPointer(int *x) {
    *x = *x * 2; // Changes original variable
}
```

### Default Parameters

C++ allows functions to have default parameter values:

```cpp
void displayMessage(string message = "Hello World") {
    cout << message << endl;
}

// Can be called as:
displayMessage(); // Uses default: "Hello World"
displayMessage("Custom message"); // Uses provided value
```

## Function Overloading

Function overloading allows multiple functions to have the same name but different parameters. This enables you to create functions that perform similar operations but on different data types or with different parameter combinations.

### Rules for Function Overloading

1. Functions must have the same name
2. Functions must differ in:
   - Number of parameters
   - Type of parameters
   - Order of parameters
3. Return type alone cannot differentiate overloaded functions

### Overloading Examples

```cpp
// Overloaded add functions
int add(int a, int b) {
    return a + b;
}

double add(double a, double b) {
    return a + b;
}

string add(string a, string b) {
    return a + b;
}

int add(int a, int b, int c) {
    return a + b + c;
}
```

### How Overloading Works

```
Function Call → Compiler → Function Selection → Execution
    │              │            │
    │              │            └─ Based on parameter match
    │              └─ Creates function signature table
    └─ With specific arguments
```

The compiler uses a process called **name mangling** to create unique internal names for overloaded functions based on their parameter types.

## Inline Functions

Inline functions are expanded at the point of call rather than being invoked through the normal function call mechanism. This can improve performance by eliminating function call overhead.

```cpp
inline int square(int x) {
    return x * x;
}

// The call:
int result = square(5);
// Gets expanded to:
int result = 5 * 5;
```

### When to Use Inline Functions

- Small, frequently called functions
- Functions with simple operations
- Performance-critical code sections

### When to Avoid Inline Functions

- Large functions (increases code size)
- Recursive functions
- Functions with complex logic

## Function Templates

Function templates allow you to create generic functions that work with multiple data types without rewriting the same code.

```cpp
template <typename T>
T maximum(T a, T b) {
    return (a > b) ? a : b;
}

// Can be used with:
int maxInt = maximum(5, 10);
double maxDouble = maximum(3.14, 2.71);
char maxChar = maximum('a', 'z');
```

## Recursive Functions

Recursive functions call themselves to solve problems that can be broken down into smaller, similar subproblems.

```cpp
int factorial(int n) {
    if (n <= 1) return 1; // Base case
    return n * factorial(n - 1); // Recursive case
}
```

```
Factorial Calculation Process:
factorial(4)
→ 4 * factorial(3)
→ 4 * 3 * factorial(2)
→ 4 * 3 * 2 * factorial(1)
→ 4 * 3 * 2 * 1
→ 24
```

## Best Practices for Functions

1. **Single Responsibility**: Each function should do one thing well
2. **Meaningful Names**: Use descriptive function names
3. **Parameter Validation**: Validate input parameters when necessary
4. **Documentation**: Comment your functions clearly
5. **Consistent Return Types**: Be consistent with return types
6. **Error Handling**: Use appropriate error handling mechanisms

## Common Pitfalls

1. **Forgetting return statements** in non-void functions
2. **Parameter type mismatches** when calling functions
3. **Ambiguous overloads** that confuse the compiler
4. **Stack overflow** from excessive recursion
5. **Side effects** in functions that should be pure

## Exam Tips

1. **Remember the rules**: Overloading requires different parameter lists, not just different return types
2. **Understand parameter passing**: Know the difference between pass by value, reference, and pointer
3. **Practice tracing**: Be able to trace through recursive function calls
4. **Know the trade-offs**: Understand when to use inline functions vs regular functions
5. **Template syntax**: Memorize the template<typename T> syntax for function templates
6. **Default parameters**: Remember that default parameters must be specified from right to left
