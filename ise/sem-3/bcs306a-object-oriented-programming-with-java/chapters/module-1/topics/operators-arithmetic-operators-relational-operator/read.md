# **Operators in Java**

## **Table of Contents**

1. [Arithmetic Operators](#arithmetic-operators)
2. [Relational Operators](#relational-operators)
3. [Boolean Logical Operators](#boolean-logical-operators)
4. [Assignment Operator](#assignment-operator)
5. [The ? Operator](#the-?-operator)
6. [Operator Precedence](#operator-precedence)
7. [Using Operators](#using-operators)

### Arithmetic Operators

---

Arithmetic operators are used to perform mathematical operations in Java. The following are the arithmetic operators available in Java:

- **Addition (`+`)**: Used to add two numbers together.
- **Subtraction (`-`)**: Used to subtract one number from another.
- **Multiplication (`*`)**: Used to multiply two numbers together.
- **Division (`/`)**: Used to divide one number by another.
- **Modulus (`%`)**: Used to find the remainder of a division operation.

```java
int a = 10;
int b = 5;

int addition = a + b;  // Output: 15
int subtraction = a - b;  // Output: 5
int multiplication = a * b;  // Output: 50
int division = a / b;  // Output: 2
int modulus = a % b;  // Output: 0
```

### Relational Operators

---

Relational operators are used to compare two values in Java. The following are the relational operators available in Java:

- **Equal (`==`)**: Used to check if two values are equal.
- **Not Equal (`!=`)**: Used to check if two values are not equal.
- **Greater Than (`>`)**: Used to check if one value is greater than another.
- **Less Than (`<`)**: Used to check if one value is less than another.
- **Greater Than or Equal (`>=`)**: Used to check if one value is greater than or equal to another.
- **Less Than or Equal (`<=`)**: Used to check if one value is less than or equal to another.

```java
int a = 10;
int b = 5;

boolean equal = (a == b);  // Output: false
boolean notEqual = (a != b);  // Output: true
boolean greaterThan = (a > b);  // Output: true
boolean lessThan = (a < b);  // Output: false
boolean greaterThanOrEqualTo = (a >= b);  // Output: true
boolean lessThanOrEqualTo = (a <= b);  // Output: true
```

### Boolean Logical Operators

---

Boolean logical operators are used to combine boolean expressions in Java. The following are the boolean logical operators available in Java:

- **AND (`&&`)**: Used to combine two boolean expressions using a logical AND operation.
- **OR (`||`)**: Used to combine two boolean expressions using a logical OR operation.
- **NOT (`!`)**: Used to negate a boolean expression.

```java
boolean a = true;
boolean b = false;

boolean and = (a && b);  // Output: false
boolean or = (a || b);  // Output: true
boolean not = (!a);  // Output: false
```

### Assignment Operator

---

The assignment operator is used to assign a value to a variable in Java.

```java
int a = 10;
a = 20;  // Output: a is now 20
```

### The ? Operator

---

The ? operator is a ternary operator that is used to assign a value to a variable based on a condition. The syntax for the ? operator is as follows:

```java
condition ? valueIfTrue : valueIfFalse;
```

```java
int age = 25;
String status = (age >= 18) ? "Adult" : "Minor";
System.out.println(status);  // Output: Adult
```

### Operator Precedence

---

Operator precedence refers to the order in which operators are evaluated in an expression. The following are the operator precedence rules in Java:

- **Arithmetic operators**: `+`, `-`, `*`, `/`, `%`
- **Relational operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical operators**: `&&`, `||`, `!`
- **Assignment operators**: `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`
- **Unary operators**: `+`, `-`, `~`

```java
int a = 10;
int b = 5;

int result = a + b * 2;  // Output: result is 20
```

As seen in the example above, the multiplication operator (`*`) has higher precedence than the addition operator (`+`). Therefore, the expression `b * 2` is evaluated first, and then the result is added to `a`.

### Using Operators

---

Operators can be used in various contexts, such as:

- **Expressions**: Operators can be used to combine values in expressions.
- **Statements**: Operators can be used to modify variables or control the flow of a program.
- **Methods**: Operators can be used to implement methods or functions.

```java
public class OperatorExample {
    public static void main(String[] args) {
        int a = 10;
        int b = 5;

        // Using arithmetic operators
        int addition = a + b;  // Output: 15
        int subtraction = a - b;  // Output: 5

        // Using relational operators
        boolean equal = (a == b);  // Output: false
        boolean notEqual = (a != b);  // Output: true

        // Using logical operators
        boolean and = (a > 0 && b > 0);  // Output: false
        boolean or = (a > 0 || b > 0);  // Output: true

        // Using the ? operator
        String status = (a >= 18) ? "Adult" : "Minor";
        System.out.println(status);  // Output: Adult
    }
}
```
