# Recursive Functions: Linear and Binary Search

## A Comprehensive Study Material for BSc Physical Science (CS) - Delhi University (NEP 2024)

---

## 1. Introduction

### What is Recursion?

Recursion is a fundamental programming paradigm where a function calls itself to solve a problem by breaking it down into smaller, more manageable sub-problems. This powerful technique is essential in computer science and forms the backbone of many algorithms, particularly in searching and sorting operations.

In the context of data structures, recursion allows us to implement elegant solutions to complex problems. Two classic examples are **Linear Search** and **Binary Search** - both can be implemented using recursive approaches, offering different trade-offs in terms of efficiency and application scenarios.

### Real-World Relevance

Recursive search algorithms are everywhere in our digital lives:

- **Database Searching**: When you search for a product on Amazon or a contact in your phone, search algorithms work behind the scenes
- **Version Control Systems**: Git uses binary search-like algorithms to find commits efficiently
- **Spell Checkers**: Dictionary lookups often employ binary search for O(log n) performance
- **Game Development**: Pathfinding algorithms use recursive concepts
- **File Systems**: Operating systems use tree traversal (recursive) to navigate folders
- **AI and Machine Learning**: Decision trees rely on recursive partitioning

Understanding these concepts is crucial for any computer science student, as they form the foundation for more advanced algorithms and data structures.

---

## 2. Understanding Recursion

### Definition

A recursive function is a function that calls itself directly or indirectly. Every recursive solution consists of two essential parts:

1. **Base Case (Termination Condition)**: The condition under which the recursion stops
2. **Recursive Case (Recursive Step)**: The part where the function calls itself with a smaller version of the problem

### How Recursion Works - The Call Stack

When a recursive function is called, the following happens:

1. Each recursive call creates a new **stack frame** in memory
2. The current function's execution is paused and its state is saved
3. The new call executes with updated parameters
4. Upon completion, control returns to the previous call, restoring its state

This mechanism allows recursion to solve complex problems elegantly, but requires careful base case definition to prevent infinite loops.

### Example: Simple Recursion

```c
// C Program: Factorial using Recursion
#include <stdio.h>

int factorial(int n) {
    // Base Case
    if (n == 0 || n == 1) {
        return 1;
    }
    // Recursive Case
    return n * factorial(n - 1);
}

int main() {
    int num = 5;
    printf("Factorial of %d is %d\n", num, factorial(num));
    return 0;
}
```

**Output:**
```
Factorial of 5 is 120
```

### Python Implementation

```python
# Python: Factorial using Recursion
def factorial(n):
    # Base Case
    if n == 0 or n == 1:
        return 1
    # Recursive Case
    return n * factorial(n - 1)

# Test
print(f"Factorial of 5 is {factorial(5)}")  # Output: 120
```

---

## 3. Linear Search (Recursive Implementation)

### What is Linear Search?

Linear Search is the simplest search algorithm that sequentially checks each element in a list until a match is found or the entire list has been searched. While typically implemented iteratively, a recursive approach demonstrates the power of recursion elegantly.

### Algorithm Design

The recursive linear search works as follows:

1. **Base Case 1**: If the index exceeds the array bounds, return "not found" (-1)
2. **Base Case 2**: If the element at current index matches the target, return the index
3. **Recursive Case**: Call the function with the next index position

### C Implementation

```c
// C Program: Recursive Linear Search
#include <stdio.h>

// Function to perform recursive linear search
int linearSearch(int arr[], int key, int index, int size) {
    // Base Case 1: Element not found (reached end of array)
    if (index >= size) {
        return -1;
    }
    
    // Base Case 2: Element found at current index
    if (arr[index] == key) {
        return index;
    }
    
    // Recursive Case: Search in the remaining elements
    return linearSearch(arr, key, index + 1, size);
}

int main() {
    int arr[] = {10, 25, 30, 45, 50, 67, 89};
    int size = sizeof(arr) / sizeof(arr[0]);
    int key = 50;
    
    int result = linearSearch(arr, key, 0, size);
    
    if (result != -1) {
        printf("Element %d found at index %d\n", key, result);
    } else {
        printf("Element %d not found in the array\n", key);
    }
    
    // Test with non-existent element
    key = 100;
    result = linearSearch(arr, key, 0, size);
    if (result != -1) {
        printf("Element %d found at index %d\n", key, result);
    } else {
        printf("Element %d not found in the array\n", key);
    }
    
    return 0;
}
```

**Output:**
```
Element 50 found at index 4
Element 100 not found in the array
```

### Python Implementation

```python
# Python: Recursive Linear Search
def linear_search(arr, key, index=0):
    """
    Recursively search for key in arr starting from index
    
    Parameters:
    arr: List to search in
    key: Element to search for
    index: Current position (default 0)
    
    Returns: Index of key if found, -1 otherwise
    """
    # Base Case 1: Element not found
    if index >= len(arr):
        return -1
    
    # Base Case 2: Element found
    if arr[index] == key:
        return index
    
    # Recursive Case
    return linear_search(arr, key, index + 1)

# Test Cases
if __name__ == "__main__":
    arr = [10, 25, 30, 45, 50, 67, 89]
    
    # Search for existing element
    result = linear_search(arr, 50)
    print(f"Element 50 found at index: {result}")  # Output: 4
    
    # Search for non-existing element
    result = linear_search(arr, 100)
    print(f"Element 100 found at index: {result}")  # Output: -1
    
    # Using list comprehension to find all occurrences
    def linear_search_all(arr, key, index=0, results=None):
        if results is None:
            results = []
        
        if index >= len(arr):
            return results
        
        if arr[index] == key:
            results.append(index)
        
        return linear_search_all(arr, key, index + 1, results)
    
    # Test with duplicates
    arr_with_dups = [5, 10, 5, 15, 5, 20]
    all_indices = linear_search_all(arr_with_dups, 5)
    print(f"Element 5 found at indices: {all_indices}")  # Output: [0, 2, 4]
```

### Complexity Analysis

| Aspect | Complexity |
|--------|------------|
| **Time Complexity** | O(n) - In worst case, we examine all elements |
| **Space Complexity** | O(n) - Due to recursive call stack (n stack frames) |
| **Best Case** | O(1) - Element found at first position |
| **Average Case** | O(n) - Element found at middle on average |

---

## 4. Binary Search (Recursive Implementation)

### What is Binary Search?

Binary Search is a highly efficient searching algorithm that works on **sorted arrays**. It repeatedly divides the search interval in half, comparing the target element with the middle element. This divide-and-conquer approach provides dramatically better performance than linear search.

### Prerequisites

Binary search **requires** the array to be:
- Sorted in ascending or descending order
- Accessible via index-based access

### Algorithm Design

The recursive binary search works as follows:

1. **Base Case 1**: If start index > end index, element not found (return -1)
2. **Base Case 2**: If middle element equals target, return the index
3. **Recursive Case 1**: If target < middle element, search in left half
4. **Recursive Case 2**: If target > middle element, search in right half

### C Implementation

```c
// C Program: Recursive Binary Search
#include <stdio.h>

// Function to perform recursive binary search
int binarySearch(int arr[], int key, int low, int high) {
    // Base Case: Element not found (search space exhausted)
    if (low > high) {
        return -1;
    }
    
    // Calculate middle index to prevent overflow
    int mid = low + (high - low) / 2;
    
    // Base Case: Element found at mid
    if (arr[mid] == key) {
        return mid;
    }
    
    // Recursive Case 1: Search in left half (elements smaller than mid)
    if (key < arr[mid]) {
        return binarySearch(arr, key, low, mid - 1);
    }
    
    // Recursive Case 2: Search in right half (elements greater than mid)
    return binarySearch(arr, key, mid + 1, high);
}

int main() {
    int arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int size = sizeof(arr) / sizeof(arr[0]);
    int key = 23;
    
    int result = binarySearch(arr, key, 0, size - 1);
    
    if (result != -1) {
        printf("Element %d found at index %d\n", key, result);
    } else {
        printf("Element %d not found in the array\n", key);
    }
    
    // Test with non-existent element
    key = 100;
    result = binarySearch(arr, key, 0, size - 1);
    if (result != -1) {
        printf("Element %d found at index %d\n", key, result);
    } else {
        printf("Element %d not found in the array\n", key);
    }
    
    return 0;
}
```

**Output:**
```
Element 23 found at index 5
Element 100 not found in the array
```

### Python Implementation

```python
# Python: Recursive Binary Search
def binary_search(arr, key, low=None, high=None):
    """
    Recursively search for key in a sorted array
    
    Parameters:
    arr: Sorted list to search in
    key: Element to search for
    low: Starting index (default 0)
    high: Ending index (default len(arr) - 1)
    
    Returns: Index of key if found, -1 otherwise
    """
    # Handle initial call
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    
    # Base Case: Element not found
    if low > high:
        return -1
    
    # Calculate middle index (prevents overflow)
    mid = low + (high - low) // 2
    
    # Base Case: Element found
    if arr[mid] == key:
        return mid
    
    # Recursive Case 1: Search left half
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    
    # Recursive Case 2: Search right half
    else:
        return binary_search(arr, key, mid + 1, high)

# Test Cases
if __name__ == "__main__":
    sorted_arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    
    # Search for existing element
    result = binary_search(sorted_arr, 23)
    print(f"Element 23 found at index: {result}")  # Output: 5
    
    # Search for first element
    result = binary_search(sorted_arr, 2)
    print(f"Element 2 found at index: {result}")  # Output: 0
    
    # Search for last element
    result = binary_search(sorted_arr, 91)
    print(f"Element 91 found at index: {result}")  # Output: 9
    
    # Search for non-existing element
    result = binary_search(sorted_arr, 100)
    print(f"Element 100 found at index: {result}")  # Output: -1
```

### Binary Search on Different Data Types

```python
# Binary Search for strings (sorted alphabetically)
def binary_search_strings(arr, key):
    """Search for a string in a sorted array of strings"""
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

# Test
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
result = binary_search_strings(fruits, "cherry")
print(f"'cherry' found at index: {result}")  # Output: 2
```

### Complexity Analysis

| Aspect | Complexity |
|--------|------------|
| **Time Complexity** | O(log n) - Each iteration halves the search space |
| **Space Complexity** | O(log n) - Due to recursive call stack |
| **Best Case** | O(1) - Element found at middle on first check |
| **Space (Iterative)** | O(1) - Can be optimized to constant space |

### Visual Representation of Binary Search

```
Array: [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
Index:  0  1  2   3   4   5    6    7   8   9

Search for: 23

Step 1: low=0, high=9, mid=4
        arr[4]=16 < 23 → Search RIGHT (low=5)
        
Step 2: low=5, high=9, mid=7
        arr[7]=56 > 23 → Search LEFT (high=6)
        
Step 3: low=5, high=6, mid=5
        arr[5]=23 == 23 → FOUND at index 5!

Total iterations: 3 (log₂10 ≈ 3.32)
```

---

## 5. Comparison: Linear Search vs Binary Search

### Key Differences

| Feature | Linear Search | Binary Search |
|---------|---------------|---------------|
| **Data Requirement** | Works on sorted/unsorted arrays | **Requires sorted array** |
| **Time Complexity** | O(n) | O(log n) |
| **Space Complexity** | O(n) (recursive) | O(log n) (recursive) |
| **Implementation** | Simpler | More complex |
| **Best Case** | O(1) | O(1) |
| **Worst Case** | O(n) | O(log n) |
| **Use When** | Small arrays, unsorted data | Large sorted datasets |

### When to Use Which?

**Use Linear Search when:**
- The array is small (less than 50 elements)
- The array is unsorted and sorting is expensive
- You need to find the first occurrence in a sorted array
- Memory is extremely limited

**Use Binary Search when:**
- The array is large (1000+ elements)
- The array is sorted
- Multiple searches will be performed
- Search performance is critical

### Hybrid Approaches

In practice, a combination is often used:

```python
# Hybrid: Start with linear search, switch to binary if needed
def hybrid_search(sorted_arr, key, threshold=10):
    """
    Uses linear search for first 'threshold' elements,
    then switches to binary search
    """
    # Linear search for small section
    for i in range(min(threshold, len(sorted_arr))):
        if sorted_arr[i] == key:
            return i
    
    # Binary search for rest
    if threshold < len(sorted_arr):
        return binary_search(sorted_arr, key, threshold, len(sorted_arr) - 1)
    
    return -1
```

---

## 6. Additional Examples and Applications

### Example 1: Finding First and Last Occurrence

```python
# Find first and last occurrence using recursion
def find_first_occurrence(arr, key, low, high, result=-1):
    """Find first occurrence of key in sorted array"""
    if low > high:
        return result
    
    mid = low + (high - low) // 2
    
    if arr[mid] == key:
        result = mid
        # Continue searching in left half for first occurrence
        return find_first_occurrence(arr, key, low, mid - 1, result)
    elif arr[mid] < key:
        return find_first_occurrence(arr, key, mid + 1, high, result)
    else:
        return find_first_occurrence(arr, key, low, mid - 1, result)

def find_last_occurrence(arr, key, low, high, result=-1):
    """Find last occurrence of key in sorted array"""
    if low > high:
        return result
    
    mid = low + (high - low) // 2
    
    if arr[mid] == key:
        result = mid
        # Continue searching in right half for last occurrence
        return find_last_occurrence(arr, key, mid + 1, high, result)
    elif arr[mid] < key:
        return find_last_occurrence(arr, key, mid + 1, high, result)
    else:
        return find_last_occurrence(arr, key, low, mid - 1, result)

# Test
arr = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8]
key = 4
first = find_first_occurrence(arr, key, 0, len(arr) - 1)
last = find_last_occurrence(arr, key, 0, len(arr) - 1)
print(f"First occurrence: {first}, Last occurrence: {last}")
# Output: First occurrence: 3, Last occurrence: 5
```

### Example 2: Searching in Rotated Array

```python
# Search in a rotated sorted array
def search_rotated(arr, key, low=0, high=None):
    """
    Search in a rotated sorted array using modified binary search
    Array was originally sorted, then rotated at some pivot
    """
    if high is None:
        high = len(arr) - 1
    
    if low > high:
        return -1
    
    mid = low + (high - low) // 2
    
    if arr[mid] == key:
        return mid
    
    # Check which half is sorted
    if arr[low] <= arr[mid]:
        # Left half is sorted
        if arr[low] <= key < arr[mid]:
            return search_rotated(arr, key, low, mid - 1)
        else:
            return search_rotated(arr, key, mid + 1, high)
    else:
        # Right half is sorted
        if arr[mid] < key <= arr[high]:
            return search_rotated(arr, key, mid + 1, high)
        else:
            return search_rotated(arr, key, low, mid - 1)

# Test
rotated = [6, 7, 8, 9, 1, 2, 3, 4, 5]
print(f"Element 3 found at index: {search_rotated(rotated, 3)}")  # Output: 6
print(f"Element 6 found at index: {search_rotated(rotated, 6)}")  # Output: 0
```

---

## 7. Delhi University Syllabus Context

This topic aligns with the **GE4A: Data Structures** paper under the NEP 2024 curriculum for BSc Physical Science (CS). Key areas covered:

- **Unit I**: Basic Data Structures and Abstract Data Types
- **Unit III**: Searching and Sorting Algorithms
- **Practical Component**: Implementation of recursive search algorithms in C/Python

### Expected Learning Outcomes

After studying this chapter, students should be able to:
1. Understand the concept of recursion and its implementation
2. Implement linear search using both iterative and recursive approaches
3. Implement binary search on sorted arrays
4. Analyze time and space complexity of search algorithms
5. Choose appropriate search algorithm based on problem requirements

---

## 8. Multiple Choice Questions (MCQs)

### Question 1
What is the time complexity of recursive binary search?
- (a) O(n)
- (b) O(log n)
- (c) O(n log n)
- (d) O(1)

**Answer: (b) O(log n)**

---

### Question 2
Which of the following is a prerequisite for binary search?
- (a) Array must be unsorted
- (b) Array must be sorted
- (c) Array must have even number of elements
- (d) Array must contain unique elements

**Answer: (b) Array must be sorted**

---

### Question 3
In recursive linear search, what happens if the element is not found?
- (a) Returns 0
- (b) Returns the index of the last element
- (c) Returns -1
- (d) Returns the size of the array

**Answer: (c) Returns -1**

---

### Question 4
What is the space complexity of recursive binary search?
- (a) O(1)
- (b) O(n)
- (c) O(log n)
- (d) O(n log n)

**Answer: (c) O(log n)**

---

### Question 5
Which search algorithm is more efficient for large sorted datasets?
- (a) Linear Search
- (b) Binary Search
- (c) Both have same efficiency
- (d) Depends on the data type

**Answer: (b) Binary Search**

---

### Question 6
What is the maximum number of comparisons needed to find an element in an array of 100 elements using binary search?
- (a) 100
- (b) 50
- (c) 7
- (d) 10

**Answer: (c) 7** (log₂100 ≈ 6.64, so 7 comparisons)

---

### Question 7
What is the base case in recursive binary search?
- (a) When the array is empty
- (b) When low > high
- (c) When mid equals the key
- (d) Both (b) and (c) can be base cases

**Answer: (d) Both (b) and (c) can be base cases**

---

### Question 8
Which implementation of binary search has O(1) space complexity?
- (a) Recursive implementation
- (b) Iterative implementation
- (c) Both have same space complexity
- (d) Neither

**Answer: (b) Iterative implementation**

---

## 9. Flashcards for Quick Review

### Flashcard 1
| Term | Recursion |
|------|-----------|
| **Definition** | A technique where a function calls itself to solve smaller sub-problems |
| **Two Essential Parts** | 1. Base Case (termination) 2. Recursive Case (self-call) |

---

### Flashcard 2
| Term | Linear Search |
|------|---------------|
| **Definition** | Sequential search checking each element until match is found |
| **Time Complexity** | O(n) |
| **Space Complexity** | O(n) for recursive |

---

### Flashcard 3
| Term | Binary Search |
|------|---------------|
| **Definition** | Divide-and-conquer search on sorted arrays by halving search space |
| **Prerequisite** | Sorted array |
| **Time Complexity** | O(log n) |

---

### Flashcard 4
| Term | Base Case |
|------|-----------|
| **Definition** | Condition that stops recursion and returns a value |
| **Importance** | Prevents infinite recursion |

---

### Flashcard 5
| Term | Call Stack |
|------|------------|
| **Definition** | Memory structure that stores function calls and their states |
| **In Recursion** | Each recursive call adds a new frame; frames are popped on return |

---

## 10. Key Takeaways

### Recursion Fundamentals
- Recursion solves problems by breaking them into smaller, similar sub-problems
- Every recursive function needs a **base case** to terminate
- Each recursive call adds a frame to the **call stack**
- Recursive solutions can be converted to iterative ones and vice versa

### Linear Search
- Simple sequential search algorithm
- Works on both sorted and unsorted arrays
- **Time Complexity**: O(n)
- **Space Complexity**: O(n) for recursive implementation
- Suitable for small datasets or unsorted data

### Binary Search
- Efficient divide-and-conquer algorithm
- **Requires sorted array** as prerequisite
- **Time Complexity**: O(log n) - dramatically faster than linear
- **Space Complexity**: O(log n) for recursive, O(1) for iterative
- Each comparison eliminates half of remaining elements
- Ideal for large, sorted datasets

### Practical Applications
- Database indexing and lookups
- Version control systems
- Spell checkers and dictionaries
- Search functionality in applications
- Debugging (binary search for bugs)

### Best Practices
1. Always define a clear base case to prevent infinite recursion
2. Ensure the recursive case moves toward the base case
3. Use binary search for large sorted datasets
4. Consider iterative implementation when stack space is limited
5. Verify array is sorted before applying binary search

### Exam Tips
- Remember: Binary search only works on sorted arrays
- Know the recurrence relation: T(n) = T(n/2) + O(1) for binary search
- Understand how to calculate mid-index without overflow: `mid = low + (high - low) / 2`
- Practice tracing recursive calls to understand algorithm flow

---

## References and Further Reading

1. "Data Structures and Algorithms in C" - M.T. Goodrich
2. "Introduction to Algorithms" - Cormen, Leiserson, Rivest, Stein
3. "Data Structures Through C" - Yashavant Kanetkar
4. Delhi University BSc (Hons) CS Syllabus - NEP 2024

---

*Generated for BSc Physical Science (CS) - Delhi University, NEP 2024*
*Subject: GE4A Data Structures*
*Topic: Recursive Functions - Linear Binary Search*