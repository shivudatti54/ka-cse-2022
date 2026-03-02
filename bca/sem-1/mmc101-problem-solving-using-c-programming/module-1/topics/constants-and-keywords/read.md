# Constants And Keywords


## Table of Contents

- [Constants And Keywords](#constants-and-keywords)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Constants in C](#constants-in-c)
  - [Keywords in C](#keywords-in-c)
  - [Important Distinctions](#important-distinctions)
- [Examples](#examples)
  - [Example 1: Working with Different Types of Constants](#example-1-working-with-different-types-of-constants)
  - [Example 2: Using const and enum](#example-2-using-const-and-enum)
  - [Example 3: Identifying Valid and Invalid Identifiers](#example-3-identifying-valid-and-invalid-identifiers)
- [Exam Tips](#exam-tips)

## Introduction

Constants and keywords form the fundamental building blocks of any C program. While variables allow us to store and manipulate data that can change during program execution, constants represent fixed values that remain unchanged throughout the program's lifetime. Understanding constants is crucial for writing robust C programs, as they help prevent accidental modification of critical values and improve code readability.

Keywords, on the other hand, are reserved words that have special meaning in the C programming language. These words cannot be used as identifiers (variable names, function names, or labels) because they are part of the language's syntax. The C language defines a specific set of keywords that implement its core functionality, including control flow statements, data types, and storage class specifiers.

In the context of Problem Solving Using C Programming, mastering constants and keywords is essential because they directly relate to how data is represented, stored, and processed in memory. For instance, understanding the difference between integer and floating-point constants helps in choosing appropriate data types, while knowledge of keywords enables proper program structure and logic implementation. This topic appears frequently in DU semester examinations, typically carrying significant weightage in both theory and practical components.

## Key Concepts

### Constants in C

A constant is a quantity that does not change its value during program execution. In C, constants can be defined using several methods, each with distinct characteristics and use cases.

#### Integer Constants

Integer constants represent whole numbers without decimal points. C supports three number systems for integer constants:

- **Decimal**: Base-10 system using digits 0-9 (e.g., 100, -45, 32767)
- **Octal**: Base-8 system using digits 0-7, prefixed with 0 (e.g., 077, 0123)
- **Hexadecimal**: Base-16 system using digits 0-9 and letters A-F, prefixed with 0x or 0X (e.g., 0xFF, 0X1A)

Integer constants can have suffixes to specify their type. The suffix 'L' or 'l' denotes long, and 'U' or 'u' denotes unsigned. For example, 123U represents an unsigned integer, while 123L represents a long integer.

#### Floating-Point Constants

Floating-point constants represent real numbers with decimal points. They are always represented in decimal form and can be written in scientific notation. For example, 3.14159, -0.5, and 2.5e-3 (representing 0.0025) are valid floating-point constants.

By default, floating-point constants are of type double. The suffix 'F' or 'f' makes it float, while 'L' or 'l' makes it long double. For instance, 3.14f is a float constant, and 3.14L is a long double constant.

#### Character Constants

Character constants are enclosed in single quotes and represent a single character. For example, 'A', '5', '#'. C also supports escape sequences (backslash character constants) for special characters like newline ('\n'), tab ('\t'), and null character ('\0').

The ASCII values of characters allow them to be used in arithmetic operations. For instance, 'A' + 1 yields 66, which is the ASCII value of 'B'.

#### String Constants

String constants (string literals) are enclosed in double quotes and represent a sequence of characters. "Hello, DU!" is a string constant. Internally, strings are stored as arrays of characters terminated by a null character ('\0').

#### Symbolic Constants

Symbolic constants are identifiers that represent constant values throughout the program. C provides two methods to define symbolic constants:

1. **Using #define preprocessor directive**: This creates a macro that performs textual substitution before compilation. For example:
   ```c
   #define PI 3.14159
   #define MAX_SIZE 100
   ```

2. **Using const keyword**: This declares a variable whose value cannot be modified after initialization:
   ```c
   const int MAX_SIZE = 100;
   int const MAX_SIZE = 100;  // Equivalent syntax
   ```

The key difference between const and #define is that const follows C's scope rules (block, function, file scope), while #define does not. Additionally, const variables have type checking, while #define macros do not.

#### Enumerated Constants

Enumerated constants create a list of named integer constants. The enum keyword is used for this purpose:
```c
enum days { MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY };
```
By default, enum constants start from 0 and increment by 1. So MONDAY = 0, TUESDAY = 1, and so on. You can also assign specific values:
```c
enum months { JAN = 1, FEB = 2, MAR = 3, APR = 4, MAY = 5, JUN = 6 };
```

### Keywords in C

Keywords are reserved words that have predefined meanings in C. The C standard defines a specific set of keywords, and programmers cannot redefine them or use them as identifiers.

#### C89/C90 Keywords (32 keywords)

The original C standard defined 32 keywords:

**Data Types**: char, int, float, double, void

**Type Modifiers**: short, long, signed, unsigned

**Control Flow**: if, else, switch, case, default, for, while, do, break, continue, return, goto

**Storage Classes**: auto, register, static, extern, const, volatile

**Other**: struct, union, enum, typedef, sizeof, void

#### C99 Keywords (5 additional keywords)

C99 added five new keywords: inline, restrict, _Bool, _Complex, and _Imaginary

#### C11 Keywords (5 additional keywords)

C11 added: _Alignas, _Alignof, _Atomic, _Noreturn, _Static_assert

#### C23 Keywords

The latest C23 standard may add additional keywords, though these vary by compiler implementation.

### Important Distinctions

Understanding the difference between constants and keywords is crucial:

- **Constants** are data values that do not change (e.g., the value 3.14159 for PI)
- **Keywords** are reserved words that have special meaning in the language syntax

Additionally, programmers should note that identifiers starting with an underscore followed by an uppercase letter or another underscore are reserved for the implementation (compiler and standard library). Using such identifiers can lead to undefined behavior.

## Examples

### Example 1: Working with Different Types of Constants

```c
#include <stdio.h>

#define PI 3.14159          // Symbolic constant using #define
#define NEWLINE '\n'        // Character constant

int main() {
    // Integer constants in different bases
    int decimal = 255;         // Decimal (base 10)
    int octal = 0377;          // Octal (base 8)
    int hexadecimal = 0xFF;    // Hexadecimal (base 16)
    
    // All three represent the same value
    printf("Decimal: %d, Octal: %o, Hex: %x%c", decimal, octal, hexadecimal, NEWLINE);
    
    // Floating-point constants
    double radius = 5.5;
    double area = PI * radius * radius;
    
    // Character constant
    char grade = 'A';
    
    // String constant
    printf("Grade: %c, Area: %.2f%c", grade, area, NEWLINE);
    
    return 0;
}
```

**Output:**
```
Decimal: 255, Octal: 377, Hex: ff
Grade: A, Area: 95.03
```

### Example 2: Using const and enum

```c
#include <stdio.h>

enum week { SUN = 0, MON = 1, TUE = 2, WED = 3, THU = 4, FRI = 5, SAT = 6 };

int main() {
    // Using const for read-only variables
    const int MAX_ATTEMPTS = 3;
    const float TAX_RATE = 0.15f;
    
    // Using enum for related constants
    enum week today = WED;
    
    printf("Maximum attempts: %d%c", MAX_ATTEMPTS, '\n');
    printf("Tax rate: %.2f%c", TAX_RATE, '\n');
    printf("Today is day number: %d%c", today, '\n');
    
    // Demonstrating enum values
    printf("Sunday = %d, Friday = %d%c", SUN, FRI, '\n');
    
    return 0;
}
```

**Output:**
```
Maximum attempts: 3
Tax rate: 0.15
Today is day number: 3
Sunday = 0, Friday = 5
```

### Example 3: Identifying Valid and Invalid Identifiers

```c
#include <stdio.h>

// VALID: Using keywords as identifiers is NOT allowed
// The following would cause compilation errors:
// int int;        // ERROR: 'int' is a keyword
// float return;   // ERROR: 'return' is a keyword
// double if;      // ERROR: 'if' is a keyword

// VALID: Using descriptive names for variables
int student_count = 50;
float percentage = 75.5;
char grade = 'A';

// VALID: Constants using #define
#define ARRAY_SIZE 100
#define MESSAGE "Hello, Student!"

int main() {
    printf("Student Count: %d%c", student_count, '\n');
    printf("Percentage: %.2f%c", percentage, '\n');
    printf("Grade: %c%c", grade, '\n');
    printf("Message: %s%c", MESSAGE, '\n');
    printf("Array Size: %d%c", ARRAY_SIZE, '\n');
    
    return 0;
}
```

## Exam Tips

1. **Remember the complete list of C keywords**: All 32 C89 keywords plus C99 and C11 additions are essential. Commonly tested keywords include if, else, for, while, do, switch, case, default, break, continue, return, int, char, float, double, void, const, static, extern, struct, union, enum, and typedef.

2. **Understand the difference between #define and const**: #define performs text substitution before compilation (no type checking, no memory allocation), while const creates actual variables with type checking and memory allocation. This distinction is frequently tested in DU exams.

3. **Know how integer constants work in different bases**: Remember that octal constants start with 0, and hexadecimal constants start with 0x or 0X. The value 012 is octal (equal to decimal 10), while 12 is decimal.

4. **Character constants use single quotes, string literals use double quotes**: This is a common source of errors. 'A' is a character constant (type int in C), while "A" is a string literal (type char array).

5. **Escape sequences represent special characters**: Remember common escape sequences like \n (newline), \t (tab), \\ (backslash), \' (single quote), \" (double quote), and \0 (null character).

6. **Enum constants start from 0 by default**: Unless explicitly assigned, the first enum constant has value 0, the next has value 1, and so on. This concept often appears in examination questions.

7. **Keywords cannot be used as variable names**: This is a fundamental rule. Any attempt to use keywords as identifiers results in compilation errors. Always avoid using reserved words for naming variables or functions.

8. **Suffixes matter for numeric constants**: Remember that L makes a constant long, U makes it unsigned, F makes a floating-point constant a float. These suffixes affect the type and storage of constants.