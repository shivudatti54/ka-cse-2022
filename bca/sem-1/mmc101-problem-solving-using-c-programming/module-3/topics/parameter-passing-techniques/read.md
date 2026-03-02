# Parameter Passing Techniques in C


## Table of Contents

- [Parameter Passing Techniques in C](#parameter-passing-techniques-in-c)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Pass by Value](#pass-by-value)
  - [Pass by Reference](#pass-by-reference)
  - [Comparison of Techniques](#comparison-of-techniques)
- [Examples](#examples)
  - [Example 1: Pass by Value Demonstration](#example-1-pass-by-value-demonstration)
  - [Example 2: Pass by Reference Using Pointers](#example-2-pass-by-reference-using-pointers)
  - [Example 3: Returning Multiple Values](#example-3-returning-multiple-values)
- [Exam Tips](#exam-tips)

## Introduction

Parameter passing is a fundamental concept in C programming that determines how data is transmitted between the calling function and the called function. When we invoke a function in C, we often need to provide it with data to work with, and the mechanism by which this data is transferred is crucial to understanding how programs behave. The way parameters are passed affects whether changes made inside the function persist after the function returns, making this topic essential for writing correct and efficient C programs.

In the context of modular programming, where complex problems are broken down into smaller, manageable functions, understanding parameter passing becomes critical. C provides two primary parameter passing techniques: Pass by Value and Pass by Reference. Each technique has its own advantages, use cases, and implications for program design. Mastery of these techniques allows programmers to choose the appropriate method based on whether they need data protection, memory efficiency, or the ability to modify caller variables.

This topic forms the bridge between basic function usage and advanced concepts like recursion, pointers, and dynamic memory management. For University of Delhi students preparing for practical examinations and theoretical exams, a thorough understanding of parameter passing techniques is indispensable, as questions on this topic frequently appear in both internal assessments and end semester examinations.

## Key Concepts

### Pass by Value

Pass by Value is the default parameter passing mechanism in C. When a parameter is passed by value, the function receives a copy of the actual argument's value. The function works with this copy, and any modifications made to the parameter inside the function do not affect the original variable in the calling function. This provides data protection, as the original data remains safe from unintended modifications.

The process works as follows: when the function is called, the value of the argument is evaluated and copied into a new memory location (the parameter). The function operates on this local copy, leaving the original unchanged. This technique is particularly useful when you want to prevent accidental modification of the caller's data or when working with simple data types like integers, characters, and floating-point numbers.

One important characteristic of pass by value is that memory is allocated for the copy within the function's scope. For small data types, this overhead is negligible, but for large structures, copying can become computationally expensive. Additionally, since only the value is transmitted, the function cannot return multiple modified values through a single parameter.

### Pass by Reference

Pass by Reference in C is achieved using pointers. Instead of passing the actual value, we pass the memory address (reference) of the variable. The function receives this address and can use it to access and modify the original data stored at that memory location. This technique enables functions to modify caller's variables and allows a function to return multiple values through its parameters.

The implementation involves using the address-of operator (&) when calling the function and the dereference operator (*) inside the function. When you pass a pointer to a function, the pointer itself is passed by value (the pointer copy points to the same memory location as the original), but the data being pointed to can be modified. This distinction between passing the pointer by value and modifying the pointed-to data is crucial for understanding C's memory model.

Pass by reference is essential for efficiently handling large data structures, as only the address (typically 4 or 8 bytes depending on the system) needs to be copied rather than the entire structure. It is also necessary when a function needs to modify multiple variables in the calling scope or when working with dynamically allocated memory.

### Comparison of Techniques

The fundamental difference between pass by value and pass by reference lies in whether the original data can be modified. In pass by value, the original is protected; in pass by reference, modification is possible and often intentional. Memory allocation also differs: pass by value creates a new copy, while pass by reference shares the same memory location. Performance implications favor pass by reference for large data structures, while pass by value is simpler and safer for small, simple data.

## Examples

### Example 1: Pass by Value Demonstration

Consider a program to swap two numbers using pass by value:

```c
#include <stdio.h>

void swap(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
    printf("Inside swap: a = %d, b = %d\n", a, b);
}

int main() {
    int x = 10, y = 20;
    printf("Before swap: x = %d, y = %d\n", x, y);
    swap(x, y);
    printf("After swap: x = %d, y = %d\n", x, y);
    return 0;
}
```

**Output:**
```
Before swap: x = 10, y = 20
Inside swap: a = 20, b = 10
After swap: x = 10, y = 20
```

**Explanation:** The swap function receives copies of x and y. Even though a and b are swapped inside the function, the original variables x and y remain unchanged because only their values were passed, not their memory addresses. This demonstrates the protective nature of pass by value.

### Example 2: Pass by Reference Using Pointers

Now let's implement the same swap using pass by reference:

```c
#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
    printf("Inside swap: *a = %d, *b = %d\n", *a, *b);
}

int main() {
    int x = 10, y = 20;
    printf("Before swap: x = %d, y = %d\n", x, y);
    swap(&x, &y);
    printf("After swap: x = %d, y = %d\n", x, y);
    return 0;
}
```

**Output:**
```
Before swap: x = 10, y = 20
Inside swap: *a = 20, *b = 10
After swap: x = 20, y = 10
```

**Explanation:** The function now receives pointers to x and y. Using the dereference operator (*), it accesses and modifies the original memory locations. After the function call, x and y are actually swapped because the modifications were made to the original variables through their addresses.

### Example 3: Returning Multiple Values

Pass by reference enables functions to return multiple values. This example calculates both the quotient and remainder of a division:

```c
#include <stdio.h>

void divide(int dividend, int divisor, int *quotient, int *remainder) {
    *quotient = dividend / divisor;
    *remainder = dividend % divisor;
}

int main() {
    int num1 = 47, num2 = 5;
    int q, r;
    
    divide(num1, num2, &q, &r);
    printf("Dividend: %d, Divisor: %d\n", num1, num2);
    printf("Quotient: %d, Remainder: %d\n", q, r);
    
    return 0;
}
```

**Output:**
```
Dividend: 47, Divisor: 5
Quotient: 9, Remainder: 2
```

**Explanation:** The divide function cannot return two values using return statement, so we use pass by reference. The addresses of q and r are passed, allowing the function to store results directly in the caller's variables. This is a common pattern in C for functions that need to output multiple values.

## Exam Tips

1. Understand that C uses pass by value by default, and pass by reference is simulated using pointers. This is a common confusion point in examinations.

2. When asked about parameter passing in C, always remember that even pointers are passed by value—the pointer copy points to the same location as the original.

3. In exam questions, carefully distinguish between modifying the pointer itself versus modifying the data it points to. These are different operations with different outcomes.

4. For array parameters, remember that arrays are always passed by reference (as pointers), regardless of whether you use pointer notation or array notation in the function parameter.

5. The address-of operator (&) must be used when calling a function that expects a pointer parameter, and the dereference operator (*) must be used inside to access the actual value.

6. Common exam trap: A function with pass by value parameters cannot modify the caller's variables, while a function with pointer parameters can.

7. When deciding between pass by value and pass by reference, consider three factors: whether modification size ( is needed, dataefficiency), and safety requirements.