# Function Definition And Call


## Table of Contents

- [Function Definition And Call](#function-definition-and-call)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Function Definition](#function-definition)
  - [Function Call](#function-call)
  - [Actual vs Formal Parameters](#actual-vs-formal-parameters)
  - [Return Statement](#return-statement)
  - [Scope and Lifetime of Variables](#scope-and-lifetime-of-variables)
  - [Function Prototype](#function-prototype)
- [Examples](#examples)
  - [Example 1: Simple Function to Calculate Factorial](#example-1-simple-function-to-calculate-factorial)
  - [Example 2: Function with Multiple Parameters](#example-2-function-with-multiple-parameters)
  - [Example 3: Void Function with Pass-by-Value Demonstration](#example-3-void-function-with-pass-by-value-demonstration)
- [Exam Tips](#exam-tips)

## Introduction

Functions are the fundamental building blocks of structured programming in C. A function is a self-contained block of code that performs a specific task and can be called from other parts of a program. The concept of functions enables programmers to break down complex problems into smaller, manageable modules, making code more organized, reusable, and easier to debug.

In the context of Problem Solving Using C Programming, understanding function definition and function call is essential for implementing modular programming paradigms. Functions allow us to encapsulate logic, avoid code duplication, and create libraries of reusable components. Every C program contains at least one function—the main() function—where execution begins. However, professional C programs typically define multiple functions to separate concerns and improve maintainability.

The importance of functions extends beyond mere code organization. They enable top-down design, where a complex problem is decomposed into simpler sub-problems, each solved by a dedicated function. This approach aligns perfectly with the problem-solving methodology taught in University of Delhi's Computer Science curriculum, preparing students to tackle real-world programming challenges efficiently.

## Key Concepts

### Function Definition

A function definition specifies the complete implementation of a function, including its return type, name, parameters, and the function body containing executable statements. The general syntax for function definition in C is:

```c
return_type function_name(parameter_list) {
    // declarations
    // statements
    // return statement (if return_type is not void)
}
```

The return_type specifies the data type of the value that the function returns to the calling function. If a function does not return any value, the return_type should be declared as void. The function_name must be a valid C identifier and should ideally reflect the purpose of the function. The parameter_list (also called formal parameters) declares the variables that receive values from the calling function, enclosed in parentheses.

The function body is a compound statement (enclosed in braces) that contains variable declarations and executable statements. When the function returns a value, the return statement must be included with an expression of the appropriate type.

### Function Call

A function call is the mechanism by which control transfers from the calling function to the called function. When a function is called, the following sequence occurs: arguments (actual parameters) are evaluated, their values are copied to the formal parameters, execution begins at the first statement of the called function, and upon completion, control returns to the point immediately following the call.

The syntax for function call is:

```c
function_name(argument_list);
```

Arguments (actual parameters) must match the formal parameters in number, type, and order. If the function returns a value, the function call can be used as an expression or assigned to a variable.

### Actual vs Formal Parameters

Understanding the distinction between actual parameters (arguments) and formal parameters is crucial. Actual parameters are the variables or expressions passed to the function at the time of calling, while formal parameters are the variables declared in the function definition that receive copies of the actual parameters.

In C, parameters are passed by value, meaning a copy of the actual parameter's value is made and assigned to the formal parameter. Any modifications to the formal parameter inside the function do not affect the original variable in the calling function.

### Return Statement

The return statement terminates the execution of a function and optionally returns a value to the calling function. Its syntax is:

```c
return expression;
```

or simply:

```c
return;
```

The expression's type must be compatible with the function's return type. A function can have multiple return statements, though only one executes during a particular call. Functions with void return type use return without a value to exit early.

### Scope and Lifetime of Variables

Variables inside a function have block scope—they are visible only within that function. Automatic variables (declared inside the function without static keyword) are created when the function is called and destroyed when it returns. Static variables, however, retain their values between function calls.

### Function Prototype

Although not strictly required in older C standards, declaring a function prototype before its definition or call is considered good practice. A function prototype declares the function's signature (return type and parameter types) to the compiler, enabling type checking and implicit conversions.

## Examples

### Example 1: Simple Function to Calculate Factorial

Problem: Write a function to calculate the factorial of a non-negative integer and demonstrate its call.

```c
#include <stdio.h>

// Function definition
int factorial(int n) {
    int result = 1;
    for (int i = 1; i <= n; i++) {
        result = result * i;
    }
    return result;
}

int main() {
    int number, fact;
    
    printf("Enter a non-negative integer: ");
    scanf("%d", &number);
    
    if (number < 0) {
        printf("Factorial is not defined for negative numbers.\n");
    } else {
        // Function call
        fact = factorial(number);
        printf("Factorial of %d is %d\n", number, fact);
    }
    
    return 0;
}
```

Step-by-step execution:
1. User enters a number, say 5
2. The function call `factorial(5)` transfers control to the factorial function
3. Inside factorial, n receives value 5 (copy of actual parameter)
4. The loop calculates 1×2×3×4×5 = 120
5. The return statement sends 120 back to main
6. The value 120 is assigned to variable fact
7. Control continues in main after the function call

Output for input 5:
```
Factorial of 5 is 120
```

### Example 2: Function with Multiple Parameters

Problem: Write a function that takes three integers and returns their average.

```c
#include <stdio.h>

// Function definition with three parameters
float calculate_average(int a, int b, int c) {
    float avg;
    avg = (float)(a + b + c) / 3;
    return avg;
}

int main() {
    int x = 10, y = 20, z = 30;
    float result;
    
    // Function call with three arguments
    result = calculate_average(x, y, z);
    
    printf("Average of %d, %d, and %d is %.2f\n", x, y, z, result);
    
    return 0;
}
```

Key observations:
- Three actual parameters (x, y, z) are passed to three formal parameters (a, b, c)
- Parameters are passed by value—a copy is made
- The function returns a float value which is captured in the main function
- Type casting (float) ensures proper floating-point division

Output:
```
Average of 10, 20, and 30 is 20.00
```

### Example 3: Void Function with Pass-by-Value Demonstration

Problem: Write a function that attempts to swap two numbers and demonstrate that changes don't affect the original values.

```c
#include <stdio.h>

// Void function - does not return a value
void swap_attempt(int a, int b) {
    int temp;
    printf("Inside swap_attempt - Before swap: a = %d, b = %d\n", a, b);
    temp = a;
    a = b;
    b = temp;
    printf("Inside swap_attempt - After swap: a = %d, b = %d\n", a, b);
}

int main() {
    int x = 5, y = 10;
    
    printf("In main - Before function call: x = %d, y = %d\n", x, y);
    
    // Function call
    swap_attempt(x, y);
    
    printf("In main - After function call: x = %d, y = %d\n", x, y);
    
    return 0;
}
```

Output:
```
In main - Before function call: x = 5, y = 10
Inside swap_attempt - Before swap: a = 5, b = 10
Inside swap_attempt - After swap: a = 10, b = 5
In main - After function call: x = 5, y = 10
```

This example demonstrates that in C, parameters are passed by value. The variables x and y in main remain unchanged because only their copies (a and b) were swapped inside the function.

## Exam Tips

1. MEMORIZE THE ANATOMY OF A FUNCTION: Remember that a function consists of return type, function name, parameter list, and function body. All four components are essential for a valid function definition.

2. UNDERSTAND PASS-BY-VALUE: In C, all arguments are passed by value. This is a frequently tested concept—be prepared to trace how changes inside a function do not affect the original arguments.

3. DIFFERENTIATE BETWEEN FORMAL AND ACTUAL PARAMETERS: Formal parameters are defined in the function signature; actual parameters are passed during the function call. They must match in number, type, and order.

4. RETURN STATEMENT RULES: A function with a non-void return type must return a value of compatible type. A function with void return type may use return without a value to exit early, or omit the return statement entirely.

5. FUNCTION PROTOTYPE PLACEMENT: When writing programs, declare function prototypes before main() if the function is defined after main(). This helps the compiler perform type checking.

6. TRACE PROGRAM EXECUTION: Practice tracing function calls step-by-step, showing how control transfers between functions and how return values are handled.

7. COMMON ERRORS TO AVOID: Forgetting to include return statement in non-void functions, mismatching parameter types between function call and definition, and incorrect function name spelling are common mistakes that cost marks in exams.

8. PRACTICE WRITING FUNCTION DEFINITIONS: Write at least 10 different function definitions covering various return types, parameter counts, and purposes to build confidence for exam questions.