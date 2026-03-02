# Expressions and Statements in C Programming


## Table of Contents

- [Expressions and Statements in C Programming](#expressions-and-statements-in-c-programming)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Expressions in C](#expressions-in-c)
  - [Operator Precedence and Associativity](#operator-precedence-and-associativity)
  - [Type Conversion in Expressions](#type-conversion-in-expressions)
  - [Statements in C](#statements-in-c)
  - [Side Effects and Sequence Points](#side-effects-and-sequence-points)
- [Examples](#examples)
  - [Example 1: Evaluating Complex Arithmetic Expressions](#example-1-evaluating-complex-arithmetic-expressions)
  - [Example 2: Using Conditional and Logical Expressions](#example-2-using-conditional-and-logical-expressions)
  - [Example 3: Type Conversion and Casting](#example-3-type-conversion-and-casting)
- [Exam Tips](#exam-tips)

## Introduction

Expressions and statements form the fundamental building blocks of any C program. While expressions represent computations that yield values, statements are the executable units that control the flow of a program. Understanding the distinction between these two concepts and mastering their usage is essential for writing effective C code. In the context of problem-solving using C programming, proficiency in expressions and statements enables programmers to transform algorithmic logic into functional code.

The C programming language provides a rich set of operators that can be combined to form complex expressions. These expressions can involve arithmetic operations, comparisons, logical operations, and assignments. Statements, on the other hand, are complete instructions that the compiler executes. From simple assignment statements to complex control structures, statements dictate how a program behaves during execution. For students at the University of Delhi, a thorough grasp of these concepts is crucial for the Internal Assessment and End Semester Examinations, as questions on expressions and statements frequently appear in paper patterns.

This topic connects directly with other essential concepts in C programming, including data types, operators, and control structures. The material covered here provides the foundation for decision-making statements and looping constructs that will be explored in subsequent topics. By mastering expressions and statements, students develop the ability to implement algorithmic solutions effectively.

## Key Concepts

### Expressions in C

An expression is a combination of operands (variables, constants, literals) and operators that evaluates to a single value. Every expression in C produces a value, which can be used in further computations or as part of a statement.

**Arithmetic Expressions** use arithmetic operators to perform mathematical calculations. The fundamental arithmetic operators include addition (+), subtraction (-), multiplication (*), division (/), and modulo (%). The division operator behaves differently for integers and floating-point numbers: integer division truncates the fractional part, while floating-point division preserves the decimal portion.

```c
int result = 10 + 5;      // result = 15
float avg = 15.0 / 4;     // avg = 3.75
int remainder = 17 % 5;   // remainder = 2
```

**Relational Expressions** compare two values using relational operators and return either true (1) or false (0). The operators include less than (<), greater than (>), less than or equal to (<=), greater than or equal to (>=), equality (==), and inequality (!=). It is crucial to distinguish between the equality operator (==) and the assignment operator (=), as using a single equals sign in a comparison context is a common source of bugs.

```c
int x = 10, y = 20;
int isLess = x < y;       // isLess = 1 (true)
int isEqual = x == y;    // isEqual = 0 (false)
```

**Logical Expressions** combine multiple conditions using logical operators: AND (&&), OR (||), and NOT (!). These operators follow short-circuit evaluation, meaning evaluation stops as soon as the result is determined. This behavior is particularly important for avoiding runtime errors, such as division by zero.

```c
int a = 5, b = 0;
int result = (a > 0) && (10 / b > 2);  // Second condition not evaluated due to short-circuit
```

**Assignment Expressions** not only assign values but also return the assigned value, allowing chained assignments. The simple assignment operator (=) is distinct from compound assignment operators (+=, -=, *=, /=, %=), which perform an operation and assignment in a single step.

```c
int x, y, z;
x = y = z = 10;    // Chained assignment, all become 10
x += 5;           // Equivalent to x = x + 5
```

**Conditional Expression** (ternary operator) provides a compact if-else construct. The syntax is condition ? expression1 : expression2. If the condition is true, expression1 is evaluated; otherwise, expression2 is evaluated.

```c
int max = (a > b) ? a : b;  // max gets the larger of a and b
```

**Comma Expression** evaluates multiple expressions from left to right and returns the value of the rightmost expression. While comma operators have lower precedence than most operators, parentheses are often necessary to achieve the desired effect.

```c
int x = (a = 5, b = 10, a + b);  // x = 15
```

### Operator Precedence and Associativity

Operator precedence determines the order in which operators are evaluated in expressions with multiple operators. Operators with higher precedence bind more tightly to their operands. When operators have equal precedence, associativity determines the order of evaluation. Most operators associate left to right, while assignment operators associate right to left.

The precedence hierarchy from highest to lowest is: parentheses, postfix operators, unary operators, multiplication/division/modulo, addition/subtraction, shift operators, relational operators, equality operators, bitwise AND, bitwise XOR, bitwise OR, logical AND, logical OR, conditional, assignment, and finally the comma operator.

### Type Conversion in Expressions

C performs implicit type conversions automatically when operands of different types appear in an expression. This process, called usual arithmetic conversion, promotes smaller types to larger types to preserve precision. For example, in an expression involving int and float, the int is promoted to float before the operation.

**Integral Promotion** converts char and short types to int or unsigned int. **Floating-Point Promotion** converts float to double if needed. When assigning between different types, the value is converted to the destination type, potentially causing truncation or loss of precision.

Explicit type conversion, known as casting, allows programmers to override implicit conversions. The syntax is (type) expression. For instance, (float) a / b ensures floating-point division even when both operands are integers.

### Statements in C

A statement is a complete instruction that causes some action to be performed. C provides several types of statements, each serving a specific purpose in program structure.

**Expression Statements** consist of an expression followed by a semicolon. These are the most common statements and include assignment statements, function calls, and increment/decrement operations.

```c
x = 5;              // Assignment statement
y = x + 10;        // Arithmetic expression statement
printf("Hello");   // Function call statement
i++;               // Increment statement
```

**Compound Statements** (blocks) group multiple statements together within curly braces {}. They are used in control structures where a group of statements needs to be executed as a single unit. Variables declared inside a block have block scope and are not accessible outside that block.

```c
{
    int temp = x;
    x = y;
    y = temp;
}
```

**Null Statement** contains only a semicolon and performs no operation. It is occasionally useful in loops where the loop body is intentionally empty.

```c
while (getchar() != '\n')
    ;  // Null statement: consume characters until newline
```

**Control Flow Statements** include selection statements (if, switch) and iteration statements (while, do-while, for). These are covered in detail in subsequent topics but fundamentally rely on expressions to determine program flow.

### Side Effects and Sequence Points

Side effects occur when an expression modifies the value of a variable. The increment operator (++) and assignment operator (=) are common sources of side effects. Sequence points define points in program execution where all side effects from previous evaluations are guaranteed to be complete.

The comma operator, function call after evaluating all arguments, and the conditional operator introduce sequence points. Understanding sequence points is crucial to avoid undefined behavior, particularly when modifying the same variable multiple times within a single expression.

```c
int i = 1;
int x = i++ + i++;  // Undefined behavior: i is modified twice without sequence point
```

## Examples

### Example 1: Evaluating Complex Arithmetic Expressions

**Problem:** Calculate the area of a triangle given three sides using Heron's formula: Area = √(s(s-a)(s-b)(s-c)), where s = (a+b+c)/2.

**Solution:**

```c
#include <stdio.h>
#include <math.h>

int main() {
    float a = 5.0, b = 6.0, c = 7.0;
    float s = (a + b + c) / 2;  // Semi-perimeter calculation
    float area = sqrt(s * (s - a) * (s - b) * (s - c));
    printf("Area = %.2f\n", area);
    return 0;
}
```

The expression s * (s - a) * (s - b) * (s - c) demonstrates nested arithmetic operations. The parentheses ensure correct order of operations, calculating each term before multiplication. Output: Area = 14.70

### Example 2: Using Conditional and Logical Expressions

**Problem:** Determine if a student qualifies for a scholarship. A student qualifies if their CGPA is 8.5 or above AND their attendance is at least 75%.

**Solution:**

```c
#include <stdio.h>

int main() {
    float cgpa = 8.8;
    int attendance = 80;
    char *status = (cgpa >= 8.5 && attendance >= 75) ? "Qualified" : "Not Qualified";
    printf("Student status: %s\n", status);
    
    // Using nested conditional for grade classification
    char grade = (cgpa >= 9.5) ? 'O' : 
                 (cgpa >= 8.5) ? 'A' :
                 (cgpa >= 7.5) ? 'B' :
                 (cgpa >= 6.5) ? 'C' : 'F';
    printf("Grade: %c\n", grade);
    return 0;
}
```

This example demonstrates combining relational and logical operators in a conditional expression. The short-circuit evaluation of && ensures that if cgpa is less than 8.5, the attendance check is never performed, improving efficiency.

### Example 3: Type Conversion and Casting

**Problem:** Calculate the average of three integer numbers and display it with decimal precision.

**Solution:**

```c
#include <stdio.h>

int main() {
    int a = 10, b = 20, c = 30;
    
    // Method 1: Cast each variable individually
    float avg1 = (float)(a + b + c) / 3;
    
    // Method 2: Cast the sum after addition
    float avg2 = (float)(a + b + c) / 3;
    
    // Method 3: Implicit conversion (division by float literal)
    float avg3 = (a + b + c) / 3.0;
    
    printf("Average 1: %.2f\n", avg1);  // Output: 20.00
    printf("Average 2: %.2f\n", avg2);  // Output: 20.00
    printf("Average 3: %.2f\n", avg3);  // Output: 20.00
    
    // Demonstrating integer division vs floating-point division
    printf("\nInteger division: %d / %d = %d\n", 7, 3, 7/3);      // 2
    printf("Float division: 7.0 / 3.0 = %.2f\n", 7.0/3.0);        // 2.33
    
    return 0;
}
```

This example illustrates the critical difference between integer and floating-point division. Casting ensures accurate decimal results when working with integer operands.

## Exam Tips

1. **Operator Precedence Questions:** Remember the mnemonic "U MAD" for Unary, Multiplicative, Additive. Parentheses always have highest precedence and should be used liberally to avoid confusion in complex expressions.

2. **Difference Between = and ==:** The equality operator (==) compares values, while assignment (=) assigns values. Using = in a conditional context is a logical error that compilers often cannot detect, leading to unexpected program behavior.

3. **Integer vs Floating-Point Division:** When both operands are integers, C performs integer division, discarding the remainder. Use floating-point literals (3.0) or explicit casting to obtain decimal results.

4. **Short-Circuit Evaluation:** In expressions using &&, if the first condition is false, subsequent conditions are not evaluated. Similarly, in ||, if the first condition is true, evaluation stops. This behavior is important for writing efficient and safe code.

5. **Side Effects Awareness:** Avoid modifying the same variable multiple times in a single expression without sequence points, as this results in undefined behavior. Expressions like i = i++ or i = i++ + ++i should be avoided.

6. **Compound Assignment Operators:** Using compound operators (x += 5) is preferred over simple operators (x = x + 5) as they are more concise and may generate more efficient machine code.

7. **Ternary Operator Usage:** The conditional operator provides compact alternatives to if-else statements but should be used judiciously. Avoid nesting ternary operators excessively, as this reduces code readability.

8. **Type Promotion Rules:** Remember that char and short are automatically promoted to int in expressions. When mixing types, always consider implicit conversions to prevent unexpected results.