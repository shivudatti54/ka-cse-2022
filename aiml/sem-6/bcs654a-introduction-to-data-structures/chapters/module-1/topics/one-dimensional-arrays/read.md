# One-Dimensional Arrays

## Introduction to Arrays

An array is a fundamental data structure in programming that stores a **fixed-size**, **sequential collection** of elements of the **same data type**. Think of it as a row of lockers, where each locker holds one item, and all lockers are identical in size and purpose. Arrays provide an efficient way to organize and access related data under a single name.

**Key Characteristics:**

- **Homogeneous Elements:** All elements must be of the same data type (e.g., all integers, all characters).
- **Contiguous Memory:** Elements are stored in consecutive memory locations.
- **Fixed Size:** The size of the array is determined at the time of declaration and cannot be changed during program execution (in most programming languages).
- **Random Access:** Any element can be accessed directly using its index.

## Declaration of One-Dimensional Arrays

A one-dimensional array is declared by specifying its data type, name, and size.

**Syntax:**
`data_type array_name[array_size];`

**Example:**

```c
int marks[5];        // Declares an array 'marks' that can hold 5 integers
float prices[10];    // Declares an array 'prices' for 10 floating-point numbers
char grade[20];      // Declares a character array 'grade' with 20 elements
```

## Memory Representation

When an array is declared, the compiler allocates a contiguous block of memory. The size of this block is calculated as:
`Total Memory = number_of_elements * size_of_each_element`

For the array `int arr[5];` on a system where an integer occupies 4 bytes:

- Total memory allocated: 5 \* 4 = 20 bytes.
- The elements are stored consecutively.

**ASCII Diagram of Memory Allocation:**

```
Memory Address   |   Value   |   Index
-----------------------------------------
1000 (base)      |   arr[0]  |   Element 0
1004             |   arr[1]  |   Element 1
1008             |   arr[2]  |   Element 2
1012             |   arr[3]  |   Element 3
1016             |   arr[4]  |   Element 4
```

## Initialization of Arrays

Arrays can be initialized at the time of declaration by providing a list of values enclosed in curly braces `{}`.

**Ways to Initialize:**

1. **Complete Initialization:** Providing values for all elements.

   ```c
   int numbers[5] = {10, 20, 30, 40, 50};
   ```

2. **Partial Initialization:** Providing values for only some elements. The remaining are set to zero.

   ```c
   int arr[5] = {1, 2}; // arr[0]=1, arr[1]=2, arr[2]=0, arr[3]=0, arr[4]=0
   ```

3. **Initialization without Specifying Size:** The compiler determines the size based on the number of initializers.
   ```c
   int values[] = {9, 8, 7, 6, 5}; // Size is automatically set to 5
   ```

## Accessing Array Elements

Array elements are accessed using an **index** (or subscript), which is an integer value starting from `0` to `size-1`.

**Syntax:**
`array_name[index]`

**Example:**

```c
int scores[4] = {95, 86, 72, 90};
printf("%d", scores[0]); // Outputs: 95 (first element)
printf("%d", scores[3]); // Outputs: 90 (last element)

scores[1] = 92; // Modifies the second element from 86 to 92
```

**⚠️ Important:** Accessing an index outside the valid range (e.g., `scores[5]` for an array of size 4) leads to **undefined behavior** (garbage values, program crashes). This is called an "out-of-bounds" error.

## Basic Operations on Arrays

### 1. Traversal

Visiting each element of the array exactly once. Typically done using a loop.

**Example:**

```c
int i;
int data[5] = {11, 22, 33, 44, 55};

// Printing all elements
for(i = 0; i < 5; i++) {
    printf("%d ", data[i]);
}
// Output: 11 22 33 44 55
```

### 2. Insertion

Adding an element at a specific position. This often requires shifting existing elements to make space.

**Example: Inserting value 99 at index 2 (third position)**

```
Original Array: [10, 20, 30, 40, 50]
After shifting: [10, 20, 99, 30, 40, 50]
// Note: This requires a larger array or overwriting if size is fixed.
```

### 3. Deletion

Removing an element from a specific position. This requires shifting subsequent elements to fill the gap.

**Example: Deleting element at index 1 (value 20)**

```
Original Array: [10, 20, 30, 40, 50]
After shifting: [10, 30, 40, 50, ?]
// The last position becomes unused or is set to a default value.
```

### 4. Searching

Finding the location of a given element.

**Linear Search Algorithm (Pseudocode):**

```
1. Start from the first element (index 0).
2. Compare the target value with each element.
3. If a match is found, return the index.
4. If the end of the array is reached, return -1 (not found).
```

**Example Code for Linear Search:**

```c
int linearSearch(int arr[], int n, int target) {
    int i;
    for (i = 0; i < n; i++) {
        if (arr[i] == target) {
            return i; // Found at index i
        }
    }
    return -1; // Not found
}
```

### 5. Sorting

Arranging elements in a specific order (ascending or descending). The **Bubble Sort** algorithm is a simple method often taught with arrays.

**Bubble Sort Algorithm (Pseudocode for Ascending Order):**

```
1. Repeat for i from 0 to n-2 (number of passes)
2.   For j from 0 to n-i-2
3.     if arr[j] > arr[j+1], swap them
```

This "bubbles" the largest value to the end in each pass.

**Example Code for Bubble Sort:**

```c
void bubbleSort(int arr[], int n) {
    int i, j, temp;
    for (i = 0; i < n-1; i++) {
        for (j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                // Swap arr[j] and arr[j+1]
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}
```

## Relationship with Pointers

In the C programming language, the name of an array is a **pointer constant** that holds the address of the first element of the array.

**Example:**

```c
int nums[3] = {50, 60, 70};
printf("%p\n", nums);    // Outputs address of nums[0], e.g., 1000
printf("%p\n", &nums[0]); // Also outputs address 1000
printf("%d\n", *nums);   // Outputs value at nums[0]: 50
```

Array elements can be accessed using pointer arithmetic:
`*(array_name + i)` is equivalent to `array_name[i]`

```c
printf("%d\n", *(nums + 1)); // Outputs value at nums[1]: 60
```

## Comparison: Arrays vs. Simple Variables

| Feature         | Simple Variable        | Array                               |
| :-------------- | :--------------------- | :---------------------------------- |
| **Storage**     | Holds a single value   | Holds a collection of values        |
| **Declaration** | `int x;`               | `int x[5];`                         |
| **Memory**      | Contiguous for itself  | Contiguous block for all elements   |
| **Access**      | By name (`x`)          | By index (`x[0]`)                   |
| **Efficiency**  | Good for isolated data | Excellent for grouped, similar data |
| **Flexibility** | Fixed single value     | Fixed size collection               |

## Common Use Cases

1.  **Storing Lists of Data:** Test scores, temperature readings, employee IDs.
2.  **Implementing Other Data Structures:** Stacks, queues, heaps (using array-based implementations).
3.  **String Handling:** In C, strings are represented as arrays of characters (`char str[20];`).
4.  **Matrix Operations:** One-dimensional arrays can represent vectors. Two-dimensional arrays (covered next) represent matrices.
5.  **Buffer for Input/Output:** Temporarily holding data read from or written to files.

## Common Errors and Pitfalls

1.  **Index Out of Bounds:** Accessing `arr[-1]` or `arr[size]`. Always ensure the index is between `0` and `size-1`.
2.  **Forgetting that Indexing Starts at 0:** The first element is `arr[0]`, not `arr[1]`.
3.  **Assuming Initialization:** Uninitialized array elements contain garbage values, not zeros (unless declared globally or statically).
4.  **Using `=` for Assignment After Declaration:** You cannot assign a whole array with `=` after declaration. You must assign elements individually.
    ```c
    int a[5];
    a = {1, 2, 3, 4, 5}; // ERROR
    ```

## Exam Tips

1.  **Memory Diagrams:** Be prepared to draw memory diagrams for array declarations and initializations. Clearly show addresses, indices, and values.
2.  **Trace Code Snippets:** Practice tracing code that involves arrays, loops, and pointer arithmetic. Step through each iteration carefully.
3.  **Algorithm Implementation:** Know how to implement standard algorithms like linear search and bubble sort. Write clean, commented code.
4.  **Pointer Connection:** Understand the relationship between arrays and pointers. You will likely be asked to access elements using pointer notation `*(arr + i)`.
5.  **Error Spotting:** Exam questions often contain code with common errors like out-of-bounds access or incorrect loop conditions. Learn to identify them.
6.  **Size Calculation:** Remember how to calculate the size of an array in bytes using the `sizeof` operator (e.g., `sizeof(arr)` returns total bytes, `sizeof(arr[0])` returns bytes per element. Number of elements = `sizeof(arr) / sizeof(arr[0])`).
