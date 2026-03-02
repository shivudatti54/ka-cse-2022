# Floating-Point Types

## Introduction

Floating-point types in Java represent real numbers—numbers that contain decimal fractions and are essential for scientific computations, financial calculations, graphics programming, and engineering applications. Unlike integers which can only represent whole numbers, floating-point types enable Java programs to handle values like 3.14159, -0.0075, or 1.23 × 10^6 with precision and efficiency.

Java provides two primitive floating-point data types: float and double. The float type occupies 32 bits and offers approximately 6-7 significant decimal digits of precision, while the double type uses 64 bits and provides approximately 15 significant decimal digits of precision. Understanding the characteristics, limitations, and proper usage of these types is crucial for writing accurate numerical programs. Many students lose marks in exams due to confusion between these types, precision errors, and incorrect literal representations.

## Key Concepts

### The float Type

The float type is a 32-bit IEEE 754 single-precision floating-point number. It can represent values ranging from approximately 1.4 × 10^-45 to 3.4 × 10^38 in magnitude, both positive and negative. The structure follows the IEEE 754 standard: 1 bit for sign, 8 bits for exponent, and 23 bits for mantissa (also called significand).

The range of positive float values is: 1.4e-45 to 3.4e38

The default value of a float variable is 0.0f (or 0.0F). The suffix 'f' or 'F' is mandatory when assigning a floating-point literal to a float variable, because by default, Java treats decimal literals as double.

```java
float pi = 3.14f;        // Correct: with f suffix
float price = 99.99F;    // Correct: with F suffix
float error = 3.14;      // Compile error: 3.14 is double by default
```

### The double Type

The double type is a 64-bit IEEE 754 double-precision floating-point number. It provides significantly greater precision with approximately 15 decimal digits of accuracy. The positive range extends from 4.9 × 10^-324 to 1.8 × 10^308.

The default value of a double variable is 0.0d (though the d suffix is optional). Double is the default type for floating-point literals in Java.

```java
double radius = 5.5;          // Valid: double by default
double height = 10.0;         // Valid: decimal literals are double
double precision = 3.14159265358979;  // High precision value
```

### Floating-Point Literals

A floating-point literal is a representation of a floating-point number in source code. Java allows two formats:

1. **Standard Decimal Notation**: Uses the decimal point
   - 3.14, 0.5, -12.34, .5 (equivalent to 0.5)

2. **Scientific Notation (E Notation)**: Uses exponent with base 10
   - 1.5e10 means 1.5 × 10^10 = 15000000000.0
   - 2.5E-5 means 2.5 × 10^-5 = 0.000025

```java
double avogadro = 6.022e23;    // 6.022 × 10^23
double plank = 6.626e-34;      // 6.626 × 10^-34
float small = 1.0e-38f;        // Using e notation with float
```

### Precision and Rounding Errors

Floating-point arithmetic in Java (and virtually all programming languages) involves inherent precision limitations. The IEEE 754 format cannot represent all real numbers exactly—it stores an approximation. This leads to rounding errors that can accumulate in calculations.

```java
// Classic precision problem
double result = 0.1 + 0.2;
System.out.println(result);    // Output: 0.30000000000000004
```

This behavior is NOT a bug—it's a fundamental characteristic of binary floating-point representation. The decimal value 0.1 cannot be represented exactly in binary, similar to how 1/3 cannot be represented exactly in decimal.

For precise decimal calculations (like financial applications), Java provides the java.math.BigDecimal class which handles arbitrary precision decimal arithmetic.

### Special Floating-Point Values

IEEE 754 defines several special values that float and double can hold:

1. **Positive Infinity (POSITIVE_INFINITY)**: Result of division 1.0/0.0
2. **Negative Infinity (NEGATIVE_INFINITY)**: Result of division -1.0/0.0
3. **NaN (Not a Number)**: Result of 0.0/0.0 or sqrt(-1)
4. **Positive Zero and Negative Zero**: 0.0 and -0.0 (both are equal but behave differently in some operations)

```java
System.out.println(Double.POSITIVE_INFINITY);  // Infinity
System.out.println(Double.NEGATIVE_INFINITY);  // -Infinity
System.out.println(Double.NaN);                // NaN
System.out.println(0.0 / 0.0);                 // NaN
System.out.println(1.0 / 0.0);                 // Infinity
```

### Type Conversion and Casting

Implicit widening conversion from float to double is automatic. However, narrowing conversion from double to float requires explicit casting.

```java
float f = 100.25f;
double d = f;          // Automatic: float to double

double d2 = 200.50;
float f2 = (float) d2; // Explicit cast required: double to float

// Casting can cause data loss if value exceeds float range
double large = 1.8e308;
float f3 = (float) large;  // Infinity (loss of precision)
```

## Examples

### Example 1: Calculating Circle Area

Write a Java program to calculate the area of a circle given its radius.

```java
public class CircleArea {
    public static void main(String[] args) {
        double radius = 7.5;
        double area = Math.PI * radius * radius;  // Using Math.PI constant
        
        System.out.println("Radius: " + radius);
        System.out.println("Area: " + area);
    }
}
```

Output:
```
Radius: 7.5
Area: 176.7145867644258
```

Explanation: We use double for radius and area because it provides better precision. Math.PI is a double constant representing π to full double precision.

### Example 2: Scientific Notation and Unit Conversion

Convert 1230000 to scientific notation and perform unit conversion (kilometers to meters).

```java
public class ScientificNotation {
    public static void main(String[] args) {
        // Using scientific notation
        double population = 1.23e6;  // 1,230,000
        System.out.println("Population: " + population);
        
        // Unit conversion using scientific notation
        double distanceKm = 5.5e3;   // 5500 kilometers
        double distanceM = distanceKm * 1000;
        
        System.out.println("Distance: " + distanceKm + " km = " + distanceM + " meters");
    }
}
```

Output:
```
Population: 1230000.0
Distance: 5500.0 km = 5500000.0 meters
```

### Example 3: Precision Comparison

Demonstrate the difference in precision between float and double.

```java
public class PrecisionDemo {
    public static void main(String[] args) {
        // Using float (32-bit)
        float f1 = 1.123456789f;
        float f2 = 1.1234567f;
        
        // Using double (64-bit)
        double d1 = 1.123456789;
        double d2 = 1.1234567;
        
        System.out.println("Float comparison:");
        System.out.println("f1: " + f1);
        System.out.println("f2: " + f2);
        
        System.out.println("\nDouble comparison:");
        System.out.println("d1: " + d1);
        System.out.println("d2: " + d2);
        
        // Demonstrating accumulation error
        float sumFloat = 0.0f;
        for (int i = 0; i < 1000; i++) {
            sumFloat += 0.1f;
        }
        System.out.println("\nFloat sum of 0.1 added 1000 times: " + sumFloat);
        
        double sumDouble = 0.0;
        for (int i = 0; i < 1000; i++) {
            sumDouble += 0.1;
        }
        System.out.println("Double sum of 0.1 added 1000 times: " + sumDouble);
    }
}
```

Expected Output:
```
Float comparison:
f1: 1.1234568
f2: 1.1234567

Double comparison:
d1: 1.123456789
d2: 1.1234567

Float sum of 0.1 added 1000 times: 99.99905
Double sum of 0.1 added 1000 times: 99.9999999999986
```

The float type loses precision much faster than double when accumulating small errors through repeated operations.

## Exam Tips

1. **Default Type Recognition**: Remember that floating-point literals WITHOUT any suffix are of type double in Java, NOT float. This is a common exam question.

2. **Suffix Usage**: Always use 'f' or 'F' suffix for float literals. Missing suffix is a compile-time error when assigning to float variables.

3. **Precision Choice**: For most general-purpose calculations, prefer double over float. The extra precision comes at minimal memory cost and is the Java standard.

4. **Equality Comparison**: Never compare floating-point numbers using == for equality. Use a tolerance-based comparison: `Math.abs(a - b) < 0.0001`

5. **Range vs Precision**: Understand that float has WIDER range but LOWER precision than double. Range (magnitude) and precision are different concepts.

6. **NaN Handling**: Remember that NaN comparisons always return false, including NaN == NaN. Use Double.isNaN() to check for NaN values.

7. **Special Values**: Know how Infinity and NaN are produced (division by zero, sqrt of negative numbers) and how they propagate in arithmetic operations.

8. **BigDecimal for Money**: For financial applications requiring exact decimal representation, BigDecimal is the recommended type, not double or float.

9. **Automatic Type Promotion**: In expressions, float is promoted to double if any operand is double. The result is double unless explicitly cast.

10. **Bit Representation**: Remember that float uses 32 bits and double uses 64 bits. This affects both range and precision significantly.