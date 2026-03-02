# Arrays and Structures

## Introduction

Arrays and structures form the foundational data structures in C programming, serving as building blocks for more complex data organization. While arrays hold collections of elements of the same data type, structures enable grouping of heterogeneous data items under a single name. Together, they provide programmers with powerful tools to organize and manipulate data efficiently in memory.

In the context of computer science, understanding arrays and structures is crucial because they directly influence how data is stored, accessed, and processed in memory. Arrays provide random access to elements with O(1) time complexity, making them ideal for scenarios requiring frequent element retrieval. Structures, on the other hand, model real-world entities by combining different data types, enabling creation of abstract data types that represent complex objects. These concepts are essential for subsequent topics like linked lists, stacks, queues, and file handling.

The importance of arrays and structures extends beyond academic considerations. In practical software development, arrays are used extensively in database systems, image processing, scientific computations, and algorithm implementation. Structures are fundamental in system programming, file I/O operations, and creating composite data types like linked list nodes. Mastery of these concepts is therefore essential for any computer science professional.

## Key Concepts

### Arrays

An array is a contiguous memory allocation that stores elements of the same data type. The key characteristics of arrays include:

**One-Dimensional Arrays:** A linear collection of elements accessed by a single index. The memory address of any element can be calculated using the formula: `Address(A[i]) = Base Address + (i * Size of Element)`, where i is the zero-based index.

**Two-Dimensional Arrays:** Elements arranged in rows and columns, accessed using two indices. They can be stored in memory using row-major order (C language) or column-major order (Fortran). In row-major storage, elements of each row are stored contiguously.

**Dynamic Arrays:** Arrays whose size is determined at runtime using dynamic memory allocation functions like malloc(), calloc(), or realloc(). This provides flexibility in memory usage but requires proper memory management.

**Array Operations:**
- Traversal: Visiting each element exactly once
- Insertion: Adding an element at a specific position
- Deletion: Removing an element from a specific position
- Searching: Finding the position of a given value (Linear Search: O(n), Binary Search: O(log n) for sorted arrays)
- Sorting: Arranging elements in order (Bubble Sort, Selection Sort, Insertion Sort)

### Structures

A structure is a user-defined data type that groups related data items of different types. Unlike arrays, structures can hold elements of different data types.

**Structure Declaration:**
```c
struct Student {
    int rollno;
    char name[50];
    float marks;
};
```

**Structure Variables:** Variables of type struct can be declared in multiple ways:
- `struct Student s1;`
- `struct Student s1, s2, s3[100];`

**Accessing Structure Members:** Using the dot (.) operator for regular variables and arrow (->) operator for pointers to structures:
- `s1.rollno = 101;`
- `struct Student *ptr = &s1; ptr->marks = 85.5;`

**Nested Structures:** Structures can contain other structures as members, allowing hierarchical data organization.

**Array of Structures:** When multiple records of the same structure type are needed, an array of structures is used, combining the benefits of both concepts.

### Memory Representation

**Array Memory Layout:** Arrays allocate contiguous memory locations. For a 2D array in row-major order, elements are stored row by row. The address calculation for A[i][j] in a 2D array with m columns is: `Address = Base + (i * m + j) * ElementSize`.

**Structure Memory Alignment:** Structures may contain padding bytes for alignment, meaning the actual size of a structure may be greater than the sum of its members. Compilers align data on word boundaries for efficient access.

## Examples

### Example 1: One-Dimensional Array Operations

**Problem:** Write a C program to find the sum and average of n numbers using an array.

**Solution:**
```c
#include <stdio.h>

int main() {
    int n, i;
    float sum = 0, avg;
    
    printf("Enter number of elements: ");
    scanf("%d", &n);
    
    int arr[n];  // Variable Length Array (C99)
    
    printf("Enter %d numbers: ", n);
    for(i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }
    
    avg = sum / n;
    
    printf("Sum = %.2f\n", sum);
    printf("Average = %.2f\n", avg);
    
    return 0;
}
```

**Step-by-step Explanation:**
1. Declare variables: n for count, i for loop counter, sum and average as floats
2. Read the number of elements from user
3. Create array of size n (VLA feature in C99)
4. Use a for loop to read each element and add to sum
5. Calculate average by dividing sum by n
6. Display results

### Example 2: Binary Search Implementation

**Problem:** Implement binary search on a sorted array to find a target element.

**Solution:**
```c
#include <stdio.h>

int binarySearch(int arr[], int size, int target) {
    int low = 0, high = size - 1, mid;
    
    while(low <= high) {
        mid = low + (high - low) / 2;  // Prevents integer overflow
        
        if(arr[mid] == target)
            return mid;
        else if(arr[mid] < target)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;  // Element not found
}

int main() {
    int arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target, result;
    
    printf("Array elements: ");
    for(int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    
    printf("\nEnter element to search: ");
    scanf("%d", &target);
    
    result = binarySearch(arr, n, target);
    
    if(result != -1)
        printf("Element found at index %d\n", result);
    else
        printf("Element not found\n");
    
    return 0;
}
```

**Key Points:**
- Time complexity: O(log n) - divides search space by 2 each iteration
- Space complexity: O(1) - uses only a few variables
- Critical: Array must be sorted before binary search
- The formula `mid = low + (high - low) / 2` prevents integer overflow when low and high are large

### Example 3: Structure with Array Members

**Problem:** Create a structure to store student information and find the topper.

**Solution:**
```c
#include <stdio.h>
#include <string.h>

struct Student {
    int rollno;
    char name[50];
    float marks[5];  // Marks in 5 subjects
};

float calculateTotal(struct Student s) {
    float total = 0;
    for(int i = 0; i < 5; i++)
        total += s.marks[i];
    return total;
}

int main() {
    struct Student students[3];
    int n = 3;
    float maxTotal = 0, currentTotal;
    int topperIndex = 0;
    
    // Input student data
    for(int i = 0; i < n; i++) {
        printf("\nEnter details for student %d:\n", i + 1);
        printf("Roll No: ");
        scanf("%d", &students[i].rollno);
        printf("Name: ");
        scanf("%s", students[i].name);
        printf("Enter marks in 5 subjects: ");
        for(int j = 0; j < 5; j++)
            scanf("%f", &students[i].marks[j]);
    }
    
    // Find topper
    for(int i = 0; i < n; i++) {
        currentTotal = calculateTotal(students[i]);
        if(currentTotal > maxTotal) {
            maxTotal = currentTotal;
            topperIndex = i;
        }
    }
    
    printf("\n*** TOPPER ***\n");
    printf("Roll No: %d\n", students[topperIndex].rollno);
    printf("Name: %s\n", students[topperIndex].name);
    printf("Total Marks: %.2f\n", maxTotal);
    
    return 0;
}
```

**Step-by-step Explanation:**
1. Define structure Student with rollno, name, and marks array
2. Create function to calculate total marks using structure parameter
3. Declare array of structures to store multiple student records
4. Input data for each student using structure variable and dot operator
5. Loop through all students to find maximum total marks
6. Display topper information

## Exam Tips

1. **Address Calculation Formula:** Remember the formula for calculating element addresses in 1D and 2D arrays. In row-major storage, for a 2D array A[m][n], address of A[i][j] = Base + (i × n + j) × size.

2. **Index vs Size:** Array indices start from 0 in C. If an array is declared as arr[10], valid indices are 0 to 9. Accessing arr[10] causes buffer overflow.

3. **Structure Padding:** Be aware that structures may have padding bytes. The size of a structure is not simply the sum of its members. Use sizeof() to determine actual size.

4. **Dynamic vs Static Arrays:** Static arrays have fixed size at compile time, while dynamic arrays use malloc()/calloc() and require free() to prevent memory leaks.

5. **Array as Function Parameter:** When passing an array to a function, it decays to a pointer. Always pass the size separately as arrays don't carry size information.

6. **Structure Assignment:** Entire structures can be assigned using the = operator in C (unlike arrays). This creates a copy of all members.

7. **Common Errors:** Remember to use & (address-of operator) when scanning array elements or structure members. Don't confuse the dot operator (.) with arrow operator (->) - latter is for pointers to structures.

8. **Memory Diagram Drawing:** Practice drawing memory layouts for arrays and structures, including proper indexing and alignment. This helps in understanding and debugging programs.