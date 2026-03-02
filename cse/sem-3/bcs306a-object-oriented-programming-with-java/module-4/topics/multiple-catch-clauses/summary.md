# Multiple Catch Clauses in Java

## Overview

Multiple catch clauses allow a single try block to handle different types of exceptions separately. Each catch block handles a specific exception type, enabling precise error handling and recovery. This approach improves code readability and maintainability by separating exception handling logic.

## Key Points

- **Multiple catch blocks** follow a try block to handle different exception types
- Each catch block catches a specific exception class and handles it differently
- Catch blocks are evaluated **top-to-bottom** — first match wins
- More specific exceptions must be caught **before** more general ones
- If superclass exception is caught first, subclass exceptions will never be reached
- A single try block can have **unlimited catch blocks**
- If no catch block matches, the exception propagates up the call stack

## Important Definitions

- **try block**: Code segment that may throw exceptions; must be followed by catch/finally
- **catch block**: Exception handler that executes when a specific exception type occurs
- **Exception hierarchy**: Throwable → Error/Exception → RuntimeException/IOException, etc.

## Key Formulas / Syntax

```java
try {
    // Risky code that may throw multiple exceptions
} catch (IOException e) {
    // Handle IOException specifically
} catch (SQLException e) {
    // Handle SQLException specifically
} catch (Exception e) {
    // Handle any other exception (catch-all)
}
```

## Comparisons

| Aspect       | Multiple Catch Blocks             | Single Catch Block         |
| ------------ | --------------------------------- | -------------------------- |
| Granularity  | Handle each exception differently | Generic handling           |
| Code clarity | More verbose but clear            | Less code, less specific   |
| Flexibility  | High - different actions per type | Low - same action for all  |
| Best for     | Diverse exception types           | Similar exception handling |

## Exam Tips

- **Remember**: Always catch **subclass exceptions before** superclass exceptions
- Common question: Identify the correct order of catch blocks for IOException, Exception, and FileNotFoundException
- If catch(Exception e) comes first, it will catch all exceptions including IO and Runtime exceptions — compiler error for unreachable catch blocks
- Java 7+ introduced multi-catch syntax: `catch(IOException | SQLException e)` as alternative
- Always log or handle exceptions; never leave catch blocks empty in practical programs
