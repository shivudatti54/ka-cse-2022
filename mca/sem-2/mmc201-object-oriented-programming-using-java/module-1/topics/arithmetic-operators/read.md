# Arithmetic Operators in Java


## Table of Contents

- [Arithmetic Operators in Java](#arithmetic-operators-in-java)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Binary Arithmetic Operators](#binary-arithmetic-operators)
  - [Unary Operators](#unary-operators)
  - [Compound Assignment Operators](#compound-assignment-operators)
  - [Operator Precedence and Associativity](#operator-precedence-and-associativity)
  - [Type Promotion in Arithmetic Expressions](#type-promotion-in-arithmetic-expressions)
- [Examples](#examples)
  - [Example 1: Basic Arithmetic Operations](#example-1-basic-arithmetic-operations)
  - [Example 2: Prefix vs Postfix Increment](#example-2-prefix-vs-postfix-increment)
  - [Example 3: Compound Assignment and Type Promotion](#example-3-compound-assignment-and-type-promotion)
- [Exam Tips](#exam-tips)

## Introduction

Arithmetic operators form the foundation of mathematical computations in Java programming. These operators enable developers to perform basic mathematical operations on variables and literals, which is essential for any computational task. In the context of Object-Oriented Programming with Java, understanding arithmetic operators is crucial as they are frequently used in constructors, methods, and various computations within classes.

Java provides a rich set of arithmetic operators that can be categorized into two main types: binary operators (which operate on two operands) and unary operators (which operate on a single operand). The binary arithmetic operators include addition (+), subtraction (-), multiplication (\*), division (/), and modulus (%), while unary operators include increment (++) and decrement (--) operators. Additionally, Java offers compound assignment operators that combine arithmetic operations with assignment in a single expression.

Mastering arithmetic operators is essential for solving numerical problems, implementing algorithms, and performing data manipulations in Java applications. These operators follow specific precedence rules and type promotion behaviors that programmers must understand to write correct and efficient code. This module explores all aspects of arithmetic operators in Java, providing detailed explanations and practical examples suitable for university examination preparation.

## Key Concepts

### Binary Arithmetic Operators

Java supports five binary arithmetic operators that work with numeric operands:

**Addition Operator (+)**: The addition operator adds two operands together. It can be used with both integer and floating-point types. For example, `int sum = 10 + 5;` results in `sum` being 15. The addition operator is also used for string concatenation when at least one operand is a String.

**Subtraction Operator (-)**: The subtraction operator subtracts the right operand from the left operand. For instance, `int diff = 20 - 8;` results in `diff` being 12. This operator can also be used as a unary minus operator to negate a numeric value.

**Multiplication Operator (\*)**: The multiplication operator multiplies two operands. For example, `int product = 7 * 6;` results in `product` being 42. This operator has higher precedence than addition and subtraction.

**Division Operator (/)**: The division operator divides the left operand by the right operand. Important behavior: when both operands are integers, integer division is performed, and the result is truncated (not rounded). For example, `int result = 17 / 5;` results in `3`, not 3.4. For floating-point division, at least one operand must be floating-point.

**Modulus Operator (%)**: The modulus operator returns the remainder of integer division. For example, `int remainder = 17 % 5;` results in `2`. The modulus operator is particularly useful for checking divisibility, implementing cyclic operations, and determining even/odd numbers.

### Unary Operators

**Increment Operator (++)**: The increment operator increases the value of a variable by 1. It can be used in two forms: prefix (++x) and postfix (x++). In prefix form, the value is incremented first, then the expression is evaluated. In postfix form, the expression is evaluated first, then the value is incremented.

**Decrement Operator (--)**: The decrement operator decreases the value of a variable by 1. Similar to increment, it has prefix (--x) and postfix (x--) forms with identical behavior patterns.

### Compound Assignment Operators

Compound assignment operators provide a shorthand for combining an arithmetic operation with assignment:

- `+=` : Addition assignment (a += b is equivalent to a = a + b)
- `-=` : Subtraction assignment (a -= b is equivalent to a = a - b)
- `*=` : Multiplication assignment (a _= b is equivalent to a = a _ b)
- `/=` : Division assignment (a /= b is equivalent to a = a / b)
- `%=` : Modulus assignment (a %= b is equivalent to a = a % b)

These operators not only simplify code but also automatically perform implicit type casting when necessary.

### Operator Precedence and Associativity

Java follows a specific order of precedence for arithmetic operators:

1. Postfix operators (++, --) have highest precedence
2. Unary operators (-, +, ++, --) come next
3. Multiplicative operators (\*, /, %) have higher precedence than additive operators
4. Addition and subtraction have the lowest precedence among arithmetic operators

All arithmetic operators are left-to-right associative, meaning operations with the same precedence are evaluated from left to right.

### Type Promotion in Arithmetic Expressions

When performing arithmetic operations, Java automatically promotes smaller types to larger types to prevent data loss:

- byte, short, and char are promoted to int before any arithmetic operation
- If any operand is long, the entire expression is promoted to long
- If any operand is float, the entire expression is promoted to float
- If any operand is double, the entire expression is promoted to double

## Examples

### Example 1: Basic Arithmetic Operations

```java
public class ArithmeticDemo {
 public static void main(String[] args) {
 int a = 20, b = 6;

 System.out.println("Addition: " + (a + b)); // Output: 26
 System.out.println("Subtraction: " + (a - b)); // Output: 14
 System.out.println("Multiplication: " + (a * b)); // Output: 120
 System.out.println("Division: " + (a / b)); // Output: 3
 System.out.println("Modulus: " + (a % b)); // Output: 2

 // Floating-point division
 double result = (double) a / b;
 System.out.println("Float Division: " + result); // Output: 3.333...
 }
}
```

### Example 2: Prefix vs Postfix Increment

```java
public class IncrementDemo {
 public static void main(String[] args) {
 int x = 5, y;

 // Prefix: increment first, then use value
 y = ++x; // x becomes 6, y is assigned 6
 System.out.println("Prefix: x = " + x + ", y = " + y);

 x = 5; // Reset x
 // Postfix: use value first, then increment
 y = x++; // y is assigned 5, then x becomes 6
 System.out.println("Postfix: x = " + x + ", y = " + y);

 // Practical application
 int count = 0;
 System.out.println(count++); // Prints 0, count becomes 1
 System.out.println(++count); // count becomes 2, prints 2
 }
}
```

### Example 3: Compound Assignment and Type Promotion

```java
public class CompoundDemo {
 public static void main(String[] args) {
 // Compound assignment operators
 int a = 10;
 a += 5; // a = 15
 a -= 3; // a = 12
 a *= 2; // a = 24
 a /= 4; // a = 6
 a %= 5; // a = 1

 // Type promotion example
 byte b = 10;
 // byte result = b * 2; // Error: cannot assign int to byte
 byte result = (byte)(b * 2); // Correct with casting

 // Automatic promotion to int
 short s = 20;
 int result2 = b + s; // Both promoted to int

 System.out.println("Final a: " + a);
 System.out.println("Byte result: " + result);
 }
}
```

## Exam Tips

1. **Remember Integer Division Rule**: In Java, when dividing two integers, the result is always an integer (truncated, not rounded). This is a frequently tested concept in university exams.

2. **Prefix vs Postfix Distinction**: Always remember that `++x` increments first then returns the new value, while `x++` returns the current value then increments. This distinction is crucial in expressions and loop conditions.

3. **Modulus with Negative Numbers**: When the dividend is negative, the modulus result carries the sign of the dividend. For example, `-10 % 3` gives `-1`, while `10 % -3` gives `1`.

4. **Compound Assignment Advantage**: Compound operators like `+=` automatically perform casting, so `int += short` works without explicit casting, unlike `int = int + short`.

5. **Byte/Short/Char Promotion**: Remember that byte, short, and char are always promoted to int during arithmetic operations. This means `byte + byte` results in an int, not a byte.

6. **Operator Precedence**: Multiplication, division, and modulus have higher precedence than addition and subtraction. Use parentheses to make your intentions clear and avoid confusion.

7. **String Concatenation with +**: The + operator performs string concatenation when either operand is a String. This can lead to unexpected results if not careful: `"Sum is: " + 5 + 5` produces "Sum is: 55", not "Sum is: 10".
