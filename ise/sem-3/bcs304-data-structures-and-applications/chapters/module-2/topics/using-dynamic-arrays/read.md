# Using Dynamic Arrays

## Introduction

Dynamic arrays represent one of the most fundamental and powerful data structures in computer science, serving as the backbone for numerous algorithms and applications. Unlike static arrays, which have a fixed size determined at compile time, dynamic arrays can grow and shrink during program execution, providing flexibility in memory management that is essential for real-world applications.

In the context of data structures, dynamic arrays play a crucial role in implementing collections that require flexible memory allocation. When we study stacks, queues, and other abstract data types, the underlying representation often relies on dynamic arrays to achieve efficient time complexity for various operations. The ability to resize arrays dynamically allows us to balance space efficiency with operational performance, a trade-off that is central to algorithm design.

This chapter explores the intricacies of dynamic arrays, including their implementation, growth strategies, and practical applications. Understanding dynamic arrays is essential for any computer science student, as they form the foundation for more complex data structures and are extensively used in software development. From implementing vector containers in C++ to creating flexible list structures in Python, dynamic arrays are ubiquitous in modern programming.

## Key Concepts

### Static vs Dynamic Arrays

Static arrays allocate memory at compile time with a predetermined fixed size. The memory address is fixed, and the array cannot expand beyond its declared capacity. This limitation leads to two primary problems: memory waste when the array is underutilized and inability to accommodate data when the array overflows.

Dynamic arrays, in contrast, solve these problems by allocating memory at runtime and automatically resizing when needed. When a dynamic array reaches its capacity, it allocates a larger array (typically twice the current capacity), copies all existing elements to the new array, and releases the old array's memory. This process, while introducing occasional O(n) overhead for resizing, ensures amortized O(1) time complexity for append operations.

### Memory Allocation and Representation

In C and C++, dynamic arrays are typically implemented using malloc/calloc for memory allocation and free for deallocation, or using new and delete operators. A dynamic array is essentially a pointer to a contiguous block of memory that can be reallocated as needed.

The implementation involves maintaining three critical pieces of information: a pointer to the array's base address, the current size (number of elements currently stored), and the capacity (maximum number of elements that can be stored before resizing is required). This metadata enables efficient tracking and management of the dynamic array's state.

```c
typedef struct {
    int *array;    // Pointer to allocated memory
    int size;      // Current number of elements
    int capacity;  // Total allocated capacity
} DynamicArray;
```

### Growth Factor and Amortized Analysis

The strategy for increasing array capacity significantly impacts overall performance. A common approach uses a growth factor of 2, where the array capacity doubles each time resizing is required. This geometric growth ensures that the amortized cost of insertion remains O(1).

The mathematical justification for the O(1) amortized cost follows: when inserting n elements into a dynamic array with doubling strategy, the total cost of all resize operations is 1 + 2 + 4 + 8 + ... + n, which equals approximately 2n - 1. Dividing by n insertions gives O(1) amortized cost per insertion.

A growth factor between 1.5 and 2 provides optimal balance between memory usage and resize frequency. A factor of 1.5 (as used in some implementations) leaves more unused memory but performs resizes more frequently, while a factor of 2 uses memory less efficiently but resizes less often.

### Shrinking Dynamic Arrays

Just as dynamic arrays grow to accommodate new elements, they can also shrink when elements are removed. When the size falls significantly below capacity (commonly below half), the array can be resized to a smaller capacity to conserve memory. This shrink operation maintains the invariant that capacity is always at least equal to size.

The shrink strategy prevents memory bloat in applications where arrays grow and shrink repeatedly. However, care must be taken to avoid thrashing, where rapid insertions and deletions cause excessive resizing operations. Implementing a threshold (such as shrinking when size drops below capacity/4) prevents this issue.

### Implementation of Basic Operations

The fundamental operations on dynamic arrays include:

**Insertion** - Adding an element at the end involves checking if size equals capacity, resizing if necessary, and placing the element at the index equal to size. The time complexity is O(1) amortized, O(n) worst case when resizing occurs.

**Deletion** - Removing the last element simply decrements the size (no actual memory modification needed). If size drops below capacity/4, the array may shrink. Time complexity is O(1).

**Access** - Random access by index is O(1) since the array provides contiguous memory with direct address calculation: address = base_address + (index × element_size).

**Search** - Linear search takes O(n) time, while binary search requires O(log n) for sorted arrays.

### 2D Dynamic Arrays

Dynamic arrays can be extended to multiple dimensions. A 2D dynamic array is typically implemented as an array of pointers, where each pointer refers to a dynamically allocated 1D array. This structure allows for flexible row lengths and efficient memory usage.

```c
int** create2DArray(int rows, int cols) {
    int **array = (int**)malloc(rows * sizeof(int*));
    for (int i = 0; i < rows; i++) {
        array[i] = (int*)malloc(cols * sizeof(int));
    }
    return array;
}
```

## Examples

### Example 1: Implementing a Dynamic Array in C

Consider implementing a dynamic array of integers with basic operations. Let's walk through creating and using such an array:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *data;
    int size;
    int capacity;
} IntArray;

void initArray(IntArray *arr, int initialCapacity) {
    arr->capacity = initialCapacity;
    arr->size = 0;
    arr->data = (int*)malloc(initialCapacity * sizeof(int));
}

void resize(IntArray *arr, int newCapacity) {
    int *newData = (int*)malloc(newCapacity * sizeof(int));
    for (int i = 0; i < arr->size; i++) {
        newData[i] = arr->data[i];
    }
    free(arr->data);
    arr->data = newData;
    arr->capacity = newCapacity;
}

void append(IntArray *arr, int value) {
    if (arr->size == arr->capacity) {
        resize(arr, arr->capacity * 2);
    }
    arr->data[arr->size++] = value;
}

int main() {
    IntArray arr;
    initArray(&arr, 2);
    
    append(&arr, 10);
    append(&arr, 20);
    append(&arr, 30);
    append(&arr, 40);
    append(&arr, 50);
    
    printf("Size: %d, Capacity: %d\n", arr.size, arr.capacity);
    printf("Elements: ");
    for (int i = 0; i < arr.size; i++) {
        printf("%d ", arr.data[i]);
    }
    
    free(arr.data);
    return 0;
}
```

The output demonstrates how the array grows: starting with capacity 2, after five insertions, the capacity becomes 16 (doubled: 2→4→8→16). This shows the dynamic resizing behavior in action.

### Example 2: Managing Memory for Polynomial Representation

In the context of polynomial representation using arrays, dynamic arrays provide an elegant solution when the polynomial degree is not known in advance. Consider representing a polynomial where we dynamically expand the coefficient array as higher-degree terms are added:

```c
typedef struct {
    double *coefficients;
    int degree;
    int capacity;
} Polynomial;

void addTerm(Polynomial *poly, int power, double coeff) {
    if (coeff == 0) return;
    
    if (power >= poly->capacity) {
        int newCapacity = (power >= poly->capacity * 2) ? 
                          power + 1 : poly->capacity * 2;
        poly->coefficients = (double*)realloc(poly->coefficients, 
                                              newCapacity * sizeof(double));
        // Initialize new slots to 0
        for (int i = poly->capacity; i < newCapacity; i++) {
            poly->coefficients[i] = 0;
        }
        poly->capacity = newCapacity;
    }
    
    poly->coefficients[power] += coeff;
    if (power > poly->degree) {
        poly->degree = power;
    }
}
```

This implementation uses realloc to efficiently expand the coefficient array, demonstrating how dynamic arrays solve the problem of unknown polynomial degrees at compile time.

### Example 3: Amortized Cost Demonstration

To empirically verify the amortized O(1) insertion cost, consider measuring total operations for inserting n elements:

```c
void analyzeGrowth(IntArray *arr, int n) {
    int resizeCount = 0;
    int currentCapacity = arr->capacity;
    
    for (int i = 0; i < n; i++) {
        if (arr->size == arr->capacity) {
            resizeCount++;
            currentCapacity = arr->capacity * 2;
        }
        append(arr, i);
    }
    
    printf("Inserted %d elements\n", n);
    printf("Final capacity: %d\n", arr->capacity);
    printf("Resizes performed: %d\n", resizeCount);
    printf("Amortized cost per insert: %.2f operations\n", 
           (double)(n + resizeCount) / n);
}
```

For n = 1,000,000 insertions, we expect approximately log₂(1,000,000) ≈ 20 resizes, giving an amortized cost very close to 1, confirming the theoretical analysis.

## Exam Tips

1. **Understand the difference between size and capacity** - Size represents actual elements stored, capacity represents allocated memory. This distinction frequently appears in exam questions.

2. **Remember the amortized analysis** - The O(1) amortized cost for dynamic array insertion is crucial. Be able to prove it mathematically using the geometric series sum.

3. **Know the resizing strategy** - Doubling the capacity provides O(1) amortized inserts. Explain why linear growth (increasing by constant) would result in O(n) amortized cost.

4. **Master address calculation** - For random access in arrays, remember: address = base + (index × element_size). This is fundamental for understanding O(1) access time.

5. **Understand realloc behavior** - The realloc function can either expand in place or allocate new memory and copy data. This efficiency consideration is important for memory management questions.

6. **Know when to shrink** - Shrinking should occur at a different threshold than growing (typically when size < capacity/4) to prevent thrashing between growth and shrink operations.

7. **Compare with linked lists** - Dynamic arrays provide O(1) random access but O(n) insertion/deletion in the middle, while linked lists provide O(1) insertion/deletion but O(n) access. This trade-off is a common exam topic.

8. **Memory allocation functions** - Be familiar with malloc, calloc, realloc, and free, including their differences: malloc allocates raw memory, calloc initializes to zero, realloc resizes existing allocation.