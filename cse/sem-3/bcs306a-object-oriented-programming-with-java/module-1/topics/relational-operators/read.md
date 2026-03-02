# Relational Operators in Java

## Table of Contents

- [Relational Operators in Java](#relational-operators-in-java)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [What Are Relational Operators?](#what-are-relational-operators)
  - [The Six Relational Operators in Java](#the-six-relational-operators-in-java)
  - [Important Characteristics and Rules](#important-characteristics-and-rules)
  - [Using Relational Operators in Control Structures](#using-relational-operators-in-control-structures)
- [Examples](#examples)
  - [Example 1: Grade Classification](#example-1-grade-classification)
  - [Example 2: Leap Year Checker](#example-2-leap-year-checker)
  - [Example 3: Password Validation](#example-3-password-validation)
- [Exam Tips](#exam-tips)

## Introduction

Relational operators are fundamental components of the Java programming language that allow programmers to compare values and make decisions based on those comparisons. These operators form the backbone of conditional statements, loops, and decision-making structures in any Java application. In the context of Object-Oriented Programming with Java (BCS306A), understanding relational operators is essential because they enable the implementation of business logic, validation checks, and flow control mechanisms.

Relational operators in Java always return a boolean value (true or false), making them ideal for use in if-else statements, while loops, for loops, and other control structures. Whether you are validating user input, sorting data, or implementing complex algorithms, relational operators will be your go-to tools for comparing values. This module covers all six relational operators in Java: equals to (==), not equals to (!=), greater than (>), less than (<), greater than or equals to (>=), and less than or equals to (<=).

## Key Concepts

### What Are Relational Operators?

Relational operators are binary operators that compare two operands and return a boolean result. They are called "relational" because they establish a relationship between two values. In Java, these operators work with primitive data types including integers (byte, short, int, long), floating-point numbers (float, double), characters (char), and even booleans (though with specific rules).

The general syntax for using relational operators is:

```
operand1 relational_operator operand2
```

For example: `a > b`, `x == y`, `price <= 100`

### The Six Relational Operators in Java

**1. Equal To (==)**
The equality operator (==) checks if two values are equal. It returns true if both operands have the same value, and false otherwise. For primitive types, it compares the actual values. For reference types, it compares memory addresses (references), unless the class overrides the equals() method.

Example:

```java
int x = 10;
int y = 20;
System.out.println(x == y); // Output: false

int z = 10;
System.out.println(x == z); // Output: true
```

**2. Not Equal To (!=)**
The not equal operator (!=) checks if two values are different. It returns true if the operands have different values, and false if they are equal.

Example:

```java
int a = 5;
int b = 10;
System.out.println(a != b); // Output: true

String s1 = "Hello";
String s2 = "Hello";
System.out.println(s1 != s2); // Output: false (same reference)
```

**3. Greater Than (>)**
The greater than operator (>) checks if the left operand is greater than the right operand. It returns true if the left value is strictly greater than the right value.

Example:

```java
int marks = 85;
System.out.println(marks > 50); // Output: true

double temperature = 25.5;
System.out.println(temperature > 30.0); // Output: false
```

**4. Less Than (<)**
The less than operator (<) checks if the left operand is less than the right operand. It returns true if the left value is strictly less than the right value.

Example:

```java
int age = 17;
System.out.println(age < 18); // Output: true

char grade = 'B';
System.out.println(grade < 'A'); // Output: false (ASCII values: B=66, A=65)
```

**5. Greater Than or Equal To (>=)**
The greater than or equal to operator (>=) returns true if the left operand is either greater than or equal to the right operand.

Example:

```java
int score = 75;
System.out.println(score >= 60); // Output: true

int value = 50;
System.out.println(value >= 100); // Output: false
```

**6. Less Than or Equal To (<=)**
The less than or equal to operator (<=) returns true if the left operand is either less than or equal to the right operand.

Example:

```java
int quantity = 10;
System.out.println(quantity <= 5); // Output: false

int balance = 1000;
System.out.println(balance <= 1000); // Output: true
```

### Important Characteristics and Rules

**1. Boolean Comparison Rules**
In Java, boolean values can only be compared using == and != operators. You cannot use >, <, >=, or <= with boolean values. This is a common source of errors for beginners.

```java
boolean flag1 = true;
boolean flag2 = false;
System.out.println(flag1 == flag2); // Output: false
System.out.println(flag1 != flag2); // Output: true
// System.out.println(flag1 > flag2); // COMPILE ERROR
```

**2. Character Comparisons**
When comparing characters, Java uses Unicode/ASCII values. Each character has a numeric value that allows mathematical operations.

```java
char c1 = 'A'; // ASCII 65
char c2 = 'a'; // ASCII 97
System.out.println(c1 < c2); // Output: true (65 < 97)
System.out.println('0' < '9'); // Output: true (48 < 57)
```

**3. Floating-Point Comparisons**
When comparing floating-point numbers, be cautious about precision issues. Due to how floating-point numbers are stored, direct equality comparisons may produce unexpected results.

```java
double d1 = 0.1 + 0.2;
double d2 = 0.3;
System.out.println(d1 == d2); // Output: false (precision issue)
System.out.println(d1 - d2 < 0.0001); // Better approach for floating-point
```

**4. Reference Comparison vs Value Comparison**
For objects (Strings, wrapper classes), == compares references (memory addresses), not the actual content. Use the equals() method for content comparison.

```java
String s1 = new String("Java");
String s2 = new String("Java");
System.out.println(s1 == s2); // Output: false (different objects)
System.out.println(s1.equals(s2)); // Output: true (same content)
```

### Using Relational Operators in Control Structures

Relational operators are extensively used in control flow statements:

**If-Else Statements:**

```java
int age = 20;
if (age >= 18) {
 System.out.println("Eligible to vote");
} else {
 System.out.println("Not eligible");
}
```

**While Loops:**

```java
int count = 0;
while (count < 5) {
 System.out.println("Count: " + count);
 count++;
}
```

**For Loops:**

```java
for (int i = 0; i <= 10; i++) {
 System.out.println(i);
}
```

**Ternary Operator:**

```java
int a = 10, b = 20;
int max = (a > b) ? a : b; // max = 20
```

## Examples

### Example 1: Grade Classification

Problem: Write a Java program to classify student grades based on marks.

```java
import java.util.Scanner;

public class GradeClassification {
 public static void main(String[] args) {
 Scanner sc = new Scanner(System.in);
 System.out.println("Enter marks (0-100): ");
 int marks = sc.nextInt();

 if (marks >= 90 && marks <= 100) {
 System.out.println("Grade: S");
 } else if (marks >= 80 && marks < 90) {
 System.out.println("Grade: A");
 } else if (marks >= 70 && marks < 80) {
 System.out.println("Grade: B");
 } else if (marks >= 60 && marks < 70) {
 System.out.println("Grade: C");
 } else if (marks >= 50 && marks < 60) {
 System.out.println("Grade: D");
 } else if (marks >= 0 && marks < 50) {
 System.out.println("Grade: F");
 } else {
 System.out.println("Invalid marks entered");
 }
 sc.close();
 }
}
```

### Example 2: Leap Year Checker

Problem: Determine if a year is a leap year using relational operators.

```java
import java.util.Scanner;

public class LeapYearCheck {
 public static void main(String[] args) {
 Scanner sc = new Scanner(System.in);
 System.out.print("Enter a year: ");
 int year = sc.nextInt();

 // A year is leap year if:
 // Divisible by 4 AND (divisible by 100 OR not divisible by 400)
 if (year % 4 == 0) {
 if (year % 100 == 0) {
 if (year % 400 == 0) {
 System.out.println(year + " is a leap year");
 } else {
 System.out.println(year + " is not a leap year");
 }
 } else {
 System.out.println(year + " is a leap year");
 }
 } else {
 System.out.println(year + " is not a leap year");
 }
 sc.close();
 }
}
```

### Example 3: Password Validation

Problem: Validate password strength using relational operators.

```java
import java.util.Scanner;

public class PasswordValidation {
 public static void main(String[] args) {
 Scanner sc = new Scanner(System.in);
 System.out.print("Enter password: ");
 String password = sc.nextLine();

 int length = password.length();
 boolean hasUpper = false;
 boolean hasLower = false;
 boolean hasDigit = false;

 for (int i = 0; i < length; i++) {
 char ch = password.charAt(i);
 if (ch >= 'A' && ch <= 'Z') hasUpper = true;
 if (ch >= 'a' && ch <= 'z') hasLower = true;
 if (ch >= '0' && ch <= '9') hasDigit = true;
 }

 // Validation checks using relational operators
 if (length >= 8) {
 System.out.println("Length: OK");
 } else {
 System.out.println("Length: Too short (minimum 8 characters)");
 }

 if (hasUpper && hasLower && hasDigit) {
 System.out.println("Password strength: Strong");
 } else {
 System.out.println("Password strength: Weak (add uppercase, lowercase, and digits)");
 }
 sc.close();
 }
}
```

## Exam Tips

1. **Remember All Six Operators**: The six relational operators are == (equals), != (not equals), > (greater than), < (less than), >= (greater than or equals), and <= (less than or equals).

2. **Always Returns Boolean**: Relational operators always return a boolean value (true or false), never integers or other types.

3. **Avoid Comparing Floating-Points Directly**: Due to precision issues, use a tolerance range when comparing float/double values instead of using ==.

4. **Reference vs Value for Objects**: When comparing objects (especially Strings), use .equals() method for content comparison, not == which compares memory addresses.

5. **Boolean Can Use Only == and !=**: Remember that boolean variables can only be compared using == and != operators, not >, <, >=, or <=.

6. **Character Comparisons Use ASCII**: When comparing characters, Java uses their ASCII/Unicode values. For example, 'A' < 'a' returns true because ASCII of 'A' is 65 and 'a' is 97.

7. **Chaining is Not Allowed**: Unlike some other languages, Java does not allow chaining relational operators like `a < b < c`. You must use logical operators: `a < b && b < c`.

8. **Common Mistake with = and ==**: A frequent exam error is using assignment operator (=) instead of equality operator (==). Always use == for comparison.

9. **Precedence**: Relational operators have lower precedence than arithmetic operators but higher than logical operators like && and ||.

10. **Null Pointer Exception**: When comparing objects with ==, ensure they are not null to avoid NullPointerException.
