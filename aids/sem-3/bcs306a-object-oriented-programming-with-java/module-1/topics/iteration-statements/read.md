# Iteration Statements in Java


## Table of Contents

- [Iteration Statements in Java](#iteration-statements-in-java)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. While Loop](#1-while-loop)
  - [2. Do-While Loop](#2-do-while-loop)
  - [3. For Loop](#3-for-loop)
  - [4. Enhanced For Loop (For-Each)](#4-enhanced-for-loop-for-each)
  - [5. Break and Continue Statements](#5-break-and-continue-statements)
  - [6. Nested Loops](#6-nested-loops)
- [Examples](#examples)
  - [Example 1: While Loop - Sum of Digits](#example-1-while-loop---sum-of-digits)
  - [Example 2: For Loop - Pattern Printing](#example-2-for-loop---pattern-printing)
  - [Example 3: Enhanced For Loop - Array Traversal](#example-3-enhanced-for-loop---array-traversal)
- [Exam Tips](#exam-tips)

## Introduction

Iteration statements, commonly known as loops, are fundamental constructs in Java programming that allow a set of instructions to be executed repeatedly based on certain conditions. These statements are essential for processing collections of data, performing repetitive calculations, and implementing algorithms that require multiple iterations. In the context of object-oriented programming with Java, understanding iteration statements is crucial for manipulating data structures, implementing business logic, and creating efficient algorithms.

Java provides four primary iteration constructs: the while loop, the do-while loop, the for loop, and the enhanced for-each loop. Each of these has specific use cases, advantages, and performance characteristics that make them suitable for different programming scenarios. Mastery of these statements is not only important for academic success in university examinations but also forms the foundation for developing real-world Java applications. The ability to choose the appropriate loop type and implement it correctly is a fundamental skill that every Java programmer must possess.

## Key Concepts

### 1. While Loop

The while loop is a pre-test iteration statement that executes a block of code repeatedly as long as a specified condition remains true. The condition is evaluated before each iteration, meaning if the condition is false initially, the loop body may never execute.

**Syntax:**

```java
while (condition) {
 // statements to be executed
}
```

The condition must be a boolean expression. The loop continues iterating until the condition becomes false. It is essential to ensure that the loop will eventually terminate by modifying the condition within the loop body, otherwise, an infinite loop will occur.

### 2. Do-While Loop

The do-while loop is a post-test iteration statement that differs from the while loop in that it guarantees the loop body executes at least once before checking the condition. This is because the condition is evaluated after the execution of the loop body.

**Syntax:**

```java
do {
 // statements to be executed
} while (condition);
```

The do-while loop is particularly useful when the loop body must be executed at least once, such as in menu-driven programs where the user must be prompted at least once before validating input.

### 3. For Loop

The for loop is the most commonly used iteration statement in Java. It provides a compact way to iterate over a range of values or a specific number of times. The for loop consists of three parts: initialization, condition, and increment/decrement.

**Syntax:**

```java
for (initialization; condition; increment/decrement) {
 // statements to be executed
}
```

- **Initialization:** Executed once at the beginning, typically used to initialize a counter variable.
- **Condition:** Evaluated before each iteration; if true, the loop body executes.
- **Increment/Decrement:** Executed after each iteration, typically used to update the counter variable.

### 4. Enhanced For Loop (For-Each)

The enhanced for loop was introduced in Java 5 to simplify iteration over arrays and collections. It eliminates the need for explicit counter management and index handling.

**Syntax:**

```java
for (data_type variable : array_or_collection) {
 // statements to be executed
}
```

This loop automatically iterates through all elements in the specified array or collection without requiring explicit index manipulation.

### 5. Break and Continue Statements

**Break Statement:** Used to terminate the loop prematurely. When encountered, the loop immediately exits and control transfers to the statement following the loop.

**Continue Statement:** Used to skip the current iteration and proceed with the next iteration. When encountered, the remaining statements in the current iteration are skipped, and the loop proceeds with the next cycle.

### 6. Nested Loops

A loop can contain another loop within its body, forming nested loops. This is commonly used for multi-dimensional array traversal, pattern printing, and matrix operations. The total number of iterations in nested loops equals the product of iterations of each loop.

## Examples

### Example 1: While Loop - Sum of Digits

**Problem:** Write a Java program to calculate the sum of digits of a given number using a while loop.

**Solution:**

```java
import java.util.Scanner;

public class SumOfDigits {
 public static void main(String[] args) {
 Scanner sc = new Scanner(System.in);
 System.out.print("Enter a number: ");
 int number = sc.nextInt();

 int sum = 0;
 int temp = Math.abs(number); // Handle negative numbers

 while (temp > 0) {
 int digit = temp % 10; // Extract last digit
 sum += digit; // Add to sum
 temp = temp / 10; // Remove last digit
 }

 System.out.println("Sum of digits: " + sum);
 sc.close();
 }
}
```

**Step-by-step execution for number 456:**

- Iteration 1: digit = 456 % 10 = 6, sum = 6, temp = 456 / 10 = 45
- Iteration 2: digit = 45 % 10 = 5, sum = 11, temp = 45 / 10 = 4
- Iteration 3: digit = 4 % 10 = 4, sum = 15, temp = 4 / 10 = 0
- Loop terminates when temp becomes 0
- Output: Sum of digits = 15

### Example 2: For Loop - Pattern Printing

**Problem:** Write a Java program to print the following pattern using a for loop:

```
*
* *
* * *
* * * *
* * * * *
```

**Solution:**

```java
public class PatternDemo {
 public static void main(String[] args) {
 int rows = 5;

 for (int i = 1; i <= rows; i++) { // Outer loop for rows
 for (int j = 1; j <= i; j++) { // Inner loop for columns
 System.out.print("* ");
 }
 System.out.println(); // Move to next line
 }
 }
}
```

**Explanation:**

- The outer loop controls the number of rows (5 iterations)
- The inner loop controls the number of stars in each row
- For i=1: inner loop runs 1 time → \*
- For i=2: inner loop runs 2 times → \* \*
- And so on until i=5

### Example 3: Enhanced For Loop - Array Traversal

**Problem:** Write a Java program to find the maximum element in an array using the enhanced for loop.

**Solution:**

```java
public class FindMaximum {
 public static void main(String[] args) {
 int[] numbers = {23, 45, 12, 67, 89, 34, 56};

 int max = numbers[0]; // Assume first element is maximum

 // Using enhanced for loop
 for (int num : numbers) {
 if (num > max) {
 max = num;
 }
 }

 System.out.println("Maximum element: " + max);
 }
}
```

**Step-by-step execution:**

- Initialize max = 23 (first element)
- num = 23: 23 > 23? No → max remains 23
- num = 45: 45 > 23? Yes → max = 45
- num = 12: 12 > 45? No → max remains 45
- num = 67: 67 > 45? Yes → max = 67
- num = 89: 89 > 67? Yes → max = 89
- num = 34: 34 > 89? No → max remains 89
- num = 56: 56 > 89? No → max remains 89
- Output: Maximum element: 89

## Exam Tips

1. **Understand the difference between while and do-while:** Remember that while is a pre-test loop (condition checked before execution) while do-while is a post-test loop (guaranteed at least one execution).

2. **Always update loop control variables:** Failing to update the loop variable results in an infinite loop, which is a common programming error.

3. **Choose the appropriate loop type:** Use for loop when the number of iterations is known, while loop when the number of iterations is unknown, and do-while when at least one execution is required.

4. **Break vs Continue:** Remember that break terminates the entire loop, while continue skips only the current iteration.

5. **Enhanced for loop limitations:** The enhanced for loop cannot be used when you need to modify the array elements or when you need the index value.

6. **Nested loop complexity:** In nested loops, the time complexity is generally the product of iterations of each loop level.

7. **Common pattern recognition:** For pattern problems, identify the number of rows (outer loop) and elements per row (inner loop) to determine loop structure.
