# Operators in Java

=====================================

Operators are a fundamental concept in programming languages, including Java. They allow programmers to perform various operations on variables, data types, and other expressions. In this section, we will delve into the different types of operators in Java, their uses, and examples.

## Arithmetic Operators

---

Arithmetic operators are used to perform mathematical operations on variables and data types. The following are the arithmetic operators in Java:

- `+` (Addition)
- `-` (Subtraction)
- `*` (Multiplication)
- `/` (Division)
- `%` (Modulus)
- `++` (Increment)
- `--` (Decrement)

### Examples

```java
// Addition
int a = 10;
int b = 5;
int sum = a + b; // sum = 15

// Subtraction
int difference = b - a; // difference = 5

// Multiplication
int product = a * b; // product = 50

// Division
double quotient = (double) a / b; // quotient = 2.0

// Modulus
int remainder = a % b; // remainder = 0

// Increment
a++; // a = 11

// Decrement
b--; // b = 4
```

## Relational Operators

---

Relational operators are used to compare the values of variables and data types. The following are the relational operators in Java:

- `==` (Equal to)
- `!=` (Not equal to)
- `>` (Greater than)
- `<` (Less than)
- `>=` (Greater than or equal to)
- `<=` (Less than or equal to)

### Examples

```java
// Equal to
int x = 10;
int y = 10;
boolean isEqual = x == y; // isEqual = true

// Not equal to
boolean isNotEqual = x != y; // isNotEqual = false

// Greater than
boolean isGreater = x > y; // isGreater = false

// Less than
boolean isLess = y < x; // isLess = true

// Greater than or equal to
boolean isGreaterOrEqual = x >= y; // isGreaterOrEqual = true

// Less than or equal to
boolean isLessOrEqual = y <= x; // isLessOrEqual = true
```

## Boolean Logical Operators

---

Boolean logical operators are used to combine boolean values using logical operations. The following are the boolean logical operators in Java:

- `&&` (And)
- `||` (Or)
- `!` (Not)

### Examples

```java
// And
boolean a = true;
boolean b = false;
boolean andResult = a && b; // andResult = false

// Or
boolean c = true;
boolean d = true;
boolean orResult = a || c; // orResult = true

// Not
boolean notResult = !a; // notResult = false
```

## Assignment Operator

---

The assignment operator is used to assign a value to a variable. The following is the assignment operator in Java:

- `=` (Assignment)

### Examples

```java
// Simple assignment
int x = 10; // x = 10

// Multiple assignment
int y = 20, z = 30; // y = 20, z = 30
```

## Null Coalescing Operator

---

The null coalescing operator is used to provide a default value when a variable is null. The following is the null coalescing operator in Java:

- `??` (Null coalescing)

### Examples

```java
// Null coalescing
String x = null;
String y = x ?? "default"; // y = "default"

// Null coalescing with multiple variables
String a = null;
String b = a ?? "default";
String c = b ?? "default"; // c = "default"
```

## Ternary Operator

---

The ternary operator is used to perform a simple if-else operation in one line. The following is the ternary operator in Java:

- `? :` (Ternary operator)

### Examples

```java
// Simple ternary
int x = 10;
int y = x > 5 ? 10 : 5; // y = 10

// Multiple ternary
int z = 10;
int w = z > 5 ? 10 : z < 5 ? 5 : 15; // w = 15
```

## Operator Precedence

---

Operator precedence is the order in which operators are evaluated during an expression evaluation. The following is the operator precedence in Java:

| Operator      | Precedence |
| ------------- | ---------- | --- | --- |
| `()`          | 1          |
| `? :`         | 2          |
| `++` and `--` | 3          |
| `+` and `-`   | 4          |
| `*` and `/`   | 5          |
| `%`           | 6          |
| `==` and `!=` | 7          |
| `>` and `<`   | 8          |
| `>=` and `<=` | 9          |
| `&&` and `    |            | `   | 10  |

### Examples

```java
// Expression with multiple operators
int x = 10;
int y = 5;
int result = x + y * 2 - 3; // result = 13
```

## Using Operators in Real-World Scenarios

---

Operators are used extensively in real-world scenarios, including:

- **Mathematical calculations**: Operators are used to perform mathematical operations such as addition, subtraction, multiplication, and division.
- **Data comparison**: Operators are used to compare data values, such as strings and numbers, to determine their equality or inequality.
- **Logical operations**: Operators are used to combine logical conditions to make decisions or execute actions.
- **Assignment and initialization**: Operators are used to assign values to variables and initialize data types.

### Example Use Case: A Simple Calculator Program

The following is an example of a simple calculator program that uses operators to perform mathematical calculations:

```java
import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the first number:");
        double num1 = scanner.nextDouble();

        System.out.println("Enter the operator (+, -, *, /):");
        char operator = scanner.next().charAt(0);

        System.out.println("Enter the second number:");
        double num2 = scanner.nextDouble();

        double result = 0;

        switch (operator) {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                result = num1 / num2;
                break;
            default:
                System.out.println("Invalid operator");
                return;
        }

        System.out.println("Result: " + result);
    }
}
```

This program uses operators to perform mathematical calculations and demonstrates the use of operators in real-world scenarios.

## Further Reading

---

- [Java Language Specification](https://docs.oracle.com/javase/specs/jls/se17/html/index.html)
- [Java Tutorials](https://docs.oracle.com/javase/tutorial/)
- [Operator Precedence in Java](https://www.geeksforgeeks.org/operator-precedence-in-java/)
- [Using Operators in Real-World Scenarios](https://www.javatpoint.com/java-operators)
- [Mathematical Operations in Java](https://www.tutorialspoint.com/java/java_mathematical_operations.htm)

By mastering operators in Java, you can write more efficient, readable, and maintainable code. Remember to use operators in real-world scenarios to make your programs more effective and user-friendly.
