# Exception Handling Options in C++

## Introduction

Exception handling is a powerful mechanism in C++ that provides a structured way to handle runtime errors and exceptional conditions that disrupt the normal flow of program execution. In traditional error handling approaches, functions return error codes or set global error variables, which often leads to cluttered code and ignored error conditions. Exception handling in C++ offers a cleaner, more robust approach by separating error detection from error handling, allowing programmers to write more maintainable and reliable software.

The concept of exception handling was introduced in C++ to address the limitations of traditional error-handling techniques. When a function encounters an error that it cannot handle, it can "throw" an exception, which is then "caught" by an appropriate handler elsewhere in the program. This mechanism allows errors to be propagated up the call stack until a suitable handler is found, enabling centralized error handling and proper resource cleanup. Understanding exception handling is essential for developing professional-grade C++ applications, especially in scenarios involving file operations, memory allocation, network communications, and other operations that can fail during execution.

This topic covers the complete spectrum of exception handling options available in C++, including the try-catch-throw paradigm, standard library exceptions, custom exception classes, best practices for exception safety, and common pitfalls to avoid. Mastery of these concepts is crucial for university examination success and for writing production-quality C++ code.

## Key Concepts

### The Try-Catch-Throw Paradigm

The foundation of exception handling in C++ rests on three essential keywords: try, catch, and throw. A try block encloses the code that might potentially throw an exception. When an exception occurs within the try block, the runtime system searches for an appropriate catch block to handle it. The throw keyword is used to explicitly signal that an exceptional condition has occurred.

The syntax involves wrapping potentially dangerous code in a try block, followed by one or more catch blocks that handle specific types of exceptions. When an exception is thrown, the catch blocks are examined in order, and the first catch block capable of handling the exception type is executed. If no matching catch block is found, the program terminates after calling the std::terminate function.

```cpp
#include <iostream>
using namespace std;

int divide(int a, int b) {
 if (b == 0) {
 throw "Division by zero error";
 }
 return a / b;
}

int main() {
 try {
 cout << "Result: " << divide(10, 0) << endl;
 }
 catch (const char* msg) {
 cout << "Exception caught: " << msg << endl;
 }
 return 0;
}
```

### Exception Types and Matching

C++ supports both built-in types and user-defined types as exceptions. When an exception is thrown, the catch blocks use exception specifications to determine appropriate handlers. Exception matching follows specific rules: exact type matches, matches to base classes, and matches to const or volatile qualified versions. Understanding these matching rules is crucial for writing effective exception handlers.

The catch block can catch exceptions by value, by reference, or by pointer. Catching by reference is generally preferred as it avoids unnecessary copying and properly handles polymorphism. When catching by value, object slicing can occur, losing derived class information. Catching by pointer requires careful consideration of exception ownership and lifetime.

### Standard Exception Hierarchy

The C++ Standard Library provides a comprehensive hierarchy of exception classes defined in the `<stdexcept>` header. At the root of this hierarchy is std::exception, which serves as the base class for all standard exceptions. The standard exception hierarchy includes logic_error (errors detectable before program execution), runtime_error (errors detectable during execution), and their various derived classes such as invalid_argument, out_of_range, length_error, and overflow_error.

Understanding this hierarchy allows programmers to catch exceptions at appropriate levels of granularity. For instance, catching std::runtime_error will handle all runtime errors, while catching specific types like std::out_of_range allows for more targeted error handling. The what() member function, inherited from std::exception, returns a C-style string describing the exception.

### Custom Exception Classes

For application-specific error conditions, programmers can create custom exception classes by deriving them from std::exception or from more specific standard exception classes. Custom exceptions should override the what() function to provide meaningful error messages. They can also include additional data members to carry context-specific information about the error.

```cpp
#include <exception>
#include <string>

class BankAccountException : public std::exception {
private:
 std::string message;
public:
 BankAccountException(const std::string& msg) : message(msg) {}

 const char* what() const noexcept override {
 return message.c_str();
 }
};

class InsufficientFundsException : public BankAccountException {
private:
 double balance;
 double requested;
public:
 InsufficientFundsException(double bal, double req)
 : BankAccountException("Insufficient funds"), balance(bal), requested(req) {}

 double getBalance() const { return balance; }
 double getRequested() const { return requested; }
};
```

### Exception Specifications and noexcept

Prior to C++11, exception specifications were used to declare which exceptions a function might throw. However, these were deprecated in C++11 and removed in C++17 in favor of the noexcept specifier. The noexcept keyword indicates that a function is guaranteed not to throw exceptions. Marking functions as noexcept allows the compiler to optimize code and provides important guarantees to callers about the function's behavior.

Functions marked as noexcept that nevertheless throw exceptions will result in std::terminate being called. The noexcept operator can also be used in constant expressions to check if a particular expression is noexcept. Understanding noexcept is essential for modern C++ programming and for writing exception-safe code.

### Exception Safety Guarantees

Exception safety refers to the guarantees a function or code segment provides regarding exceptions. C++ provides several levels of exception safety: the basic guarantee ensures that no resources are leaked and objects remain in a valid (though unspecified) state; the strong guarantee ensures that the program state remains unchanged if an exception occurs (essentially making operations atomic); and the nothrow guarantee ensures that exceptions are never thrown.

Writing exception-safe code requires careful consideration of resource management, often employing techniques such as RAII (Resource Acquisition Is Initialization) with smart pointers, using standard library containers that manage memory automatically, and designing functions to provide appropriate exception safety guarantees based on their requirements.

### Multiple Exceptions and Catch All

When multiple different exceptions can be thrown from within a try block, multiple catch blocks can handle each type separately. This allows for differentiated handling based on the specific error that occurred. Additionally, the ellipsis catch handler (catch(...)) can catch any exception type, serving as a fallback handler for unexpected exceptions.

The order of catch blocks is significant: more specific exception types should be caught before more general ones. Attempting to catch a base class before a derived class will result in the derived class exception being sliced when caught by the base class handler.

## Examples

### Example 1: Basic Exception Handling with Multiple Catch Blocks

Consider a function that performs division and can throw different types of exceptions based on the nature of the error:

```cpp
#include <iostream>
#include <stdexcept>
using namespace std;

double safeDivide(double numerator, double denominator) {
 if (denominator == 0) {
 throw invalid_argument("Denominator cannot be zero");
 }
 if (denominator < 0) {
 throw domain_error("Denominator cannot be negative");
 }
 if (numerator > DBL_MAX * denominator) {
 throw overflow_error("Result too large");
 }
 return numerator / denominator;
}

int main() {
 double num = 100, den = 0;

 try {
 double result = safeDivide(num, den);
 cout << "Result: " << result << endl;
 }
 catch (const invalid_argument& e) {
 cout << "Invalid argument: " << e.what() << endl;
 }
 catch (const domain_error& e) {
 cout << "Domain error: " << e.what() << endl;
 }
 catch (const overflow_error& e) {
 cout << "Overflow error: " << e.what() << endl;
 }
 catch (const exception& e) {
 cout << "Standard exception: " << e.what() << endl;
 }

 return 0;
}
```

This example demonstrates proper ordering of catch blocks from most specific to most general, ensuring that each exception type is handled appropriately.

### Example 2: Custom Exception with Inheritance

Here's a comprehensive example demonstrating custom exception classes with inheritance hierarchy:

```cpp
#include <iostream>
#include <exception>
#include <string>
using namespace std;

// Base exception class
class VehicleException : public exception {
protected:
 string msg;
public:
 VehicleException(const string& message) : msg(message) {}
 const char* what() const noexcept override {
 return msg.c_str();
 }
};

// Derived exception for specific errors
class SpeedException : public VehicleException {
private:
 double currentSpeed;
 double maxSpeed;
public:
 SpeedException(double current, double max, const string& msg)
 : VehicleException(msg), currentSpeed(current), maxSpeed(max) {}

 double getCurrentSpeed() const { return currentSpeed; }
 double getMaxSpeed() const { return maxSpeed; }
};

class Car {
private:
 double speed;
 double maxSpeed;
public:
 Car(double max) : speed(0), maxSpeed(max) {}

 void accelerate(double increment) {
 double newSpeed = speed + increment;
 if (newSpeed > maxSpeed) {
 throw SpeedException(speed, maxSpeed,
 "Cannot exceed maximum speed");
 }
 speed = newSpeed;
 }

 void brake(double decrement) {
 speed = max(0.0, speed - decrement);
 if (speed < 0) {
 throw VehicleException("Speed cannot be negative");
 }
 }

 double getSpeed() const { return speed; }
};

int main() {
 Car myCar(120.0);

 try {
 myCar.accelerate(130.0); // This will throw SpeedException
 }
 catch (const SpeedException& e) {
 cout << "Speed Exception!" << endl;
 cout << "Current: " << e.getCurrentSpeed() << " km/h" << endl;
 cout << "Maximum: " << e.getMaxSpeed() << " km/h" << endl;
 cout << "Message: " << e.what() << endl;
 }
 catch (const VehicleException& e) {
 cout << "Vehicle Exception: " << e.what() << endl;
 }
 catch (const exception& e) {
 cout << "Exception: " << e.what() << endl;
 }

 return 0;
}
```

This example demonstrates polymorphism in exception handling, where a derived class exception (SpeedException) is caught by a handler expecting a base class reference (VehicleException).

### Example 3: Exception Safety with RAII

This example illustrates proper exception safety using RAII principles:

```cpp
#include <iostream>
#include <memory>
using namespace std;

class Resource {
public:
 Resource() { cout << "Resource acquired" << endl; }
 ~Resource() { cout << "Resource released" << endl; }
 void use() { cout << "Resource used" << endl; }
 void fail() { throw runtime_error("Resource operation failed"); }
};

void processWithSafety() {
 // Using unique_ptr for automatic memory management
 unique_ptr<Resource> res = make_unique<Resource>();

 try {
 res->use();
 res->fail(); // Throws exception
 res->use(); // This line never executes
 }
 catch (const runtime_error& e) {
 cout << "Caught: " << e.what() << endl;
 // unique_ptr automatically cleans up when going out of scope
 throw; // Re-throw the exception
 }
}

int main() {
 try {
 processWithSafety();
 }
 catch (const runtime_error& e) {
 cout << "Final handler caught: " << e.what() << endl;
 }

 cout << "Program continues normally" << endl;
 return 0;
}
```

This example demonstrates how RAII with smart pointers ensures proper resource cleanup even when exceptions are thrown, providing the basic exception safety guarantee.

## Exam Tips

1. **Remember the try-catch-throw syntax**: In exams, always remember that exceptions must be thrown within try blocks and caught by corresponding catch blocks. The throw keyword can throw any type including primitive types.

2. **Exception matching rules**: Remember that catch blocks are matched in order, and the first matching catch block is executed. More derived exception types should be caught before base class types to avoid object slicing.

3. **Standard exception hierarchy**: Know the hierarchy starting from std::exception, understanding the difference between logic_error and runtime_error, and remember that all standard exceptions have a what() method.

4. **Avoid empty catch blocks**: Never write empty catch blocks that swallow exceptions without any handling. This is a common poor practice and exam question antipattern.

5. **Use references in catch blocks**: Always catch exceptions by reference (const reference preferred) to avoid object slicing and unnecessary copying.

6. **Understand noexcept**: Remember that functions marked as noexcept that throw exceptions will call std::terminate. The noexcept specifier is the modern replacement for deprecated exception specifications.

7. **Exception safety levels**: Know the three guarantee levels: basic (no leaks, valid state), strong (commit or rollback), and nothrow. RAII is the primary technique for achieving exception safety.

8. **Re-throwing exceptions**: Remember that throw; (without an exception object) re-throws the currently caught exception, which is useful for exception propagation after logging or partial handling.

9. **catch(...) usage**: The catch(...) catches all exceptions and is useful for cleanup operations, but should generally be followed by re-throwing the exception.

10. **Resource management**: In exam questions, always consider whether RAII or try-catch-finally patterns (though finally doesn't exist in C++) are needed for proper resource cleanup.
