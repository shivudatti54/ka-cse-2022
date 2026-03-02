# Arrays and Structures

## Introduction

Arrays and structures form the foundation of non-primitive data structures in computer programming. These data types allow programmers to organize and manage multiple data elements efficiently, enabling the development of complex software solutions. While arrays store homogeneous data elements (elements of the same data type), structures provide a mechanism to store heterogeneous data elements (elements of different data types) under a single name.

In the context of the University of Delhi's Computer Science curriculum, understanding arrays and structures is essential for several reasons. First, these concepts directly relate to memory management and efficient data organization—topics frequently examined in internal assessments and end-semester examinations. Second, arrays serve as the building blocks for more advanced data structures such as stacks, queues, trees, and graphs. Third, structures are fundamental to implementing abstract data types and object-oriented programming concepts.

This topic carries significant weightage in DU examinations, typically accounting for 12-18 marks in the end-semester paper. Students must master both theoretical concepts and practical implementation details to score well. The relationship between arrays, pointers, and dynamic memory allocation is particularly important, as questions frequently test the interplay between these concepts.

## Key Concepts

### Arrays

An array is a collection of elements of the same data type stored in contiguous memory locations. Arrays enable programmers to store multiple values under a single variable name, accessed using an index or subscript. The index starts from 0 (in C/C++) and goes up to (n-1) for an array of n elements.

**One-Dimensional Arrays:** A linear array consists of elements stored in consecutive memory locations. The syntax for declaration in C is `data_type array_name[size];`. For example, `int marks[5];` declares an array named marks that can hold 5 integer values. The memory allocated is calculated as: `base_address + (index × size_of_element)`.

**Two-Dimensional Arrays:** These arrays are organized as rows and columns, similar to a matrix. Declaration syntax is `data_type array_name[rows][cols];`. For instance, `int matrix[3][4];` creates a 3×4 matrix with 12 total elements. In memory, 2D arrays are stored in row-major order (consecutive elements of each row are stored together) in C/C++.

**Multi-Dimensional Arrays:** Arrays can have any number of dimensions. A three-dimensional array can be visualized as a cube of data elements. Declaration: `int arr[2][3][4];` creates a 2×3×4 array with 24 elements.

**Static vs Dynamic Arrays:** Static arrays have a fixed size determined at compile time, while dynamic arrays are created using dynamic memory allocation functions like `malloc()` and `calloc()` in C, or `new` operator in C++. Dynamic arrays provide flexibility but require manual memory management.

### Structures

A structure is a user-defined data type that groups together related data items of different types. Unlike arrays, structures can hold variables of different data types. The keyword `struct` is used to define structures in C/C++.

**Structure Definition:** The syntax is:
```c
struct structure_name {
    data_type member1;
    data_type member2;
    // more members
};
```

**Structure Variables:** Variables of structure type can be declared in multiple ways:
```c
struct Book {
    char title[50];
    char author[50];
    int pages;
    float price;
};

struct Book b1;  // Direct declaration
struct Book b2 = {"C Programming", "Dennis Ritchie", 400, 299.99};
```

**Accessing Structure Members:** The dot operator (.) is used to access members of a structure variable. For example: `b1.pages = 500;` assigns 500 to the pages member of b1.

**Nested Structures:** Structures can contain other structures as members, enabling complex data representations. For example, a date structure can be embedded within an employee structure.

**Arrays of Structures:** The most common use of structures is creating arrays of structures to manage collections of records. This is extensively used in database applications: `struct Student students[100];` creates an array of 100 Student records.

### Pointers and Arrays

In C/C++, arrays and pointers have a close relationship. The array name itself acts as a pointer to the first element of the array. For an array `int arr[5];`, the expression `arr` is equivalent to `&arr[0]`. This relationship enables pointer arithmetic for array traversal.

**Pointer Arithmetic:** When a pointer points to an array element, adding 1 to the pointer moves it to the next element. If `ptr` points to `arr[0]`, then `ptr + 1` points to `arr[1]`, and the address calculation is: `new_address = current_address + (n × size_of_element)`.

### Dynamic Memory Allocation

Dynamic arrays are created using heap memory, allowing arrays to grow or shrink at runtime. In C, `malloc()` allocates a specified number of bytes and returns a void pointer. `calloc()` allocates memory for an array and initializes all bytes to zero. `realloc()` resizes previously allocated memory. In C++, the `new` and `delete` operators perform the same functions.

## Examples

### Example 1: Operations on One-Dimensional Array

Write a C program to find the sum and average of n elements stored in an array.

```c
#include <stdio.h>

int main() {
    int n, i;
    float sum = 0, avg;
    
    printf("Enter number of elements: ");
    scanf("%d", &n);
    
    int arr[n];  // VLA (Variable Length Array) - C99
    
    printf("Enter %d elements: ", n);
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

**Step-by-step explanation:**
1. Declare variables: n for number of elements, i for loop counter, sum (float for precision), avg
2. Read the value of n from user
3. Declare array of size n (VLA in C99)
4. Use for loop to read n elements and accumulate their sum
5. Calculate average by dividing sum by n
6. Display results

### Example 2: Dynamic Array Implementation

Implement a dynamic array in C that grows as needed.

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr = NULL;
    int size = 0, capacity = 0, element;
    
    printf("Enter elements (-1 to stop):\n");
    while(scanf("%d", &element) == 1 && element != -1) {
        if(size == capacity) {
            capacity = (capacity == 0) ? 1 : capacity * 2;
            arr = (int*)realloc(arr, capacity * sizeof(int));
        }
        arr[size++] = element;
    }
    
    printf("\nArray elements: ");
    for(int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\nSize: %d, Capacity: %d\n", size, capacity);
    
    free(arr);
    return 0;
}
```

**Step-by-step explanation:**
1. Initialize pointer as NULL and size/capacity as 0
2. In the loop, check if array is full (size equals capacity)
3. If full, double the capacity using realloc
4. Insert element and increment size
5. After loop, print all elements and free the allocated memory
6. This demonstrates dynamic array growth with doubling strategy

### Example 3: Array of Structures for Student Records

Write a program to store and display information of n students using structures.

```c
#include <stdio.h>
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
    
    struct Student s[n];  // Array of structures
    
    // Input student details
    for(int i = 0; i < n; i++) {
        printf("\nEnter details for student %d:\n", i+1);
        printf("Roll No: ");
        scanf("%d", &s[i].rollno);
        printf("Name: ");
        scanf("%s", s[i].name);
        printf("Marks: ");
        scanf("%f", &s[i].marks);
    }
    
    // Display student details
    printf("\n--- Student Records ---\n");
    for(int i = 0; i < n; i++) {
        printf("Roll No: %d, Name: %s, Marks: %.2f\n", 
               s[i].rollno, s[i].name, s[i].marks);
    }
    
    return 0;
}
```

**Step-by-step explanation:**
1. Define structure Student with rollno, name, and marks members
2. Create array of n Student structures
3. Use loop to input details for each student using the dot operator
4. Use another loop to display all student records
5. This pattern is fundamental for database applications

## Exam Tips

1. **Memory Address Calculation:** In examinations, questions frequently ask to calculate the address of an element in a 2D array stored in row-major or column-major order. Remember: Row-major address = Base + [(i × n + j) × size], where i is row index, j is column index, and n is number of columns.

2. **Array vs Structure Differences:** Be prepared to write differences between arrays and structures. Arrays store homogeneous data, structures store heterogeneous data. Arrays use subscript notation, structures use dot operator. Array name is a constant pointer, structure name is a variable.

3. **Pointer-Arithmetic in Arrays:** If `int arr[5] = {10,20,30,40,50}` and `int *ptr = arr`, then `*(ptr+2)` gives 30, and `ptr[3]` gives 40. These are equivalent notations.

4. **Storage Classes with Arrays:** Understand how `static`, `auto`, and `extern` storage classes affect array initialization and lifetime. Static arrays are initialized to zero by default.

5. **Padding and Packing in Structures:** Structure members are stored in memory with alignment requirements. The `sizeof(struct)` may be greater than the sum of individual members due to padding. Use `#pragma pack(1)` or `__attribute__((packed))` to disable padding.

6. **Dynamic Memory Functions:** Know when to use malloc vs calloc. Calloc zero-initializes memory while malloc does not. Always check for NULL after allocation and free memory when done to avoid memory leaks.

7. **Time Complexity Analysis:** For array operations: accessing by index is O(1), linear search is O(n), insertion at end is O(1) but may require resizing. Be prepared to analyze and compare these complexities.

8. **Representation of Polynomials:** Polynomials can be represented using arrays where index represents exponent and value represents coefficient. For sparse polynomials (with many zero coefficients), use arrays of structures containing coefficient and exponent pairs.