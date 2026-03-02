# Merge Sort and Quick Sort: Comprehensive Study Material

## Design and Analysis of Algorithms — BSc (Hons) Computer Science

### Delhi University NEP 2024 UGCF Syllabus Context

This study material aligns with the Delhi University NEP 2024 UGCF syllabus for **Design and Analysis of Algorithms**, specifically covering the unit on **Sorting Algorithms**. Both Merge Sort and Quick Sort are fundamental divide-and-conquer sorting algorithms that form the backbone of algorithmic thinking and are essential for university examinations and practical applications.

---

## 1. Introduction

Sorting is one of the most fundamental operations in computer science. Whether it's organizing emails by date, arranging e-commerce products by price, or sorting search results by relevance—sorting algorithms power countless real-world applications. In the context of the Delhi University curriculum, understanding efficient sorting algorithms is crucial for developing optimized software solutions.

Two of the most important comparison-based sorting algorithms are **Merge Sort** and **Quick Sort**. Both employ the **divide-and-conquer** paradigm, but they differ significantly in their approach, time complexity, space requirements, and practical performance characteristics.

---

## 2. Merge Sort

### 2.1 Concept and Overview

Merge Sort is a **stable**, **comparison-based** sorting algorithm that follows the divide-and-conquer paradigm. It was invented by John von Neumann in 1945. The algorithm works by:

1. **Dividing** the unsorted array into n subarrays, each containing one element (a sorted subarray)
2. **Conquer** (merge) by repeatedly merging adjacent subarrays to produce new sorted subarrays
3. **Combine** until there is only one subarray remaining (the sorted array)

### 2.2 Why Merge Sort Matters

- **Guaranteed O(n log n) time complexity** — always efficient regardless of input
- **Stable sort** — maintains the relative order of equal elements
- **External sorting** — ideal for sorting large files that don't fit in memory
- **Parallel processing** — easily parallelizable due to independent subproblems

### 2.3 Algorithm Steps

```
MergeSort(A, p, r):
    if p < r:
        q = floor((p + r) / 2)
        MergeSort(A, p, q)      // Left half
        MergeSort(A, q + 1, r)  // Right half
        Merge(A, p, q, r)       // Merge sorted halves
```

```
Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    create L[1..n1+1] and R[1..n2+1]
    for i = 1 to n1:
        L[i] = A[p + i - 1]
    for j = 1 to n2:
        R[j] = A[q + j]
    L[n1 + 1] = ∞
    R[n2 + 1] = ∞
    i = 1
    j = 1
    for k = p to r:
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
```

### 2.4 Detailed Example

**Input Array:** [38, 27, 43, 3, 9, 82, 10]

**Step-by-Step Execution:**

1. **Divide Phase:**
   - Original: [38, 27, 43, 3, 9, 82, 10]
   - Split: [38, 27, 43, 3] | [9, 82, 10]
   - Split: [38, 27] | [43, 3] | [9, 82] | [10]
   - Split: [38] | [27] | [43] | [3] | [9] | [82] | [10]

2. **Merge Phase:**
   - Merge [38] and [27]: [27, 38]
   - Merge [43] and [3]: [3, 43]
   - Merge [9] and [82]: [9, 82]
   - Merge [27, 38] and [3, 43]: [3, 27, 38, 43]
   - Merge [9, 82] and [10]: [9, 10, 82]
   - Final Merge: [3, 9, 10, 27, 38, 43, 82]

### 2.5 Implementation in C

```c
#include <stdio.h>

void merge(int arr[], int p, int q, int r) {
    int n1 = q - p + 1;
    int n2 = r - q;
    int L[n1], R[n2];
    
    for (int i = 0; i < n1; i++)
        L[i] = arr[p + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[q + 1 + j];
    
    int i = 0, j = 0, k = p;
    
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k++] = L[i++];
        } else {
            arr[k++] = R[j++];
        }
    }
    
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void mergeSort(int arr[], int p, int r) {
    if (p < r) {
        int q = p + (r - p) / 2;
        mergeSort(arr, p, q);
        mergeSort(arr, q + 1, r);
        merge(arr, p, q, r);
    }
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int arr[] = {38, 27, 43, 3, 9, 82, 10};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    printf("Original array: ");
    printArray(arr, n);
    
    mergeSort(arr, 0, n - 1);
    
    printf("Sorted array: ");
    printArray(arr, n);
    
    return 0;
}
```

### 2.6 Time and Space Complexity

| Aspect | Complexity |
|--------|------------|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n log n) |
| Space Complexity | O(n) — requires auxiliary array |

---

## 3. Quick Sort

### 3.1 Concept and Overview

Quick Sort is another divide-and-conquer algorithm, but unlike Merge Sort, it **does most of the work** during the **partitioning** step rather than during merging. It is an **in-place** sorting algorithm (though not stable) that is widely used due to its excellent average-case performance and cache efficiency.

The algorithm works by:
1. **Selecting a pivot** element from the array
2. **Partitioning** the array so that all elements smaller than the pivot are on the left, and all elements greater than the pivot are on the right
3. **Recursively** applying the same process to the left and right subarrays

### 3.2 Why Quick Sort Matters

- **In-place sorting** — requires minimal extra memory O(log n) for recursion stack
- **Cache-friendly** — excellent spatial locality
- **Average-case O(n log n)** — faster than other O(n log n) algorithms in practice
- ** Widely used** — default sorting algorithm in many libraries (like C's qsort, Java's Arrays.sort for primitives)

### 3.3 Algorithm Steps

```
QuickSort(A, low, high):
    if low < high:
        pi = Partition(A, low, high)  // pi is partitioning index
        QuickSort(A, low, pi - 1)     // Sort elements before partition
        QuickSort(A, pi + 1, high)    // Sort elements after partition
```

```
Partition(A, low, high):
    pivot = A[high]    // Selecting last element as pivot
    i = low - 1        // Index of smaller element
    
    for j = low to high - 1:
        if A[j] <= pivot:
            i = i + 1
            swap A[i] and A[j]
    
    swap A[i + 1] and A[high]
    return i + 1
```

### 3.4 Detailed Example

**Input Array:** [10, 7, 8, 9, 1, 5]
**Choosing pivot:** Last element = 5 (1-based indexing shows position)

**First Partition (pivot = 1):**

```
Initial: [10, 7, 8, 9, 1, 5], pivot = 1 (value 5)

j=0: 10 <= 5? No → i = -1, no swap
j=1: 7 <= 5? No → i = -1, no swap  
j=2: 8 <= 5? No → i = -1, no swap
j=3: 9 <= 5? No → i = -1, no swap
j=4: 1 <= 5? Yes → i = 0, swap arr[0] and arr[4]
    Array: [1, 7, 8, 9, 10, 5]

After loop: swap arr[i+1] and arr[high]
    Array: [1, 5, 8, 9, 10, 7]
    Partition index = 1
```

**Recursive Calls:**
- Left subarray [1]: Already sorted
- Right subarray [8, 9, 10, 7]: Continue partitioning

### 3.5 Implementation in C

```c
#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];  // Pivot element
    int i = (low - 1);
    
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        
        // Sort elements before partition
        quickSort(arr, low, pi - 1);
        
        // Sort elements after partition
        quickSort(arr, pi + 1, high);
    }
}

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    printf("Original array: ");
    printArray(arr, n);
    
    quickSort(arr, 0, n - 1);
    
    printf("Sorted array: ");
    printArray(arr, n);
    
    return 0;
}
```

### 3.6 Pivot Selection Strategies

The efficiency of Quick Sort heavily depends on pivot selection:

| Strategy | Description | Impact |
|----------|-------------|--------|
| **First element** | Always pick arr[0] | Degrades to O(n²) for sorted arrays |
| **Last element** | Always pick arr[high] | Default implementation, same issue |
| **Random** | Random index selection | Good average case, eliminates worst-case for specific patterns |
| **Median-of-three** | Pick median of first, middle, last | Better distribution, commonly used |
| **Median-of-medians** | Theoretical median selection | Guarantees O(n log n) but adds overhead |

### 3.7 Time and Space Complexity

| Aspect | Complexity |
|--------|------------|
| Best Case | O(n log n) — balanced partitions |
| Average Case | O(n log n) |
| Worst Case | O(n²) — when array is already sorted and pivot is smallest/largest |
| Space Complexity | O(log n) — recursion stack (worst case O(n)) |

---

## 4. Comparison: Merge Sort vs Quick Sort

### 4.1 Side-by-Side Analysis

| Feature | Merge Sort | Quick Sort |
|---------|-----------|------------|
| **Algorithm Type** | Divide and Conquer | Divide and Conquer |
| **Time (Best)** | O(n log n) | O(n log n) |
| **Time (Average)** | O(n log n) | O(n log n) |
| **Time (Worst)** | O(n log n) | O(n²) |
| **Space Complexity** | O(n) | O(log n) |
| **Stable** | Yes | No |
| **In-place** | No | Yes (mostly) |
| **Cache Efficiency** | Moderate | Excellent |
| **Parallelizable** | Yes | Difficult |

### 4.2 When to Use Which?

**Use Merge Sort when:**
- You need stable sorting
- External sorting (large files)
- Linked list sorting (no random access needed)
- Guaranteed O(n log n) performance is required
- Working with parallel systems

**Use Quick Sort when:**
- Memory is constrained (in-place)
- Average performance matters more than worst-case
- Cache efficiency is important
- Working with arrays (random access available)
- Internal sorting of small to medium datasets

---

## 5. Multiple Choice Questions

### MCQ 1: Merge Sort Time Complexity
**Question:** What is the worst-case time complexity of Merge Sort?

A) O(n)
B) O(n log n)
C) O(n²)
D) O(log n)

**Answer:** B) O(n log n)

**Explanation:** Merge Sort consistently performs at O(n log n) regardless of the input arrangement. It divides the array into halves (log n levels) and merges them in O(n) time at each level, resulting in O(n log n) for all cases—best, average, and worst.

---

### MCQ 2: Quick Sort Partition
**Question:** In the standard Quick Sort partition scheme (Lomuto partition), which element is typically chosen as the pivot?

A) First element
B) Random element
C) Last element
D) Middle element

**Answer:** C) Last element

**Explanation:** The Lomuto partition scheme, which is commonly taught and implemented, selects the last element (arr[high]) as the pivot. While simple, this can lead to O(n²) worst-case behavior for already sorted arrays. The Hoare partition scheme uses a different approach.

---

### MCQ 3: Stability in Sorting
**Question:** Which of the following sorting algorithms is NOT stable?

A) Bubble Sort
B) Merge Sort
C) Insertion Sort
D) Quick Sort

**Answer:** D) Quick Sort

**Explanation:** Quick Sort is not a stable sorting algorithm because it swaps elements based on comparison with the pivot, which can change the relative order of equal elements. For example, if we have two elements with the same value but different original positions, Quick Sort may place them in either order after partitioning. Merge Sort, Bubble Sort, and Insertion Sort are stable because they maintain the relative order of equal elements.

---

### MCQ 4: Space Complexity
**Question:** What is the space complexity of Quick Sort (considering the recursion stack)?

A) O(1)
B) O(n)
C) O(log n)
D) O(n log n)

**Answer:** C) O(log n)

**Explanation:** Quick Sort is considered an in-place sorting algorithm because it only requires O(log n) auxiliary space for the recursion stack in the average and best cases. This is because the array is partitioned recursively, and the maximum depth of the recursion tree is O(log n) when partitions are reasonably balanced. In the worst case (already sorted array with last element as pivot), the space complexity becomes O(n) due to skewed recursion.

---

### MCQ 5: External Sorting
**Question:** Which sorting algorithm is more suitable for sorting large files that don't fit in memory (external sorting)?

A) Quick Sort
B) Bubble Sort
C) Merge Sort
D) Insertion Sort

**Answer:** C) Merge Sort

**Explanation:** Merge Sort is the algorithm of choice for external sorting (sorting data stored on disk or tape) because:
1. It has guaranteed O(n log n) performance
2. It can be easily implemented for sequential access (suitable for tapes/drives)
3. It naturally handles merge operations on sorted chunks
4. It can merge already sorted segments efficiently

Quick Sort requires random access for partitioning, making it less suitable for external sorting.

---

## 6. Flashcards

### Flashcard 1: Merge Sort Definition
**Front:** What is Merge Sort?

**Back:** Merge Sort is a stable, divide-and-conquer sorting algorithm that divides the input array into two halves, recursively sorts them, and then merges the sorted halves back together. It guarantees O(n log n) time complexity in all cases.

---

### Flashcard 2: Merge Sort Key Property
**Front:** Why is Merge Sort considered stable?

**Back:** Merge Sort is stable because when merging equal elements, it always takes the element from the left subarray first, preserving the relative order of equal elements in the sorted output.

---

### Flashcard 3: Quick Sort Pivot
**Front:** What is the role of the pivot in Quick Sort?

**Back:** The pivot is a selected element used to partition the array. Elements smaller than the pivot are moved to its left, and elements greater than the pivot are moved to its right. The pivot's final position is its sorted position in the array.

---

### Flashcard 4: Quick Sort Worst Case
**Front:** When does Quick Sort exhibit O(n²) time complexity?

**Back:** Quick Sort exhibits O(n²) worst-case time complexity when:
1. The array is already sorted (ascending or descending)
2. The pivot is always the smallest or largest element
3. All elements are identical

This happens when partitions are extremely unbalanced.

---

### Flashcard 5: Key Difference
**Front:** What is the fundamental difference between Merge Sort and Quick Sort in terms of where the work is done?

**Back:** In Merge Sort, the "conquer" (merging) step does most of the work after recursive calls complete. In Quick Sort, the "divide" (partitioning) step does most of the work before making recursive calls. This is why Quick Sort is in-place while Merge Sort requires O(n) auxiliary space.

---

### Flashcard 6: In-Place Algorithm
**Front:** What does it mean for an algorithm to be "in-place"?

**Back:** An in-place algorithm uses only O(1) or O(log n) auxiliary space (ignoring the input). Quick Sort is considered in-place because it only needs O(log n) space for recursion stack. Merge Sort is NOT in-place because it requires O(n) additional space for the temporary arrays during merging.

---

## 7. Key Takeaways

1. **Divide-and-Conquer Paradigm**: Both Merge Sort and Quick Sort follow the divide-and-conquer strategy, but they differ in how they divide and conquer.

2. **Merge Sort Guarantees**: Merge Sort provides guaranteed O(n log n) time complexity and is stable, making it ideal for applications requiring predictable performance and maintaining element order.

3. **Quick Sort Efficiency**: Quick Sort offers excellent average-case performance O(n log n) and is cache-efficient, but its worst-case O(n²) can be mitigated with good pivot selection strategies (randomized, median-of-three).

4. **Space Trade-offs**: Merge Sort trades space (O(n)) for guaranteed time complexity, while Quick Sort trades predictable time for lower space requirements O(log n).

5. **Stability Matters**: For applications where maintaining the relative order of equal elements is important, Merge Sort is preferred over Quick Sort.

6. **Practical Usage**: Many programming libraries use hybrid algorithms (like Timsort) that combine the best of both worlds, but understanding these fundamental algorithms is essential for algorithmic thinking.

7. **Exam Focus**: For Delhi University examinations, remember the time/space complexities, stability properties, and be able to trace through examples of both algorithms step-by-step.

---

*This study material is prepared for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF curriculum.*