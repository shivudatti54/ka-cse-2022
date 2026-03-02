# Algorithm Analysis Framework

## Table of Contents

- [Algorithm Analysis Framework](#algorithm-analysis-framework)
- [Introduction](#introduction)
- [Mathematical Foundations and Formal Definitions](#mathematical-foundations-and-formal-definitions)
  - [Input Size and Basic Operations](#input-size-and-basic-operations)
  - [Formal Definition of Asymptotic Notations](#formal-definition-of-asymptotic-notations)
  - [Proof of Asymptotic Notation Properties](#proof-of-asymptotic-notation-properties)
- [Time Complexity Analysis](#time-complexity-analysis)
  - [Complexity Classes](#complexity-classes)
  - [Best, Worst, and Average Case Analysis](#best-worst-and-average-case-analysis)
  - [Recurrence Relations and Master Theorem](#recurrence-relations-and-master-theorem)
- [Space Complexity Analysis](#space-complexity-analysis)
- [Worked Examples](#worked-examples)
  - [Example 1: Nested Loops with Variable Bounds](#example-1-nested-loops-with-variable-bounds)
  - [Example 2: Recursive Algorithm Analysis](#example-2-recursive-algorithm-analysis)
  - [Example 3: Logarithmic Loop Analysis](#example-3-logarithmic-loop-analysis)
- [Application-Level Assessment](#application-level-assessment)
  - [Multiple Choice Questions](#multiple-choice-questions)

## Introduction

The Algorithm Analysis Framework constitutes the foundational mathematical apparatus enabling computer scientists and software engineers to evaluate, compare, and systematically improve the efficiency of algorithmic solutions. Within the context of the university's Analysis and Design of Algorithms course (BCS401), this framework provides the rigorous quantitative tools necessary for measuring how an algorithm's computational resource requirements scale with input size. The ability to perform such analysis is indispensable in professional software development, as it enables informed decisions regarding algorithm selection, optimization priorities, and performance guarantees in production systems.

The significance of algorithm analysis becomes particularly pronounced when addressing large-scale data processing challenges, where seemingly minor inefficiencies can accumulate into substantial computational overhead. Consider a database containing $10^6$ records requiring a search operation: linear search exhibits $O(n)$ complexity yielding potentially $10^6$ comparisons, whereas binary search achieves $O(\log n)$ complexity requiring merely 20 comparisons—a reduction of five orders of magnitude. This module establishes the formal mathematical foundations and standardized notation systems that permit precise, objective expression of such efficiency differentials, thereby enabling evidence-based algorithmic selection rather than intuition-driven choices.

## Mathematical Foundations and Formal Definitions

### Input Size and Basic Operations

The analysis of any algorithm commences with the precise characterization of **input size**, formally denoted as $n$, which quantifies the magnitude of the problem instance. The appropriate metric for input size varies according to problem domain: for sorting algorithms, $n$ represents the number of elements in the array; for graph algorithms, $n$ may denote either vertex count $|V|$ or edge count $|E|$; for string processing problems, $n$ typically represents the string length. The selection of a mathematically appropriate input size metric constitutes the first critical step in rigorous algorithm analysis.

**Basic operations** are the fundamental atomic steps within an algorithm whose execution count correlates directly and monotonically with the algorithm's running time. Examples include comparison operations in sorting algorithms ($A[i] < A[j]$), assignment operations in iterative constructs, arithmetic operations in mathematical computations, or array access operations. Identifying the dominant basic operation—often through the method of worst-case common loop counting—enables construction of a simplified analytical model that captures the essential computational complexity while abstracting implementation details.

### Formal Definition of Asymptotic Notations

Asymptotic notation provides a mathematically rigorous framework for describing the growth rate of functions as the input size approaches infinity. These notations establish theoretical bounds that remain independent of constant factors and lower-order terms, focusing exclusively on the fundamental growth behavior.

**Big-O Notation (Upper Bound)**: The formal definition states that a function $f(n)$ is in the set $O(g(n))$ if and only if there exist positive constants $c$ and $n_0$ such that:

$$0 \leq f(n) \leq c \cdot g(n) \quad \text{for all } n \geq n_0$$

In set notation, we express this as $f(n) \in O(g(n))$, though conventional usage often writes $f(n) = O(g(n))$. Big-O notation establishes an upper bound on growth rate, representing the worst-case scenario. For instance, $f(n) = 3n^2 + 5n + 2$ belongs to $O(n^2)$ because for $c = 4$ and $n_0 = 5$, we have $3n^2 + 5n + 2 \leq 4n^2$ for all $n \geq 5$.

**Big-Omega Notation (Lower Bound)**: A function $f(n)$ is in $\Omega(g(n))$ if there exist positive constants $c$ and $n_0$ such that:

$$f(n) \geq c \cdot g(n) \geq 0 \quad \text{for all } n \geq n_0$$

Big-Omega provides a lower bound, indicating the best-case or minimum time complexity. For the same function $f(n) = 3n^2 + 5n + 2$, we have $f(n) \in \Omega(n^2)$ since $3n^2 \leq f(n)$ for $c = 3$ and $n_0 = 1$.

**Theta Notation (Tight Bound)**: A function $f(n)$ is in $\Theta(g(n))$ if it is bounded both above and below by functions proportional to $g(n)$:

$$c_1 \cdot g(n) \leq f(n) \leq c_2 \cdot g(n) \quad \text{for all } n \geq n_0$$

Formally, $f(n) = \Theta(g(n))$ if and only if $f(n) = O(g(n))$ and $f(n) = \Omega(g(n))$. For our example, $3n^2 + 5n + 2 = \Theta(n^2)$ because we can select $c_1 = 1$, $c_2 = 4$, and $n_0 = 5$ to satisfy the condition.

### Proof of Asymptotic Notation Properties

**Theorem (Transitivity)**: If $f(n) = O(g(n))$ and $g(n) = O(h(n))$, then $f(n) = O(h(n))$.

_Proof_: By definition, $f(n) \leq c_1 \cdot g(n)$ for $n \geq n_1$ and $g(n) \leq c_2 \cdot h(n)$ for $n \geq n_2$. Combining these inequalities for $n \geq \max(n_1, n_2)$:

$$f(n) \leq c_1 \cdot g(n) \leq c_1 \cdot c_2 \cdot h(n) = c \cdot h(n)$$

where $c = c_1 \cdot c_2$. This establishes $f(n) = O(h(n))$. $\square$

**Theorem**: $f(n) = \Theta(g(n))$ if and only if $g(n) = \Theta(f(n))$.

_Proof_: By definition, $f(n) = \Theta(g(n))$ implies $f(n) = O(g(n))$ and $f(n) = \Omega(g(n))$. From $f(n) = O(g(n))$, there exist $c_1, n_1$ such that $f(n) \leq c_1 g(n)$, yielding $g(n) \geq (1/c_1)f(n)$. From $f(n) = \Omega(g(n))$, there exist $c_2, n_2$ such that $f(n) \geq c_2 g(n)$, yielding $g(n) \leq (1/c_2)f(n)$. Combining these for $n \geq \max(n_1, n_2)$ establishes the symmetric bounds, proving $g(n) = \Theta(f(n))$. $\square$

## Time Complexity Analysis

### Complexity Classes

Algorithms are systematically classified according to their time complexity, ordered from most efficient to least efficient:

| Complexity Class  | Notation      | Example Algorithm           |
| ----------------- | ------------- | --------------------------- |
| Constant Time     | $O(1)$        | Array index access          |
| Logarithmic Time  | $O(\log n)$   | Binary search               |
| Linear Time       | $O(n)$        | Linear search, traversal    |
| Linearithmic Time | $O(n \log n)$ | Merge sort, Heap sort       |
| Quadratic Time    | $O(n^2)$      | Bubble sort, Insertion sort |
| Cubic Time        | $O(n^3)$      | Naive matrix multiplication |
| Exponential Time  | $O(2^n)$      | Recursive Fibonacci         |
| Factorial Time    | $O(n!)$       | Permutation generation      |

### Best, Worst, and Average Case Analysis

The performance characteristics of algorithms exhibit significant variation depending upon input characteristics:

**Best Case** represents the most favorable input distribution yielding minimal running time. In linear search, if the target element resides at the first position, the algorithm performs exactly one comparison, yielding $T_{best}(n) = \Omega(1)$.

**Worst Case** denotes the input pattern producing maximal running time. For linear search, worst case occurs when the target element resides at the final position or does not exist within the array, resulting in $T_{worst}(n) = O(n)$.

**Average Case** analysis requires assumptions regarding input distribution. Assuming uniform probability distribution where each of the $n$ positions is equally likely to contain the target (and assuming the target exists with probability $p$), the expected number of comparisons is:

$$E[n_{comparisons}] = p \cdot \frac{n+1}{2} + (1-p) \cdot n$$

This yields $\Theta(n)$ average-case complexity for constant $p$.

### Recurrence Relations and Master Theorem

For recursive algorithms, time complexity is expressed through recurrence relations. Consider the recurrence for binary search:

$$T(n) = T(n/2) + O(1)$$

The Master Theorem provides asymptotic solutions for recurrences of the form $T(n) = aT(n/b) + f(n)$ where $a \geq 1$, $b > 1$:

- If $f(n) = O(n^{\log_b a - \epsilon})$ for some $\epsilon > 0$, then $T(n) = \Theta(n^{\log_b a})$
- If $f(n) = \Theta(n^{\log_b a})$, then $T(n) = \Theta(n^{\log_b a} \log n)$
- If $f(n) = \Omega(n^{\log_b a + \epsilon})$ and $af(n/b) \leq cf(n)$ for some $c < 1$ and sufficiently large $n$, then $T(n) = \Theta(f(n))$

For binary search with $a = 1$, $b = 2$, and $f(n) = \Theta(1)$, we have $n^{\log_2 1} = n^0 = 1$, yielding case 2: $T(n) = \Theta(\log n)$.

## Space Complexity Analysis

Space complexity $S(n)$ measures memory consumption as a function of input size, encompassing both input storage and auxiliary space required during computation. An algorithm utilizing $O(1)$ auxiliary space is termed **in-place**.

**Example**: Merge Sort requires $O(n)$ auxiliary space for the temporary arrays during merging, whereas Quick Sort typically operates in-place with $O(\log n)$ auxiliary space for recursion stack in the average case, though $O(n)$ in the worst case when unbalanced partitions occur.

## Worked Examples

### Example 1: Nested Loops with Variable Bounds

**Problem**: Determine the time complexity of:

```python
count = 0
for i in range(n):
 for j in range(i, n):
 count += 1
```

**Solution**: The outer loop executes $n$ times. For each $i$ from $0$ to $n-1$, the inner loop executes $(n-i)$ times. The total number of iterations equals:

$$\sum_{i=0}^{n-1} (n-i) = n + (n-1) + (n-2) + \cdots + 1 = \frac{n(n+1)}{2} = \frac{n^2}{2} + \frac{n}{2}$$

Applying asymptotic bounds, we observe $n^2/2 \leq n(n+1)/2 \leq n^2$ for $n \geq 1$. Therefore, the complexity is $\Theta(n^2)$.

### Example 2: Recursive Algorithm Analysis

**Problem**: Analyze the recurrence $T(n) = 2T(n/2) + n$ with $T(1) = 1$.

**Solution**: Applying the Master Theorem with $a = 2$, $b = 2$, we have $n^{\log_2 2} = n^1 = n$. Since $f(n) = \Theta(n^{\log_b a})$, we are in Case 2, yielding $T(n) = \Theta(n \log n)$. This complexity matches that of Merge Sort, where the $n$ term represents the cost of the merging step.

### Example 3: Logarithmic Loop Analysis

**Problem**: Determine complexity of:

```python
i = n
while i >= 1:
 i = i // 2
```

**Solution**: The loop variable $i$ takes values $n, n/2, n/4, \ldots, 1$. After $k$ iterations, $i = n/2^k$. The loop terminates when $i < 1$, i.e., when $n/2^k < 1$, or $k > \log_2 n$. Thus, the loop executes $\lfloor \log_2 n \rfloor + 1$ times, yielding $\Theta(\log n)$ complexity.

## Application-Level Assessment

### Multiple Choice Questions

**Question 1**: Consider the following code fragment:

```python
result = 0
for i in range(n):
 for j in range(i+1):
 result += i * j
```

The time complexity of this algorithm is:

- (a) $\Theta(n)$
- (b) $\Theta(n^2)$
- (c) $\Theta(n^3)$
- (d) $\Theta(n^4)$

**Answer**: (b) $\Theta(n^2)$

_Explanation_: The outer loop runs $n$ times. For each $i$, the inner loop runs $(i+1)$ times. The total operations equal $\sum_{i=0}^{n-1} (i+1) = \sum_{k=1}^{n} k = n(n+1)/2 = \Theta(n^2)$.

**Question 2**: The recurrence $T(n) = 3T(n/4) + n^2$ has asymptotic complexity:

- (a) $\Theta(n^{\log_4 3})$
- (b) $\Theta(n^2)$
- (c) $\Theta(n^2 \log n)$
- (d) $\Theta(n^{\log_4 3} \log n)$

**Answer**: (b) $\Theta(n^2)$

_Explanation_: Here $a = 3$, $b = 4$, so $n^{\log_4 3} = n^{0.792...}$. Since $f(n) = n^2 = \Omega(n^{\log_4 3 + \epsilon})$ with $\epsilon \approx 0.208$, and the regularity condition holds ($3(n/4)^2 = 3n^2/16 \leq cn^2$ for $c = 3/16 < 1$), we are in Case 3 of the Master Theorem, yielding $\Theta(n^2)$.

**Question 3**: Which of the following statements is TRUE?

- (a) $n^2 = O(n^3)$
- (b) $n^2 = \Omega(n^3)$
- (c) $2^n = O(n!)$
- (d) $\log n = O(\sqrt{n})$

**Answer**: (a), (c), and (d)

_Explanation_: (a) True: $n^2 \leq n^3$ for $n \geq 1$, so $n^2 = O(n^3)$. (b) False: $n^2 \not\geq c \cdot n^3$ for any positive $c$ as $n \to \infty$. (c) True: factorial grows faster than exponential, so $2^n = O(n!)$. (d) True: $\log n = O(\sqrt{n})$ because $\log n / \sqrt{n} \to 0$ as $n \to \infty$.

**Question 4**: An algorithm performs exactly $n^2 / 2 - n / 2$ comparisons for input size $n$. Its asymptotic notation is:

- (a) $O(n)$
- (b) $\Theta(n)$
- (c) $\Theta(n^2)$
- (d) $\Omega(n^3)$

**Answer**: (c) $\Theta(n^2)$

_Explanation_: $n^2/2 - n/2 = \Theta(n^2)$ because the dominant term is $n^2/2$, and we can establish both upper and lower bounds: $n^2/4 \leq n^2/2 - n/2 \leq n^2$ for $n \geq 2$.
