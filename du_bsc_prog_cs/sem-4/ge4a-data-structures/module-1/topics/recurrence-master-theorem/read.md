# Recurrence Master Theorem: Comprehensive Study Material

## Subject: Ge4A Data Structures | BSc Physical Science (CS) — Delhi University NEP 2024

---

## 1. Introduction

The **Master Theorem** is one of the most powerful tools in algorithm analysis, providing a systematic way to solve recurrence relations that arise in divide-and-conquer algorithms. For students pursuing BSc Physical Science (CS) at Delhi University under NEP 2024, understanding this theorem is essential for analyzing the time complexity of recursive algorithms—a core competency in the Ge4A Data Structures syllabus.

### What is a Recurrence Relation?

A **recurrence relation** is a mathematical equation that defines a sequence recursively—each term is defined in terms of previous terms. In algorithm analysis, recurrences express the running time of algorithms that call themselves (recursive algorithms).

**Example:** The recurrence for merge sort is:
```
T(n) = 2T(n/2) + O(n)
```
This states that solving a problem of size `n` requires:
- Solving two subproblems of size `n/2` each
- Plus `O(n)` time for merging the results

### Real-World Relevance

Master Theorem finds application in analyzing many practical algorithms:

- **Search algorithms**: Binary Search, Exponential Search
- **Sorting algorithms**: Merge Sort, Quick Sort, Heap Sort
- **Matrix operations**: Strassen's Matrix Multiplication
- **Data structures**: Balanced BST operations, Segment Trees
- **Graph algorithms**: FFT (Fast Fourier Transform), Karatsuba multiplication

Understanding how to analyze these algorithms enables you to make informed decisions about which algorithm to use in production software, impacting performance in search engines, database systems, and real-time applications.

---

## 2. Understanding Recurrence Relations

### Standard Form for Master Theorem

The Master Theorem applies to recurrences of the following form:

```
T(n) = aT(n/b) + f(n)
```

Where:
- **n** = input size (must be >= 1)
- **a** = number of subproblems (a ≥ 1, integer)
- **b** = factor by which problem size shrinks (b > 1, integer)
- **f(n)** = cost of combining subproblem results (the "work done outside the recursive calls")

### Key Terminology

| Term | Definition |
|------|------------|
| **Recurrence** | An equation that defines T(n) in terms of T of smaller inputs |
| **Base Case** | The condition that stops the recursion (e.g., T(1) = O(1)) |
| **Dividing Phase** | Splitting the problem (represented by a and b) |
| **Conquering Phase** | Solving subproblems recursively |
| **Combining Phase** | Merging results (represented by f(n)) |

### The Role of n/b and f(n)

The term **n/b** represents how the problem is divided. For merge sort, we divide into 2 equal parts (n/b = n/2). For binary search, we also divide into 2 equal parts but only solve ONE subproblem (a=1).

The function **f(n)** represents the "cost at each level" of recursion—the work done to divide the problem and combine results.

---

## 3. The Master Theorem

### Formal Statement

Let **T(n)** be a monotonically increasing function (or assume T(n) is defined for all n ≥ 1) that satisfies:

```
T(n) = aT(n/b) + f(n)
```

Where:
- a ≥ 1 and b > 1 are constants
- f(n) is asymptotically positive (f(n) > 0 for large n)

Let **n^log_b(a)** be the critical function. Then:

| Case | Condition | Solution |
|------|-----------|----------|
| **Case 1** | f(n) = O(n^log_b(a-ε)) for some ε > 0 | T(n) = Θ(n^log_b(a)) |
| **Case 2** | f(n) = Θ(n^log_b(a) * log^k n) where k ≥ 0 | T(n) = Θ(n^log_b(a) * log^(k+1) n) |
| **Case 3** | f(n) = Ω(n^log_b(a+ε)) for some ε > 0 **AND** regularity condition | T(n) = Θ(f(n)) |

### Understanding the Three Cases

#### Case 1: Polynomial Gap (f(n) is polynomially smaller)

If **f(n)** grows asymptotically **slower** than n^log_b(a) by a polynomial factor, then the solution is dominated by the recursive work:

```
T(n) = Θ(n^log_b(a))
```

**Interpretation:** The cost of combining results is negligible compared to the work done in subproblems.

#### Case 2: Balanced (f(n) is roughly equal to n^log_b(a))

If **f(n)** grows at the same rate as n^log_b(a) (within polylogarithmic factors), we get an extra logarithmic factor:

```
T(n) = Θ(n^log_b(a) * log n)  [when k = 0]
T(n) = Θ(n^log_b(a) * log^k+1 n)  [general case]
```

**Interpretation:** The cost of combining equals the work in subproblems, leading to a polylog factor.

#### Case 3: f(n) is polynomially larger

If **f(n)** grows asymptotically **faster** than n^log_b(a) by a polynomial factor, then the solution is dominated by the combining cost:

```
T(n) = Θ(f(n))
```

**But there's a critical condition:** The **regularity condition** must hold:

```
a * f(n/b) ≤ c * f(n) for some c < 1 and large n
```

This ensures that the cost at each recursive level decreases geometrically, allowing us to sum an infinite geometric series.

---

## 4. Polynomial Comparison: Why Answer A is Correct

This section clarifies a common confusion point that was incorrectly addressed in previous materials.

### The Critical MCQ Explained

**Question:** What is the solution to T(n) = 2T(n/2) + n²?

**Options:**
- A. Θ(n²)
- B. Θ(n log n)
- C. Θ(n)
- D. Θ(n³)

**Correct Answer: A. Θ(n²)**

### Detailed Polynomial Comparison

Let's identify the parameters:
- a = 2
- b = 2
- f(n) = n²

First, calculate n^log_b(a):
- log_b(a) = log_2(2) = 1
- n^log_b(a) = n¹ = n

Now compare f(n) = n² with n^log_b(a) = n:

**Comparison:**
- n² vs n
- n² / n = n
- As n → ∞, n² grows **much faster** than n

This is a **polynomial difference**—n² is larger by a factor of n (which is polynomial in n).

**Step-by-step Analysis:**

1. n^log_b(a) = n¹ = n
2. f(n) = n²
3. Compare exponents: 2 vs 1
4. The difference is 2 - 1 = 1 (which is ε = 1)
5. Since f(n) = Ω(n^(1+ε)) where ε = 1 > 0, we are in **Case 3**
6. Check regularity condition: a × f(n/b) = 2 × (n/2)² = 2 × n²/4 = n²/2
7. For c = 3/4 < 1: a × f(n/b) = n²/2 ≤ (3/4)n² = c × f(n) ✓
8. Therefore: T(n) = Θ(f(n)) = Θ(n²)

### Summary Table for Comparison

| Comparison | Case | When to Apply |
|------------|------|---------------|
| f(n) < n^log_b(a) | Case 1 | Polynomial gap where f(n) grows slower |
| f(n) ≈ n^log_b(a) | Case 2 | Within polylog factors (same polynomial) |
| f(n) > n^log_b(a) | Case 3 | Polynomial gap where f(n) grows faster |

**Key Insight:** The comparison is between the **exponents** of n in polynomial functions. If the difference is a constant (not log n), it's a polynomial difference.

---

## 5. Limitations of Master Theorem

The Master Theorem has several important limitations that every student must understand:

### 5.1 Not Applicable When:

1. **a is not constant**: If a depends on n (e.g., a = n), the theorem doesn't apply
2. **b is not constant**: The division factor must be constant
3. **f(n) is not polynomially comparable**: When f(n) is between n^log_b(a) and n^log_b(a) × log^k n but k doesn't fit
4. **Non-polynomial differences**: When f(n) = n^log_b(a) × log²n (the gap is logarithmic, not polynomial)
5. **Subtractive vs Additive**: The theorem requires the "+ f(n)" form, not "- f(n)"

### 5.2 Specific Cases Not Covered:

```
T(n) = T(n/2) + n sin n     # f(n) oscillates
T(n) = 2T(n/2) + n/log n    # Gap is log n, not polynomial
T(n) = T(n-1) + n           # Not divide-and-conquer (b=1)
T(n) = T(√n) + n            # Root division
```

### 5.3 The Handshake Theorem (Akra-Bazzi)

For more general recurrences, the **Akra-Bazzi method** can be used:

```
T(x) = Σ a_i T(b_i x) + g(x)
```

This extends Master Theorem to cases where b is not constant or subproblems are not equal.

---

## 6. Detailed Examples with Code

### Example 1: Binary Search

Binary search divides the problem in half but only processes ONE subproblem.

**Algorithm:**
```
BinarySearch(A[0..n-1], target):
    if low > high:
        return -1
    mid = (low + high) / 2
    if A[mid] == target:
        return mid
    else if A[mid] < target:
        return BinarySearch(A, mid+1, high)
    else:
        return BinarySearch(A, low, mid-1)
```

**Recurrence:**
- a = 1 (one subproblem)
- b = 2 (divide by 2)
- f(n) = O(1) or O(Θ(1)) for calculating mid

**Analysis:**
- n^log_b(a) = n^log_2(1) = n^0 = 1
- f(n) = 1 = Θ(1) = Θ(n^0)

This is **Case 2** with k = 0:
- T(n) = Θ(1 × log n) = Θ(log n)

**Python Implementation:**
```python
def binary_search(arr, target):
    """
    Binary Search Implementation
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion stack
    """
    def _search(low, high):
        if low > high:
            return -1
        
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return _search(mid + 1, high)
        else:
            return _search(low, mid - 1)
    
    return _search(0, len(arr) - 1)

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(arr, 7))  # Output: 3
```

---

### Example 2: Merge Sort

Merge sort divides into two equal parts and processes BOTH.

**Algorithm:**
```
MergeSort(A[0..n-1]):
    if n <= 1:
        return
    mid = n/2
    MergeSort(A[0..mid-1])
    MergeSort(A[mid..n-1])
    Merge(A, mid)
```

**Recurrence:**
- a = 2 (two subproblems)
- b = 2 (divide into halves)
- f(n) = O(n) for merging

**Analysis:**
- n^log_b(a) = n^log_2(2) = n^1 = n
- f(n) = n

This is **Case 2** with k = 0:
- T(n) = Θ(n × log n) = Θ(n log n)

**Python Implementation:**
```python
def merge_sort(arr):
    """
    Merge Sort Implementation
    Time Complexity: O(n log n)
    Space Complexity: O(n) for the temporary array
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays"""
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
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Output: [11, 12, 22, 25, 34, 64, 90]
```

---

### Example 3: Strassen's Matrix Multiplication

Strassen's algorithm is more efficient than naive O(n³) matrix multiplication.

**Recurrence:**
- a = 7 (seven subproblems)
- b = 2 (divide into 2×2 blocks)
- f(n) = O(n^log_2(7)) ≈ O(n^2.807) for combining

**Analysis:**
- n^log_b(a) = n^log_2(7) ≈ n^2.807
- f(n) = n^2

Since n^2 grows slower than n^2.807 (Case 1):
- T(n) = Θ(n^log_2(7)) ≈ Θ(n^2.807)

This is asymptotically better than naive O(n³) multiplication.

---

## 7. Practice Questions with Explanations

### Multiple Choice Questions

#### MCQ 1: Binary Search
**Q:** What is the time complexity of Binary Search using Master Theorem?
- A. O(n)
- B. O(log n)
- C. O(n log n)
- D. O(1)

**Answer: B. O(log n)**

**Explanation:** 
- a = 1, b = 2, f(n) = 1
- n^log_b(a) = n^0 = 1
- f(n) = Θ(1) = Θ(n^0 × log^0 n) = Case 2 with k = 0
- T(n) = Θ(n^0 × log^1 n) = Θ(log n)

---

#### MCQ 2: Merge Sort (Addressed Issue)
**Q:** What is the solution to T(n) = 2T(n/2) + n²?
- A. Θ(n²)
- B. Θ(n log n)
- C. Θ(n)
- D. Θ(n³)

**Answer: A. Θ(n²)**

**Explanation (Detailed):**
- a = 2, b = 2, f(n) = n²
- n^log_b(a) = n^log_2(2) = n^1 = n
- Compare: n² vs n → n² is larger by factor of n (polynomial difference)
- f(n) = Ω(n^(1+ε)) where ε = 1
- This is **Case 3** (not Case 2!)
- Check regularity: a × f(n/b) = 2 × (n/2)² = 2 × n²/4 = n²/2 ≤ c × n² for c = 3/4
- Therefore: T(n) = Θ(f(n)) = Θ(n²)

---

#### MCQ 3: Ternary Search
**Q:** A recursive algorithm divides problem into 3 equal parts with O(n) work at each level. What is the complexity?
- A. Θ(n)
- B. Θ(n log 3)
- C. Θ(n log n)
- D. Θ(n²)

**Answer: C. Θ(n log n)**

**Explanation:**
- a = 3, b = 3, f(n) = n
- n^log_b(a) = n^log_3(3) = n^1 = n
- f(n) = Θ(n) = Θ(n^1 × log^0 n)
- This is Case 2 with k = 0
- T(n) = Θ(n × log n)

---

#### MCQ 4: Limitations
**Q:** Which recurrence CANNOT be solved using Master Theorem?
- A. T(n) = 2T(n/2) + n log n
- B. T(n) = T(n-1) + n
- C. T(n) = 4T(n/2) + n²
- D. T(n) = 3T(n/3) + n

**Answer: B. T(n) = T(n-1) + n**

**Explanation:**
- Master Theorem requires the problem to be divided by a constant factor b > 1
- Here b = n/(n-1) → not constant
- This is linear recurrence (subtracts 1, doesn't divide), solved by different methods
- Other recurrences fit the Master Theorem form

---

### Fill in the Blanks

1. In T(n) = aT(n/b) + f(n), the parameter **a** represents the number of recursive subproblems.

2. The critical function n^log_b(a) represents the work done by the **recursive portion** of the algorithm.

3. When f(n) = Θ(n^log_b(a)), we get an extra **logarithmic** factor in the solution.

---

## 8. Flashcards (Complete Set)

| Term | Definition |
|------|------------|
| **Master Theorem** | A formula for solving recurrences of form T(n) = aT(n/b) + f(n) |
| **Recurrence Relation** | An equation that defines T(n) in terms of T of smaller inputs |
| **Case 1** | f(n) = O(n^log_b(a-ε)) → T(n) = Θ(n^log_b(a)) |
| **Case 2** | f(n) = Θ(n^log_b(a) × log^k n) → T(n) = Θ(n^log_b(a) × log^(k+1) n) |
| **Case 3** | f(n) = Ω(n^log_b(a+ε)) with regularity → T(n) = Θ(f(n)) |
| **Regularity Condition** | a × f(n/b) ≤ c × f(n) for some c < 1 (for Case 3) |
| **Base Case** | The condition that stops recursion (e.g., n ≤ 1) |
| **Divide and Conquer** | Algorithm design paradigm that breaks problem into smaller subproblems |
| **a** | Number of subproblems in Master Theorem (a ≥ 1) |
| **b** | Factor by which problem size shrinks (b > 1) |
| **f(n)** | Cost of combining results in divide-and-conquer |
| **Akra-Bazzi Method** | More general method for recurrences not covered by Master Theorem |
| **Binary Search** | Example of Case 2 with T(n) = T(n/2) + O(1) → Θ(log n) |
| **Merge Sort** | Example of Case 2 with T(n) = 2T(n/2) + O(n) → Θ(n log n) |

---

## 9. Key Takeaways

1. **Master Theorem Formula**: For recurrences T(n) = aT(n/b) + f(n), compare f(n) with n^log_b(a):
   - If f(n) is polynomially smaller → **Case 1**: Θ(n^log_b(a))
   - If f(n) equals n^log_b(a) → **Case 2**: Θ(n^log_b(a) × log n)
   - If f(n) is polynomially larger → **Case 3**: Θ(f(n)) [with regularity condition]

2. **Polynomial vs Polylogarithmic**: The key distinction is whether the difference between exponents is constant (polynomial) or logarithmic. Case 2 specifically handles polylog differences.

3. **Regularity Condition**: For Case 3, always verify a × f(n/b) ≤ c × f(n) for some c < 1 before concluding T(n) = Θ(f(n)).

4. **Know the Limitations**: Master Theorem doesn't apply when b is not constant, a is not constant, or f(n) is not polynomially comparable to n^log_b(a).

5. **Common Examples to Remember**:
   - Binary Search: T(n) = T(n/2) + O(1) = Θ(log n)
   - Merge Sort: T(n) = 2T(n/2) + O(n) = Θ(n log n)
   - Binary Tree Traversal: T(n) = 2T(n/2) + O(1) = Θ(n)

6. **Delhi University NEP 2024 Focus**: The Ge4A Data Structures syllabus emphasizes practical algorithm analysis. Master Theorem is frequently tested in internal assessments and end-semester examinations.

---

*Prepared for BSc Physical Science (CS) | Ge4A Data Structures | Delhi University NEP 2024*