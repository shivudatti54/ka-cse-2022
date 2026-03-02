# Introduction to Algorithm Analysis

## What is Algorithm Analysis?

Algorithm analysis is a fundamental concept in computer science that involves evaluating the efficiency of algorithms in terms of time and space requirements. It provides a theoretical framework for comparing different algorithms that solve the same problem, helping us determine which algorithm is most efficient for a given scenario.

At its core, algorithm analysis answers the question: "How does the performance of an algorithm scale as the input size increases?"

## Why Analyze Algorithms?

There are several important reasons for analyzing algorithms:

1. **Performance Prediction**: Estimate how an algorithm will perform with large inputs
2. **Comparison**: Objectively compare different algorithms for the same problem
3. **Optimization**: Identify bottlenecks and opportunities for improvement
4. **Resource Planning**: Determine hardware requirements for specific workloads
5. **Theoretical Understanding**: Develop insights about computational problems

## Key Concepts in Algorithm Analysis

### Input Size (n)

The input size represents the amount of data the algorithm needs to process. This could be:

- Number of elements in an array
- Number of nodes in a graph
- Number of bits in a binary number
- Size of a file in bytes

### Time Complexity

Time complexity measures the amount of time an algorithm takes to complete as a function of the input size. We typically count the number of "basic operations" performed.

```
Example: Linear Search
For each element in array of size n:
    Compare element with target (1 operation)

Total operations: n (in worst case)
Time complexity: O(n)
```

### Space Complexity

Space complexity measures the amount of memory an algorithm requires as a function of the input size. This includes:

- Space for the input data
- Auxiliary space (extra space used by the algorithm)
- Space for the output

```
Example: Reversing an array
Input: Array of size n
Auxiliary space: New array of size n
Space complexity: O(n)
```

## Basic Operations and Counting

When analyzing algorithms, we focus on dominant operations that contribute most to the running time:

| Operation Type        | Examples     | Relative Cost |
| --------------------- | ------------ | ------------- |
| Arithmetic operations | +, -, \*, /  | Low           |
| Comparisons           | <, >, ==, != | Low           |
| Assignments           | x = y        | Low           |
| Function calls        | func()       | Medium        |
| Memory allocation     | new, malloc  | High          |
| I/O operations        | read, write  | Very High     |

```
Example: Simple summation algorithm

function sum(array, n):
    total = 0              // 1 assignment
    for i = 0 to n-1:     // n iterations
        total += array[i]  // n additions + n assignments
    return total           // 1 return

Total operations: 1 + n*(1+1) + 1 = 2n + 2
```

## Asymptotic Analysis

Asymptotic analysis describes the behavior of algorithms as the input size approaches infinity. It focuses on the growth rate rather than exact operation counts.

### Why Asymptotic Analysis?

1. **Machine independence**: Avoids hardware-specific measurements
2. **Focus on growth**: Captures the essential scaling behavior
3. **Simplification**: Ignores constants and lower-order terms
4. **Practical relevance**: For large inputs, growth rate dominates performance

## Asymptotic Notations

### Big-O Notation (O)

Big-O notation describes the **upper bound** of an algorithm's growth rate. It represents the worst-case scenario.

**Formal definition**: f(n) = O(g(n)) if there exist positive constants c and n₀ such that 0 ≤ f(n) ≤ c·g(n) for all n ≥ n₀.

```
Example: f(n) = 3n² + 2n + 1 = O(n²)
We can choose c = 4 and n₀ = 1:
3n² + 2n + 1 ≤ 4n² for all n ≥ 1
```

### Omega Notation (Ω)

Omega notation describes the **lower bound** of an algorithm's growth rate. It represents the best-case scenario.

**Formal definition**: f(n) = Ω(g(n)) if there exist positive constants c and n₀ such that 0 ≤ c·g(n) ≤ f(n) for all n ≥ n₀.

```
Example: f(n) = 3n² + 2n + 1 = Ω(n²)
We can choose c = 3 and n₀ = 0:
3n² ≤ 3n² + 2n + 1 for all n ≥ 0
```

### Theta Notation (Θ)

Theta notation describes the **tight bound** of an algorithm's growth rate. It represents both upper and lower bounds.

**Formal definition**: f(n) = Θ(g(n)) if there exist positive constants c₁, c₂, and n₀ such that 0 ≤ c₁·g(n) ≤ f(n) ≤ c₂·g(n) for all n ≥ n₀.

```
Example: f(n) = 3n² + 2n + 1 = Θ(n²)
We can choose c₁ = 3, c₂ = 4, and n₀ = 1:
3n² ≤ 3n² + 2n + 1 ≤ 4n² for all n ≥ 1
```

## Common Complexity Classes

| Complexity Class | Name         | Example Algorithms                                       |
| ---------------- | ------------ | -------------------------------------------------------- |
| O(1)             | Constant     | Array access, arithmetic operations                      |
| O(log n)         | Logarithmic  | Binary search, balanced tree operations                  |
| O(n)             | Linear       | Linear search, traversing a list                         |
| O(n log n)       | Linearithmic | Efficient sorting (Merge Sort, QuickSort)                |
| O(n²)            | Quadratic    | Bubble Sort, Selection Sort, naive matrix multiplication |
| O(n³)            | Cubic        | Floyd-Warshall algorithm, naive matrix multiplication    |
| O(2ⁿ)            | Exponential  | Traveling Salesman (brute force), subset generation      |
| O(n!)            | Factorial    | Permutation generation, brute force for TSP              |

## Growth Rate Comparison

```
n    | log n | n   | n log n | n²     | 2ⁿ
-----|-------|-----|---------|--------|---------
10   | 3     | 10  | 30      | 100    | 1,024
100  | 7     | 100 | 700     | 10,000 | 1.27e+30
1000 | 10    | 1000| 10,000  | 1e+6   | 1.07e+301
```

This table shows why exponential algorithms become impractical even for moderately sized inputs.

## Case Analysis: Best, Worst, and Average Cases

### Best Case Analysis

The best case represents the scenario where the algorithm performs with minimum time/space requirements.

```
Example: Linear Search
Best case: Target is the first element
Operations: 1 comparison
Time complexity: Ω(1)
```

### Worst Case Analysis

The worst case represents the scenario where the algorithm performs with maximum time/space requirements.

```
Example: Linear Search
Worst case: Target is the last element or not present
Operations: n comparisons
Time complexity: O(n)
```

### Average Case Analysis

The average case represents the expected performance over all possible inputs, often using probability distributions.

```
Example: Linear Search
Average case: Target is equally likely to be at any position
Expected comparisons: (n+1)/2
Time complexity: Θ(n)
```

## Space Complexity Analysis

Space complexity analysis follows similar principles to time complexity but focuses on memory usage.

```
Example: Recursive Fibonacci

function fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

Space complexity: O(n) due to recursion stack depth
```

## Practical Examples

### Example 1: Constant Time O(1)

```python
def get_first_element(arr):
    return arr[0]  # Single operation, independent of input size
```

### Example 2: Linear Time O(n)

```python
def find_max(arr):
    max_val = arr[0]           # 1 assignment
    for i in range(1, len(arr)): # n-1 iterations
        if arr[i] > max_val:   # n-1 comparisons
            max_val = arr[i]   # Up to n-1 assignments
    return max_val             # 1 return
# Total: O(n)
```

### Example 3: Quadratic Time O(n²)

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):         # n iterations
        for j in range(0, n-i-1): # n-i-1 iterations each time
            if arr[j] > arr[j+1]: # Comparison
                arr[j], arr[j+1] = arr[j+1], arr[j] # Swap
# Total: O(n²)
```

## Common Mistakes in Algorithm Analysis

1. **Ignoring constants**: While constants are ignored in asymptotic analysis, they matter in practice
2. **Confusing worst-case and average-case**: These can be very different
3. **Overlooking hidden costs**: Function calls, memory allocation, I/O operations
4. **Assuming optimal conditions**: Real-world factors like cache effects, branch prediction
5. **Misapplying asymptotic notation**: Using Big-O when Theta is more appropriate

## Exam Tips

1. **Focus on dominant terms**: When simplifying expressions, keep only the fastest-growing term
2. **Understand the definitions**: Be able to apply the formal definitions of O, Ω, and Θ
3. **Practice with examples**: Work through multiple examples of different complexity classes
4. **Compare algorithms**: Be prepared to compare time and space complexities of different approaches
5. **Consider both time and space**: Some algorithms trade time for space or vice versa
6. **Watch for recursion**: Recursive algorithms often have hidden space complexity in the call stack
7. **Remember best/worst/average cases**: Different scenarios may have different complexities
8. **Use proper notation**: Write complexity classes correctly (O(n), not O(n))
