# Built In Functions in C Programming


## Table of Contents

- [Built In Functions in C Programming](#built-in-functions-in-c-programming)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Header Files and Function Prototypes](#header-files-and-function-prototypes)
  - [Categories of Built-In Functions](#categories-of-built-in-functions)
- [Examples](#examples)
  - [Example 1: String Manipulation Program](#example-1-string-manipulation-program)
  - [Example 2: Mathematical Operations Program](#example-2-mathematical-operations-program)
  - [Example 3: Character Classification Program](#example-3-character-classification-program)
- [Exam Tips](#exam-tips)

## Introduction

Built-in functions, also known as library functions or pre-defined functions, are an integral part of the C programming language. These functions are provided by the C standard library and are readily available for programmers to use without requiring any additional implementation. The C standard library contains hundreds of functions organized into various header files, each serving specific purposes ranging from input/output operations to mathematical computations and string manipulations.

Understanding and effectively utilizing built-in functions is crucial for writing efficient and professional C programs. Rather than reinventing the wheel by writing custom code for common operations, programmers can leverage these optimized, tested, and reliable functions. This approach not only saves development time but also ensures better performance and reduced chances of errors. For students preparing for DU semester examinations, a thorough understanding of built-in functions is essential as they form the foundation for solving complex programming problems efficiently.

The C standard library functions are categorized based on their functionality and are accessed by including the appropriate header files using the #include preprocessor directive. Some of the most commonly used header files include stdio.h for input/output operations, string.h for string handling, math.h for mathematical functions, ctype.h for character classification, and stdlib.h for general utility functions.

## Key Concepts

### Header Files and Function Prototypes

Before using any built-in function, programmers must include the corresponding header file using the #include directive. Each header file contains function prototypes that declare the function name, return type, and parameter types. This enables the compiler to perform type checking and ensures proper function calls. For example, to use printf and scanf, programmers must include stdio.h, while mathematical functions require math.h.

### Categories of Built-In Functions

**Input/Output Functions (stdio.h)**

The standard input/output functions form the backbone of C programming for interacting with users. The printf() function is used for formatted output to the console, allowing programmers to display data of various types with precise control over formatting. Its counterpart, scanf(), reads formatted input from the keyboard. Other important I/O functions include getchar() for reading a single character, putchar() for outputting a single character, gets() for reading a string (though considered unsafe), and puts() for displaying a string followed by a newline.

**String Handling Functions (string.h)**

The string.h header provides a comprehensive set of functions for string manipulation. The strlen() function returns the length of a string, while strcpy() copies one string to another. String concatenation is performed using strcat(), and strcmp() compares two strings lexicographically. Additional functions include strrev() to reverse a string, strupr() to convert to uppercase, and strlwr() to convert to lowercase.

**Mathematical Functions (math.h)**

The math library provides elementary and advanced mathematical operations. Key functions include sqrt() for square root, pow() for exponentiation, abs() for absolute value of integers, fabs() for absolute value of floating-point numbers, ceil() for rounding up, floor() for rounding down, and trigonometric functions such as sin(), cos(), and tan() along with their inverse counterparts.

**Character Functions (ctype.h)**

Character classification and conversion functions are provided by ctype.h. The isalpha() function checks if a character is alphabetic, isdigit() checks for digits, isupper() and islower() check case, and tolower() and toupper() perform case conversion. These functions are particularly useful for input validation and data processing.

**Memory Allocation Functions (stdlib.h)**

The stdlib.h header contains memory management functions essential for dynamic memory allocation. malloc() allocates a specified number of bytes, calloc() allocates memory for an array with initialization to zero, realloc() adjusts previously allocated memory, and free() releases allocated memory. Proper use of these functions is critical for preventing memory leaks.

**Utility Functions (stdlib.h)**

Additional utility functions include atoi(), atol(), and atof() for converting strings to integer, long, and floating-point numbers respectively. The exit() function terminates program execution, while system() allows execution of operating system commands.

## Examples

### Example 1: String Manipulation Program

Write a program to accept a string from the user, convert it to uppercase, find its length, and display the results.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char str[100], upper_str[100];
    int length;
    
    printf("Enter a string: ");
    gets(str);
    
    // Find length using strlen()
    length = strlen(str);
    printf("Length of string: %d\n", length);
    
    // Copy string using strcpy()
    strcpy(upper_str, str);
    
    // Convert to uppercase using strupr()
    strupr(upper_str);
    printf("Uppercase: %s\n", upper_str);
    
    // Convert back to lowercase using strlwr()
    strlwr(upper_str);
    printf("Lowercase: %s\n", upper_str);
    
    return 0;
}
```

**Output:**
```
Enter a string: Hello World
Length of string: 11
Uppercase: HELLO WORLD
Lowercase: hello world
```

### Example 2: Mathematical Operations Program

Write a program to calculate the square root of a number and raise it to a power using mathematical functions.

```c
#include <stdio.h>
#include <math.h>

int main() {
    double num, result, power;
    int exponent;
    
    printf("Enter a number: ");
    scanf("%lf", &num);
    
    printf("Enter exponent: ");
    scanf("%d", &exponent);
    
    // Calculate square root using sqrt()
    result = sqrt(num);
    printf("Square root of %.2f = %.2f\n", num, result);
    
    // Calculate power using pow()
    power = pow(num, exponent);
    printf("%.2f raised to power %d = %.2f\n", num, exponent, power);
    
    // Demonstrate ceil() and floor()
    double value = 7.8;
    printf("ceil(%.1f) = %.1f\n", value, ceil(value));
    printf("floor(%.1f) = %.1f\n", value, floor(value));
    
    return 0;
}
```

**Output:**
```
Enter a number: 16
Enter exponent: 3
Square root of 16.00 = 4.00
16.00 raised to power 3 = 4096.00
ceil(7.8) = 8.0
floor(7.8) = 7.0
```

### Example 3: Character Classification Program

Write a program to accept a character and check whether it is uppercase, lowercase, digit, or special character.

```c
#include <stdio.h>
#include <ctype.h>

int main() {
    char ch;
    
    printf("Enter a character: ");
    scanf("%c", &ch);
    
    // Check character type using ctype.h functions
    if (isalpha(ch)) {
        printf("'%c' is an alphabetic character\n", ch);
        if (isupper(ch))
            printf("It is uppercase\n");
        else
            printf("It is lowercase\n");
    }
    else if (isdigit(ch))
        printf("'%c' is a digit\n", ch);
    else
        printf("'%c' is a special character\n", ch);
    
    // Convert to uppercase
    printf("Uppercase: %c\n", toupper(ch));
    // Convert to lowercase
    printf("Lowercase: %c\n", tolower(ch));
    
    return 0;
}
```

**Output:**
```
Enter a character: A
'A' is an alphabetic character
It is uppercase
Uppercase: A
Lowercase: a
```

## Exam Tips

1. **ALWAYS include the correct header file** before using any built-in function. This is a common source of compilation errors. Remember that stdio.h is required for printf and scanf, string.h for string functions, math.h for mathematical functions, and ctype.h for character functions.

2. **Understanding function return types** is crucial. Functions like strlen() return size_t (or int in some implementations), while mathematical functions like sqrt() and pow() return double. Always store the return value in an appropriate variable type.

3. **String functions require character arrays**, not string literals, for manipulation. Functions like strcpy() and strcat() need destination arrays large enough to hold the result.

4. **The difference between abs() and fabs()**: abs() works with integers, while fabs() is required for floating-point numbers. Using the wrong function leads to incorrect results.

5. **scanf() requires the address of variables**, so always use the ampersand (&) operator with scanf for primitive types. For strings, the array name itself serves as the address.

6. **Memory allocation functions return void pointers**, which should be cast to the appropriate pointer type. Always check if malloc() or calloc() returns NULL before using the allocated memory.

7. **Built-in functions are more efficient** than user-defined implementations because they are optimized at the library level. Always prefer using library functions over writing custom code for common operations.

8. **For string comparison, use strcmp()** and never use the == operator. The == operator compares addresses, not string contents. strcmp() returns 0 for equal strings, negative for first string less than second, and positive for first string greater than second.

9. **Remember the purpose of key functions**: strlen counts characters excluding null terminator, strcpy includes null terminator, strcat appends source to destination, and strcmp performs case-sensitive comparison.

10. **Practical examination questions** frequently ask students to write programs using built-in functions for string reversal, palindrome checking, string copying, concatenation, and mathematical calculations. Practice these thoroughly.