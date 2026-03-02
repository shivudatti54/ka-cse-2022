# Binary Search Using Recursion


## Table of Contents

- [Binary Search Using Recursion](#binary-search-using-recursion)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Understanding Binary Search](#understanding-binary-search)
  - [Recursion Fundamentals](#recursion-fundamentals)
  - [Combining Binary Search with Recursion](#combining-binary-search-with-recursion)
  - [Time and Space Complexity](#time-and-space-complexity)
  - [Trace of Recursive Binary Search](#trace-of-recursive-binary-search)
- [Examples](#examples)
  - [Example 1: Basic Recursive Binary Search](#example-1-basic-recursive-binary-search)
  - [Example 2: Finding First Occurrence in Duplicates](#example-2-finding-first-occurrence-in-duplicates)
  - [Example 3: Binary Search with Custom Comparison Function](#example-3-binary-search-with-custom-comparison-function)
- [Exam Tips](#exam-tips)

## Introduction

Binary Search is one of the most fundamental and efficient searching algorithms in computer science, particularly relevant in the context of the University of Delhi's Computer Science curriculum. The algorithm works on the principle of DIVIDE AND CONQUER, repeatedly dividing the sorted array into halves to locate the target element. When combined with recursion—a programming paradigm where a function calls itself to solve smaller instances of the same problem—binary search becomes an elegant demonstration of how recursion can simplify complex algorithmic implementations.

In the context of Problem Solving Using C Programming, understanding binary search using recursion is essential for several reasons. First, it reinforces the concept of recursion, which is a core topic in your Module 3. Second, it demonstrates how recursive functions can replace iterative constructs, providing an alternative approach to problem-solving. Third, binary search has a time complexity of O(log n), making it significantly faster than linear search for large datasets—a critical consideration in real-world applications. For your internal assessment and end semester exams, this topic frequently appears as programming questions, conceptual explanations, and complexity analysis problems.

This article will comprehensively cover the theoretical foundations, implementation details, practical examples, and examination strategies necessary to master binary search using recursion in C programming.

## Key Concepts

### Understanding Binary Search

Binary search is applicable only on sorted arrays (either in ascending or descending order). The algorithm works by comparing the target element with the middle element of the array. If they are equal, the search is successful. If the target is less than the middle element, the search continues in the left half; otherwise, it continues in the right half. This process repeats until the element is found or the subarray becomes empty.

The fundamental steps of binary search are:
1. Determine the middle element of the current search range
2. Compare the middle element with the target value
3. If equal, return the index
4. If target is smaller, search in the left half
5. If target is larger, search in the right half
6. If search range becomes empty, return -1 (not found)

### Recursion Fundamentals

Recursion in C programming occurs when a function calls itself either directly or indirectly. Each recursive call solves a smaller version of the original problem until it reaches a base case—a condition where the problem can be solved directly without further recursion.

A recursive function typically consists of:
- Base Case: The condition that terminates the recursion
- Recursive Case: The part where the function calls itself with modified parameters

For binary search, the base case occurs when the element is found or when the search range becomes empty (low index exceeds high index). The recursive case involves calling the binary search function with updated low and high boundary values.

### Combining Binary Search with Recursion

When implementing binary search using recursion, we pass three parameters to the function: the array, the search key, and two indices defining the search range (typically called low and high). At each recursive call, we calculate the middle index using the formula: mid = (low + high) / 2. We then compare the element at arr[mid] with the key and make a recursive call to either the left half or right half depending on the comparison result.

The recursive binary search function follows this logic:

```c
int binarySearch(int arr[], int low, int high, int key) {
    // Base case: element not found
    if (low > high) {
        return -1;
    }
    
    // Calculate middle index
    int mid = low + (high - low) / 2;
    
    // Element found at mid
    if (arr[mid] == key) {
        return mid;
    }
    
    // Element is in left half
    if (arr[mid] > key) {
        return binarySearch(arr, low, mid - 1, key);
    }
    
    // Element is in right half
    return binarySearch(arr, mid + 1, high, key);
}
```

### Time and Space Complexity

Understanding complexity analysis is crucial for your DU examinations. Binary search using recursion has the following complexity characteristics:

TIME COMPLEXITY: O(log n)
- At each recursive call, the search space is reduced by half
- The recurrence relation is T(n) = T(n/2) + O(1)
- Solving this gives T(n) = O(log n)

SPACE COMPLEXITY: O(log n)
- Due to recursive calls, the call stack uses additional memory
- Each recursive call adds a frame to the stack
- Maximum depth of recursion is O(log n)

### Trace of Recursive Binary Search

Understanding the execution trace helps in debugging and conceptual clarity. Consider searching for element 42 in a sorted array: [10, 20, 30, 40, 42, 50, 60, 70, 80, 90]

Call 1: low=0, high=9, mid=4, arr[4]=42 → FOUND, returns 4
The recursion terminates here as the element is found at mid.

Consider searching for element 25 in the same array:
Call 1: low=0, high=9, mid=4, arr[4]=42 > 25 → search left half
Call 2: low=0, high=3, mid=1, arr[1]=20 < 25 → search right half
Call 3: low=2, high=3, mid=2, arr[2]=30 > 25 → search left half
Call 4: low=2, high=1 → low > high → NOT FOUND, returns -1

## Examples

### Example 1: Basic Recursive Binary Search

Problem: Write a C program to search for element 45 in the array {12, 23, 34, 45, 56, 67, 78} using recursive binary search.

Solution:

```c
#include <stdio.h>

int binarySearch(int arr[], int low, int high, int key) {
    if (low > high) {
        return -1;
    }
    
    int mid = low + (high - low) / 2;
    
    if (arr[mid] == key) {
        return mid;
    }
    else if (arr[mid] > key) {
        return binarySearch(arr, low, mid - 1, key);
    }
    else {
        return binarySearch(arr, mid + 1, high, key);
    }
}

int main() {
    int arr[] = {12, 23, 34, 45, 56, 67, 78};
    int n = sizeof(arr) / sizeof(arr[0]);
    int key = 45;
    
    int result = binarySearch(arr, 0, n - 1, key);
    
    if (result != -1) {
        printf("Element found at index %d\n", result);
    } else {
        printf("Element not found\n");
    }
    
    return 0;
}
```

Output: Element found at index 3

Step-by-step trace:
- Initial call: low=0, high=6, mid=3
- arr[3]=45 equals key → returns 3

### Example 2: Finding First Occurrence in Duplicates

Problem: In a sorted array with duplicate values, modify binary search to find the first occurrence of the key.

Solution:

```c
#include <stdio.h>

int firstOccurrence(int arr[], int low, int high, int key) {
    if (low > high) {
        return -1;
    }
    
    int mid = low + (high - low) / 2;
    
    if (arr[mid] == key) {
        // Check if this is the first occurrence
        if (mid == low || arr[mid - 1] < key) {
            return mid;
        } else {
            // Search in left half for earlier occurrence
            return firstOccurrence(arr, low, mid - 1, key);
        }
    }
    else if (arr[mid] > key) {
        return firstOccurrence(arr, low, mid - 1, key);
    }
    else {
        return firstOccurrence(arr, mid + 1, high, key);
    }
}

int main() {
    int arr[] = {10, 20, 30, 30, 30, 40, 50};
    int n = sizeof(arr) / sizeof(arr[0]);
    int key = 30;
    
    int result = firstOccurrence(arr, 0, n - 1, key);
    
    if (result != -1) {
        printf("First occurrence at index %d\n", result);
    } else {
        printf("Element not found\n");
    }
    
    return 0;
}
```

Output: First occurrence at index 2

### Example 3: Binary Search with Custom Comparison Function

Problem: Search for a string in a sorted array of strings using recursive binary search.

Solution:

```c
#include <stdio.h>
#include <string.h>

int binarySearchStrings(char arr[][20], int low, int high, char key[]) {
    if (low > high) {
        return -1;
    }
    
    int mid = low + (high - low) / 2;
    int cmp = strcmp(arr[mid], key);
    
    if (cmp == 0) {
        return mid;
    }
    else if (cmp > 0) {
        return binarySearchStrings(arr, low, mid - 1, key);
    }
    else {
        return binarySearchStrings(arr, mid + 1, high, key);
    }
}

int main() {
    char arr[][20] = {"apple", "banana", "cherry", "grape", "mango"};
    char key[] = "cherry";
    int n = 5;
    
    int result = binarySearchStrings(arr, 0, n - 1, key);
    
    if (result != -1) {
        printf("String found at index %d\n", result);
    } else {
        printf("String not found\n");
    }
    
    return 0;
}
```

Output: String found at index 2

## Exam Tips

For your DU semester examinations, keep the following points in mind:

1. PREREQUISITE CONDITION: Always remember that binary search requires a SORTED array. Never apply binary search on an unsorted array—this is a common mistake that examiners look for.

2. MIDDLE INDEX CALCULATION: Use mid = low + (high - low) / 2 instead of (low + high) / 2 to prevent INTEGER OVERFLOW in languages where integers have fixed size.

3. BASE CASE: The base case for binary search is typically (low > high) or (low <= high) depending on implementation. Ensure your termination condition is correct to avoid infinite recursion.

4. ITERATIVE VS RECURSIVE: Be prepared to convert between iterative and recursive implementations. The iterative version uses a while loop; the recursive version uses function calls.

5. COMPLEXITY ANALYSIS: Remember that recursive binary search has O(log n) time complexity but O(log n) space complexity due to recursion stack, whereas iterative has O(1) space complexity.

6. HANDLING DUPLICATES: Understand variations like finding first occurrence, last occurrence, and count of occurrences using modified binary search.

7. TRACE EXECUTION: Practice tracing recursive binary search by hand. Examiners frequently ask you to show step-by-step execution for a specific input.

8. RETURN VALUES: Always specify what the function returns—typically the index of the found element or -1 if not found. Some implementations return the position where the element should be inserted.