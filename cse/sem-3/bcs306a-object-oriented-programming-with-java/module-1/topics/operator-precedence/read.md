# Operator Precedence in Java

## Table of Contents

- [Operator Precedence in Java](#operator-precedence-in-java)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [What is Operator Precedence?](#what-is-operator-precedence)
  - [The Precedence Hierarchy](#the-precedence-hierarchy)
  - [Associativity](#associativity)
  - [Parentheses Override Precedence](#parentheses-override-precedence)
- [Examples](#examples)
  - [Example 1: Basic Arithmetic Precedence](#example-1-basic-arithmetic-precedence)
  - [Example 2: Complex Expression with Multiple Operators](#example-2-complex-expression-with-multiple-operators)
  - [Example 3: Logical and Relational Operators](#example-3-logical-and-relational-operators)
  - [Example 4: Unary and Assignment Precedence](#example-4-unary-and-assignment-precedence)
- [Exam Tips](#exam-tips)

## Introduction

Operator precedence is a fundamental concept in Java programming that determines the order in which operators are evaluated in an expression containing multiple operators. When an expression has multiple operators, the Java compiler must decide which operator to evaluate first, second, third, and so on. Without a well-defined precedence rule, expressions like `2 + 3 * 4` would be ambiguous - would it evaluate to `(2 + 3) * 4 = 20` or `2 + (3 * 4) = 14`? Operator precedence provides the answer by establishing a hierarchy of operators based on their binding strength.

Understanding operator precedence is crucial for writing correct Java programs and for debugging expressions that don't produce expected results. In the the syllabus for Object-Oriented Programming with Java (BCS306A), this topic forms the foundation for understanding complex expressions, which are essential for implementing conditional statements, loops, and mathematical computations in Java applications.

## Key Concepts

### What is Operator Precedence?

Operator precedence determines the order in which operators are evaluated in an expression when multiple operators are present. Operators with higher precedence are evaluated first. In Java, there are 15 levels of operator precedence, with parentheses having the highest precedence (level 15), and the assignment operator having the lowest precedence (level 2).

### The Precedence Hierarchy

Java operators follow this general precedence order (from highest to lowest):

1. **Postfix operators**: `expr++`, `expr--` (highest precedence)
2. **Unary operators**: `++expr`, `--expr`, `+`, `-`, `!`, `~`, `(type)`
3. **Multiplicative**: `*`, `/`, `%`
4. **Additive**: `+`, `-`
5. **Shift**: `<<`, `>>`, `>>>`
6. **Relational**: `<`, `>`, `<=`, `>=`, `instanceof`
7. **Equality**: `==`, `!=`
8. **Bitwise AND**: `&`
9. **Bitwise XOR**: `^`
10. **Bitwise OR**: `|`
11. **Logical AND**: `&&`
12. **Logical OR**: `||`
13. **Ternary**: `? :`
14. **Assignment**: `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `^=`, `|=`, `<<=`, `>>=`, `>>>=` (lowest precedence)

### Associativity

When operators have the same precedence, associativity determines the order of evaluation. Most operators in Java are left-to-right associative. However, unary operators, ternary operator, and assignment operators are right-to-left associative.

For example:

- `a + b - c` is evaluated as `(a + b) - c` (left-to-right)
- `a = b = c` is evaluated as `a = (b = c)` (right-to-left)
- `++a++` is evaluated as `++(a++)` (right-to-left, though this is not valid Java)

### Parentheses Override Precedence

Parentheses `()` have the highest precedence and can be used to explicitly specify the order of evaluation. Using parentheses makes code more readable and ensures the intended order of operations, regardless of the default precedence rules.

## Examples

### Example 1: Basic Arithmetic Precedence

**Problem:** Evaluate the following expression:

```java
int result = 10 + 5 * 2;
```

**Solution:**
According to precedence rules, multiplication (`*`) has higher precedence than addition (`+`). So:

- Step 1: Evaluate `5 * 2` first → `10`
- Step 2: Then evaluate `10 + 10` → `20`
- **Final Result: 20**

To add first, we would need parentheses:

```java
int result = (10 + 5) * 2; // Result: 30
```

### Example 2: Complex Expression with Multiple Operators

**Problem:** What is the output of the following code?

```java
int a = 5;
int b = 10;
int c = 2;
int result = a + b * c - a / b % c;
System.out.println(result);
```

**Solution:**
Using precedence rules:

- Multiplicative operators (`*`, `/`, `%`) are evaluated before additive (`+`, `-`)
- Among multiplicative, left-to-right: `/` then `%` then `*`

Step 1: `b * c` → `10 * 2` → `20`
Step 2: `a / b` → `5 / 10` → `0` (integer division)
Step 3: `(a / b) % c` → `0 % 2` → `0`
Step 4: `a + (b * c)` → `5 + 20` → `25`
Step 5: `25 - ((a / b) % c)` → `25 - 0` → `25`

**Output: 25**

### Example 3: Logical and Relational Operators

**Problem:** What is the output?

```java
int x = 5;
int y = 10;
boolean result = x > 3 && y < 20 || x == 5 && y != 10;
System.out.println(result);
```

**Solution:**
Precedence order: Relational → Logical AND → Logical OR

Step 1: Evaluate relational operators:

- `x > 3` → `5 > 3` → `true`
- `y < 20` → `10 < 20` → `true`
- `x == 5` → `5 == 5` → `true`
- `y != 10` → `10 != 10` → `false`

Step 2: Evaluate `&&` (before `||`):

- `x > 3 && y < 20` → `true && true` → `true`
- `x == 5 && y != 10` → `true && false` → `false`

Step 3: Evaluate `||`:

- `true || false` → `true`

**Output: true**

### Example 4: Unary and Assignment Precedence

**Problem:** What is the output?

```java
int a = 5;
int b = a++ + ++a;
System.out.println(b);
```

**Solution:**

- `a++` is post-increment: use value (5), then increment (a becomes 6)
- `++a` is pre-increment: increment first (a becomes 7), then use value (7)

Expression: `a++ + ++a` = `5 + 7` = `12`

**Output: 12**

## Exam Tips

1. **Remember the hierarchy**: Multiplicative (`* / %`) comes before Additive (`+ -`), which comes before Relational (`< > <= >=`), which comes before Equality (`== !=`).

2. **Logical operators order**: `!` (not) → `&&` (and) → `||` (or). Remember that `&&` has higher precedence than `||`.

3. **Assignment is lowest**: The assignment operator `=` has the lowest precedence, meaning it's evaluated almost last (except for the ternary `? :`).

4. **Parentheses are safest**: When in doubt, use parentheses to explicitly define the order. This makes code readable and prevents bugs.

5. **Integer division matters**: Remember that `/` performs integer division when both operands are integers, truncating the decimal part.

6. **Short-circuit evaluation**: For `&&` and `||`, Java uses short-circuit evaluation. If the first operand of `&&` is false, the second is not evaluated. Similarly, if the first operand of `||` is true, the second is not evaluated.

7. **Associativity rules**: Most operators are left-to-right associative. Assignment and ternary operators are right-to-left associative.

8. **Practice with compound expressions**: university exams frequently ask to evaluate complex expressions with multiple operator types. Practice step-by-step evaluation.
