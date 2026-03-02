# User Defined Exceptions in C++

## Introduction
User-defined exceptions are custom exception classes created by programmers to handle specific error conditions that are not covered by C++'s standard exception hierarchy. In the context of Delhi University's Ge1B Programming Using Cpp syllabus (NEP 2024), understanding user-defined exceptions is essential for writing robust and maintainable C++ programs.

## Key Concepts

### Need for User-Defined Exceptions
- Standard exceptions (std::exception, std::runtime_error, etc.) may not represent domain-specific error conditions
- Allow programmers to create meaningful error types specific to application logic
- Improve code readability and debugging by providing context-specific error information

### Creating Custom Exception Classes
- Inherit from std::exception or its derived classes
- Override the what() method to return descriptive error messages
- Can include additional member variables for error details

```cpp
class InvalidInputException : public std::exception {
    std::string message;
public:
    InvalidInputException(const std::string& msg) : message(msg) {}
    const char* what() const noexcept override {
        return message.c_str();
    }
};
```

### Throwing and Catching User-Defined Exceptions
- Use `throw` keyword to raise custom exceptions
- Catch using reference to base exception class for polymorphism
- Multiple catch blocks can handle different exception types

```cpp
try {
    throw InvalidInputException("Age cannot be negative");
} catch (const InvalidInputException& e) {
    std::cout << e.what() << std::endl;
}
```

### Best Practices
- Derive from std::exception for consistent exception handling
- Use meaningful class names indicating error type
- Follow naming conventions (end with "Exception" or "Error")
- Throw by value, catch by const reference
- Keep exception classes simple and focused

## Exam Quick Reference

| Topic | Key Points |
|-------|------------|
| Definition | Custom exception classes inheriting from std::exception |
| Creation | Override what() method |
| Throwing | throw keyword with custom object |
| Catching | catch by const reference |
| Advantage | Domain-specific error handling |

## Conclusion
User-defined exceptions are a powerful feature in C++ that enable programmers to create meaningful, application-specific error handling mechanisms. For Delhi University exams, remember to emphasize inheritance from std::exception, proper throw/catch semantics, and the importance of custom exceptions in building reliable software systems. Focus on understanding when and how to create custom exception classes rather than just memorizing syntax.