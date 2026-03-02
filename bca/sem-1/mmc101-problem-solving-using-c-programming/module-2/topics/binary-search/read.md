# Binary Search


## Table of Contents

- [Binary Search](#binary-search)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Prerequisites for Binary Search](#prerequisites-for-binary-search)
  - [The Binary Search Philosophy](#the-binary-search-philosophy)
  - [Two Implementations in C](#two-implementations-in-c)
  - [Time and Space Complexity](#time-and-space-complexity)
  - [Boundary Conditions](#boundary-conditions)
- [Examples](#examples)
  - [Example 1: Searching in an Ascending Array](#example-1-searching-in-an-ascending-array)
  - [Example 2: Element Not Found](#example-2-element-not-found)
  - [Example 3: Practical Application - Student Record Lookup](#example-3-practical-application---student-record-lookup)
- [Exam Tips](#exam-tips)

## Introduction

Binary Search is one of the most fundamental and efficient searching algorithms in computer science. Unlike linear search, which examines each element sequentially until the target is found, binary search dramatically reduces the search space by repeatedly dividing the search interval in half. This divide-and-conquer approach makes binary search exceptionally fast, with a time complexity of O(log n), making it indispensable for handling large datasets.

The algorithm works only on sorted arrays, which is a critical prerequisite that students must understand. In the context of C programming, binary search demonstrates how to manipulate arrays efficiently and implement recursive functions effectively. This algorithm forms the backbone of many real-world applications including database indexing, dictionary lookups, and debug logging systems. For University of Delhi examinations, binary search is frequently tested through code implementation, time complexity analysis, and comparative questions with linear search.

Understanding binary search is essential not only for academic success but also for technical interviews and competitive programming. The algorithm exemplifies how mathematical insight can transform an O(n) problem into an O(log n) solution—a concept that appears repeatedly in algorithm design.

## Key Concepts

### Prerequisites for Binary Search

Binary search requires a SORTED array as input. The sorting can be in ascending or descending order, though ascending order is the conventional approach in most implementations. If the array is unsorted, binary search will produce incorrect results. This requirement distinguishes binary search from linear search and necessitates preprocessing steps when dealing with unsorted data.

### The Binary Search Philosophy

The algorithm operates on the principle of eliminating half of the remaining elements in each iteration. At each step, we compare the target element with the middle element of the current search range:

1. If the middle element equals the target, the search is successful.
2. If the target is less than the middle element, we search only the left half.
3. If the target is greater than the middle element, we search only the right half.

This process continues until the element is found or the search range becomes empty (element not found).

### Two Implementations in C

Binary search can be implemented using two approaches: iterative and recursive. Both implementations have the same time complexity but differ in space complexity and code structure.

**Iterative Implementation:**

The iterative approach uses a while loop to continuously narrow down the search range using two pointers, typically called 'low' and 'high'. The middle index is calculated using the formula: mid = low + (high - low) / 2. The formula (low + high) / 2 can cause integer overflow in some languages, though C handles large integers reasonably well.

```c
#include <stdio.h>

int binarySearch(int arr[], int size, int target) {
    int low = 0;
    int high = size - 1;
    
    while (low <= high) {
        int mid = low + (high - low) / 2;
        
        if (arr[mid] == target) {
            return mid;  // Element found at index mid
        }
        else if (arr[mid] < target) {
            low = mid + 1;  // Search right half
        }
        else {
            high = mid - 1;  // Search left half
        }
    }
    
    return -1;  // Element not found
}

int main() {
    int arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int size = sizeof(arr) / sizeof(arr[0]);
    int target = 23;
    
    int result = binarySearch(arr, size, target);
    
    if (result != -1) {
        printf("Element found at index %d\n", result);
    } else {
        printf("Element not found in the array\n");
    }
    
    return 0;
}
```

**Recursive Implementation:**

The recursive approach expresses binary search as a function that calls itself with updated search boundaries. This method is conceptually elegant but uses additional stack space.

```c
#include <stdio.h>

int binarySearchRecursive(int arr[], int low, int high, int target) {
    if (low > high) {
        return -1;  // Base case: element not found
    }
    
    int mid = low + (high - low) / 2;
    
    if (arr[mid] == target) {
        return mid;  // Element found
    }
    else if (arr[mid] < target) {
        return binarySearchRecursive(arr, mid + 1, high, target);  // Right half
    }
    else {
        return binarySearchRecursive(arr, low, mid - 1, target);  // Left half
    }
}

int main() {
    int arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int size = sizeof(arr) / sizeof(arr[0]);
    int target = 56;
    
    int result = binarySearchRecursive(arr, 0, size - 1, target);
    
    if (result != -1) {
        printf("Element found at index %d\n", result);
    } else {
        printf("Element not found\n");
    }
    
    return 0;
}
```

### Time and Space Complexity

**Time Complexity:**

The time complexity of binary search is O(log n) base 2. This logarithmic behavior occurs because each comparison eliminates approximately half of the remaining elements. For an array of n elements, the maximum number of comparisons is log₂(n) + 1. In Big O notation, this simplifies to O(log n).

To understand this better: if we have 1000 elements, linear search might require up to 1000 comparisons in the worst case. Binary search requires at most log₂(1000) ≈ 10 comparisons. For 1 million elements, binary search needs only about 20 comparisons compared to 1 million for linear search.

**Space Complexity:**

- Iterative implementation: O(1) - constant extra space
- Recursive implementation: O(log n) - due to recursive call stack

### Boundary Conditions

Several boundary conditions must be handled carefully:

1. **Empty array:** size = 0, should return -1
2. **Single element array:** size = 1, check if it matches
3. **Element at first position:** arr[0] = target
4. **Element at last position:** arr[n-1] = target
5. **Element not present:** search exhausts all possibilities

The condition `while (low <= high)` is crucial. Using `<` instead of `<=` would miss elements at boundary positions.

## Examples

### Example 1: Searching in an Ascending Array

Consider the sorted array: [3, 7, 15, 28, 31, 42, 56, 69, 81]

Search for target = 42.

**Step-by-step execution:**

- Initial: low = 0, high = 8
- Iteration 1: mid = (0 + 8) / 2 = 4
  - arr[4] = 31 < 42, so low = 4 + 1 = 5
- Iteration 2: low = 5, high = 8, mid = (5 + 8) / 2 = 6
  - arr[6] = 56 > 42, so high = 6 - 1 = 5
- Iteration 3: low = 5, high = 5, mid = (5 + 5) / 2 = 5
  - arr[5] = 42 == 42, found!

Number of comparisons: 3
Worst case would have been log₂(9) + 1 ≈ 4 comparisons.

### Example 2: Element Not Found

Consider the sorted array: [5, 12, 18, 24, 30, 37, 45, 52]

Search for target = 20.

**Step-by-step execution:**

- Initial: low = 0, high = 7
- Iteration 1: mid = (0 + 7) / 2 = 3
  - arr[3] = 24 > 20, so high = 3 - 1 = 2
- Iteration 2: low = 0, high = 2, mid = (0 + 2) / 2 = 1
  - arr[1] = 12 < 20, so low = 1 + 1 = 2
- Iteration 3: low = 2, high = 2, mid = (0 + 2) / 2 = 1 (recalculated since low changed)
  - Actually recalculate: mid = (2 + 2) / 2 = 2
  - arr[2] = 18 < 20, so low = 2 + 1 = 3
- Iteration 4: low = 3, high = 2 (low > high)
  - Exit loop, return -1

Element 20 not found in the array.

### Example 3: Practical Application - Student Record Lookup

In a college database system, student roll numbers are stored in sorted order. Binary search can quickly locate a student's record.

```c
#include <stdio.h>

typedef struct {
    int rollNo;
    char name[50];
    float marks;
} Student;

int binarySearchStudent(Student students[], int size, int rollNo) {
    int low = 0;
    int high = size - 1;
    
    while (low <= high) {
        int mid = low + (high - low) / 2;
        
        if (students[mid].rollNo == rollNo) {
            return mid;
        }
        else if (students[mid].rollNo < rollNo) {
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }
    
    return -1;
}

int main() {
    Student students[] = {
        {101, "Amit", 85.5},
        {103, "Bina", 92.0},
        {107, "Charan", 78.5},
        {110, "Divya", 88.0},
        {115, "Eshan", 95.5}
    };
    int size = sizeof(students) / sizeof(students[0]);
    int searchRoll = 107;
    
    int index = binarySearchStudent(students, size, searchRoll);
    
    if (index != -1) {
        printf("Student Found: %s with marks %.2f\n", 
               students[index].name, students[index].marks);
    } else {
        printf("Student with roll number %d not found\n", searchRoll);
    }
    
    return 0;
}
```

## Exam Tips

1. **Always verify array is sorted:** Before applying binary search, state that the prerequisite is a sorted array. This is a common viva voce question.

2. **Choose the right loop condition:** Remember to use `<=` (less than or equal to) in the while condition, not `<`. Using `<` will fail for elements at boundary positions.

3. **Mid-point calculation:** Use `mid = low + (high - low) / 2` instead of `mid = (low + high) / 2` to prevent potential integer overflow in some implementations.

4. **Return value convention:** In C, typically return the index if found, or -1 if not found. Know this convention for implementing functions.

5. **Complexity comparison:** Be prepared to compare binary search O(log n) with linear search O(n). For n = 1000, binary search needs ~10 comparisons vs 1000 for linear search.

6. **Recursive vs Iterative:** Iterative uses O(1) space while recursive uses O(log n) space. For array searches, iterative is generally preferred in practice.

7. **Worst case vs Best case:** Worst case is O(log n) when element is not found or is at the last position checked. Best case is O(1) when element is at the middle position.

8. **Practice dry runs:** Be able to manually trace through binary search for a given array and target. This is frequently asked in written examinations.