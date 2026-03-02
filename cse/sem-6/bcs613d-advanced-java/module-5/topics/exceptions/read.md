# Exception Handling in Java

## Introduction

Exception handling is a critical mechanism in Java that enables developers to manage runtime errors systematically. An exception is an event occurring during program execution that disrupts normal flow, such as invalid input, missing files, or network failures. Java's exception handling framework follows object-oriented principles, allowing errors to be encapsulated as objects and handled through dedicated code blocks.

Effective exception handling provides three key benefits:

1. **Fault Isolation**: Separates error-handling code from business logic
2. **Error Recovery**: Enables programs to continue execution after non-fatal errors
3. **Diagnostics**: Provides stack traces and error messages for debugging

In enterprise applications, proper exception handling is crucial for:

- Database transaction management
- File system operations
- Network communication reliability
- User input validation

## Java Exception Hierarchy

Java's exception classes inherit from `java.lang.Throwable`:

```
Throwable
├── Error (Unchecked)
│ ├── OutOfMemoryError
│ └── StackOverflowError
│
└── Exception (Checked)
 ├── IOException
 │ ├── FileNotFoundException
 │ └── EOFException
 │
 └── RuntimeException (Unchecked)
 ├── NullPointerException
 ├── ArrayIndexOutOfBoundsException
 └── ArithmeticException
```

**Key Classifications**:

- **Checked Exceptions**: Must be declared or handled (subclasses of `Exception`)
- **Unchecked Exceptions**: Not required to be declared (`RuntimeException` and `Error` subclasses)

## Try-Catch-Finally Mechanism

### Basic Syntax

```java
try {
 // Code that might throw exceptions
}
catch (ExceptionType1 e1) {
 // Handler for ExceptionType1
}
catch (ExceptionType2 e2) {
 // Handler for ExceptionType2
}
finally {
 // Cleanup code (always executes)
}
```

### Multi-Catch (Java 7+)

```java
try {
 // Code throwing multiple exception types
}
catch (IOException | SQLException e) {
 // Handle both exception types
}
```

## Throws and Throw Keywords

### Method Declaration with Throws

```java
public void readFile() throws IOException {
 // Method code that may throw IOException
}
```

### Explicit Exception Throwing

```java
public void validateAge(int age) {
 if(age < 0) {
 throw new IllegalArgumentException("Age cannot be negative");
 }
}
```

## Custom Exceptions

### Creating Custom Exception Class

```java
public class InsufficientFundsException extends Exception {
 public InsufficientFundsException(String message) {
 super(message);
 }

 public InsufficientFundsException(String message, Throwable cause) {
 super(message, cause);
 }
}
```

### Usage Example

```java
public void withdraw(double amount) throws InsufficientFundsException {
 if(amount > balance) {
 throw new InsufficientFundsException("Balance short by " + (amount - balance));
 }
 // Withdrawal logic
}
```

## Exception Propagation

### Call Stack Propagation

```java
public class PropagationDemo {
 void method1() {
 method2();
 }

 void method2() {
 method3();
 }

 void method3() {
 throw new ArithmeticException("Divide by zero");
 }

 public static void main(String[] args) {
 try {
 new PropagationDemo().method1();
 }
 catch(ArithmeticException e) {
 System.out.println("Caught in main: " + e.getMessage());
 }
 }
}
```

**Output**:

```
Caught in main: Divide by zero
```

## Common Java Exceptions

| Exception Type                   | Typical Cause                   | Checked/Unchecked |
| -------------------------------- | ------------------------------- | ----------------- |
| `NullPointerException`           | Accessing null object reference | Unchecked         |
| `ArrayIndexOutOfBoundsException` | Invalid array index access      | Unchecked         |
| `NumberFormatException`          | Invalid numeric conversion      | Unchecked         |
| `FileNotFoundException`          | Missing file access             | Checked           |
| `SQLException`                   | Database operation failure      | Checked           |

## Real-World Applications

1. **Database Operations**:

```java
try (Connection conn = DriverManager.getConnection(url);
 Statement stmt = conn.createStatement()) {
 // Execute SQL queries
}
catch (SQLException e) {
 // Log error and rollback transaction
}
```

2. **File Handling**:

```java
try (BufferedReader br = new BufferedReader(new FileReader("data.txt"))) {
 String line;
 while ((line = br.readLine()) != null) {
 // Process file content
 }
}
catch (IOException e) {
 System.err.println("File error: " + e.getMessage());
}
```

3. **Network Operations**:

```java
try {
 URL url = new URL("https://api.example.com/data");
 HttpURLConnection conn = (HttpURLConnection) url.openConnection();
 // Handle response
}
catch (MalformedURLException e) {
 // Handle invalid URL format
}
catch (IOException e) {
 // Handle network errors
}
```

## Examples

### Example 1: Basic Exception Handling

```java
public class DivisionDemo {
 public static void main(String[] args) {
 Scanner sc = new Scanner(System.in);

 try {
 System.out.print("Enter numerator: ");
 int num = sc.nextInt();

 System.out.print("Enter denominator: ");
 int den = sc.nextInt();

 System.out.println("Result: " + (num/den));
 }
 catch (ArithmeticException e) {
 System.out.println("Error: Division by zero");
 }
 catch (InputMismatchException e) {
 System.out.println("Error: Invalid integer input");
 }
 finally {
 sc.close();
 System.out.println("Scanner closed");
 }
 }
}
```

### Example 2: Custom Exception Implementation

```java
class InvalidTemperatureException extends Exception {
 public InvalidTemperatureException(String message) {
 super(message);
 }
}

public class ReactorControl {
 void checkTemperature(double temp) throws InvalidTemperatureException {
 if(temp > 1000) {
 throw new InvalidTemperatureException(
 "Critical temperature reached: " + temp + "°C");
 }
 }

 public static void main(String[] args) {
 ReactorControl reactor = new ReactorControl();
 try {
 reactor.checkTemperature(1200);
 }
 catch (InvalidTemperatureException e) {
 System.out.println("Safety Protocol Activated: " + e.getMessage());
 }
 }
}
```

## Exam Tips

1. **Checked vs Unchecked**:

- Checked exceptions must be handled or declared
- Unchecked exceptions (Runtime/Error) don't require declaration

2. **Finally Block**:

- Always executes unless JVM exits (System.exit())
- Used for resource cleanup (file handles, database connections)

3. **Exception Propagation**:

- Uncaught exceptions propagate up the call stack
- Can be caught at any level in the method hierarchy

4. **Multi-Catch**:

- Use pipe (|) to catch multiple exceptions in one block
- Catch parameter is implicitly final

5. **Try-With-Resources**:

- AutoCloseable resources declared in try header
- Resources closed automatically in reverse declaration order

6. **Custom Exceptions**:

- Always provide constructors with String parameter
- Include cause parameter for exception chaining

7. **Common Mistakes**:

- Catching Throwable/Exception too early
- Swallowing exceptions (empty catch blocks)
- Improper resource closing order (ResultSet → Statement → Connection)
