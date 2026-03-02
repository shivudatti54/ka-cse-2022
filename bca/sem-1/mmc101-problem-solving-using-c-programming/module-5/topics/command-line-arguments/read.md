# Command Line Arguments in C Programming


## Table of Contents

- [Command Line Arguments in C Programming](#command-line-arguments-in-c-programming)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Understanding argc and argv](#understanding-argc-and-argv)
  - [Argument Processing Mechanism](#argument-processing-mechanism)
  - [Passing Different Types of Data](#passing-different-types-of-data)
  - [Handling Options and Flags](#handling-options-and-flags)
- [Examples](#examples)
  - [Example 1: Basic Program to Display Arguments](#example-1-basic-program-to-display-arguments)
  - [Example 2: Calculator Using Command Line Arguments](#example-2-calculator-using-command-line-arguments)
  - [Example 3: File Processing with Command Line Arguments](#example-3-file-processing-with-command-line-arguments)
- [Exam Tips](#exam-tips)

## Introduction

Command line arguments provide a powerful mechanism for passing data to C programs at the time of execution. Instead of relying solely on interactive input through scanf or other input functions, command line arguments allow programs to receive values directly from the terminal or command prompt during program launch. This feature is extensively used in real-world software development, from simple utility programs to complex system applications.

In the context of problem solving using C programming, command line arguments enable the creation of more flexible and automated solutions. Consider scenarios where you need to process multiple files, configure program behavior, or integrate your program with shell scripts and other software tools. Command line arguments make all of this possible by establishing a direct communication channel between the operating system and your program at runtime.

The University of Delhi Computer Science curriculum emphasizes command line arguments as an essential skill, particularly because many practical programming assignments and laboratory examinations require students to implement programs that accept external parameters. Understanding this topic not only helps in academic success but also prepares students for professional software development where command-line interfaces remain prevalent.

## Key Concepts

### Understanding argc and argv

Every C program that accepts command line arguments must define two parameters in the main function: argc (argument count) and argv (argument vector). The main function signature for such programs is:

```c
int main(int argc, char *argv[])
```

The parameter argc (argument count) is an integer that stores the total number of arguments passed to the program, including the program name itself. This value is always at least one because the first argument is always the program's executable name.

The parameter argv (argument vector) is an array of character pointers (strings). Each element of this array points to a null-terminated string representing an individual argument. By convention:
- argv[0] contains the program name or path
- argv[1] through argv[argc-1] contain the actual arguments
- argv[argc] is always NULL (a sentinel value)

### Argument Processing Mechanism

When you execute a program from the command line, the shell parses the entire command line string and passes individual arguments to your program. The operating system populates the argc and argv parameters before your main function is invoked. Arguments are typically separated by whitespace, and if an argument itself contains spaces, it must be enclosed in quotes.

For example, executing `./myprogram hello world 123` results in:
- argc = 4
- argv[0] = "./myprogram" (or the program path)
- argv[1] = "hello"
- argv[2] = "world"
- argv[3] = "123"

### Passing Different Types of Data

Since all command line arguments are received as character strings, numeric and other data types require conversion. The C standard library provides functions like atoi() for integer conversion, atof() for floating-point conversion, and strtol() for more robust integer parsing with error checking.

For integer arguments:
```c
int num = atoi(argv[1]);
```

For floating-point arguments:
```c
double value = atof(argv[1]);
```

### Handling Options and Flags

Many command line programs support flags (like -v for verbose or -o for output) and options with values (like -f filename). This requires parsing the argv array to identify and extract these parameters. The getopt() function from POSIX libraries provides a standardized way to handle option parsing, though for basic DU syllabus requirements, manual parsing is typically expected.

## Examples

### Example 1: Basic Program to Display Arguments

Write a program that displays all command line arguments along with their indices.

```c
#include <stdio.h>

int main(int argc, char *argv[])
{
    printf("Total arguments: %d\n", argc);
    
    for (int i = 0; i < argc; i++)
    {
        printf("argv[%d] = %s\n", i, argv[i]);
    }
    
    return 0;
}
```

**Execution:** `./display_args one two three four`

**Output:**
```
Total arguments: 5
argv[0] = ./display_args
argv[1] = one
argv[2] = two
argv[3] = three
argv[4] = four
```

### Example 2: Calculator Using Command Line Arguments

Create a calculator program that performs basic arithmetic operations using command line arguments. The program should accept three parameters: two numbers and an operator.

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Check minimum number of arguments
    if (argc != 4)
    {
        printf("Usage: %s <number1> <operator> <number2>\n", argv[0]);
        printf("Operators: + - * /\n");
        return 1;
    }
    
    // Convert string arguments to numbers
    double num1 = atof(argv[1]);
    char operator = argv[2][0];  // First character of the operator string
    double num2 = atof(argv[3]);
    double result;
    
    // Perform the operation
    switch (operator)
    {
        case '+':
            result = num1 + num2;
            printf("%.2f + %.2f = %.2f\n", num1, num2, result);
            break;
        case '-':
            result = num1 - num2;
            printf("%.2f - %.2f = %.2f\n", num1, num2, result);
            break;
        case '*':
            result = num1 * num2;
            printf("%.2f * %.2f = %.2f\n", num1, num2, result);
            break;
        case '/':
            if (num2 == 0)
            {
                printf("Error: Division by zero!\n");
                return 1;
            }
            result = num1 / num2;
            printf("%.2f / %.2f = %.2f\n", num1, num2, result);
            break;
        default:
            printf("Error: Invalid operator '%c'\n", operator);
            return 1;
    }
    
    return 0;
}
```

**Execution:** `./calculator 25 + 17`

**Output:**
```
25.00 + 17.00 = 42.00
```

### Example 3: File Processing with Command Line Arguments

Write a program that accepts a filename as a command line argument and displays its contents along with line numbers.

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Validate command line arguments
    if (argc != 2)
    {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }
    
    // Open the file specified as command line argument
    FILE *fp = fopen(argv[1], "r");
    
    if (fp == NULL)
    {
        printf("Error: Cannot open file '%s'\n", argv[1]);
        return 1;
    }
    
    // Read and display file contents with line numbers
    char buffer[1000];
    int line_number = 1;
    
    printf("Contents of '%s':\n", argv[1]);
    printf("------------------------\n");
    
    while (fgets(buffer, sizeof(buffer), fp) != NULL)
    {
        printf("%4d: %s", line_number, buffer);
        line_number++;
    }
    
    fclose(fp);
    return 0;
}
```

**Execution:** `./showfile data.txt`

**Output:**
```
Contents of 'data.txt':
------------------------
   1: Hello, this is a test file.
   2: Command line arguments make programs flexible.
   3: This is the third line.
```

## Exam Tips

1. **REMEMBER THE BASICS**: argc always includes the program name itself, so argc = 1 means no additional arguments were passed beyond the program name.

2. **argv[0] IS ALWAYS PRESENT**: Never assume argv[1] exists without checking argc first. Always validate argc before accessing argv[1] or higher indices to avoid segmentation faults.

3. **ALL ARGUMENTS ARE STRINGS**: Command line arguments are character arrays (strings). Use atoi(), atof(), or strtol() for numeric conversion. Remember that atoi() returns 0 on failure, which may be ambiguous if 0 is a valid input.

4. **CHAR *argv[] IS EQUIVALENT TO CHAR **argv**: These two declarations are identical in function signature. Understanding this equivalence helps in reading different code styles.

5. **WHITESPACE SEPARATION**: By default, command line arguments are separated by whitespace. If an argument contains spaces, it must be quoted: `./program "hello world"`.

6. **COMMON ERROR CHECKING**: Always check argc before accessing argv indices beyond 0. Common exam questions ask you to identify bugs in code that fails to perform this validation.

7. **EXIT STATUS MATTERS**: Programs can return different exit codes. Returning 0 typically indicates success, while non-zero values indicate errors. This is useful for shell script integration.

8. **SOME FUNCTIONS SUPPORT ADDITIONAL PARAMETERS**: The main function can also accept a third parameter for environment variables: `int main(int argc, char *argv[], char *envp[])`. Though not always required, knowing this shows deeper understanding.