# Searching and Sorting Algorithms

## Comprehensive Study Material for GE7A: Design and Analysis of Algorithms

---

## Table of Contents

1. [Introduction and Real-World Relevance](#introduction-and-real-world-relevance)
2. [Searching Algorithms](#searching-algorithms)
   - Linear Search
   - Binary Search
3. [Sorting Algorithms](#sorting-algorithms)
   - Bubble Sort
   - Selection Sort
   - Insertion Sort
   - Merge Sort
   - Quick Sort
   - Heap Sort
4. [Algorithm Comparison and Analysis](#algorithm-comparison-and-analysis)
5. [Key Takeaways](#key-takeaways)
6. [Assessment Questions](#assessment-questions)

---

## Introduction and Real-World Relevance

### What Are Searching and Sorting Algorithms?

**Searching** and **sorting** are two fundamental operations in computer science that form the backbone of countless applications. **Searching** refers to the process of finding a specific element within a collection of data, while **sorting** involves arranging data in a particular order (ascending or descending).

### Real-World Relevance

These algorithms are ubiquitous in everyday applications:

- **E-commerce Platforms**: When you search for a product on Amazon or Flipkart, efficient search algorithms retrieve results in milliseconds. Sorting algorithms arrange products by price, rating, or relevance.
- **Contact Management**: Your phone's contact list uses searching to find a person by name and sorting to maintain alphabetical order.
- **Banking Systems**: Transaction history is sorted by date, and account searches use efficient algorithms to locate specific records.
- **Social Media**: Friend recommendations and news feed organization rely on sorting based on relevance and chronology.
- **Database Systems**: Every query you run involves searching through indexed data and returning sorted results.

### Delhi University Syllabus Context

This topic aligns with **GE7A: Design and Analysis of Algorithms** under the NEP 2024 curriculum for BSc Physical Science (CS). Students must understand not just the implementation but also the **time complexity** analysis, which is crucial for writing efficient code in placements and higher studies.

---

## Searching Algorithms

### 1. Linear Search (Sequential Search)

#### Concept

Linear Search is the simplest search algorithm. It checks each element in the list sequentially until the target element is found or the list ends.

#### Algorithm

```
LINEAR_SEARCH(array, target):
    for i from 0 to length(array) - 1:
        if array[i] == target:
            return i  // Element found at index i
    return -1  // Element not found
```

#### Python Implementation

```python
def linear_search(arr, target):
    """
    Linear Search Algorithm
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

# Example usage
data = [23, 45, 12, 67, 89, 34, 56]
result = linear_search(data, 67)
print(f"Element found at index: {result}")  # Output: 3
```

#### When to Use

- Small datasets
- Unsorted data
- When data is accessed sequentially

---

### 2. Binary Search

#### Concept

Binary Search efficiently finds the position of a target value in a **sorted array**. It repeatedly divides the search interval in half, comparing the target with the middle element.

#### Algorithm

```
BINARY_SEARCH(array, target):
    left = 0
    right = length(array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] == target:
            return mid
        else if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  // Element not found
```

#### Python Implementation (Iterative)

```python
def binary_search(arr, target):
    """
    Binary Search Algorithm (Iterative)
    Time Complexity: O(log n)
    Space Complexity: O(1)
    Requirements: Sorted array
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Example usage
sorted_data = [11, 22, 33, 44, 55, 66, 77, 88, 99]
result = binary_search(sorted_data, 55)
print(f"Element found at index: {result}")  # Output: 4
```

#### Python Implementation (Recursive)

```python
def binary_search_recursive(arr, target, left, right):
    """
    Binary Search Algorithm (Recursive)
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion stack
    """
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Example usage
sorted_data = [11, 22, 33, 44, 55, 66, 77, 88, 99]
result = binary_search_recursive(sorted_data, 77, 0, len(sorted_data) - 1)
print(f"Element found at index: {result}")  # Output: 6
```

---

## Sorting Algorithms

### 1. Bubble Sort

#### Concept

Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The largest element "bubbles up" to the end in each pass.

#### Algorithm

```
BUBBLE_SORT(array):
    n = length(array)
    for i from 0 to n-1:
        swapped = false
        for j from 0 to n-i-2:
            if array[j] > array[j+1]:
                swap(array[j], array[j+1])
                swapped = true
        if not swapped:
            break  // Array already sorted
```

#### Python Implementation

```python
def bubble_sort(arr):
    """
    Bubble Sort Algorithm
    Time Complexity: O(n²) worst/average, O(n) best (already sorted)
    Space Complexity: O(1)
    Stable: Yes
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    
    return arr

# Example usage
data = [64, 34, 25, 12, 22, 11, 90]
print("Original:", data)
sorted_data = bubble_sort(data.copy())
print("Sorted:", sorted_data)
# Output: [11, 12, 22, 25, 34, 64, 90]
```

---

### 2. Selection Sort

#### Concept

Selection Sort divides the input into sorted and unsorted regions. It repeatedly selects the minimum (or maximum) element from the unsorted region and moves it to the sorted region.

#### Algorithm

```
SELECTION_SORT(array):
    n = length(array)
    for i from 0 to n-1:
        min_index = i
        for j from i+1 to n-1:
            if array[j] < array[min_index]:
                min_index = j
        swap(array[i], array[min_index])
```

#### Python Implementation

```python
def selection_sort(arr):
    """
    Selection Sort Algorithm
    Time Complexity: O(n²) for all cases
    Space Complexity: O(1)
    Stable: No
    """
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Example usage
data = [64, 25, 12, 22, 11]
print("Original:", data)
sorted_data = selection_sort(data.copy())
print("Sorted:", sorted_data)
# Output: [11, 12, 22, 25, 64]
```

---

### 3. Insertion Sort

#### Concept

Insertion Sort builds the final sorted array one item at a time. It is efficient for small data sets or nearly sorted data.

#### Algorithm

```
INSERTION_SORT(array):
    for i from 1 to length(array) - 1:
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
```

#### Python Implementation

```python
def insertion_sort(arr):
    """
    Insertion Sort Algorithm
    Time Complexity: O(n²) worst/average, O(n) best (nearly sorted)
    Space Complexity: O(1)
    Stable: Yes
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr

# Example usage
data = [12, 11, 13, 5, 6]
print("Original:", data)
sorted_data = insertion_sort(data.copy())
print("Sorted:", sorted_data)
# Output: [5, 6, 11, 12, 13]
```

---

### 4. Merge Sort

#### Concept

Merge Sort is a **divide-and-conquer** algorithm that divides the array into halves, recursively sorts them, and then merges the sorted halves. It guarantees O(n log n) performance.

#### Algorithm

```
MERGE_SORT(array):
    if length(array) <= 1:
        return array
    
    mid = length(array) // 2
    left = MERGE_SORT(array[0:mid])
    right = MERGE_SORT(array[mid:])
    
    return MERGE(left, right)


MERGE(left, right):
    result = []
    i = j = 0
    
    while i < length(left) and j < length(right):
        if left[i] <= right[j]:
            append left[i] to result
            i++
        else:
            append right[j] to result
            j++
    
    append remaining elements of left and right to result
    return result
```

#### Python Implementation

```python
def merge_sort(arr):
    """
    Merge Sort Algorithm (Divide and Conquer)
    Time Complexity: O(n log n) for all cases
    Space Complexity: O(n)
    Stable: Yes
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Example usage
data = [38, 27, 43, 3, 9, 82, 10]
print("Original:", data)
sorted_data = merge_sort(data)
print("Sorted:", sorted_data)
# Output: [3, 9, 10, 27, 38, 43, 82]
```

#### Detailed Walkthrough

For array `[38, 27, 43, 3, 9, 82, 10]`:

1. **Divide**: Split into `[38, 27, 43, 3]` and `[9, 82, 10]`
2. **Conquer**: 
   - Left: `[38, 27, 43, 3]` → `[38, 27]` and `[43, 3]` → `[38]` `[27]` `[43]` `[3]`
   - Merge: `[27, 38]` and `[3, 43]` → `[3, 27, 38, 43]`
   - Right: `[9, 82, 10]` → `[9, 82]` and `[10]` → `[9]` `[82]` `[10]`
   - Merge: `[9, 82]` and `[10]` → `[9, 10, 82]`
3. **Combine**: `[3, 27, 38, 43]` + `[9, 10, 82]` → `[3, 9, 10, 27, 38, 43, 82]`

---

### 5. Quick Sort

#### Concept

Quick Sort is another **divide-and-conquer** algorithm that selects a **pivot** element and partitions the array around the pivot. Elements smaller than the pivot go to the left, and greater elements go to the right.

#### Algorithm

```
QUICK_SORT(array, low, high):
    if low < high:
        pi = PARTITION(array, low, high)
        QUICK_SORT(array, low, pi - 1)
        QUICK_SORT(array, pi + 1, high)


PARTITION(array, low, high):
    pivot = array[high]
    i = low - 1
    
    for j from low to high - 1:
        if array[j] <= pivot:
            i = i + 1
            swap(array[i], array[j])
    
    swap(array[i + 1], array[high])
    return i + 1
```

#### Python Implementation

```python
def quick_sort(arr):
    """
    Quick Sort Algorithm (Divide and Conquer)
    Time Complexity: O(n log n) average, O(n²) worst
    Space Complexity: O(log n)
    Stable: No
    """
    return quick_sort_helper(arr, 0, len(arr) - 1)


def quick_sort_helper(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_helper(arr, low, pi - 1)
        quick_sort_helper(arr, pi + 1, high)
    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage
data = [10, 7, 8, 9, 1, 5]
print("Original:", data)
sorted_data = quick_sort(data.copy())
print("Sorted:", sorted_data)
# Output: [1, 5, 7, 8, 9, 10]
```

#### Detailed Walkthrough

For array `[10, 7, 8, 9, 1, 5]` with pivot = 5:

1. **First partition**: Pivot = 5
   - Compare: 10>5(swap), 7>5(swap), 8>5(swap), 9>5(swap), 1≤5(no swap)
   - After partition: `[1, 7, 8, 9, 10, 5]` → swap 5 and 7 → `[1, 5, 8, 9, 10, 7]`
   - Pivot at index 1

2. **Left subarray** `[1]`: Already sorted
3. **Right subarray** `[8, 9, 10, 7]`: Recursively sort

---

### 6. Heap Sort

#### Concept

Heap Sort uses a binary heap data structure. It converts the array into a **max-heap** (or min-heap), then repeatedly extracts the maximum (or minimum) element and rebuilds the heap.

#### Key Concepts

- **Binary Heap**: A complete binary tree where each parent is greater (max-heap) or smaller (min-heap) than its children
- **Heapify**: The process of converting a binary tree into a heap

#### Algorithm

```
HEAP_SORT(array):
    n = length(array)
    
    // Build max heap
    for i from n//2 - 1 down to 0:
        HEAPIFY(array, n, i)
    
    // Extract elements from heap
    for i from n-1 down to 1:
        swap(array[0], array[i])
        HEAPIFY(array, i, 0)


HEAPIFY(array, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < n and array[left] > array[largest]:
        largest = left
    
    if right < n and array[right] > array[largest]:
        largest = right
    
    if largest != i:
        swap(array[i], array[largest])
        HEAPIFY(array, n, largest)
```

#### Python Implementation

```python
def heap_sort(arr):
    """
    Heap Sort Algorithm
    Time Complexity: O(n log n) for all cases
    Space Complexity: O(1)
    Stable: No
    """
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Example usage
data = [12, 11, 13, 5, 6, 7]
print("Original:", data)
sorted_data = heap_sort(data.copy())
print("Sorted:", sorted_data)
# Output: [5, 6, 7, 11, 12, 13]
```

---

## Algorithm Comparison and Analysis

### Time Complexity Comparison

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity |
|-----------|-----------|---------------|------------|------------------|
| Linear Search | O(n) | O(n) | O(n) | O(1) |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |

### When to Use Which Algorithm

1. **Small datasets (< 50 elements)**: Insertion Sort or Bubble Sort
2. **Nearly sorted data**: Insertion Sort or Bubble Sort
3. **Large datasets**: Merge Sort, Quick Sort, or Heap Sort
4. **Memory constraints**: Heap Sort (O(1) space)
5. **Stability required**: Merge Sort or Insertion Sort
6. **Random data**: Quick Sort (generally fastest in practice)

---

## Key Takeaways

### Searching Algorithms

- **Linear Search** is simple but inefficient for large datasets (O(n))
- **Binary Search** requires sorted data but provides O(log n) performance
- Binary Search can be implemented iteratively or recursively

### Sorting Algorithms

- **Bubble Sort**, **Selection Sort**, and **Insertion Sort** are simple O(n²) algorithms suitable for educational purposes and small datasets
- **Merge Sort** guarantees O(n log n) time complexity but requires O(n) extra space
- **Quick Sort** is fast in practice but has O(n²) worst-case; can be improved with randomized pivot selection
- **Heap Sort** provides O(n log n) time with O(1) space but is not stable

### Important Properties

| Algorithm | Stable | In-Place | Divide & Conquer |
|-----------|--------|----------|------------------|
| Bubble Sort | Yes | Yes | No |
| Selection Sort | No | Yes | No |
| Insertion Sort | Yes | Yes | No |
| Merge Sort | Yes | No | Yes |
| Quick Sort | No | Yes | Yes |
| Heap Sort | No | Yes | No |

### Delhi University Exam Tips

- Remember to explain the algorithm before writing code
- Always mention time and space complexity
- Draw diagrams for sorting algorithms (especially Merge Sort and Quick Sort)
- Know when to use each algorithm based on data characteristics

---

## Assessment Questions

### Level 1: Basic Understanding

**Q1.** What is the time complexity of binary search on a sorted array of size n?

(a) O(n)  
(b) O(n²)  
(c) O(log n)  
(d) O(n log n)

**Q2.** Which sorting algorithm is considered stable?

(a) Quick Sort  
(b) Heap Sort  
(c) Selection Sort  
(d) Merge Sort

**Q3.** In bubble sort, after the first pass, which element will be at the correct position?

(a) First element  
(b) Second element  
(c) Smallest element  
(d) Largest element

**Q4.** What is the worst-case time complexity of Quick Sort?

(a) O(n)  
(b) O(n log n)  
(c) O(n²)  
(d) O(log n)

**Q5.** Which algorithm requires the array to be sorted beforehand?

(a) Linear Search  
(b) Binary Search  
(c) Bubble Sort  
(d) Selection Sort

### Level 2: Intermediate Analysis

**Q6.** For an array that is already sorted in ascending order, which sorting algorithm will give the best performance?

(a) Quick Sort  
(b) Merge Sort  
(c) Insertion Sort  
(d) Selection Sort

**Q7.** Merge Sort is preferred over Quick Sort for sorting linked lists because:

(a) Quick Sort requires random access  
(b) Merge Sort uses less memory  
(c) Quick Sort is unstable  
(d) Merge Sort is faster

**Q8.** What is the space complexity of Merge Sort?

(a) O(1)  
(b) O(log n)  
(c) O(n)  
(d) O(n²)

**Q9.** In heap sort, we build a max-heap to sort in:

(a) Ascending order  
(b) Descending order  
(c) Random order  
(d) No specific order

**Q10.** Which searching algorithm works on both sorted and unsorted arrays?

(a) Binary Search  
(b) Linear Search  
(c) Jump Search  
(d) Exponential Search

### Level 3: Advanced Application

**Q11.** Write the recursive algorithm for binary search and analyze its time complexity.

**Q12.** Trace through the execution of Quick Sort on the array: `[35, 22, 18, 10, 28, 42]`. Show all steps and the final sorted array.

**Q13.** Compare Merge Sort and Quick Sort in terms of:
- Time complexity
- Space complexity
- Stability
- Best use cases

**Q14.** Explain the divide-and-conquer approach used in Merge Sort with a suitable example.

**Q15.** Write a Python program to count the number of comparisons made in binary search for a given target element.

### Level 4: Problem Solving

**Q16.** Given two sorted arrays of size m and n, write an algorithm to find the median of the combined sorted array in O(log(m+n)) time complexity.

**Q17.** Modify the bubble sort algorithm to stop early if the array becomes sorted before completing all passes. Write the modified algorithm.

**Q18.** Implement a function that uses binary search to find the first occurrence of a duplicate element in a sorted array.

**Q19.** Design an algorithm to find the kth smallest element in an unsorted array. Analyze its time complexity for different approaches.

**Q20.** Explain why Quick Sort is generally faster than Merge Sort in practice despite having the same average-case time complexity.

### Programming Questions

**Q21.** Write a complete Python program implementing merge sort with detailed comments explaining each step.

**Q22.** Implement a hybrid sorting algorithm that uses insertion sort for small subarrays (size ≤ 10) and merge sort for larger ones. Explain the rationale behind this approach.

---

## Answer Key

| Q No. | Answer |
|-------|--------|
| Q1 | (c) O(log n) |
| Q2 | (d) Merge Sort |
| Q3 | (d) Largest element |
| Q4 | (c) O(n²) |
| Q5 | (b) Binary Search |
| Q6 | (c) Insertion Sort |
| Q7 | (a) Quick Sort requires random access |
| Q8 | (c) O(n) |
| Q9 | (a) Ascending order |
| Q10 | (b) Linear Search |

---

## References and Further Reading

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
2. Goodrich, M. T., & Tamassia, R. (2015). *Data Structures and Algorithms in Python*. Wiley.
3. Delhi University B.Sc. Physical Science (CS) Syllabus, NEP 2024.
4. GeeksforGeeks - Searching and Sorting Algorithms

---

*Document prepared for GE7A: Design and Analysis of Algorithms, Delhi University, NEP 2024*