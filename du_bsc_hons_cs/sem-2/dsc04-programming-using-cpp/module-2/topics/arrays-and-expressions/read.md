# Arrays and Expressions in C++

## A Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

**Real-World Relevance:**

Arrays and expressions form the backbone of data manipulation in computer science. Consider a student record management system at Delhi University—storing marks of 5000 students requires efficient data structures. An **array** provides contiguous memory to store multiple values of the same data type, enabling fast access and manipulation. **Expressions** combine operators and operands to compute values, essential for algorithmic logic.

In competitive programming, game development (storing pixel data), scientific simulations (weather modeling), and database systems (indexing), arrays are indispensable. This unit aligns with the Delhi University syllabus under "Programming Using C++" and covers foundational concepts required for advanced data structures.

---

## 2. One-Dimensional Arrays

### 2.1 Definition and Declaration

An **array** is a collection of elements stored at contiguous memory locations, accessible via an index.

**Syntax:**
```cpp
data_type array_name[array_size];
```

**Example:**
```cpp
int marks[5];          // Array of 5 integers (uninitialized)
float prices[3] = {10.5, 20.0, 15.75};  // Array with initialization
char grade = 'A';
```

### 2.2 Array Initialization

C++ offers multiple initialization methods:

```cpp
// Method 1: Specify size
int arr1[3] = {10, 20, 30};

// Method 2: Omit size (compiler deduces)
int arr2[] = {1, 2, 3, 4, 5};

// Method 3: Partial initialization (remaining elements = 0)
int arr3[5] = {1, 2};  // arr3 = {1, 2, 0, 0, 0}

// Method 4: Initialize all to zero
int arr4[3] = {};  // All elements = 0
```

### 2.3 Accessing Elements

Array indices **begin at 0** (not 1). Accessing `arr[5]` in an array of size 5 causes **buffer overflow**.

```cpp
int data[4] = {100, 200, 300, 400};

for (int i = 0; i < 4; i++) {
    cout << "data[" << i << "] = " << data[i] << endl;
}
```

**Output:**
```
data[0] = 100
data[1] = 200
data[2] = 300
data[3] = 400
```

### 2.4 Memory Representation

```
Index:     0      1      2      3      4
Address:  0x1000 0x1004 0x1008 0x100C 0x1010
Value:    10     20     30     40     50
          ↑                              ↑
         Base Address                Last Element
```

*Each `int` occupies 4 bytes; addresses increment by 4.*

---

## 3. Multi-Dimensional Arrays

### 3.1 Two-Dimensional Arrays

A 2D array represents **matrices** or **tables**.

**Declaration:**
```cpp
data_type array_name[rows][columns];
```

**Example: Student Marks Matrix (3 students, 4 subjects)**

```cpp
int marks[3][4] = {
    {85, 90, 78, 92},   // Student 1
    {88, 76, 95, 81},   // Student 2
    {90, 85, 88, 79}    // Student 3
};

// Accessing elements
cout << marks[1][2];  // Output: 95 (Student 2, Subject 3)
```

**Memory Layout (Row-Major Order in C++):**

```
marks[0][0] → marks[0][1] → marks[0][2] → marks[0][3] →
marks[1][0] → marks[1][1] → marks[1][2] → marks[1][3] →
marks[2][0] → marks[2][1] → marks[2][2] → marks[2][3]
```

### 3.2 Three-Dimensional Arrays

Useful for 3D data like images (RGB channels) or spatial data.

```cpp
// 2 pages, 3 rows, 4 columns
int cube[2][3][4] = {
    { // Page 0
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    },
    { // Page 1
        {13, 14, 15, 16},
        {17, 18, 19, 20},
        {21, 22, 23, 24}
    }
};

cout << cube[1][2][3];  // Output: 24
```

### 3.3 Initializing Multi-Dimensional Arrays

```cpp
// Both are equivalent
int A[2][3] = {1, 2, 3, 4, 5, 6};
int B[2][3] = {{1, 2, 3}, {4, 5, 6}};
```

---

## 4. Pointers and Array Relationship

### 4.1 Fundamental Relationship

In C++, **the name of an array is a pointer to its first element**.

```cpp
int arr[5] = {10, 20, 30, 40, 50};

cout << "arr: " << arr << endl;        // Address of first element
cout << "&arr[0]: " << &arr[0] << endl; // Same address
cout << "*arr: " << *arr << endl;       // arr[0] = 10
```

**Key Insight:** `arr[i]` is equivalent to `*(arr + i)`

### 4.2 Pointer Arithmetic

| Operation | Meaning |
|-----------|---------|
| `ptr + 1` | Moves to next element (adds `sizeof(type)` bytes) |
| `ptr - 1` | Moves to previous element |
| `ptr++` / `++ptr` | Increments pointer |
| `ptr--` | Decrements pointer |

```cpp
int arr[] = {10, 20, 30, 40, 50};
int* ptr = arr;  // Points to arr[0]

cout << *ptr << endl;       // 10
ptr++;
cout << *ptr << endl;       // 20
cout << *(ptr + 2) << endl; // 40 (arr[3])
```

### 4.3 Array as Function Parameter

When passing an array to a function, it **decays to a pointer**:

```cpp
void display(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
}

int main() {
    int data[] = {5, 10, 15, 20};
    display(data, 4);  // Output: 5 10 15 20
    return 0;
}
```

---

## 5. Dynamic Arrays

### 5.1 Limitations of Static Arrays

- Size must be known at compile time
- Fixed size cannot be modified during runtime
- May cause memory wastage or insufficient space

### 5.2 Dynamic Memory Allocation Using `new` and `delete`

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;

    // Allocate dynamic array
    int* dynamicArr = new int[n];

    // Input elements
    for (int i = 0; i < n; i++) {
        cin >> dynamicArr[i];
    }

    // Display
    for (int i = 0; i < n; i++) {
        cout << dynamicArr[i] << " ";
    }

    // Deallocate memory
    delete[] dynamicArr;
    dynamicArr = nullptr;

    return 0;
}
```

### 5.3 2D Dynamic Arrays

```cpp
int rows = 3, cols = 4;

// Allocate 2D array
int** matrix = new int*[rows];
for (int i = 0; i < rows; i++) {
    matrix[i] = new int[cols];
}

// Use matrix...
// Deallocate
for (int i = 0; i < rows; i++) {
    delete[] matrix[i];
}
delete[] matrix;
```

### 5.4 Introduction to `std::vector` (Modern C++)

The C++ Standard Library provides `std::vector` for dynamic arrays with automatic memory management:

```cpp
#include <vector>
#include <algorithm>  // for sort

int main() {
    vector<int> vec;           // Empty vector
    vec.push_back(10);
    vec.push_back(30);
    vec.push_back(20);

    // Automatic resizing
    vec[2] = 25;  // Direct access like array

    // Sort
    sort(vec.begin(), vec.end());

    for (int x : vec) {
        cout << x << " ";  // Output: 10 25 30
    }

    return 0;
}
```

---

## 6. Array Operations

### 6.1 Searching

#### Linear Search (O(n))

```cpp
int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key) {
            return i;  // Found at index i
        }
    }
    return -1;  // Not found
}
```

#### Binary Search (O(log n)) — Requires **sorted array**

```cpp
int binarySearch(int arr[], int n, int key) {
    int low = 0, high = n - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (arr[mid] == key)
            return mid;
        else if (arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}
```

### 6.2 Sorting

#### Bubble Sort (O(n²))

```cpp
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
```

#### Selection Sort (O(n²))

```cpp
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx])
                minIdx = j;
        }
        swap(arr[i], arr[minIdx]);
    }
}
```

#### Using `std::sort` (C++ Standard Library) — Recommended

```cpp
#include <algorithm>

int arr[] = {64, 25, 12, 22, 11};
int n = sizeof(arr) / sizeof(arr[0]);

sort(arr, arr + n);  // Sorts in ascending order

// For descending:
sort(arr, arr + n, greater<int>());
```

---

## 7. Expressions in C++

### 7.1 Operators Overview

| Category | Operators | Example |
|----------|-----------|---------|
| Arithmetic | `+`, `-`, `*`, `/`, `%` | `a + b`, `a % b` |
| Relational | `<`, `>`, `<=`, `>=`, `==`, `!=` | `a == b` |
| Logical | `&&`, `\|\|`, `!` | `a && b` |
| Bitwise | `&`, `\|`, `^`, `~`, `<<`, `>>` | `a \| b` |
| Assignment | `=`, `+=`, `-=`, `*=`, `/=`, `%=` | `a += 5` |
| Increment/Decrement | `++`, `--` | `a++`, `--b` |

### 7.2 Operator Precedence and Associativity

**Precedence (Highest to Lowest):**

| Precedence | Operators | Associativity |
|------------|-----------|---------------|
| 1 (Highest) | `()` (parentheses) | Left-to-Right |
| 2 | `!`, `++`, `--` (unary) | Right-to-Left |
| 3 | `*`, `/`, `%` | Left-to-Right |
| 4 | `+`, `-` | Left-to-Right |
| 5 | `<<`, `>>` | Left-to-Right |
| 6 | `<`, `>`, `<=`, `>=` | Left-to-Right |
| 7 | `==`, `!=` | Left-to-Right |
| 8 | `&` (bitwise AND) | Left-to-Right |
| 9 | `^` (bitwise XOR) | Left-to-Right |
| 10 | `\|` (bitwise OR) | Left-to-Right |
| 11 | `&&` | Left-to-Right |
| 12 | `\|\|` | Left-to-Right |
| 13 | `=` (assignment) | Right-to-Left |

**Example Evaluation:**

```cpp
int result = 5 + 3 * 2;  // 5 + 6 = 11 (multiplication has higher precedence)

int x = 10, y = 5;
int result2 = ++x * y--;  // ++x = 11, y-- uses 5, then y becomes 4
// result2 = 11 * 5 = 55

bool a = true, b = false;
bool result3 = a || b && false;  // a || (b && false) = true || false = true
```

### 7.3 Complex Expressions

**Expression with Mixed Operators:**

```cpp
int a = 5, b = 10, c = 15;
int result = (a + b) * c - b / 2 + a % 3;
// Step 1: (5 + 10) = 15
// Step 2: 15 * 15 = 225
// Step 3: 10 / 2 = 5
// Step 4: 225 - 5 = 220
// Step 5: 5 % 3 = 2
// Step 6: 220 + 2 = 222
```

**Bitwise Expression:**

```cpp
int x = 12;  // Binary: 1100
int y = 10;  // Binary: 1010

cout << (x & y) << endl;  // 8  (1000)
cout << (x | y) << endl;  // 14 (1110)
cout << (x ^ y) << endl;  // 6  (0110)
cout << (~x) << endl;     // -13 (two's complement)
```

### 7.4 Side Effects and Evaluation Order

C++ does **not** guarantee evaluation order for function arguments (except certain operators):

```cpp
int i = 1;
int arr[5] = {0, 10, 20, 30, 40};

// Undefined behavior - order of evaluation not specified
arr[i] = i++;  // Could be arr[1] = 1 or arr[1] = 2
```

---

## 8. Arrays as Function Parameters

### 8.1 Passing Arrays to Functions

Three equivalent ways to declare array parameters:

```cpp
void func1(int arr[], int size) { }      // Preferred
void func2(int* arr, int size) { }       // Explicit pointer
void func3(int arr[10], int size) { }     // Size hint (ignored by compiler)
```

### 8.2 Passing Multi-Dimensional Arrays

```cpp
// Must specify column size for 2D arrays
void printMatrix(int arr[][3], int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    int matrix[2][3] = {{1, 2, 3}, {4, 5, 6}};
    printMatrix(matrix, 2, 3);
    return 0;
}
```

### 8.3 Returning Arrays from Functions

Cannot return raw arrays directly. Use **pointers** or **`std::vector`**:

```cpp
// Method 1: Return pointer (caller must manage memory)
int* createArray(int size) {
    int* arr = new int[size];
    for (int i = 0; i < size; i++) {
        arr[i] = i * 10;
    }
    return arr;
}

// Method 2: Return vector (recommended)
#include <vector>
std::vector<int> createVector(int size) {
    std::vector<int> v(size);
    for (int i = 0; i < size; i++) {
        v[i] = i * 10;
    }
    return v;
}
```

---

## Key Takeaways

1. **Arrays** provide contiguous memory storage for elements of the same type, with O(1) random access via indices.

2. **Multi-dimensional arrays** (2D, 3D) use row-major storage in C++, useful for matrices and 3D data.

3. **Array-pointer relationship**: Array name decays to pointer to first element; `arr[i] ≡ *(arr + i)`.

4. **Dynamic arrays** using `new`/`delete` allow runtime size determination; `std::vector` is the modern C++ recommended approach.

5. **Search algorithms**: Linear search O(n) for unsorted data; binary search O(log n) requires sorted data.

6. **Sorting algorithms**: Bubble and Selection sort O(n²); `std::sort` uses efficient O(n log n) algorithms.

7. **Operator precedence** determines expression evaluation order; use parentheses for clarity.

8. **Bitwise operators** manipulate individual bits—essential for low-level programming and optimization.

9. When **passing arrays to functions**, they decay to pointers; array size must be passed separately.

---

## Assessment Questions

### Multiple Choice Questions (MCQs)

**Level 1: Easy**

1. What is the index of the first element in a C++ array?
   - A) 1
   - B) 0
   - C) -1
   - D) Depends on declaration

2. What does `arr` represent when `arr` is an array name?
   - A) The first element
   - B) The address of the first element
   - C) The size of the array
   - D) A pointer to the last element

3. Which operator has the highest precedence?
   - A) `+`
   - B) `*`
   - C) `()`
   - D) `=`

**Level 2: Medium**

4. What is the output?
   ```cpp
   int arr[] = {10, 20, 30};
   int* ptr = arr + 1;
   cout << *ptr;
   ```
   - A) 10
   - B) 20
   - C) 30
   - D) Garbage value

5. For a 3×4 integer array, what is the total memory required (in bytes)?
   - A) 12
   - B) 24
   - C) 48
   - D) 96

6. Which sorting algorithm is NOT O(n²)?
   - A) Bubble Sort
   - B) Selection Sort
   - C) Insertion Sort
   - D) std::sort

7. What does `5 + 3 * 2` evaluate to?
   - A) 16
   - B) 11
   - C) 13
   - D) 6

**Level 3: Hard**

8. What is the output?
   ```cpp
   int x = 5;
   int y = x++ + ++x;
   cout << y;
   ```
   - A) 10
   - B) 11
   - C) 12
   - D) Undefined

9. Given `int arr[3][2] = {{1,2}, {3,4}, {5,6}}`, what is `arr[2][0]`?
   - A) 3
   - B) 4
   - C) 5
   - D) 6

10. Binary search requires which condition?
    - A) Array must be unsorted
    - B) Array must be sorted
    - C) Array must have even number of elements
    - D) Array must be globally sorted in ascending order

### Descriptive Questions

**Level 1: Recall**

1. Explain the difference between static and dynamic arrays with examples.
2. List the operator precedence from highest to lowest for: `*`, `+`, `&&`, `||`, `=`.

**Level 2: Application**

3. Write a C++ program to find the sum of all elements in a 2D array (3×3 matrix).
4. Implement a function that reverses an array in place without using another array.
5. Evaluate the expression: `int a = 10, b = 3; cout << (a % b + a / b);`

**Level 3: Analysis**

6. Compare linear search and binary search in terms of time complexity, prerequisites, and use cases.
7. Analyze why `std::vector` is preferred over raw dynamic arrays in modern C++.
8. Explain the concept of "array decaying to pointer" and its implications when passing arrays to functions.

**Level 4: Synthesis**

9. Design a C++ program that:
   - Creates a dynamic array of integers
   - Sorts it using bubble sort
   - Searches for an element using binary search
   - Handles edge cases (empty array, element not found)

10. Write a function that accepts a 2D array representing a student's marks (5 students, 3 subjects) and calculates the average marks for each student.

---

## Answer Key

**MCQ Answers:**
1. B (0)
2. B (Address of first element)
3. C (())
4. B (20)
5. C (48) — 3×4×4 = 48 bytes
6. D (std::sort)
7. B (11) — 3*2 = 6, then 5+6 = 11
8. C (12) — x++ uses 5 (x becomes 6), ++x uses 7 (x becomes 7), sum = 5+7 = 12
9. C (5)
10. B (Array must be sorted)

---

*This study material covers the complete syllabus for "Arrays And Expressions" under Programming Using C++ for BSc (Hons) Computer Science, Delhi University (NEP 2024 UGCF).*