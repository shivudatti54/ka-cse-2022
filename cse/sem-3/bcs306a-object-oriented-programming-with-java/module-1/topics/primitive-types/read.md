# Primitive Types in Java

## Table of Contents

- [Primitive Types in Java](#primitive-types-in-java)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [The Eight Primitive Types](#the-eight-primitive-types)
  - [Default Values](#default-values)
  - [Type Conversion in Java](#type-conversion-in-java)
- [Examples](#examples)
  - [Example 1: Working with Integer Types](#example-1-working-with-integer-types)
  - [Example 2: Floating-Point and Character Types](#example-2-floating-point-and-character-types)
  - [Example 3: Type Conversion Demonstration](#example-3-type-conversion-demonstration)
- [Exam Tips](#exam-tips)

## Introduction

Primitive types are the fundamental data types in Java that represent simple values rather than objects. Unlike languages such as Python where everything is an object, Java maintains a distinction between primitive types and reference types. This design choice was made deliberately for performance reasons, as primitive types are stored directly in the stack memory and do not require the overhead of object creation.

Understanding primitive types is crucial for any Java programmer because they form the building blocks of all data manipulation in the language. Whether you are performing mathematical calculations, storing boolean flags, or working with character data, you will rely on primitive types extensively. In the context of Object-Oriented Programming, primitives play a vital role even though they are not objects themselves—Java provides wrapper classes to bridge this gap when object representation is required.

In this module, we will explore all eight primitive types in Java, their characteristics, ranges, default values, and the type conversion mechanisms that allow interoperability between different primitive types.

## Key Concepts

### The Eight Primitive Types

Java defines exactly eight primitive data types, which are also known as built-in types. These are categorized into four groups based on the kind of data they store.

**Integral Types:**

- **byte**: An 8-bit signed integer with values ranging from -128 to 127. It is the smallest integer type in Java and is commonly used when working with binary data or when memory conservation is critical.
- **short**: A 16-bit signed integer ranging from -32,768 to 32,767. It is less commonly used but can be useful for interoperability with systems that use 16-bit data.
- **int**: A 32-bit signed integer ranging from approximately -2.1 billion to 2.1 billion. This is the most frequently used integer type in Java for general-purpose arithmetic.
- **long**: A 64-bit signed integer ranging from about -9.2 quintillion to 9.2 quintillion. It is used when int is insufficient to hold large values, such as timestamps or large counts.

**Floating-Point Types:**

- **float**: A 32-bit floating-point number following IEEE 754 standard. It can represent values with approximately 6-7 significant decimal digits. Used when memory is a concern or when working with graphical coordinates.
- **double**: A 64-bit floating-point number with approximately 15 significant decimal digits. This is the default choice for floating-point arithmetic in Java.

**Character Type:**

- **char**: A 16-bit unsigned integer representing a single Unicode character. It can hold values from 0 to 65,535, corresponding to Unicode code points. Note that char is unsigned in Java, unlike in C/C++.

**Boolean Type:**

- **boolean**: Represents logical values and can hold only two possible values: true or false. The size of boolean is not precisely specified by the JVM implementation, though it is typically implemented as a single byte.

### Default Values

Primitive types have specific default values when used as instance variables in a class. However, local variables (variables declared inside methods) must be explicitly initialized before use—attempting to use an uninitialized local variable results in a compile-time error.

| Type    | Default Value             |
| ------- | ------------------------- |
| byte    | 0                         |
| short   | 0                         |
| int     | 0                         |
| long    | 0L                        |
| float   | 0.0f                      |
| double  | 0.0d                      |
| char    | '\u0000' (null character) |
| boolean | false                     |

### Type Conversion in Java

Java provides two types of type conversion for primitive types: widening (implicit) conversion and narrowing (explicit) conversion.

**Widening Conversion (Implicit):**
This occurs automatically when a smaller type is assigned to a larger type. The conversion is safe because no data loss occurs. The hierarchy for widening is:
byte → short → int → long → float → double
char → int → long → float → double

For example:

```java
int num = 100;
long largeNum = num; // Automatic widening
double d = num; // Automatic widening
```

**Narrowing Conversion (Explicit):**
This requires explicit casting because there is potential for data loss. The programmer must explicitly indicate the intention to convert using the cast operator:

```java
double d = 100.5;
int num = (int) d; // Result: 100 (decimal part truncated)
```

**Type Promotion in Expressions:**
When performing arithmetic operations, Java automatically promotes smaller types to larger types. For instance, when adding an int and a long, the int is promoted to long, and the result is long. This is known as binary numeric promotion.

## Examples

### Example 1: Working with Integer Types

```java
public class IntegerTypesDemo {
 public static void main(String[] args) {
 // byte: Range -128 to 127
 byte smallNumber = 100;
 System.out.println("byte value: " + smallNumber);

 // short: Range -32768 to 32767
 short shortNumber = 32000;
 System.out.println("short value: " + shortNumber);

 // int: Default integer type
 int normalNumber = 1_000_000; // Underscore allowed in Java 7+
 System.out.println("int value: " + normalNumber);

 // long: For large integers
 long largeNumber = 9_223_372_036_854_775_807L;
 System.out.println("long value: " + largeNumber);

 // Demonstration of overflow
 byte maxByte = 127;
 // byte overflow = maxByte + 1; // Would cause compilation error
 byte afterOverflow = (byte)(maxByte + 1); // Becomes -128
 System.out.println("After overflow: " + afterOverflow);
 }
}
```

### Example 2: Floating-Point and Character Types

```java
public class FloatCharDemo {
 public static void main(String[] args) {
 // float requires 'f' or 'F' suffix
 float pi = 3.14159f;
 System.out.println("float pi: " + pi);

 // double is default for decimal literals
 double e = 2.718281828;
 System.out.println("double e: " + e);

 // char stores single characters
 char grade = 'A';
 char unicodeChar = '\u0041'; // Same as 'A'
 System.out.println("char grade: " + grade);
 System.out.println("Unicode char: " + unicodeChar);

 // Demonstrating char as numeric type
 char c = 'A';
 int asciiValue = c; // Widening conversion to int
 System.out.println("ASCII value of A: " + asciiValue);
 }
}
```

### Example 3: Type Conversion Demonstration

```java
public class TypeConversionDemo {
 public static void main(String[] args) {
 // Widening (implicit) conversion
 int num = 50;
 long longNum = num; // int to long
 double doubleNum = num; // int to double
 System.out.println("Widening: " + longNum + ", " + doubleNum);

 // Narrowing (explicit) conversion with casting
 double bigNum = 123.456;
 int intNum = (int) bigNum; // Truncates decimal part
 System.out.println("Narrowing double to int: " + intNum);

 // char to int widening
 char letter = 'Z';
 int letterValue = letter;
 System.out.println("Char 'Z' as int: " + letterValue);

 // Arithmetic type promotion
 int a = 10;
 double b = 20.5;
 double result = a + b; // int promoted to double
 System.out.println("Type promotion result: " + result);

 // Demonstrating data loss in narrowing
 int largeInt = 1000;
 byte smallByte = (byte) largeInt;
 System.out.println("Data loss in narrowing: " + smallByte);
 // 1000 in binary: 1111101000
 // When stored in byte (8 bits), only lower 8 bits are kept
 // Result: -24 (due to two's complement interpretation)
 }
}
```

## Exam Tips

1. **Remember the eight primitive types**: byte, short, int, long, float, double, char, and boolean. This is a common short-answer question in university exams.

2. **Know the sizes and ranges**: Understand that int is 32-bit, long is 64-bit, float is 32-bit, and double is 64-bit. Be able to state approximate ranges for each type.

3. **Default values are important**: Remember that instance variables of primitive types get default values (0, 0.0, false, '\u0000'), but local variables do not and must be initialized before use.

4. **Widening vs Narrowing**: Automatic conversion happens only for widening (small to large). Narrowing requires explicit casting. Remember the widening hierarchy: byte → short → int → long → float → double.

5. **Character type specifics**: Remember that Java char is 16-bit unsigned (0 to 65535), unlike C/C++ where it is 8-bit signed. This allows it to store Unicode characters.

6. **Floating-point literals**: Remember to add 'f' or 'F' suffix for float literals. Without the suffix, decimal literals are treated as double by default.

7. **Integer literals**: By default, integer literals are int. Use 'L' or 'l' suffix for long literals. Underscores are allowed in numeric literals for readability (Java 7+).

8. **Boolean in conditions**: Remember that in Java, you cannot use integers where boolean is expected (unlike C/C++). The condition must evaluate to true or false.
