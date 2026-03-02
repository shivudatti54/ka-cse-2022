# Jump Statements in Java

## Table of Contents

- [Jump Statements in Java](#jump-statements-in-java)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Break Statement](#1-break-statement)
  - [2. Continue Statement](#2-continue-statement)
  - [3. Return Statement](#3-return-statement)
  - [4. Labeled Statements](#4-labeled-statements)
- [Examples](#examples)
  - [Example 1: Finding First Prime Number](#example-1-finding-first-prime-number)
  - [Example 2: Skip Even Numbers](#example-2-skip-even-numbers)
  - [Example 3: Matrix Search with Labeled Break](#example-3-matrix-search-with-labeled-break)
- [Exam Tips](#exam-tips)

## Introduction

Jump statements are fundamental control flow mechanisms in Java that allow programmers to alter the normal sequential execution of a program. These statements enable you to transfer control from one point to another within a block of code, providing greater control over loops, switch statements, and method execution. In Java, there are three primary jump statements: break, continue, and return. Additionally, the throw statement can be considered a jump mechanism for exception handling.

Understanding jump statements is crucial for writing efficient and controlled Java programs. They are extensively used in loop constructs to exit prematurely, skip iterations, or transfer control to specific labeled statements. Without jump statements, programmers would struggle to handle complex control flow scenarios, especially when dealing with nested loops or error conditions. The proper use of these statements leads to cleaner, more readable code and prevents unnecessary iterations or computations.

## Key Concepts

### 1. Break Statement

The break statement is used to terminate the execution of a loop (for, while, do-while) or a switch statement immediately. When encountered, control jumps to the statement immediately following the loop or switch block.

**Syntax:**

```java
break;
```

**Types of break:**

- **Unlabeled break:** Terminates the innermost loop or switch
- **Labeled break:** Terminates the outer loop specified by the label

**Unlabeled break example:**

```java
for (int i = 1; i <= 10; i++) {
 if (i == 5) {
 break; // exits loop when i equals 5
 }
 System.out.println(i);
}
// Output: 1 2 3 4
```

**Labeled break example:**

```java
outerLoop:
for (int i = 1; i <= 3; i++) {
 for (int j = 1; j <= 3; j++) {
 if (i == 2 && j == 2) {
 break outerLoop; // exits both loops
 }
 System.out.println("i=" + i + ", j=" + j);
 }
}
```

### 2. Continue Statement

The continue statement skips the current iteration of a loop and proceeds with the next iteration. Unlike break which terminates the loop entirely, continue only skips the remaining statements in the current iteration.

**Syntax:**

```java
continue;
```

**Types of continue:**

- **Unlabeled continue:** Skips to the next iteration of the innermost loop
- **Labeled continue:** Skips to the next iteration of the outer loop specified by the label

**Unlabeled continue example:**

```java
for (int i = 1; i <= 5; i++) {
 if (i == 3) {
 continue; // skips printing when i equals 3
 }
 System.out.println(i);
}
// Output: 1 2 4 5
```

**Labeled continue example:**

```java
outerLoop:
for (int i = 1; i <= 3; i++) {
 for (int j = 1; j <= 3; j++) {
 if (j == 2) {
 continue outerLoop; // skips to next iteration of outer loop
 }
 System.out.println("i=" + i + ", j=" + j);
 }
}
```

### 3. Return Statement

The return statement is used to exit from a method and optionally return a value to the calling method. It terminates the execution of the method immediately, and control returns to the caller.

**Syntax:**

```java
return; // for void methods
return value; // for methods returning a value
```

**Examples:**

```java
// Method returning void
public void display() {
 System.out.println("Hello");
 return; // optional in void methods
}

// Method returning int
public int findMax(int a, int b) {
 if (a > b) {
 return a;
 } else {
 return b;
 }
}
```

### 4. Labeled Statements

Labels are identifiers followed by a colon that can be applied to statements. They are primarily used with break and continue to control the flow in nested loops.

**Syntax:**

```java
labelName:
for (int i = 0; i < n; i++) {
 // loop body
}
```

## Examples

### Example 1: Finding First Prime Number

**Problem:** Write a program to find the first prime number in a given range using break statement.

```java
public class PrimeFinder {
 public static void main(String[] args) {
 int start = 10;
 int end = 50;

 for (int num = start; num <= end; num++) {
 boolean isPrime = true;

 for (int i = 2; i <= num / 2; i++) {
 if (num % i == 0) {
 isPrime = false;
 break; // no need to check further
 }
 }

 if (isPrime) {
 System.out.println("First prime number: " + num);
 break; // exit loop after finding first prime
 }
 }
 }
}
// Output: First prime number: 11
```

**Explanation:** The outer loop iterates through numbers from 10 to 50. For each number, we check if it's prime by dividing it by numbers from 2 to num/2. If we find a divisor, we use break to exit the inner loop (no need to continue checking). Once we find a prime number, we use break to exit the outer loop completely.

### Example 2: Skip Even Numbers

**Problem:** Write a program to print odd numbers from 1 to 10 using continue statement.

```java
public class OddNumbers {
 public static void main(String[] args) {
 System.out.println("Odd numbers from 1 to 10:");

 for (int i = 1; i <= 10; i++) {
 if (i % 2 == 0) {
 continue; // skip even numbers
 }
 System.out.print(i + " ");
 }
 }
}
// Output: Odd numbers from 1 to 10:
// 1 3 5 7 9
```

**Explanation:** The continue statement checks if the number is even. If it is, the remaining statements in that iteration are skipped, and the loop proceeds to the next iteration. This efficiently prints only odd numbers.

### Example 3: Matrix Search with Labeled Break

**Problem:** Search for a specific element in a 2D matrix and exit both loops when found.

```java
public class MatrixSearch {
 public static void main(String[] args) {
 int[][] matrix = {
 {1, 2, 3},
 {4, 5, 6},
 {7, 8, 9}
 };
 int search = 7;
 boolean found = false;

 searchLoop:
 for (int i = 0; i < matrix.length; i++) {
 for (int j = 0; j < matrix[i].length; j++) {
 if (matrix[i][j] == search) {
 System.out.println("Found " + search + " at position [" + i + "][" + j + "]");
 found = true;
 break searchLoop; // exits both loops
 }
 }
 }

 if (!found) {
 System.out.println("Element not found");
 }
 }
}
// Output: Found 7 at position [2][0]
```

**Explanation:** Using a labeled break, we can exit from nested loops simultaneously. When the element is found, break searchLoop terminates both the inner and outer loops immediately, which is more efficient than using a flag variable.

## Exam Tips

1. **Remember the key difference:** break terminates the loop entirely, while continue skips only the current iteration.

2. **Labeled vs Unlabeled:** In nested loops, unlabeled break/continue only affects the innermost loop. Use labels to control outer loops.

3. **Return statement placement:** return immediately exits the method; no code after return in the same block will execute.

4. **Break in switch:** Remember that break is essential in switch cases to prevent fall-through (unless fall-through is intentional).

5. **Continue with if:** continue is always associated with an if statement; without it, it would skip all iterations unconditionally.

6. **Void methods:** In void methods, return is optional at the end but useful for early exit based on conditions.

7. **Label syntax:** Labels must be placed before the loop definition and followed by a colon (:).

8. **Avoid infinite loops:** Be careful with break and continue to ensure loops don't become infinite due to incorrect placement.
