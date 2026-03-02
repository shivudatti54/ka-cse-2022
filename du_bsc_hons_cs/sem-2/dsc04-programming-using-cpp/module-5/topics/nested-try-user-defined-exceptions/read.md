# Nested Try Blocks and User-Defined Exceptions in C++

## Introduction

Exception handling is a powerful mechanism in C++ that separates error detection from error handling, making programs more robust and maintainable. While basic try-catch blocks form the foundation of exception handling, real-world scenarios often demand more sophisticated approaches. **Nested try blocks** allow for hierarchical error handling where exceptions can be caught at multiple levels, providing finer control over error recovery. Simultaneously, **user-defined exceptions** enable programmers to create application-specific error types that go beyond C++'s built-in exception classes.

In the context of University of Delhi's B.Sc. (Hons.) Computer Science program, understanding nested try blocks and custom exceptions is essential for building industrial-grade C++ applications. These concepts are frequently tested in semester examinations, with questions often requiring students to trace exception propagation through nested blocks or design custom exception classes for specific scenarios. This topic builds upon basic exception handling concepts and prepares students for advanced C++ programming patterns used in real software development.

## Key Concepts

### 1. Nested Try Blocks

A **nested try block** occurs when one try-catch statement is placed inside another try block. This structure becomes necessary when different levels of error handling are required—perhaps different catch blocks at different levels need to handle different types of exceptions.

**Syntax Structure:**
```cpp
try {
    // Outer try block
    try {
        // Inner try block
    }
    catch (ExceptionType1 e) {
        // Handle at inner level
    }
}
catch (ExceptionType2 e) {
    // Handle at outer level
}
```

**Key Characteristics:**
- When an exception is thrown in the inner try block, the catch blocks within that inner block are checked first
- If no matching catch block exists in the inner try, the exception propagates to the outer try's catch blocks
- This allows for graceful degradation—handle what you can locally, escalate what you cannot

### 2. Rethrowing Exceptions

Sometimes, after catching an exception in an inner block, you may want to propagate it to an outer handler. This is achieved using the `throw;` statement without any operand.

**Important Distinction:**
- `throw;` — Rethrows the current exception object to an outer catch block
- `throw e;` — Creates a new exception from the caught object e (slicing can occur)

```cpp
try {
    try {
        throw runtime_error("Original error");
    }
    catch (const runtime_error& e) {
        cout << "Caught: " << e.what() << endl;
        throw; // Rethrows the same exception
    }
}
catch (const exception& e) {
    cout << "Outer catch: " << e.what() << endl;
}
```

### 3. Exception Propagation Through Nested Blocks

When an exception is thrown:
1. The runtime searches for a matching catch block in the current try block
2. If found, the exception is handled and propagation stops
3. If not found, local destructors are called (stack unwinding) and the exception propagates outward
4. This continues until either a catch block handles it or the program terminates

```cpp
#include <iostream>
using namespace std;

void function3() {
    throw runtime_error("Error in function3");
}

void function2() {
    try {
        function3();
    }
    catch (runtime_error& e) {
        cout << "Caught in function2: " << e.what() << endl;
        throw; // Rethrows to outer handler
    }
}

void function1() {
    try {
        function2();
    }
    catch (runtime_error& e) {
        cout << "Caught in function1: " << e.what() << endl;
    }
}
```

### 4. User-Defined Exceptions

C++ allows creation of custom exception classes by inheriting from `std::exception` (preferably) or any other exception class. This enables application-specific error handling.

**Why Create User-Defined Exceptions?**
- Semantic clarity: Custom exception names convey meaning
- Rich error information: Can include additional data members
- Type safety: Different exception types for different error conditions
- Hierarchical organization: Can create exception hierarchies

**Basic User-Defined Exception:**
```cpp
#include <exception>
#include <string>

class MyException : public exception {
private:
    string message;
public:
    MyException(const string& msg) : message(msg) {}
    const char* what() const noexcept override {
        return message.c_str();
    }
};
```

### 5. Standard Exception Hierarchy

Understanding the standard exception hierarchy helps in designing effective custom exceptions:

```
exception (std)
├── logic_error
│   ├── invalid_argument
│   ├── length_error
│   ├── out_of_range
├── runtime_error
│   ├── range_error
│   ├── overflow_error
│   ├── underflow_error
├── bad_alloc
├── bad_cast
├── ios_base::failure
```

### 6. Exception Specifications (Deprecated)

C++98 introduced exception specifications (throw lists), but they were deprecated in C++11 and removed in C++17. Modern C++ uses `noexcept` instead for specifying functions that do not throw exceptions.

```cpp
void safeFunction() noexcept {
    // This function promises not to throw
}
```

## Examples

### Example 1: Tracing Nested Try-Catch Execution

**Problem:** What is the output of the following program?

```cpp
#include <iostream>
using namespace std;

int main() {
    try {
        cout << "Outer try start\n";
        try {
            cout << "Inner try start\n";
            throw 20;
        }
        catch (int e) {
            cout << "Inner catch: " << e << "\n";
            throw;
        }
        catch (double e) {
            cout << "Inner catch double: " << e << "\n";
        }
        cout << "After inner try-catch\n";
    }
    catch (int e) {
        cout << "Outer catch: " << e << "\n";
    }
    cout << "End of program\n";
    return 0;
}
```

**Solution:**

**Step-by-step execution:**
1. "Outer try start" is printed
2. "Inner try start" is printed
3. `throw 20;` throws an integer exception
4. First catch block for `int e` in inner try catches it
5. "Inner catch: 20" is printed
6. `throw;` rethrows the exception to outer handler
7. Inner try-catch block ends (subsequent statements in inner try not executed)
8. Outer catch block catches the rethrown exception
9. "Outer catch: 20" is printed
10. "End of program" is printed

**Output:**
```
Outer try start
Inner try start
Inner catch: 20
Outer catch: 20
End of program
```

### Example 2: Banking Application with User-Defined Exceptions

**Problem:** Design a banking system with custom exceptions for invalid transactions.

```cpp
#include <iostream>
#include <string>
#include <exception>
using namespace std;

// Custom exception for insufficient balance
class InsufficientFundsException : public exception {
private:
    double balance;
    double requested;
public:
    InsufficientFundsException(double bal, double req) 
        : balance(bal), requested(req) {}
    
    const char* what() const noexcept override {
        return "Insufficient funds for this transaction";
    }
    
    double getBalance() const { return balance; }
    double getRequested() const { return requested; }
};

// Custom exception for invalid account
class InvalidAccountException : public exception {
private:
    string accountId;
public:
    InvalidAccountException(const string& id) : accountId(id) {}
    
    const char* what() const noexcept override {
        return "Invalid account ID";
    }
    
    const string& getAccountId() const { return accountId; }
};

class BankAccount {
private:
    string accountId;
    double balance;
public:
    BankAccount(string id, double bal) : accountId(id), balance(bal) {}
    
    void withdraw(double amount) {
        if (balance < amount) {
            throw InsufficientFundsException(balance, amount);
        }
        balance -= amount;
        cout << "Withdrawal successful. New balance: " << balance << endl;
    }
    
    void deposit(double amount) {
        if (amount <= 0) {
            throw invalid_argument("Deposit amount must be positive");
        }
        balance += amount;
        cout << "Deposit successful. New balance: " << balance << endl;
    }
};

int main() {
    BankAccount account("ACC123", 5000);
    
    try {
        account.deposit(1000);  // Valid
        account.withdraw(7000); // Should throw - exceeds balance
    }
    catch (const InsufficientFundsException& e) {
        cout << "Error: " << e.what() << endl;
        cout << "  Balance: " << e.getBalance() << endl;
        cout << "  Requested: " << e.getRequested() << endl;
    }
    catch (const invalid_argument& e) {
        cout << "Invalid argument: " << e.what() << endl;
    }
    
    return 0;
}
```

**Output:**
```
Deposit successful. New balance: 6000
Error: Insufficient funds for this transaction
  Balance: 6000
  Requested: 7000
```

### Example 3: Multi-Level Exception Handling

**Problem:** Create a program demonstrating exception handling at three different levels.

```cpp
#include <iostream>
#include <stdexcept>
using namespace std;

class Level3Exception : public runtime_error {
public:
    Level3Exception() : runtime_error("Level 3 Error") {}
};

class Level2Exception : public runtime_error {
public:
    Level2Exception() : runtime_error("Level 2 Error") {}
};

void level3() {
    throw Level3Exception();
}

void level2() {
    try {
        level3();
    }
    catch (Level3Exception& e) {
        cout << "Caught at Level 2: " << e.what() << endl;
        throw Level2Exception(); // Convert to different exception
    }
}

void level1() {
    try {
        level2();
    }
    catch (Level2Exception& e) {
        cout << "Caught at Level 1: " << e.what() << endl;
    }
    catch (Level3Exception& e) {
        cout << "Caught Level3 at Level 1: " << e.what() << endl;
    }
}

int main() {
    try {
        level1();
    }
    catch (exception& e) {
        cout << "Caught at main: " << e.what() << endl;
    }
    cout << "Program continues normally\n";
    return 0;
}
```

**Output:**
```
Caught at Level 2: Level 3 Error
Caught at Level 1: Level 2 Error
Program continues normally
```

## Exam Tips

1. **Exception Propagation Rule**: Remember that when an exception is thrown, control transfers to the nearest enclosing catch block that can handle that exception type. If no catch block matches, `std::terminate()` is called.

2. **Catch Block Order Matters**: When catching multiple exception types, catch more specific exceptions first. Base class catch blocks should come last, otherwise, derived class exceptions will be caught by the base class handler.

3. **Always Catch by Reference**: Use `catch (const exception& e)` instead of catching by value to avoid object slicing and ensure proper polymorphic behavior.

4. **Rethrow Correctly**: Use `throw;` (without operand) to rethrow the current exception. Using `throw e;` creates a new exception and may cause slicing.

5. **User-Defined Exception Best Practice**: Inherit from `std::exception` and override the `what()` virtual function to provide meaningful error messages.

6. **Noexcept Functions**: Remember that if a function declared `noexcept` throws an exception, `std::terminate()` is called immediately.

7. **Nested Try Execution Flow**: Practice tracing programs with nested try blocks—exception propagates outward until caught, and intermediate code after the throw point is never executed.

8. **Stack Unwinding**: Understand that when an exception propagates, local objects are destroyed in reverse order of construction (stack unwinding), calling their destructors.