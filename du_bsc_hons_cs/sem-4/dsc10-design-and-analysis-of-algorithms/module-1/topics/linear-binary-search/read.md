# Linear Binary Search: A Comprehensive Study Material

## Design and Analysis of Algorithms (DAA)

---

## Table of Contents

1. [Introduction to Binary Search](#1-introduction-to-binary-search)
2. [Real-World Relevance](#2-real-world-relevance)
3. [Prerequisites and Basic Concepts](#3-prerequisites-and-basic-concepts)
4. [How Binary Search Works](#4-how-binary-search-works)
5. [Algorithm Pseudocode](#5-algorithm-pseudocode)
6. [Code Implementations](#6-code-implementations)
7. [Time and Space Complexity Analysis](#7-time-and-space-complexity-analysis)
8. [Binary Search Variants](#8-binary-search-variants)
9. [Edge Cases and Common Pitfalls](#9-edge-cases-and-common-pitfalls)
10. [Practical Examples and Applications](#10-practical-examples-and-applications)
11. [Multiple Choice Questions (MCQs)](#11-multiple-choice-questions-mcqs)
12. [Flashcards for Quick Revision](#12-flashcards-for-quick-revision)
13. [Key Takeaways](#13-key-takeaways)
14. [Delhi University Syllabus Reference](#14-delhi-university-syllabus-reference)

---

## 1. Introduction to Binary Search

Binary Search is one of the most fundamental and efficient searching algorithms in computer science. It is a **divide-and-conquer** algorithm that works on **sorted arrays** (or sorted collections) by repeatedly dividing the search interval in half.

The key insight behind binary search is this: if we know the array is sorted, we can eliminate half of the remaining elements in each iteration. This makes binary search incredibly efficient compared to linear search, especially for large datasets.

**Note on Terminology**: The term "Linear Binary Search" is a misnomer in algorithmic terminology. **Linear Search** and **Binary Search** are two distinct algorithms:
- **Linear Search**: O(n) time complexity, checks elements one by one
- **Binary Search**: O(log n) time complexity, divides search space in half each step

This study material focuses exclusively on **Binary Search** as specified in the Delhi University syllabus.

---

## 2. Real-World Relevance

Binary search has numerous practical applications in the real world:

### 2.1 Database Systems
- Indexing and searching records in sorted databases
- B-tree and B+ tree implementations use binary search principles

### 2.2 Programming Tools
- IDEs use binary search for "Go to Line" functionality
- Version control systems (like Git) use binary search for bug localization

### 2.3 Everyday Applications
- **Dictionary lookup**: Finding a word in a physical dictionary
- **Phone book searches**: Finding a contact in a sorted list
- **ISBN lookup**: Finding books in library catalogs

### 2.4 Technical Interviews
- Binary search is a **frequently asked topic** in technical interviews at top companies like Google, Microsoft, Amazon, and Flipkart

---

## 3. Prerequisites and Basic Concepts

Before understanding binary search, you must understand:

### 3.1 Sorted Array Requirement
Binary search **only works on sorted arrays**. If the array is unsorted, you must first sort it (using algorithms like Merge Sort, Quick Sort, etc.).

### 3.2 Key Terminology
- **Search Space**: The portion of the array currently being searched
- **Middle Element**: The element at the midpoint of the current search space
- **Lower Bound (left)**: The starting index of the search space
- **Upper Bound (right)**: The ending index of the search space

---

## 4. How Binary Search Works

The binary search algorithm follows these steps:

### 4.1 Step-by-Step Process

1. **Initialize**: Set `left = 0` and `right = n-1` (where n is array length)

2. **Find Middle**: Calculate `mid = left + (right - left) / 2` (to avoid integer overflow)

3. **Compare**:
   - If `arr[mid] == target`: Element found! Return `mid`
   - If `arr[mid] < target`: Target is in the **right half**, set `left = mid + 1`
   - If `arr[mid] > target`: Target is in the **left half**, set `right = mid - 1`

4. **Repeat**: Continue until `left > right`

5. **Not Found**: If the loop ends without finding the target, return -1 (or appropriate indicator)

### 4.2 Visual Example

Consider searching for `target = 15` in the sorted array:

```
Index:    0   1   2   3   4   5   6   7   8   9   10
Array:   [2,  5,  8,  10, 12, 15, 18, 20, 25, 30, 35]
                                  ↑
                                Target

Iteration 1:
  left = 0, right = 10, mid = 5
  arr[5] = 15 == target → FOUND at index 5!

Total comparisons: 1
```

Consider searching for `target = 25`:

```
Array:   [2,  5,  8,  10, 12, 15, 18, 20, 25, 30, 35]
          0   1   2   3   4   5   6   7   8   9   10

Iteration 1:
  left = 0, right = 10, mid = 5
  arr[5] = 15 < 25 → search right half
  left = 6

Iteration 2:
  left = 6, right = 10, mid = 8
  arr[8] = 25 == target → FOUND at index 8!

Total comparisons: 2
```

---

## 5. Algorithm Pseudocode

### 5.1 Iterative Binary Search

```
BinarySearch(arr, target):
    left = 0
    right = length(arr) - 1
    
    while left <= right:
        mid = left + (right - left) / 2
        
        if arr[mid] == target:
            return mid        // Element found
        
        else if arr[mid] < target:
            left = mid + 1    // Search right half
        
        else:
            right = mid - 1   // Search left half
    
    return -1                 // Element not found
```

### 5.2 Recursive Binary Search

```
BinarySearchRecursive(arr, target, left, right):
    if left > right:
        return -1             // Base case: not found
    
    mid = left + (right - left) / 2
    
    if arr[mid] == target:
        return mid            // Element found
    
    else if arr[mid] < target:
        return BinarySearchRecursive(arr, target, mid + 1, right)
    
    else:
        return BinarySearchRecursive(arr, target, left, mid - 1)
```

---

## 6. Code Implementations

### 6.1 C Implementation (Iterative)

```c
#include <stdio.h>

// Iterative Binary Search in C
int binarySearch(int arr[], int n, int target) {
    int left = 0;
    int right = n - 1;
    
    while (left <= right) {
        // Calculate mid to avoid integer overflow
        int mid = left + (right - left) / 2;
        
        // Check if target is present at mid
        if (arr[mid] == target) {
            return mid;  // Element found, return index
        }
        
        // If target greater, ignore left half
        if (arr[mid] < target) {
            left = mid + 1;
        }
        // If target smaller, ignore right half
        else {
            right = mid - 1;
        }
    }
    
    // Element not found
    return -1;
}

int main() {
    int arr[] = {2, 5, 8, 10, 12, 15, 18, 20, 25, 30, 35};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 25;
    
    int result = binarySearch(arr, n, target);
    
    if (result != -1) {
        printf("Element found at index %d\n", result);
    } else {
        printf("Element not found in the array\n");
    }
    
    return 0;
}
```

**Output:**
```
Element found at index 8
```

### 6.2 Python Implementation (Recursive)

```python
# Recursive Binary Search in Python
def binary_search_recursive(arr, target, left, right):
    """
    Recursive binary search implementation
    
    Args:
        arr: Sorted array of elements
        target: Element to search for
        left: Left boundary of search space
        right: Right boundary of search space
    
    Returns:
        Index of target if found, -1 otherwise
    """
    # Base case: search space is empty
    if left > right:
        return -1
    
    # Calculate middle index (avoids overflow)
    mid = left + (right - left) // 2
    
    # Check if target is at mid
    if arr[mid] == target:
        return mid
    
    # If target is greater, search right half
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    
    # If target is smaller, search left half
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def binary_search(arr, target):
    """Wrapper function for recursive binary search"""
    return binary_search_recursive(arr, target, 0, len(arr) - 1)


# Example usage
if __name__ == "__main__":
    arr = [2, 5, 8, 10, 12, 15, 18, 20, 25, 30, 35]
    target = 15
    
    result = binary_search(arr, target)
    
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")
```

**Output:**
```
Element found at index 5
```

### 6.3 Java Implementation (Iterative)

```java
public class BinarySearch {
    
    public static int binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
        
        while (left <= right) {
            // Calculate mid to prevent integer overflow
            int mid = left + (right - left) / 2;
            
            if (arr[mid] == target) {
                return mid;  // Found
            } else if (arr[mid] < target) {
                left = mid + 1;  // Search right half
            } else {
                right = mid - 1; // Search left half
            }
        }
        
        return -1;  // Not found
    }
    
    public static void main(String[] args) {
        int[] arr = {2, 5, 8, 10, 12, 15, 18, 20, 25, 30, 35};
        int target = 20;
        
        int result = binarySearch(arr, target);
        
        if (result != -1) {
            System.out.println("Element found at index: " + result);
        } else {
            System.out.println("Element not found");
        }
    }
}
```

---

## 7. Time and Space Complexity Analysis

### 7.1 Time Complexity

| Case | Complexity | Explanation |
|------|------------|-------------|
| **Best Case** | O(1) | Target found at middle index in first comparison |
| **Average Case** | O(log n) | Each iteration halves the search space |
| **Worst Case** | O(log n) | Target is at either end or not present |

**Derivation**: If we have n elements, after k iterations, the remaining search space is n/2^k. The search ends when n/2^k = 1, so k = log₂(n.

### 7.2 Space Complexity

| Implementation | Space Complexity | Reason |
|----------------|------------------|--------|
| **Iterative** | O(1) | Only uses a few variables |
| **Recursive** | O(log n) | Recursive call stack (depth of recursion) |

### 7.3 Comparison with Linear Search

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| **Linear Search** | O(1) | O(n) | O(n) | O(1) |
| **Binary Search** | O(1) | O(log n) | O(log n) | O(1) / O(log n) |

For n = 1,000,000 elements:
- Linear Search: Up to 1,000,000 comparisons
- Binary Search: Maximum 20 comparisons!

---

## 8. Binary Search Variants

### 8.1 Find First Occurrence of Target

When duplicates exist, we often need to find the **first occurrence** of the target element.

```c
int findFirstOccurrence(int arr[], int n, int target) {
    int left = 0, right = n - 1;
    int result = -1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            result = mid;      // Store the index
            right = mid - 1;   // Continue searching left
        }
        else if (arr[mid] < target) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    
    return result;
}
```

**Example:**
```
Array: [2, 4, 4, 4, 7, 9, 9, 11]
Target: 4
First Occurrence: Index 1
```

### 8.2 Find Last Occurrence of Target

```c
int findLastOccurrence(int arr[], int n, int target) {
    int left = 0, right = n - 1;
    int result = -1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            result = mid;      // Store the index
            left = mid + 1;   // Continue searching right
        }
        else if (arr[mid] < target) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    
    return result;
}
```

**Example:**
```
Array: [2, 4, 4, 4, 7, 9, 9, 11]
Target: 4
Last Occurrence: Index 3
```

### 8.3 Count of Occurrences

```
count = lastOccurrence - firstOccurrence + 1
```

### 8.4 Lower Bound (First Element ≥ Target)

```c
int lowerBound(int arr[], int n, int target) {
    int left = 0, right = n;
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    
    return left;
}
```

### 8.5 Upper Bound (First Element > Target)

```c
int upperBound(int arr[], int n, int target) {
    int left = 0, right = n;
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    
    return left;
}
```

---

## 9. Edge Cases and Common Pitfalls

### 9.1 Critical Edge Cases to Handle

1. **Empty Array**: `arr == null` or `n == 0`
2. **Single Element Array**: Direct comparison
3. **Target Not Present**: Must return -1
4. **Target at Boundaries**: First or last element
5. **All Elements Same**: Find first/last occurrence
6. **Duplicate Elements**: Handle first/last occurrence

### 9.2 Common Pitfalls

#### Pitfall 1: Integer Overflow
**Wrong:**
```c
int mid = (left + right) / 2;  // Can overflow if left + right > INT_MAX
```

**Correct:**
```c
int mid = left + (right - left) / 2;  // Safe from overflow
```

#### Pitfall 2: Wrong Loop Condition
**Wrong:**
```c
while (left < right)  // Misses elements when left == right
```

**Correct:**
```c
while (left <= right)  // Includes all elements
```

#### Pitfall 3: Incorrect Boundary Update
**Wrong:**
```c
left = mid;    // Can cause infinite loop
right = mid;   // Can cause infinite loop
```

**Correct:**
```c
left = mid + 1;   // Exclude mid from search
right = mid - 1;  // Exclude mid from search
```

#### Pitfall 4: Unsorted Data
Binary search **will not work** on unsorted arrays. Always ensure data is sorted before applying binary search.

### 9.3 Testing Your Implementation

Test with these cases:
- Empty array
- Single element (found/not found)
- Target at first position
- Target at last position
- Target in middle
- Target not present
- All same elements
- Duplicate elements

---

## 10. Practical Examples and Applications

### 10.1 Example 1: Finding Square Root

```c
// Find square root of a number using binary search
// Returns floor of square root

long long findSquareRoot(long long n) {
    if (n == 0 || n == 1)
        return n;
    
    long long left = 1, right = n, result = 0;
    
    while (left <= right) {
        long long mid = left + (right - left) / 2;
        
        // If mid*mid is equal to n, return mid
        if (mid * mid == n)
            return mid;
        
        // If mid*mid < n, store mid and search in right half
        if (mid * mid < n) {
            result = mid;    // Store candidate
            left = mid + 1;
        }
        // If mid*mid > n, search in left half
        else {
            right = mid - 1;
        }
    }
    
    return result;  // Floor of square root
}
```

**Example:** `n = 16` → Returns `4`  
**Example:** `n = 15` → Returns `3`

### 10.2 Example 2: Searching in Rotated Array

```c
// Search in a rotated sorted array
// Array was sorted, then rotated at some pivot

int searchInRotatedArray(int arr[], int n, int target) {
    int left = 0, right = n - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target)
            return mid;
        
        // Check if left half is sorted
        if (arr[left] <= arr[mid]) {
            if (target >= arr[left] && target < arr[mid])
                right = mid - 1;
            else
                left = mid + 1;
        }
        // Right half is sorted
        else {
            if (target > arr[mid] && target <= arr[right])
                left = mid + 1;
            else
                right = mid - 1;
        }
    }
    
    return -1;
}
```

**Example:**
```
Array: [15, 18, 2, 5, 6, 8, 11]
Target: 5
Result: Index 3
```

### 10.3 Example 3: Binary Search in Competitive Programming

```python
# Finding the position to insert in a sorted list
# (Python's bisect module concept)

def binary_insert_position(arr, target):
    """
    Find the position where target should be inserted
    to maintain sorted order
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left


# Example
arr = [1, 3, 5, 7]
target = 4
print(binary_insert_position(arr, target))  # Output: 2
# arr becomes [1, 3, 4, 5, 7]
```

---

## 11. Multiple Choice Questions (MCQs)

### Easy Level

**Q1. What is the time complexity of binary search?**
- A) O(n)
- B) O(n²)
- C) O(log n)
- D) O(n log n)

**Answer: C) O(log n)**

---

**Q2. Binary search works on which type of data structure?**
- A) Unsorted array
- B) Sorted array
- C) Linked list
- D) Binary tree

**Answer: B) Sorted array**

---

**Q3. In binary search, what is the maximum number of comparisons needed for an array of 100 elements?**
- A) 10
- B) 7
- C) 50
- D) 100

**Answer: B) 7** (log₂100 ≈ 6.64, round up to 7)

---

### Medium Level

**Q4. What is the space complexity of iterative binary search?**
- A) O(n)
- B) O(log n)
- C) O(1)
- D) O(n log n)

**Answer: C) O(1)**

---

**Q5. Which of the following is TRUE about binary search?**
- A) It works on linked lists
- B) It requires random access to elements
- C) It always returns the first occurrence
- D) It cannot be implemented recursively

**Answer: B) It requires random access to elements**

---

**Q6. In binary search, if the target element is greater than the middle element, which half do we search?**
- A) Left half
- B) Right half
- C) Both halves
- D) Neither half

**Answer: B) Right half**

---

**Q7. What is the best-case time complexity of binary search?**
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n log n)

**Answer: A) O(1)** (when target is at middle position)

---

### Difficult Level

**Q8. To avoid integer overflow in calculating mid index, which formula should be used?**
- A) `mid = (left + right) / 2`
- B) `mid = left + (right - left) / 2`
- C) `mid = right - (right - left) / 2`
- D) `mid = (left * right) / 2`

**Answer: B) `mid = left + (right - left) / 2`**

---

**Q9. What is the output of binary search if the element is not found?**
- A) 0
- B) -1
- C) null
- D) Infinity

**Answer: B) -1** (or appropriate "not found" indicator)

---

**Q10. How many iterations are needed to find an element in an array of 1024 elements using binary search?**
- A) 1024
- B) 512
- C) 10
- D) 11

**Answer: C) 10** (log₂1024 = 10)

---

**Q11. In a sorted array with duplicates [2, 4, 4, 4, 7], what does lower_bound(4) return?**
- A) 1
- B) 2
- C) 3
- D) 4

**Answer: A) 1** (first index where arr[i] >= 4)

---

**Q12. Which variant of binary search finds the last occurrence of a duplicate element?**
- A) Continue searching left after finding a match
- B) Continue searching right after finding a match
- C) Stop immediately when found
- D) Use linear search

**Answer: B) Continue searching right after finding a match**

---

## 12. Flashcards for Quick Revision

| # | Concept | Answer |
|---|---------|--------|
| 1 | Time Complexity (Worst Case) | **O(log n)** |
| 2 | Space Complexity (Iterative) | **O(1)** |
| 3 | Space Complexity (Recursive) | **O(log n)** |
| 4 | Prerequisite for Binary Search | **Sorted Array** |
| 5 | Best Case Time Complexity | **O(1)** |
| 6 | How to avoid integer overflow | **mid = left + (right - left) / 2** |
| 7 | Loop condition | **left <= right** |
| 8 | Search right half when | **arr[mid] < target** |
| 9 | Search left half when | **arr[mid] > target** |
| 10 | Maximum comparisons for n=1000 | **10** (log₂1000 ≈ 9.97) |
| 11 | Algorithm Type | **Divide and Conquer** |
| 12 | Found element return | **mid (index)** |
| 13 | Not found return | **-1** |
| 14 | Find first occurrence | **Continue left after match** |
| 15 | Find last occurrence | **Continue right after match** |
| 16 | Why is it called "Binary"? | **Divides into 2 parts each step** |
| 17 | Alternative name | **Half-interval search** |
| 18 | Lower bound definition | **First index where arr[i] >= target** |
| 19 | Upper bound definition | **First index where arr[i] > target** |
| 20 | Number of elements checked in log n | **log₂n** |

---

## 13. Key Takeaways

### Core Concepts
1. **Binary Search** is a divide-and-conquer algorithm requiring a **sorted array**
2. **Time Complexity**: O(log n) - extremely efficient for large datasets
3. **Space Complexity**: O(1) for iterative, O(log n) for recursive implementation

### Implementation Highlights
4. Always use **`left + (right - left) / 2`** to avoid integer overflow
5. Use **iterative approach** for better space efficiency
6. Handle **edge cases**: empty array, single element, boundary elements

### Important Variants
7. **First/Last Occurrence**: Continue searching in appropriate direction after finding a match
8. **Lower/Upper Bound**: Find insertion positions for elements
9. **Rotated Array Search**: Modified binary search handling rotation

### Practical Applications
10. Used in **databases**, **version control** (git bisect), **dictionary lookups**
11. Foundation for **B-trees** and **balanced search trees**
12. Essential topic for **technical interviews**

### Common Mistakes to Avoid
13. ❌ Don't use binary search on unsorted data
14. ❌ Don't use `left + right` (overflow risk)
15. ❌ Don't use `left < right` (misses single element)

---

## 14. Delhi University Syllabus Reference

This content aligns with the **NEP 2024 UGCF** syllabus for **BSc (Hons) Computer Science** at Delhi University, specifically covering:

- **Unit I: Searching and Sorting**
  - Binary Search algorithm and its analysis
  - Variants of binary search
  - Time and space complexity

- **Learning Outcomes**:
  - Understanding of divide-and-conquer approach
  - Ability to implement binary search in multiple programming languages
  - Knowledge of algorithmic complexity analysis

- **Suggested Practical Lab Exercises**:
  - Implement iterative and recursive binary search
  - Find first and last occurrence of elements
  - Solve problems like searching in rotated arrays

---

*End of Study Material*

**Author Note**: This comprehensive study material covers all aspects of Binary Search as required for the Delhi University BSc (Hons) Computer Science curriculum under NEP 2024 UGCF. The content includes theoretical concepts, code implementations, complexity analysis, variants, edge cases, practical examples, MCQs at varying difficulty levels, and flashcards for quick revision.