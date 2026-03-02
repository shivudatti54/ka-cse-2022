# Operators and Expressions

## Introduction

Operators and expressions are fundamental building blocks of programming languages. They allow us to perform operations on data and control the flow of our programs. In this topic, we will explore the different types of operators and expressions in programming, their syntax, and their usage.

Operators are symbols used to perform operations on operands, which are values or variables. Expressions are combinations of operators and operands that evaluate to a value. Understanding how to use operators and expressions effectively is crucial for writing efficient and effective code.

In this topic, we will cover the basics of operators and expressions, including arithmetic, assignment, comparison, logical, and bitwise operators. We will also discuss the order of operations, type casting, and operator overloading.

## Key Concepts

### Arithmetic Operators

Arithmetic operators are used to perform mathematical operations on operands. The following are the arithmetic operators in C:

* `+` (addition)
* `-` (subtraction)
* `*` (multiplication)
* `/` (division)
* `%` (modulus)
* `++` (increment)
* `--` (decrement)

### Assignment Operators

Assignment operators are used to assign values to variables. The following are the assignment operators in C:

* `=` (assignment)
* `+=` (addition assignment)
* `-=` (subtraction assignment)
* `*=` (multiplication assignment)
* `/=` (division assignment)
* `%=` (modulus assignment)

### Comparison Operators

Comparison operators are used to compare operands. The following are the comparison operators in C:

* `==` (equal to)
* `!=` (not equal to)
* `>` (greater than)
* `<` (less than)
* `>=` (greater than or equal to)
* `<=` (less than or equal to)

### Logical Operators

Logical operators are used to perform logical operations on operands. The following are the logical operators in C:

* `&&` (logical and)
* `||` (logical or)
* `!` (logical not)

### Bitwise Operators

Bitwise operators are used to perform bitwise operations on operands. The following are the bitwise operators in C:

* `&` (bitwise and)
* `|` (bitwise or)
* `^` (bitwise xor)
* `~` (bitwise not)
* `<<` (left shift)
* `>>` (right shift)

### Order of Operations

The order of operations is the order in which operators are evaluated when there are multiple operators in an expression. The following is the order of operations in C:

1. Parentheses
2. Postfix operators (`++`, `--`)
3. Unary operators (`+`, `-`, `!`, `~`)
4. Multiplication and division operators (`*`, `/`, `%`)
5. Addition and subtraction operators (`+`, `-`)
6. Shift operators (`<<`, `>>`)
7. Comparison operators (`==`, `!=`, `>`, `<`, `>=` , `<=`)
8. Logical operators (`&&`, `||`)
9. Assignment operators (`=`, `+=`, `-=`, `*=`, `/=`, `%=`)

### Type Casting

Type casting is the process of converting a value from one data type to another. There are two types of type casting in C:

* Implicit type casting: This is done automatically by the compiler.
* Explicit type casting: This is done manually by the programmer using the cast operator.

### Operator Overloading

Operator overloading is the process of redefining the behavior of an operator for a user-defined data type. This allows us to use operators with our own data types.

## Examples

### Example 1: Arithmetic Operators

```c
#include <stdio.h>

int main() {
    int a = 10;
    int b = 5;

    printf("a + b = %d\n", a + b);
    printf("a - b = %d\n", a - b);
    printf("a * b = %d\n", a * b);
    printf("a / b = %d\n", a / b);
    printf("a %% b = %d\n", a % b);

    return 0;
}
```

### Example 2: Assignment Operators

```c
#include <stdio.h>

int main() {
    int a = 10;

    a += 5;
    printf("a = %d\n", a);

    a -= 3;
    printf("a = %d\n", a);

    a *= 2;
    printf("a = %d\n", a);

    a /= 2;
    printf("a = %d\n", a);

    return 0;
}
```

### Example 3: Comparison Operators

```c
#include <stdio.h>

int main() {
    int a = 10;
    int b = 5;

    printf("a == b: %d\n", a == b);
    printf("a != b: %d\n", a != b);
    printf("a > b: %d\n", a > b);
    printf("a < b: %d\n", a < b);
    printf("a >= b: %d\n", a >= b);
    printf("a <= b: %d\n", a <= b);

    return 0;
}
```

## Exam Tips

1. Understand the order of operations and how it affects the evaluation of expressions.
2. Know the difference between implicit and explicit type casting.
3. Be able to explain the behavior of operator overloading.
4. Understand how to use arithmetic, assignment, comparison, logical, and bitwise operators.
5. Be able to write expressions using operators and operands.
6. Understand how to use parentheses to group expressions and change the order of operations.
7. Know how to use the cast operator to perform explicit type casting.