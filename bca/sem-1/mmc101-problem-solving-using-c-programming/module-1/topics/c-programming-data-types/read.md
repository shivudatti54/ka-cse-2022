# C Programming Data Types


## Table of Contents

- [C Programming Data Types](#c-programming-data-types)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Primary Data Types](#primary-data-types)
  - [Type Modifiers](#type-modifiers)
  - [Derived Data Types](#derived-data-types)
  - [The sizeof Operator](#the-sizeof-operator)
  - [Type Conversion](#type-conversion)
- [Examples](#examples)
  - [Example 1: Basic Data Type Declaration and Size Determination](#example-1-basic-data-type-declaration-and-size-determination)
  - [Example 2: Type Modifiers and Range Demonstration](#example-2-type-modifiers-and-range-demonstration)
  - [Example 3: Type Conversion Illustration](#example-3-type-conversion-illustration)
- [Exam Tips](#exam-tips)

## Introduction

Data types constitute the fundamental building blocks of any C program. In C programming, a data type defines the type of data that a variable can hold, the memory space allocated for that variable, and the set of operations that can be performed on it. Understanding data types is crucial because they directly impact memory utilization, program efficiency, and the accuracy of computational results.

The C programming language provides a rich collection of data types that allow programmers to handle different kinds of data efficiently. From simple integer values to complex user-defined structures, C offers a comprehensive type system that forms the foundation for developing robust and efficient software solutions. For students at the University of Delhi, mastering data types is essential as it appears consistently in both internal assessments and end-semester examinations, typically accounting for 8-12 marks in theory papers.

This topic covers the complete spectrum of C data types: primary or fundamental data types, derived data types, user-defined data types, and the type modifiers that extend their capabilities. A thorough understanding of these concepts enables programmers to write memory-efficient code and prevents common programming errors related to type mismatches.

## Key Concepts

### Primary Data Types

Primary data types, also known as fundamental or basic data types, are the atomic data types in C from which all other types are constructed.

**Integer Data Type (int)**: The integer data type is used to store whole numbers without any decimal component. On most systems, an `int` occupies 4 bytes (32 bits) of memory, allowing it to store values ranging from -2,147,483,648 to 2,147,483,647. Integers are typically used for counting, indexing arrays, and representing whole number quantities.

**Floating-Point Data Type (float)**: The `float` data type represents single-precision floating-point numbers with decimal components. It occupies 4 bytes of memory and provides approximately 6-7 significant digits of precision. Float variables are used when mathematical calculations require decimal precision, such as scientific calculations or financial computations where exact integer representation is insufficient.

**Double Precision Data Type (double)**: The `double` data type provides double-precision floating-point representation, occupying 8 bytes of memory with approximately 15-16 significant digits of precision. Due to its larger size and higher precision, `double` is the default data type for floating-point literals in C and is preferred for complex mathematical computations requiring high accuracy.

**Character Data Type (char)**: The `char` data type stores individual characters from the character set, typically occupying 1 byte (8 bits) of memory. Characters are enclosed in single quotes, such as 'A', '7', or '$'. The char type actually stores the ASCII numeric code of the character, allowing arithmetic operations on characters.

**Void Data Type (void)**: The `void` data type represents the absence of type information. It is used in three primary contexts: to indicate that a function returns no value, to indicate that a function accepts no parameters, and as a generic pointer type (void*).

### Type Modifiers

C provides several type modifiers that alter the characteristics of the primary data types, primarily affecting their range and memory consumption.

**Signed and Unsigned Modifiers**: The `signed` modifier allows variables to store both positive and negative values, while `unsigned` restricts variables to non-negative values only. For example, an `unsigned int` can store values from 0 to 4,294,967,295, double the positive range of a signed `int`.

**Short and Long Modifiers**: The `short` modifier reduces the storage size, while `long` increases it. A `short int` typically uses 2 bytes, while a `long int` uses 4 bytes on most systems. The `long long` modifier provides 8 bytes of storage for extremely large integers.

### Derived Data Types

Derived data types are constructed from primary data types and include arrays, pointers, functions, and structures.

**Arrays**: An array is a collection of elements of the same data type stored in contiguous memory locations. Arrays provide efficient storage and quick access to multiple values using index notation. For example, `int numbers[10]` declares an array capable of holding 10 integer values.

**Pointers**: A pointer is a variable that stores the memory address of another variable. Pointers are denoted by the `*` symbol and provide powerful capabilities for dynamic memory allocation, array manipulation, and function callback implementation.

**Structures**: A structure is a composite data type that groups together variables of different data types under a single name. Structures allow programmers to create custom data types that represent complex real-world entities.

**Unions**: Similar to structures, unions allow storing different data types in the same memory location. However, unions allocate memory equal to the size of their largest member, enabling memory-efficient storage of mutually exclusive data.

### The sizeof Operator

The `sizeof` operator is a compile-time unary operator that returns the size, in bytes, of its operand. It is essential for writing portable code and determining memory requirements. The syntax is `sizeof(expression)` or `sizeof(type)`. For example, `sizeof(int)` returns 4 on most systems, while `sizeof(char)` always returns 1.

### Type Conversion

Type conversion involves changing a value from one data type to another and occurs in two forms in C.

**Implicit Type Conversion**: Also known as automatic conversion, implicit conversion happens automatically when expressions contain mixed data types. The compiler automatically converts smaller types to larger types to prevent data loss. The conversion hierarchy follows: char → int → long → float → double.

**Explicit Type Conversion**: Also called type casting, explicit conversion is performed by the programmer using the cast operator with the syntax `(target_type)expression`. For example, `(int)3.14` converts the floating-point value 3.14 to integer 3.

## Examples

### Example 1: Basic Data Type Declaration and Size Determination

```c
#include <stdio.h>

int main() {
    // Primary data type declarations
    int age = 22;
    float percentage = 85.75;
    double salary = 50000.50;
    char grade = 'A';
    
    // Displaying sizes using sizeof operator
    printf("Size of int: %zu bytes\n", sizeof(int));
    printf("Size of float: %zu bytes\n", sizeof(float));
    printf("Size of double: %zu bytes\n", sizeof(double));
    printf("Size of char: %zu bytes\n", sizeof(char));
    
    // Displaying variable values
    printf("\nAge: %d\n", age);
    printf("Percentage: %.2f\n", percentage);
    printf("Salary: %.2f\n", salary);
    printf("Grade: %c\n", grade);
    
    return 0;
}
```

**Output:**
```
Size of int: 4 bytes
Size of float: 4 bytes
Size of double: 8 bytes
Size of char: 1 bytes

Age: 22
Percentage: 85.75
Salary: 50000.50
Grade: A
```

### Example 2: Type Modifiers and Range Demonstration

```c
#include <stdio.h>
#include <limits.h>  // For integer limit constants

int main() {
    // Demonstrating signed and unsigned integers
    signed int signedNum = -100;
    unsigned int unsignedNum = 200;
    
    printf("Signed int: %d\n", signedNum);
    printf("Unsigned int: %u\n", unsignedNum);
    
    // Demonstrating long and short modifiers
    long int largeNum = 1234567890L;
    short int smallNum = 100;
    
    printf("Long int: %ld\n", largeNum);
    printf("Short int: %hd\n", smallNum);
    
    // Displaying system limits
    printf("\nINT_MAX: %d\n", INT_MAX);
    printf("INT_MIN: %d\n", INT_MIN);
    printf("UINT_MAX: %u\n", UINT_MAX);
    
    return 0;
}
```

### Example 3: Type Conversion Illustration

```c
#include <stdio.h>

int main() {
    // Implicit type conversion
    int num1 = 10;
    float num2 = 5.5;
    float result1 = num1 + num2;  // int converted to float
    
    printf("Implicit conversion: %d + %.2f = %.2f\n", num1, num2, result1);
    
    // Explicit type conversion (type casting)
    float num3 = 10.7;
    int result2 = (int)num3;  // Explicitly cast float to int
    
    printf("Explicit conversion: (int)%.2f = %d\n", num3, result2);
    
    // Division with type conversion
    int a = 7, b = 2;
    float div1 = a / b;        // Integer division (result: 3)
    float div2 = (float)a / b; // Explicit conversion (result: 3.50)
    
    printf("\nInteger division: %d / %d = %d\n", a, b, a/b);
    printf("With casting: (float)%d / %d = %.2f\n", a, b, div2);
    
    return 0;
}
```

**Output:**
```
Implicit conversion: 10 + 5.50 = 15.50
Explicit conversion: (int)10.70 = 10

Integer division: 7 / 2 = 3
With casting: (float)7 / 2 = 3.50
```

## Exam Tips

1. **Memorize Standard Sizes**: Remember that on most systems, char is 1 byte, int is 4 bytes, float is 4 bytes, and double is 8 bytes. These values are frequently tested in examination questions.

2. **Understand Range Calculations**: For signed integers using n bits, the range is -2^(n-1) to 2^(n-1)-1. For unsigned integers, the range is 0 to 2^n - 1. This concept regularly appears in 2-3 mark questions.

3. **Differentiate Implicit vs Explicit Conversion**: Implicit conversion happens automatically by the compiler, while explicit conversion requires the cast operator. Questions often ask students to predict the output of mixed-type expressions.

4. **Remember Default Types**: Floating-point literals like 3.14 are double by default. Use suffix 'f' or 'F' for float literals, such as 3.14f.

5. **Void Pointer Usage**: Understand that void* can hold addresses of any data type, but requires explicit casting when dereferenced. This is a common source of confusion in practical exams.

6. **sizeof Operator Syntax**: Remember that sizeof is a compile-time operator. It can be used as sizeof(var) or sizeof(type), and the result type is size_t.

7. **Integer Division Trap**: When dividing two integers in C, the result is always an integer, discarding the decimal portion. Always remember to cast at least one operand to float for decimal results.

8. **ASCII Values**: Character constants in C store ASCII values. This allows arithmetic operations on char variables, such as 'A' + 1 yielding 'B' (since ASCII of 'A' is 65).