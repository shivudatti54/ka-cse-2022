# Introduction to Arrays


## Table of Contents

- [Introduction to Arrays](#introduction-to-arrays)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition and Characteristics of Arrays](#definition-and-characteristics-of-arrays)
  - [Array Declaration and Initialization](#array-declaration-and-initialization)
  - [Memory Representation](#memory-representation)
  - [Accessing Array Elements](#accessing-array-elements)
  - [One-Dimensional vs Multi-Dimensional Arrays](#one-dimensional-vs-multi-dimensional-arrays)
  - [Relationship Between Arrays and Pointers](#relationship-between-arrays-and-pointers)
- [Examples](#examples)
  - [Example 1: Declaring, Initializing, and Accessing Arrays](#example-1-declaring-initializing-and-accessing-arrays)
  - [Example 2: Computing Sum and Average Using Arrays](#example-2-computing-sum-and-average-using-arrays)
  - [Example 3: Finding Maximum and Minimum Values](#example-3-finding-maximum-and-minimum-values)
- [Exam Tips](#exam-tips)

## Introduction

In the realm of computer programming, data structures form the backbone of efficient problem-solving. Among the most fundamental and widely used data structures is the array. When solving real-world computational problems, we frequently encounter situations where we need to store and manipulate multiple values of the same data type—be it a list of student marks, a collection of temperatures recorded over a week, or a sequence of characters forming words. While individual variables can hold single values, they become impractical when dealing with large datasets. Arrays provide an elegant solution to this problem by allowing programmers to store multiple elements of the same type under a single name, accessible through index-based retrieval.

The concept of arrays transcends specific programming languages; it represents a universal approach to organized data storage. In the C programming language, arrays serve as the foundation for more complex data structures and algorithms. Understanding arrays is crucial for any programmer because nearly every non-trivial program utilizes them in some form. From simple tasks like finding the maximum value in a list to complex operations like sorting and searching, arrays provide the mechanism for efficient data management. This topic introduces the fundamental concepts of arrays, their memory representation, declaration syntax, and practical applications in C programming.

For students preparing for University of Delhi examinations, arrays represent a high-weightage topic that frequently appears in both theoretical questions and practical programming assignments. The Internal Assessment component often includes programs requiring array manipulation, while the End Semester Examination tests conceptual understanding through both direct questions and problem-solving scenarios. Mastery of arrays also paves the way for understanding two-dimensional arrays, strings, and various sorting and searching algorithms covered in subsequent topics.

## Key Concepts

### Definition and Characteristics of Arrays

An array is a contiguous collection of elements of the same data type that are stored in memory and accessed using one or more indices. The term "contiguous" is particularly important—it means that all elements of an array occupy consecutive memory locations, which enables efficient access patterns. This contiguous storage distinguishes arrays from other data structures like linked lists, where elements can be scattered throughout memory.

The key characteristics of arrays include FIXED SIZE (determined at compile time in C), HOMOGENEOUS ELEMENTS (all elements must be of the same type), CONTIGUOUS MEMORY STORAGE, ZERO-BASED INDEXING (the first element is accessed using index 0), and RANDOM ACCESS capability (any element can be accessed directly in constant time). These characteristics make arrays ideal for scenarios where fast access to elements is paramount and the number of elements is known beforehand.

### Array Declaration and Initialization

In C programming, array declaration follows a specific syntax that specifies the data type of elements, the array name, and the number of elements. The general form is: data_type array_name[number_of_elements]; For example, int marks[10]; declares an array named marks that can hold 10 integer values. The size specification must be a constant expression in standard C—the size cannot be determined at runtime from user input in older C standards, though C99 introduced variable-length arrays (VLAs) with some limitations.

Array initialization can occur at the time of declaration or through subsequent assignment statements. During declaration, initialization can be performed using an initializer list: int numbers[5] = {10, 20, 30, 40, 50}; If the array is partially initialized, the remaining elements are automatically set to zero. When the array size is omitted in initialization, C automatically determines the size based on the number of initializers: int numbers[] = {10, 20, 30}; creates an array of size 3.

### Memory Representation

Understanding how arrays are stored in memory is fundamental to grasping their behavior in C. When an array is declared, the compiler allocates a contiguous block of memory large enough to hold all elements. For instance, if we declare int arr[5]; on a system where int occupies 4 bytes, the compiler allocates 20 consecutive bytes (5 × 4). The array name (arr) acts as a pointer to the base address—the memory location of the first element.

Consider the array declaration: int marks[5] = {85, 90, 78, 92, 88}; If the base address is 1000 (in decimal), the memory layout would be: marks[0] at address 1000, marks[1] at address 1004, marks[2] at address 1008, marks[3] at address 1012, and marks[4] at address 1016. This predictable memory layout enables constant-time access to any element through the formula: address_of_element = base_address + (index × size_of_element). This mathematical relationship is why arrays provide O(1) or constant time complexity for element access—a critical advantage in performance-critical applications.

### Accessing Array Elements

Array elements are accessed using the index operator [] with the element's position. The syntax array_name[index] retrieves or modifies the element at the specified position. It is crucial to remember that C uses ZERO-BASED INDEXING, meaning the first element is accessed using index 0, not 1. Accessing an index outside the valid range (0 to size-1) results in undefined behavior—this is one of the most common sources of bugs in C programs and can lead to memory corruption or program crashes.

The process of accessing an array element involves computing the memory address using the formula mentioned earlier. When the program executes marks[2], the compiler generates code that calculates the address as base + (2 × sizeof(int)), retrieves the value at that address, and returns it. This computation happens behind the scenes, but understanding the mechanism helps programmers appreciate why arrays are so efficient for random access.

### One-Dimensional vs Multi-Dimensional Arrays

While this introduction focuses primarily on one-dimensional arrays, it is worth noting that C supports multi-dimensional arrays. A two-dimensional array, for example, can be visualized as a table with rows and columns. The declaration int matrix[3][4]; creates a 3×4 matrix with 3 rows and 4 columns, totaling 12 elements. Two-dimensional arrays are stored in row-major order in C, meaning elements in the first row are stored consecutively, followed by elements in the second row, and so on. This storage pattern has implications for cache efficiency and should be considered when optimizing performance-critical code.

### Relationship Between Arrays and Pointers

In C, there is a deep and sometimes confusing relationship between arrays and pointers. The array name, when used in most expressions, decays to a pointer to the first element of the array. This means that arr and &arr[0] evaluate to the same address. However, arrays and pointers are not identical—an array occupies storage for all its elements, while a pointer is simply a variable that stores a memory address. Understanding this distinction becomes crucial when passing arrays to functions, where the array decays to a pointer, losing information about its size.

## Examples

### Example 1: Declaring, Initializing, and Accessing Arrays

Problem: Write a C program to declare an array of 5 integers, initialize it with values {25, 30, 35, 40, 45}, and display all elements along with their indices.

Solution:

```c
#include <stdio.h>

int main() {
    // Declaration and initialization
    int numbers[5] = {25, 30, 35, 40, 45};
    int i;
    
    // Accessing and displaying elements
    printf("Array elements and their indices:\n");
    for (i = 0; i < 5; i++) {
        printf("numbers[%d] = %d\n", i, numbers[i]);
    }
    
    return 0;
}
```

Output:
```
Array elements and their indices:
numbers[0] = 25
numbers[1] = 30
numbers[2] = 35
numbers[3] = 40
numbers[4] = 45
```

Explanation: The program demonstrates three essential operations. First, we declare an integer array of size 5 using int numbers[5]; Second, we initialize it with five values using the initializer list syntax. Third, we use a for loop to iterate through indices 0 to 4, accessing each element using the index operator and printing both the index and value. The loop counter i serves as both the index and the loop control variable, demonstrating the typical pattern for array traversal.

### Example 2: Computing Sum and Average Using Arrays

Problem: Given an array of 6 floating-point numbers representing temperatures recorded over six days, write a program to calculate and display the sum and average of these temperatures.

Solution:

```c
#include <stdio.h>

int main() {
    float temperatures[6] = {22.5, 24.1, 19.8, 21.3, 25.0, 23.7};
    float sum = 0.0, average;
    int i;
    
    // Calculate sum using array elements
    for (i = 0; i < 6; i++) {
        sum = sum + temperatures[i];
    }
    
    // Calculate average
    average = sum / 6;
    
    printf("Temperature readings: ");
    for (i = 0; i < 6; i++) {
        printf("%.1f ", temperatures[i]);
    }
    printf("\n");
    printf("Sum of temperatures: %.2f\n", sum);
    printf("Average temperature: %.2f\n", average);
    
    return 0;
}
```

Output:
```
Temperature readings: 22.5 24.1 19.8 21.3 25.0 23.7 
Sum of temperatures: 136.40
Average temperature: 22.73
```

Explanation: This program illustrates practical use of arrays in data processing. We declare an array to store six temperature values, then use a running sum pattern to calculate the total. The average is computed by dividing the sum by the number of elements (6). Note that we use float for both the array elements and the sum/average variables to maintain precision. The program also demonstrates array traversal for display purposes, showing how to process each element systematically.

### Example 3: Finding Maximum and Minimum Values

Problem: Create an array of 8 integers representing the marks obtained by students. Write a program to find and display the maximum and minimum marks in the array.

Solution:

```c
#include <stdio.h>

int main() {
    int marks[8] = {72, 85, 91, 68, 79, 95, 88, 76};
    int max, min, i;
    
    // Initialize max and min with first element
    max = marks[0];
    min = marks[0];
    
    // Compare each element with current max and min
    for (i = 1; i < 8; i++) {
        if (marks[i] > max) {
            max = marks[i];
        }
        if (marks[i] < min) {
            min = marks[i];
        }
    }
    
    printf("Student marks: ");
    for (i = 0; i < 8; i++) {
        printf("%d ", marks[i]);
    }
    printf("\n");
    printf("Maximum marks: %d\n", max);
    printf("Minimum marks: %d\n", min);
    
    return 0;
}
```

Output:
```
Student marks: 72 85 91 68 79 95 88 76 
Maximum marks: 95
Minimum marks: 68
```

Explanation: The algorithm for finding maximum and minimum follows a classic pattern. We initialize both max and min to the first array element (marks[0]), then iterate through the remaining elements (starting from index 1). For each element, we compare it with the current maximum—if it's greater, we update max. Similarly, we compare with the current minimum and update if necessary. This approach requires only one pass through the array, making it O(n) in time complexity. The output correctly identifies 95 as the maximum and 68 as the minimum from the given dataset.

## Exam Tips

When preparing for University of Delhi examinations on arrays, keep the following points in mind to maximize your scores:

First, UNDERSTAND THE FUNDAMENTALS OF ZERO-BASED INDEXING. Many students lose marks by forgetting that the first element of an array is accessed using index 0, not 1. This is a fundamental characteristic of C programming and a frequent source of errors in both theory and practical questions.

Second, REMEMBER THAT ARRAY SIZE MUST BE KNOWN AT COMPILE TIME IN STANDARD C. While variable-length arrays were introduced in C99, traditional exam questions expect constant-sized arrays. Know how to declare arrays with specific sizes and initialize them properly.

Third, ALWAYS CHECK ARRAY BOUNDS BEFORE ACCESSING ELEMENTS. In theory questions, remember that accessing elements outside the valid range (0 to n-1) causes undefined behavior. When writing programs, ensure your loop conditions prevent out-of-bounds access.

Fourth, UNDERSTAND THE RELATIONSHIP BETWEEN ARRAY NAME AND POINTER. The array name represents the base address (address of first element), but the array itself is not a pointer. This distinction is crucial for understanding function parameter passing and memory operations.

Fifth, PRACTICE WRITING PROGRAMS FOR COMMON OPERATIONS. Array reversal, finding sum/average, searching for elements, and finding maximum/minimum are frequently asked in practical examinations. Practice these until you can write them fluently.

Sixth, KNOW HOW TO PASS ARRAYS TO FUNCTIONS. When an array is passed to a function, it decays to a pointer, so the function doesn't know the array's size. You must either pass the size as a separate parameter or use a sentinel value.

Seventh, PAY ATTENTION TO MEMORY REPRESENTATION IN THEORY QUESTIONS. Understanding how elements are stored contiguously in memory and being able to calculate addresses using the formula base + (index × element_size) demonstrates deep conceptual understanding and frequently appears in examination questions.