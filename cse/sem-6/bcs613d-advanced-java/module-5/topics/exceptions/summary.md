# Exception Handling - Summary

## Key Definitions and Concepts

- **Exception**: Runtime error disrupting program flow (e.g., `NullPointerException`)
- **Throwable**: Root class for all exceptions (`Error` and `Exception`)
- **Error**: Unrecoverable system-level failure (e.g., `OutOfMemoryError`)
- **Checked Exception**: Must be declared/caught (compile-time enforcement, e.g., `IOException`)
- **Unchecked Exception**: Runtime exceptions (subclasses of `RuntimeException`)
- **try-catch-finally**: Code blocks for exception handling
- **throw**: Keyword to explicitly throw exception
- **throws**: Method declaration clause for exception propagation
- **try-with-resources**: Automatic resource management (Java 7+)

## Important Syntax and Hierarchy

```java
// Basic try-catch
try {
    // Code that might throw exception
} catch (ExceptionType1 e1) {
    // Handler 1
} catch (ExceptionType2 e2) {
    // Handler 2
} finally {
    // Always executes
}

// Exception Hierarchy
Throwable
├── Error
└── Exception
    ├── RuntimeException
    └── Checked Exceptions

// try-with-resources
try (ResourceType res = new Resource()) {
    // Use resource
}
```

## Key Points

1. Exception handling prevents program termination on errors
2. `try` block contains risky code, `catch` handles exceptions, `finally` cleans up resources
3. Checked exceptions require explicit handling (compile-time check)
4. Unchecked exceptions (Runtime/Logic errors) can be prevented with proper coding
5. Exception propagation allows handling at appropriate levels
6. Custom exceptions extend `Exception` or `RuntimeException`
7. `try-with-resources` automatically closes `AutoCloseable` resources
8. Multiple catch blocks must order exceptions from specific to general
9. `finally` block executes regardless of exception occurrence
10. JDBC exceptions: `SQLException`, `ClassNotFoundException`, `BatchUpdateException`

## Common Mistakes to Avoid

1. Catching generic `Exception` instead of specific exceptions
2. Swallowing exceptions (empty catch blocks)
3. Improper resource closing order (ResultSet → Statement → Connection)
4. Using `throws` instead of proper handling in critical methods
5. Ignoring return codes from `executeUpdate()` in JDBC
6. Forgetting `Class.forName()` for JDBC driver registration

## Revision Tips

1. Practice writing custom exceptions with proper inheritance
2. Memorize exception hierarchy using mnemonics: "TEA" (Throwable → Error/Exception → Application exceptions)
3. Focus on JDBC exception patterns:
   ```java
   try (Connection conn = DriverManager.getConnection(url);
        Statement stmt = conn.createStatement()) {
       // JDBC operations
   } catch (SQLException e) {
       System.err.println("Error code: " + e.getErrorCode());
   }
   ```
4. Create flashcards for exception methods:
   - `getMessage()`: Returns error description
   - `printStackTrace()`: Prints stack trace to System.err
   - `getErrorCode()`: JDBC-specific error code (SQLException)
