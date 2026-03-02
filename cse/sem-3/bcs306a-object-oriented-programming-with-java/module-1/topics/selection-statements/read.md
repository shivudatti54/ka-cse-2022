# Selection Statements in Java

## Table of Contents

- [Selection Statements in Java](#selection-statements-in-java)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Simple if Statement](#1-simple-if-statement)
  - [2. if-else Statement](#2-if-else-statement)
  - [3. else-if Ladder (Nested if-else)](#3-else-if-ladder-nested-if-else)
  - [4. Switch Statement](#4-switch-statement)
  - [5. Ternary Operator (Conditional Operator)](#5-ternary-operator-conditional-operator)
- [Examples](#examples)
  - [Example 1: Leap Year Check](#example-1-leap-year-check)
  - [Example 2: Calculator using Switch](#example-2-calculator-using-switch)
  - [Example 3: Traffic Light Simulation](#example-3-traffic-light-simulation)
- [Exam Tips](#exam-tips)

## Introduction

Selection statements are fundamental control structures in Java that allow programmers to execute different blocks of code based on certain conditions. These statements form the backbone of decision-making in programming, enabling applications to respond dynamically to user inputs and varying runtime conditions. In object-oriented programming with Java, understanding selection statements is crucial as they control the flow of execution and determine which code paths are followed during program execution.

In the context of the university's BCS306A curriculum, selection statements are covered in Module 1 as they represent foundational concepts that students must master before moving to more complex topics like loops, methods, and object-oriented concepts. Java provides two primary categories of selection statements: the if statement (including if-else and nested if-else) and the switch statement. Each of these serves different use cases and offers various levels of flexibility for programmers. This chapter explores all these constructs in detail, with emphasis on syntax, behavior, and practical applications that are essential for university examinations and practical programming scenarios.

The ability to make decisions based on conditions is what distinguishes a program from a mere list of instructions. Whether it's validating user input, implementing game logic, or making business decisions in software, selection statements are ubiquitous in real-world applications. Mastery of these constructs not only helps in passing university exams but also builds the analytical thinking required for solving complex programming problems.

## Key Concepts

### 1. Simple if Statement

The simplest form of selection statement in Java is the `if` statement. It executes a block of code only when a specified condition evaluates to `true`. If the condition is `false`, the entire block is skipped, and the program continues with the next statement after the if block.

The syntax follows:

```java
if (condition) {
 // statements to execute if condition is true
}
```

The condition must be a boolean expression—meaning it must evaluate to either `true` or `false`. Java does not allow numeric values as conditions (unlike C/C++), which is an important safety feature. The curly braces are optional when the if block contains only a single statement, but using braces is highly recommended for code clarity and to avoid common errors.

Example:

```java
int age = 20;
if (age >= 18) {
 System.out.println("Eligible to vote");
}
```

In this example, the message "Eligible to vote" will be printed only when age is 18 or greater.

### 2. if-else Statement

The `if-else` statement extends the simple if statement by providing an alternative block of code that executes when the condition is false. This allows programs to handle both true and false outcomes of a condition, making it possible to implement binary decisions.

The syntax is:

```java
if (condition) {
 // statements if condition is true
} else {
 // statements if condition is false
}
```

The else clause cannot exist without a corresponding if statement. The else block executes only when the if condition evaluates to false. This construct is essential for implementing validation logic, password checking, and numerous other scenarios where two distinct paths must be followed.

Example:

```java
int number = -5;
if (number > 0) {
 System.out.println("Positive number");
} else {
 System.out.println("Non-positive number");
}
```

This code will output "Non-positive number" since -5 is not greater than 0.

### 3. else-if Ladder (Nested if-else)

When multiple conditions need to be checked in sequence, the else-if ladder provides a clean way to handle such scenarios. This construct allows programmers to test multiple conditions in order, executing the block corresponding to the first true condition. If no condition is true, the final else block (if present) is executed.

The syntax structure:

```java
if (condition1) {
 // statements for condition1
} else if (condition2) {
 // statements for condition2
} else if (condition3) {
 // statements for condition3
} else {
 // statements if all conditions are false
}
```

Important characteristics:

- Conditions are evaluated from top to bottom
- Only one block executes—the first one with a true condition
- The final else is optional but provides a default action
- Once a condition is true, remaining conditions are not evaluated

Example for grade calculation:

```java
int marks = 85;
char grade;

if (marks >= 90) {
 grade = 'S';
} else if (marks >= 80) {
 grade = 'A';
} else if (marks >= 70) {
 grade = 'B';
} else if (marks >= 60) {
 grade = 'C';
} else if (marks >= 50) {
 grade = 'D';
} else {
 grade = 'F';
}

System.out.println("Grade: " + grade); // Output: Grade: A
```

### 4. Switch Statement

The switch statement provides a multi-way branch mechanism that tests a variable against multiple values. It offers an alternative to long else-if chains when the decision depends on comparing a single variable against multiple constant values. Prior to Java 14, switch was only a statement, but from Java 14 onwards, it can also be used as an expression.

#### Traditional switch statement (pre-Java 14):

```java
switch (expression) {
 case value1:
 // statements
 break;
 case value2:
 // statements
 break;
 default:
 // default statements
}
```

Key points about switch:

- The expression must evaluate to `char`, `byte`, `short`, `int`, `String`, or enum types
- Each case value must be a compile-time constant
- The `break` statement is crucial to prevent fall-through (continuing to the next case)
- The `default` case is optional and executes when no matching case is found
- Multiple cases can be grouped together without break for common handling

Example:

```java
int day = 3;
String dayName;

switch (day) {
 case 1:
 dayName = "Sunday";
 break;
 case 2:
 dayName = "Monday";
 break;
 case 3:
 dayName = "Tuesday";
 break;
 case 4:
 dayName = "Wednesday";
 break;
 case 5:
 dayName = "Thursday";
 break;
 case 6:
 dayName = "Friday";
 break;
 case 7:
 dayName = "Saturday";
 break;
 default:
 dayName = "Invalid day";
}

System.out.println(dayName); // Output: Tuesday
```

#### Modern switch (Java 14+):

Java 14 introduced switch expressions that allow using switch as an expression that returns a value. This simplifies code and reduces boilerplate:

```java
int day = 3;
String dayName = switch (day) {
 case 1 -> "Sunday";
 case 2 -> "Monday";
 case 3 -> "Tuesday";
 case 4 -> "Wednesday";
 case 5 -> "Thursday";
 case 6 -> "Friday";
 case 7 -> "Saturday";
 default -> "Invalid day";
};

System.out.println(dayName); // Output: Tuesday
```

This arrow syntax eliminates the need for break statements and provides a more concise way to write switch logic. Multiple cases can be combined using commas:

```java
String result = switch (month) {
 case 12, 1, 2 -> "Winter";
 case 3, 4, 5 -> "Spring";
 case 6, 7, 8 -> "Summer";
 case 9, 10, 11 -> "Autumn";
 default -> "Invalid month";
};
```

### 5. Ternary Operator (Conditional Operator)

The ternary operator `?:` is a compact form of the if-else statement. It takes three operands and provides a shorthand way of making binary decisions. While not technically a selection statement, it's often grouped with them due to its conditional nature.

Syntax:

```java
variable = (condition) ? valueIfTrue : valueIfFalse;
```

Example:

```java
int a = 10, b = 20;
int max = (a > b) ? a : b;
System.out.println("Maximum: " + max); // Output: Maximum: 20
```

The ternary operator is particularly useful for simple conditional assignments and can be nested, though deep nesting reduces readability.

## Examples

### Example 1: Leap Year Check

Problem: Write a Java program to check whether a given year is a leap year or not.

Solution:

```java
import java.util.Scanner;

public class LeapYearCheck {
 public static void main(String[] args) {
 Scanner sc = new Scanner(System.in);
 System.out.print("Enter a year: ");
 int year = sc.nextInt();

 // Leap year conditions:
 // 1. Divisible by 4 AND not divisible by 100
 // 2. OR divisible by 400

 if (year % 400 == 0) {
 System.out.println(year + " is a leap year");
 } else if (year % 100 == 0) {
 System.out.println(year + " is not a leap year");
 } else if (year % 4 == 0) {
 System.out.println(year + " is a leap year");
 } else {
 System.out.println(year + " is not a leap year");
 }

 sc.close();
 }
}
```

Step-by-step explanation:

1. First check: If year is divisible by 400, it's a leap year (handles century years like 2000)
2. Second check: If year is divisible by 100 but not 400, it's not a leap year (like 1900)
3. Third check: If year is divisible by 4 but not 100, it's a leap year (like 2020)
4. Final else: All other years are not leap years

### Example 2: Calculator using Switch

Problem: Create a simple calculator that performs basic arithmetic operations.

Solution:

```java
import java.util.Scanner;

public class SimpleCalculator {
 public static void main(String[] args) {
 Scanner sc = new Scanner(System.in);

 System.out.println("Simple Calculator");
 System.out.println("=================");
 System.out.print("Enter first number: ");
 double num1 = sc.nextDouble();

 System.out.print("Enter operator (+, -, *, /): ");
 char operator = sc.next().charAt(0);

 System.out.print("Enter second number: ");
 double num2 = sc.nextDouble();

 double result;

 switch (operator) {
 case '+':
 result = num1 + num2;
 System.out.println("Result: " + num1 + " + " + num2 + " = " + result);
 break;
 case '-':
 result = num1 - num2;
 System.out.println("Result: " + num1 + " - " + num2 + " = " + result);
 break;
 case '*':
 result = num1 * num2;
 System.out.println("Result: " + num1 + " * " + num2 + " = " + result);
 break;
 case '/':
 if (num2 != 0) {
 result = num1 / num2;
 System.out.println("Result: " + num1 + " / " + num2 + " = " + result);
 } else {
 System.out.println("Error: Division by zero is not allowed");
 }
 break;
 default:
 System.out.println("Error: Invalid operator");
 }

 sc.close();
 }
}
```

### Example 3: Traffic Light Simulation

Problem: Write a program that displays a message based on the traffic light color.

Solution using modern switch expression (Java 14+):

```java
public class TrafficLight {
 public static void main(String[] args) {
 String color = "red";

 String message = switch (color.toLowerCase()) {
 case "red" -> "STOP - Wait for the signal to change";
 case "yellow" -> "SLOW DOWN - Get ready to stop";
 case "green" -> "GO - You can proceed";
 default -> "Invalid color - Please check the traffic light";
 };

 System.out.println(message);
 }
}
```

Output: STOP - Wait for the signal to change

## Exam Tips

1. **Remember that Java conditions must be boolean**: Unlike C/C++, you cannot use integer variables directly in conditions. Writing `if (x = 5)` will cause a compilation error—this is actually a safety feature in Java.

2. **Don't forget break statements in switch**: In traditional switch statements, omitting break causes fall-through, where execution continues to the next case. This is a common source of bugs in examination answers.

3. **Switch expression vs statement**: From Java 14+, understand both forms. The expression form returns a value and uses arrows (→), while the statement form uses colons and requires break.

4. **Operator precedence in conditions**: Remember that relational operators (>, <, >=, <=) have higher precedence than equality operators (==, !=), which have higher precedence than logical operators (&&, ||).

5. **Use braces consistently**: Even for single statements in if/switch, using braces improves readability and prevents subtle bugs. Examiners appreciate clean, well-formatted code.

6. **Case sensitivity**: String comparisons in switch are case-sensitive. Use `.toLowerCase()` or `.toUpperCase()` when case-insensitive matching is needed.

7. **Default placement**: In switch statements, default can be placed anywhere (not necessarily at the end), but conventionally it's placed at the end for readability.

8. **Avoid deep nesting**: Deeply nested if-else structures are hard to read and maintain. Consider refactoring using switch or methods when nesting exceeds 2-3 levels.
