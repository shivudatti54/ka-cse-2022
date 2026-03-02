# **Exception Handling: Exception Handling Fundamentals, Handling Derived-Class Exceptions, Exception Handling Options, Applying Exception Handling**

## **Table of Contents**

1. [Exception Handling Fundamentals](#exception-handling-fundamentals)
2. [Handling Derived-Class Exceptions](#handling-derived-class-exceptions)
3. [Exception Handling Options](#exception-handling-options)
4. [Applying Exception Handling](#applying-exception-handling)

## **Exception Handling Fundamentals**

Exception handling is a mechanism that allows a program to recover from errors and unexpected events. In C++, exceptions are used to handle runtime errors, such as division by zero or null pointer dereferences.

- **Definition:** Exception handling is a process of catching and handling exceptions, which are exceptions to the normal flow of the program.
- **Purpose:** The purpose of exception handling is to prevent the program from crashing or terminating unexpectedly.

**Key Concepts:**

- **Exception:** An exception is an event that occurs during the execution of a program, such as division by zero or null pointer dereference.
- **Exception Handling Mechanism:** Exception handling mechanisms are used to detect and handle exceptions.
- **Throw Statement:** The throw statement is used to declare an exception and transfer control to the exception handling mechanism.
- **catch Clause:** The catch clause is used to handle exceptions.

**Example:**

```cpp
#include <iostream>

void divide(int numerator, int denominator) {
    try {
        if (denominator == 0) {
            throw std::runtime_error("Division by zero");
        }
        int result = numerator / denominator;
        std::cout << "Result: " << result << std::endl;
    }
    catch (const std::runtime_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
}

int main() {
    divide(10, 0);
    return 0;
}
```

In this example, the `divide` function throws a `std::runtime_error` exception when the denominator is zero. The `catch` clause is used to handle this exception and display an error message.

## **Handling Derived-Class Exceptions**

When you have a derived-class exception, you can handle it in the same way as a base-class exception. The `catch` clause can specify a specific exception type to handle.

- **Declaration:** `catch (ExceptionType& e) {`
- **Example:**

```cpp
#include <iostream>
#include <stdexcept>

class CustomException : public std::runtime_error {
public:
    CustomException(const std::string& message) : std::runtime_error(message) {}
};

void divide(int numerator, int denominator) {
    try {
        if (denominator == 0) {
            throw CustomException("Division by zero");
        }
        int result = numerator / denominator;
        std::cout << "Result: " << result << std::endl;
    }
    catch (const CustomException& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    catch (const std::runtime_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
}

int main() {
    divide(10, 0);
    return 0;
}
```

In this example, a `CustomException` class is derived from `std::runtime_error`. The `divide` function throws a `CustomException` exception when the denominator is zero. The `catch` clause is used to handle this exception and display an error message.

## **Exception Handling Options**

C++ provides several exception handling options:

- **Throw Statement:** The `throw` statement is used to declare an exception.
- **try-catch-finally Clause:** The `try-catch-finally` clause is used to handle exceptions and perform cleanup actions.
- **try-catch Block:** The `try-catch` block is used to handle exceptions.

**Example:**

```cpp
#include <iostream>
#include <stdexcept>

void divide(int numerator, int denominator) {
    try {
        if (denominator == 0) {
            throw std::runtime_error("Division by zero");
        }
        int result = numerator / denominator;
        std::cout << "Result: " << result << std::endl;
    }
    catch (const std::runtime_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    catch (...) {
        std::cerr << "Unknown error" << std::endl;
    }
}

int main() {
    divide(10, 0);
    return 0;
}
```

In this example, the `divide` function uses the `try-catch` block to handle exceptions. The `catch` clause is used to handle exceptions and display error messages.

## **Applying Exception Handling**

Exception handling is a crucial mechanism in C++ programming. Here are some best practices for applying exception handling:

- **Use Exceptions to Handle Errors:** Use exceptions to handle errors and unexpected events.
- **Catch Specific Exceptions:** Catch specific exceptions to handle different types of errors.
- **Perform Cleanup Actions:** Perform cleanup actions to release resources and prevent memory leaks.
- **Keep Exceptions Local:** Keep exceptions local to the method or function where they are thrown.
- **Avoid Overthrowing Exceptions:** Avoid overthrowing exceptions to prevent exceptions from propagating up the call stack.

**Key Takeaways:**

- Exception handling is a mechanism that allows a program to recover from errors and unexpected events.
- Use exceptions to handle errors and unexpected events.
- Catch specific exceptions to handle different types of errors.
- Perform cleanup actions to release resources and prevent memory leaks.
- Keep exceptions local to the method or function where they are thrown.
