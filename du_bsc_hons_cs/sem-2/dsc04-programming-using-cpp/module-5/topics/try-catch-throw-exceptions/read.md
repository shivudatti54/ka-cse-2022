# Exception Handling in C++ (try-catch-throw)

## Introduction

Exception handling is a powerful mechanism in C++ that provides a structured way to deal with runtime errors and exceptional conditions that may arise during program execution. Unlike traditional error handling techniques such as return codes or error flags, exception handling allows programmers to separate error detection from error handling, making code more robust, readable, and maintainable.

In the context of the University of Delhi's Computer Science curriculum, exception handling represents a fundamental paradigm that every C++ programmer must master. Real-world applications frequently encounter situations that cannot be predicted at compile time—division by zero, file not found, memory allocation failures, invalid input, and network failures are all examples of runtime anomalies that can crash an unprepared program. By implementing proper exception handling, developers can ensure that their applications gracefully manage these unexpected conditions rather than terminating abruptly.

This topic covers the three essential components of C++ exception handling: the `try` block for identifying code that might throw exceptions, the `catch` blocks for handling specific exception types, and the `throw` statement for signaling that an exceptional condition has occurred. Understanding these mechanisms is essential for developing professional-quality software that meets industry standards.

## Key Concepts

### The Try Block

The `try` block encloses a section of code where exceptions might occur. When an exception is thrown within a `try` block, the program immediately transfers control to the appropriate `catch` block that can handle that particular exception type. Any code within the `try` block that appears after the point where an exception is thrown will not execute.

The syntax for a try block is straightforward:

```cpp
try {
    // Code that might throw an exception
    // Multiple statements can be placed here
}
```

It is crucial to understand that only exceptions thrown within the `try` block (either directly or in functions called from within it) can be caught by the associated `catch` blocks. If an exception occurs outside a try block and is not caught elsewhere, the program will terminate.

### The Throw Statement

The `throw` statement is used to signal that an exceptional condition has occurred. When a `throw` statement is executed, it creates an exception object that carries information about the error. This object is then propagated up the call stack until it is caught by an appropriate exception handler.

C++ allows throwing of any data type, including primitive types, pointers, and user-defined objects. However, throwing objects of class type (especially those derived from the standard `std::exception` class) is considered best practice because it allows for more informative error messages and cleaner exception hierarchies.

```cpp
throw runtime_error("Division by zero attempted");
throw -1;  // Less informative, not recommended
throw myExceptionClass("Custom error message");
```

### The Catch Block

The `catch` block follows a `try` block and contains the code that handles the exception. Each `catch` block is designed to catch exceptions of a specific type. When an exception is thrown, the runtime system examines each `catch` block in sequence and executes the first one whose type matches the thrown exception.

C++ supports several types of exception handlers:

**Specific Type Catch:**
```cpp
catch (int ex) {
    cout << "Integer exception caught: " << ex << endl;
}
```

**Catch All Handler:**
```cpp
catch (...) {
    cout << "Any exception caught" << endl;
}
```

The ellipsis (`...`) in the catch block parameter list indicates a catch-all handler that can catch any type of exception. This should typically be used as the last catch block to handle any unexpected exceptions.

### Exception Specifications and noexcept

Modern C++ provides the `noexcept` specifier to indicate whether a function might throw exceptions. Functions marked as `noexcept` promise not to throw exceptions, and if they do, `std::terminate` is called immediately. This allows compilers to perform optimizations and helps document the function's exception guarantees.

```cpp
void criticalFunction() noexcept {
    // This function promises not to throw
}
```

### Standard Exception Hierarchy

C++ provides a hierarchy of standard exception classes defined in the `<exception>` header. Understanding this hierarchy helps in creating meaningful exception handlers:

- `std::exception` - Base class for all standard exceptions
- `std::runtime_error` - Errors that occur during runtime
- `std::logic_error` - Errors in program logic
- `std::bad_alloc` - Memory allocation failures
- `std::out_of_range` - Index out of bounds
- `std::invalid_argument` - Invalid argument passed to function

### Stack Unwinding

When an exception is thrown and not caught locally, C++ performs stack unwinding—progressively destroying local objects (calling their destructors) as the exception propagates up the call stack. This ensures proper resource cleanup through RAII (Resource Acquisition Is Initialization) principles. This behavior is particularly important for preventing memory leaks and ensuring that resources are properly released even when exceptions occur.

### Rethrowing Exceptions

Sometimes, after catching an exception, a handler may decide that it cannot fully handle the exception and should propagate it to an outer try-catch block. This is accomplished using `throw;` (without an exception object):

```cpp
catch (exception& e) {
    cerr << "Logging: " << e.what() << endl;
    throw;  // Rethrow the current exception
}
```

It is important to note the difference between `throw;` and `throw e;`. The former rethrows the original exception object, preserving all information, while the latter creates a new exception object (slicing can occur if throwing by value).

## Examples

### Example 1: Division by Zero Handler

```cpp
#include <iostream>
#include <stdexcept>
using namespace std;

double divide(double numerator, double denominator) {
    if (denominator == 0) {
        throw runtime_error("Division by zero is not allowed");
    }
    return numerator / denominator;
}

int main() {
    double a, b, result;
    cout << "Enter numerator: ";
    cin >> a;
    cout << "Enter denominator: ";
    cin >> b;
    
    try {
        result = divide(a, b);
        cout << "Result: " << result << endl;
    }
    catch (runtime_error& e) {
        cout << "Error caught: " << e.what() << endl;
        cout << "Please provide a non-zero denominator." << endl;
    }
    
    return 0;
}
```

**Step-by-step Explanation:**
1. The main function prompts the user for two numbers
2. The `divide()` function is called within a try block
3. If the denominator is zero, `runtime_error` is thrown with a descriptive message
4. The catch block receives the exception and displays the error message
5. The program continues execution after the catch block

### Example 2: Multiple Exception Types

```cpp
#include <iostream>
#include <vector>
#include <stdexcept>
using namespace std;

int main() {
    vector<int> numbers = {10, 20, 30, 40, 50};
    int index;
    
    cout << "Enter an index (0-4): ";
    cin >> index;
    
    try {
        if (index < 0) {
            throw invalid_argument("Index cannot be negative");
        }
        if (index >= numbers.size()) {
            throw out_of_range("Index exceeds vector size");
        }
        
        cout << "Value at index " << index << " is: " << numbers[index] << endl;
    }
    catch (invalid_argument& e) {
        cout << "Invalid input: " << e.what() << endl;
    }
    catch (out_of_range& e) {
        cout << "Range error: " << e.what() << endl;
    }
    catch (...) {
        cout << "An unexpected error occurred" << endl;
    }
    
    return 0;
}
```

**Step-by-step Explanation:**
1. A vector is created with five integer values
2. User input is received for the index
3. The try block checks for negative index (throws `invalid_argument`)
4. If index exceeds size, throws `out_of_range`
5. Different catch blocks handle specific exception types
6. The catch-all handler serves as a fallback for any other exceptions

### Example 3: Custom Exception Class

```cpp
#include <iostream>
#include <exception>
using namespace std;

class BankTransactionException : public exception {
private:
    string message;
public:
    BankTransactionException(const string& msg) : message(msg) {}
    const char* what() const noexcept override {
        return message.c_str();
    }
};

class BankAccount {
private:
    double balance;
    double withdrawalLimit;
public:
    BankAccount(double bal, double limit) : balance(bal), withdrawalLimit(limit) {}
    
    void withdraw(double amount) {
        if (amount > balance) {
            throw BankTransactionException("Insufficient funds");
        }
        if (amount > withdrawalLimit) {
            throw BankTransactionException("Amount exceeds withdrawal limit");
        }
        balance -= amount;
        cout << "Withdrawal successful. New balance: " << balance << endl;
    }
};

int main() {
    BankAccount account(5000, 10000);
    
    try {
        account.withdraw(7000);  // Exceeds balance
    }
    catch (const BankTransactionException& e) {
        cout << "Transaction failed: " << e.what() << endl;
    }
    
    return 0;
}
```

**Step-by-step Explanation:**
1. A custom exception class inherits from `std::exception`
2. The `what()` method is overridden to provide custom error messages
3. The BankAccount class uses the custom exception for business logic errors
4. When withdrawal amount exceeds balance, exception is thrown
5. The catch block handles the custom exception type

## Exam Tips

For the University of Delhi semester examinations, keep the following points in mind:

1. **Syntax Accuracy**: Remember the correct syntax is `try { } catch (exception_type) { }`. A common mistake is placing semicolons after catch blocks or forgetting the ellipsis for catch-all handlers.

2. **Order of Catch Blocks**: Always place more specific exception handlers before general ones. The compiler will reject code where a catch-all handler precedes specific handlers.

3. **Exception Propagation**: Understand that uncaught exceptions propagate up the call stack. If not caught anywhere, the program terminates by calling `std::terminate()`.

4. **Throwing by Value, Catching by Reference**: The recommended practice is to throw exceptions by value and catch them by const reference. This prevents object slicing and allows polymorphic behavior.

5. **Standard Exception Classes**: Know the difference between `std::runtime_error` (runtime problems) and `std::logic_error` (program logic errors). Be familiar with common standard exceptions like `std::out_of_range` and `std::invalid_argument`.

6. **Destructors and Exceptions**: Never throw exceptions from destructors. If a destructor must fail, consider using `std::terminate()` or logging the failure, as throwing during stack unwinding leads to program termination.

7. **RAII and Exception Safety**: Understand how RAII (Resource Acquisition Is Initialization) through smart pointers and other RAII objects ensures proper resource cleanup even when exceptions occur.

8. ** noexcept Specifier**: Know that marking functions as `noexcept` allows optimizations and that violations lead to calling `std::terminate()` rather than the unexpected exception.

9. **Difference between throw and rethrow**: `throw;` rethrows the current exception while `throw e;` throws a new copy (which may cause slicing).

10. **Practice Writing Complete Programs**: Examination questions often require complete programs with proper exception handling. Practice writing try-catch blocks within function definitions and understanding how exceptions propagate through function calls.