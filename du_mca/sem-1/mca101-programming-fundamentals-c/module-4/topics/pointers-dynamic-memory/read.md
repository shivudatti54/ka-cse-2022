# Pointers and Dynamic Memory Allocation
## Programming Fundamentals C — MCA (Delhi University)

---

## 1. Introduction

Pointers are one of the most powerful and distinctive features of the C programming language. They provide a means by which to access memory locations directly, enabling efficient memory management, dynamic data structure creation, and hardware-level programming. In modern computing, understanding pointers is essential for system programming, embedded systems, operating system development, and competitive programming.

**Real-World Relevance:**
- **Memory Management:** Operating systems use pointers to manage RAM allocation and deallocation
- **Data Structures:** Implementation of linked lists, trees, graphs, and dynamic arrays relies on pointers
- **Function Call Optimization:** Passing large structures by reference (via pointers) avoids copying overhead
- **Hardware Access:** Device drivers interact with hardware through memory-mapped I/O using pointers
- **Embedded Systems:** Direct memory access and hardware register manipulation

This topic carries significant weight in the MCA syllabus (Revised June 2024) and typically accounts for 12-15 marks in end-semester examinations.

---

## 2. Fundamentals of Pointers

### 2.1 What is a Pointer?

A pointer is a variable that stores the **memory address** of another variable. Unlike regular variables that hold data values, pointers hold memory addresses as their values.

### 2.2 Pointer Declaration and Initialization

```c
int num = 42;
int *ptr;          // Declaration: ptr is a pointer to an integer
ptr = &num;        // Initialization: & (address-of operator) gets address of num
```

**Key Points:**
- `*` in declaration indicates that the variable is a pointer
- `&` (address-of operator) returns the memory address of a variable
- `*` (dereference/indirection operator) accesses the value at the pointed location

```c
printf("Address of num: %p", &num);    // %p for printing addresses
printf("Value of ptr: %p", ptr);        // ptr stores address
printf("Value at address: %d", *ptr);  // Dereferencing: 42
```

### 2.3 Pointer Types

All pointers have the same size (typically 4 bytes on 32-bit systems, 8 bytes on 64-bit systems), but they must be typed for proper pointer arithmetic:

```c
int *intPtr;       // Pointer to int
float *floatPtr;   // Pointer to float
char *charPtr;     // Pointer to char
void *genericPtr;  // Generic pointer (void pointer)
```

---

## 3. Pointer Arithmetic

C allows specific arithmetic operations on pointers:

| Operation | Description |
|-----------|-------------|
| `ptr + n` | Advances pointer by n elements of pointed type |
| `ptr - n` | Moves pointer back by n elements |
| `ptr1 - ptr2` | Returns difference in elements (only between same type pointers) |
| `ptr++` / `++ptr` | Increment to next element |
| `ptr--` / `--ptr` | Decrement to previous element |

**Example:**
```c
int arr[5] = {10, 20, 30, 40, 50};
int *ptr = arr;    // Array name decays to pointer to first element

printf("%d ", *ptr);    // 10
printf("%d ", *(ptr+1)); // 20
printf("%d ", *ptr+1);   // 11 (addition has lower precedence than *)
```

---

## 4. Pointers and Arrays: The Deep Relationship

### 4.1 Array Name as Pointer

In most contexts, the array name acts as a **pointer to the first element**:

```c
int arr[5] = {1, 2, 3, 4, 5};
int *ptr = arr;    // Equivalent to: int *ptr = &arr[0];

// Both expressions access the same memory location
printf("%d %d", arr[0], *ptr);        // Both print 1
printf("%d %d", arr[1], *(ptr+1));    // Both print 2
```

### 4.2 Key Differences

| Array | Pointer |
|-------|---------|
| Fixed memory allocation at compile time | Can be reassigned to different addresses |
| `sizeof(arr)` gives total array size | `sizeof(ptr)` gives pointer size only |
| Cannot be assigned (not an lvalue) | Can be assigned freely |

### 4.3 Passing Arrays to Functions

When passing arrays to functions, they decay to pointers:

```c
void printArray(int *arr, int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", *(arr + i));  // or arr[i]
    }
}

int main() {
    int nums[5] = {1, 2, 3, 4, 5};
    printArray(nums, 5);  // Array decays to pointer
    return 0;
}
```

### 4.4 Pointer to Multidimensional Arrays

```c
int matrix[3][4] = {{1,2,3,4}, {5,6,7,8}, {9,10,11,12}};
int (*rowPtr)[4] = matrix;    // Pointer to array of 4 integers
int *elementPtr = &matrix[0][0];  // Pointer to first element

printf("%d", *(*(matrix + 1) + 2));  // matrix[1][2] = 7
```

---

## 5. Pointers and Strings

Strings in C are character arrays terminated by a null character (`\0`). Pointers provide powerful string manipulation:

```c
char str[] = "Hello";        // Array form
char *ptr = "Hello";         // Pointer form (string literal)

// Both are accessed similarly
printf("%c %c", str[0], ptr[0]);    // H H

// String functions using pointers
char source[] = "Copy this";
char dest[20];
char *s = source;
char *d = dest;

while (*s != '\0') {
    *d = *s;
    s++;
    d++;
}
*d = '\0';  // Don't forget null terminator
```

---

## 6. Pointers to Pointers

A pointer to a pointer stores the address of another pointer:

```c
int num = 100;
int *ptr1 = &num;      // Pointer to int
int **ptr2 = &ptr1;    // Pointer to pointer to int

printf("%d", **ptr2);  // 100
```

**Practical Use Cases:**

1. **Dynamic 2D Arrays:**
```c
int **createMatrix(int rows, int cols) {
    int **matrix = (int **)malloc(rows * sizeof(int *));
    for (int i = 0; i < rows; i++) {
        matrix[i] = (int *)malloc(cols * sizeof(int));
    }
    return matrix;
}
```

2. **Modifying pointers in functions:**
```c
void allocateInt(int **ptr) {
    *ptr = (int *)malloc(sizeof(int));
    **ptr = 42;
}

int *p = NULL;
allocateInt(&p);  // Pass address of pointer to modify it
printf("%d", *p); // 42
```

3. **Command-line arguments:**
```c
int main(int argc, char *argv[])  // argv is char** (array of strings)
```

---

## 7. Function Pointers

Function pointers store addresses of functions, enabling callback mechanisms and dynamic function calls.

### 7.1 Declaration and Usage

```c
int add(int a, int b) {
    return a + b;
}

int (*funcPtr)(int, int);  // Declaration: pointer to function returning int
funcPtr = add;             // Assignment (function name decays to pointer)

int result = funcPtr(5, 3);  // Calling through pointer: 8
```

### 7.2 Callback Implementation

```c
void bubbleSort(int *arr, int n, int (*compare)(int, int)) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (compare(arr[j], arr[j+1]) > 0) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int ascending(int a, int b) { return a - b; }
int descending(int a, int b) { return b - a; }

int main() {
    int arr[] = {5, 2, 8, 1, 9};
    bubbleSort(arr, 5, ascending);   // Sorts ascending
    bubbleSort(arr, 5, descending);   // Sorts descending
    return 0;
}
```

### 7.3 Array of Function Pointers

```c
int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }
int mul(int a, int b) { return a * b; }

int (*operations[3])(int, int) = {add, sub, mul};

int main() {
    printf("%d", operations[0](10, 5));  // 15
    printf("%d", operations[1](10, 5));   // 5
    printf("%d", operations[2](10, 5));   // 50
}
```

---

## 8. Dynamic Memory Allocation

### 8.1 Stack vs Heap

| Aspect | Stack | Heap |
|--------|-------|------|
| Memory | Contiguous block | Non-contiguous, scattered |
| Allocation | Compile-time (automatic) | Runtime (manual) |
| Deallocation | Automatic (function return) | Manual (free) |
| Size | Limited (~1-8 MB) | Large (system RAM) |
| Access | Faster | Slower |
| Management | OS/Compiler | Programmer |

**Memory Layout of a C Program:**
```
+------------------+
|      Code        |  (Text Segment)
+------------------+
|     Global       |  (Data Segment)
+------------------+
|       Heap       |  (Grows upward)
|        ↓         |
|        ↑         |
|      Stack       |  (Grows downward)
+------------------+
|    Command Line  |
|   Environment    |
+------------------+
```

### 8.2 Dynamic Allocation Functions

#### malloc() - Memory Allocation
```c
void *malloc(size_t size);

// Example: Allocate memory for 5 integers
int *arr = (int *)malloc(5 * sizeof(int));
if (arr == NULL) {
    printf("Memory allocation failed");
    exit(1);
}
arr[0] = 10;
// Always check for NULL
```

#### calloc() - Contiguous Allocation
```c
void *calloc(size_t num, size_t size);

// Initializes all bytes to zero
int *arr = (int *)calloc(5, sizeof(int));  // All elements = 0
```

**Key Difference:**
```c
int *m = (int *)malloc(5 * sizeof(int));  // Contains garbage values
int *c = (int *)calloc(5, sizeof(int));    // All values = 0
```

#### realloc() - Reallocation
```c
void *realloc(void *ptr, size_t newSize);

// Expand array from 5 to 10 elements
int *newArr = (int *)realloc(arr, 10 * sizeof(int));
if (newArr == NULL) {
    printf("Reallocation failed");
    free(arr);
    exit(1);
}
arr = newArr;
```

#### free() - Deallocation
```c
free(ptr);  // Releases allocated memory
ptr = NULL; // Prevent dangling pointer
```

### 8.3 Complete Example: Dynamic Array

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    printf("Enter number of elements: ");
    scanf("%d", &n);
    
    // Dynamic allocation
    int *arr = (int *)malloc(n * sizeof(int));
    if (arr == NULL) {
        printf("Memory allocation failed");
        return 1;
    }
    
    // Input elements
    printf("Enter %d elements: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", arr + i);  // or &arr[i]
    }
    
    // Display elements
    printf("Elements: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", *(arr + i));
    }
    
    // Free memory
    free(arr);
    return 0;
}
```

---

## 9. Const and Volatile Pointers

### 9.1 Types of Const Pointers

1. **Pointer to Constant:**
```c
int num = 10;
const int *ptr = &num;  // Cannot modify *ptr, but can change ptr
// *ptr = 20;  // ERROR
ptr = &another;  // OK
```

2. **Constant Pointer:**
```c
int num = 10;
int *const ptr = &num;  // Cannot change ptr, but can modify *ptr
*ptr = 20;  // OK
// ptr = &another;  // ERROR
```

3. **Constant Pointer to Constant:**
```c
int num = 10;
const int *const ptr = &num;  // Neither can be changed
```

### 9.2 Volatile Pointer

Used for hardware registers or shared memory:

```c
volatile int *ptr = (volatile int *)0x40001000;  // Hardware register
```

---

## 10. Common Pitfalls and Best Practices

### 10.1 Dangling Pointers

A pointer that points to freed memory or an invalid address:

```c
// Problem: Dangling pointer
int *ptr = (int *)malloc(sizeof(int));
free(ptr);
// ptr is now dangling (still holds old address)

// Solution: Always set to NULL after free
ptr = NULL;
```

### 10.2 Memory Leaks

Failing to release dynamically allocated memory:

```c
// Memory leak: No free()
void leakyFunction() {
    int *ptr = (int *)malloc(sizeof(int));
    // Missing: free(ptr);
}

// Fixed version
void correctFunction() {
    int *ptr = (int *)malloc(sizeof(int));
    if (ptr) {
        // Use pointer
        free(ptr);
        ptr = NULL;
    }
}
```

### 10.3 Null Pointers

Always initialize pointers and check before use:

```c
int *ptr = NULL;
// Always check before dereferencing
if (ptr != NULL) {
    printf("%d", *ptr);
}
```

### 10.4 Uninitialized Pointers

Never use uninitialized pointers:

```c
// WRONG
int *ptr;
*ptr = 10;  // Writing to random memory - CRASH

// CORRECT
int *ptr = (int *)malloc(sizeof(int));
*ptr = 10;
```

### 10.5 Memory Checker Tools

Use **valgrind** to detect memory issues:
```bash
valgrind --leak-check=full ./program
```

---

## 11. Practical Examples

### Example 1: Dynamic String Handling

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* stringConcatenate(const char *s1, const char *s2) {
    // Allocate memory for both strings + null terminator
    char *result = (char *)malloc(strlen(s1) + strlen(s2) + 1);
    if (result == NULL) {
        return NULL;
    }
    
    // Copy first string
    char *ptr = result;
    while (*s1) {
        *ptr++ = *s1++;
    }
    
    // Append second string
    while (*s2) {
        *ptr++ = *s2++;
    }
    *ptr = '\0';
    
    return result;
}

int main() {
    char *str1 = "Hello ";
    char *str2 = "World!";
    
    char *concat = stringConcatenate(str1, str2);
    if (concat) {
        printf("Concatenated: %s\n", concat);
        free(concat);  // Don't forget to free!
    }
    return 0;
}
```

### Example 2: Linked List Node Creation

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

struct Node* createNode(int value) {
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Memory allocation failed");
        return NULL;
    }
    newNode->data = value;
    newNode->next = NULL;
    return newNode;
}

void insertAtEnd(struct Node **head, int value) {
    struct Node *newNode = createNode(value);
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    struct Node *temp = *head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
}

void displayList(struct Node *head) {
    while (head != NULL) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

int main() {
    struct Node *head = NULL;
    insertAtEnd(&head, 10);
    insertAtEnd(&head, 20);
    insertAtEnd(&head, 30);
    displayList(head);
    return 0;
}
```

---

## 12. Key Takeaways

1. **Pointers store memory addresses**, enabling direct memory access and manipulation
2. **Pointer types** ensure type safety in pointer arithmetic operations
3. **Arrays and pointers** have a deep relationship—array names decay to pointers in most contexts
4. **Dynamic memory allocation** (malloc/calloc/realloc/free) allows runtime memory management
5. **Pointer to pointers** is essential for modifying pointer values and creating multidimensional structures
6. **Function pointers** enable callbacks, state machines, and polymorphic behavior
7. **Memory leaks and dangling pointers** are critical bugs—always free memory and set pointers to NULL
8. **const and volatile** qualifiers add safety to pointer usage
9. **Stack memory** is limited and automatic; **heap memory** is larger but requires manual management

---

## 13. Challenging Assessment Questions

### Multiple Choice Questions

**Easy:**
1. What does `*ptr` denote in C?
   - a) Address stored in ptr
   - b) Value at address stored in ptr
   - c) Multiplication
   - d) Comment

2. Which operator is used to get the address of a variable?
   - a) *
   - b) &
   - c) %
   - d) #

**Medium:**
3. What will be the output?
   ```c
   int arr[5] = {1, 2, 3, 4, 5};
   int *ptr = arr + 2;
   printf("%d", *(ptr - 1));
   ```
   - a) 1
   - b) 2
   - c) 3
   - d) 4

4. What is the difference between `malloc` and `calloc`?
   - a) malloc is faster
   - b) calloc initializes memory to zero
   - c) malloc takes one argument, calloc takes two
   - d) Both b and c

5. A pointer that has been freed but not set to NULL is called:
   - a) Null pointer
   - b) Wild pointer
   - c) Dangling pointer
   - d) Constant pointer

**Hard:**
6. Consider:
   ```c
   int arr[3][2] = {{1,2}, {3,4}, {5,6}};
   printf("%d %d", *(arr[1]+1), *(*(arr+1)+1));
   ```
   What is the output?
   - a) 3 3
   - b) 4 4
   - c) 4 5
   - d) 4 6

7. What does the following function do?
   ```c
   void foo(int *p, int *q) {
       int *temp;
       temp = p;
       p = q;
       q = temp;
   }
   ```
   - a) Swaps values pointed by p and q
   - b) Swaps pointer addresses locally
   - c) Swaps global variables
   - d) Causes compilation error

8. If `int **ptr` is a pointer to pointer to int, what is the size of `ptr` on a 64-bit system?
   - a) 2 bytes
   - b) 4 bytes
   - c) 8 bytes
   - d) 16 bytes

9. Which of the following is NOT a valid way to declare a pointer to function returning int?
   - a) `int *func();`
   - b) `int (*func)();`
   - c) `int (*func)(int, int);`
   - d) None of the above

10. What is the output?
    ```c
    int const *p = NULL;
    int num = 10;
    p = &num;
    printf("%d", *p);
    ```
    - a) Compilation error
    - b) 10
    - c) Garbage value
    - d) 0

**Answers:** 1-b, 2-b, 3-b, 4-d, 5-c, 6-b, 7-b, 8-c, 9-a, 10-b

---

## 14. Exam Tips and Important Questions

### Frequently Asked Questions in Exams:

1. **Explain the difference between array and pointer with example**
2. **Write a program to dynamically allocate memory for a 2D array**
3. **Explain malloc, calloc, realloc, and free with syntax and differences**
4. **What is a dangling pointer? How can it be avoided?**
5. **Explain pointer arithmetic with examples**
6. **What is memory leak? How to prevent it?**
7. **Explain function pointers with a practical example**
8. **Write a program to reverse a string using pointers**
9. **Explain const and volatile pointers with examples**
10. **Difference between stack and heap memory**

### Common Program Patterns to Practice:
- Dynamic array creation and manipulation
- String operations using pointers
- Pointer arithmetic in arrays
- Dynamic memory for structures (linked list nodes)
- Function pointers for callbacks

### Key Scoring Points:
- Always mention `#include <stdlib.h>` for dynamic memory functions
- Always check for NULL after malloc/calloc/realloc
- Always free dynamically allocated memory
- Always initialize pointers before use
- Use proper format specifiers (`%p` for addresses, `%d` for integers)
- Explain concepts with clean, commented code examples

---

*Prepared for MCA (Delhi University) — Revised June 2024 Syllabus*
*Topic Coverage: Unit III — Pointers and Dynamic Memory Management*