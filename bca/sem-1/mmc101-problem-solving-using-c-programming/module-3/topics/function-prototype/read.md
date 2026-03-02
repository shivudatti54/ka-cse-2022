# Function Prototype in C


## Table of Contents

- [Function Prototype in C](#function-prototype-in-c)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [What is a Function Prototype?](#what-is-a-function-prototype)
  - [Why Do We Need Function Prototypes?](#why-do-we-need-function-prototypes)
  - [Components of a Function Prototype](#components-of-a-function-prototype)
  - [Function Prototypes with Arrays](#function-prototypes-with-arrays)
  - [Function Prototypes with Pointers](#function-prototypes-with-pointers)
- [Examples](#examples)
  - [Example 1: Basic Function Prototype](#example-1-basic-function-prototype)
  - [Example 2: Function Prototype with Different Parameter Types](#example-2-function-prototype-with-different-parameter-types)
  - [Example 3: Function Prototype with Pointers](#example-3-function-prototype-with-pointers)
- [Exam Tips](#exam-tips)

## Introduction

A function prototype in C is a declaration that provides information about the function's name, return type, and parameter list to the compiler before the actual function definition appears in the program. When you write a function prototype, you are essentially telling the compiler: "This function exists, it returns this type of value, and it accepts these arguments." This becomes crucial in larger programs where functions may be defined after they are called, which is the standard practice in modular programming.

The function prototype serves as an interface between the function caller and the function definition. It enables the compiler to perform type checking at compile time, ensuring that the arguments passed to a function match the expected parameter types. Without function prototypes, the compiler would assume default return types (typically int) and could lead to subtle bugs that are difficult to detect. In modern C programming, function prototypes are not just recommended but essential for writing robust, maintainable code.

Understanding function prototypes is particularly important for DU students because this concept appears frequently in end-semester examinations. The ability to correctly declare and use function prototypes demonstrates a student's understanding of C's type system and function call mechanics, which are foundational skills for any programmer.

## Key Concepts

### What is a Function Prototype?

A function prototype is a declaration statement that specifies the function's return type, name, and parameter types (and optionally parameter names) before the actual function definition. It tells the compiler everything it needs to know to validate function calls correctly.

The general syntax of a function prototype is:

```
return_type function_name(parameter_type1 parameter_name1, parameter_type2 parameter_name2, ...);
```

Or without parameter names:

```
return_type function_name(parameter_type1, parameter_type2, ...);
```

Both forms are valid, but including parameter names improves code readability.

### Why Do We Need Function Prototypes?

The primary purpose of function prototypes is to enable forward referencing. In C, functions are typically defined after the main() function or in a different source file. Without a prototype, the compiler would not know how to handle function calls that appear before the function definition.

Consider this scenario: if you call a function calculateSum() inside main() but define calculateSum() after main(), the compiler would generate an error or assume incorrect return type without the prototype. The function prototype resolves this by telling the compiler in advance what the function looks like.

Additionally, function prototypes provide automatic type conversion. If you pass an argument of type float to a function expecting a double parameter, the compiler can perform the necessary conversion based on the prototype information.

### Components of a Function Prototype

**Return Type**: Specifies the data type of the value returned by the function. If the function does not return anything, the return type is void. For example, a function that prints values might have a void return type, while a function that computes a sum would return int or float.

**Function Name**: Must be a valid C identifier. By convention, function names in C are lowercase with underscores for readability (e.g., calculate_area, print_message).

**Parameter List**: Each parameter must have a type specified. Parameters can be of any data type including int, float, char, arrays, pointers, or even void (meaning no parameters). The parameter list in the prototype must match the parameter list in the definition.

**Void Parameter**: When a function accepts no parameters, use void in the parameter list. For example: `int getValue(void);` This explicitly indicates that the function takes no arguments, distinguishing it from a function where the parameter list is simply empty (which is old-style C and means unspecified parameters).

### Function Prototypes with Arrays

When passing arrays to functions, the array parameter can be specified in several ways. The most common approaches include using pointer notation `int func(int *arr)`, using array notation `int func(int arr[])`, or specifying array size `int func(int arr[10])`. The compiler treats all three forms identically since arrays are passed as pointers in C.

### Function Prototypes with Pointers

Pointer parameters in prototypes are declared using the pointer operator *. For example, a function that swaps two integers using pointers would have prototype: `void swap(int *x, int *y);` This tells the compiler that the function expects memory addresses, not integer values.

## Examples

### Example 1: Basic Function Prototype

```c
#include <stdio.h>

// Function prototypes
int add(int a, int b);
void printResult(int result);

int main() {
    int x = 10, y = 20;
    int sum = add(x, y);
    printResult(sum);
    return 0;
}

// Function definitions
int add(int a, int b) {
    return a + b;
}

void printResult(int result) {
    printf("The sum is: %d\n", result);
}
```

**Output:**
```
The sum is: 30
```

In this example, the function prototypes `int add(int a, int b);` and `void printResult(int result);` are declared before main(). This allows the compiler to verify that calls to these functions match their declarations. The add function returns an integer, while printResult returns void (nothing).

### Example 2: Function Prototype with Different Parameter Types

```c
#include <stdio.h>

// Function prototypes with different types
double calculateAverage(int a, int b, int c);
float calculatePercentage(float obtained, float total);
void displayGrade(char grade);

int main() {
    int m1 = 85, m2 = 90, m3 = 78;
    float marks = 450.0, total = 500.0;
    
    double avg = calculateAverage(m1, m2, m3);
    float perc = calculatePercentage(marks, total);
    
    printf("Average: %.2f\n", avg);
    printf("Percentage: %.2f%%\n", perc);
    
    if (perc >= 90)
        displayGrade('A');
    else if (perc >= 80)
        displayGrade('B');
    else
        displayGrade('C');
    
    return 0;
}

double calculateAverage(int a, int b, int c) {
    return (a + b + c) / 3.0;
}

float calculatePercentage(float obtained, float total) {
    return (obtained / total) * 100;
}

void displayGrade(char grade) {
    printf("Grade: %c\n", grade);
}
```

**Output:**
```
Average: 84.33
Percentage: 90.00%
Grade: A
```

This example demonstrates function prototypes with mixed data types. Note how the compiler automatically handles type conversion: when integers are passed to calculateAverage which expects int parameters, they are used directly, while the division by 3.0 promotes the result to double.

### Example 3: Function Prototype with Pointers

```c
#include <stdio.h>

// Function prototype with pointer parameters
void swap(int *x, int *y);
void updateValue(int *ptr, int newValue);

int main() {
    int num1 = 25, num2 = 40;
    
    printf("Before swap: num1 = %d, num2 = %d\n", num1, num2);
    swap(&num1, &num2);
    printf("After swap: num1 = %d, num2 = %d\n", num1, num2);
    
    int value = 100;
    printf("Before update: value = %d\n", value);
    updateValue(&value, 250);
    printf("After update: value = %d\n", value);
    
    return 0;
}

void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

void updateValue(int *ptr, int newValue) {
    *ptr = newValue;
}
```

**Output:**
```
Before swap: num1 = 25, num2 = 40
After swap: num1 = 40, num2 = 25
Before update: value = 100
After update: value = 250
```

This example shows function prototypes where parameters are pointers. The prototype `void swap(int *x, int *y);` indicates that the function expects addresses of integer variables. When calling such functions, the address-of operator (&) must be used, and inside the function, the dereference operator (*) accesses the actual values.

## Exam Tips

1. **Remember the semicolon**: A common mistake is forgetting the semicolon at the end of the function prototype. The prototype is a declaration, not a definition, so it must end with a semicolon.

2. **Parameter names are optional**: Both `int add(int a, int b);` and `int add(int, int);` are valid prototypes. Including names improves readability and helps during debugging.

3. **void as parameter**: Always use `void` when a function takes no parameters. Writing `int func();` in modern C means unspecified parameters, not no parameters. Use `int func(void);` for functions that accept nothing.

4. **Match prototype and definition**: The prototype must match the definition exactly in terms of return type, function name, and parameter types. Any mismatch will cause a compilation error or undefined behavior.

5. **Array parameters are pointers**: When you declare `void func(int arr[10])`, the compiler treats it as `void func(int *arr)`. The size specification in the prototype is ignored.

6. **Order of declaration matters**: Place function prototypes either at the beginning of the file or in a header file. They must appear before any function that calls them.

7. **Default integer return (old style)**: In older C without prototypes, functions were assumed to return int. Always explicitly specify the return type to avoid ambiguity and compiler warnings.