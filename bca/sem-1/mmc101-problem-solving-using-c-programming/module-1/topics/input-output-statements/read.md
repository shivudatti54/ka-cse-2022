# Input Output Statements in C Programming


## Table of Contents

- [Input Output Statements in C Programming](#input-output-statements-in-c-programming)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [The stdio.h Header File](#the-stdioh-header-file)
  - [printf() Function - Formatted Output](#printf-function---formatted-output)
  - [scanf() Function - Formatted Input](#scanf-function---formatted-input)
  - [Character I/O Functions](#character-io-functions)
  - [String I/O Functions](#string-io-functions)
  - [Escape Sequences](#escape-sequences)
- [Examples](#examples)
  - [Example 1: Basic printf() Usage](#example-1-basic-printf-usage)
  - [Example 2: Using scanf() with Multiple Inputs](#example-2-using-scanf-with-multiple-inputs)
  - [Example 3: Using getchar() for Character Input](#example-3-using-getchar-for-character-input)
- [Exam Tips](#exam-tips)

## Introduction

Input and Output operations form the backbone of any interactive computer program. In C programming, the Standard Input/Output library (stdio.h) provides a comprehensive set of functions that enable communication between the program and external devices, typically the keyboard and monitor. Understanding these I/O functions is essential for any C programmer as they serve as the primary means of interacting with users and processing data.

The C language follows a philosophy of treating input and output as stream-based operations. When a C program begins execution, three streams are automatically opened: standard input (stdin), standard output (stdout), and standard error (stderr). The stdio.h header file contains all the function prototypes and macros necessary for performing formatted and unformatted I/O operations. Without these functions, programs would be unable to receive data from users or display results, making them essentially useless in practical applications.

This topic covers the fundamental I/O functions in C: printf() for formatted output, scanf() for formatted input, getchar() and putchar() for character I/O, and gets() and puts() for string handling. Mastery of these functions is crucial for the DU Computer Science curriculum and forms the foundation for more advanced programming concepts.

## Key Concepts

### The stdio.h Header File

The standard input/output header file stdio.h must be included at the beginning of any program that performs I/O operations. This header provides the function definitions, macros, and type definitions required for I/O functions. The '#include <stdio.h>' directive informs the preprocessor to insert the contents of the stdio.h header into the program before compilation.

### printf() Function - Formatted Output

The printf() function is used to display output to the standard output device (typically the monitor). Its general syntax is:

```c
printf("format string", argument1, argument2, ...);
```

The format string can contain:
- Ordinary characters that are printed verbatim
- Escape sequences for special characters
- Format specifiers that indicate how arguments should be printed

**Format Specifiers:**
- %d or %i: Signed integer
- %u: Unsigned integer
- %f: Floating-point number
- %c: Character
- %s: String
- %p: Pointer address
- %x or %X: Hexadecimal number
- %o: Octal number
- %%: Print a percent sign

**Precision Modifiers:**
- %5d: Print integer in a field of width 5 (right-aligned)
- %-5d: Print integer in a field of width 5 (left-aligned)
- %.2f: Print floating-point with 2 decimal places

### scanf() Function - Formatted Input

The scanf() function reads data from standard input and stores it at the memory locations specified by its arguments. Its general syntax is:

```c
scanf("format string", &argument1, &argument2, ...);
```

The ampersand (&) operator is crucial as it provides the memory address of the variable where the input should be stored. For strings (character arrays), the ampersand is not required since the array name already represents the base address.

**Important Considerations for scanf():**
- The format specifiers in scanf() should match the data types of variables exactly
- Whitespace in the format string causes scanf() to skip any amount of whitespace in input
- Non-whitespace characters in the format string require exact matching in input
- scanf() returns the number of successfully read items

### Character I/O Functions

**getchar()**: Reads a single character from stdin. It waits for user input and returns the character as an integer (to accommodate EOF).

```c
int ch;
ch = getchar();
```

**putchar()**: Outputs a single character to stdout.

```c
putchar('A');
putchar(ch);
```

### String I/O Functions

**gets()**: Reads a line of text from stdin until a newline or EOF is encountered. Note: This function is dangerous due to buffer overflow and has been removed from C11. Use fgets() instead.

**puts()**: Displays a string followed by a newline character.

```c
char name[50];
gets(name);  // Use fgets(name, 50, stdin); instead
puts(name);
```

### Escape Sequences

Escape sequences allow printing of special characters:

- \n: Newline
- \t: Horizontal tab
- \r: Carriage return
- \b: Backspace
- \a: Alert/bell
- \\: Backslash
- \': Single quote
- \": Double quote
- \?: Question mark

## Examples

### Example 1: Basic printf() Usage

Write a program to display a student's information:

```c
#include <stdio.h>

int main() {
    int rollNo = 101;
    char name[] = "Priya Sharma";
    float marks = 87.5;
    
    printf("Student Details\n");
    printf("---------------\n");
    printf("Roll Number: %d\n", rollNo);
    printf("Name: %s\n", name);
    printf("Marks: %.2f\n", marks);
    
    return 0;
}
```

**Output:**
```
Student Details
---------------
Roll Number: 101
Name: Priya Sharma
Marks: 87.50
```

### Example 2: Using scanf() with Multiple Inputs

Write a program to calculate the area of a rectangle:

```c
#include <stdio.h>

int main() {
    float length, width, area;
    
    printf("Enter length of rectangle: ");
    scanf("%f", &length);
    
    printf("Enter width of rectangle: ");
    scanf("%f", &width);
    
    area = length * width;
    printf("Area of rectangle = %.2f square units\n", area);
    
    return 0;
}
```

**Sample Execution:**
```
Enter length of rectangle: 5.5
Enter width of rectangle: 3.2
Area of rectangle = 17.60 square units
```

### Example 3: Using getchar() for Character Input

Write a program to convert lowercase letter to uppercase:

```c
#include <stdio.h>

int main() {
    char ch;
    
    printf("Enter a lowercase letter: ");
    ch = getchar();
    
    // Convert to uppercase using ASCII arithmetic
    if (ch >= 'a' && ch <= 'z') {
        ch = ch - 32;  // ASCII difference between lowercase and uppercase
        printf("Uppercase letter: %c\n", ch);
    } else {
        printf("Please enter a lowercase letter!\n");
    }
    
    return 0;
}
```

## Exam Tips

1. Remember to include '#include <stdio.h>' for all I/O operations - this is a common mistake that leads to compilation errors.

2. Always use the address-of operator (&) with scanf() for all variable types except character arrays (strings).

3. The return value of scanf() indicates the number of successfully read items - use this for input validation.

4. Format specifiers must exactly match the data types: use %d for int, %f for float, %lf for double, %c for char.

5. For precise floating-point output, use format specifiers like %.2f to control decimal places.

6. The difference between %d and %i in printf() is negligible, but %i in scanf() can interpret hexadecimal (0x) and octal (0) prefixes.

7. getchar() returns an int, not a char, to accommodate the EOF constant - store the result in an int variable.

8. Escape sequences begin with a backslash (\) and are interpreted specially - \n moves to new line, \t provides tab spacing.

9. Left-justify output using the minus sign in format specifier: %-10s aligns text left within 10-character width.

10. For string input with spaces, scanf() with %s stops at whitespace - use fgets() for multi-word strings.