# Pointer Reference Variables in C++

## A Comprehensive Study Material for BSc Physical Science (CS) - Delhi University (NEP 2024)

---

## 1. Introduction

### 1.1 What are Pointers and Reference Variables?

In C++, **pointers** and **reference variables** are two fundamental concepts that allow programmers to work with memory addresses directly. These are essential tools for efficient memory management, dynamic data structures, and pass-by-reference semantics. As per the Delhi University BSc Physical Science (CS) syllabus under GE1B "Programming Using C++", mastering these concepts is crucial for understanding how C++ manages memory and how data is passed between functions.

**Pointers** are variables that store the memory address of another variable. They provide indirect access to data and enable powerful operations like dynamic memory allocation, array manipulation, and creating complex data structures.

**Reference variables** are aliases (alternative names) for existing variables. They provide a way to pass variables to functions by reference, allowing functions to modify the original data without creating copies.

### 1.2 Real-World Relevance

Understanding pointers and references is essential because:

- **Dynamic Memory Allocation**: Applications like video games, database systems, and embedded systems require dynamic memory management
- **Data Structures**: Linked lists, trees, graphs, and other complex data structures rely heavily on pointers
- **Function Efficiency**: Passing large objects by reference (rather than by value) saves memory and improves performance
- **System Programming**: Operating systems and device drivers use pointers for hardware interaction
- **Resource Management**: Smart pointers in modern C++ help prevent memory leaks

---

## 2. Pointers in C++

### 2.1 Declaration and Initialization

A pointer variable is declared using the asterisk (*) symbol. The syntax is:

```cpp
data_type* pointer_name;
```

Or equivalently:

```cpp
data_type *pointer_name;
```

**Example:**

```cpp
int age = 25;
int* ptr;          // Declaration of an integer pointer
ptr = &age;        // & is the address-of operator
```

The `&` operator (address-of) returns the memory address of a variable. The `*` operator (dereference) accesses the value stored at that address.

### 2.2 Working with Pointers

```cpp
#include <iostream>
using namespace std;

int main() {
    int number = 42;
    int* ptr = &number;
    
    cout << "Value of number: " << number << endl;
    cout << "Address of number: " << &number << endl;
    cout << "Value stored in ptr: " << ptr << endl;
    cout << "Dereferenced value (*ptr): " << *ptr << endl;
    
    *ptr = 100;  // Modifying value through pointer
    cout << "New value of number: " << number << endl;
    
    return 0;
}
```

**Output:**
```
Value of number: 42
Address of number: 0x7ffd5a3c4a44
Value stored in ptr: 0x7ffd5a3c4a44
Dereferenced value (*ptr): 42
New value of number: 100
```

### 2.3 Pointer Types

C++ is a statically typed language, so pointers must be declared with a specific data type:

```cpp
int* intPtr;      // Pointer to integer
char* charPtr;    // Pointer to character
double* dblPtr;   // Pointer to double
void* voidPtr;    // Void pointer - can point to any type
```

---

## 3. Reference Variables in C++

### 3.1 What are Reference Variables?

A **reference variable** is an alias (alternative name) for an existing variable. It is created using the ampersand (&) symbol in the declaration. Unlike pointers, references must be initialized when declared and cannot be reseated to refer to a different variable.

**Syntax:**

```cpp
data_type& reference_name = variable_name;
```

### 3.2 Key Properties of References

1. **No Separate Memory**: References typically share the same memory address as the original variable
2. **Must be Initialized**: A reference must be initialized during declaration
3. **Cannot be Null**: Unlike pointers, references cannot be null
4. **Cannot be Reseated**: Once initialized, a reference always refers to the same variable

### 3.3 Example: Understanding References

```cpp
#include <iostream>
using namespace std;

int main() {
    int original = 50;
    int& ref = original;  // ref is an alias for original
    
    cout << "Original value: " << original << endl;
    cout << "Reference value: " << ref << endl;
    cout << "Address of original: " << &original << endl;
    cout << "Address of reference: " << &ref << endl;
    
    ref = 100;  // Modifying through reference
    cout << "After modification - Original: " << original << endl;
    
    return 0;
}
```

**Output:**
```
Original value: 50
Reference value: 50
Address of original: 0x7ffd5a3c4a44
Address of reference: 0x7ffd5a3c4a44
After modification - Original: 100
```

---

## 4. Pointer Arithmetic

### 4.1 Overview

C++ allows certain arithmetic operations on pointers. These operations are particularly useful when working with arrays. The valid operations are:

- **Increment (++)**: Move to next memory location of the same type
- **Decrement (--)**: Move to previous memory location
- **Addition (+)**: Add an integer to a pointer
- **Subtraction (-)**: Subtract an integer from a pointer or subtract two pointers

### 4.2 How Pointer Arithmetic Works

When you perform arithmetic on pointers, the compiler automatically scales the value by the size of the data type. For example, if an `int` is 4 bytes, incrementing an `int*` moves the pointer 4 bytes forward in memory.

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int* ptr = arr;  // Points to first element (arr[0])
    
    cout << "Initial position - *ptr: " << *ptr << endl;
    
    ptr++;  // Move to next integer
    cout << "After ptr++ - *ptr: " << *ptr << endl;
    
    ptr = ptr + 2;  // Move 2 positions ahead
    cout << "After ptr + 2 - *ptr: " << *ptr << endl;
    
    // Pointer subtraction
    int* ptr2 = &arr[4];
    long diff = ptr2 - ptr;
    cout << "Difference between pointers: " << diff << endl;
    
    return 0;
}
```

**Output:**
```
Initial position - *ptr: 10
After ptr++ - *ptr: 20
After ptr + 2 - *ptr: 50
Difference between pointers: 2
```

---

## 5. Arrays and Pointers

### 5.1 The Relationship

In C++, the name of an array acts as a **pointer constant** pointing to the first element of the array. This is a fundamental relationship that enables array manipulation through pointers.

```cpp
int numbers[] = {1, 2, 3, 4, 5};
int* ptr = numbers;  // Equivalent to: int* ptr = &numbers[0];
```

### 5.2 Array Traversal Using Pointers

```cpp
#include <iostream>
using namespace std;

int main() {
    int marks[] = {85, 90, 78, 92, 88};
    int n = sizeof(marks) / sizeof(marks[0]);
    
    // Using array index notation
    cout << "Using array notation: ";
    for (int i = 0; i < n; i++) {
        cout << marks[i] << " ";
    }
    cout << endl;
    
    // Using pointer arithmetic
    cout << "Using pointer arithmetic: ";
    int* ptr = marks;
    for (int i = 0; i < n; i++) {
        cout << *(ptr + i) << " ";  // or *(marks + i)
    }
    cout << endl;
    
    // Using pointer increment
    cout << "Using pointer increment: ";
    for (int* p = marks; p < marks + n; p++) {
        cout << *p << " ";
    }
    cout << endl;
    
    return 0;
}
```

**Output:**
```
Using array notation: 85 90 78 92 88
Using pointer arithmetic: 85 90 78 92 88
Using pointer increment: 85 90 78 92 88
```

### 5.3 Passing Arrays to Functions

When passing arrays to functions, they decay to pointers. This is why sizeof() doesn't work as expected inside functions:

```cpp
#include <iostream>
using namespace std;

// Function to calculate average - array decays to pointer
double calculateAverage(int arr[], int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];  // or *(arr + i)
    }
    return static_cast<double>(sum) / size;
}

int main() {
    int scores[] = {85, 90, 78, 92, 88};
    int n = sizeof(scores) / sizeof(scores[0]);
    
    cout << "Average score: " << calculateAverage(scores, n) << endl;
    
    return 0;
}
```

---

## 6. Dynamic Memory Allocation

### 6.1 Introduction

Dynamic memory allocation allows programs to allocate memory at runtime rather than compile time. This is essential for creating data structures whose size is not known until runtime. C++ provides two operators for dynamic memory allocation:

- **`new`**: Allocates memory
- **`delete`**: Deallocates memory

### 6.2 Single Variable Allocation

```cpp
#include <iostream>
using namespace std;

int main() {
    // Allocate a single integer
    int* ptr = new int;
    *ptr = 42;
    
    cout << "Value: " << *ptr << endl;
    
    // Deallocate when done
    delete ptr;
    ptr = nullptr;  // Good practice to avoid dangling pointers
    
    return 0;
}
```

### 6.3 Array Allocation

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;
    
    // Dynamic array allocation
    int* arr = new int[n];
    
    // Input values
    for (int i = 0; i < n; i++) {
        cout << "Enter element " << i + 1 << ": ";
        cin >> arr[i];
    }
    
    // Display values
    cout << "Entered values: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    // Deallocate
    delete[] arr;
    arr = nullptr;
    
    return 0;
}
```

### 6.4 Dynamic 2D Arrays

```cpp
#include <iostream>
using namespace std;

int main() {
    int rows = 3, cols = 4;
    
    // Allocate 2D array
    int** matrix = new int*[rows];
    for (int i = 0; i < rows; i++) {
        matrix[i] = new int[cols];
    }
    
    // Initialize with values
    int count = 1;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            matrix[i][j] = count++;
        }
    }
    
    // Display matrix
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cout << matrix[i][j] << "\t";
        }
        cout << endl;
    }
    
    // Deallocate
    for (int i = 0; i < rows; i++) {
        delete[] matrix[i];
    }
    delete[] matrix;
    matrix = nullptr;
    
    return 0;
}
```

---

## 7. Const Pointers and Pointers to Const

### 7.1 Types of Const with Pointers

C++ provides several ways to use `const` with pointers:

1. **Pointer to Constant**: Cannot modify the value through the pointer
2. **Constant Pointer**: Cannot change the address it points to
3. **Constant Pointer to Constant**: Neither the address nor the value can be changed

### 7.2 Examples

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 20;
    
    // 1. Pointer to constant (data is const, pointer can change)
    const int* p1 = &a;
    // *p1 = 30;  // ERROR: Cannot modify through p1
    p1 = &b;     // OK: Can change the address
    
    // 2. Constant pointer (address is const, data can change)
    int* const p2 = &a;
    *p2 = 30;    // OK: Can modify through p2
    // p2 = &b;   // ERROR: Cannot change address
    
    // 3. Constant pointer to constant (both are const)
    const int* const p3 = &a;
    // *p3 = 40;  // ERROR
    // p3 = &b;   // ERROR
    
    cout << "a = " << a << ", b = " << b << endl;
    
    return 0;
}
```

---

## 8. Pass-by-Reference Semantics

### 8.1 Pass-by-Value vs Pass-by-Reference

Understanding the difference is crucial for writing efficient C++ code:

- **Pass-by-Value**: Creates a copy of the argument; changes don't affect the original
- **Pass-by-Reference**: The function works with the original data

### 8.2 Pass-by-Reference Using References

```cpp
#include <iostream>
using namespace std;

// Pass by reference using reference variable
void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    int x = 10, y = 20;
    
    cout << "Before swap: x = " << x << ", y = " << y << endl;
    swap(x, y);
    cout << "After swap: x = " << x << ", y = " << y << endl;
    
    return 0;
}
```

**Output:**
```
Before swap: x = 10, y = 20
After swap: x = 20, y = 10
```

### 8.3 Pass-by-Reference Using Pointers

```cpp
#include <iostream>
using namespace std;

// Pass by reference using pointers
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 10, y = 20;
    
    cout << "Before swap: x = " << x << ", y = " << y << endl;
    swap(&x, &y);
    cout << "After swap: x = " << x << ", y = " << y << endl;
    
    return 0;
}
```

### 8.4 When to Use References vs Pointers

| Scenario | Use References | Use Pointers |
|----------|-----------------|--------------|
| Modifying caller variables | ✓ | ✓ |
| Optional parameters (null) | ✗ | ✓ |
| Dynamic polymorphism | ✗ | ✓ |
| Clear intent of "output" parameter | ✓ | ✓ |
| No modification needed | const reference | const pointer |

---

## 9. Pointers to Pointers (Double Pointers)

### 9.1 Concept

A pointer to a pointer is a variable that stores the address of another pointer. This is useful for:

- Dynamic 2D arrays
- Modifying pointers within functions
- Creating linked data structures

```cpp
#include <iostream>
using namespace std;

int main() {
    int value = 42;
    int* ptr1 = &value;      // Pointer to int
    int** ptr2 = &ptr1;      // Pointer to pointer to int
    
    cout << "value: " << value << endl;
    cout << "*ptr1: " << *ptr1 << endl;
    cout << "**ptr2: " << **ptr2 << endl;
    
    return 0;
}
```

### 9.2 Practical Example: Modifying a Pointer

```cpp
#include <iostream>
using namespace std;

void allocateAndInit(int** ptr) {
    *ptr = new int(100);
}

int main() {
    int* p = nullptr;
    allocateAndInit(&p);  // Pass address of pointer
    
    cout << "Value: " << *p << endl;
    
    delete p;
    return 0;
}
```

---

## 10. Common Pitfalls and Best Practices

### 10.1 Common Errors

1. **Uninitialized Pointers**: Always initialize pointers
2. **Dangling Pointers**: Always deallocate memory properly
3. **Memory Leaks**: Always pair new with delete
4. **Null Pointer Dereference**: Always check for nullptr
5. **Pointer Arithmetic on Invalid Memory**: Stay within bounds

### 10.2 Best Practices

```cpp
#include <iostream>
using namespace std;

// Best Practice: Use nullptr instead of NULL
void process(int* ptr) {
    if (ptr != nullptr) {
        cout << "Value: " << *ptr << endl;
    }
}

int main() {
    // Best Practice: Initialize pointers
    int* safePtr = nullptr;
    
    // Best Practice: Check before dereferencing
    if (safePtr != nullptr) {
        cout << *safePtr << endl;
    } else {
        cout << "Pointer is null" << endl;
    }
    
    return 0;
}
```

---

## 11. Delhi University Syllabus Context

As per the GE1B "Programming Using C++" course under NEP 2024 for BSc Physical Science (CS), this study material covers:

- ✓ Pointers: declaration, initialization, and operations
- ✓ Reference variables and their usage
- ✓ Pointer arithmetic
- ✓ Arrays and pointers relationship
- ✓ Dynamic memory allocation (new/delete)
- ✓ Const pointers
- ✓ Pass-by-reference semantics
- ✓ Practical examples and applications

These concepts form the foundation for understanding data structures, memory management, and advanced C++ programming, which are essential for the curriculum.

---

## 12. Key Takeaways

### Pointers
- **Definition**: Variables that store memory addresses of other variables
- **Operators**: `&` (address-of) and `*` (dereference)
- **Types**: Can be typed (int*, char*) or void (void*)
- **Arithmetic**: Support ++, --, +, - operations scaled by data type size

### Reference Variables
- **Definition**: Aliases for existing variables
- **Key Features**: Must be initialized, cannot be null, cannot be reseated
- **Advantage**: Cleaner syntax than pointers for pass-by-reference

### Arrays and Pointers
- Array names decay to pointers to first element
- Pointer arithmetic enables array traversal
- Useful for function parameter passing

### Dynamic Memory
- `new` allocates memory; `delete` deallocates
- Always use `delete[]` for arrays
- Always set pointers to nullptr after deletion

### Const with Pointers
- `const int* p`: Cannot modify data through p
- `int* const p`: Cannot change the address
- `const int* const p`: Neither data nor address can change

### Pass-by-Reference
- References: `void func(int& var)`
- Pointers: `void func(int* var)`
- Both allow modification of caller's data without copying

---

## Assessment Questions

### Multiple Choice Questions

1. **What does a pointer store?**
   - (a) A value
   - (b) A memory address
   - (c) A reference
   - (d) None of the above

2. **Which operator is used to get the address of a variable?**
   - (a) *
   - (b) &
   - (c) →
   - (d) #

3. **What is the output of: int x = 10; int* p = &x; cout << *p;**
   - (a) Address of x
   - (b) 10
   - (c) 0
   - (d) Error

4. **What is a reference variable?**
   - (a) A pointer to a pointer
   - (b) An alias for another variable
   - (c) A constant pointer
   - (d) A null pointer

5. **Which operator is used to dereference a pointer?**
   - (a) &
   - (b) *
   - (d) →
   - (d) %

6. **What is the correct way to declare a constant pointer?**
   - (a) const int* p
   - (b) int const* p
   - (c) int* const p
   - (d) Both (a) and (c)

7. **What does `new` return if allocation fails?**
   - (a) null
   - (b) nullptr
   - (c) 0
   - (d) Throws std::bad_alloc

8. **What is the relationship between arrays and pointers?**
   - (a) They are the same
   - (b) Array name is a pointer constant
   - (c) Pointers cannot work with arrays
   - (d) Arrays cannot be indexed

9. **What is the output of: int a = 5; int& r = a; r = 10; cout << a;**
   - (a) 5
   - (b) 10
   - (c) 15
   - (d) Error

10. **Which is NOT a valid pointer arithmetic operation?**
    - (a) ptr + 1
    - (b) ptr - 1
    - (c) ptr * 2
    - (d) ptr++

### Fill in the Blanks

1. The operator used to access the value at an address stored in a pointer is called the ________ operator.
2. A reference variable must be ________ during declaration.
3. The ________ operator returns the memory address of a variable.
4. Dynamic memory allocation in C++ uses ________ and ________ operators.
5. A pointer that does not point to any valid memory is called a ________ pointer.
6. Array name acts as a ________ pointer pointing to the first element.
7. The process of passing variables to functions without copying is called ________.
8. A ________ pointer can point to any data type.

### Coding Exercises

1. Write a C++ program to swap two numbers using pointers.
2. Write a C++ program to find the sum of array elements using pointer notation.
3. Write a C++ program to dynamically allocate an array and find its maximum element.
4. Write a C++ program demonstrating the difference between pass-by-value, pass-by-reference, and pass-by-pointer.

---

*Study Material prepared for Delhi University BSc Physical Science (CS) - NEP 2024*
*Subject: GE1B Programming Using C++*