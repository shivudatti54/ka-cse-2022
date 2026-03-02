# Type Wrappers in Java

## Table of Contents

- [Type Wrappers in Java](#type-wrappers-in-java)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Wrapper Classes Hierarchy](#wrapper-classes-hierarchy)
  - [Autoboxing and Unboxing](#autoboxing-and-unboxing)
  - [Common Wrapper Class Methods](#common-wrapper-class-methods)
  - [Value Comparison](#value-comparison)
- [Examples](#examples)
  - [Example 1: Explicit Boxing and Unboxing](#example-1-explicit-boxing-and-unboxing)
  - [Example 2: Autoboxing and Unboxing in Operations](#example-2-autoboxing-and-unboxing-in-operations)
  - [Example 3: Using Wrapper Class Constants and Methods](#example-3-using-wrapper-class-constants-and-methods)
- [Exam Tips](#exam-tips)

## Introduction

Type wrappers in Java are classes that encapsulate primitive data types within objects. Java provides a wrapper class for each of the eight primitive data types: Integer, Long, Float, Double, Short, Byte, Character, and Boolean. These wrapper classes reside in the java.lang package and are automatically imported into every Java program. The primary motivation behind type wrappers is to allow primitive values to be treated as objects, which is essential for compatibility with Java's object-oriented features such as collections, generics, and reflection mechanisms.

Before the introduction of autoboxing and unboxing in Java 5, developers had to explicitly convert primitive values to wrapper objects and vice versa using constructor methods. This process was verbose and error-prone. The Java platform now handles these conversions automatically, making code more readable and concise while maintaining the underlying object representation when needed.

## Key Concepts

### Wrapper Classes Hierarchy

All numeric wrapper classes (Integer, Long, Float, Double, Short, Byte) extend the abstract class Number, which provides methods for converting values to different primitive types. Character and Boolean are direct subclasses of Object. The wrapper classes are immutable—once created, their values cannot be changed.

### Autoboxing and Unboxing

Autoboxing is the automatic conversion from a primitive type to its corresponding wrapper class. For example, when an int is assigned to an Integer variable or passed to a method expecting an Integer, the compiler automatically wraps the primitive. Unboxing is the reverse process—automatic conversion from wrapper to primitive. These features were introduced in Java 5 (J2SE 5.0) and significantly simplified code that previously required explicit conversions.

### Common Wrapper Class Methods

Each numeric wrapper class provides several important methods. The `valueOf(String s)` method parses a String and returns a wrapper object. The `parseXxx(String s)` method (where Xxx is the primitive type) returns the primitive value. The `toString()` method converts the wrapper object to its String representation. Additionally, each wrapper class contains constants like `MIN_VALUE` and `MAX_VALUE` that define the range of values for that type.

### Value Comparison

An important distinction exists between using `==` and `.equals()` with wrapper objects. The `==` operator compares object references (memory addresses), while `.equals()` compares actual values. Due to caching, wrapper objects for certain values may share references, but this behavior is not guaranteed and should not be relied upon. Always use `.equals()` for value comparisons.

## Examples

### Example 1: Explicit Boxing and Unboxing

```java
public class WrapperDemo {
 public static void main(String[] args) {
 // Explicit boxing (manual conversion from primitive to object)
 Integer num = new Integer(42);

 // Explicit unboxing (manual conversion from object to primitive)
 int primitive = num.intValue();

 System.out.println("Wrapper object: " + num);
 System.out.println("Primitive value: " + primitive);
 }
}
```

### Example 2: Autoboxing and Unboxing in Operations

```java
public class AutoBoxDemo {
 public static void main(String[] args) {
 Integer a = 10; // Autoboxing: int -> Integer
 Integer b = 20; // Autoboxing

 // Unboxing occurs automatically during arithmetic operations
 Integer sum = a + b; // Both unbox to int, add, then box result

 System.out.println("Sum: " + sum); // Output: Sum: 30

 // Using wrapper in collections (requires boxing)
 java.util.ArrayList<Integer> list = new java.util.ArrayList<>();
 list.add(100); // Autoboxing: int -> Integer

 int value = list.get(0); // Unboxing: Integer -> int
 System.out.println("Retrieved: " + value);
 }
}
```

### Example 3: Using Wrapper Class Constants and Methods

```public class WrapperConstants {
 public static void main(String[] args) {
 // Using MIN_VALUE and MAX_VALUE constants
 System.out.println("Integer MIN: " + Integer.MIN_VALUE);
 System.out.println("Integer MAX: " + Integer.MAX_VALUE);

 // Parsing String to wrapper and primitive
 String str = "12345";
 Integer wrapped = Integer.valueOf(str);
 int parsed = Integer.parseInt(str);

 System.out.println("ValueOf: " + wrapped);
 System.out.println("ParseInt: " + parsed);

 // Converting wrapper to different types
 Double d = 99.99;
 System.out.println("As int: " + d.intValue());
 System.out.println("As long: " + d.longValue());
 }
}
```

## Exam Tips

1. Remember that wrapper classes are immutable—creating a new wrapper object is necessary to change its value.

2. The `valueOf()` method returns a wrapper object, while `parseXxx()` returns a primitive value—distinguish between them in exam questions.

3. Numeric wrapper classes (except Character and Boolean) extend the abstract Number class, which provides methods like `doubleValue()`, `floatValue()`, and `intValue()`.

4. All wrapper classes are final, meaning they cannot be subclassed.

5. Autoboxing works with ternary operators and in method arguments where the parameter type differs from the argument type.

6. Be cautious with `==` comparisons on wrapper objects—they compare references, not values.

7. Wrapper classes are required when working with generics and collections, as these structures store objects, not primitives.

8. The Boolean wrapper class treats any non-null, non-true string as false when using `valueOf()` with strings.
