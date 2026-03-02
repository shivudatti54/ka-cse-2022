# Time Complexity Analysis

## A Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction to Time Complexity Analysis

### 1.1 What is Time Complexity?

Time complexity is a fundamental concept in computer science that measures the amount of time an algorithm takes to complete as a function of the input size. It provides a theoretical estimate of the execution time without relying on hardware-specific factors like processor speed or programming language efficiency. Understanding time complexity is crucial for designing efficient algorithms, especially when dealing with large datasets where performance differences between algorithms can be dramatic.

In the context of the Delhi University BSc (Hons) Computer Science curriculum (NEP 2024 UGCF), time complexity analysis forms a core component of the Data Structures subject. This topic helps students evaluate and compare algorithms,选择最优解决方案, and understand how algorithm design impacts software performance in real-world applications.

### 1.2 Real-World Relevance

Consider a scenario where you are developing a search feature for an e-commerce platform with millions of products. If your search algorithm takes O(n²) time, searching through 1 million products could require up to 1 trillion operations. However, with an O(n log n) algorithm, this reduces to approximately 20 million operations—a massive difference in user experience. Similarly, when processing big data, running an inefficient algorithm can make the difference between completing a task in seconds versus days.

In practical software development, time complexity analysis helps:
- **Predict scalability**: How will the algorithm perform as data grows?
- **Optimize resources**: Reduce server costs and improve response times
- **Make informed design choices**: Select appropriate data structures and algorithms
- **Pass technical interviews**: Core topic in placement examinations

---

## 2. Asymptotic Notation

Asymptotic notation provides a standardized language to describe the efficiency of algorithms. It captures the growth rate of an algorithm's time or space requirements as the input size approaches infinity.

### 2.1 Big-O Notation (O-notation) — Upper Bound

Big-O notation represents the worst-case scenario, describing the upper bound on the time an algorithm can take.

**Formal Definition:** f(n) = O(g(n)) if there exist positive constants c and n₀ such that 0 ≤ f(n) ≤ c × g(n) for all n ≥ n₀

**Intuitive Meaning:** "The algorithm will not take more time than..."

```python
# Example: Linear Search
def linear_search(arr, target):
    for element in arr:  # This loop runs at most n times
        if element == target:
            return True
    return False

# Time Complexity: O(n) — worst case is searching all elements
```

### 2.2 Big-Omega Notation (Ω-notation) — Lower Bound

Omega notation represents the best-case scenario, describing the lower bound on the time.

**Formal Definition:** f(n) = Ω(g(n)) if there exist positive constants c and n₀ such that 0 ≤ c × g(n) ≤ f(n) for all n ≥ n₀

**Intuitive Meaning:** "The algorithm will take at least..."

For the linear search example above:
- Best case: Ω(1) — element found at first position
- Worst case: Ω(n) — element not found or at last position

### 2.3 Big-Theta Notation (Θ-notation) — Tight Bound

Theta notation provides a tight bound, meaning the algorithm's time is both O(g(n)) and Ω(g(n)).

**Formal Definition:** f(n) = Θ(g(n)) if there exist positive constants c₁, c₂, and n₀ such that 0 ≤ c₁ × g(n) ≤ f(n) ≤ c₂ × g(n) for all n ≥ n₀

**Intuitive Meaning:** "The algorithm takes exactly..."

**Example:** Accessing an array element by index is Θ(1) — constant time regardless of array size.

### 2.4 Little-O Notation (o-notation)

Little-o represents an upper bound that is not tight.

**Formal Definition:** f(n) = o(g(n)) if for all c > 0, there exists n₀ such that 0 ≤ f(n) < c × g(n) for all n ≥ n₀

**Example:** n = o(n²) but n ≠ o(n)

### 2.5 Little-Omega Notation (ω-notation)

Little-omega represents a lower bound that is not tight.

**Formal Definition:** f(n) = ω(g(n)) if for all c > 0, there exists n₀ such that 0 ≤ c × g(n) < f(n) for all n ≥ n₀

**Example:** n² = ω(n) but n² ≠ ω(n²)

---

## 3. Common Time Complexities

Understanding common time complexities helps in quick algorithm analysis and comparison.

### 3.1 Complexity Hierarchy (From Best to Worst)

| Complexity | Name | Example Algorithm |
|------------|------|-------------------|
| O(1) | Constant | Array index access, Hash table lookup |
| O(log n) | Logarithmic | Binary search, Binary tree operations |
| O(n) | Linear | Linear search, Traversing an array |
| O(n log n) | Linearithmic | Merge sort, Heap sort, Quick sort (average) |
| O(n²) | Quadratic | Bubble sort, Insertion sort, Nested loops |
| O(n³) | Cubic | Floyd-Warshall algorithm, Naive matrix multiplication |
| O(2^n) | Exponential | Recursive Fibonacci, Subset generation |
| O(n!) | Factorial | Permutation generation, Traveling Salesman (naive) |

### 3.2 Detailed Breakdown with Visual Growth

```python
# Let's visualize the growth rates
# Assuming 1 operation takes 1 microsecond

# n = 10
# O(1):     1 µs
# O(log n): 3.3 µs
# O(n):     10 µs
# O(n log n): 33 µs
# O(n²):    100 µs
# O(2^n):   1,024 µs (~1ms)
# O(n!):    3.6 million µs (~3.6s)

# n = 20
# O(1):     1 µs
# O(log n): 4.3 µs
# O(n):     20 µs
# O(n log n): 86 µs
# O(n²):    400 µs
# O(2^n):   1,048,576 µs (~1s)
# O(n!):    2.4 × 10^18 µs (~7.7 years!)
```

---

## 4. Loop Analysis

Loop analysis is the most common technique for determining time complexity in practice.

### 4.1 Simple Loops

```python
# Example 1: Single loop
def sum_array(arr):
    total = 0
    for i in range(len(arr)):  # Executes n times
        total += arr[i]
    return total

# Time Complexity: O(n)
```

### 4.2 Nested Loops

```python
# Example 2: Nested loops - O(n²)
def print_pairs(arr):
    n = len(arr)
    for i in range(n):         # Runs n times
        for j in range(n):     # Runs n times for each i
            print(arr[i], arr[j])

# Time Complexity: O(n × n) = O(n²)

# Example 3: Nested loops with different ranges - O(n²)
def triangle_pattern(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1):
            print(arr[j], end=" ")
        print()

# Time Complexity: n + (n-1) + (n-2) + ... + 1 = n(n+1)/2 = O(n²)
```

### 4.3 Loops with Variable Increments

```python
# Example 4: Loop with logarithmic increment - O(log n)
def binary_search_example(arr, target):
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

# Time Complexity: O(log n) — search space halves each iteration

# Example 5: Loop with doubling - O(log n)
def power_of_two(n):
    result = 1
    while result < n:
        result *= 2
    return result

# Time Complexity: O(log n) — doubles until exceeding n
```

### 4.4 Consecutive Statements

```python
# Example 6: Consecutive operations - Sum of complexities
def consecutive_example(n):
    # Statement 1: O(1)
    print("Hello")
    
    # Statement 2: O(n)
    for i in range(n):
        print(i)
    
    # Statement 3: O(n²)
    for i in range(n):
        for j in range(n):
            print(i, j)

# Time Complexity: O(1) + O(n) + O(n²) = O(n²)
# (Dominant term wins)
```

---

## 5. Recurrence Relations

Recurrence relations define sequences recursively and are essential for analyzing recursive algorithms.

### 5.1 What is a Recurrence Relation?

A recurrence relation expresses the time complexity T(n) of a problem of size n in terms of smaller subproblems.

**Common Examples:**

1. **Binary Search:** T(n) = T(n/2) + O(1)
2. **Merge Sort:** T(n) = 2T(n/2) + O(n)
3. **Linear Search (recursive):** T(n) = T(n-1) + O(1)

### 5.2 Substitution Method

This method involves guessing the solution and proving it correct by induction.

**Example:** Solve T(n) = 2T(n/2) + n, T(1) = 1

**Solution:**
- Guess: T(n) = n log n + n
- Base case: T(1) = 1 ✓
- Assume T(k) = k log k + k for all k < n
- Prove for n: T(n) = 2T(n/2) + n
  = 2[(n/2)log(n/2) + n/2] + n
  = n(log(n/2)) + n + n
  = n(log n - log 2) + 2n
  = n log n - n + 2n
  = n log n + n ✓

**Answer:** T(n) = Θ(n log n)

### 5.3 Recursion Tree Method

This visual method breaks down the recurrence into levels.

**Example:** T(n) = 2T(n/2) + n

```
Level 0: n
Level 1: 2 × (n/2) = n
Level 2: 4 × (n/4) = n
...
Level log n: n × 1 = n
```

Total: n × (log n + 1) = n log n + n = **Θ(n log n)**

### 5.4 Master Theorem

The Master Theorem provides a direct solution for recurrences of the form:
> T(n) = aT(n/b) + f(n)

Where a ≥ 1, b > 1, and f(n) is asymptotically positive.

**Cases:**
1. If f(n) = O(n^log_b(a - ε)), then T(n) = Θ(n^log_b(a))
2. If f(n) = Θ(n^log_b(a)), then T(n) = Θ(n^log_b(a) log n)
3. If f(n) = Ω(n^log_b(a + ε)), then T(n) = Θ(f(n))

**Examples:**

| Recurrence | a | b | n^log_b(a) | Result |
|------------|---|---|------------|--------|
| T(n) = 2T(n/2) + n | 2 | 2 | n | Case 2: Θ(n log n) |
| T(n) = T(n/2) + O(1) | 1 | 2 | n^0 = 1 | Case 2: Θ(log n) |
| T(n) = 2T(n/2) + n² | 2 | 2 | n | Case 3: Θ(n²) |

---

## 6. Best, Average, and Worst Case Analysis

Different inputs can cause the same algorithm to have vastly different running times. We analyze all three cases for a complete picture.

### 6.1 Definitions

- **Best Case:** The most favorable input that results in minimum running time
- **Worst Case:** The least favorable input that results in maximum running time
- **Average Case:** Expected running time over all possible inputs (requires statistical assumptions)

### 6.2 Linear Search Analysis

```python
def linear_search(arr, target):
    """
    Search for target in unsorted array
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Element found
    return -1  # Element not found
```

**Analysis:**
- **Best Case:** Ω(1) — element found at first position
- **Worst Case:** O(n) — element not found or at last position
- **Average Case:** Θ(n) — assuming element is equally likely to be at any position or not present

For a successful search: (1 + 2 + 3 + ... + n)/n = (n+1)/2 = Θ(n)
For unsuccessful search: n comparisons = Θ(n)

### 6.3 Quick Sort Analysis

```python
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

**Analysis:**
- **Best Case:** Ω(n log n) — pivot always splits array in half
- **Worst Case:** O(n²) — pivot is always smallest or largest element
- **Average Case:** Θ(n log n) — random pivot selection

---

## 7. Detailed Examples with Code

### 7.1 Example 1: Bubble Sort — O(n²) Time Complexity

Bubble Sort is a simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    return arr

# Time Complexity Analysis:
# Outer loop: runs n times
# Inner loop: runs n-1, n-2, ..., 1 times
# Total: n + (n-1) + (n-2) + ... + 1 = n(n+1)/2 = O(n²)

# Best Case: O(n) — already sorted (with optimization)
# Worst Case: O(n²) — reverse sorted
# Average Case: O(n²)
```

**Practical Example:**

```python
# Testing Bubble Sort
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", numbers)
sorted_numbers = bubble_sort(numbers.copy())
print("Sorted array:", sorted_numbers)
```

### 7.2 Example 2: Binary Search — O(log n) Time Complexity

Binary Search is an efficient algorithm for finding an item in a sorted array by repeatedly dividing the search interval in half.

```python
def binary_search(arr, target):
    """
    Iterative Binary Search
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Calculate middle index (avoids overflow)
        mid = left + (right - left) // 2
        
        # Check if target is at mid
        if arr[mid] == target:
            return mid
        
        # If target greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target smaller, ignore right half
        else:
            right = mid - 1
    
    # Element not found
    return -1

def binary_search_recursive(arr, target, left=None, right=None):
    """
    Recursive Binary Search
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion stack
    """
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    
    # Base case: element not found
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Testing Binary Search
sorted_numbers = [2, 3, 4, 10, 40, 50, 60, 70]
target = 10

result = binary_search(sorted_numbers, target)
print(f"Element found at index: {result}")  # Output: 3
```

**Comparison with Linear Search:**

| n | Linear Search (O(n)) | Binary Search (O(log n)) |
|---|---------------------|-------------------------|
| 10 | 10 operations | 4 operations |
| 100 | 100 operations | 7 operations |
| 1,000 | 1,000 operations | 10 operations |
| 1,000,000 | 1,000,000 operations | 20 operations |

---

## 8. Key Takeaways

1. **Asymptotic Notation** provides standardized ways to express algorithm efficiency:
   - **O(n)**: Upper bound (worst case)
   - **Ω(n)**: Lower bound (best case)
   - **Θ(n)**: Tight bound (exact growth rate)

2. **Common Complexities** in increasing order:
   O(1) → O(log n) → O(n) → O(n log n) → O(n²) → O(2^n) → O(n!)

3. **Loop Analysis** techniques:
   - Single loop: O(n)
   - Nested loops: Multiply complexities
   - Halving search space: O(log n)
   - Dominant term wins in sums

4. **Recurrence Relations** can be solved using:
   - Substitution method
   - Recursion tree method
   - Master Theorem (for divide-and-conquer)

5. **Case Analysis** is essential:
   - Best case, worst case, and average case can differ significantly
   - Always consider all three for complete analysis

6. **Algorithm Choice Matters**: The difference between O(n²) and O(n log n) becomes enormous for large inputs.

7. **Delhi University Context**: This topic is essential for:
   - Semester examinations (Theory Paper)
   - Practical examinations (algorithm implementation)
   - Placement tests and competitive exams

---

## 9. Assessment Section

### 9.1 Multiple Choice Questions (MCQs)

**Level 1: Easy**

1. What is the time complexity of accessing an element in an array by index?
   - a) O(1)
   - b) O(n)
   - c) O(log n)
   - d) O(n²)
   
   **Answer: a) O(1)**

2. Which sorting algorithm has the worst-case time complexity of O(n²)?
   - a) Merge Sort
   - b) Heap Sort
   - c) Quick Sort
   - d) Bubble Sort
   
   **Answer: d) Bubble Sort**

**Level 2: Medium**

3. What is the time complexity of the following code?
   ```python
   for i in range(n):
       for j in range(i, n):
           print(i, j)
   ```
   - a) O(n)
   - b) O(n²)
   - c) O(n³)
   - d) O(n log n)
   
   **Answer: b) O(n²)**

4. Binary Search has a time complexity of:
   - a) O(n)
   - b) O(n²)
   - c) O(log n)
   - d) O(1)
   
   **Answer: c) O(log n)**

5. Which notation represents the average-case analysis?
   - a) Big-O
   - b) Big-Omega
   - c) Big-Theta
   - d) Little-O
   
   **Answer: c) Big-Theta**

**Level 3: Hard**

6. Using the Master Theorem, solve T(n) = 3T(n/2) + n²:
   - a) Θ(n²)
   - b) Θ(n^log₂³)
   - c) Θ(n² log n)
   - d) Θ(n^log₂³ × log n)
   
   **Answer: a) Θ(n²)**

7. What is the time complexity of the recurrence: T(n) = T(n-1) + O(1)?
   - a) O(1)
   - b) O(log n)
   - c) O(n)
   - d) O(n²)
   
   **Answer: c) O(n)**

8. Consider the following code and identify the tightest bound:
   ```python
   i = n
   while i > 1:
       i = i // 2
   ```
   - a) O(1)
   - b) O(log n)
   - c) O(n)
   - d) O(n log n)
   
   **Answer: b) O(log n)**

9. What is the best, worst, and average case time complexity of Quick Sort respectively?
   - a) O(n log n), O(n²), O(n²)
   - b) O(n log n), O(n log n), O(n²)
   - c) O(n log n), O(n²), O(n log n)
   - d) O(n), O(n²), O(n log n)
   
   **Answer: c) O(n log n), O(n²), O(n log n)**

10. The time complexity of accessing the middle element in a singly linked list is:
    - a) O(1)
    - b) O(n)
    - c) O(log n)
    - d) O(n²)
    
    **Answer: b) O(n)** (must traverse)

### 9.2 Flashcards

**Card 1:**
> **Q:** What is Big-O notation used for?
> **A:** Big-O notation describes the upper bound (worst-case) time complexity of an algorithm.

**Card 2:**
> **Q:** What is the time complexity of merging two sorted arrays of size n?
> **A:** Θ(n) — linear time, as each element is processed exactly once.

**Card 3:**
> **Q:** Why is O(n²) worse than O(n log n)?
> **A:** For n = 1,000,000, n² = 10¹² operations while n log n ≈ 20 million operations — a 50,000× difference.

**Card 4:**
> **Q:** What does it mean when we say T(n) = Θ(f(n))?
> **A:** It means f(n) is both an upper bound and lower bound on T(n), providing a tight asymptotic characterization.

**Card 5:**
> **Q:** What is the time complexity of the recursive Fibonacci calculation?
> **A:** O(2^n) — exponential, as each call generates two more calls, creating a binary tree of height n.

**Card 6:**
> **Q:** How does the Master Theorem help in analyzing algorithms?
> **A:** It provides a direct solution for recurrences of the form T(n) = aT(n/b) + f(n), which appear in divide-and-conquer algorithms.

**Card 7:**
> **Q:** What is the space complexity of recursive binary search?
> **A:** O(log n) — due to the recursion call stack depth.

**Card 8:**
> **Q:** When analyzing algorithms, why do we ignore constant factors?
> **A:** For large inputs, the growth rate dominates. Constants depend on hardware and implementation, while asymptotic behavior determines scalability.

### 9.3 Short Answer Questions

1. **Explain the difference between O, Ω, and Θ notations with examples.**

2. **Analyze the time complexity of the following code segment:**
   ```python
   for i in range(n):
       j = n
       while j > 0:
           j = j // 2
   ```

3. **Using the Master Theorem, determine the time complexity of Merge Sort.**

4. **Explain why Quick Sort has O(n²) worst-case but is still preferred over O(n log n) algorithms in practice.**

5. **What is amortized analysis? Give an example of an algorithm where amortized analysis is useful.**

### 9.4 Long Answer Questions

1. **Derive the time complexity of Insertion Sort by analyzing its loops. Also discuss its best, average, and worst-case scenarios.**

2. **Solve the recurrence relation T(n) = 3T(n/4) + n² using the Master Theorem and verify your answer using the recursion tree method.**

3. **Compare and contrast Linear Search and Binary Search. Under what circumstances would you choose one over the other?**

4. **Write a detailed note on asymptotic notations, explaining their mathematical definitions and practical significance in algorithm analysis.**

---

## 10. References

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.

2. Dasgupta, S., Papadimitriou, C. H., & Vazirani, U. V. (2006). *Algorithms*. McGraw-Hill.

3. Delhi University BSc (Hons) Computer Science Syllabus — NEP 2024 UGCF.

4. Sedgewick, R. (2011). *Algorithms* (4th ed.). Addison-Wesley.

---

*This study material is prepared for BSc (Hons) Computer Science students at Delhi University as per the NEP 2024 UGCF curriculum.*