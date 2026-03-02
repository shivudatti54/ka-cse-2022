# One Dimensional Arrays


## Table of Contents

- [One Dimensional Arrays](#one-dimensional-arrays)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Declaration and Memory Allocation](#declaration-and-memory-allocation)
  - [Indexing and Element Access](#indexing-and-element-access)
  - [Initialization of Arrays](#initialization-of-arrays)
  - [Arrays and Functions](#arrays-and-functions)
  - [Common Array Operations](#common-array-operations)
- [Examples](#examples)
  - [Example 1: Finding the Second Largest Element](#example-1-finding-the-second-largest-element)
  - [Example 2: Separating Odd and Even Elements](#example-2-separating-odd-and-even-elements)
  - [Example 3: Merging Two Sorted Arrays](#example-3-merging-two-sorted-arrays)
- [Exam Tips](#exam-tips)

## Introduction

One dimensional arrays represent the most fundamental structured data type in the C programming language. While simple variables can hold only a single value, arrays enable storage and manipulation of multiple related values of the same data type under a single identifier. This capability is essential for solving real-world computational problems where we need to process collections of data such as student marks, temperature readings, inventory quantities, or any sequence of homogeneous elements.

The importance of one dimensional arrays in computer science cannot be overstated. They form the foundation for understanding more complex data structures like matrices (two-dimensional arrays), stacks, queues, and linked lists. In the context of problem solving, arrays provide efficient random access to elements through indices, making algorithms for searching, sorting, and data manipulation computationally practical. For students preparing for University of Delhi examinations, a thorough understanding of array operations, memory representation, and function interactions is crucial as this topic frequently appears in both theory and practical examinations.

## Key Concepts

### Declaration and Memory Allocation

A one dimensional array is declared by specifying the data type of its elements, followed by the array name and the number of elements in square brackets. The general syntax is:

```c
data_type array_name[array_size];
```

For example, to declare an array to store the marks of 30 students:

```c
float marks[30];
```

When the compiler encounters this declaration, it allocates contiguous memory locations equal to (sizeof(data_type) × array_size) bytes. For the float array above, assuming 4 bytes per float, the total memory allocated would be 120 bytes. The array name "marks" represents the base address of the array, which is the memory location of the first element.

### Indexing and Element Access

Array indices in C always start from 0 and go up to (array_size - 1). This zero-based indexing is a characteristic feature of C and many programming languages. If we declare `int numbers[5]`, the valid indices are 0, 1, 2, 3, and 4. Accessing an element at index i is accomplished through the subscript operator: `numbers[i]`.

The compiler computes the memory address of any element using the formula: `base_address + (index × size_of_element)`. This direct addressing mechanism allows O(1) constant time access to any element, which is significantly faster than sequential access methods.

### Initialization of Arrays

Arrays can be initialized at the time of declaration in several ways. Complete initialization provides values for all elements:

```c
int digits[5] = {0, 1, 2, 3, 4};
```

Partial initialization where fewer values are provided assigns zero to remaining elements:

```c
int values[5] = {10, 20, 30};
```

After this initialization, values[0]=10, values[1]=20, values[2]=30, values[3]=0, and values[4]=0. When array size is omitted, the compiler determines the size from the number of initializers:

```c
char vowels[] = {'a', 'e', 'i', 'o', 'u'};
```

This creates an array of exactly 5 characters.

### Arrays and Functions

When arrays are passed to functions, they are passed by reference rather than by value. Only the base address of the array is passed to the function, meaning modifications made inside the function affect the original array. This is both a powerful feature and a potential source of bugs if not understood correctly.

```c
void modify_array(int arr[], int n) {
    arr[0] = 100;  // Modifies the original array
}

int main() {
    int nums[5] = {1, 2, 3, 4, 5};
    modify_array(nums, 5);
    printf("%d", nums[0]);  // Prints 100
    return 0;
}
```

The array parameter `int arr[]` is equivalent to `int *arr` in function parameters. The size of the array is not passed automatically, so we must pass the size as a separate parameter.

### Common Array Operations

Several fundamental operations are performed on one dimensional arrays. Finding the sum and average of elements requires traversing the entire array:

```c
int sum = 0;
for (int i = 0; i < n; i++) {
    sum += array[i];
}
float average = (float)sum / n;
```

Finding maximum and minimum elements similarly require a single pass through the array, maintaining track of the largest and smallest values seen so far. Reversing an array can be done in-place by swapping elements from the beginning and end, moving toward the center.

## Examples

### Example 1: Finding the Second Largest Element

**Problem:** Given an array of n integers, write a C program to find the second largest element.

**Solution:**

```c
#include <stdio.h>

int find_second_largest(int arr[], int n) {
    if (n < 2) {
        printf("Array must have at least 2 elements\n");
        return -1;
    }
    
    int largest = arr[0];
    int second_largest = arr[0];
    
    for (int i = 1; i < n; i++) {
        if (arr[i] > largest) {
            second_largest = largest;
            largest = arr[i];
        } else if (arr[i] > second_largest && arr[i] != largest) {
            second_largest = arr[i];
        }
    }
    
    return second_largest;
}

int main() {
    int n;
    printf("Enter number of elements: ");
    scanf("%d", &n);
    
    int arr[n];
    printf("Enter %d elements: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    
    int result = find_second_largest(arr, n);
    printf("Second largest element: %d\n", result);
    
    return 0;
}
```

**Step-by-step explanation:**
1. Initialize both largest and second_largest with the first element
2. Traverse the array from the second element
3. If current element is greater than largest, shift largest to second_largest and update largest
4. Otherwise, if current element is greater than second_largest and not equal to largest, update second_largest
5. Return the second largest value

### Example 2: Separating Odd and Even Elements

**Problem:** Given an array of integers, create two separate arrays containing odd and even numbers respectively.

**Solution:**

```c
#include <stdio.h>

void separate_odd_even(int arr[], int n, int odd[], int even[], int *odd_count, int *even_count) {
    *odd_count = 0;
    *even_count = 0;
    
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) {
            even[*even_count] = arr[i];
            (*even_count)++;
        } else {
            odd[*odd_count] = arr[i];
            (*odd_count)++;
        }
    }
}

int main() {
    int arr[] = {12, 7, 9, 4, 15, 6, 21, 8};
    int n = 8;
    
    int odd[n], even[n];
    int odd_count, even_count;
    
    separate_odd_even(arr, n, odd, even, &odd_count, &even_count);
    
    printf("Odd elements: ");
    for (int i = 0; i < odd_count; i++) {
        printf("%d ", odd[i]);
    }
    
    printf("\nEven elements: ");
    for (int i = 0; i < even_count; i++) {
        printf("%d ", even[i]);
    }
    
    return 0;
}
```

**Output:**
```
Odd elements: 7 9 15 21 
Even elements: 12 4 6 8 
```

### Example 3: Merging Two Sorted Arrays

**Problem:** Merge two sorted arrays into a single sorted array.

**Solution:**

```c
#include <stdio.h>

void merge_arrays(int arr1[], int n1, int arr2[], int n2, int merged[]) {
    int i = 0, j = 0, k = 0;
    
    while (i < n1 && j < n2) {
        if (arr1[i] <= arr2[j]) {
            merged[k++] = arr1[i++];
        } else {
            merged[k++] = arr2[j++];
        }
    }
    
    while (i < n1) {
        merged[k++] = arr1[i++];
    }
    
    while (j < n2) {
        merged[k++] = arr2[j++];
    }
}

int main() {
    int arr1[] = {2, 5, 8, 12, 16};
    int arr2[] = {3, 6, 9, 11, 14, 18};
    int n1 = 5, n2 = 6;
    int merged[n1 + n2];
    
    merge_arrays(arr1, n1, arr2, n2, merged);
    
    printf("Merged sorted array: ");
    for (int i = 0; i < n1 + n2; i++) {
        printf("%d ", merged[i]);
    }
    
    return 0;
}
```

**Output:**
```
Merged sorted array: 2 3 5 6 8 9 11 12 14 16 18 
```

## Exam Tips

1. **Zero-based indexing**: Remember that array indices always start from 0, not 1. A common mistake is attempting to access array[array_size] which causes buffer overflow.

2. **Array bounds checking**: C does not perform automatic bounds checking. Accessing elements outside the declared array size leads to undefined behavior. In exams, always ensure loop boundaries are correct.

3. **Pass by reference**: When passing arrays to functions, understand that modifications affect the original array. If you need to preserve the original, create a copy first.

4. **Memory layout**: Arrays store elements in contiguous memory locations. This property is essential for understanding pointer arithmetic and why array names decay to pointers.

5. **Initialization differences**: Uninitialized local arrays contain garbage values, while global and static arrays are automatically initialized to zero. This distinction frequently appears in examination questions.

6. **Variable Length Arrays (VLA)**: Modern C supports VLAs where array size is determined at runtime, but they have limitations and may not be supported in all compilers for exam purposes.

7. **Difference between array name and pointer**: While the array name represents the base address, it is not a modifiable l-value. You cannot assign a new address to an array name.

8. **Common operations complexity**: Searching requires O(n) time, finding max/min requires O(n), and merging sorted arrays requires O(n1+n2). Know these complexities for algorithm analysis questions.

9. **Practice trace-based questions**: Many exam questions ask you to trace through array operations and predict output. Practice with various initialization patterns and loop configurations.

10. **Boundary conditions**: Always consider edge cases such as empty arrays, single-element arrays, and arrays with duplicate values when writing and analyzing code.