# Arrays, Decision Making, and Iteration in C++

## Introduction

Programming in C++ requires mastering fundamental control structures that form the backbone of algorithmic thinking. This module covers three essential pillars of C++ programming: arrays for data storage, decision-making statements for conditional execution, and iteration constructs for repetitive tasks. These concepts are not merely academic—they constitute the practical toolkit that every programmer uses daily in solving real-world problems.

Arrays enable storage of multiple related data items under a single variable name, making data management efficient and organized. Decision-making structures like if-else and switch statements allow programs to take different paths based on conditions—a necessity for any program that responds to user input or external data. Iteration statements (loops) empower programmers to process large volumes of data efficiently, from calculating factorials to searching databases. Together, these constructs transform simple instructions into powerful algorithms capable of solving complex computational problems.

For University of Delhi students preparing for practical and theoretical examinations, understanding these constructs deeply is essential. Internal assessment questions frequently test conceptual clarity, while end-semester examinations demand both theoretical understanding and practical implementation skills.

## Key Concepts

### 1. Arrays in C++

An array is a contiguous memory structure that stores multiple elements of the same data type. Unlike primitive variables that hold single values, arrays provide a systematic way to handle collections of related data—be it a list of student marks, temperatures across days, or characters in a string.

**Declaration and Initialization:**

```cpp
// Declaration
int marks[5];          // Array of 5 integers (uninitialized)
float prices[10];     // Array of 10 floating-point numbers
char name[20];        // Array of 20 characters

// Initialization at declaration
int numbers[5] = {10, 20, 30, 40, 50};
int data[] = {1, 2, 3};        // Size automatically inferred as 3
int matrix[3][3];             // 2D array (3x3 matrix)
```

**Array Indexing:**
- Arrays are zero-indexed in C++, meaning the first element is at index 0
- Valid indices range from 0 to (n-1) for an array of size n
- Accessing invalid indices causes undefined behavior (buffer overflow)

**Important Characteristics:**
- Arrays provide O(1) random access to elements
- Array name acts as a pointer to the first element
- Size must be known at compile time (for static arrays)
- Arrays pass to functions as pointers, losing size information

### 2. One-Dimensional Array Operations

Common operations on arrays include:
- **Linear Search:** Sequentially checking each element (O(n) complexity)
- **Finding Maximum/Minimum:** Tracking largest/smallest values during traversal
- **Sum and Average:** Accumulating values and dividing by count
- **Reversing:** Swapping elements from beginning and end

### 3. Two-Dimensional Arrays

Two-dimensional arrays represent matrices or tables:

```cpp
int matrix[3][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};

// Accessing elements
int element = matrix[1][2];  // Returns 7
```

Memory is stored in row-major order (elements of first row, then second row, etc.).

### 4. Decision Making Statements

**if Statement:**
The simplest conditional structure executes code only when a condition is true.

```cpp
if (percentage >= 60) {
    cout << "First Division";
}
```

**if-else Statement:**
Provides alternative execution path when condition is false.

```cpp
if (age >= 18) {
    cout << "Eligible to vote";
} else {
    cout << "Not eligible";
}
```

**else-if Ladder:**
Handles multiple mutually exclusive conditions.

```cpp
if (marks >= 90) {
    grade = 'O';
} else if (marks >= 80) {
    grade = 'A';
} else if (marks >= 70) {
    grade = 'B';
} else if (marks >= 60) {
    grade = 'C';
} else {
    grade = 'F';
}
```

**switch Statement:**
Efficient for menu-driven programs with multiple discrete choices.

```cpp
switch (choice) {
    case 1:
        cout << "You chose Add";
        break;
    case 2:
        cout << "You chose Subtract";
        break;
    case 3:
        cout << "You chose Multiply";
        break;
    default:
        cout << "Invalid choice";
}
```

**Key Points about switch:**
- Expression must evaluate to integral or enumeration type
- break statements prevent fall-through (unless intentional)
- default case is optional but recommended
- Case labels must be constant expressions

### 5. Iteration Statements (Loops)

**for Loop:**
Best used when the number of iterations is known beforehand.

```cpp
// Traditional for loop
for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
}

// Range-based for loop (C++11 onwards)
for (int val : array) {
    cout << val << " ";
}
```

**while Loop:**
Pre-test loop—condition checked before execution; suitable when iterations depend on dynamic conditions.

```cpp
while (n > 0) {
    cout << n << " ";
    n--;
}
```

**do-while Loop:**
Post-test loop—executes at least once regardless of condition.

```cpp
do {
    cout << "Enter positive number: ";
    cin >> num;
} while (num <= 0);
```

### 6. Loop Control Statements

- **break:** Terminates the innermost loop or switch
- **continue:** Skips remaining statements in current iteration, proceeds to next
- **goto:** Unconditionally transfers control (generally discouraged)

```cpp
// Example: Finding first negative number
for (int i = 0; i < n; i++) {
    if (arr[i] < 0) {
        cout << "First negative at index " << i << endl;
        break;  // Exit loop once found
    }
}

// Example: Printing odd numbers only
for (int i = 1; i <= 10; i++) {
    if (i % 2 == 0) {
        continue;  // Skip even numbers
    }
    cout << i << " ";
}
```

### 7. Nested Loops

Loops within loops enable processing of multi-dimensional data and complex patterns.

```cpp
// Printing multiplication table
for (int i = 1; i <= 10; i++) {
    for (int j = 1; j <= 10; j++) {
        cout << i * j << "\t";
    }
    cout << endl;
}

// Matrix addition
for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
        result[i][j] = matrix1[i][j] + matrix2[i][j];
    }
}
```

## Examples

### Example 1: Array Operations - Finding Maximum and Minimum

**Problem:** Write a program to find the largest and smallest element in an array of n integers.

**Solution:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;
    
    int arr[n];
    cout << "Enter " << n << " elements: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    // Initialize with first element
    int max = arr[0];
    int min = arr[0];
    
    // Traverse remaining elements
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
        if (arr[i] < min) {
            min = arr[i];
        }
    }
    
    cout << "Maximum: " << max << endl;
    cout << "Minimum: " << min << endl;
    
    return 0;
}
```

**Step-by-step explanation:**
1. Accept array size and elements from user
2. Initialize max and min with first array element
3. Iterate from index 1 to n-1
4. Compare each element with current max/min
5. Update max/min as necessary
6. Display results

### Example 2: Grade Classification using Decision Making

**Problem:** Write a program to calculate grade based on marks using if-else ladder.

**Solution:**

```cpp
#include <iostream>
using namespace std;

int main() {
    float marks;
    char grade;
    string remarks;
    
    cout << "Enter marks (0-100): ";
    cin >> marks;
    
    if (marks < 0 || marks > 100) {
        cout << "Invalid marks!" << endl;
        return 0;
    }
    
    if (marks >= 90) {
        grade = 'O';
        remarks = "Outstanding";
    } else if (marks >= 80) {
        grade = 'A';
        remarks = "Excellent";
    } else if (marks >= 70) {
        grade = 'B';
        remarks = "Very Good";
    } else if (marks >= 60) {
        grade = 'C';
        remarks = "Good";
    } else if (marks >= 50) {
        grade = 'D';
        remarks = "Pass";
    } else {
        grade = 'F';
        remarks = "Fail - Need Improvement";
    }
    
    cout << "Grade: " << grade << endl;
    cout << "Remarks: " << remarks << endl;
    
    return 0;
}
```

**Key Points:**
- Conditions checked in descending order (highest first)
- Each else-if is mutually exclusive
- Input validation prevents invalid grades

### Example 3: Pattern Printing using Nested Loops

**Problem:** Print the following pattern:
```
*
* *
* * *
* * * *
* * * * *
```

**Solution:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int rows;
    cout << "Enter number of rows: ";
    cin >> rows;
    
    for (int i = 1; i <= rows; i++) {
        // Inner loop for columns
        for (int j = 1; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;  // New line after each row
    }
    
    return 0;
}
```

**Trace:**
- i=1: j runs from 1 to 1 → prints 1 star
- i=2: j runs from 1 to 2 → prints 2 stars
- i=3: j runs from 1 to 3 → prints 3 stars
- Continues until i=rows

### Example 4: Menu-Driven Calculator using switch

**Solution:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int choice;
    double a, b, result;
    
    cout << "===== Calculator =====" << endl;
    cout << "1. Addition" << endl;
    cout << "2. Subtraction" << endl;
    cout << "3. Multiplication" << endl;
    cout << "4. Division" << endl;
    cout << "======================" << endl;
    cout << "Enter your choice (1-4): ";
    cin >> choice;
    
    cout << "Enter two numbers: ";
    cin >> a >> b;
    
    switch (choice) {
        case 1:
            result = a + b;
            cout << "Result: " << result << endl;
            break;
        case 2:
            result = a - b;
            cout << "Result: " << result << endl;
            break;
        case 3:
            result = a * b;
            cout << "Result: " << result << endl;
            break;
        case 4:
            if (b != 0) {
                result = a / b;
                cout << "Result: " << result << endl;
            } else {
                cout << "Error: Division by zero!" << endl;
            }
            break;
        default:
            cout << "Invalid choice!" << endl;
    }
    
    return 0;
}
```

## Exam Tips

1. **Array Indexing:** Remember arrays are zero-indexed. For an array of size n, valid indices are 0 to n-1. Common mistake: using index n (which causes overflow).

2. **Loop Initialization:** Always initialize loop variables. Uninitialized variables lead to garbage values and unpredictable results.

3. **Off-by-One Errors:** Double-check loop conditions. Use `<=` when you need to include the final value, `<` otherwise.

4. **switch Limitations:** Remember switch cannot work with float, double, or string types. Use if-else for such conditions.

5. **break vs continue:** break exits the loop entirely; continue skips only the current iteration.

6. **Infinite Loops:** Ensure loop conditions will eventually become false. Common mistake: forgetting to update loop variable.

7. **Input Validation:** Always validate user inputs, especially for switch choices and array indices.

8. **2D Array Memory:** Remember C++ uses row-major order. Accessing `matrix[i][j]` means element at row i, column j.

9. **Time Complexity:** For practical questions, analyze time complexity. Linear search is O(n), accessing element by index is O(1).

10. **Code Tracing:** Examination questions often ask you to trace code and predict output. Practice by manually executing loops with sample inputs.

11. **Common Errors:** Watch for missing headers, using = instead of == in conditions, and forgetting to include necessary libraries.