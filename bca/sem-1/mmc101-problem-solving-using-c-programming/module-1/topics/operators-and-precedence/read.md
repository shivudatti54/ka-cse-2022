# Operators and Precedence in C Programming


## Table of Contents

- [Operators and Precedence in C Programming](#operators-and-precedence-in-c-programming)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Types of Operators in C](#types-of-operators-in-c)
  - [Operator Precedence and Associativity](#operator-precedence-and-associativity)
  - [Type Conversion in Expressions](#type-conversion-in-expressions)
- [Examples](#examples)
  - [Example 1: Understanding Precedence with Arithmetic Operators](#example-1-understanding-precedence-with-arithmetic-operators)
  - [Example 2: Increment and Decrement Operators](#example-2-increment-and-decrement-operators)
  - [Example 3: Logical Operators and Short-Circuit Evaluation](#example-3-logical-operators-and-short-circuit-evaluation)
  - [Example 4: Bitwise Operators](#example-4-bitwise-operators)
- [Exam Tips](#exam-tips)

## Introduction

Operators are fundamental building blocks in any programming language that allow us to perform operations on data. In C programming, operators enable manipulation of variables and values through arithmetic, logical, comparisons, and bit-level operations. Understanding operators and their precedence is crucial for writing correct and efficient C programs, as the order in which operations are evaluated directly affects the output of expressions.

The C language provides a rich set of operators that can be categorized into several types based on their functionality. Mastery of these operators and their precedence rules is essential for solving computational problems effectively. When writing complex expressions, the compiler follows specific rules to determine which operator to evaluate first, and without this knowledge, programmers may encounter unexpected results. This topic forms the foundation for writing logical expressions in decision-making statements, loops, and mathematical computations throughout your C programming journey.

## Key Concepts

### Types of Operators in C

C provides several categories of operators, each serving specific purposes in program development.

**Arithmetic Operators** form the backbone of mathematical computations in C. The binary arithmetic operators include addition (+), subtraction (-), multiplication (*), division (/), and modulus (%). The modulus operator (%) returns the remainder of integer division and works only with integer operands. Additionally, C provides unary operators: unary + (positive) and unary - (negative). The increment (++) and decrement (--) operators are special arithmetic operators that increase or decrease a variable's value by 1. The prefix form (++i) increments before using the value, while the postfix form (i++) uses the value before incrementing.

**Relational Operators** are used to compare two values and return either true (1) or false (0). The less than (<), greater than (>), less than or equal to (<=), greater than or equal to (>=), equal to (==), and not equal to (!=) operators fall into this category. These operators are extensively used in conditional statements and loops to control program flow.

**Logical Operators** combine multiple conditions in C programming. The logical AND (&&) returns true only if both operands are true, logical OR (||) returns true if at least one operand is true, and logical NOT (!) inverts the truth value of its operand. These operators follow short-circuit evaluation, meaning the second operand is not evaluated if the result can be determined from the first operand.

**Assignment Operators** assign values to variables, with the simple assignment operator (=) being the most fundamental. C also provides compound assignment operators that combine arithmetic or bitwise operations with assignment: +=, -=, *=, /=, %=, <<=, >>=, &=, ^=, and |=. These operators provide concise ways to update variable values.

**Bitwise Operators** perform operations at the individual bit level. The bitwise AND (&), OR (|), XOR (^), NOT (~), left shift (<<), and right shift (>>) operators manipulate integer values at their binary representation level. These operators are particularly useful in systems programming, embedded systems, and optimization scenarios.

**Ternary Operator** (?:) is a unique operator in C that provides a compact if-else functionality. The syntax is condition ? expression1 : expression2, where expression1 is evaluated if condition is true, otherwise expression2 is evaluated.

**Comma Operator** evaluates multiple expressions from left to right and returns the value of the rightmost expression. It is primarily used in for loops to initialize or update multiple variables.

**sizeof Operator** returns the size in bytes of a data type or variable. This operator is essential for memory-related operations and creating portable code.

### Operator Precedence and Associativity

When an expression contains multiple operators, the compiler must determine the order of evaluation. Operator precedence rules define which operator gets evaluated first when different operators are present in an expression. Higher precedence operators bind more tightly to their operands than lower precedence operators.

The precedence hierarchy from highest to lowest is as follows: postfix operators (++, --, function calls, array subscript, member access) have the highest precedence, followed by unary operators (+, -, !, ~, ++, --, sizeof, cast), then multiplicative operators (*, /, %), additive operators (+, -), shift operators (<<, >>), relational operators (<, <=, >, >=), equality operators (==, !=), bitwise AND (&), bitwise XOR (^), bitwise OR (|), logical AND (&&), logical OR (||), ternary operator (?:), assignment operators (=, +=, -=, etc.), and finally the comma operator (,) has the lowest precedence.

When operators have the same precedence, associativity determines the order of evaluation. Most operators associate from left to right, meaning the expression a - b - c is evaluated as (a - b) - c. However, assignment operators and the ternary operator associate from right to left. The expression a = b = c is evaluated as a = (b = c).

Understanding these rules is critical because they affect program behavior. For instance, the expression a + b * c evaluates as a + (b * c) because multiplication has higher precedence than addition. Similarly, the expression a || b && c evaluates as a || (b && c) because && has higher precedence than ||.

### Type Conversion in Expressions

When operators have operands of different types, C performs implicit type conversions through the usual arithmetic conversions. These conversions ensure that both operands have the same type before the operation is performed. For example, when an int and a float are used together, the int is converted to float before the operation. The compiler follows a hierarchy: int, unsigned int, long, unsigned long, float, double, long double.

Programmers can also use explicit type casting (type) expression to force conversion to a specific type. For instance, (int) 3.7 results in 3, truncating the decimal portion. Understanding type conversion is essential to avoid unexpected results, especially in division operations where integer division yields an integer result.

## Examples

### Example 1: Understanding Precedence with Arithmetic Operators

Consider the expression: result = 10 + 5 * 2 - 8 / 4

Step-by-step evaluation:
- Multiplication and division have higher precedence than addition and subtraction
- First: 5 * 2 = 10
- First: 8 / 4 = 2 (integer division)
- Expression becomes: result = 10 + 10 - 2
- Then: 10 + 10 = 20
- Finally: 20 - 2 = 18
- Result: 18

To change the order, use parentheses: result = (10 + 5) * (2 - 8) / 4
- (10 + 5) = 15
- (2 - 8) = -6
- 15 * (-6) = -90
- -90 / 4 = -22 (integer division truncates toward zero)
- Result: -22

### Example 2: Increment and Decrement Operators

```c
#include <stdio.h>
int main() {
    int a = 5, b, c;
    
    b = a++;  // Postfix: assign first, then increment
    printf("b = %d, a = %d\n", b, a);  // b = 5, a = 6
    
    c = ++a;  // Prefix: increment first, then assign
    printf("c = %d, a = %d\n", c, a);  // c = 7, a = 7
    
    int x = 10;
    printf("%d %d %d\n", x++, ++x, x);
    // x++ uses 10, then x becomes 11
    // ++x increments to 12, uses 12
    // x uses 12
    // Output: 10 12 12
    
    return 0;
}
```

This example demonstrates the crucial difference between prefix and postfix operators and how they affect value usage in expressions.

### Example 3: Logical Operators and Short-Circuit Evaluation

```c
#include <stdio.h>
int main() {
    int a = 5, b = 10, result;
    
    // Logical AND with short-circuit
    result = (a > 3) && (b++ > 5);
    printf("result = %d, b = %d\n", result, b);
    // First condition (a > 3) is true, so second is evaluated
    // b++ > 5 is true (10 > 5), b becomes 11
    // result = 1, b = 11
    
    a = 2; b = 10;
    result = (a > 3) && (b++ > 5);
    printf("result = %d, b = %d\n", result, b);
    // First condition (a > 3) is false
    // Short-circuit: second condition NOT evaluated
    // b remains 10
    // result = 0, b = 10
    
    return 0;
}
```

This demonstrates short-circuit evaluation where the second operand is not evaluated if the overall result is already determined.

### Example 4: Bitwise Operators

```c
#include <stdio.h>
int main() {
    unsigned int x = 12;    // Binary: 1100
    unsigned int y = 10;    // Binary: 1010
    
    printf("x & y = %d\n", x & y);   // 1000 = 8
    printf("x | y = %d\n", x | y);   // 1110 = 14
    printf("x ^ y = %d\n", x ^ y);   // 0110 = 6
    printf("~x = %d\n", ~x);         // Two's complement
    
    printf("x << 2 = %d\n", x << 2); // 1100 << 2 = 110000 = 48
    printf("x >> 2 = %d\n", x >> 2); // 1100 >> 2 = 11 = 3
    
    return 0;
}
```

Bitwise operations are essential for low-level programming tasks like setting flags, masking, and optimizing memory usage.

## Exam Tips

For DU semester examinations, keep these key points in mind:

1. MEMORIZE THE PRECEDENCE TABLE: The order from highest to lowest is postfix → unary → multiplicative → additive → shift → relational → equality → bitwise AND → bitwise XOR → bitwise OR → logical AND → logical OR → ternary → assignment → comma.

2. DIFFERENTIATE PREFIX AND POSTFIX: Remember that ++a increments before the value is used, while a++ uses the value before incrementing. This frequently appears in exams with printf and assignment statements.

3. LOGICAL OPERATORS SHORT-CIRCUIT: In (cond1 && cond2), if cond1 is false, cond2 is not evaluated. Similarly, in (cond1 || cond2), if cond1 is true, cond2 is not evaluated.

4. ASSIGNMENT VS EQUALITY: Common mistake is using = (assignment) instead of == (equality comparison) in conditional statements. The compiler may not always catch this.

5. INTEGER DIVISION TRUNCATES: When dividing integers in C, the result is truncated toward zero. 7/3 equals 2, not 2.333. Use casting or float operands for decimal results.

6. MODULUS WORKS WITH INTEGERS ONLY: The % operator requires both operands to be integers. Using it with floating-point values causes a compile error.

7. ASSOCIATIVITY MATTERS: Most operators associate left-to-right, but assignment and ternary operators associate right-to-left. Write a = b = c = 5 to understand this.

8. USE PARENTHESES FOR CLARITY: When in doubt about precedence, use parentheses. This makes code readable and guarantees the intended evaluation order.