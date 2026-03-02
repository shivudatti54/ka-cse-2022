# Static and Dynamic Memory Allocation in C++

## Introduction

Memory management is one of the most critical aspects of programming in C++, and understanding the difference between static and dynamic memory allocation is fundamental to writing efficient, bug-free code. In the context of University of Delhi's Computer Science program, this topic forms the backbone of resource management and is frequently tested in both internal assessments and end-semester examinations.

When a C++ program executes, the operating system allocates memory in two primary regions: the stack and the heap. Static memory allocation occurs at compile time, where memory is allocated on the stack for fixed-size variables and data structures. This allocation is automatic—the memory is allocated when a function is called and deallocated when the function returns. In contrast, dynamic memory allocation occurs at runtime on the heap, giving programmers explicit control over when memory is allocated and released. This flexibility is essential for creating data structures whose size is unknown at compile time, such as linked lists, trees, and dynamic arrays.

The importance of mastering memory allocation extends beyond academic requirements. In real-world software development, improper memory management leads to common bugs like memory leaks, dangling pointers, buffer overflows, and undefined behavior. Companies like Google, Microsoft, and Amazon frequently test candidates' understanding of memory management in technical interviews, making this topic essential for your career prospects.

## Key Concepts

### Static Memory Allocation

Static memory allocation happens at compile time, and the memory remains allocated throughout the program's execution for global variables or throughout the scope for local variables. The compiler determines the exact size of all variables during compilation, and this information is fixed.

**Stack Memory**: The stack is a contiguous region of memory that grows and shrinks as functions are called and return. Local variables, function parameters, and return addresses are stored here. The stack follows a Last-In-First-Out (LIFO) order.

Key characteristics of static allocation:
- Memory size must be known at compile time
- Allocation and deallocation are automatic (compiler-managed)
- Faster access compared to heap memory
- Limited stack size (typically 1-8 MB)
- No risk of memory leaks (automatic cleanup)

```cpp
// Static memory allocation examples
int num = 10;              // 4 bytes on stack
char grade = 'A';          // 1 byte on stack
double prices[100];        // 800 bytes on stack
std::string name = "DU";   // Small string optimization may apply
```

### Dynamic Memory Allocation

Dynamic memory allocation occurs at runtime using the heap, a large pool of memory available to programs. The programmer has explicit control over when memory is allocated and freed.

**Heap Memory**: The heap is a larger but slower region of memory used for dynamic allocation. Memory here must be manually managed by the programmer.

#### The `new` Operator

The `new` operator allocates memory on the heap and returns a pointer to the allocated memory.

```cpp
// Single variable allocation
int* ptr = new int;        // Allocates sizeof(int) bytes
*ptr = 25;                 // Assigns value through pointer
delete ptr;                // Releases memory

// Array allocation
int* arr = new int[50];    // Allocates array of 50 integers
delete[] arr;              // Must use delete[] for arrays
```

#### The `delete` Operator

The `delete` operator frees memory that was allocated with `new`. Using `delete` on memory not allocated with `new`, or failing to delete memory, leads to undefined behavior.

```cpp
// Correct usage
int* p1 = new int(100);    // Allocation with initialization
delete p1;                 // Single object deallocation

int* p2 = new int[10];     // Array allocation
delete[] p2;               // Array deallocation (note the brackets)

// Common mistakes:
int x;
int* p3 = &x;
delete p3;                 // WRONG: p3 doesn't point to heap memory

int* p4;
delete p4;                 // WRONG: p4 is uninitialized (wild pointer)
```

### C-Style Memory Management

Before C++ introduced the `new` and `delete` operators, C-style memory management using `malloc()`, `calloc()`, `realloc()`, and `free()` was used. Understanding these is important for legacy code and competitive programming.

| Function | Purpose | Syntax |
|----------|---------|--------|
| `malloc()` | Allocates uninitialized memory | `malloc(size_in_bytes)` |
| `calloc()` | Allocates zero-initialized memory | `calloc(num_elements, size_of_each)` |
| `realloc()` | Resizes previously allocated memory | `realloc(ptr, new_size)` |
| `free()` | Releases allocated memory | `free(ptr)` |

```cpp
// C-style allocation
int* ptr = (int*)malloc(sizeof(int));    // Allocate 4 bytes
*ptr = 42;
free(ptr);                               // Release memory

// Array with calloc (zero-initialized)
int* arr = (int*)calloc(10, sizeof(int)); // 10 integers, all zero

// Resize with realloc
arr = (int*)realloc(arr, 20 * sizeof(int)); // Now 20 integers
free(arr);
```

### Smart Pointers (Modern C++)

C++11 introduced smart pointers that automatically manage memory, reducing the risk of memory leaks. These are part of the Standard Library and are highly recommended for modern C++ programming.

```cpp
#include <memory>

// unique_ptr - exclusive ownership
std::unique_ptr<int> uptr = std::make_unique<int>(100);
// Automatically deleted when uptr goes out of scope

// shared_ptr - shared ownership with reference counting
std::shared_ptr<int> sptr1 = std::make_shared<int>(50);
std::shared_ptr<int> sptr2 = sptr1; // Reference count = 2

// weak_ptr - non-owning reference to shared_ptr
std::weak_ptr<int> wptr = sptr1;
```

## Examples

### Example 1: Dynamic Array Implementation

**Problem**: Write a program that dynamically allocates an array of integers, takes input from the user, and displays the sum.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;
    
    // Dynamic memory allocation
    int* arr = new int[n];
    
    // Input elements
    cout << "Enter " << n << " integers:" << endl;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    // Calculate sum
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    
    cout << "Sum: " << sum << endl;
    
    // Important: Free the allocated memory
    delete[] arr;
    
    return 0;
}
```

**Output Example**:
```
Enter number of elements: 5
Enter 5 integers:
10 20 30 40 50
Sum: 150
```

### Example 2: 2D Dynamic Array

**Problem**: Create a dynamic 2D array (matrix) of size m×n and initialize it.

```cpp
#include <iostream>
using namespace std;

int main() {
    int rows = 3, cols = 4;
    
    // Allocate pointer to array of pointers (array of rows)
    int** matrix = new int*[rows];
    
    // Allocate each row
    for (int i = 0; i < rows; i++) {
        matrix[i] = new int[cols];
    }
    
    // Initialize with values
    int val = 1;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            matrix[i][j] = val++;
        }
    }
    
    // Display matrix
    cout << "Matrix:" << endl;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cout << matrix[i][j] << "\t";
        }
        cout << endl;
    }
    
    // Deallocate memory (reverse order)
    for (int i = 0; i < rows; i++) {
        delete[] matrix[i];
    }
    delete[] matrix;
    
    return 0;
}
```

### Example 3: Understanding Memory Leaks

**Problem**: Identify the memory leak in the following code and fix it.

```cpp
#include <iostream>
using namespace std;

void leakyFunction() {
    int* ptr = new int[100];
    // Some operations
    // Missing delete[] - MEMORY LEAK!
}

void fixedFunction() {
    int* ptr = new int[100];
    // Some operations
    delete[] ptr;  // Memory properly released
}

// Better approach using smart pointers
void modernApproach() {
    auto ptr = make_unique<int[]>(100);
    // No need to delete - automatic cleanup
}
```

## Exam Tips

1. **Remember the difference**: Static allocation uses stack memory (automatic, compile-time), while dynamic allocation uses heap memory (manual, runtime).

2. **Always pair new with delete**: For every `new`, there must be a corresponding `delete`. For arrays, use `delete[]`.

3. **Smart pointers in modern C++**: Prefer `std::unique_ptr` and `std::make_unique` over raw pointers to prevent memory leaks.

4. **malloc vs new**: `malloc` returns `void*` and requires casting, while `new` returns the correctly typed pointer. `new` calls constructors, `malloc` does not.

5. **NULL vs nullptr**: Always use `nullptr` (C++11) instead of `NULL` for null pointers to avoid ambiguity with function overloading.

6. **Memory leak detection**: In exams, trace through code to identify paths where `delete` is not executed (especially in error conditions or early returns).

7. **Dangling pointers**: After `delete`, set pointers to `nullptr` to avoid accessing freed memory accidentally.

8. **Stack overflow**: Be aware that large static arrays (like `int arr[1000000]`) can cause stack overflow; use dynamic allocation for large data.

9. **Virtual memory**: Understand that stack has limited size while heap can grow (subject to system limits).

10. **Common exam question**: Predict the output or identify errors in code involving `new`, `delete`, and pointer arithmetic.