# Comments in Java Programming


## Table of Contents

- [Comments in Java Programming](#comments-in-java-programming)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Single-Line Comments](#1-single-line-comments)
  - [2. Multi-Line Comments](#2-multi-line-comments)
  - [3. Documentation Comments (Javadoc Comments)](#3-documentation-comments-javadoc-comments)
  - [4. Nested Comments](#4-nested-comments)
  - [5. Commenting Best Practices](#5-commenting-best-practices)
- [Examples](#examples)
  - [Example 1: Basic Comment Usage](#example-1-basic-comment-usage)
  - [Example 2: Using Javadoc Comments](#example-2-using-javadoc-comments)
  - [Example 3: Using Comments for Debugging](#example-3-using-comments-for-debugging)
- [Exam Tips](#exam-tips)

## Introduction

Comments are an essential yet often overlooked aspect of programming. In Java, comments are non-executable statements that are completely ignored by the Java compiler. They serve as internal documentation within the source code, helping programmers understand, maintain, and debug their programs effectively. While comments do not affect the program's execution, they play a crucial role in software development, especially in collaborative environments where multiple developers work on the same codebase.

For students studying Object Oriented Programming with Java under the university's 2022 Scheme, understanding comments is fundamental as it forms the basis of writing clean, maintainable, and professional code. This module covers the three types of comments supported by Java: single-line comments, multi-line comments, and documentation comments. Mastery of these comment types is essential not only for academic purposes but also for professional software development practices.

## Key Concepts

### 1. Single-Line Comments

Single-line comments in Java begin with two forward slashes (//) and extend to the end of the current line. They are used for brief explanations or notes about a specific line of code. The Java compiler ignores everything after // until the end of that line.

**Syntax:**

```java
// This is a single-line comment
int age = 25; // This comment describes the variable
```

Single-line comments are commonly used for:

- Adding brief explanations for variable declarations
- Temporarily disabling a line of code during debugging
- Adding quick notes about specific operations

### 2. Multi-Line Comments

Multi-line comments start with a forward slash followed by an asterisk (/_) and end with an asterisk followed by a forward slash (_/). Everything between these delimiters is treated as a comment and is ignored by the compiler. These are useful for longer explanations that span multiple lines.

**Syntax:**

```java
/*
 * This is a multi-line comment.
 * It can span across multiple lines.
 * The compiler ignores everything inside.
 */
int result = a + b;
```

**Important Note:** The opening /_ and closing _/ must appear together. Any text between them is treated as a comment, including the asterisks often placed at the beginning of each line for visual formatting.

### 3. Documentation Comments (Javadoc Comments)

Documentation comments are a special type of multi-line comments that begin with /\*_ and end with _/. These comments are used to generate external documentation automatically using the Javadoc tool. Documentation comments can include special tags starting with @ to provide structured information about classes, methods, fields, and parameters.

**Syntax:**

```java
/**
 * This class demonstrates the usage of documentation comments.
 *
 * @author John Doe
 * @version 1.0
 * @since 2024
 */
public class Student {

 /**
 * This method calculates the average of two numbers.
 *
 * @param num1 the first number
 * @param num2 the second number
 * @return the average of num1 and num2
 */
 public double calculateAverage(int num1, int num2) {
 return (num1 + num2) / 2.0;
 }
}
```

**Common Javadoc Tags:**

- @author: Specifies the author of the class
- @version: Specifies the version of the program
- @param: Describes a parameter of a method
- @return: Describes the return value of a method
- @since: Specifies when the feature was introduced
- @throws: Documents exceptions that a method may throw

### 4. Nested Comments

Unlike some other programming languages, Java does not support nested multi-line comments. Attempting to nest comments will result in compilation errors. This is an important consideration when commenting out sections of code that already contain comments.

**Invalid Example (Will cause error):**

```java
/*
 /* This is invalid and will cause compilation error */
*/
```

### 5. Commenting Best Practices

Writing effective comments is an art that every programmer should master:

1. **Be Concise and Clear:** Comments should explain "why" rather than "what" the code does. The code itself should be self-explanatory for simple operations.

2. **Keep Comments Updated:** Outdated comments are worse than no comments. Always update comments when modifying code.

3. **Use Proper Grammar:** Since comments are part of documentation, maintain proper spelling and grammar.

4. **Avoid Obvious Comments:** Do not state what is evident from the code itself.

5. **Use Documentation Comments for Public APIs:** Always document public classes, methods, and fields that will be used by other developers.

## Examples

### Example 1: Basic Comment Usage

```java
// Program to demonstrate different types of comments
// Author: Student Name
// Date: 2024

public class CommentDemo {
 public static void main(String[] args) {
 /*
 * This program calculates the area of a rectangle
 * It demonstrates the use of single-line and multi-line comments
 */

 double length = 10.5; // Length of the rectangle
 double width = 5.0; // Width of the rectangle

 // Calculate area
 double area = length * width;

 // Display the result
 System.out.println("Area of rectangle: " + area);
 }
}
```

**Output:**

```
Area of rectangle: 52.5
```

### Example 2: Using Javadoc Comments

```java
/**
 * A class representing a Bank Account.
 * This class demonstrates object-oriented programming concepts
 * with proper documentation comments.
 *
 * @author university Student
 * @version 1.0
 * @since January 2024
 */
public class BankAccount {
 private double balance; // Stores the current balance

 /**
 * Constructor to initialize a new bank account.
 *
 * @param initialBalance the initial balance for the account
 */
 public BankAccount(double initialBalance) {
 balance = initialBalance; // Initialize balance
 }

 /**
 * Deposits money into the account.
 *
 * @param amount the amount to be deposited
 */
 public void deposit(double amount) {
 if (amount > 0) {
 balance = balance + amount;
 System.out.println("Deposited: " + amount);
 }
 }

 /**
 * Withdraws money from the account.
 *
 * @param amount the amount to be withdrawn
 */
 public void withdraw(double amount) {
 if (amount > 0 && amount <= balance) {
 balance = balance - amount;
 System.out.println("Withdrawn: " + amount);
 }
 }

 /**
 * Gets the current balance of the account.
 *
 * @return the current balance
 */
 public double getBalance() {
 return balance;
 }
}
```

### Example 3: Using Comments for Debugging

```java
public class DebugExample {
 public static void main(String[] args) {
 int[] numbers = {5, 10, 15, 20, 25};
 int sum = 0;

 // Calculate sum of array elements
 for (int i = 0; i < numbers.length; i++) {
 sum = sum + numbers[i];
 // System.out.println("Current sum: " + sum); // Debug line
 }

 System.out.println("Total sum: " + sum);

 // Uncomment the following line to see array elements
 // for (int num : numbers) {
 // System.out.println(num);
 // }
 }
}
```

## Exam Tips

1. **Remember the Syntax:** Single-line comments use //, multi-line comments use /\* _/, and documentation comments use /\*\* _/.

2. **Javadoc is Executable:** Remember that documentation comments (/\*\* \*/) are used by the Javadoc tool to generate HTML documentation.

3. **Compiler Ignores Comments:** Comments are completely ignored during compilation - they have no effect on program execution or memory.

4. **No Nested Comments:** Java does not support nested multi-line comments, so be careful when commenting out code sections.

5. **Javadoc Tags are Important:** Know the common Javadoc tags like @param, @return, @author, and @version for exam purposes.

6. **Purpose of Comments:** Understand that comments improve code readability, maintainability, and facilitate team collaboration.

7. **Best Practices Matter:** Follow commenting best practices - explain "why" not "what," keep comments updated, and avoid obvious statements.

8. **Variable Declaration Comments:** When adding comments to variable declarations, place them either before the declaration or after on the same line.

9. **Documentation Generation:** Remember that Javadoc comments can be converted to HTML documentation using the javadoc command.

10. **Commenting During Exams:** In practical exams, demonstrating proper commenting shows good programming practice and may earn additional marks.
