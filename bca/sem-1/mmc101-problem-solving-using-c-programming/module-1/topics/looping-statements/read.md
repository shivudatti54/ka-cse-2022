# Looping Statements in C Programming


## Table of Contents

- [Looping Statements in C Programming](#looping-statements-in-c-programming)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [The While Loop](#the-while-loop)
  - [The Do-While Loop](#the-do-while-loop)
  - [The For Loop](#the-for-loop)
  - [Nested Loops](#nested-loops)
  - [Loop Control Statements](#loop-control-statements)
  - [Infinite Loops](#infinite-loops)
- [Examples](#examples)
  - [Example 1: Sum of First N Natural Numbers](#example-1-sum-of-first-n-natural-numbers)
  - [Example 2: Menu-Driven Program Using Do-While](#example-2-menu-driven-program-using-do-while)
  - [Example 3: Multiplication Table Using Nested For Loop](#example-3-multiplication-table-using-nested-for-loop)
  - [Example 4: Pattern Printing Using Continue](#example-4-pattern-printing-using-continue)
- [Exam Tips](#exam-tips)

## Introduction

Looping statements are fundamental constructs in C programming that allow a set of instructions to be executed repeatedly based on certain conditions. In problem-solving scenarios, we frequently encounter situations where the same operation needs to be performed multiple times - whether it's calculating the sum of a series, processing each element of an array, or displaying a menu until the user exits. Without loops, programmers would be forced to write the same code statement multiple times, making programs inefficient, lengthy, and difficult to maintain.

The C language provides three primary looping constructs: the while loop, the do-while loop, and the for loop. Each loop type serves specific purposes and is suitable for different programming scenarios. Understanding when and how to use each loop type is essential for writing efficient C programs. Additionally, C provides loop control statements like break, continue, and goto that modify the flow of loop execution, giving programmers fine-grained control over iterative processes.

Mastering loops is crucial for DU Computer Science students because iterative problem-solving forms the backbone of algorithmic thinking. Whether you are implementing search algorithms, sorting techniques, or mathematical computations, loops will be your primary tool. This topic also carries significant weight in internal assessments and end-semester examinations, making thorough understanding imperative for academic success.

## Key Concepts

### The While Loop

The while loop is an entry-controlled loop that executes a block of code as long as a specified condition remains true. The condition is evaluated before each iteration, meaning if the condition is false initially, the loop body may not execute at all.

Syntax:
```c
while (condition) {
    // statements to be executed
    // update statement (crucial to avoid infinite loop)
}
```

The loop consists of three essential components: initialization (done before the loop), condition (checked before each iteration), and update (modifies the loop variable to eventually terminate the loop).

### The Do-While Loop

The do-while loop is an exit-controlled loop that guarantees the loop body executes at least once, regardless of the condition. This is its distinguishing feature from the while loop. The condition is evaluated after each iteration, making it suitable for menu-driven programs where user input must be processed at least once.

Syntax:
```c
do {
    // statements to be executed
    // update statement
} while (condition);
```

Note the the semicolon after the while condition - this is a common source of errors if omitted.

### The For Loop

The for loop is the most versatile and commonly used iteration construct in C. It combines initialization, condition checking, and updating into a single line, making it ideal for scenarios where the number of iterations is known beforehand.

Syntax:
```c
for (initialization; condition; update) {
    // statements to be executed
}
```

All three components are optional - you can write an infinite for loop as `for(;;)` or omit sections based on requirements.

### Nested Loops

When one loop is placed inside another loop, it is called a nested loop. Nested loops are essential for problems involving matrices, pattern generation, and multi-dimensional data processing. The total number of iterations equals the product of iterations of all loops.

Example structure:
```c
for (i = 0; i < n; i++) {
    for (j = 0; j < m; j++) {
        // inner loop statements
    }
}
```

### Loop Control Statements

**Break Statement:** Immediately terminates the innermost loop and transfers control to the statement following the loop. It is commonly used in search algorithms and switch statements.

**Continue Statement:** Skips the remaining statements in the current iteration and transfers control to the next iteration of the loop. It is useful when specific iterations need to be bypassed based on certain conditions.

**Goto Statement:** Transfers control to a labeled statement. While C permits its use, it is generally discouraged because it makes code difficult to read and maintain. Modern programming practices recommend avoiding goto except in specific error-handling scenarios.

### Infinite Loops

An infinite loop runs indefinitely because the termination condition never becomes false. This can occur due to programming errors or intentional design (such as embedded systems waiting for input). Common causes include forgetting the update statement or setting an incorrect condition.

Example of intentional infinite loop:
```c
while (1) {
    // statements
}
```

## Examples

### Example 1: Sum of First N Natural Numbers

**Problem:** Write a C program to calculate the sum of the first N natural numbers using a while loop.

**Solution:**
```c
#include <stdio.h>

int main() {
    int n, i = 1, sum = 0;
    
    printf("Enter the value of N: ");
    scanf("%d", &n);
    
    while (i <= n) {
        sum = sum + i;
        i++;
    }
    
    printf("Sum of first %d natural numbers = %d\n", n, sum);
    
    return 0;
}
```

**Step-by-step execution for n = 5:**
- Initial: i = 1, sum = 0
- Iteration 1: i = 1 ≤ 5, sum = 0 + 1 = 1, i = 2
- Iteration 2: i = 2 ≤ 5, sum = 1 + 2 = 3, i = 3
- Iteration 3: i = 3 ≤ 5, sum = 3 + 3 = 6, i = 4
- Iteration 4: i = 4 ≤ 5, sum = 6 + 4 = 10, i = 5
- Iteration 5: i = 5 ≤ 5, sum = 10 + 5 = 15, i = 6
- Iteration 6: i = 6 > 5, loop terminates
- Output: 15

### Example 2: Menu-Driven Program Using Do-While

**Problem:** Create a simple calculator using a do-while loop that displays a menu and performs operations until the user chooses to exit.

**Solution:**
```c
#include <stdio.h>

int main() {
    int choice;
    float a, b, result;
    
    do {
        printf("\n--- Simple Calculator ---\n");
        printf("1. Addition\n");
        printf("2. Subtraction\n");
        printf("3. Multiplication\n");
        printf("4. Division\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        
        if (choice >= 1 && choice <= 4) {
            printf("Enter two numbers: ");
            scanf("%f %f", &a, &b);
        }
        
        switch (choice) {
            case 1:
                result = a + b;
                printf("Result: %.2f\n", result);
                break;
            case 2:
                result = a - b;
                printf("Result: %.2f\n", result);
                break;
            case 3:
                result = a * b;
                printf("Result: %.2f\n", result);
                break;
            case 4:
                if (b != 0) {
                    result = a / b;
                    printf("Result: %.2f\n", result);
                } else {
                    printf("Error: Division by zero!\n");
                }
                break;
            case 5:
                printf("Exiting calculator. Goodbye!\n");
                break;
            default:
                printf("Invalid choice! Please try again.\n");
        }
    } while (choice != 5);
    
    return 0;
}
```

**Key features:** The do-while ensures the menu displays at least once. The loop continues until choice equals 5.

### Example 3: Multiplication Table Using Nested For Loop

**Problem:** Display multiplication tables from 1 to n using nested loops.

**Solution:**
```c
#include <stdio.h>

int main() {
    int n, i, j;
    
    printf("Enter the value of N: ");
    scanf("%d", &n);
    
    for (i = 1; i <= n; i++) {
        printf("\nMultiplication Table of %d:\n", i);
        for (j = 1; j <= 10; j++) {
            printf("%d x %d = %d\n", i, j, i * j);
        }
    }
    
    return 0;
}
```

**Execution flow:** For each value of i from 1 to n, the inner loop executes completely from j = 1 to j = 10. This produces n tables, each with 10 multiplications.

### Example 4: Pattern Printing Using Continue

**Problem:** Print numbers from 1 to 10 but skip multiples of 3 using the continue statement.

**Solution:**
```c
#include <stdio.h>

int main() {
    int i;
    
    printf("Numbers from 1 to 10 (excluding multiples of 3):\n");
    
    for (i = 1; i <= 10; i++) {
        if (i % 3 == 0) {
            continue;  // Skip this iteration
        }
        printf("%d ", i);
    }
    
    return 0;
}
```

**Output:** 1 2 4 5 7 8 10

The continue statement causes the loop to skip printing when i is divisible by 3, but the loop continues to the next iteration.

## Exam Tips

1. **Difference between while and do-while:** Remember that while is entry-controlled (condition checked first) while do-while is exit-controlled (executes at least once). This distinction frequently appears in exam questions.

2. **Semicolon placement:** A common mistake is placing a semicolon after the while statement in while and for loops, creating an empty loop body. For example, `while(i <= 10);` creates an infinite loop.

3. **Loop termination:** Always ensure your loop has a termination condition that will eventually become false. Missing update statements lead to infinite loops.

4. **For loop components are optional:** In exams, you may be asked to identify valid for loop syntax. Remember all three parts (initialization, condition, update) are optional, and you can even have an infinite for loop.

5. **Break vs Continue:** Understand that break terminates the entire loop, while continue skips only the current iteration. This difference is crucial for tracing program output.

6. **Tracing loop outputs:** Practice tracing programs with nested loops. Questions often ask for the output of given code segments, requiring you to track iteration values carefully.

7. **Choosing the right loop:** Use for loop when the number of iterations is known, while loop when it's unknown but condition-based, and do-while when you need at least one execution.

8. **Nested loop complexity:** When asked about the number of executions in nested loops, multiply the iteration counts of each loop level.