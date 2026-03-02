# Introduction to Data Structures

## Introduction

Data structures form the foundation of computer science and software engineering, serving as the backbone for organizing, storing, and manipulating data efficiently in computer systems. In an era where applications process millions of data points daily, understanding how to structure data optimally has become a critical skill for every programmer and computer scientist. The study of data structures enables us to write programs that execute faster, consume less memory, and solve complex computational problems with elegance and efficiency.

The importance of data structures extends far beyond academic exercises. Every software application, from simple mobile apps to complex enterprise systems, relies on appropriate data structures to function effectively. When you search for information on Google, stream a video on Netflix, or navigate through social media feeds, sophisticated data structures work behind the scenes to deliver seamless user experiences. Database systems use B-trees for efficient indexing, operating systems employ linked lists and queues for process scheduling, and compilers utilize hash tables and stacks for syntax parsing. The ability to select and implement the right data structure distinguishes competent programmers from exceptional ones.

This chapter introduces the fundamental concepts of data structures, their classifications, and the essential operations that can be performed on them. We begin by exploring what data structures are, why they matter, and how they are categorized. Understanding these foundational concepts will prepare you to dive deeper into specific data structures like arrays, linked lists, trees, and graphs that form the core of computer science education at University of Delhi.

## Key Concepts

### Definition and Importance of Data Structures

A data structure is a specialized format for organizing, processing, and storing data that enables efficient access and modification. More precisely, it is a collection of data values, the relationships among them, and the functions or operations that can be applied to the data. The choice of data structure significantly impacts the performance of algorithms, making it essential to select appropriate structures based on the problem requirements.

Consider a telephone directory application. If you store contacts in an unordered array and need to find a specific person, you might need to examine every entry in the worst case, resulting in O(n) time complexity. However, if you store the same contacts in a balanced binary search tree, the search operation takes only O(log n) time. This dramatic difference in performance illustrates why data structure selection matters. For small datasets, the difference might be imperceptible, but as data grows to millions or billions of records, the right data structure becomes indispensable.

### Classification of Data Structures

Data structures are broadly classified into two categories: primitive and non-primitive data structures. This classification forms the basis for understanding how different types of data are represented and manipulated in computer memory.

PRIMITIVE DATA STRUCTURES are the basic building blocks provided by programming languages. They represent single values and cannot be broken down into simpler components. The primitive data structures include:

INTEGER (int): Represents whole numbers without decimal points. In most programming languages, integers have fixed storage sizes. For example, a 32-bit integer can store values ranging from -2,147,483,648 to 2,147,483,647. Memory allocation for integers is typically 4 bytes on modern systems.

FLOATING-POINT (float): Represents real numbers with decimal points. Float data types follow IEEE 754 standards for floating-point arithmetic. They consume typically 4 bytes and provide approximately 7 decimal digits of precision.

CHARACTER (char): Represents individual characters from character sets like ASCII or Unicode. A character typically occupies 1 byte for ASCII characters and can store letters, digits, symbols, or control characters.

BOOLEAN (bool): Represents logical values with two states: true or false. Boolean values are fundamental for decision-making in programs and typically consume 1 byte, though bit-level storage is possible for optimization.

DOUBLE (double): Provides extended precision for floating-point numbers, typically consuming 8 bytes and offering approximately 15 decimal digits of precision.

NON-PRIMITIVE DATA structures, also called composite or abstract data types, are constructed from primitive data types. They organize collections of data items and provide more complex operations. Non-primitive data structures are further classified into:

LINEAR DATA STRUCTURES: Elements are arranged in a sequential manner where each element is connected to its previous and next element. Examples include arrays, linked lists, stacks, and queues. In linear structures, traversal occurs in a single pass from one end to the other.

NON-LINEAR DATA STRUCTURES: Elements are not arranged sequentially. Each element can connect to multiple other elements, forming hierarchical or network relationships. Examples include trees and graphs. Non-linear structures represent complex relationships that cannot be captured by simple sequential arrangements.

### Data Structure Operations

Regardless of the specific type, most data structures support a set of fundamental operations. Understanding these operations helps in analyzing and comparing different data structures for specific use cases.

TRAVERSAL: Accessing each element exactly once in a systematic manner. Traversal is essential for processing all data items, whether for printing, searching, or performing computations. For an array, traversal involves iterating through indices sequentially. For a tree, traversal can occur in different orders: pre-order, in-order, post-order, or level-order.

INSERTION: Adding a new element to the data structure at a specified position. Insertion operations require careful consideration of where the new element goes and how existing elements are affected. In an unsorted array, insertion at the end takes O(1) time, while insertion at the beginning requires shifting all existing elements, taking O(n) time.

DELETION: Removing an existing element from the data structure. Similar to insertion, deletion may require shifting elements to maintain the structure's integrity. Deleting from a sorted array requires finding the element first, which takes O(n) time in the worst case, followed by shifting elements.

SEARCHING: Finding the location of a specific element within the data structure. Searching can be performed using various algorithms, with linear search being the simplest (O(n) time) and binary search being efficient for sorted data (O(log n) time).

SORTING: Arranging elements in a specified order (ascending or descending). Sorting is one of the most fundamental operations in computer science, with numerous algorithms available, including bubble sort, insertion sort, merge sort, and quick sort, each with different time and space complexities.

UPDATING: Modifying existing elements within the data structure. This operation requires accessing the element first and then changing its value, with time complexity depending on how the element is located.

### Pointers and Dynamic Memory Allocation

Pointers serve as the foundation for implementing dynamic data structures. A pointer is a variable that stores the memory address of another variable. Understanding pointers is crucial for working with linked lists, trees, and other dynamic structures where memory is allocated at runtime.

In C and C++, the ampersand (&) operator returns the address of a variable, while the asterisk (*) operator declares a pointer variable or dereferences it to access the value at the stored address. Consider the following example:

```c
int num = 42;
int *ptr = &num;  // ptr now stores the address of num
printf("%d", *ptr);  // prints 42, the value at the address stored in ptr
```

DYNAMIC MEMORY ALLOCATION allows programs to request memory from the heap during runtime, rather than relying solely on stack memory allocated at compile time. This flexibility enables data structures to grow and shrink as needed. In C, malloc() allocates a specified number of bytes and returns a pointer to the allocated memory, while calloc() allocates memory for an array and initializes all bytes to zero. The free() function releases previously allocated memory back to the system.

Dynamic memory allocation is essential for implementing linked lists, where nodes are created as needed and connected through pointers. Without dynamic allocation, we would need to predefine the maximum size of our data structure, leading to either wasted memory or capacity limitations.

### Abstract Data Types (ADTs)

An Abstract Data Type (ADT) defines a data structure by its behavior (operations) rather than its implementation. ADTs provide a layer of abstraction that separates what a data structure does from how it accomplishes it. For example, a stack ADT is defined by its operations: push (add element), pop (remove element), and peek (view top element). The implementation could use an array or a linked list, but the interface remains the same.

This abstraction is crucial in software engineering because it allows changing the underlying implementation without affecting code that uses the data structure. Programs become more modular, maintainable, and adaptable to changing requirements.

## Examples

### Example 1: Analyzing Time Complexity of Array Operations

Suppose we have an array of n integers and we need to perform various operations. Let us analyze the time complexity of each operation:

INSERTION AT THE END: If we maintain a size counter, we can directly place the new element at index size and increment the counter. This operation takes O(1) constant time, regardless of array size.

INSERTION AT THE BEGINNING: To insert at index 0, we must shift all existing n elements one position to the right before placing the new element. This requires n assignments and takes O(n) time.

SEARCHING: In an unsorted array, we must examine each element sequentially until we find the target or exhaust the array. In the worst case (element not found), we examine all n elements, resulting in O(n) time complexity. However, if the array is sorted, we can use binary search to achieve O(log n) complexity.

DELETION: Similar to insertion, deletion at the end takes O(1), while deletion at the beginning requires shifting n-1 elements, taking O(n) time.

This analysis demonstrates why understanding data structure operations is critical for writing efficient code. Choosing where to insert elements can significantly impact performance for large datasets.

### Example 2: Implementing a Simple Array Structure

Let us implement a basic array structure with operations for initialization, insertion, and traversal in C:

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

struct Array {
    int data[MAX_SIZE];
    int size;
};

void initialize(struct Array *arr) {
    arr->size = 0;
}

void insert(struct Array *arr, int position, int value) {
    if (arr->size >= MAX_SIZE) {
        printf("Array is full. Cannot insert.\n");
        return;
    }
    if (position < 0 || position > arr->size) {
        printf("Invalid position.\n");
        return;
    }
    // Shift elements to the right
    for (int i = arr->size; i > position; i--) {
        arr->data[i] = arr->data[i-1];
    }
    arr->data[position] = value;
    arr->size++;
}

void traverse(struct Array *arr) {
    printf("Array elements: ");
    for (int i = 0; i < arr->size; i++) {
        printf("%d ", arr->data[i]);
    }
    printf("\n");
}

int main() {
    struct Array arr;
    initialize(&arr);
    
    insert(&arr, 0, 10);
    insert(&arr, 1, 20);
    insert(&arr, 2, 30);
    insert(&arr, 1, 15);
    
    traverse(&arr);  // Output: 10 15 20 30
    
    return 0;
}
```

This example demonstrates how arrays store elements contiguously in memory and how insertion requires shifting existing elements. The main limitation of this static array implementation is the fixed maximum size defined at compile time.

### Example 3: Dynamic Memory Allocation for Flexible Storage

Consider implementing a dynamic array that can grow as needed:

```c
#include <stdio.h>
#include <stdlib.h>

struct DynamicArray {
    int *data;
    int capacity;
    int size;
};

void initDynamicArray(struct DynamicArray *arr, int initialCapacity) {
    arr->data = (int *)malloc(initialCapacity * sizeof(int));
    arr->capacity = initialCapacity;
    arr->size = 0;
}

void insertDynamic(struct DynamicArray *arr, int value) {
    // Double capacity if array is full
    if (arr->size >= arr->capacity) {
        arr->capacity *= 2;
        arr->data = (int *)realloc(arr->data, arr->capacity * sizeof(int));
    }
    arr->data[arr->size] = value;
    arr->size++;
}

void freeArray(struct DynamicArray *arr) {
    free(arr->data);
    arr->data = NULL;
}
```

This implementation overcomes the fixed-size limitation by allocating memory from the heap. When the array becomes full, it allocates a larger chunk of memory and copies existing elements to the new location using realloc(). This approach is how C++'s vector and Java's ArrayList are implemented internally.

## Exam Tips

Understanding data structures thoroughly is essential for scoring well in DU semester examinations. The following tips will help you prepare effectively:

PRIMITIVE VS NON-PRIMITIVE DISTINCTION IS FREQUENTLY ASKED: Ensure you can clearly distinguish between primitive data types (int, float, char, double) and non-primitive data structures (arrays, linked lists, trees, graphs). Remember that primitive types store single values, while non-primitive types store collections.

TIME COMPLEXITY ANALYSIS CARRIES SIGNIFICANT WEIGHT: Practice analyzing the time complexity of basic operations (traversal, insertion, deletion, search) on different data structures. Know that array access by index is O(1), while searching in an unsorted array is O(n).

POINTER CONCEPTS ARE FUNDAMENTAL: Many students struggle with pointers in C. Practice declaring pointers, understanding address-of (&) and dereference (*) operators, and visualizing memory layouts. Draw memory diagrams to reinforce your understanding.

KNOW THE CLASSIFICATION HIERARCHY: Be able to draw and explain the complete classification tree of data structures. Linear structures include arrays, linked lists, stacks, and queues. Non-linear structures include trees and graphs.

DYNAMIC MEMORY FUNCTIONS ARE ESSENTIAL: Memorize the purposes of malloc(), calloc(), realloc(), and free(). Understand when to use each function and remember that failed allocation returns NULL.

ABSTRACT DATA TYPES REQUIRE CONCEPTUAL UNDERSTANDING: Study ADTs from the perspective of interface vs implementation. Be able to define the operations supported by basic ADTs like stack, queue, and list without referencing specific implementations.

WRITE CODE WITH PROPER SYNTAX: In practical exams, you must write code that compiles. Practice writing clean, well-indented code with meaningful variable names. Pay attention to pointer syntax in C.

DIAGRAMMATIC REPRESENTATION HELPS IN EXPLANATIONS: When explaining data structures, use diagrams to show how elements are organized in memory. This is particularly important for linked lists, trees, and arrays.

REVISION OF BASIC OPERATIONS: Review how each operation (insert, delete, search, update) works on arrays. Pay special attention to what happens to elements before and after the affected position during insertion and deletion.