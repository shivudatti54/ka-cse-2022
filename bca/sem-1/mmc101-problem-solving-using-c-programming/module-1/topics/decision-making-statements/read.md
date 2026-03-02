# Decision Making Statements in C


## Table of Contents

- [Decision Making Statements in C](#decision-making-statements-in-c)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [The if Statement](#the-if-statement)
  - [The if-else Statement](#the-if-else-statement)
  - [Nested if-else Statements](#nested-if-else-statements)
  - [The else-if Ladder](#the-else-if-ladder)
- [Examples](#examples)
  - [Example 1: Checking if a Number is Positive](#example-1-checking-if-a-number-is-positive)
  - [Example 2: Leap Year Determination](#example-2-leap-year-determination)
  - [Example 3: Calculating Bonus Based on Salary and Experience](#example-3-calculating-bonus-based-on-salary-and-experience)
- [Exam Tips](#exam-tips)

## Introduction

Decision making statements are fundamental constructs in programming that allow the program to execute different blocks of code based on certain conditions. In the C programming language, these statements form the backbone of control flow, enabling developers to create dynamic and responsive software. Without decision making capabilities, a program would simply execute statements sequentially from start to finish, making it impossible to handle varying inputs or create meaningful business logic.

The ability to make decisions based on conditions is what distinguishes a simple calculator from a truly useful application. Whether validating user input, implementing game logic, or controlling industrial machinery, decision making statements are indispensable. In C programming, we primarily use the `if` statement, the `if-else` statement, nested `if-else` constructs, and the else-if ladder to implement these capabilities. Understanding these constructs thoroughly is essential for any programmer, as they are the building blocks for more complex algorithms and program structures.

In the context of the University of Delhi's Computer Science curriculum, decision making statements appear frequently in examinations and form the foundation for understanding subsequent topics like loops and functions. Mastery of these statements is crucial for solving real-world problems programmatically.

## Key Concepts

### The if Statement

The `if` statement is the simplest form of decision making in C. It evaluates a condition (an expression that evaluates to true or false) and executes a block of code only if the condition is true. The syntax follows a specific pattern where the condition must be enclosed in parentheses, and the code to be executed upon a true condition must be placed within curly braces if it consists of multiple statements.

The general syntax is: `if (condition) { statements; }`

When the condition evaluates to a non-zero value, it is considered true, and the statements within the block are executed. If the condition evaluates to zero (false), the entire block is skipped, and program execution continues to the next statement after the `if` block. It is important to note that the condition must be a scalar expression that can be evaluated to a numeric value.

In C, any non-zero value is treated as true, including negative numbers. This is a common source of bugs for beginners who might accidentally write conditions that always evaluate to true. The condition can involve relational operators (`<`, `>`, `<=`, `>=`, `==`, `!=`), logical operators (`&&`, `||`, `!`), or any expression that evaluates to an integer.

### The if-else Statement

The `if-else` statement extends the simple `if` statement by providing an alternative block of code to execute when the condition is false. This allows the program to take one of two paths based on the evaluation of a single condition. The `else` keyword is paired with an `if` and provides the default action when the `if` condition is not satisfied.

The syntax is: `if (condition) { statements for true; } else { statements for false; }`

This construct is particularly useful when we need to handle both positive and negative cases. For example, checking whether a number is even or odd, validating login credentials, or determining whether a student has passed or failed an examination. The `else` block ensures that exactly one of the two paths will always be executed, making the program behavior predictable and well-defined.

It is worth noting that the `else` clause does not have a condition of its own; it simply acts as the fallback for the preceding `if` condition. Both the `if` and `else` blocks can contain multiple statements, but they must be properly enclosed in curly braces to form compound statements.

### Nested if-else Statements

When we need to check multiple conditions in sequence, we can nest `if-else` statements within each other. This allows for more complex decision making where the evaluation of one condition depends on the result of a previous condition. Nested `if-else` structures can become deeply complicated, so it is important to maintain proper indentation and logical organization.

The general form involves placing an entire `if-else` construct inside either the `if` block or the `else` block of an outer `if-else` statement. Each level of nesting adds another dimension to the decision-making process. For instance, determining the quadrant of a Cartesian point requires checking both x and y coordinates, which naturally leads to a nested structure.

However, excessive nesting (often referred to as the "arrowhead" anti-pattern) makes code difficult to read and maintain. Modern programming practices suggest limiting nesting depth or using other control structures when possible. In examination contexts, students should be careful to properly match `if` and `else` keywords, as C uses a rule where each `else` is associated with the nearest unmatched `if` in the same block.

### The else-if Ladder

The else-if ladder (also called the else-if chain) is a specific pattern of nested `if-else` statements used when we need to check multiple mutually exclusive conditions in sequence. Instead of deeply nesting conditions, we chain multiple `else if` clauses, each with its own condition. The conditions are evaluated from top to bottom, and the first condition that evaluates to true causes its corresponding block to execute.

The syntax follows: `if (condition1) { statements1; } else if (condition2) { statements2; } else if (condition3) { statements3; } else { default statements; }`

This construct is particularly useful for implementing range checks, menu-driven programs, and grading systems. For example, assigning letter grades based on percentage marks or determining the shipping cost based on weight both benefit from the else-if ladder structure. The final `else` clause is optional but highly recommended as it handles the case when none of the conditions are met, preventing silent failures.

## Examples

### Example 1: Checking if a Number is Positive

Problem: Write a C program to check whether a given integer is positive, negative, or zero.

```c
#include <stdio.h>

int main() {
    int num;
    
    printf("Enter an integer: ");
    scanf("%d", &num);
    
    if (num > 0) {
        printf("The number is POSITIVE.\n");
    }
    else if (num < 0) {
        printf("The number is NEGATIVE.\n");
    }
    else {
        printf("The number is ZERO.\n");
    }
    
    return 0;
}
```

Step-by-step solution: First, we declare an integer variable `num` to store the user input. The `printf` function prompts the user, and `scanf` reads the input into the variable. The else-if ladder then checks three mutually exclusive conditions: whether `num` is greater than zero, less than zero, or neither (which means zero). Only one of these three branches will execute because the conditions are mutually exclusive and cover all possible integer values.

### Example 2: Leap Year Determination

Problem: Write a program to determine whether a given year is a leap year.

```c
#include <stdio.h>

int main() {
    int year;
    
    printf("Enter a year: ");
    scanf("%d", &year);
    
    if (year % 4 == 0) {
        if (year % 100 == 0) {
            if (year % 400 == 0) {
                printf("%d is a LEAP YEAR.\n", year);
            }
            else {
                printf("%d is NOT A LEAP YEAR.\n", year);
            }
        }
        else {
            printf("%d is a LEAP YEAR.\n", year);
        }
    }
    else {
        printf("%d is NOT A LEAP YEAR.\n", year);
    }
    
    return 0;
}
```

Step-by-step solution: A leap year is divisible by 4, but century years (divisible by 100) are only leap years if they are also divisible by 400. This requires nested if-else logic. The outer `if` checks divisibility by 4. If true, we enter the nested structure to check century year rules. The inner nesting checks divisibility by 100, and the innermost check handles the 400-year exception. This demonstrates how nested conditions can represent complex business logic.

### Example 3: Calculating Bonus Based on Salary and Experience

Problem: An employee receives a bonus based on their salary and years of experience. If salary is above Rs 50,000 and experience is more than 5 years, bonus is 20%. If salary is above Rs 30,000 and experience is more than 3 years, bonus is 10%. Otherwise, no bonus.

```c
#include <stdio.h>

int main() {
    float salary, bonus = 0;
    int experience;
    
    printf("Enter salary (Rs): ");
    scanf("%f", &salary);
    
    printf("Enter years of experience: ");
    scanf("%d", &experience);
    
    if (salary > 50000 && experience > 5) {
        bonus = salary * 0.20;
        printf("Bonus: Rs %.2f (20%%)\n", bonus);
    }
    else if (salary > 30000 && experience > 3) {
        bonus = salary * 0.10;
        printf("Bonus: Rs %.2f (10%%)\n", bonus);
    }
    else {
        printf("No bonus applicable.\n");
    }
    
    return 0;
}
```

Step-by-step solution: We use two float variables for salary and bonus, and one integer for experience. The else-if ladder checks the conditions in order of higher benefit (20% first, then 10%). The logical AND operator (`&&`) ensures both conditions must be true. The `%` symbol in the printf requires `%%` to print a literal percent sign. This example demonstrates how decision making can be combined with arithmetic operations.

## Exam Tips

1. Remember that in C, the condition in an `if` statement must evaluate to a scalar value. Any non-zero value is treated as true, including negative numbers.

2. The `else` keyword always associates with the nearest unmatched `if` in the same block. Use curly braces to clarify association when writing nested conditions.

3. When comparing two values for equality, use `==` (double equals). A common mistake is using `=` (assignment operator) which assigns rather than compares.

4. In examination questions, carefully trace through all possible input scenarios to verify your logic covers all cases including boundary conditions.

5. The else-if ladder stops at the first true condition. Therefore, the order of conditions matters for efficiency and correctness.

6. Always initialize variables before using them in conditions. Using uninitialized variables leads to undefined behavior.

7. For complex conditions, consider breaking them into smaller parts using logical operators or intermediate boolean variables to improve readability.

8. Don't forget that integer division in C truncates decimal values. When comparing calculated values, be aware of potential precision issues.

9. The final `else` clause in an else-if ladder is optional but recommended to handle unexpected cases or as a default action.

10. Practice writing decision making code with proper indentation, as messy code often leads to logical errors that are hard to debug during examinations.