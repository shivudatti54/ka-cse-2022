# Handling Derived Class Exceptions in C++

## Introduction

Exception handling is a critical paradigm in C++ that provides a structured mechanism for dealing with runtime errors and exceptional conditions. When working with object-oriented programming, exceptions are often implemented as class objects, particularly in the context of derived class hierarchies. Understanding how to properly handle exceptions in class hierarchies is essential for writing robust and maintainable C++ applications.

In C++, the standard library provides a comprehensive exception class hierarchy, and programmers can create custom exception classes by deriving from standard exception types. This topic explores the intricacies of handling exceptions in derived class scenarios, including catching exceptions by reference, virtual function behavior with exceptions, and best practices for designing exception hierarchies. Mastery of these concepts is vital for CSE students as exception handling forms a significant portion of Object-Oriented Programming assessments and practical applications.

## Key Concepts

### Exception Handling Basics

Exception handling in C++ involves three key keywords: `try`, `catch`, and `throw`. The `try` block contains code that might throw an exception, the `catch` block handles the exception, and the `throw` keyword is used to raise an exception. When an exception is thrown, the runtime system searches for the nearest matching catch block to handle it.

```cpp
try {
 // Code that may throw an exception
 throw runtime_error("An error occurred");
}
catch (const runtime_error& e) {
 cout << "Caught: " << e.what() << endl;
}
```

### Exception Class Hierarchy

C++ provides a standard exception hierarchy with `std::exception` as the base class. Common derived classes include `runtime_error`, `logic_error`, `bad_alloc`, and `ios_base::failure`. Understanding this hierarchy allows programmers to catch exceptions at appropriate levels of abstraction.

```
std::exception
├── std::logic_error
│ ├── std::invalid_argument
│ ├── std::domain_error
│ ├── std::length_error
│ └── std::out_of_range
├── std::runtime_error
│ ├── std::range_error
│ ├── std::overflow_error
│ └── std::underflow_error
├── std::bad_alloc
└── std::bad_cast
```

### Creating Custom Exception Classes

Programmers can create custom exception classes by deriving from `std::exception` or its derived classes. This allows for application-specific error handling with custom error messages and additional member variables.

```cpp
class MyCustomException : public std::runtime_error {
private:
 int errorCode;
 string timestamp;
public:
 MyCustomException(const string& msg, int code)
 : std::runtime_error(msg), errorCode(code) {
 // Get current timestamp
 }
 int getErrorCode() const { return errorCode; }
};
```

### Catching Exceptions by Reference

One of the most important principles in C++ exception handling is to catch exceptions by reference rather than by value or by pointer. This avoids object slicing and ensures proper virtual function behavior.

```cpp
// WRONG - Object slicing occurs
try {
 throw DerivedException();
}
catch (BaseException e) { // Slicing! Derived part is lost
 // Only BaseException part is accessible
}

// CORRECT - Catch by reference
try {
 throw DerivedException();
}
catch (BaseException& e) { // Preserves polymorphic behavior
 // Full object is accessible
}

// ALSO CORRECT - Catch by const reference
try {
 throw DerivedException();
}
catch (const BaseException& e) { // Recommended for read-only access
 // Full object accessible
}
```

### Virtual Functions and Exception Handling

When catching base class references, virtual functions called within the catch block exhibit polymorphic behavior. This allows derived class-specific implementations to be invoked.

```cpp
class BaseException : public std::exception {
public:
 virtual const char* what() const noexcept override {
 return "Base Exception";
 }
 virtual string getDetailedInfo() const {
 return "Base class info";
 }
};

class DerivedException : public BaseException {
public:
 virtual const char* what() const noexcept override {
 return "Derived Exception";
 }
 string getDetailedInfo() const override {
 return "Derived class specific info";
 }
};

void handleException() {
 try {
 throw DerivedException();
 }
 catch (BaseException& e) {
 cout << e.what() << endl; // Prints "Derived Exception"
 cout << e.getDetailedInfo() << endl; // Polymorphic call
 }
}
```

### Exception Specifications and noexcept

C++11 introduced `noexcept` specifier to indicate whether a function can throw exceptions. This is important for exception safety and optimization.

```cpp
// Function guaranteed not to throw
void safeFunction() noexcept {
 // No exceptions can escape this function
}

// Function may throw
void riskyFunction() {
 throw std::runtime_error("May fail");
}

// Dynamic exception specification (deprecated but still seen)
void oldStyleFunction() throw(std::runtime_error);
```

### Stack Unwinding and Exception Propagation

When an exception is thrown, the stack is "unwound" - local objects are destroyed in reverse order of construction, and the search for an appropriate handler continues up the call stack.

```cpp
class Resource {
public:
 Resource() { cout << "Resource acquired\n"; }
 ~Resource() { cout << "Resource released\n"; }
};

void func2() {
 Resource r;
 throw std::runtime_error("Error in func2");
}

void func1() {
 func2(); // Exception propagates here
}

int main() {
 try {
 func1();
 }
 catch (const std::exception& e) {
 cout << "Caught: " << e.what() << endl;
 }
 // Output shows destructor called during stack unwinding
}
```

### Rethrowing Exceptions

Exceptions can be rethrown using `throw;` (without an operand) within a catch block. This propagates the original exception to an outer try-catch block.

```cpp
try {
 // Code that might throw
 throw DerivedException();
}
catch (BaseException& e) {
 // Log the exception
 logError(e.what());
 // Rethrow to let upper-level handler deal with it
 throw; // Preserves original exception object
}
```

## Examples

### Example 1: Banking Application Exception Hierarchy

Design an exception hierarchy for a banking application with different account types and specific error conditions.

```cpp
#include <iostream>
#include <stdexcept>
#include <string>
using namespace std;

// Base exception class
class BankingException : public std::runtime_error {
private:
 long accountNumber;
public:
 BankingException(const string& msg, long accNum)
 : std::runtime_error(msg), accountNumber(accNum) {}
 long getAccountNumber() const { return accountNumber; }
};

// Derived exception for insufficient funds
class InsufficientFundsException : public BankingException {
private:
 double currentBalance;
 double requestedAmount;
public:
 InsufficientFundsException(long accNum, double balance, double requested)
 : BankingException("Insufficient funds", accNum),
 currentBalance(balance), requestedAmount(requested) {}

 double getCurrentBalance() const { return currentBalance; }
 double getRequestedAmount() const { return requestedAmount; }
 double getDeficit() const { return requestedAmount - currentBalance; }
};

// Derived exception for invalid transactions
class InvalidTransactionException : public BankingException {
private:
 string transactionType;
public:
 InvalidTransactionException(long accNum, const string& transType)
 : BankingException("Invalid transaction", accNum),
 transactionType(transType) {}
 string getTransactionType() const { return transactionType; }
};

// Account class demonstrating exception handling
class Account {
private:
 long accountNumber;
 double balance;
 string accountType;
public:
 Account(long accNum, double initialBalance, const string& type)
 : accountNumber(accNum), balance(initialBalance), accountType(type) {}

 void withdraw(double amount) {
 if (amount <= 0) {
 throw InvalidTransactionException(accountNumber, "Negative amount");
 }
 if (amount > balance) {
 throw InsufficientFundsException(accountNumber, balance, amount);
 }
 balance -= amount;
 cout << "Withdrawal successful. New balance: " << balance << endl;
 }

 double getBalance() const { return balance; }
};

int main() {
 Account savings(1001, 5000, "Savings");

 try {
 cout << "Attempting to withdraw 10000..." << endl;
 savings.withdraw(10000);
 }
 catch (const InsufficientFundsException& e) {
 cout << "ERROR: " << e.what() << endl;
 cout << "Account: " << e.getAccountNumber() << endl;
 cout << "Current Balance: $" << e.getCurrentBalance() << endl;
 cout << "Requested: $" << e.getRequestedAmount() << endl;
 cout << "Deficit: $" << e.getDeficit() << endl;
 }
 catch (const BankingException& e) {
 cout << "Banking Error: " << e.what() << endl;
 cout << "Account: " << e.getAccountNumber() << endl;
 }

 return 0;
}
```

### Example 2: Polymorphic Exception Handling in File Processing

This example demonstrates handling different file-related exceptions through a common base class handler.

```cpp
#include <iostream>
#include <fstream>
#include <exception>
#include <string>
using namespace std;

// Custom exception hierarchy for file operations
class FileException : public std::exception {
protected:
 string filename;
 string operation;
public:
 FileException(const string& file, const string& op)
 : filename(file), operation(op) {}
 virtual const char* what() const noexcept override {
 return "File operation failed";
 }
 virtual void printDetails() const {
 cout << "File: " << filename << ", Operation: " << operation << endl;
 }
 virtual ~FileException() {}
};

class FileNotFoundException : public FileException {
public:
 FileNotFoundException(const string& file)
 : FileException(file, "read") {}
 const char* what() const noexcept override {
 return "File not found";
 }
};

class PermissionDeniedException : public FileException {
public:
 PermissionDeniedException(const string& file)
 : FileException(file, "read") {}
 const char* what() const noexcept override {
 return "Permission denied";
 }
};

class DiskFullException : public FileException {
public:
 DiskFullException(const string& file)
 : FileException(file, "write") {}
 const char* what() const noexcept override {
 return "Disk full";
 }
};

// File processor demonstrating polymorphic exception handling
class FileProcessor {
public:
 void processFile(const string& filename, bool simulateError = false) {
 try {
 if (simulateError) {
 throw PermissionDeniedException(filename);
 }

 ifstream file(filename);
 if (!file.is_open()) {
 throw FileNotFoundException(filename);
 }

 // Process file contents
 cout << "Processing file: " << filename << endl;
 file.close();
 }
 catch (FileException& e) {
 // Polymorphic catch - handles all derived exceptions
 e.printDetails();
 throw; // Rethrow after logging
 }
 }
};

int main() {
 FileProcessor processor;

 try {
 processor.processFile("data.txt", true);
 }
 catch (const FileNotFoundException& e) {
 cout << "Handle missing file: " << e.what() << endl;
 }
 catch (const PermissionDeniedException& e) {
 cout << "Handle permission issue: " << e.what() << endl;
 }
 catch (const FileException& e) {
 cout << "General file error: " << e.what() << endl;
 }
 catch (const exception& e) {
 cout << "Unexpected error: " << e.what() << endl;
 }

 return 0;
}
```

### Example 3: Multi-level Exception Handling with Class Hierarchy

This comprehensive example demonstrates exception propagation through multiple levels of function calls.

```cpp
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;

// Exception class hierarchy
class MathException : public std::runtime_error {
public:
 MathException(const string& msg) : std::runtime_error(msg) {}
};

class DivisionByZeroException : public MathException {
private:
 double divisor;
public:
 DivisionByZeroException(double div)
 : MathException("Division by zero attempted"), divisor(div) {}
 double getDivisor() const { return divisor; }
};

class OverflowException : public MathException {
private:
 double value;
public:
 OverflowException(double val)
 : MathException("Arithmetic overflow"), value(val) {}
 double getValue() const { return value; }
};

// Calculator class
class Calculator {
public:
 double divide(double a, double b) {
 if (b == 0) {
 throw DivisionByZeroException(b);
 }
 return a / b;
 }

 double multiply(double a, double b) {
 // Check for potential overflow
 if (a != 0 && b > numeric_limits<double>::max() / abs(a)) {
 throw OverflowException(a * b);
 }
 return a * b;
 }
};

// Business logic layer
class BusinessLogic {
 Calculator calc;
public:
 double calculateAverage(double a, double b) {
 try {
 double sum = calc.multiply(a, b);
 return calc.divide(sum, 2.0);
 }
 catch (const MathException& e) {
 // Log and rethrow
 cout << "Math error in BusinessLogic: " << e.what() << endl;
 throw;
 }
 }
};

// Presentation layer
class UI {
 BusinessLogic logic;
public:
 void displayResult(double a, double b) {
 try {
 double result = logic.calculateAverage(a, b);
 cout << "Average of " << a << " and " << b
 << " is " << result << endl;
 }
 catch (const DivisionByZeroException& e) {
 cout << "Caught at UI level: " << e.what() << endl;
 cout << "Attempted to divide by: " << e.getDivisor() << endl;
 }
 catch (const OverflowException& e) {
 cout << "Caught at UI level: Overflow with value "
 << e.getValue() << endl;
 }
 catch (const MathException& e) {
 cout << "General math error: " << e.what() << endl;
 }
 catch (const exception& e) {
 cout << "Unexpected error: " << e.what() << endl;
 }
 }
};

int main() {
 UI ui;

 cout << "Test 1: Normal operation" << endl;
 ui.displayResult(10.0, 20.0);

 cout << "\nTest 2: Division by zero" << endl;
 ui.displayResult(10.0, 0.0);

 cout << "\nTest 3: Overflow" << endl;
 ui.displayResult(1e308, 1e308);

 return 0;
}
```

## Exam Tips

1. **Always catch by reference**: Remember to use `catch(const BaseClass& e)` instead of catching by value or pointer to avoid object slicing and preserve polymorphism.

2. **Order of catch blocks matters**: More specific exception types must be caught before more general ones. The compiler will give a warning or error if unreachable catch blocks exist.

3. **Virtual function behavior**: When catching base class references, virtual functions like `what()` will call the derived class implementation due to polymorphism.

4. **Use what() method**: The `std::exception` class provides the virtual `what()` method for getting the exception message string.

5. **Rethrow correctly**: Use `throw;` without an operand to rethrow the current exception. Using `throw e;` would throw a copy of the caught exception, losing the original type information.

6. **Standard exception hierarchy**: Know the difference between `logic_error` (programmer errors) and `runtime_error` (external conditions).

7. **Noexcept functions**: Functions marked as `noexcept` will call `std::terminate()` if an exception escapes them. This is important for understanding program behavior.

8. **Destructor exceptions**: Never throw exceptions from destructors. If a destructor must fail, consider logging the error or using `std::terminate()`.
