# Finally Block in Java

## Overview

The finally block in Java is used to execute important code, such as releasing system resources, regardless of whether an exception was thrown. It is typically used in conjunction with try-catch blocks.

## Key Points

- The finally block is always executed, regardless of whether an exception was thrown.
- It is used for cleanup code, such as closing files or database connections.
- The finally block is optional, but it is a good practice to include it when working with resources that need to be released.
- If an exception is thrown in the try block, the catch block will execute, followed by the finally block.
- If no exception is thrown, the finally block will still execute after the try block.

## Important Definitions

- **Try Block**: The block of code where exceptions may occur.
- **Catch Block**: The block of code that handles exceptions thrown in the try block.
- **Finally Block**: The block of code that always executes, regardless of whether an exception was thrown.

## Key Syntax

```java
try {
 // Code that might throw an exception
} catch (ExceptionType e) {
 // Handle the exception
} finally {
 // Cleanup code that always executes
}
```

## Exam Tips

- Make sure to include a finally block when working with resources that need to be released.
- Understand the order of execution: try, catch (if an exception is thrown), finally.
