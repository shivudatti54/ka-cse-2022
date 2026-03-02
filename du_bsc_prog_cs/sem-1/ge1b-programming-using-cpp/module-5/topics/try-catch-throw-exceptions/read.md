# Exception Handling in C++ (try-catch-throw)

## Introduction

Exception handling is a powerful mechanism in C++ that provides a structured way to handle runtime errors and exceptional conditions that may occur during program execution. Instead of using traditional error codes that must be checked at every function call, C++ offers a clean separation between normal program logic and error-handling code through the try-catch-throw paradigm. This topic is fundamental for developing robust, production-quality software that can gracefully handle unexpected situations such as invalid input, file not found, memory allocation failures, or division by zero.

In the University of Delhi Computer Science curriculum, exception handling forms a critical part of the software development paradigm. Understanding exception handling is essential not only for writing correct programs but also for building systems that are maintainable and scalable. Modern C++ programming heavily relies on exceptions for error reporting, especially in the Standard Template Library (STL) and frameworks like Qt and Boost. Students must master these concepts to write programs that meet industry standards and succeed in their end-semester examinations.

## Key Concepts

### What is an Exception?

An exception is an unexpected event or error condition that disrupts the normal flow of program execution. Exceptions can be caused by various factors including invalid user input, hardware failures, resource constraints, or logical errors in the code. When an exceptional situation occurs, the program needs to detect it and respond appropriately rather than crashing abruptly.

### The try Block

The try block encloses a group of statements that might generate an exception. It is the region of code where exceptions are monitored. If any statement within the try block throws an exception, the control immediately transfers to the nearest matching catch block. The syntax requires that every try block must be followed by at least one catch block, otherwise it results in a compilation error.

```cpp
try {
    // Code that might throw an exception
    int result = division(a, b);
    cout << "Result: " << result << endl;
}
```

### The throw Statement

The throw keyword is used to signal that an exceptional condition has occurred. When throw is executed, it creates an exception object and transfers control to the nearest matching catch block. The throw statement can throw any type of data including built-in types, user-defined types, and even standard exception objects.

```cpp
throw 10;           // Throws an integer
throw "Error";      // Throws a C-string
throw runtime_error("Custom error message");
```

### The catch Block

The catch block is a specialized exception handler that catches exceptions thrown within the corresponding try block. Each catch block is designed to handle a specific type of exception. When an exception is thrown, the runtime system searches for the first catch block that can handle the thrown exception type (exception matching follows specific rules including base-derived relationships).

```cpp
catch (int e) {
    cout << "Integer exception caught: " << e << endl;
}
catch (const string& e) {
    cout << "String exception: " << e << endl;
}
catch (...) {
    cout << "All other exceptions caught" << endl;
}
```

### Exception Hierarchy in C++

C++ provides a comprehensive hierarchy of standard exceptions defined in the `<stdexcept>` header. At the root of this hierarchy is `std::exception`, which provides a virtual what() function to obtain a description of the exception. The hierarchy includes `std::logic_error` (for detectable errors in program logic), `std::runtime_error` (for errors detectable only at runtime), and various derived classes like `std::invalid_argument`, `std::out_of_range`, `std::overflow_error`, and `std::underflow_error`.

### Custom Exception Classes

For application-specific error handling, programmers can create custom exception classes by inheriting from `std::exception` or one of its derived classes. This allows for rich error information and type-safe exception handling. Custom exceptions should override the `what()` function to provide meaningful error messages.

```cpp
class InvalidAgeException : public std::exception {
private:
    string message;
public:
    InvalidAgeException(const string& msg) : message(msg) {}
    const char* what() const noexcept override {
        return message.c_str();
    }
};
```

### Exception Specifications and noexcept

The noexcept specifier (introduced in C++11) indicates that a function does not throw exceptions. If a noexcept function throws an exception, `std::terminate` is called immediately. This specifier helps the compiler optimize code and provides a guarantee to callers about exception safety. The older throw() specification is deprecated but still seen in legacy code.

```cpp
void criticalFunction() noexcept {
    // This function promises not to throw
}
```

### Exception Safety Levels

There are three levels of exception safety that a function can provide: basic guarantee (the program remains in a valid state), strong guarantee (either the operation succeeds completely or has no effect), and noexcept guarantee (the operation will not throw). Writing exception-safe code requires careful design and understanding of RAII (Resource Acquisition Is Initialization) principles.

## Examples

### Example 1: Division by Zero Handling

```cpp
#include <iostream>
using namespace std;

double divide(int a, int b) {
    if (b == 0) {
        throw "Division by zero!";
    }
    return static_cast<double>(a) / b;
}

int main() {
    int x = 10, y = 0;
    
    try {
        double result = divide(x, y);
        cout << "Result: " << result << endl;
    }
    catch (const char* msg) {
        cout << "Exception caught: " << msg << endl;
    }
    
    y = 2;
    try {
        double result = divide(x, y);
        cout << "Result: " << result << endl;
    }
    catch (const char* msg) {
        cout << "Exception caught: " << msg << endl;
    }
    
    return 0;
}
```

Output:
```
Exception caught: Division by zero!
Result: 5
```

### Example 2: Using Standard Exception Classes

```cpp
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;

int main() {
    vector<int> v(5);
    
    try {
        // Attempt to access invalid index
        cout << v.at(10) << endl;
    }
    catch (const out_of_range& e) {
        cout << "Out of range exception: " << e.what() << endl;
    }
    catch (const exception& e) {
        cout << "Standard exception: " << e.what() << endl;
    }
    
    try {
        // Intentional overflow
        int* arr = new int[1000000000000];
    }
    catch (const bad_alloc& e) {
        cout << "Memory allocation failed: " << e.what() << endl;
    }
    
    return 0;
}
```

### Example 3: Custom Exception Class

```cpp
#include <iostream>
#include <exception>
#include <string>
using namespace std;

class BankAccount {
private:
    double balance;
    string accountName;
    
public:
    BankAccount(const string& name, double initialBalance) 
        : accountName(name), balance(initialBalance) {}
    
    void withdraw(double amount) {
        if (amount < 0) {
            throw invalid_argument("Withdrawal amount cannot be negative");
        }
        if (amount > balance) {
            throw runtime_error("Insufficient funds");
        }
        balance -= amount;
        cout << "Withdrawal successful. New balance: " << balance << endl;
    }
    
    void deposit(double amount) {
        if (amount < 0) {
            throw invalid_argument("Deposit amount cannot be negative");
        }
        balance += amount;
        cout << "Deposit successful. New balance: " << balance << endl;
    }
};

int main() {
    BankAccount account("John Doe", 1000);
    
    try {
        account.deposit(500);
        account.withdraw(2000);  // This will throw
    }
    catch (const invalid_argument& e) {
        cout << "Invalid argument: " << e.what() << endl;
    }
    catch (const runtime_error& e) {
        cout << "Runtime error: " << e.what() << endl;
    }
    
    try {
        account.withdraw(-100);  // Negative withdrawal
    }
    catch (const invalid_argument& e) {
        cout << "Invalid argument: " << e.what() << endl;
    }
    
    return 0;
}
```

## Exam Tips

1. **Remember the syntax order**: In C++, exceptions must be caught in the order of most derived to base class. If you catch `std::exception` before `std::runtime_error`, the more specific exception will never be caught.

2. **Use ellipsis catch for universal handling**: The catch(...) block catches all exceptions, useful when you don't care about the exception type, but should be used sparingly as it provides no information about the exception.

3. **Understand when to use exceptions vs return codes**: For constructor failures and operator overloading, exceptions are preferred. For performance-critical code in tight loops, traditional error handling might be more appropriate.

4. **Rethrow exceptions carefully**: When you catch an exception and want to propagate it further, use `throw;` (without arguments) to rethrow the original exception and preserve the exception stack trace.

5. **Noexcept functions**: Remember that if a function is declared noexcept and throws an exception, the program calls `std::terminate()` immediately without calling destructors for local objects.

6. **RAII principle**: Use RAII (Resource Acquisition Is Initialization) with smart pointers and other RAII wrappers to ensure proper resource cleanup even when exceptions occur.

7. **Standard exception hierarchy**: Know the difference between `std::logic_error` (programmer's fault, detectable before runtime) and `std::runtime_error` (only detectable at runtime). This distinction is frequently tested in exams.