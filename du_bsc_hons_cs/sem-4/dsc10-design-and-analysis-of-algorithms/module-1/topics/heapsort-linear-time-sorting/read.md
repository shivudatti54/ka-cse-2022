# Heapsort and Linear Time Sorting Algorithms

## Design and Analysis of Algorithms (DAA)

### BSc (Hons) Computer Science — Delhi University, NEP 2024 UGCF

---

## Table of Contents

1. [Introduction and Real-World Relevance](#1-introduction-and-real-world-relevance)
2. [Heap Data Structure](#2-heap-data-structure)
3. [The Heapify Operation](#3-the-heapify-operation)
4. [Building a Max-Heap](#4-building-a-max-heap)
5. [HeapSort Algorithm](#5-heapsort-algorithm)
6. [Analysis of HeapSort](#6-analysis-of-heapsort)
7. [Linear Time Sorting Algorithms](#7-linear-time-sorting-algorithms)
   - 7.1 [Counting Sort](#71-counting-sort)
   - 7.2 [Radix Sort](#72-radix-sort)
   - 7.3 [Bucket Sort](#73-bucket-sort)
8. [Comparison of Sorting Algorithms](#8-comparison-of-sorting-algorithms)
9. [Key Takeaways](#9-key-takeaways)
10. [Practice Questions](#10-practice-questions)

---

## 1. Introduction and Real-World Relevance

Sorting is one of the most fundamental operations in computer science. Whether it's organizing customer records in a database, ranking search results, or arranging data for efficient processing, sorting algorithms form the backbone of countless applications.

### Why This Topic Matters

This unit covers two important categories of sorting algorithms:

1. **Comparison-based sorting** - HeapSort, which achieves O(n log n) time complexity using a specialized tree-based data structure
2. **Non-comparison-based sorting** - Linear time sorting algorithms (Counting Sort, Radix Sort, Bucket Sort) that can achieve O(n) time complexity under certain conditions

According to the Delhi University NEP 2024 UGCF syllabus for Design and Analysis of Algorithms, students must understand both categories, their implementations, time complexities, and practical applications.

### Real-World Applications

| Application | Sorting Algorithm Used | Reason |
|-------------|----------------------|--------|
| Database indexing | HeapSort, Radix Sort | Stability and predictable performance |
| Operating System task scheduling | HeapSort (priority queues) | Efficient extraction of minimum/maximum |
| Birthday party arrangements | Bucket Sort | Data distribution in known ranges |
| Grading systems | Counting Sort | Integer data with limited range |
| ISBN book sorting | Radix Sort | Fixed-length string/number data |

---

## 2. Heap Data Structure

A **heap** is a complete binary tree that satisfies the **heap property**:

- **Max-Heap**: Parent node ≥ Children nodes
- **Min-Heap**: Parent node ≤ Children nodes

### Array Representation of Heaps

Heaps are efficiently represented using arrays because they are complete binary trees. This sequential representation eliminates the need for pointers.

```
Index:    0   1   2   3   4   5   6
Array:   [50][30][20][15][10][8][16]
              ↓       ↓
           Children of index 1 (30):
           Left child  = 2(1) + 1 = 3 → index 3 = 15
           Right child = 2(1) + 2 = 4 → index 4 = 10

           Parent of index 4:
           Parent = floor((4-1)/2) = floor(1.5) = 1 → index 1 = 30
```

### Key Formulas for Array Representation

For a node at index `i`:

- **Left Child**: `2i + 1`
- **Right Child**: `2i + 2`
- **Parent**: `⌊(i - 1) / 2⌋`
- **Last non-leaf node**: `⌊(n/2)⌋ - 1`

---

## 3. The Heapify Operation

**Heapify** (or **Max-Heapify**) is the fundamental operation that maintains the heap property. It assumes that the subtrees rooted at the left and right children of node `i` are already heaps, but the node `i` might violate the heap property.

### Pseudocode: MAX-HEAPIFY

```
MAX-HEAPIFY(A, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < heap_size[A] and A[left] > A[largest]:
        largest = left
    
    if right < heap_size[A] and A[right] > A[largest]:
        largest = right
    
    if largest != i:
        swap A[i] with A[largest]
        MAX-HEAPIFY(A, largest)
```

### Detailed Example of Heapify

Consider the following array representation of a binary tree:

```
Initial Array: [4, 10, 3, 5, 1]

Tree Representation:
        4(0)
       /    \
    10(1)    3(2)
    /  \
  5(3)  1(4)

Heap Property Violation at index 0 (value 4):
- Left child at index 1: 10 (greater than 4)
- Right child at index 2: 3 (not greater than largest)
- Largest = 1 (index of value 10)

Step 1: Swap A[0] and A[1]
Array becomes: [10, 4, 3, 5, 1]

Tree after swap:
        10(0)
       /    \
    4(1)     3(2)
    /  \
  5(3)  1(4)

Now check subtree rooted at index 1:
- Left child (index 3): 5 > 4 ✓
- Right child (index 4): 1 < 5
- Largest = 3 (index of value 5)

Step 2: Swap A[1] and A[3]
Array becomes: [10, 5, 3, 4, 1]

Tree after final swap:
        10(0)
       /    \
    5(1)     3(2)
    /  \
  4(3)  1(4)

Now all nodes satisfy max-heap property!
```

### Java Implementation of Heapify

```java
public class HeapSort {
    
    // Max-Heapify operation
    public static void maxHeapify(int[] arr, int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        
        // Check if left child exists and is greater than root
        if (left < n && arr[left] > arr[largest]) {
            largest = left;
        }
        
        // Check if right child exists and is greater than current largest
        if (right < n && arr[right] > arr[largest]) {
            largest = right;
        }
        
        // If largest is not root, swap and continue heapifying
        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;
            
            // Recursively heapify the affected sub-tree
            maxHeapify(arr, n, largest);
        }
    }
}
```

---

## 4. Building a Max-Heap

To build a max-heap from an unsorted array, we need to heapify all non-leaf nodes in reverse order (from last non-leaf node to root).

### Why Start from Last Non-Leaf Node?

- Leaf nodes (indices from ⌊n/2⌋ to n-1) are already single-element heaps
- We only need to heapify nodes that have children
- The last non-leaf node is at index ⌊n/2⌋ - 1

### Pseudocode: BUILD-MAX-HEAP

```
BUILD-MAX-HEAP(A):
    heap_size[A] = length[A]
    for i = floor(length[A]/2) - 1 downto 0:
        MAX-HEAPIFY(A, i)
```

### Complete Example: Building a Max-Heap

**Input Array**: [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

**Step-by-Step Process:**

```
Initial tree (not a heap):
           4(0)
         /      \
       1(1)      3(2)
      /   \      /   \
    2(3)  16(4) 9(5) 10(6)
    /  \
  14(7) 8(8)  7(9)

Last non-leaf node index = floor(10/2) - 1 = 4

Heapify from index 4 to 0:

Index 4 (value 16): Already satisfies heap property
Index 3 (value 2): Heapify → largest = 7 (14)
                   Swap 2 and 14 → [4,1,3,14,16,9,10,2,8,7]
Index 2 (value 3): Heapify → largest = 6 (10)
                   Swap 3 and 10 → [4,1,10,14,16,9,3,2,8,7]
Index 1 (value 1): Heapify → largest = 3 (14)
                   Swap 1 and 14 → [4,14,10,1,16,9,3,2,8,7]
                   Continue heapify at index 3 → largest = 7 (8)
                   Swap 1 and 8 → [4,14,10,8,16,9,3,2,1,7]
Index 0 (value 4): Heapify → largest = 1 (14)
                   Swap 4 and 14 → [14,4,10,8,16,9,3,2,1,7]
                   Continue heapify at index 1 → largest = 3 (8)
                   Swap 4 and 8 → [14,8,10,4,16,9,3,2,1,7]

Final Max-Heap:
           14(0)
         /      \
       8(1)      10(2)
      /   \      /   \
    4(3)  16(4) 9(5)  3(6)
    /  \
  2(7)  1(8)  7(9)

Array: [14, 8, 10, 4, 16, 9, 3, 2, 1, 7]
```

### Java Implementation: Build Max-Heap

```java
public static void buildMaxHeap(int[] arr) {
    int n = arr.length;
    
    // Start from last non-leaf node and heapify each node
    for (int i = n / 2 - 1; i >= 0; i--) {
        maxHeapify(arr, n, i);
    }
}
```

---

## 5. HeapSort Algorithm

HeapSort combines the heap data structure with a sorting algorithm. The basic idea is:

1. Build a max-heap from the input array
2. Repeatedly extract the maximum element (root) and place it at the end
3. Reduce the heap size and heapify the root
4. Continue until the heap is empty

### Pseudocode: HEAPSORT

```
HEAPSORT(A):
    BUILD-MAX-HEAP(A)          // Build max-heap from unsorted array
    for i = length[A] - 1 downto 1:
        swap A[0] with A[i]    // Move current root (max) to end
        heap_size[A] = heap_size[A] - 1
        MAX-HEAPIFY(A, 0)      // Restore heap property for reduced heap
```

### Complete Example: HeapSort

**Input Array**: [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

**Step 1: Build Max-Heap**
```
Max-Heap: [14, 8, 10, 4, 16, 9, 3, 2, 1, 7]
```

**Step 2: Sort by Extracting Maximum**

| Iteration | Array State | Action |
|-----------|-------------|--------|
| 1 | [14,8,10,4,16,9,3,2,1,7] | Swap 14 with 7, heapify [0-8] |
| 2 | [10,8,9,4,7,3,2,1,16] | Swap 10 with 1, heapify [0-7] |
| 3 | [9,8,3,4,7,1,2,10,16] | Swap 9 with 2, heapify [0-6] |
| 4 | [8,7,3,4,2,1,9,10,16] | Swap 8 with 1, heapify [0-5] |
| 5 | [7,4,3,1,2,8,9,10,16] | Swap 7 with 2, heapify [0-4] |
| 6 | [4,2,3,1,7,8,9,10,16] | Swap 4 with 7, heapify [0-3] |
| 7 | [3,2,1,4,7,8,9,10,16] | Swap 3 with 4, heapify [0-2] |
| 8 | [2,1,3,4,7,8,9,10,16] | Swap 2 with 3, heapify [0-1] |
| 9 | [1,2,3,4,7,8,9,10,16] | Swap 1 with 2, heapify [0-0] |

**Sorted Array**: [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]

### Complete Java Implementation

```java
public class HeapSortComplete {
    
    // Main HeapSort method
    public static void heapSort(int[] arr) {
        int n = arr.length;
        
        // Build max heap
        buildMaxHeap(arr);
        
        // Extract elements from heap one by one
        for (int i = n - 1; i > 0; i--) {
            // Move current root to end
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;
            
            // Call max heapify on the reduced heap
            maxHeapify(arr, i, 0);
        }
    }
    
    // Build max heap
    private static void buildMaxHeap(int[] arr) {
        int n = arr.length;
        for (int i = n / 2 - 1; i >= 0; i--) {
            maxHeapify(arr, n, i);
        }
    }
    
    // Max heapify
    private static void maxHeapify(int[] arr, int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        
        if (left < n && arr[left] > arr[largest])
            largest = left;
        
        if (right < n && arr[right] > arr[largest])
            largest = right;
        
        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;
            
            maxHeapify(arr, n, largest);
        }
    }
    
    // Test the implementation
    public static void main(String[] args) {
        int[] arr = {4, 1, 3, 2, 16, 9, 10, 14, 8, 7};
        
        System.out.println("Original Array:");
        printArray(arr);
        
        heapSort(arr);
        
        System.out.println("Sorted Array:");
        printArray(arr);
    }
    
    private static void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
```

### Output:
```
Original Array:
4 1 3 2 16 9 10 14 8 7 
Sorted Array:
1 2 3 4 7 8 9 10 14 16 
```

---

## 6. Analysis of HeapSort

### Time Complexity Analysis

| Operation | Complexity | Explanation |
|-----------|------------|-------------|
| Building Max-Heap | O(n) | Technically O(n), can be proven by harmonic series |
| Each MAX-HEAPIFY | O(log n) | Height of heap = ⌊log₂n⌋ |
| Extraction Loop | O(n log n) | n extractions × O(log n) each |
| **Total** | **O(n log n)** | Worst, Average, and Best case |

**Proof of Building Heap Complexity:**
- Nodes at height h: ⌊n/2^h+1⌋
- Heapify cost at height h: O(h)
- Total: Σ (n/2^h+1) × h = O(n × Σ h/2^h) = O(n)

### Space Complexity

- **In-place sorting**: O(1) auxiliary space
- The sorting is performed within the original array

### Stability Analysis

**HeapSort is NOT a stable sorting algorithm.**

Example demonstrating instability:
```
Initial: [2a, 2b, 1]  where 2a comes before 2b
After sorting: [1, 2b, 2a]  (2a and 2b may swap positions)
```

### Advantages and Disadvantages

| Advantages | Disadvantages |
|------------|---------------|
| O(n log n) worst-case time complexity | Not stable |
| In-place sorting (O(1) extra space) | Cache-unfriendly (not sequential access) |
| Predictable performance | Slower in practice than QuickSort |
| Excellent for priority queue implementations | Complex to implement correctly |

---

## 7. Linear Time Sorting Algorithms

Unlike comparison-based sorting (which have a theoretical lower bound of Ω(n log n)), linear time sorting algorithms can achieve O(n) under specific conditions. These algorithms make assumptions about the nature of input data.

### 7.1 Counting Sort

Counting Sort works by determining, for each element, the number of elements less than it. It uses this information to place elements directly in their correct position.

#### Key Characteristics
- **Time Complexity**: O(n + k) where k is the range of input
- **Space Complexity**: O(n + k)
- **Stable**: Yes
- **Use Case**: When range of input (k) is not significantly larger than n

#### Pseudocode: COUNTING-SORT

```
COUNTING-SORT(A, B, k):
    // A: input array, B: output array, k: range of input
    let C[0..k] be a new array
    for i = 0 to k:
        C[i] = 0
    
    // Count occurrences of each value
    for j = 1 to length[A]:
        C[A[j]] = C[A[j]] + 1
    
    // C[i] now contains the number of elements equal to i
    
    // Transform to cumulative count (position calculation)
    for i = 1 to k:
        C[i] = C[i] + C[i-1]
    
    // Build output array (traverse A from right to maintain stability)
    for j = length[A] down to 1:
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1
```

#### Example: Counting Sort

**Input**: [2, 5, 3, 0, 2, 3, 0, 3]
**k (max value)**: 5

```
Step 1: Initialize count array C[0..5] = [0, 0, 0, 0, 0, 0]

Step 2: Count occurrences
C[2]++, C[5]++, C[3]++, C[0]++, C[2]++, C[3]++, C[0]++, C[3]++
C = [2, 0, 2, 3, 0, 1]

Step 3: Cumulative count
C[0] = 2
C[1] = 2
C[2] = 4
C[3] = 7
C[4] = 7
C[5] = 8

C now represents: C[i] = position of last occurrence of i + 1

Step 4: Build output (traversing right to left for stability)
j=8: A[8]=3 → B[7]=3 → C[3]=6
j=7: A[7]=0 → B[1]=0 → C[0]=1
j=6: A[6]=0 → B[0]=0 → C[0]=0
j=5: A[5]=3 → B[6]=3 → C[3]=5
j=4: A[4]=2 → B[3]=2 → C[2]=3
j=3: A[3]=3 → B[5]=3 → C[3]=4
j=2: A[2]=5 → B[7]=5 → C[5]=7
j=1: A[1]=2 → B[2]=2 → C[2]=2

Output B: [0, 0, 2, 2, 3, 3, 3, 5]
```

#### Java Implementation: Counting Sort

```java
public class CountingSort {
    
    public static int[] countingSort(int[] arr) {
        // Find the range of input
        int max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        
        // Create count array
        int[] count = new int[max + 1];
        
        // Count occurrences
        for (int i = 0; i < arr.length; i++) {
            count[arr[i]]++;
        }
        
        // Cumulative count
        for (int i = 1; i <= max; i++) {
            count[i] += count[i - 1];
        }
        
        // Build output array
        int[] output = new int[arr.length];
        for (int i = arr.length - 1; i >= 0; i--) {
            output[count[arr[i]] - 1] = arr[i];
            count[arr[i]]--;
        }
        
        return output;
    }
    
    public static void main(String[] args) {
        int[] arr = {2, 5, 3, 0, 2, 3, 0, 3};
        
        System.out.println("Original: ");
        for (int num : arr) System.out.print(num + " ");
        
        int[] sorted = countingSort(arr);
        
        System.out.println("\nSorted: ");
        for (int num : sorted) System.out.print(num + " ");
    }
}
```

---

### 7.2 Radix Sort

Radix Sort processes digits of numbers one at a time, starting from the least significant digit (LSD) or most significant digit (MSD). It uses a stable subroutine (typically Counting Sort) for digit processing.

#### Key Characteristics
- **Time Complexity**: O(d × (n + k)) where d = number of digits, k = base
- **Space Complexity**: O(n + k)
- **Stable**: Yes (depends on stable counting sort)
- **Use Case**: When data has fixed number of "digits" (e.g., integers, strings)

#### Types of Radix Sort

1. **LSD Radix Sort**: Process from least significant to most significant digit
2. **MSD Radix Sort**: Process from most significant to least significant digit

#### Pseudocode: LSD RADIX-SORT

```
RADIX-SORT(A, d):
    // Sort A based on d digits
    for i = 1 to d:
        // Use a stable sort (like Counting Sort) to sort A by i-th digit
        COUNTING-SORT(A, i)
```

#### Example: Radix Sort

**Input**: [329, 457, 657, 839, 436, 720, 355]
**Assuming base 10 (digits 0-9)**

```
Pass 1 (Unit's place - 1's digit):
Numbers: 329, 457, 657, 839, 436, 720, 355
1's:     9,    7,    7,    9,    6,    0,    5
After sorting by 1's digit:
[720, 355, 436, 457, 657, 329, 839]

Pass 2 (Ten's place - 10's digit):
Numbers: 720, 355, 436, 457, 657, 329, 839
10's:    2,    5,    3,    5,    5,    2,    3
After sorting by 10's digit:
[720, 329, 436, 839, 355, 457, 657]

Pass 3 (Hundred's place - 100's digit):
Numbers: 720, 329, 436, 839, 355, 457, 657
100's:  7,    3,    4,    8,    3,    4,    6
After sorting by 100's digit:
[329, 355, 436, 457, 657, 720, 839]

Final Sorted Array: [329, 355, 436, 457, 657, 720, 839]
```

#### Java Implementation: Radix Sort

```java
public class RadixSort {
    
    // Find maximum number to know number of digits
    private static int getMax(int[] arr) {
        int max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        return max;
    }
    
    // Counting sort for specific digit
    private static void countingSortByDigit(int[] arr, int exp) {
        int n = arr.length;
        int[] output = new int[n];
        int[] count = new int[10]; // Digits 0-9
        
        // Initialize count array
        for (int i = 0; i < 10; i++) {
            count[i] = 0;
        }
        
        // Count occurrences of digits at current position
        for (int i = 0; i < n; i++) {
            int digit = (arr[i] / exp) % 10;
            count[digit]++;
        }
        
        // Change count[i] to contain actual position
        for (int i = 1; i < 10; i++) {
            count[i] += count[i - 1];
        }
        
        // Build output array (traverse backwards for stability)
        for (int i = n - 1; i >= 0; i--) {
            int digit = (arr[i] / exp) % 10;
            output[count[digit] - 1] = arr[i];
            count[digit]--;
        }
        
        // Copy output to original array
        for (int i = 0; i < n; i++) {
            arr[i] = output[i];
        }
    }
    
    // Main Radix Sort function
    public static void radixSort(int[] arr) {
        int max = getMax(arr);
        
        // Apply counting sort for each digit
        for (int exp = 1; max / exp > 0; exp *= 10) {
            countingSortByDigit(arr, exp);
        }
    }
    
    public static void main(String[] args) {
        int[] arr = {329, 457, 657, 839, 436, 720, 355};
        
        System.out.println("Original: ");
        for (int num : arr) System.out.print(num + " ");
        
        radixSort(arr);
        
        System.out.println("\nSorted: ");
        for (int num : arr) System.out.print(num + " ");
    }
}
```

---

### 7.3 Bucket Sort

Bucket Sort distributes elements into a number of buckets, sorts each bucket individually (usually with another sorting algorithm like Insertion Sort), then concatenates all buckets.

#### Key Characteristics
- **Time Complexity**: O(n + k) average case, O(n²) worst case
- **Space Complexity**: O(n + k)
- **Stable**: Depends on the sorting algorithm used for buckets
- **Use Case**: When input is uniformly distributed over a range

#### Pseudocode: BUCKET-SORT

```
BUCKET-SORT(A):
    n = length[A]
    let B[0..n-1] be a new array (array of empty buckets)
    
    // Step 1: Distribute elements into buckets
    for i = 0 to n-1:
        // Insert A[i] into bucket B[floor(n * A[i])]
        // (assuming elements are in [0, 1) range)
    
    // Step 2: Sort each bucket (usually with Insertion Sort)
    for i = 0 to n-1:
        INSERTION-SORT(B[i])
    
    // Step 3: Concatenate all buckets
    concatenate B[0], B[1], ..., B[n-1] into A
```

#### Example: Bucket Sort

**Input**: [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
**All elements in range [0, 1)**

```
Step 1: Distribute into buckets (using floor(n * value))

Index 0: [0.17, 0.21, 0.12]    (0.0-0.29)
Index 1: [0.78]                (0.7-0.79)
Index 2: [0.26, 0.23]         (0.2-0.39)
Index 3: [0.39]               (0.3-0.39)
Index 4: []                   (0.4-0.49)
Index 5: []                   (0.5-0.59)
Index 6: [0.68, 0.72]         (0.6-0.79)
Index 7: []                   (0.7-0.79)
Index 8: [0.78]               (already handled above)
Index 9: [0.94]               (0.9-1.0)

Step 2: Sort each bucket (Insertion Sort)

Index 0: [0.12, 0.17, 0.21]
Index 1: [0.78]
Index 2: [0.23, 0.26]
Index 3: [0.39]
Index 4: []
Index 5: []
Index 6: [0.68, 0.72]
Index 7: []
Index 8: []
Index 9: [0.94]

Step 3: Concatenate

Sorted: [0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94]
```

#### Java Implementation: Bucket Sort

```java
import java.util.ArrayList;
import java.util.Collections;

public class BucketSort {
    
    public static void bucketSort(double[] arr) {
        int n = arr.length;
        
        // Create empty buckets
        @SuppressWarnings("unchecked")
        ArrayList<Double>[] buckets = new ArrayList[n];
        
        for (int i = 0; i < n; i++) {
            buckets[i] = new ArrayList<>();
        }
        
        // Distribute elements into buckets
        for (int i = 0; i < n; i++) {
            int bucketIndex = (int) (n * arr[i]);
            buckets[bucketIndex].add(arr[i]);
        }
        
        // Sort individual buckets using Collections.sort
        for (int i = 0; i < n; i++) {
            Collections.sort(buckets[i]);
        }
        
        // Concatenate all buckets into original array
        int index = 0;
        for (int i = 0; i < n; i++) {
            for (double num : buckets[i]) {
                arr[index++] = num;
            }
        }
    }
    
    public static void main(String[] args) {
        double[] arr = {0.78, 0.17, 0.39, 0.26, 0.72, 
                       0.94, 0.21, 0.12, 0.23, 0.68};
        
        System.out.println("Original: ");
        for (double num : arr) System.out.printf("%.2f ", num);
        
        bucketSort(arr);
        
        System.out.println("\nSorted: ");
        for (double num : arr) System.out.printf("%.2f ", num);
    }
}
```

---

## 8. Comparison of Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| **HeapSort** | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| **Counting Sort** | O(n + k) | O(n + k) | O(n + k) | O(n + k) | Yes |
| **Radix Sort** | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | O(n + k) | Yes |
| **Bucket Sort** | O(n + k) | O(n + k) | O(n²) | O(n + k) | Yes |
| **QuickSort** | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| **MergeSort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |

### When to Use Which Algorithm

1. **General Purpose**: QuickSort, MergeSort, HeapSort
2. **Integer Data with Limited Range**: Counting Sort
3. **Fixed-length Strings/Numbers**: Radix Sort
4. **Uniformly Distributed Floats**: Bucket Sort
5. **Memory Constrained**: HeapSort (O(1) space)
6. **Stability Required**: MergeSort, Counting Sort, Radix Sort

---

## 9. Key Takeaways

### HeapSort
- ✅ Uses a **binary heap** data structure (complete binary tree with heap property)
- ✅ Achieves **O(n log n)** time complexity in all cases (best, average, worst)
- ✅ Is an **in-place** sorting algorithm with **O(1)** auxiliary space
- ❌ **Not stable** - equal elements may change relative order
- ✅ Excellent for **priority queue** implementations

### Linear Time Sorting
- ✅ Can achieve **O(n)** time complexity under specific conditions
- ✅ **Counting Sort**: Works for integers with limited range; stable
- ✅ **Radix Sort**: Works for fixed-length keys (integers, strings); stable
- ✅ **Bucket Sort**: Works when input is uniformly distributed; average O(n)
- ❌ Not comparison-based, so bypass the Ω(n log n) lower bound

### Delhi University NEP 2024 UGCF Important Points
- Understand heapify operation and its recursive nature
- Be able to trace through HeapSort step-by-step
- Know when to apply each linear-time sorting algorithm
- Remember that stability matters in certain applications
- Practice implementing all algorithms in code

---

## 10. Practice Questions

### Multiple Choice Questions

**Q1. What is the time complexity of building a max-heap from an unsorted array of n elements?**

A) O(n)  
B) O(n log n)  
C) O(log n)  
D) O(n²)

**Answer: A) O(n)**  
*Explanation: Building a max-heap takes linear time O(n) because of the properties of the binary tree structure.*

---

**Q2. In a max-heap, the parent node is:**

A) Greater than or equal to both children  
B) Smaller than or equal to both children  
C) Greater than at least one child  
D) Always greater than both children

**Answer: A) Greater than or equal to both children**  
*Explanation: This is the definition of a max-heap property.*

---

**Q3. Which sorting algorithm is NOT stable?**

A) Counting Sort  
B) MergeSort  
C) HeapSort  
D) Radix Sort

**Answer: C) HeapSort**  
*Explanation: HeapSort is not stable because elements may change relative order during the heapify operations.*

---

**Q4. The auxiliary space complexity of HeapSort is:**

A) O(n)  
B) O(log n)  
C) O(1)  
D) O(n log n)

**Answer: C) O(1)**  
*Explanation: HeapSort is an in-place sorting algorithm requiring only O(1) auxiliary space.*

---

**Q5. Which linear time sorting algorithm requires the input to be uniformly distributed for best performance?**

A) Counting Sort  
B) Radix Sort  
C) Bucket Sort  
D) All of them

**Answer: C) Bucket Sort**  
*Explanation: Bucket Sort achieves O(n) average case when elements are uniformly distributed across the range.*

---

### Short Answer Questions

**Q6. Explain why HeapSort is considered an in-place sorting algorithm.**

HeapSort is considered in-place because it only requires O(1) auxiliary space beyond the input array. All operations (building the heap, swapping elements, heapify) are performed within the original array without creating additional data structures proportional to input size.

---

**Q7. Why is HeapSort not stable? Give an example.**

HeapSort is not stable because during the heapify operations, elements with equal keys may change their relative order. For example, consider an array [2a, 2b, 1] where 2a appears before 2b. After heapification and extraction, we might get [1, 2b, 2a], where 2a and 2b have swapped positions.

---

**Q8. When should Counting Sort be preferred over HeapSort?**

Counting Sort should be preferred when:
- The range of input values (k) is not significantly larger than n
- Sorting integers or data that can be mapped to integers
- Stability is required
- Time complexity matters more than space

---

### Long Answer Questions

**Q9. Trace through the HeapSort algorithm step-by-step for the array: [5, 3, 8, 4, 1, 6, 2]**

*Solution:*

**Step 1: Build Max-Heap**
- Start from index n/2 - 1 = 2
- Heapify index 2 (value 8): Already heap
- Heapify index 1 (value 3): Swap with 5 → [5, 5, 8, 4, 1, 6, 2] → [5, 5, 8, 4, 1, 6, 2]
- Heapify index 0 (value 5): Swap with 8 → [8, 5, 5, 4, 1, 6, 2]
- Continue heapify: [8, 5, 6, 4, 1, 5, 2]

Final Max-Heap: [8, 5, 6, 4, 1, 5, 2]

**Step 2: Extract elements**
- Extract 8: Swap with 2 → [2, 5, 6, 4, 1, 5, 8] → Heapify → [6, 5, 5, 4, 1, 2, 8]
- Extract 6: Swap with 2 → [2, 5, 5, 4, 1, 6, 8] → Heapify → [5, 5, 2, 4, 1, 6, 8]
- Extract 5: Swap with 1 → [1, 5, 2, 4, 5, 6, 8] → Heapify → [5, 4, 2, 1, 5, 6, 8]
- Extract 5: Swap with 1 → [1, 4, 2, 5, 5, 6, 8] → Heapify → [4, 1, 2, 5, 5, 6, 8]
- Extract 4: Swap with 5 → [5, 1, 2, 4, 5, 6, 8] → Heapify → [2, 1, 4, 5, 5, 6, 8]
- Extract 2: Swap with 1 → [1, 2, 4, 5, 5, 6, 8] → Heapify → [1, 2, 4, 5, 5, 6, 8]

**Sorted Array**: [1, 2, 4, 5, 5, 6, 8]

---

**Q10. Compare and contrast HeapSort and QuickSort. Under what circumstances would you choose one over the other?**

*Solution:*

| Aspect | HeapSort | QuickSort |
|--------|----------|-----------|
| Time (Worst) | O(n log n) | O(n²) |
| Time (Average) | O(n log n) | O(n log n) |
| Space | O(1) | O(log n) for recursion |
| Stability | Not stable | Not stable |
| Cache efficiency | Poor | Good |

**Choose QuickSort when:**
- Average case performance is acceptable
- Cache efficiency matters (sequential memory access)
- Working with arrays in memory

**Choose HeapSort when:**
- Guaranteed O(n log n) time is required
- Memory is severely constrained (O(1) space)
- Implementing priority queues

---

## References

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
2. Sahni, S. (2016). *Data Structures, Algorithms and Applications in Java* (2nd ed.). Universities Press.
3. Delhi University NEP 2024 UGCF Syllabus - Design and Analysis of Algorithms.

---

*This study material is prepared for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF curriculum.*