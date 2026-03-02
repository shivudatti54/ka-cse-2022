# Heapsort and Randomized Algorithms
## Ge7A: Design and Analysis of Algorithms
### BSc Physical Science (CS) - Delhi University, NEP 2024

---

## 1. Introduction

Sorting and selection are fundamental operations in computer science, serving as building blocks for more complex algorithms. In this study material, we explore two powerful algorithmic paradigms: **Heapsort**, a comparison-based sorting algorithm with guaranteed O(n log n) time complexity, and **Randomized Algorithms**, which incorporate randomness to achieve better average-case performance or simplicity.

### Real-World Relevance

- **Operating Systems**: Task scheduling often uses heap-based priority queues
- **Databases**: Order-by queries utilize efficient sorting algorithms
- **Graph Algorithms**: Dijkstra's shortest path uses min-heaps
- **Randomized Load Balancing**: Web servers use random selection for distributing requests
- **Gaming**: Randomized algorithms power AI decision-making and procedural content generation

---

## 2. Heaps and Heapsort

### 2.1 What is a Heap?

A **heap** is a complete binary tree data structure that satisfies the **heap property**:

- **Max-Heap**: Parent node ≥ Children nodes
- **Min-Heap**: Parent node ≤ Children nodes

The tree is **complete**, meaning all levels are filled except possibly the last, which is filled from left to right.

### 2.2 Heap Representation

Heaps are typically implemented using **arrays** for efficient space usage:

```
Index:     0   1   2   3   4   5   6
Array:    [50][30][20][15][10][8][5]
```

**Parent-Child Relationships** (for index i):
- Parent: floor((i-1)/2)
- Left Child: 2i + 1
- Right Child: 2i + 2

### 2.3 Heap Operations

#### Max-Heapify

The `heapify` operation maintains the max-heap property. If a node violates the heap property, we "sink" it down by swapping with the larger child.

```python
def max_heapify(arr, n, i):
    """
    Heapify subtree rooted at index i.
    n is the size of the heap.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Check if left child exists and is greater
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check if right child exists and is greater
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)
```

#### Build Max-Heap

Convert an unsorted array into a max-heap:

```python
def build_max_heap(arr):
    n = len(arr)
    
    # Start from last non-leaf node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)
    
    return arr
```

### 2.4 Heapsort Algorithm

Heapsort combines the heap property with in-place sorting:

```python
def heapsort(arr):
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        
        # Call max heapify on reduced heap
        max_heapify(arr, i, 0)
    
    return arr
```

### 2.5 Heapsort Example

Let's trace through heapsort with the array `[4, 10, 3, 5, 1]`:

**Step 1: Build Max-Heap**
```
Initial array: [4, 10, 3, 5, 1]

After building max-heap:
        10
       /  \
      5    3
     / \
    4   1

Array: [10, 5, 3, 4, 1]
```

**Step 2: Sort**
- Swap 10 and 1: `[1, 5, 3, 4, 10]` → Heapify: `[5, 4, 3, 1, 10]`
- Swap 5 and 1: `[1, 4, 3, 5, 10]` → Heapify: `[4, 1, 3, 5, 10]`
- Swap 4 and 3: `[3, 1, 4, 5, 10]` → Heapify: `[3, 1, 4, 5, 10]`
- Swap 3 and 1: `[1, 3, 4, 5, 10]`

**Sorted Array**: `[1, 3, 4, 5, 10]`

### 2.6 Time Complexity Analysis

| Operation | Time Complexity |
|-----------|-----------------|
| Heapify   | O(log n)        |
| Build Heap| O(n)            |
| Heapsort  | O(n log n)      |

**Detailed Analysis**:

1. **Build Max-Heap**: O(n) - Each heapify operation takes O(log n), but we process n/2 nodes
2. **Extraction Phase**: We perform n-1 extractions, each taking O(log n)

**Space Complexity**: O(1) - In-place sorting

**Stability**: Heapsort is **not stable** - equal elements may change relative order.

---

## 3. Randomized Algorithms

### 3.1 Introduction

A **randomized algorithm** uses random numbers to influence its behavior. Unlike deterministic algorithms, randomized algorithms can produce different outputs for the same input.

**Why Use Randomness?**:
- Simpler implementations
- Better average-case performance
- Avoid worst-case scenarios
- Solve problems with no efficient deterministic solution

### 3.2 Types of Randomized Algorithms

#### Monte Carlo Algorithms

- Always run in fixed time
- May produce incorrect answers with small probability
- Example: Randomized QuickSort, Monte Carlo integration

#### Las Vegas Algorithms

- Always produce correct results
- Running time is random (may vary)
- Example: Randomized QuickSelect, Randomized Quicksort

### 3.3 Randomized Quicksort

Standard Quicksort can degrade to O(n²) with bad pivot selection. **Randomized Quicksort** randomly selects the pivot to avoid worst-case behavior.

```python
import random

def randomized_partition(arr, low, high):
    # Random pivot selection
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

def quicksort(arr):
    randomized_quicksort(arr, 0, len(arr) - 1)
    return arr
```

### 3.4 Probabilistic Analysis

#### Expected Running Time of Randomized Quicksort

**Key Insight**: The expected running time is O(n log n), regardless of input distribution.

**Proof Outline**:
- Each element has equal probability of being chosen as pivot
- After partitioning, pivot is in its final sorted position
- Expected depth of recursion tree: O(log n)
- Each level processes n elements: O(n)
- Therefore: O(n log n)

```
Random Pivot Selection:
P(element i is pivot) = 1/n

Expected comparisons per level = n - 1
Expected number of levels = log n (base e)
Expected time = O(n log n)
```

#### Analysis of Randomized QuickSelect

QuickSelect finds the k-th smallest element:

```python
import random

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    if low == high:
        return arr[low]
    
    pivot_index = randomized_partition(arr, low, high)
    
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, high, k)
```

**Expected Time**: O(n) - With high probability, we reduce the problem size significantly with each partition.

### 3.5 Comparison: Deterministic vs Randomized

| Aspect | Deterministic | Randomized |
|--------|---------------|------------|
| Running Time | O(n log n) worst-case | O(n log n) expected |
| Pivot Selection | Fixed (last/first element) | Random |
| Predictability | Always same output | May vary |
| Implementation | Slightly complex | Simpler often |
| Probability of failure | 0% | ~0% (Las Vegas) |

---

## 4. Monte Carlo Example: Randomized Matrix Multiplication Verification

```python
import random

def verify_matrix_multiply(A, B, C, num_tests=20):
    """
    Monte Carlo algorithm to verify A × B = C
    """
    n = len(A)
    
    for _ in range(num_tests):
        # Generate random vector
        x = [random.randint(0, 1) for _ in range(n)]
        
        # Compute (A × B) × x
        Bx = [sum(B[i][j] * x[j] for j in range(n)) for i in range(n)]
        ABx = [sum(A[i][j] * Bx[j] for j in range(n)) for i in range(n)]
        
        # Compute C × x
        Cx = [sum(C[i][j] * x[j] for j in range(n)) for i in range(n)]
        
        if ABx != Cx:
            return False  # Definitely incorrect
    
    return True  # Probably correct
```

**Error Probability**: If C ≠ A×B, the algorithm returns false with probability ≥ 1 - 1/2^t where t is the number of tests.

---

## 5. Key Takeaways

### Heapsort
- Heap is a complete binary tree with heap property (max-heap or min-heap)
- Heapsort uses O(n) time to build heap and O(n log n) for sorting
- In-place sorting with O(1) auxiliary space
- Not stable but guarantees O(n log n) worst-case performance
- Priority queues are efficiently implemented using heaps

### Randomized Algorithms
- Randomized algorithms use randomness to improve average-case performance
- **Monte Carlo**: Fixed time, may produce incorrect results (probability of error can be made arbitrarily small)
- **Las Vegas**: Always correct, running time is random
- Randomized Quicksort achieves O(n log n) expected time regardless of input
- Probabilistic analysis provides guarantees on average performance

---

## 6. Practice Questions (MCQs)

### Level 1: Basic

1. **In a max-heap, the parent node is:**
   - a) Greater than or equal to children
   - b) Less than or equal to children
   - c) Always greater than children
   - d) Always smaller than children
   - **Answer: a)**

2. **The time complexity of building a max-heap from an unsorted array is:**
   - a) O(n)
   - b) O(n log n)
   - c) O(log n)
   - d) O(n²)
   - **Answer: a)**

3. **Randomized Quicksort is an example of:**
   - a) Monte Carlo algorithm
   - b) Las Vegas algorithm
   - c) Deterministic algorithm
   - d) Greedy algorithm
   - **Answer: b)**

### Level 2: Intermediate

4. **Which of the following is NOT a property of heapsort?**
   - a) In-place sorting
   - b) Stable sorting
   - c) O(n log n) time complexity
   - d) Uses heap data structure
   - **Answer: b)**

5. **In a binary heap stored in an array, for index i, the right child is at index:**
   - a) 2i
   - b) 2i + 1
   - c) 2i + 2
   - d) floor((i-1)/2)
   - **Answer: c)**

6. **The expected time complexity of randomized quicksort is:**
   - a) O(n)
   - b) O(n log n)
   - c) O(n²)
   - d) O(log n)
   - **Answer: b)**

### Level 3: Advanced

7. **A Las Vegas algorithm always:**
   - a) Runs in expected polynomial time
   - b) Produces correct results
   - c) Has bounded error probability
   - d) Uses random sampling
   - **Answer: b)**

8. **In randomized quicksort, the probability that a given element is chosen as pivot is:**
   - a) 1/n²
   - b) 1/n
   - c) 1/2
   - d) Depends on input
   - **Answer: b)**

9. **Which algorithm is used to find the k-th smallest element in expected O(n) time?**
   - a) HeapSort
   - b) Randomized QuickSelect
   - c) Binary Search
   - d) MergeSort
   - **Answer: b)**

10. **In Monte Carlo algorithms, reducing error probability requires:**
    - a) More random bits
    - b) More iterations/tests
    - c) Deterministic verification
    - d) Larger input size
    - **Answer: b)**

---

## 7. Flashcards

| Term | Definition |
|------|------------|
| **Heap** | Complete binary tree satisfying heap property (parent ≥ children for max-heap) |
| **Heapify** | Process to maintain heap property by moving element down the tree |
| **Heapsort** | Comparison-based sorting using binary heap, O(n log n) time |
| **Randomized Algorithm** | Algorithm using random numbers to influence computation |
| **Monte Carlo** | Randomized algorithm with fixed running time, may produce wrong answer |
| **Las Vegas** | Randomized algorithm that always produces correct result, variable time |
| **Expected Time** | Average running time over all possible random choices |
| **Probabilistic Analysis** | Mathematical analysis of algorithm performance using probability theory |
| **Pivot** | Element used to partition array in Quicksort |
| **QuickSelect** | Algorithm to find k-th smallest element using partitioning |

---

## 8. References and Syllabus Alignment

This content covers the following topics from **Ge7A Design and Analysis of Algorithms** (Delhi University, NEP 2024):

1. **Sorting Algorithms**: Heapsort, Heap data structure, Time complexity analysis
2. **Divide and Conquer**: Quicksort, Randomized versions
3. **Algorithmic Paradigms**: Randomized algorithms, Probabilistic analysis
4. **Algorithm Design Techniques**: Comparison-based sorting, In-place sorting

**Suggested Reading**:
- Cormen, Leiserson, Rivest, Stein - *Introduction to Algorithms*
- Goodrich, Tamassia - *Data Structures and Algorithms in Python*
- Rajagopalan - *Design and Analysis of Algorithms* (For DU syllabus)

---

*Study Material prepared for BSc Physical Science (CS), Delhi University, NEP 2024*