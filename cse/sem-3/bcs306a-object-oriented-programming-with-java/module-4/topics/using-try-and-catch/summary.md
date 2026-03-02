# Using Try and Catch - Summary

## Key Definitions

- **Exception**: An abnormal condition that disrupts the normal flow of program execution during runtime
- **Try Block**: A code block containing statements that might throw exceptions, requiring monitoring
- **Catch Block**: A handler block that executes when a specific type of exception is caught
- **Exception Object**: An instance containing details about the error, including message and stack trace
- **Exception Hierarchy**: The inheritance relationship between exception classes in Java

## Important Formulas

Basic try-catch syntax:
```java
try {
    // statements that may throw exception
} catch (ExceptionType variableName) {
    // handling code
}
```

Multiple catch blocks:
```java
try {
    // statements
} catch (ExceptionType1 e) {
    // handler 1
} catch (ExceptionType2 e) {
    // handler 2
}
```

## Key Points

1. The try block must be followed by at least one catch or finally block for valid syntax
2. When an exception occurs, execution transfers to the matching catch block immediately
3. Only one catch block executes for each exception occurrence
4. Catch blocks are evaluated in order from top to bottom
5. Subclass exceptions must be caught before their superclass exceptions
6. The exception object provides getMessage() and printStackTrace() methods
7. If no exception occurs, all catch blocks are skipped entirely
8. After catch block execution, program continues with statements after the try-catch structure

## Common Mistakes

1. **Wrong Catch Order**: Placing general exception handlers (like Exception) before specific ones (like IOException), causing compilation error or catching wrong exceptions
2. **Empty Catch Blocks**: Using empty catch blocks that silently swallow exceptions without logging or handling, making debugging difficult
3. **Catching Too Broadly**: Catching Exception or Throwable for all errors prevents proper error diagnosis and may hide bugs in the code
4. **Missing Exception Handling**: Not wrapping potentially dangerous code in try-catch, leading to program crashes when exceptions occur