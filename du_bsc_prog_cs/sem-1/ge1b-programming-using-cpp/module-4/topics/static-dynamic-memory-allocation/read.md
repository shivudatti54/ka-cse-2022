# Static and Dynamic Memory Allocation in C++

## Introduction

Memory management is one of the most critical aspects of programming in C++. Understanding how memory is allocated and deallocated is essential for writing efficient, bug-free programs. In C++, memory is divided into different segments, each serving a specific purpose. The two primary methods of memory allocation are **static (compile-time) allocation** and **dynamic (runtime) allocation**. 

Static memory allocation occurs when the compiler determines the size of variables at compile time, while dynamic memory allocation allows programmers to request memory during program execution. This flexibility is particularly important when working with data structures whose size is unknown until runtime, such as linked lists, trees, and dynamic arrays. For University of Delhi's Computer Science students, mastering this topic is crucial not only for academic success but also for developing professional-grade C++ programming skills. This module explores the intricacies of both allocation methods, their advantages, disadvantages, and practical applications in real-world scenarios.

## Key Concepts

### Memory Segments in C++

When a C++ program executes, the system's memory is divided into several segments:

1. **Code Segment (Text Segment)**: Contains the compiled machine code of the program. This segment is typically read-only.

2. **Data Segment**: Stores global and static variables. It is further divided into:
   - **Initialized Data Segment**: Contains explicitly initialized global and static variables
   - **Uninitialized Data Segment (BSS)**: Contains uninitialized global and static variables (automatically initialized to zero)

3. **Stack Segment**: Used for storing function call information, local variables, and return addresses. Memory allocation and deallocation happen automatically (LIFO - Last In First Out).

4. **Heap Segment**: Also known as the "free store," this is where dynamic memory allocation occurs. The heap grows upward (in most architectures) and is managed by the programmer.

### Static Memory Allocation

Static memory allocation occurs at compile time, before the program begins execution. The compiler determines the exact amount of memory needed for each variable and allocates it in either the stack or data segment.

**Characteristics of Static Allocation:**
- Memory size must be known at compile time
- Memory is allocated automatically when the program starts
- Memory is deallocated automatically when the variable goes out of scope
- No explicit memory management required by the programmer
- Faster execution (no runtime overhead)

**Examples of Static Allocation:**
```cpp
int x = 10;              // Stack allocation
int arr[100];            // Stack allocation (fixed size)
static int y = 20;       // Data segment
```

### Dynamic Memory Allocation

Dynamic memory allocation allows programs to request memory at runtime using the **heap** segment. This is essential when:
- The size of data is unknown until runtime
- You need memory that persists beyond the scope of a function
- You want to optimize memory usage by allocating only what's needed

**C++ Dynamic Allocation Operators:**

1. **new operator**: Allocates single object
```cpp
int* ptr = new int;           // Allocates one integer on heap
int* ptr = new int(50);       // Allocates and initializes to 50
```

2. **new[] operator**: Allocates array
```cpp
int* arr = new int[100];      // Allocates array of 100 integers
```

3. **delete operator**: Deallocates single object
```cpp
delete ptr;                   // Frees memory pointed by ptr
ptr = nullptr;                // Good practice to avoid dangling pointer
```

4. **delete[] operator**: Deallocates array
```cpp
delete[] arr;                 // Frees the entire array
```

### Pointers and Memory Addresses

Pointers are variables that store memory addresses. They are the primary mechanism for accessing dynamically allocated memory.

```cpp
int* ptr = new int;    // ptr holds address of allocated memory
*ptr = 25;             // Dereferencing to store value
cout << *ptr;          // Accessing the value
```

### Memory Leaks and Dangling Pointers

**Memory Leak**: Occurs when dynamically allocated memory is not deallocated, causing the program to consume more and more memory over time.

```cpp
// Memory leak example
void leakyFunction() {
    int* ptr = new int[100];
    // Missing delete[] ptr;
    // Each call leaks 100 integers
}
```

**Dangling Pointer**: A pointer that points to memory that has been freed. Accessing such memory leads to undefined behavior.

```cpp
// Dangling pointer example
int* ptr = new int(10);
delete ptr;
// ptr is now a dangling pointer
// Accessing *ptr here is dangerous
ptr = nullptr;  // Prevents accidental access
```

### Smart Pointers (Modern C++)

C++11 introduced smart pointers that automatically manage memory, preventing leaks:

1. **unique_ptr**: Exclusive ownership, automatically deletes when it goes out of scope
```cpp
#include <memory>
std::unique_ptr<int> ptr = std::make_unique<int>(25);
```

2. **shared_ptr**: Shared ownership with reference counting
```cpp
std::shared_ptr<int> ptr1 = std::make_shared<int>(50);
std::shared_ptr<int> ptr2 = ptr1;  // Both point to same memory
```

## Examples

### Example 1: Dynamic Array Input

**Problem**: Write a program to dynamically allocate an array of n integers, accept values, and display them.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;
    
    // Dynamic allocation
    int* arr = new int[n];
    
    // Accept values
    cout << "Enter " << n << " integers:" << endl;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    // Display values
    cout << "You entered: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    // Deallocate memory
    delete[] arr;
    
    return 0;
}
```

**Explanation**: 
- We use `new int[n]` to allocate memory for n integers at runtime
- The array can be of any size determined by user input
- `delete[] arr` frees the entire array memory

### Example 2: Dynamic 2D Array

**Problem**: Create a dynamic 2D array (matrix) of size m×n and initialize with values.

```cpp
#include <iostream>
using namespace std;

int main() {
    int m, n;
    cout << "Enter rows and columns: ";
    cin >> m >> n;
    
    // Allocate 2D array dynamically
    int** matrix = new int*[m];      // Array of row pointers
    for (int i = 0; i < m; i++) {
        matrix[i] = new int[n];      // Each row has n columns
    }
    
    // Initialize with values
    int value = 1;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            matrix[i][j] = value++;
        }
    }
    
    // Display matrix
    cout << "Matrix:" << endl;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cout << matrix[i][j] << "\t";
        }
        cout << endl;
    }
    
    // Deallocate memory (important: reverse order)
    for (int i = 0; i < m; i++) {
        delete[] matrix[i];
    }
    delete[] matrix;
    
    return 0;
}
```

**Key Points**:
- First allocate array of pointers (rows), then each row
- Always deallocate in reverse order of allocation
- Failure to deallocate causes memory leaks

### Example 3: Using Smart Pointers

**Problem**: Demonstrate automatic memory management using smart pointers.

```cpp
#include <iostream>
#include <memory>
using namespace std;

class Rectangle {
    int width, height;
public:
    Rectangle(int w, int h) : width(w), height(h) {
        cout << "Constructor called" << endl;
    }
    ~Rectangle() {
        cout << "Destructor called" << endl;
    }
    int area() { return width * height; }
};

int main() {
    cout << "Using unique_ptr:" << endl;
    {
        unique_ptr<Rectangle> ptr = make_unique<Rectangle>(10, 5);
        cout << "Area: " << ptr->area() << endl;
        // Automatic deletion when ptr goes out of scope
    }
    cout << "Outside scope - memory freed" << endl;
    
    cout << "\nUsing shared_ptr:" << endl;
    {
        shared_ptr<Rectangle> ptr1 = make_shared<Rectangle>(20, 10);
        shared_ptr<Rectangle> ptr2 = ptr1;  // Reference count = 2
        cout << "ptr1 area: " << ptr1->area() << endl;
        cout << "ptr2 area: " << ptr2->area() << endl;
        cout << "Reference count: " << ptr2.use_count() << endl;
        // Memory freed only when both ptr1 and ptr2 go out of scope
    }
    cout << "Outside scope - memory freed" << endl;
    
    return 0;
}
```

**Output**:
```
Using unique_ptr:
Constructor called
Area: 50
Destructor called
Outside scope - memory freed

Using shared_ptr:
Constructor called
ptr1 area: 200
ptr2 area: 200
Reference count: 2
Destructor called
Outside scope - memory freed
```

## Exam Tips

1. **Understand the difference between stack and heap allocation**: Stack allocation is automatic and fast but limited in size; heap allocation is flexible but requires manual management.

2. **Always pair new with delete, and new[] with delete[]**: Mismatching these causes undefined behavior and memory corruption.

3. **Set pointers to nullptr after deletion**: This prevents dangling pointer bugs and makes debugging easier.

4. **Remember the memory layout**: Code segment → Data segment → Heap → Stack (in most systems).

5. **Smart pointers are preferred in modern C++**: In C++11 and above, use unique_ptr and shared_ptr instead of raw pointers for better memory safety.

6. **Common exam questions**:
   - Difference between static and dynamic allocation
   - Write code to create/delete 1D and 2D dynamic arrays
   - Identify memory leaks in code
   - Explain dangling pointers and how to avoid them

7. **Time complexity matters**: Accessing elements in static and dynamic arrays is O(1), but dynamic allocation itself takes O(n) time where n is the size.