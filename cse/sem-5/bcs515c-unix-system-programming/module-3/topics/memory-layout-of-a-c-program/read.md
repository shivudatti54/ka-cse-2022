# Memory Layout of a C Program

## Introduction

Understanding the memory layout of a C program is fundamental to mastering C programming and system-level concepts. When a C program is executed, the operating system allocates memory in a specific manner to store different components of the program such as code, global variables, local variables, dynamic memory, and return addresses. This organized memory arrangement follows a standard structure that is consistent across most operating systems including Linux, Windows, and UNIX.

The memory layout is crucial for several reasons: it helps programmers understand how variables are stored, why certain operations work the way they do, and how to avoid common pitfalls like buffer overflows, memory leaks, and segmentation faults. For CSE students preparing for examinations, this topic forms the foundation for understanding pointers, dynamic memory allocation, recursion, and system programming concepts.

In this comprehensive guide, we will explore each section of the memory layout in detail, examine how C programs utilize memory during execution, and reinforce understanding through practical examples and examination-oriented tips.

## Key Concepts

### Overview of Memory Layout

When a C program is loaded into memory for execution, the operating system creates a process and allocates memory in a specific pattern. The complete memory layout of a C program consists of several distinct regions, each serving a specific purpose. From lowest address to highest address, the typical layout follows this order: Text Segment (Code), Data Segment, BSS Segment, Heap, and Stack.

The memory layout can be visualized as a contiguous block of virtual memory assigned to the process. Each region has different characteristics regarding read/write permissions, growth direction, and lifetime of data stored within it. Understanding these characteristics is essential for writing efficient and bug-free C programs.

### Text Segment (Code Segment)

The text segment, also known as the code segment, is the region of memory that contains the executable instructions of the program. This segment is typically read-only to prevent accidental modification of program code, which could lead to unpredictable behavior or security vulnerabilities. The text segment is loaded from the executable file when the program starts and remains constant throughout program execution.

The size of the text segment depends on the complexity and size of the program code. In systems with memory protection, the text segment has read and execute permissions but not write permissions. This design prevents programs from modifying their own code, which is a security feature that helps detect and prevent certain types of malicious software.

### Data Segment

The data segment is divided into two parts: initialized data and uninitialized data. The initialized data segment (also called the data segment proper) stores global variables and static variables that have been explicitly initialized by the programmer. This segment is further subdivided based on whether the data is read-only or read-write.

For example, global variables like `int global_var = 100;` and static variables like `static int static_var = 50;` are stored in the initialized data segment. The data segment is readable and writable, allowing programs to modify these variables during execution. The size of this segment is determined at compile time based on the declared initialized global and static variables.

### BSS Segment (Block Started by Symbol)

The BSS segment stores uninitialized global variables and static variables. These are variables that are declared but not assigned any initial value. The C standard automatically initializes uninitialized global and static variables to zero. The BSS segment is typically mapped to zero-initialized pages in memory for efficiency, rather than storing explicit zero values in the executable file.

For instance, variables like `int uninit_global;` and `static int uninit_static;` are stored in the BSS segment. The BSS segment is writable and grows as more uninitialized global variables are declared. Understanding the BSS segment is important because it affects the size of the executable file and the memory footprint of the program.

### Heap

The heap is a dynamic memory region that grows upward (toward higher addresses) from the bottom of the memory layout. Memory in the heap is allocated dynamically during program execution using functions like `malloc()`, `calloc()`, and `realloc()`. The heap is shared among all threads within a process and must be managed carefully to avoid memory leaks and dangling pointers.

Memory allocated on the heap persists until it is explicitly freed using the `free()` function or until the program terminates. The heap is managed by the memory allocator, which maintains metadata about allocated and free blocks. When memory is allocated using `malloc()`, the allocator finds a suitable free block and returns a pointer to the allocated memory. If no suitable block is found, the allocator may request more memory from the operating system using system calls like `brk()` or `mmap()`.

### Stack

The stack is another dynamic memory region that grows downward (toward lower addresses) from the top of the memory layout. The stack is used to store function call information, local variables, return addresses, and function parameters. Each time a function is called, a new stack frame (also called activation record) is pushed onto the stack, and when the function returns, the stack frame is popped.

Local variables declared inside functions, function parameters, and return addresses are all stored on the stack. The stack operates in a Last-In-First-Out (LIFO) manner, which makes it efficient for managing function calls. The stack size is typically fixed and determined at program startup, though it can be configured in some systems. Stack memory is automatically managed by the compiler, so programmers do not need to explicitly allocate or deallocate stack variables.

### Memory Management and Pointers

Pointers play a crucial role in C programming by allowing programs to manipulate memory addresses directly. Pointers can reference any region of the memory layout, including the stack, heap, and data segments. Understanding how pointers interact with different memory regions is essential for writing correct and efficient C programs.

When a pointer is dereferenced, the program accesses the memory location it points to. However, accessing invalid memory addresses can lead to undefined behavior, including segmentation faults. Common errors include dereferencing null pointers, using uninitialized pointers, accessing memory after it has been freed (dangling pointers), and buffer overflows that corrupt adjacent memory.

## Examples

### Example 1: Visualizing Memory Layout

Consider the following C program to understand memory layout:

```c
#include <stdio.h>
#include <stdlib.h>

int global_initialized = 100; // Stored in Data Segment
int global_uninitialized; // Stored in BSS Segment

void function() {
 static int static_local = 50; // Stored in Data Segment
 int local_auto; // Stored in Stack
 printf("Static local: %d\n", static_local);
}

int main() {
 int local_var = 25; // Stored in Stack
 int *heap_ptr; // Stored in Stack (pointer variable)

 heap_ptr = (int*)malloc(sizeof(int)); // Heap allocation
 *heap_ptr = 75;

 printf("Global initialized: %d\n", global_initialized);
 printf("Global uninitialized: %d\n", global_uninitialized);
 printf("Local variable: %d\n", local_var);
 printf("Heap variable: %d\n", *heap_ptr);

 function();
 free(heap_ptr); // Free heap memory

 return 0;
}
```

In this program:

- `global_initialized` is in the Data Segment (initialized data)
- `global_uninitialized` is in the BSS Segment (uninitialized data)
- `static_local` inside `function()` is in the Data Segment
- `local_var`, `heap_ptr`, and the parameter in `printf()` are on the Stack
- The memory allocated by `malloc()` is on the Heap

### Example 2: Stack Frame Demonstration

```c
#include <stdio.h>

int factorial(int n) {
 if (n <= 1)
 return 1;
 return n * factorial(n - 1);
}

int main() {
 int result = factorial(5);
 printf("Factorial: %d\n", result);
 return 0;
}
```

When `factorial(5)` is called:

1. Main pushes n=5 onto stack, calls factorial
2. factorial(5) pushes n=5, calls factorial(4)
3. This continues until factorial(1) returns 1
4. Then each function returns, popping stack frames

Each recursive call creates a new stack frame containing the parameter `n` and the return address. The stack grows downward with each call and shrinks as functions return.

### Example 3: Heap vs Stack Allocation

```c
#include <stdio.h>
#include <stdlib.h>

void stack_alloc() {
 int arr[1000]; // Allocates 4000 bytes on stack
 arr[0] = 10;
 printf("Stack array first element: %d\n", arr[0]);
}

void heap_alloc() {
 int *arr = (int*)malloc(1000 * sizeof(int)); // Heap allocation
 arr[0] = 20;
 printf("Heap array first element: %d\n", arr[0]);
 free(arr); // Must free heap memory explicitly
}

int main() {
 stack_alloc();
 heap_alloc();
 return 0;
}
```

This example demonstrates the key difference between stack and heap allocation. Stack allocation is automatic and deallocation happens when the function returns. Heap allocation requires explicit management with `malloc()` and `free()`. The stack has limited size (typically 8MB default on Linux), so large arrays should be allocated on the heap.

## Exam Tips

1. **Know the Order**: Remember the memory layout order from low to high address: Text → Data → BSS → Heap → Stack. This is frequently asked in examinations.

2. **BSS vs Data Segment**: Understand that initialized global/static variables go to the Data segment, while uninitialized ones go to the BSS segment. The BSS is zero-initialized by the OS.

3. **Stack Growth Direction**: Remember that the Stack grows downward (toward lower addresses) while the Heap grows upward (toward higher addresses).

4. **Variable Storage Classes**: Be able to identify where different storage class specifiers store variables: `auto` and `register` on stack, `static` and `global` in Data/BSS, `extern` for external linkage.

5. **Memory Leak**: A memory leak occurs when heap memory is allocated but not freed before program termination. This is an important concept for system programming questions.

6. **Stack Overflow**: Stack overflow happens when the stack grows into the heap region or exceeds its allocated size, often due to excessive recursion or large local arrays.

7. **Segmentation Fault**: This occurs when a program tries to access memory it is not permitted to access, such as dereferencing an invalid pointer or accessing freed memory.

8. **Practical Understanding**: Be prepared to draw and explain a diagram of memory layout for given C code, identifying which variables go to which sections.
