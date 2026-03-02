# **Operators in Java**

## **Table of Contents**

1. [Arithmetic Operators](#arithmetic-operators)
2. [Relational Operators](#relational-operators)
3. [Boolean Logical Operators](#boolean-logical-operators)
4. [Assignment Operator](#assignment-operator)
5. [The ? Operator](#the-operator)
6. [Operator Precedence](#operator-precedence)
7. [Using Operators Correctly](#using-operators-correctly)

## **Arithmetic Operators**

Arithmetic operators are used to perform mathematical operations on variables.

### Examples of Arithmetic Operators

- Addition: `a = a + b;` (e.g., `x = 5 + 3;`)
- Subtraction: `a = a - b;` (e.g., `x = 5 - 3;`)
- Multiplication: `a = a * b;` (e.g., `x = 5 * 3;`)
- Division: `a = a / b;` (e.g., `x = 5 / 3;`)
- Modulus (remainder): `a = a % b;` (e.g., `x = 5 % 3;`)

## **Relational Operators**

Relational operators are used to compare values.

### Examples of Relational Operators

- Equal to: `a == b;` (e.g., `x = 5; if (x == 5) { ... }`)
- Not equal to: `a != b;` (e.g., `x = 5; if (x != 5) { ... }`)
- Greater than: `a > b;` (e.g., `x = 5; if (x > 5) { ... }`)
- Less than: `a < b;` (e.g., `x = 5; if (x < 5) { ... }`)
- Greater than or equal to: `a >= b;` (e.g., `x = 5; if (x >= 5) { ... }`)
- Less than or equal to: `a <= b;` (e.g., `x = 5; if (x <= 5) { ... }`)

## **Boolean Logical Operators**

Boolean logical operators are used to combine Boolean values.

### Examples of Boolean Logical Operators

- AND: `a && b;` (e.g., `x = 5; y = 3; if (x > 0 && y > 0) { ... }`)
- OR: `a || b;` (e.g., `x = 5; y = 3; if (x > 0 || y > 0) { ... }`)
- NOT: `!a;` (e.g., `x = 5; if (!x > 0) { ... }`)

## **Assignment Operator**

The assignment operator is used to assign a value to a variable.

### Example of Assignment Operator

- `a = b;` (e.g., `x = 5; y = 3; x = y;`)

## **The ? Operator**

The ? operator is used to return a value if a condition is true, otherwise it returns a default value.

### Examples of The ? Operator

- `int x = 5; int y = x > 0 ? 10 : 0;` (e.g., `x = 5; y = x > 0 ? 10 : 0;` => `y = 10`)
- `int x = 5; int y = x > 0 ? 10 : 5;` (e.g., `x = 5; y = x > 0 ? 10 : 5;` => `y = 5`)

## **Operator Precedence**

Operator precedence is the order in which operators are evaluated when they appear in an expression.

### Examples of Operator Precedence

- `a + b * c;` (e.g., `x = 5; y = 3; z = 2; x = x + y * z;` => `x = 5 + 6;` => `x = 11`)
- `a == b && c > 0;` (e.g., `x = 5; y = 3; if (x == y && x > 0) { ... }`)

## **Using Operators Correctly**

- Always use parentheses to group expressions and ensure the correct order of operations.
- Use operators consistently throughout your code.
- Avoid using operators in unclear or ambiguous situations.
- Use the `==` operator to compare values, not `=` (which is used for assignment).

By following these guidelines and using operators correctly, you can write more efficient, readable, and maintainable code in Java.
