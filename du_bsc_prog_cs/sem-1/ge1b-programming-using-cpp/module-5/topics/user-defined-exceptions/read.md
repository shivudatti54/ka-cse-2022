# User Defined Exceptions in C++

## Comprehensive Study Material for BSc Physical Science (CS) - Delhi University NEP 2024

---

## 1. Introduction

Exception handling is a fundamental mechanism in C++ that allows programs to respond to extraordinary situations gracefully. While C++ provides a rich set of standard exception classes through the `<stdexcept>` header, real-world applications often require custom exception types that accurately represent domain-specific error conditions.

**User-defined exceptions** (also called custom exceptions) are exception classes created by programmers to represent application-specific error conditions that are not adequately covered by standard exceptions. In the context of the Delhi University BSc Physical Science (CS) curriculum under NEP 2024, understanding user-defined exceptions is essential for building robust, maintainable C++ applications.

### Real-World Relevance

Consider a banking application where you need to handle scenarios like:
- Insufficient funds for withdrawal
- Invalid account number format
- Transaction limit exceeded
- Account locked due to multiple failed attempts

None of these scenarios fit neatly into standard exceptions like `std::runtime_error` or `std::logic_error`. User-defined exceptions allow you to create meaningful error types that clearly communicate what went wrong, making debugging and error handling significantly more effective.

---

## 2. Why User-Defined Exceptions?

### Limitations of Standard Exceptions

1. **Generic Nature**: Standard exceptions like `std::exception`, `std::runtime_error`, and `std::logic_error` are too generic for specific applications.

2. **Lack of Context**: Standard exceptions don't carry application-specific data that might be helpful for error handling.

3. **Poor Debugging**: When an exception is caught, you often need specific information about what triggered it.

### Benefits of User-Defined Exceptions

- **Type Safety**: Each exception type represents a specific category of error
- **Rich Error Information**: Can include additional members to store error context
- **Hierarchical Organization**: Can be organized in inheritance hierarchies
- **Better Error Messages**: Custom `what()` messages provide meaningful feedback
- **Facilitates Unit Testing**: Specific exception types make testing error conditions easier

---

## 3. Basic Syntax and Structure

A user-defined exception is simply a class that inherits from the standard `std::exception` class (typically from `std::runtime_error` or `std::logic_error`). The key requirement is that the class must be throwable and should override the `what()` virtual function.

### Fundamental Rules

1. User-defined exceptions should derive from `std::exception` (directly or indirectly)
2. They should be thrown by value and caught by reference
3. The `what()` function must return a descriptive C-style string

### Class Hierarchy Overview

```
std::exception
    ├── std::logic_error
    │     ├── std::invalid_argument
    │     ├── std::domain_error
    │     ├── std::length_error
    │     └── std::out_of_range
    └── std::runtime_error
          ├── std::range_error
          ├── std::overflow_error
          └── std::underflow_error
```

---

## 4. Creating Custom Exception Classes

### Simple User-Defined Exception

```cpp
#include <iostream>
#include <exception>
#include <string>

// Simple user-defined exception
class NegativeValueException : public std::runtime_error {
public:
    NegativeValueException() 
        : std::runtime_error("Negative value encountered") {}
    
    explicit NegativeValueException(const std::string& message)
        : std::runtime_error(message) {}
};

int main() {
    try {
        int value = -5;
        if (value < 0) {
            throw NegativeValueException("Value cannot be negative");
        }
    }
    catch (const std::exception& e) {
        std::cout << "Exception caught: " << e.what() << std::endl;
    }
    return 0;
}
```

### Rich User-Defined Exception with Additional Data

```cpp
#include <iostream>
#include <exception>
#include <string>
#include <sstream>

class BankTransactionException : public std::runtime_error {
private:
    double attemptedAmount;
    double availableBalance;
    std::string accountId;

public:
    BankTransactionException(const std::string& accId, 
                           double balance, 
                           double amount,
                           const std::string& message)
        : std::runtime_error(message),
          attemptedAmount(amount),
          availableBalance(balance),
          accountId(accId) {}

    // Getter functions for detailed error information
    double getAttemptedAmount() const { return attemptedAmount; }
    double getAvailableBalance() const { return availableBalance; }
    std::string getAccountId() const { return accountId; }

    // Override what() to provide comprehensive error information
    const char* what() const noexcept override {
        std::ostringstream oss;
        oss << std::runtime_error::what() 
            << " | Account: " << accountId
            << " | Attempted: " << attemptedAmount
            << " | Available: " << availableBalance;
        
        // Note: In practice, you'd store this string
        // For simplicity, returning base message
        return std::runtime_error::what();
    }
};
```

---

## 5. Throwing and Catching User-Defined Exceptions

### Basic Throwing and Catching

```cpp
#include <iostream>
#include <stdexcept>
#include <string>

class InsufficientFundsException : public std::runtime_error {
private:
    double balance;
    double requested;

public:
    InsufficientFundsException(double bal, double req)
        : std::runtime_error("Insufficient funds"),
          balance(bal),
          requested(req) {}

    double getBalance() const { return balance; }
    double getRequested() const { return requested; }
};

class BankAccount {
private:
    std::string accountNumber;
    double balance;

public:
    BankAccount(const std::string& accNo, double initialBalance)
        : accountNumber(accNo), balance(initialBalance) {}

    void withdraw(double amount) {
        if (amount > balance) {
            throw InsufficientFundsException(balance, amount);
        }
        balance -= amount;
        std::cout << "Withdrawal successful. New balance: " << balance << std::endl;
    }
};

int main() {
    BankAccount account("ACC123", 1000.0);

    try {
        std::cout << "Attempting to withdraw 1500..." << std::endl;
        account.withdraw(1500.0);
    }
    catch (const InsufficientFundsException& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        std::cerr << "Requested: " << e.getRequested() 
                  << ", Available: " << e.getBalance() << std::endl;
    }

    return 0;
}
```

### Catching Multiple Exception Types

```cpp
#include <iostream>
#include <stdexcept>
#include <string>

// Custom exception hierarchy
class MathException : public std::runtime_error {
public:
    MathException(const std::string& msg) : std::runtime_error(msg) {}
};

class DivisionByZeroException : public MathException {
public:
    DivisionByZeroException() : MathException("Cannot divide by zero") {}
};

class OverflowException : public MathException {
public:
    OverflowException() : MathException("Math overflow occurred") {}
};

int divide(int a, int b) {
    if (b == 0) {
        throw DivisionByZeroException();
    }
    if (a > INT_MAX / b) {
        throw OverflowException();
    }
    return a / b;
}

int main() {
    try {
        int result = divide(100, 0);
    }
    catch (const DivisionByZeroException& e) {
        std::cerr << "Division Error: " << e.what() << std::endl;
    }
    catch (const OverflowException& e) {
        std::cerr << "Overflow Error: " << e.what() << std::endl;
    }
    catch (const MathException& e) {
        std::cerr << "Math Error: " << e.what() << std::endl;
    }
    catch (const std::exception& e) {
        std::cerr << "Unexpected Error: " << e.what() << std::endl;
    }

    return 0;
}
```

---

## 6. Practical Example: Student Record Management System

This comprehensive example demonstrates user-defined exceptions in a student record management context:

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <stdexcept>
#include <sstream>

// ============================================
// USER-DEFINED EXCEPTION CLASSES
// ============================================

// Base exception for student management system
class StudentManagementException : public std::runtime_error {
protected:
    int errorCode;
public:
    StudentManagementException(const std::string& msg, int code = -1)
        : std::runtime_error(msg), errorCode(code) {}
    int getErrorCode() const { return errorCode; }
};

// Exception for invalid roll number
class InvalidRollNumberException : public StudentManagementException {
private:
    std::string attemptedRollNumber;
public:
    InvalidRollNumberException(const std::string& roll)
        : StudentManagementException("Invalid roll number format", 101),
          attemptedRollNumber(roll) {}
    
    const char* what() const noexcept override {
        std::ostringstream oss;
        oss << "Error 101: Invalid roll number '" << attemptedRollNumber 
            << "'. Roll number must be positive integer.";
        return oss.str().c_str();
    }
};

// Exception for invalid marks
class InvalidMarksException : public StudentManagementException {
private:
    double invalidMarks;
    double maxMarks;
public:
    InvalidMarksException(double marks, double max = 100.0)
        : StudentManagementException("Marks out of valid range", 102),
          invalidMarks(marks), maxMarks(max) {}
    
    const char* what() const noexcept override {
        std::ostringstream oss;
        oss << "Error 102: Invalid marks " << invalidMarks 
            << ". Must be between 0 and " << maxMarks;
        return oss.str().c_str();
    }
};

// Exception for duplicate student
class DuplicateStudentException : public StudentManagementException {
private:
    std::string rollNumber;
public:
    DuplicateStudentException(const std::string& roll)
        : StudentManagementException("Student already exists", 103),
          rollNumber(roll) {}
    
    const char* what() const noexcept override {
        std::ostringstream oss;
        oss << "Error 103: Student with roll number '" << rollNumber 
            << "' already exists in the system.";
        return oss.str().c_str();
    }
};

// Exception for student not found
class StudentNotFoundException : public StudentManagementException {
private:
    std::string rollNumber;
public:
    StudentNotFoundException(const std::string& roll)
        : StudentManagementException("Student not found", 104),
          rollNumber(roll) {}
    
    const char* what() const noexcept override {
        std::ostringstream oss;
        oss << "Error 104: No student found with roll number '" << rollNumber << "'";
        return oss.str().c_str();
    }
};

// ============================================
// STUDENT CLASS
// ============================================

class Student {
private:
    int rollNumber;
    std::string name;
    double marks;
    static const double MAX_MARKS = 100.0;

public:
    Student(int roll, const std::string& studentName, double studentMarks)
        : name(studentName) {
        
        // Validate roll number
        if (roll <= 0) {
            throw InvalidRollNumberException(std::to_string(roll));
        }
        rollNumber = roll;

        // Validate marks
        if (studentMarks < 0 || studentMarks > MAX_MARKS) {
            throw InvalidMarksException(studentMarks, MAX_MARKS);
        }
        marks = studentMarks;
    }

    int getRollNumber() const { return rollNumber; }
    std::string getName() const { return name; }
    double getMarks() const { return marks; }

    void display() const {
        std::cout << "Roll No: " << rollNumber 
                  << ", Name: " << name 
                  << ", Marks: " << marks << std::endl;
    }
};

// ============================================
// STUDENT MANAGER CLASS
// ============================================

class StudentManager {
private:
    std::vector<Student> students;

public:
    void addStudent(const Student& student) {
        // Check for duplicate
        for (const auto& s : students) {
            if (s.getRollNumber() == student.getRollNumber()) {
                throw DuplicateStudentException(std::to_string(student.getRollNumber()));
            }
        }
        students.push_back(student);
        std::cout << "Student added successfully." << std::endl;
    }

    Student& findStudent(int rollNumber) {
        for (auto& s : students) {
            if (s.getRollNumber() == rollNumber) {
                return s;
            }
        }
        throw StudentNotFoundException(std::to_string(rollNumber));
    }

    void displayAll() const {
        std::cout << "\n=== All Students ===" << std::endl;
        for (const auto& s : students) {
            s.display();
        }
    }
};

// ============================================
// MAIN FUNCTION - DEMONSTRATION
// ============================================

int main() {
    StudentManager manager;

    std::cout << "=== Student Management System Demo ===" << std::endl;

    // Test Case 1: Valid student creation
    try {
        Student s1(101, "Amit Kumar", 85.5);
        std::cout << "\nTest 1: Creating valid student..." << std::endl;
        manager.addStudent(s1);
    }
    catch (const StudentManagementException& e) {
        std::cerr << e.what() << std::endl;
    }

    // Test Case 2: Invalid roll number
    try {
        Student s2(-5, "Invalid Student", 90.0);
    }
    catch (const InvalidRollNumberException& e) {
        std::cerr << "\nTest 2 (Expected): " << e.what() << std::endl;
    }

    // Test Case 3: Invalid marks
    try {
        Student s3(102, "Rahul Sharma", 150.0);
    }
    catch (const InvalidMarksException& e) {
        std::cerr << "\nTest 3 (Expected): " << e.what() << std::endl;
    }

    // Test Case 4: Duplicate student
    try {
        Student s4(101, "Duplicate Entry", 75.0); // Same roll as s1
        manager.addStudent(s4);
    }
    catch (const DuplicateStudentException& e) {
        std::cerr << "\nTest 4 (Expected): " << e.what() << std::endl;
    }

    // Test Case 5: Student not found
    try {
        Student& s = manager.findStudent(999);
        s.display();
    }
    catch (const StudentNotFoundException& e) {
        std::cerr << "\nTest 5 (Expected): " << e.what() << std::endl;
    }

    // Test Case 6: Adding another valid student
    try {
        Student s5(102, "Priya Singh", 92.0);
        manager.addStudent(s5);
        Student s6(103, "Vikram Patel", 78.5);
        manager.addStudent(s6);
    }
    catch (const StudentManagementException& e) {
        std::cerr << e.what() << std::endl;
    }

    // Display all students
    manager.displayAll();

    std::cout << "\n=== Demo Complete ===" << std::endl;

    return 0;
}
```

---

## 7. Exception Safety Concepts

Exception safety is a crucial concept that ensures your program remains in a valid state when an exception occurs. According to the Delhi University syllabus, you should understand the following levels:

### Levels of Exception Safety

1. **No Guarantee (No Safety)**: If an exception is thrown, the program may be in an undefined state. This is unacceptable for robust code.

2. **Basic Guarantee**: If an exception is thrown, the program is in a valid state. No resources are leaked, and invariants are maintained.

3. **Strong Guarantee**: If an exception is thrown, the program's state remains unchanged. This is also known as "commit or rollback" semantics.

4. **No-Throw Guarantee**: The operation cannot throw an exception and will always succeed.

### Best Practices for Exception Safety

```cpp
#include <memory> // for std::unique_ptr

class ExceptionSafeClass {
private:
    std::unique_ptr<int> data;  // Smart pointer for automatic cleanup

public:
    ExceptionSafeClass() : data(std::make_unique<int>(0)) {}

    void safeOperation() {
        // Use smart pointers to prevent resource leaks
        auto temp = std::make_unique<int>(42);
        
        // If this line throws, unique_ptr temp will clean itself up
        // Original data remains unchanged (Strong Guarantee)
        data = std::move(temp);
    }

    // noexcept ensures this function won't throw
    void criticalOperation() noexcept {
        // Perform operations that cannot fail
    }
};
```

---

## 8. Best Practices for User-Defined Exceptions

### Do's

1. **Inherit from std::exception**: Always derive your exceptions from the standard exception hierarchy
2. **Override what()**: Provide meaningful error messages
3. **Use const correctness**: Make member functions const where applicable
4. **Throw by value, catch by reference**: Always `throw MyException()` and `catch (const MyException& e)`
5. **Use noexcept sparingly**: Only mark functions noexcept when they truly cannot throw

### Don'ts

1. **Don't throw in destructors**: This can cause program termination
2. **Don't catch by value**: This causes object slicing
3. **Don't use exceptions for flow control**: Use exceptions only for exceptional conditions
4. **Don't swallow exceptions**: Always handle or re-throw caught exceptions

---

## 9. Common Pitfalls

### Object Slicing

```cpp
// WRONG - Object slicing occurs
try {
    throw DerivedException();
}
catch (BaseException e) {  // Caught by value - WRONG!
    // Only base class part is copied
}

// CORRECT - Caught by reference
try {
    throw DerivedException();
}
catch (const BaseException& e) {  // Caught by reference - CORRECT!
    // Full object is accessible
}
```

### Exception Specification Issues

In modern C++ (C++11 and later), exception specifications are deprecated. Instead, use `noexcept` when appropriate:

```cpp
// Old style (deprecated)
void oldStyle() throw(std::runtime_error);

// Modern C++ style
void modernStyle() noexcept;  // Function promises not to throw
void normalFunction();        // May throw
```

---

## 10. Delhi University Syllabus Context

This topic aligns with the following components of the BSc Physical Science (CS) curriculum under NEP 2024:

- **Unit III: Object-Oriented Programming in C++** - Exception handling as a key OOP concept
- **Practical Component** - Implementation of custom exception classes
- **Error Handling** - Understanding of robust error management in software development

The study of user-defined exceptions prepares students for:
- Building industrial-strength C++ applications
- Understanding exception safety in real-world codebases
- Working with modern C++ libraries and frameworks

---

## 11. Key Takeaways

1. **User-defined exceptions** are custom exception classes that represent application-specific error conditions

2. They should **inherit from std::exception** (preferably through std::runtime_error or std::logic_error)

3. The **what() virtual function** must be overridden to provide meaningful error messages

4. **Throw by value, catch by reference** to avoid object slicing

5. User-defined exceptions can carry **additional context** (error codes, values, etc.)

6. **Exception hierarchies** allow handling related exceptions at different levels

7. **Exception safety** ensures programs remain in valid states when exceptions occur

8. Follow **best practices**: use smart pointers, avoid throwing in destructors, and handle all exceptions appropriately

---

## 12. Assessment Questions

### Multiple Choice Questions

**Question 1:** Which C++ standard exception class is most commonly used as a base for user-defined exceptions in practice?

- A) std::exception
- B) std::runtime_error ✓ (Correct: Most practical applications use runtime_error as it represents errors detectable at runtime)
- C) std::logic_error
- D) std::bad_alloc

**Question 2:** What is the correct way to catch a user-defined exception?

```cpp
try {
    throw MyException("Error");
}
catch (/* fill in */) { }
```

- A) `catch (MyException e)`
- B) `catch (MyException* e)`
- C) `catch (const MyException& e)` ✓
- D) `catch (MyException& e, const char* msg)`

**Question 3:** Which function must be overridden in a user-defined exception class?

- A) `what()` ✓
- B) `throw()`
- C) `catch()`
- D) `except()`

**Question 4:** What does the `noexcept` specifier indicate?

- A) The function can throw any exception
- B) The function will throw std::bad_exception if an error occurs
- C) The function promises not to throw exceptions ✓
- D) The function catches all exceptions

**Question 5:** What is "object slicing" in the context of exception handling?

- A) Memory allocation failure
- B) Losing derived class data when catching by value ✓
- C) Cutting off exception messages
- D) Improper exception hierarchy design

**Question 6:** Which level of exception guarantee ensures that if an operation fails, the program state remains unchanged?

- A) Basic guarantee
- B) Strong guarantee ✓
- C) No-throw guarantee
- D) No guarantee

**Question 7:** What is the primary benefit of user-defined exceptions over standard exceptions?

- A) They are faster
- B) They can carry application-specific error information ✓
- C) They are required by C++ standard
- D) They work without try-catch blocks

**Question 8:** In a class hierarchy of exceptions, which catch block should be placed first?

- A) Base exception class
- B) Derived exception classes ✓
- C) std::exception
- D) It doesn't matter

**Question 9:** Which header file contains std::runtime_error?

- A) \<exception\>
- B) \<stdexcept\> ✓
- C) \<runtime\>
- D) \<error\>

**Question 10:** What happens if an exception is thrown from a destructor?

- A) It is automatically caught
- B) It causes std::terminate to be called ✓
- C) It is ignored
- D) It is converted to a warning

### Fill in the Blanks

1. A user-defined exception should override the virtual function **`what()`** to provide error descriptions.

2. The practice of throwing exceptions by value and catching by reference prevents **object slicing**.

3. When exceptions are organized in a hierarchy, more **specific** (derived) exceptions should be caught before more **general** (base) exceptions.

4. The **`noexcept`** specifier in C++ indicates that a function will not throw exceptions.

5. A **strong exception guarantee** ensures that if an operation fails, the program's state is unchanged.

### True/False Questions

1. **True or False:** User-defined exceptions must always inherit directly from std::exception.
   - **False** - They can inherit from any class in the exception hierarchy

2. **True or False:** Catching exceptions by value is always the recommended approach.
   - **False** - Catching by reference is recommended to avoid object slicing

3. **True or False:** Using exceptions for normal program flow control is a good practice.
   - **False** - Exceptions should only be used for exceptional conditions

4. **True or False:** The what() function should return a C-style string.
   - **True** - This is the required return type for compatibility

5. **True or False:** Smart pointers help achieve exception safety by preventing resource leaks.
   - **True** - RAII with smart pointers is a key exception safety technique

---

## 13. Flashcards for Quick Review

| Term | Definition |
|------|------------|
| **User-Defined Exception** | A custom exception class created by the programmer to represent application-specific error conditions |
| **Object Slicing** | The problem that occurs when a derived class object is copied into a base class object, losing derived class data |
| **noexcept** | A C++ specifier indicating that a function promises not to throw exceptions |
| **Exception Safety** | The guarantee that a program remains in a valid state when an exception is thrown |
| **Strong Guarantee** | An exception safety level where if an operation fails, the program state remains unchanged |
| **RAII** | Resource Acquisition Is Initialization - a technique using constructors/destructors for resource management |
| **what()** | A virtual function in std::exception that returns a C-string describing the exception |
| **Exception Hierarchy** | A tree-like structure where exception classes inherit from each other |

---

## 14. Programming Exercises

1. **Create an AgeValidationException** class that throws when an invalid age (negative or > 150) is provided. Include the invalid age value in the exception message.

2. **Design a CalculatorException** hierarchy with DivideByZeroException and OverflowException. Implement a calculator class that throws appropriate exceptions.

3. **Implement a FileProcessor** class with custom exceptions for FileNotFoundException, PermissionDeniedException, and InvalidFormatException.

4. **Modify the Student Management System** example to add a GradeOutOfRangeException and implement grade-based filtering.

5. **Create a NetworkException** hierarchy for a simulated network application with ConnectionTimeoutException, DataCorruptedException, and ServerUnavailableException.

---

*This comprehensive study material covers all essential aspects of User-Defined Exceptions in C++ as per the Delhi University NEP 2024 syllabus for BSc Physical Science (CS).*