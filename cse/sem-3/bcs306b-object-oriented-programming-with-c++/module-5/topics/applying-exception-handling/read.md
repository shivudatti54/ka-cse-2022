# Applying Exception Handling in C++

## Introduction

Exception handling is a powerful mechanism in C++ that provides a structured way to handle runtime errors and exceptional conditions that may occur during program execution. Unlike traditional error handling techniques such as return codes or error flags, exception handling separates error detection from error handling, making code more readable, maintainable, and robust. In the context of Object-Oriented Programming with C++, exception handling becomes particularly important as it integrates seamlessly with class hierarchies and object lifecycles.

The need for exception handling arises from the fact that many operations in C++ can fail in ways that cannot be handled locally. For instance, when allocating memory dynamically, the system may run out of memory. When accessing array elements, we might encounter index out of bounds. When performing file operations, the file might not exist or be inaccessible. Traditional error handling approaches often lead to cluttered code with numerous if-else checks scattered throughout the program. Exception handling provides a cleaner alternative by propagating errors to appropriate handlers that can decide how to respond.

In the university's Object-Oriented Programming with C++ curriculum, understanding exception handling is essential for developing professional-quality software. It is particularly crucial when working with constructors, destructors, and polymorphic class hierarchies where error conditions need to be communicated across object boundaries. This module covers the practical application of exception handling mechanisms in C++ programs.

## Key Concepts

### The try-catch-throw Mechanism

The foundation of exception handling in C++ consists of three keywords: try, catch, and throw. The **try block** contains the code that might throw an exception. It is followed by one or more **catch blocks** that handle specific types of exceptions. When an error condition is detected within the try block, a program can **throw** an exception using the throw keyword, which transfers control to the appropriate catch handler.

The syntax involves wrapping potentially dangerous code in a try block, followed by catch handlers that specify the type of exception they can handle:

```cpp
try {
 // Code that might throw an exception
 if (error_condition) {
 throw exception_value;
 }
} catch (type1 arg) {
 // Handle exception of type1
} catch (type2 arg) {
 // Handle exception of type2
}
```

### Exception Types and Multiple Catch Blocks

C++ allows throwing exceptions of any type, including primitive types, classes, and pointers. When an exception is thrown, the runtime system searches through the catch blocks in order, looking for the first handler whose type matches the thrown exception type. This process is called exception matching. For class types, the catch handler can also handle exceptions of derived class types if the catch parameter is a reference or pointer to the base class.

Multiple catch blocks can be used to handle different exception types differently:

```cpp
try {
 // Risky operations
} catch (const std::overflow_error& e) {
 std::cout << "Overflow: " << e.what() << std::endl;
} catch (const std::runtime_error& e) {
 std::cout << "Runtime error: " << e.what() << std::endl;
} catch (const std::exception& e) {
 std::cout << "Standard exception: " << e.what() << std::endl;
} catch (...) {
 std::cout << "Unknown exception caught" << std::endl;
}
```

The catch(...) handler is a special handler that catches any exception type, useful as a last resort handler or for cleanup operations.

### Exception Specifications and noexcept

C++11 introduced the **noexcept** specifier to indicate whether a function might throw exceptions. A function declared as noexcept promises not to throw exceptions. If such a function throws an exception, std::terminate is called immediately. This specifier helps the compiler optimize code and provides important documentation about function behavior:

```cpp
void criticalOperation() noexcept {
 // This function guarantees not to throw
}

void potentiallyRisky() {
 // May throw exceptions
}
```

### Stack Unwinding and Exception Propagation

When an exception is thrown, the C++ runtime system performs **stack unwinding**: it destroys all local objects that were created in the try block and in functions on the call stack between the throw point and the catch handler. This ensures proper resource cleanup and prevents memory leaks. However, if a destructor throws an exception during stack unwinding, std::terminate is called, making it crucial to ensure destructors do not throw.

### Rethrowing Exceptions

A catch handler can choose to rethrow the exception it catches using `throw;` (without an argument). This is useful when a handler can partially handle an exception but needs to pass it to an outer catch block:

```cpp
try {
 // Some operation
} catch (const std::exception& e) {
 std::log_error(e.what());
 throw; // Rethrow the same exception
}
```

### User-Defined Exceptions

For application-specific error handling, C++ allows creating custom exception classes, typically derived from std::exception. This enables meaningful error messages and hierarchical exception handling:

```cpp
class MyException : public std::exception {
 std::string msg;
public:
 MyException(const std::string& m) : msg(m) {}
 const char* what() const noexcept override {
 return msg.c_str();
 }
};

throw MyException("Custom error occurred");
```

### Exception Handling in Constructors and Destructors

Exception handling in constructors requires special attention because if a constructor throws an exception, the object being constructed is never considered fully created, and its destructor will not be called. This necessitates careful resource management using try-catch blocks within constructors or using smart pointers for dynamic resources.

In destructors, throwing exceptions is strongly discouraged because destructors may be called during stack unwinding due to another exception. If a destructor throws during this process, std::terminate is invoked.

## Examples

### Example 1: Division by Zero Handling

```cpp
#include <iostream>
#include <stdexcept>

double divide(double a, double b) {
 if (b == 0) {
 throw std::invalid_argument("Division by zero is not allowed");
 }
 return a / b;
}

int main() {
 double x = 10.0, y = 0.0;

 try {
 double result = divide(x, y);
 std::cout << "Result: " << result << std::endl;
 } catch (const std::invalid_argument& e) {
 std::cout << "Error caught: " << e.what() << std::endl;
 std::cout << "Please provide a non-zero divisor" << std::endl;
 }

 return 0;
}
```

In this example, when y equals zero, the divide function throws a std::invalid_argument exception. The catch block catches this specific exception type and provides a user-friendly error message. The program continues execution after handling the exception rather than terminating abruptly.

### Example 2: File Processing with Exception Handling

```cpp
#include <iostream>
#include <fstream>
#include <stdexcept>

class FileHandler {
private:
 std::ifstream file;
 std::string filename;

public:
 FileHandler(const std::string& name) : filename(name) {
 file.open(filename);
 if (!file.is_open()) {
 throw std::runtime_error("Cannot open file: " + filename);
 }
 }

 void readData() {
 if (!(file >> std::ws)) {
 throw std::runtime_error("File is empty or unreadable");
 }
 // Process file data
 }

 ~FileHandler() {
 if (file.is_open()) {
 file.close();
 }
 }
};

int main() {
 try {
 FileHandler handler("data.txt");
 handler.readData();
 std::cout << "File processed successfully" << std::endl;
 } catch (const std::runtime_error& e) {
 std::cerr << "File error: " << e.what() << std::endl;
 return 1;
 }

 return 0;
}
```

This example demonstrates exception handling in a class that manages file resources. The constructor throws an exception if the file cannot be opened, and the readData method throws if the file cannot be read. The main function handles these exceptions appropriately, demonstrating how exceptions can propagate through multiple layers of function calls.

### Example 3: Custom Exception Hierarchy

```cpp
#include <iostream>
#include <exception>
#include <string>

class BankException : public std::exception {
protected:
 std::string message;
public:
 BankException(const std::string& msg) : message(msg) {}
 const char* what() const noexcept override {
 return message.c_str();
 }
};

class InsufficientFundsException : public BankException {
 double balance;
 double withdrawal;
public:
 InsufficientFundsException(double bal, double with)
 : BankException("Insufficient funds"), balance(bal), withdrawal(with) {}

 void display() const {
 std::cout << "Current Balance: " << balance << std::endl;
 std::cout << "Requested Withdrawal: " << withdrawal << std::endl;
 }
};

class Account {
 double balance;
public:
 Account(double initial) : balance(initial) {}

 void withdraw(double amount) {
 if (amount > balance) {
 throw InsufficientFundsException(balance, amount);
 }
 balance -= amount;
 std::cout << "Withdrawal successful. New balance: " << balance << std::endl;
 }
};

int main() {
 Account acc(1000.0);

 try {
 acc.withdraw(1500.0); // This will throw
 } catch (const InsufficientFundsException& e) {
 std::cout << "Exception: " << e.what() << std::endl;
 e.display();
 } catch (const BankException& e) {
 std::cout << "Bank error: " << e.what() << std::endl;
 } catch (const std::exception& e) {
 std::cout << "Unexpected error: " << e.what() << std::endl;
 }

 return 0;
}
```

This comprehensive example shows a custom exception hierarchy. The base class BankException inherits from std::exception, and InsufficientFundsException inherits from it. The catch blocks are ordered from most specific to most general, ensuring that derived class exceptions are caught by their specific handlers.

## Exam Tips

1. **Remember the exception handling syntax**: The correct order is try → catch blocks immediately after. A try block must be followed by at least one catch block, otherwise compilation error occurs.

2. **Exception matching rules**: C++ uses best-match semantics. For class types, a catch handler with a reference parameter can catch exceptions of derived types. Catch blocks should be ordered from most derived to least derived class.

3. **Always catch by const reference**: Use `catch(const std::exception& e)` rather than catching by value, which would cause object slicing and lose derived class information.

4. **The catch(...) handler**: This catches any exception type. Place it as the last catch block to handle unexpected exceptions gracefully.

5. **Exception safety guarantee levels**: Understand the three levels - basic guarantee (object remains usable), strong guarantee (operation either succeeds or has no effect), and noexcept guarantee (function will not throw).

6. **Stack unwinding**: Remember that local objects are destroyed during stack unwinding. This is why RAII (Resource Acquisition Is Initialization) with RAII-compliant classes like smart pointers is important.

7. **Destructors should never throw**: If a destructor throws during exception handling, std::terminate is called. Always wrap potentially throwing operations in try-catch within destructors if necessary.

8. **noexcept functions**: Functions marked as noexcept that throw exceptions will result in immediate calls to std::terminate.

9. **Re-throwing exceptions**: Use `throw;` to rethrow the caught exception. Do not use `throw e;` as this creates a copy and changes the exception type information.

10. **Standard exception hierarchy**: Know the hierarchy: std::exception → std::logic_error → std::runtime_error, and their derived classes like invalid_argument, out_of_range, overflow_error.
