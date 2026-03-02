# Fundamentals of Data Structures in C

## Introduction

Data structures are the backbone of computer science and software development. They provide a systematic way of organizing and storing data so that it can be accessed and modified efficiently. In the context of the C programming language, understanding fundamental data structures is essential for writing efficient, optimized code. C, being a procedural language with rich support for pointers and memory management, offers direct control over how data is stored and manipulated in memory.

The study of data structures in C encompasses understanding primitive data types, composite data types, and the various operations that can be performed on them. For students at the University of Delhi, this topic forms the foundation upon which more advanced data structures like linked lists, stacks, queues, trees, and graphs are built. The concepts covered here are not merely theoretical—they have direct practical applications in database systems, operating systems, compilers, and application software development.

In this chapter, we will explore the fundamental data structures available in C, including arrays, pointers, structures, and dynamic memory allocation. We will examine how these constructs work at the memory level and understand the time and space complexity considerations that guide the choice of appropriate data structures for specific problems.

## Key Concepts

### Primitive Data Types in C

C provides several primitive data types that form the building blocks for all data structures. The basic data types include:

**Integer types**: `char` (1 byte), `short` (2 bytes), `int` (typically 4 bytes), `long` (4 or 8 bytes), and `long long` (8 bytes). These can be signed or unsigned. The choice of integer type affects memory usage and the range of values that can be stored.

**Floating-point types**: `float` (4 bytes, single precision), `double` (8 bytes, double precision), and `long double` (extended precision). These types store real numbers with varying degrees of accuracy.

**Void type**: The `void` type represents the absence of a type and is used in various contexts, particularly in function return types and generic pointers.

### Arrays in C

An array is a contiguous collection of elements of the same data type. It is the most fundamental non-primitive data structure in C and provides O(1) access time to any element if the index is known.

**One-dimensional Arrays**: A 1D array is declared as `type array_name[size]`. The elements are stored in consecutive memory locations. For example, `int arr[5];` declares an array of 5 integers. Array indices in C begin from 0, so valid indices are 0 through 4.

**Two-dimensional Arrays**: A 2D array can be visualized as a matrix with rows and columns. It is declared as `type array_name[rows][cols]`. In memory, a 2D array is stored in row-major order, meaning all elements of the first row are stored consecutively, followed by elements of the second row, and so on.

```c
int matrix[3][4];  // 3 rows, 4 columns
```

**Array as Function Parameter**: When an array is passed to a function, it decays to a pointer to its first element. This means the function receives the memory address, not a copy of the array. The size information is lost, so passing the size as a separate parameter is necessary.

### Pointers in C

Pointers are variables that store memory addresses of other variables. They are fundamental to understanding how data structures are implemented in C and provide powerful capabilities for dynamic memory management.

**Pointer Declaration and Initialization**: A pointer is declared by specifying the type it points to, followed by an asterisk: `int *ptr;`. The address-of operator (`&`) is used to obtain the address of a variable.

**Pointer Arithmetic**: Pointers can be incremented and decremented. When a pointer to an integer is incremented, it moves by `sizeof(int)` bytes in memory. This property makes pointer arithmetic essential for traversing arrays.

**Pointer to Arrays**: The name of an array acts as a pointer to its first element. For an array `arr`, `arr` and `&arr[0]` are equivalent.

### Structures in C

A structure is a composite data type that groups together variables of different types under a single name. Unlike arrays, structures can hold elements of different data types.

**Structure Definition and Declaration**: The `struct` keyword is used to define a structure:

```c
struct Student {
    int rollno;
    char name[50];
    float marks;
};
```

**Accessing Structure Members**: The dot operator (`.`) is used to access structure members when working with structure variables, while the arrow operator (`->`) is used when working with pointers to structures.

**Structure Padding**: C compilers may add padding bytes between members of a structure for alignment purposes. This affects the total size of a structure, which may be larger than the sum of individual member sizes.

### Dynamic Memory Allocation

Static arrays have a fixed size determined at compile time. Dynamic memory allocation allows programs to allocate memory at runtime, providing flexibility in handling data of unknown size.

**malloc()**: Allocates a specified number of bytes and returns a pointer to the first byte. The allocated memory is uninitialized.

```c
int *ptr = (int *)malloc(5 * sizeof(int));
```

**calloc()**: Allocates memory for an array of specified elements and initializes all bytes to zero.

```c
int *ptr = (int *)calloc(5, sizeof(int));
```

**realloc()**: Resizes previously allocated memory. It can either expand or contract the memory block.

**free()**: Releases dynamically allocated memory. Failing to free memory leads to memory leaks.

### Linked Structures Using Pointers

While arrays provide fast access, they have limitations: fixed size and expensive insertion/deletion operations. Linked structures, built using pointers, overcome these limitations.

**Singly Linked List**: Each node contains data and a pointer to the next node. Insertion and deletion at the beginning can be done in O(1) time.

**Doubly Linked List**: Each node contains pointers to both the previous and next nodes, allowing traversal in both directions.

### Time and Space Complexity

Understanding complexity is crucial for selecting appropriate data structures:

| Operation | Array (O) | Linked List (O) |
|-----------|-----------|-----------------|
| Access by index | O(1) | O(n) |
| Insertion at beginning | O(n) | O(1) |
| Deletion at beginning | O(n) | O(1) |
| Insertion at end | O(1)* | O(n) or O(1)** |

*With pointer to last element
**With tail pointer

## Examples

### Example 1: Array Initialization and Traversal

Write a C program to find the sum and average of n elements stored in an array.

```c
#include <stdio.h>

int main() {
    int n;
    printf("Enter number of elements: ");
    scanf("%d", &n);
    
    int arr[n];  // Variable Length Array (C99 feature)
    printf("Enter %d elements:\n", n);
    
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    
    float average = (float)sum / n;
    
    printf("Sum = %d\n", sum);
    printf("Average = %.2f\n", average);
    
    return 0;
}
```

**Step-by-step explanation**:
1. Declare an integer variable `n` to store the number of elements
2. Use a VLA (Variable Length Array) to create an array of size n
3. Use a for loop to input n elements
4. Initialize sum to 0 and traverse the array to accumulate the sum
5. Cast sum to float before division to get accurate average
6. Display results

### Example 2: Dynamic Memory Allocation for Student Records

Create a structure to store student information and dynamically allocate memory for n students.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Student {
    int rollno;
    char name[50];
    float marks;
};

int main() {
    int n;
    printf("Enter number of students: ");
    scanf("%d", &n);
    
    // Dynamically allocate array of structures
    struct Student *students = (struct Student *)malloc(n * sizeof(struct Student));
    
    if (students == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }
    
    // Input student details
    for (int i = 0; i < n; i++) {
        printf("\nEnter details for student %d:\n", i + 1);
        printf("Roll Number: ");
        scanf("%d", &students[i].rollno);
        printf("Name: ");
        scanf("%s", students[i].name);
        printf("Marks: ");
        scanf("%f", &students[i].marks);
    }
    
    // Display student details
    printf("\nStudent Details:\n");
    printf("%-10s %-20s %-10s\n", "Roll No", "Name", "Marks");
    printf("------------------------------------------\n");
    for (int i = 0; i < n; i++) {
        printf("%-10d %-20s %-10.2f\n", 
               students[i].rollno, 
               students[i].name, 
               students[i].marks);
    }
    
    // Calculate average
    float total = 0;
    for (int i = 0; i < n; i++) {
        total += students[i].marks;
    }
    printf("\nClass Average: %.2f\n", total / n);
    
    free(students);
    return 0;
}
```

**Key concepts demonstrated**:
- Structure definition and usage
- Dynamic memory allocation using malloc()
- Memory allocation checking
- Array of structures accessed via pointer
- Proper memory deallocation using free()

### Example 3: Implementing a Simple Stack using Arrays

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

struct Stack {
    int top;
    int array[MAX_SIZE];
};

void initStack(struct Stack *s) {
    s->top = -1;
}

int isFull(struct Stack *s) {
    return s->top == MAX_SIZE - 1;
}

int isEmpty(struct Stack *s) {
    return s->top == -1;
}

void push(struct Stack *s, int value) {
    if (isFull(s)) {
        printf("Stack Overflow!\n");
        return;
    }
    s->array[++s->top] = value;
    printf("Pushed %d\n", value);
}

int pop(struct Stack *s) {
    if (isEmpty(s)) {
        printf("Stack Underflow!\n");
        return -1;
    }
    return s->array[s->top--];
}

int peek(struct Stack *s) {
    if (isEmpty(s)) {
        printf("Stack is empty!\n");
        return -1;
    }
    return s->array[s->top];
}

int main() {
    struct Stack s;
    initStack(&s);
    
    push(&s, 10);
    push(&s, 20);
    push(&s, 30);
    
    printf("Top element: %d\n", peek(&s));
    printf("Popped: %d\n", pop(&s));
    printf("Popped: %d\n", pop(&s));
    
    return 0;
}
```

This example demonstrates how arrays serve as the underlying storage for abstract data types like stacks, showcasing the practical application of fundamental data structures.

## Exam Tips

1. **Memory Layout Understanding**: Be prepared to draw memory layouts for arrays and structures. Questions frequently ask about how data is stored in memory, especially for 2D arrays in row-major vs column-major order.

2. **Pointer Arithmetic**: Practice problems involving pointer arithmetic. Remember that `ptr + i` points to `i` elements after `ptr`, not `i` bytes.

3. **Difference between malloc and calloc**: This is a common exam question. Remember that malloc allocates uninitialized memory while calloc initializes to zero.

4. **Structure Padding**: Understand how compilers align structures. This affects the size of structures and is often tested in exams.

5. **Array vs Pointer**: Know that array name is not a modifiable l-value but a constant pointer. The expressions `arr` and `&arr` have different types but same address value.

6. **Dynamic Memory Common Errors**: Be aware of common errors like dangling pointers, memory leaks, and accessing freed memory. These are frequently tested in practical exams.

7. **Time Complexity**: Memorize the time complexities for basic operations on arrays. Questions asking to compare array implementations with other data structures are common.

8. **Passing Arrays to Functions**: Remember that arrays are passed by reference (as pointers). To pass size information, you must pass it as a separate parameter.

9. **Practice Writing Code**: Write programs to implement basic operations on arrays, structures, and pointers. Lab exam questions often require implementing search, sort, or manipulation operations.

10. **Key Definitions**: Know precise definitions of terms like abstract data type, data structure, primitive and non-primitive data types.