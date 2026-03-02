# Linear Search


## Table of Contents

- [Linear Search](#linear-search)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of Linear Search](#definition-of-linear-search)
  - [Algorithm Description](#algorithm-description)
  - [Implementation in C](#implementation-in-c)
  - [Sentinel Linear Search](#sentinel-linear-search)
  - [Time and Space Complexity](#time-and-space-complexity)
  - [Recursive Implementation](#recursive-implementation)
- [Examples](#examples)
  - [Example 1: Searching in an Unsorted Array](#example-1-searching-in-an-unsorted-array)
  - [Example 2: Element Not Present](#example-2-element-not-present)
  - [Example 3: Finding First Occurrence in Duplicate Array](#example-3-finding-first-occurrence-in-duplicate-array)
- [Exam Tips](#exam-tips)

## Introduction

Linear Search, also known as Sequential Search, is one of the most fundamental searching algorithms in computer science. It represents the most straightforward approach to finding a target element within a collection of data: we examine each element one by one, in sequence, until we either find the target or exhaust all available elements. This brute-force methodology, while conceptually simple, forms the bedrock upon which more sophisticated search algorithms are built.

The importance of Linear Search in the context of problem solving using C programming cannot be overstated. For students at the University of Delhi, understanding Linear Search is essential not only because it frequently appears in examination questions but also because it develops the analytical thinking required for algorithm design. In real-world applications, Linear Search remains relevant for small datasets, unsorted data, and situations where the overhead of preprocessing (as required by Binary Search) cannot be justified. When working with linked lists, which are inherently sequential structures, Linear Search is often the only viable search option. Furthermore, the concepts of iteration, condition checking, and index manipulation learned through Linear Search directly apply to numerous other algorithms and programming challenges.

## Key Concepts

### Definition of Linear Search

Linear Search is a searching algorithm that traverses a list or array sequentially, comparing each element with the target value until a match is found or the entire list has been examined. The algorithm returns the index of the first occurrence of the target element if found, or a special value (typically -1 in C programming) to indicate absence.

### Algorithm Description

The Linear Search algorithm follows a systematic approach. Starting from the first element (index 0), the algorithm compares the current element with the target value. If they match, the search terminates successfully, and the current index is returned. If they do not match, the algorithm moves to the next element and repeats the comparison. This process continues until either the element is found or the array bounds are exceeded, in which case the search terminates unsuccessfully.

### Implementation in C

The implementation of Linear Search in C requires understanding of arrays, loops, and conditional statements. Here is the standard implementation:

```c
#include <stdio.h>

int linearSearch(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            return i;  // Element found, return its index
        }
    }
    return -1;  // Element not found
}

int main() {
    int arr[] = {12, 45, 67, 89, 23, 56, 78};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 23;
    
    int result = linearSearch(arr, n, target);
    
    if (result != -1) {
        printf("Element found at index %d\n", result);
    } else {
        printf("Element not found in the array\n");
    }
    
    return 0;
}
```

### Sentinel Linear Search

An optimization to the basic Linear Search involves using a sentinel value. This technique eliminates the need to check array bounds on every iteration by placing the target value at the end of the array. The algorithm thus guarantees finding the element without repeatedly checking the loop termination condition:

```c
int sentinelLinearSearch(int arr[], int n, int target) {
    int last = arr[n - 1];
    arr[n - 1] = target;  // Set sentinel
    
    int i = 0;
    while (arr[i] != target) {
        i++;
    }
    
    arr[n - 1] = last;  // Restore original element
    
    if (i < n - 1 || last == target) {
        return i;
    }
    return -1;
}
```

### Time and Space Complexity

Understanding complexity analysis is crucial for algorithm evaluation. For Linear Search:

**Best Case Complexity**: O(1) — occurs when the target element is found at the first position (index 0).

**Worst Case Complexity**: O(n) — occurs when the target element is at the last position or not present in the array, requiring n comparisons.

**Average Case Complexity**: O(n) — statistically, we expect to examine approximately n/2 elements, which simplifies to O(n) in Big-O notation.

**Space Complexity**: O(1) — Linear Search requires only a constant amount of extra space for variables regardless of input size.

### Recursive Implementation

Linear Search can also be implemented recursively, though the iterative approach is generally preferred due to lower overhead:

```c
int recursiveLinearSearch(int arr[], int n, int target, int index) {
    if (index >= n) {
        return -1;  // Element not found
    }
    if (arr[index] == target) {
        return index;  // Element found
    }
    return recursiveLinearSearch(arr, n, target, index + 1);
}
```

## Examples

### Example 1: Searching in an Unsorted Array

Consider an array of integers representing student roll numbers: {45, 23, 89, 12, 67, 34, 90}. We need to find if roll number 67 exists.

Step-by-step execution:
- Start at index 0: arr[0] = 45, compare with 67 → Not equal, move to next
- Index 1: arr[1] = 23, compare with 67 → Not equal, move to next
- Index 2: arr[2] = 89, compare with 67 → Not equal, move to next
- Index 3: arr[3] = 12, compare with 67 → Not equal, move to next
- Index 4: arr[4] = 67, compare with 67 → Equal! Element found at index 4

The algorithm performs 5 comparisons before finding the element.

### Example 2: Element Not Present

Consider searching for value 100 in array: {5, 10, 15, 20, 25}.

Execution:
- Index 0: 5 ≠ 100, continue
- Index 1: 10 ≠ 100, continue
- Index 2: 15 ≠ 100, continue
- Index 3: 20 ≠ 100, continue
- Index 4: 25 ≠ 100, continue
- Index 5: Bounds exceeded, terminate and return -1

The algorithm makes 5 comparisons before determining the element is absent.

### Example 3: Finding First Occurrence in Duplicate Array

When an array contains duplicate elements, Linear Search returns the index of the first occurrence:

Array: {15, 22, 15, 37, 15, 48}, Target: 15

The search will return index 0 (the first 15), even though the element also appears at indices 2 and 4.

## Exam Tips

For students appearing in DU semester examinations, the following points are essential:

1. **Understand the algorithm step-by-step**: Be prepared to trace through the algorithm manually with a given input array and target value. This is a common examination question.

2. **Complexity analysis is frequently tested**: Remember that Linear Search has O(n) time complexity in all cases except the best case. Clearly distinguish between best, worst, and average cases.

3. **Return value conventions**: In C programming, Linear Search typically returns the index (0 to n-1) on success and -1 on failure. Some implementations may return n or n+1—always clarify in your answer.

4. **Base case in recursion**: When writing recursive Linear Search, ensure you handle the base case (index reaching n) correctly to avoid infinite recursion.

5. **Comparison with Binary Search**: Understand that Binary Search requires sorted data and has O(log n) complexity, while Linear Search works on unsorted data but has O(n) complexity. Know when to apply each.

6. **Sentinel optimization**: The sentinel version reduces one comparison per iteration by eliminating the bounds check, though both versions have O(n) complexity.

7. **Practice dry runs**: Examination questions often ask you to simulate the algorithm. Practice tracing through arrays manually, counting the number of comparisons made.

8. **Code writing accuracy**: When writing C code for Linear Search, ensure correct array indexing, loop boundaries, and return statements. Common errors include off-by-one errors in loop conditions.