# Complexity Analysis & Big O Notation

## Introduction
Complexity analysis forms the cornerstone of algorithm design and evaluation. In computer science, it provides a systematic way to compare the efficiency of algorithms independent of hardware specifications. For MCA students working with large-scale systems, understanding complexity becomes crucial when dealing with Big Data, real-time systems, and resource-constrained environments.

Big O notation serves as the primary tool for asymptotic analysis, describing how an algorithm's resource requirements grow as input size increases. Industry giants like Google and Amazon use complexity analysis to optimize search algorithms, recommendation systems, and cloud infrastructure. In DU's MCA program, this concept is fundamental for courses ranging from Advanced Algorithms to Distributed Systems.

The 2024 NEP emphasizes applied learning, making practical complexity analysis skills essential. Whether optimizing a route-finding algorithm for Delhi Metro's network or improving Ola's surge pricing calculations, Big O analysis helps engineers make data-driven decisions about algorithm selection.

## Key Concepts
1. **Asymptotic Behavior**: Analysis of algorithms as input size approaches infinity
2. **Big O (O)**: Upper bound of growth rate (Worst-case analysis)
3. **Omega (Ω)**: Lower bound (Best-case analysis)
4. **Theta (Θ)**: Tight bound (Average-case analysis)
5. **Time vs Space Complexity**: Trade-off analysis fundamental in mobile app development
6. **Amortized Analysis**: Critical for data structure operations (e.g., Dynamic Arrays)
7. **Recurrence Relations**: Solving using Master Theorem for divide-and-conquer algorithms

**Formal Definition**: 
f(n) = O(g(n)) iff ∃ constants c > 0 and n₀ ≥ 0 such that 0 ≤ f(n) ≤ c·g(n) ∀ n ≥ n₀

## Examples

**Example 1: Nested Loops Analysis**
```python
def matrix_operations(n):
    total = 0
    for i in range(n):          # O(n)
        for j in range(n):      # O(n)
            total += i*j        # O(1) constant operation
    return total
```
**Solution:**
- Outer loop runs n times
- Inner loop runs n times per outer iteration
- Total operations = n * n * 1 = n²
- Time Complexity: O(n²)

**Example 2: Recursive Fibonacci**
```python
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2) 
```
**Solution:**
- Recursion tree has ≈ 2ⁿ nodes
- Recurrence relation: T(n) = T(n-1) + T(n-2) + O(1)
- Time Complexity: O(2ⁿ) exponential time

**Example 3: Binary Search**
```python
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```
**Solution:**
- With each iteration, search space halves
- Recurrence: T(n) = T(n/2) + O(1)
- Solved using Master Theorem: O(log n)

## Exam Tips
1. Always analyze worst-case scenarios unless specified otherwise
2. For nested loops, multiply complexities (O(n²) for two nested O(n) loops)
3. In recursive algorithms, identify the recursion tree depth and branching factor
4. Remember that constants and lower-order terms are dropped: O(3n² + 2n + 5) → O(n²)
5. When comparing algorithms, O(n log n) always beats O(n²) for large n
6. For space complexity, consider auxiliary space + input size
7. Master Theorem applies only to recurrences of form T(n) = aT(n/b) + f(n)