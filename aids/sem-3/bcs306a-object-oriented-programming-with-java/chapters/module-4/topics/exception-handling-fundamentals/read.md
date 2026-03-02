# Exception Handling in C++

## Introduction to Exception Handling

Exception handling is a powerful mechanism in C++ that allows programs to handle runtime errors gracefully. Instead of letting the program crash or producing incorrect results when an error occurs, exception handling provides a structured way to detect, report, and manage errors.

**Why Exception Handling?**
- Separates error-handling code from normal program logic
- Allows errors to be handled at appropriate levels in the program hierarchy
- Provides a standardized way to handle various types of errors
- Prevents program termination due to unhandled errors

## Basic Exception Handling Syntax

C++ provides three keywords for exception handling:
- `try`: Identifies a block of code where exceptions might occur
- `catch`: Catches and handles exceptions thrown from the try block
- `throw`: Throws an exception when a problem is detected

```cpp
try {
    // Code that might throw an exception
    if (error_condition) {
        throw exception_object;
    }
}
catch (ExceptionType e) {
    // Code to handle the exception
}
```

## Throwing Exceptions

You can throw exceptions of any data type, but it's recommended to use objects (especially those derived from std::exception) for better organization and information.

```cpp
// Throwing primitive types
throw 42;
throw "Error occurred";

// Throwing objects
class MyException {
public:
    const char* what() const { return "My custom exception"; }
};
throw MyException();
```

## Catching Exceptions

Multiple catch blocks can be used to handle different types of exceptions:

```cpp
try {
    // Code that might throw exceptions
}
catch (int e) {
    cout << "Integer exception: " << e << endl;
}
catch (const char* e) {
    cout << "String exception: " << e << endl;
}
catch (const std::exception& e) {
    cout << "Standard exception: " << e.what() << endl;
}
catch (...) {
    cout << "Unknown exception caught" << endl;
}
```

## Standard Exception Hierarchy

C++ provides a hierarchy of standard exception classes in the `<stdexcept>` header:

```
std::exception
├── std::logic_error
│   ├── std::invalid_argument
│   ├── std::domain_error
│   ├── std::length_error
│   └── std::out_of_range
├── std::runtime_error
│   ├── std::range_error
│   ├── std::overflow_error
│   ├── std::underflow_error
│   └── std::system_error
└── std::bad_alloc (from new failures)
```

**Table: Common Standard Exceptions**
| Exception Class | Description | Typical Use Case |
|----------------|-------------|------------------|
| `std::invalid_argument` | Invalid argument passed to function | Function parameter validation |
| `std::out_of_range` | Value out of valid range | Array/vector index validation |
| `std::runtime_error` | Errors that occur during runtime | File I/O errors, network issues |
| `std::bad_alloc` | Memory allocation failure | When new operator fails |

## Creating Custom Exceptions

You can create your own exception classes by inheriting from standard exception classes:

```cpp
#include <stdexcept>
#include <string>

class FileNotFoundException : public std::runtime_error {
public:
    FileNotFoundException(const std::string& filename)
        : std::runtime_error("File not found: " + filename) {}
};

// Usage
try {
    if (!file_exists("data.txt")) {
        throw FileNotFoundException("data.txt");
    }
}
catch (const FileNotFoundException& e) {
    std::cout << e.what() << std::endl;
}
```

## Exception Propagation

When an exception is thrown but not caught in the current scope, it propagates up the call stack until it finds a matching catch block or terminates the program.

```
Function Call Stack:
main()
├── function1()
│   └── function2()
│       └── function3() ← Exception thrown here
```

If function3() doesn't handle the exception, it propagates to function2(), then function1(), and finally main(). If no handler is found, std::terminate() is called.

## Exception Safety Guarantees

C++ defines three levels of exception safety:

1. **No-throw guarantee**: Operation will not throw exceptions
2. **Strong guarantee**: Operation either completes successfully or has no effect if an exception occurs (transactional)
3. **Basic guarantee**: If an exception occurs, no resources are leaked and objects remain in valid state

## RAII and Exception Handling

Resource Acquisition Is Initialization (RAII) is crucial for exception-safe code. Resources are managed by objects whose destructors automatically clean up resources.

```cpp
class FileHandler {
private:
    FILE* file;
public:
    FileHandler(const char* filename) : file(fopen(filename, "r")) {
        if (!file) throw std::runtime_error("Cannot open file");
    }
    ~FileHandler() { if (file) fclose(file); }
    // Prevent copying
    FileHandler(const FileHandler&) = delete;
    FileHandler& operator=(const FileHandler&) = delete;
};

// Usage - file automatically closed even if exception occurs
try {
    FileHandler fh("data.txt");
    // Work with file
}
catch (const std::exception& e) {
    // File automatically closed by FileHandler destructor
}
```

## Advanced Exception Handling Techniques

### Exception Specifications (Deprecated)

C++98 had exception specifications, but they're deprecated in C++11 and removed in C++17:

```cpp
// Old style (deprecated)
void func() throw(std::exception); // Can only throw std::exception
void func() throw();               // Will not throw any exceptions

// C++11 style
void func() noexcept;              // Will not throw any exceptions
```

### Nested Exception Handling

You can nest try-catch blocks and rethrow exceptions:

```cpp
try {
    try {
        throw std::runtime_error("Inner exception");
    }
    catch (const std::exception& e) {
        std::cout << "Caught: " << e.what() << std::endl;
        throw; // Rethrow the same exception
    }
}
catch (const std::exception& e) {
    std::cout << "Outer catch: " << e.what() << std::endl;
}
```

### Exception Handling in Constructors

Constructors should handle exceptions carefully to avoid partially constructed objects:

```cpp
class ResourceHolder {
private:
    int* resource1;
    double* resource2;
    
public:
    ResourceHolder() : resource1(new int(42)), resource2(nullptr) {
        try {
            resource2 = new double(3.14);
            // More initialization that might throw
        }
        catch (...) {
            delete resource1; // Clean up acquired resources
            throw; // Re-throw the exception
        }
    }
    
    ~ResourceHolder() {
        delete resource1;
        delete resource2;
    }
};
```

## Best Practices for Exception Handling

1. **Throw by value, catch by const reference**
2. **Derive custom exceptions from std::exception**
3. **Use RAII for resource management**
4. **Don't throw exceptions from destructors**
5. **Catch specific exceptions before general ones**
6. **Document exception guarantees for your functions**
7. **Use noexcept for functions that shouldn't throw**

## Performance Considerations

Exception handling has minimal overhead when no exceptions occur. The cost comes mainly when exceptions are thrown. Modern compilers implement "zero-cost" exception handling where the cost is paid only when exceptions actually occur.

## Comparison: Error Handling Techniques

| Technique | Pros | Cons |
|-----------|------|------|
| Return Codes | Simple, predictable performance | Can be ignored, clutters interface |
| Exceptions | Separates error handling, automatic propagation | Overhead when thrown, harder to predict flow |
| Assertions | Catches programming errors during development | Disabled in release builds |

## Real-World Example: Database Connection

```cpp
class DatabaseConnection {
private:
    Connection* conn;
    
public:
    DatabaseConnection(const std::string& connectionString) {
        conn = connect_to_database(connectionString);
        if (!conn) {
            throw DatabaseConnectionException("Failed to connect to database");
        }
    }
    
    ~DatabaseConnection() {
        disconnect_from_database(conn);
    }
    
    void executeQuery(const std::string& query) {
        Result* result = execute_database_query(conn, query);
        if (!result) {
            throw DatabaseQueryException("Query execution failed");
        }
        // Process result
    }
};

// Usage
try {
    DatabaseConnection db("host=localhost;db=test");
    db.executeQuery("SELECT * FROM users");
}
catch (const DatabaseConnectionException& e) {
    std::cerr << "Connection error: " << e.what() << std::endl;
}
catch (const DatabaseQueryException& e) {
    std::cerr << "Query error: " << e.what() << std::endl;
}
catch (const std::exception& e) {
    std::cerr << "General error: " << e.what() << std::endl;
}
```

## Exam Tips

1. **Remember the three keywords**: `try`, `catch`, `throw`
2. **Catch order matters**: Specific exceptions should be caught before general ones
3. **RAII is key**: Always use resource-managing objects for exception safety
4. **Don't throw from destructors**: This can lead to program termination
5. **Use standard exceptions**: Derive custom exceptions from std::exception when possible
6. **Understand exception propagation**: Exceptions bubble up until caught
7. **Exception safety guarantees**: Know the difference between no-throw, strong, and basic guarantees