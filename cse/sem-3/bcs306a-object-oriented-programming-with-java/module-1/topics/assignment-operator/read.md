# Assignment Operators in Java

## Table of Contents

- [Assignment Operators in Java](#assignment-operators-in-java)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Simple Assignment Operator (=)](#1-simple-assignment-operator-)
  - [2. Compound Assignment Operators](#2-compound-assignment-operators)
  - [3. Assignment with Type Casting](#3-assignment-with-type-casting)
  - [4. Chained Assignment](#4-chained-assignment)
  - [5. Assignment in Object References](#5-assignment-in-object-references)
  - [6. Operator Precedence and Associativity](#6-operator-precedence-and-associativity)
- [Examples](#examples)
  - [Example 1: Simple and Compound Assignment](#example-1-simple-and-compound-assignment)
  - [Example 2: Chained Assignment](#example-2-chained-assignment)
  - [Example 3: Reference Assignment in OOP](#example-3-reference-assignment-in-oop)
- [Exam Tips](#exam-tips)

## Introduction

Assignment operators are fundamental constructs in Java that allow programmers to assign values to variables. They form the backbone of variable initialization and value modification in any Java program. In the context of Object-Oriented Programming with Java, understanding assignment operators is crucial as they interact with object references, primitive data types, and contribute to writing efficient, concise code.

The assignment operator (=) is the most basic operator in Java, yet it serves as the foundation for more complex operations. Beyond the simple assignment, Java provides compound assignment operators that combine arithmetic or bitwise operations with assignment in a single step. These operators not only make code more readable but also enable the Java compiler to optimize bytecode generation. This module explores the various assignment operators available in Java, their syntax, behavior, and practical applications in OOP scenarios.

## Key Concepts

### 1. Simple Assignment Operator (=)

The simple assignment operator is denoted by a single equals sign (=) and is used to assign a value to a variable. The syntax is:

```java
variable = expression;
```

The right-hand side (RHS) can be a literal, a variable, an expression, or a method call. The assignment operator has right-to-left associativity, meaning the expression on the right is evaluated first, and then the result is assigned to the variable on the left.

**Important Rules:**

- The variable on the left must be a declared variable (or a valid lvalue)
- The type of the expression must be compatible with the variable's type
- Primitive types are assigned by value (copying the actual value)
- Object references are assigned by reference (copying the memory address)

### 2. Compound Assignment Operators

Compound assignment operators combine an arithmetic or bitwise operation with assignment in a single statement. The general syntax is:

```java
variable operator= expression;
```

This is equivalent to:

```java
variable = variable operator expression;
```

**Types of Compound Assignment Operators:**

| Operator | Name                      | Example  | Equivalent To |
| -------- | ------------------------- | -------- | ------------- |
| +=       | Addition assignment       | a += 5   | a = a + 5     |
| -=       | Subtraction assignment    | a -= 3   | a = a - 3     |
| \*=      | Multiplication assignment | a \*= 2  | a = a \* 2    |
| /=       | Division assignment       | a /= 4   | a = a / 4     |
| %=       | Modulus assignment        | a %= 7   | a = a % 7     |
| &=       | Bitwise AND assignment    | a &= b   | a = a & b     |
| \|=      | Bitwise OR assignment     | a \|= b  | a = a \| b    |
| ^=       | Bitwise XOR assignment    | a ^= b   | a = a ^ b     |
| <<=      | Left shift assignment     | a <<= 2  | a = a << 2    |
| >>=      | Right shift assignment    | a >>= 2  | a = a >> 2    |
| >>>=     | Unsigned right shift      | a >>>= 2 | a = a >>> 2   |

### 3. Assignment with Type Casting

When assigning a value of one type to a variable of another type, explicit casting may be required:

```java
double d = 10.5;
int i = (int) d; // Explicit cast - i becomes 10
```

For assignment between compatible types (like int to long), implicit casting occurs automatically:

```java
int i = 100;
long l = i; // Implicit widening conversion
```

### 4. Chained Assignment

Java allows chained assignment where multiple variables are assigned the same value in a single statement:

```java
int a, b, c;
a = b = c = 10; // All three variables get value 10
```

This works because the assignment operator returns the assigned value, which becomes the right-hand operand for the next assignment.

### 5. Assignment in Object References

Understanding reference assignment is crucial in OOP:

```java
class Student {
 String name;
}

Student s1 = new Student();
s1.name = "John";

Student s2 = s1; // s2 now references the same object as s1
s2.name = "Mike"; // Modifies the shared object

System.out.println(s1.name); // Prints: Mike
```

### 6. Operator Precedence and Associativity

Assignment operators have low precedence, evaluated after most other operations. They have right-to-left associativity:

```java
int x = 10;
int y = 20;
int z = 30;

x = y = z; // Evaluated as x = (y = z)
// z = 30, y = 30, x = 30
```

## Examples

### Example 1: Simple and Compound Assignment

**Problem:** Write a Java program demonstrating various assignment operations.

```java
public class AssignmentDemo {
 public static void main(String[] args) {
 // Simple assignment
 int a = 10;
 System.out.println("Initial value: " + a);

 // Compound assignment operators
 a += 5; // a = a + 5 = 10 + 5 = 15
 System.out.println("After a += 5: " + a);

 a -= 3; // a = a - 3 = 15 - 3 = 12
 System.out.println("After a -= 3: " + a);

 a *= 2; // a = a * 2 = 12 * 2 = 24
 System.out.println("After a *= 2: " + a);

 a /= 4; // a = a / 4 = 24 / 4 = 6
 System.out.println("After a /= 4: " + a);

 a %= 5; // a = a % 5 = 6 % 5 = 1
 System.out.println("After a %= 5: " + a);
 }
}
```

**Output:**

```
Initial value: 10
After a += 5: 15
After a -= 3: 12
After a *= 2: 24
After a /= 4: 6
After a %= 5: 1
```

### Example 2: Chained Assignment

**Problem:** Demonstrate chained assignment with different data types.

```java
public class ChainedAssignment {
 public static void main(String[] args) {
 int x, y, z;

 // Chained assignment - right to left evaluation
 x = y = z = 100;
 System.out.println("x = " + x + ", y = " + y + ", z = " + z);

 // Using with expressions
 double d1, d2, d3;
 d1 = d2 = d3 = 15.5 * 2;
 System.out.println("d1 = " + d1 + ", d2 = " + d2 + ", d3 = " + d3);

 // Mixing with other operators
 int a = 10;
 int b = 20;
 int c = 30;
 a = b = c; // c=30 assigned to b, then b=30 assigned to a
 System.out.println("a = " + a + ", b = " + b + ", c = " + c);
 }
}
```

**Output:**

```
x = 100, y = 100, z = 100
d1 = 31.0, d2 = 31.0, d3 = 31.0
a = 30, b = 30, c = 30
```

### Example 3: Reference Assignment in OOP

**Problem:** Demonstrate the difference between primitive and reference assignment.

```java
class Box {
 int length = 10;
 int width = 5;
}

public class ReferenceAssignment {
 public static void main(String[] args) {
 // Primitive assignment - copy by value
 int num1 = 25;
 int num2 = num1; // num2 gets a copy of num1's value
 num2 = 50; // Changing num2 doesn't affect num1

 System.out.println("num1 = " + num1); // 25
 System.out.println("num2 = " + num2); // 50

 // Reference assignment - copy by reference
 Box box1 = new Box();
 Box box2 = box1; // box2 references the same object

 System.out.println("Before: box1.area = " + (box1.length * box1.width));

 box2.length = 20; // Modifying box2 affects the shared object

 System.out.println("After: box1.area = " + (box1.length * box1.width));
 System.out.println("After: box2.area = " + (box2.length * box2.width));

 // Creating a true copy
 Box box3 = new Box();
 box3.length = box1.length;
 box3.width = box1.width;

 box3.length = 30;
 System.out.println("After modifying box3:");
 System.out.println("box1.area = " + (box1.length * box1.width));
 System.out.println("box3.area = " + (box3.length * box3.width));
 }
}
```

**Output:**

```
num1 = 25
num2 = 50
Before: box1.area = 50
After: box1.area = 100
After: box2.area = 100
After modifying box3:
box1.area = 100
box3.area = 150
```

## Exam Tips

1. **Remember the Assignment Return Value:** The assignment operator returns the assigned value, which enables chained assignments and expressions like `System.out.println(x = 10)`.

2. **Compound Operators Save Evaluation:** `x += 5` is more efficient than `x = x + 5` because the variable `x` is evaluated only once.

3. **Reference vs. Value Assignment:** In exams, always distinguish between primitive assignments (copies value) and object reference assignments (shares the same object).

4. **Operator Precedence:** Assignment operators have the lowest precedence among operators, evaluated after arithmetic and other operations.

5. **Type Compatibility:** Be careful with implicit and explicit casting in assignments. Narrowing conversions require explicit casting and may cause data loss.

6. **Right-to-Left Associativity:** Remember that assignment evaluates from right to left. In `a = b = c = 10`, all variables get the value 10.

7. **Compound Operators with Different Types:** When using compound operators, automatic type promotion occurs. For example, `int x = 5; x += 5.5;` results in x = 10 (truncated).

8. **Common Mistake - Confusion between = and ==:** In Java, `=` is assignment and `==` is comparison. Using `=` in a condition (like `if(x = 5)`) causes a compile error in Java (unlike C/C++).
