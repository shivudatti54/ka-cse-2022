# Fundamentals of Data Structures in C

## Introduction

Data structures form the backbone of efficient computer programming and software development. In the context of the C programming language, understanding fundamental data structures is essential for writing optimized code that can handle complex computational problems. The study of data structures enables us to organize, store, and manipulate data efficiently, which is crucial for developing scalable software applications.

The C programming language provides a powerful set of tools for implementing data structures due to its close relationship with memory management. Unlike higher-level languages, C offers direct control over memory through pointers, manual memory allocation using malloc() and calloc(), and the ability to work with raw memory addresses. This low-level control makes C an ideal language for understanding how data structures actually work internally.

For students at the University of Delhi, mastering fundamentals of data structures in C is particularly important because it forms the foundation for advanced topics like algorithms, database systems, and operating system concepts. The concepts covered here will be repeatedly applied in courses on data analysis, software engineering, and computer networks. This chapter introduces the essential building blocks that every computer science student must understand before proceeding to more complex data structures like trees, graphs, and hash tables.

## Key Concepts

### Primitive Data Types

C language provides several primitive data types that serve as the foundation for building more complex data structures. The basic primitive types include: int for integers (typically 4 bytes), float for floating-point numbers (4 bytes), double for double-precision floating-point numbers (8 bytes), and char for characters (1 byte). Understanding the memory representation of these types is crucial because data structures ultimately store these primitive types in various arrangements.

The size of these data types may vary depending on the system architecture, which is why the sizeof operator is frequently used in portable C programs. For instance, on a 32-bit system, an int might be 2 or 4 bytes, while on a 64-bit system, it is typically 4 bytes. This variability highlights the importance of writing portable code and understanding how data is represented in memory.

### Arrays

Arrays are the simplest and most fundamental data structure in C. They represent a contiguous block of memory containing elements of the same type. The key characteristics of arrays include constant-time access to any element using an index, fixed size determined at compile time (for static arrays), and contiguous memory allocation. Arrays provide the foundation for implementing more complex data structures like stacks, queues, and heaps.

When declaring an array in C, the syntax is straightforward: type array_name[size]; creates an array of the specified type with the given number of elements. For example, int numbers[10]; creates an array that can hold 10 integers. Array indices in C start from 0, meaning the first element is accessed using index 0, and the last element is accessed using index size-1. One critical aspect to remember is that C does not perform bounds checking, so accessing elements outside the array bounds leads to undefined behavior and potential security vulnerabilities.

Multi-dimensional arrays in C are implemented as arrays of arrays. A two-dimensional array like int matrix[3][4]; represents a table with 3 rows and 4 columns. In memory, this is stored as a contiguous block of 12 integers, with row-major ordering meaning all elements of the first row are stored followed by the second row, and so on.

### Structures

Structures (struct) in C allow the grouping of heterogeneous data types into a single unit. While arrays can only hold elements of the same type, structures can combine different data types, making them ideal for representing real-world entities. For example, a student record might consist of a name (character array), roll number (integer), and marks (float) - all of which can be stored together in a structure.

The syntax for defining a structure uses the struct keyword. Once defined, structure variables can be declared and accessed using the dot (.) operator for regular variables and the arrow operator (->) when working with pointers to structures. Structures are extensively used in building more advanced data structures like linked lists, trees, and hash tables because they allow us to create complex nodes with multiple fields.

Memory padding is an important consideration when working with structures. The compiler may insert padding bytes between members to align data on appropriate memory boundaries for faster access. This can be controlled using the #pragma pack directive or attributes in modern C compilers.

### Pointers and Dynamic Memory Allocation

Pointers are perhaps the most distinctive and powerful feature of C, enabling dynamic data structure creation. A pointer is a variable that stores the memory address of another variable. The unary operator (&) returns the address of a variable, while the dereference operator (*) accesses the value stored at the address pointed to by a pointer.

Dynamic memory allocation allows programs to request memory at runtime rather than compile time. The functions malloc(), calloc(), realloc(), and free() from stdlib.h manage heap memory. malloc(size) allocates the specified number of bytes and returns a pointer to the beginning of the allocated memory. calloc(n, size) allocates memory for n elements of the given size and initializes all bytes to zero. realloc() allows resizing previously allocated memory, while free() releases the memory back to the system.

Understanding pointers and dynamic memory allocation is essential because most non-linear data structures like linked lists, trees, and graphs require dynamic memory management. Memory leaks occur when allocated memory is not properly freed, which can cause programs to consume excessive memory over time.

### Linked Lists

A linked list is a linear data structure where elements (called nodes) are stored in objects, and each node contains a reference to the next node. Unlike arrays, linked lists do not require contiguous memory and can grow or shrink dynamically. The basic building block of a linked list is a structure containing the data and a pointer to the next node.

Singly linked lists allow traversal in one direction only, from the head to the end. Each node contains data and a pointer to the next node, with the last node pointing to NULL to indicate the end of the list. Doubly linked lists maintain pointers to both the next and previous nodes, enabling bidirectional traversal at the cost of additional memory.

The fundamental operations on linked lists include insertion (at the beginning, end, or middle), deletion (from the beginning, end, or middle), searching for an element, and traversal to visit all nodes. Each operation has different time complexities: insertion at the head is O(1), while searching requires O(n) in the worst case.

## Examples

### Example 1: Implementing a Dynamic Array

Problem: Create a dynamic array that can grow as needed to store integers.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *data;
    int size;
    int capacity;
} DynamicArray;

void initArray(DynamicArray *arr, int initialCapacity) {
    arr->data = (int *)malloc(initialCapacity * sizeof(int));
    arr->size = 0;
    arr->capacity = initialCapacity;
}

void insertElement(DynamicArray *arr, int value) {
    if (arr->size == arr->capacity) {
        arr->capacity *= 2;
        arr->data = (int *)realloc(arr->data, arr->capacity * sizeof(int));
    }
    arr->data[arr->size++] = value;
}

void printArray(DynamicArray *arr) {
    printf("Array contents: ");
    for (int i = 0; i < arr->size; i++) {
        printf("%d ", arr->data[i]);
    }
    printf("\n");
}

int main() {
    DynamicArray arr;
    initArray(&arr, 4);
    
    insertElement(&arr, 10);
    insertElement(&arr, 20);
    insertElement(&arr, 30);
    insertElement(&arr, 40);
    insertElement(&arr, 50);  // Triggers doubling
    
    printArray(&arr);
    printf("Size: %d, Capacity: %d\n", arr.size, arr.capacity);
    
    free(arr.data);
    return 0;
}
```

This example demonstrates the concept of amortized time complexity. While individual insertions may be expensive when resizing occurs, the average cost per insertion remains O(1). The array grows exponentially (doubling capacity) to ensure that resizing becomes increasingly rare.

### Example 2: Creating and Traversing a Singly Linked List

Problem: Implement a singly linked list with functions to add nodes at the beginning and print all nodes.

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

struct Node* createNode(int value) {
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = NULL;
    return newNode;
}

void insertAtBeginning(struct Node **head, int value) {
    struct Node *newNode = createNode(value);
    newNode->next = *head;
    *head = newNode;
}

void printList(struct Node *head) {
    struct Node *temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

int main() {
    struct Node *head = NULL;
    
    insertAtBeginning(&head, 30);
    insertAtBeginning(&head, 20);
    insertAtBeginning(&head, 10);
    
    printList(head);  // Output: 10 -> 20 -> 30 -> NULL
    
    // Free memory
    struct Node *temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
    
    return 0;
}
```

This example illustrates the power of dynamic memory allocation for creating flexible data structures. The insertAtBeginning function demonstrates how pointers allow us to modify the head pointer itself by passing its address.

### Example 3: Structure for Student Records

Problem: Define a structure to store student information and create an array of student records.

```c
#include <stdio.h>
#include <string.h>

struct Student {
    int rollNo;
    char name[50];
    float marks;
};

void displayStudent(struct Student s) {
    printf("Roll No: %d\n", s.rollNo);
    printf("Name: %s\n", s.name);
    printf("Marks: %.2f\n", s.marks);
}

int main() {
    struct Student students[3];
    
    students[0].rollNo = 101;
    strcpy(students[0].name, "Amit Kumar");
    students[0].marks = 85.5;
    
    students[1].rollNo = 102;
    strcpy(students[1].name, "Priya Sharma");
    students[1].marks = 92.0;
    
    students[2].rollNo = 103;
    strcpy(students[2].name, "Raj Patel");
    students[2].marks = 78.5;
    
    for (int i = 0; i < 3; i++) {
        displayStudent(students[i]);
        printf("---\n");
    }
    
    return 0;
}
```

This example demonstrates how structures can be used to create composite data types that represent real-world entities. The array of structures provides a simple database-like organization of records.

## Exam Tips

1. UNDERSTAND POINTER ARITHMETIC: In exams, questions frequently test understanding of pointer operations. Remember that incrementing a pointer moves it by the size of the pointed-to type, not by one byte.

2. DIFFERENTIATE BETWEEN STACK AND HEAP: Static arrays are allocated on the stack, while dynamic memory using malloc() is allocated on the heap. Stack allocation is faster but limited in size, while heap can handle larger allocations but requires manual management.

3. TIME COMPLEXITY MATTERS: Be prepared to analyze time complexities of basic operations. Array access is O(1), searching is O(n), while linked list insertion at head is O(1) but search is O(n).

4. MEMORY LEAK AWARENESS: Always remember to pair every malloc() with a free(). In exam questions, if you write code that allocates memory, mention that it should be freed to avoid memory leaks.

5. STRUCTURE PADDING: The compiler may add padding to structures for alignment. The order of members in a structure can affect its total size, which is why arrangement matters in certain scenarios.

6. POINTERS TO STRUCTURES: When passing structures to functions, passing by value copies the entire structure. Passing by reference (using pointers) is more efficient for large structures.

7. ARRAY VS POINTER DIFFERENCE: Although array names decay to pointers in many contexts, they are fundamentally different. sizeof(array) gives the total bytes, while sizeof(pointer) gives pointer size only.

8. NULL POINTER CHECKING: Always check if malloc() returns NULL before using the allocated memory. This is especially important in exam code snippets where error handling is tested.