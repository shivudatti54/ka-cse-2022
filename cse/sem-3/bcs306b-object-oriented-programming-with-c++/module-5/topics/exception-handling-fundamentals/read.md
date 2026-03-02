# Exception Handling Fundamentals

## Introduction

Exception handling is a powerful mechanism in C++ that provides a structured way to handle runtime errors and exceptional conditions that may occur during program execution. In C++, traditional error handling using return codes and error flags often leads to complex and error-prone code, especially when multiple functions are involved. Exception handling in C++ offers a cleaner alternative by separating error detection from error handling, allowing programs to respond to exceptional circumstances in a more graceful and maintainable manner.

The fundamental philosophy behind exception handling is that a function that detects an error condition can "throw" an exception, and the appropriate handler somewhere up the call stack can "catch" and process it. This mechanism ensures that errors are not silently ignored, as unhandled exceptions typically cause program termination. Understanding exception handling is crucial for developing robust C++ applications, as it enables programmers to write code that can handle unexpected situations gracefully while maintaining program stability and producing meaningful error messages for debugging purposes.

In the context of object-oriented programming with C++, exception handling becomes even more significant as it integrates seamlessly with the class hierarchies and RAII (Resource Acquisition Is Initialization) principles commonly used in C++ applications. This topic covers the fundamental concepts, syntax, and best practices of exception handling that every C++ programmer must master.

## Key Concepts

### Exception Handling Mechanism

The C++ exception handling mechanism revolves around three keywords: **try**, **throw**, and **catch**. A try block encloses the code that might throw an exception, a throw statement actually throws an exception when an error condition is detected, and catch blocks handle specific types of exceptions.

The syntax involves wrapping potentially risky code within a try block, followed by one or more catch blocks that specify the type of exception they can handle:

```cpp
try {
 // Code that might throw an exception
 risky_operation();
}
catch (exception_type1& e) {
 // Handle exception_type1
}
catch (exception_type2& e) {
 // Handle exception_type2
}
```

### Throwing Exceptions

The **throw** keyword is used to signal that an exceptional condition has occurred. When a throw statement is executed, the normal program flow is interrupted, and the exception propagation mechanism searches for an appropriate catch handler. An exception can be thrown with any data type, including primitive types, pointers, and class objects. Throwing class objects (especially those derived from the standard exception class) is the preferred approach as it allows for richer error information.

```cpp
void divide(int a, int b) {
 if (b == 0) {
 throw "Division by zero!";
 }
 cout << "Result: " << a / b << endl;
}
```

### Catch Block Behavior

Catch blocks are examined in sequence, and the first one capable of handling the thrown exception type is executed. It is important to note that catch blocks should be ordered from most specific to most general types, as more general catch handlers will intercept exceptions intended for more specific handlers. Additionally, catch blocks can catch exceptions by value, by reference, or by pointer, with catching by reference being the recommended approach to avoid object slicing.

```cpp
try {
 throw runtime_error("Error occurred");
}
catch (const runtime_error& e) {
 cout << "Caught: " << e.what() << endl;
}
```

### Exception Specifications and noexcept

Modern C++ provides the **noexcept** specifier to indicate whether a function is expected to throw exceptions. Functions marked as noexcept promise not to throw exceptions, and if they do, std::terminate is called immediately. This specifier is important for optimization opportunities and for communicating contract expectations to users of a function. C++ also supports dynamic exception specifications (deprecated in C++11 and removed in C++17), which should be avoided in modern code.

### Standard Exception Hierarchy

C++ provides a comprehensive hierarchy of standard exception classes defined in the `<exception>` header. At the root is the base class `std::exception`, which provides the virtual `what()` method for obtaining error messages. Key derived classes include `std::runtime_error` (for errors detectable only at runtime), `std::logic_error` (for errors detectable before program execution), `std::bad_alloc` (for memory allocation failures), and `std::bad_cast` (for failed dynamic casts). Using these standard exception types ensures consistency and allows for more generic exception handling.

### Stack Unwinding

When an exception is thrown, the C++ runtime system performs stack unwinding, destroying local objects as the stack is popped to find an appropriate handler. This process ensures that properly written destructors are called, making RAII-based resource management work correctly with exceptions. However, this also means that any cleanup code must be placed in destructors or use RAII wrappers rather than relying on code after a throw statement.

### Rethrowing Exceptions

Sometimes after catching an exception, a handler may not be able to fully handle the exception and needs to propagate it to an outer try-catch block. This is achieved using a rethrow statement with just the `throw;` keyword (without any operand). Rethrowing is useful when performing partial cleanup while allowing the exception to continue propagating.

```cpp
try {
 // Some operation
}
catch (const exception& e) {
 log_error(e.what());
 throw; // Rethrow the same exception
}
```

### Multiple Exceptions

A try block can be followed by multiple catch blocks to handle different types of exceptions differently. The ellipsis catch handler `catch(...)` can catch any exception that doesn't match previous handlers, providing a last-resort handler. This is particularly useful for logging or performing cleanup before program termination.

## Examples

### Example 1: Basic Exception Handling with Division

Write a program that performs division with exception handling for division by zero:

```cpp
#include <iostream>
#include <stdexcept>
using namespace std;

class DivisionException : public runtime_error {
public:
 DivisionException() : runtime_error("Division by zero attempted") {}
};

double divide(int numerator, int denominator) {
 if (denominator == 0) {
 throw DivisionException();
 }
 return static_cast<double>(numerator) / denominator;
}

int main() {
 int a, b;
 cout << "Enter numerator: ";
 cin >> a;
 cout << "Enter denominator: ";
 cin >> b;

 try {
 double result = divide(a, b);
 cout << "Result: " << result << endl;
 }
 catch (const DivisionException& e) {
 cout << "Error: " << e.what() << endl;
 return 1;
 }

 return 0;
}
```

**Step-by-step solution:**

1. Define a custom exception class `DivisionException` inheriting from `runtime_error`
2. In the `divide()` function, check if denominator is zero before performing division
3. If denominator is zero, throw the custom exception with an appropriate message
4. In main(), wrap the division call in a try block
5. Catch the exception and display the error message, returning error code 1 on failure

### Example 2: Multiple Exception Types

Create a program that handles different types of exceptions for array operations:

```cpp
#include <iostream>
#include <stdexcept>
using namespace std;

class Array {
private:
 int* arr;
 int size;

public:
 Array(int s) : size(s) {
 arr = new int[size];
 }

 ~Array() {
 delete[] arr;
 }

 int& operator[](int index) {
 if (index < 0 || index >= size) {
 throw out_of_range("Array index out of bounds");
 }
 return arr[index];
 }

 void fill(int value) {
 if (size <= 0) {
 throw invalid_argument("Invalid array size");
 }
 for (int i = 0; i < size; i++) {
 arr[i] = value;
 }
 }
};

int main() {
 try {
 Array arr(5);

 // Test out_of_range exception
 arr[10] = 100;
 }
 catch (const out_of_range& e) {
 cout << "Out of range error: " << e.what() << endl;
 }
 catch (const invalid_argument& e) {
 cout << "Invalid argument: " << e.what() << endl;
 }
 catch (const exception& e) {
 cout << "General error: " << e.what() << endl;
 }

 cout << "Program continues after handling exception" << endl;
 return 0;
}
```

**Step-by-step solution:**

1. Create an Array class with bounds checking in the subscript operator
2. The operator[] throws `out_of_range` for invalid indices
3. The fill() method throws `invalid_argument` for invalid sizes
4. In main(), attempt an out-of-bounds access to trigger the first catch block
5. Multiple catch blocks handle different exception types specifically
6. The general `exception` catch acts as a fallback for any other exceptions

### Example 3: Nested Try-Catch with Rethrowing

Implement a file processing scenario with nested exception handling:

```cpp
#include <iostream>
#include <fstream>
#include <stdexcept>
using namespace std;

void processFile(const string& filename) {
 ifstream file(filename);
 if (!file.is_open()) {
 throw runtime_error("Cannot open file: " + filename);
 }

 // Process file contents
 string line;
 while (getline(file, line)) {
 cout << line << endl;
 }
}

void handleData() {
 try {
 processFile("data.txt");
 }
 catch (const runtime_error& e) {
 cerr << "File error: " << e.what() << endl;
 throw; // Rethrow to let outer handler deal with it
 }
}

int main() {
 try {
 handleData();
 }
 catch (const exception& e) {
 cout << "Final handler caught: " << e.what() << endl;
 return 1;
 }

 cout << "File processed successfully" << endl;
 return 0;
}
```

**Step-by-step solution:**

1. The `processFile()` function throws a runtime_error if the file cannot be opened
2. The `handleData()` function wraps the processFile call in its own try-catch
3. After logging the error, it rethrows the exception using `throw;` for outer handling
4. The main() function provides the final catch block that handles the rethrown exception
5. This demonstrates proper error propagation through multiple levels of the call stack

## Exam Tips

1. **Remember the three keywords**: The exception handling mechanism in C++ is built on try (to monitor), throw (to signal), and catch (to handle) - these three are essential for any exception handling code.

2. **Order of catch blocks matters**: Always place more specific exception handlers before general ones. Placing `catch(...)` last ensures it catches any unhandled exceptions.

3. **Catch by reference**: Always catch exceptions by reference (preferably const reference) to avoid object slicing and unnecessary copying.

4. **Standard exception hierarchy**: Know that `std::exception` is the base class, with `runtime_error` and `logic_error` being important derived classes for custom exceptions.

5. **Use what() method**: The virtual `what()` method inherited from `std::exception` returns a C-string describing the error - this is crucial for meaningful error messages.

6. **Stack unwinding ensures RAII**: Local objects are destroyed during stack unwinding, making RAII (destructors for resource cleanup) work correctly with exceptions.

7. **Custom exception classes**: For exam problems, creating custom exception classes by inheriting from `std::runtime_error` or `std::logic_error` demonstrates better OOP understanding.

8. **noexcept functions**: Remember that functions marked as noexcept will call std::terminate if they throw an exception, rather than allowing it to propagate.
