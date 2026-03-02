# Type Conversion and Casting in Java

## Table of Contents

- [Type Conversion and Casting in Java](#type-conversion-and-casting-in-java)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Implicit Type Conversion (Widening)](#1-implicit-type-conversion-widening)
  - [2. Explicit Type Conversion (Narrowing/Casting)](#2-explicit-type-conversion-narrowingcasting)
  - [3. Type Conversion in Arithmetic Expressions](#3-type-conversion-in-arithmetic-expressions)
  - [4. Reference Type Casting](#4-reference-type-casting)
  - [5. String to Numeric Conversion](#5-string-to-numeric-conversion)
- [Examples](#examples)
  - [Example 1: Implicit and Explicit Conversion](#example-1-implicit-and-explicit-conversion)
  - [Example 2: Reference Type Casting with instanceof](#example-2-reference-type-casting-with-instanceof)
  - [Example 3: String to Number Conversion with Error Handling](#example-3-string-to-number-conversion-with-error-handling)
- [Exam Tips](#exam-tips)

## Introduction

Type conversion and casting are fundamental concepts in Java that allow programmers to convert data from one type to another. In the context of object-oriented programming with Java, understanding these mechanisms is crucial for writing robust and error-free code. Type conversion becomes particularly important when dealing with inheritance hierarchies, polymorphism, and data type compatibility in expressions.

In Java, type conversion can be performed in two ways: implicitly (automatically by the compiler) and explicitly (manually by the programmer through casting). The Java compiler performs implicit conversions when there is no loss of data, such as converting a smaller integer type to a larger one. However, when converting from a larger type to a smaller type, or when converting between unrelated types, explicit casting becomes necessary. This topic forms the foundation for understanding more advanced OOP concepts like polymorphism and type safety in Java applications.

## Key Concepts

### 1. Implicit Type Conversion (Widening)

Implicit type conversion, also known as widening conversion, occurs automatically when a smaller data type is assigned to a larger data type. The Java compiler handles this conversion automatically because there is no possibility of data loss. The hierarchy of widening for primitive types follows a specific order where each type can be safely converted to any type above it in the hierarchy.

The widening conversion order in Java is: byte → short → char → int → long → float → double. When converting from byte to short, short to char, or any other step up this hierarchy, the conversion happens automatically without any special syntax. For example, when assigning an int value to a double variable, Java automatically converts the int to double. This automatic conversion is particularly useful in arithmetic expressions where operands of different types are mixed.

```java
int num = 100;
long longNum = num; // Implicit conversion from int to long
double doubleNum = longNum; // Implicit conversion from long to double
```

### 2. Explicit Type Conversion (Narrowing/Casting)

Explicit type conversion, also called narrowing or casting, is required when converting from a larger data type to a smaller data type, or when converting between incompatible types. This conversion carries the risk of data loss and must be performed manually by the programmer using the cast operator. The syntax involves placing the target type in parentheses before the value to be converted.

When casting from double to int, for example, the decimal portion is simply truncated, which can lead to significant data loss. Similarly, converting from long to short may result in unexpected results if the value exceeds the range of the target type. It is the programmer's responsibility to ensure that the value being cast is within the acceptable range of the target type to avoid unexpected results.

```java
double pi = 3.14159;
int intPi = (int) pi; // Result: 3 (decimal portion truncated)

long bigNumber = 1000;
short smallNumber = (short) bigNumber; // Works if within range
```

### 3. Type Conversion in Arithmetic Expressions

Java automatically promotes operands in arithmetic expressions to larger types to prevent data loss during calculations. This is known as binary numeric promotion. When performing arithmetic operations on operands of different types, Java converts both operands to the larger type before performing the operation. This automatic promotion ensures that the result of arithmetic operations maintains precision as much as possible.

If one operand is double, the other is converted to double. Similarly, if one operand is float, the other becomes float, and the same logic applies to long and integer types. Understanding this automatic promotion is essential for predicting the data type of the result and avoiding unexpected type conversions in complex expressions.

```java
int a = 10;
double b = 5.5;
double result = a + b; // a is promoted to double, result is double

byte b1 = 10;
byte b2 = 20;
int result2 = b1 + b2; // Both promoted to int, result is int
```

### 4. Reference Type Casting

In object-oriented Java, casting also applies to reference types (objects). Reference type casting allows conversion between related classes in an inheritance hierarchy. Upcasting converts a subclass reference to a superclass reference, while downcasting converts a superclass reference back to a subclass reference. Upcasting is always safe and can be done implicitly, while downcasting requires explicit casting and may throw a ClassCastException at runtime if the object is not actually an instance of the target class.

The instanceof operator is used to check if an object is an instance of a particular class or interface before performing a downcast. This operator helps prevent runtime errors by allowing programmers to verify the type before attempting the cast. Proper use of instanceof combined with casting enables polymorphic behavior and type-safe operations in Java applications.

```java
class Animal { }
class Dog extends Animal { }

Animal animal = new Dog(); // Upcasting (implicit)
Dog dog = (Dog) animal; // Downcasting (explicit)

if (animal instanceof Dog) {
 Dog d = (Dog) animal; // Safe downcast after instanceof check
}
```

### 5. String to Numeric Conversion

Java provides wrapper classes and methods for converting String values to primitive types. The parseXxx() methods of wrapper classes such as Integer, Double, and Boolean are commonly used for this purpose. These methods parse the string and return the corresponding primitive value. If the string cannot be parsed into the target type, a NumberFormatException is thrown at runtime.

The valueOf() method returns a wrapper object instead of a primitive value. Both approaches are valid and the choice depends on whether a primitive or wrapper object is needed. These conversions are essential when reading user input or processing data from files, as input is typically received as strings.

```java
String str = "123";
int num = Integer.parseInt(str); // Returns primitive int
Integer numObj = Integer.valueOf(str); // Returns Integer object

String str2 = "3.14";
double pi = Double.parseDouble(str2);
```

## Examples

### Example 1: Implicit and Explicit Conversion

**Problem:** Demonstrate type conversion with the following scenario: A program needs to calculate the average of three numbers: 10, 20, and 30, stored in byte variables, and display the result as a double.

**Solution:**

```java
public class TypeConversionDemo {
 public static void main(String[] args) {
 // Step 1: Declare byte variables
 byte a = 10;
 byte b = 20;
 byte c = 30;

 // Step 2: Implicit conversion happens automatically
 // When adding bytes, they are promoted to int
 int sum = a + b + c; // a, b, c promoted to int during addition

 // Step 3: Calculate average - implicit conversion to double
 double average = sum / 3.0; // sum promoted to double for division

 // Display result
 System.out.println("Sum: " + sum);
 System.out.println("Average: " + average);
 }
}
```

**Output:**

```
Sum: 60
Average: 20.0
```

### Example 2: Reference Type Casting with instanceof

**Problem:** Create a program demonstrating safe downcasting using instanceof operator with an inheritance hierarchy of Vehicle, Car, and Bicycle classes.

**Solution:**

```java
class Vehicle {
 void drive() {
 System.out.println("Vehicle is driving");
 }
}

class Car extends Vehicle {
 @Override
 void drive() {
 System.out.println("Car is driving");
 }

 void playMusic() {
 System.out.println("Playing music in car");
 }
}

class Bicycle extends Vehicle {
 @Override
 void drive() {
 System.out.println("Bicycle is riding");
 }

 void ringBell() {
 System.out.println("Ringing bicycle bell");
 }
}

public class ReferenceCastingDemo {
 public static void main(String[] args) {
 // Create array of vehicles
 Vehicle[] vehicles = new Vehicle[3];
 vehicles[0] = new Car(); // Upcasting
 vehicles[1] = new Bicycle(); // Upcasting
 vehicles[2] = new Vehicle();

 // Process each vehicle safely
 for (Vehicle v : vehicles) {
 v.drive();

 // Safe downcasting using instanceof
 if (v instanceof Car) {
 Car car = (Car) v;
 car.playMusic();
 } else if (v instanceof Bicycle) {
 Bicycle bike = (Bicycle) v;
 bike.ringBell();
 }
 System.out.println();
 }
 }
}
```

### Example 3: String to Number Conversion with Error Handling

**Problem:** Write a program that converts string input to integers and handles conversion errors gracefully.

**Solution:**

```java
public class StringConversionDemo {
 public static void main(String[] args) {
 String[] inputs = {"100", "50.5", "Hello", "200"};

 for (String input : inputs) {
 try {
 // Attempt conversion using Integer.parseInt
 int number = Integer.parseInt(input);
 System.out.println("Successfully converted: " + number);
 } catch (NumberFormatException e) {
 System.out.println("Cannot convert '" + input + "' to integer");
 }
 }

 // Demonstrate Double conversion
 String floatStr = "99.99";
 double value = Double.parseDouble(floatStr);
 System.out.println("\nDouble value: " + value);

 // Integer wrapper with valueOf
 Integer wrappedInt = Integer.valueOf("42");
 System.out.println("Wrapper value: " + wrappedInt);
 }
}
```

## Exam Tips

1. **Remember the widening hierarchy:** byte → short → char → int → long → float → double. This order is frequently tested in university examinations.

2. **Implicit vs Explicit:** Implicit conversions happen automatically (widening), while explicit conversions require cast operator (narrowing). Always remember that narrowing requires explicit casting syntax.

3. **Arithmetic promotion rules:** In binary operations, byte, short, and char are promoted to int. If either operand is double, the other becomes double, and so on.

4. **Downcasting safety:** Always use instanceof operator before downcasting to avoid ClassCastException at runtime. This is a common exam question.

5. **String conversions:** Remember that parseXxx() returns primitive values while valueOf() returns wrapper objects. Invalid conversions throw NumberFormatException.

6. **Assignment vs Arithmetic conversions:** Assignment conversions follow widening rules strictly, while arithmetic operations have their own promotion rules that include int promotion for smaller types.

7. **Reference casting rules:** Upcasting (subclass to superclass) is implicit and safe; downcasting (superclass to subclass) requires explicit casting and may fail at runtime.
