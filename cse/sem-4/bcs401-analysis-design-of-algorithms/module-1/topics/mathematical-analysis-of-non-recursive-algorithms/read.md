# Mathematical Analysis of Non-Recursive Algorithms

## Table of Contents

- [Mathematical Analysis of Non-Recursive Algorithms](#mathematical-analysis-of-non-recursive-algorithms)
- [Introduction](#introduction)
- [Theoretical Framework for Analysis](#theoretical-framework-for-analysis)
  - [Step-Count Method](#step-count-method)
  - [Asymptotic Notation Definitions](#asymptotic-notation-definitions)
- [Worked Examples](#worked-examples)
  - [Example 1: Linear Search Analysis](#example-1-linear-search-analysis)
  - [Example 2: Nested Independent Loops - Selection Sort](#example-2-nested-independent-loops---selection-sort)
  - [Example 3: Logarithmic Loop Analysis](#example-3-logarithmic-loop-analysis)
  - [Example 4: Nested Dependent Loops](#example-4-nested-dependent-loops)
- [Common Summation Formulas](#common-summation-formulas)
- [Case Analysis](#case-analysis)
  - [Best, Worst, and Average Case](#best-worst-and-average-case)
  - [Space Complexity](#space-complexity)
- [Complexity Hierarchy](#complexity-hierarchy)
- [Conclusion](#conclusion)

## Introduction

Algorithm analysis constitutes a fundamental discipline in computer science, providing the mathematical framework necessary to evaluate and compare algorithmic efficiency in terms of time and space requirements. The mathematical analysis of non-recursive algorithms establishes the foundational techniques for evaluating algorithm performance prior to implementation, representing an essential competency within the Analysis and Design of Algorithms curriculum.

Non-recursive algorithms, alternatively termed iterative algorithms, solve problems through loops and iterative constructs without self-referential calls. The analysis of such algorithms requires precise quantification of basic operations and the expression of running time as a function of input size using asymptotic notation. This analytical capability proves indispensable for software engineers and computer scientists tasked with developing efficient, scalable solutions.

The significance of algorithm analysis has intensified dramatically with the exponential growth of data volumes across applications spanning big data analytics, machine learning, and distributed computing systems. A meticulously analyzed algorithm can process millions of data points within seconds, whereas an inefficient alternative might require hours or fail to complete entirely.

## Theoretical Framework for Analysis

### Step-Count Method

The systematic analysis of non-recursive algorithms follows a precise methodological framework:

1. **Identify the input size parameter (n)**: Determine the characteristic measure of problem size. For sorting problems, n represents the number of elements; for matrix operations, n typically represents matrix dimension; for graph algorithms, n may denote vertices or edges.

2. **Identify the basic operation**: The basic operation constitutes the fundamental computation executed most frequently and contributing predominantly to total running time. In comparison-based sorting, this is the comparison operation; in searching, it is the key comparison; in matrix algorithms, it is often arithmetic operations on individual elements.

3. **Determine frequency count**: Establish how many times the basic operation executes as a function of input size n, considering the algorithm's control structure.

4. **Express as summation**: Formulate the total execution count as a summation expression based on loop boundaries and control flow.

5. **Evaluate the summation**: Solve the summation to obtain a closed-form expression representing the exact count.

6. **Apply asymptotic notation**: Express the result using Big-O, Ω, or Θ notation to capture asymptotic behavior.

### Asymptotic Notation Definitions

**Big-O Notation (Upper Bound)**: A function f(n) is O(g(n)) if there exist positive constants c and n₀ such that 0 ≤ f(n) ≤ c·g(n) for all n ≥ n₀. This establishes an upper bound on growth rate.

**Big-Omega Notation (Lower Bound)**: A function f(n) is Ω(g(n)) if there exist positive constants c and n₀ such that 0 ≤ c·g(n) ≤ f(n) for all n ≥ n₀. This establishes a lower bound.

**Big-Theta Notation (Tight Bound)**: A function f(n) is Θ(g(n)) if f(n) = O(g(n)) and f(n) = Ω(g(n)), meaning g(n) provides both upper and lower bounds on f(n)'s growth.

## Worked Examples

### Example 1: Linear Search Analysis

Consider the linear search algorithm that traverses an array sequentially to find a target element:

```
Algorithm LinearSearch(A[0..n-1], key)
 for i ← 0 to n-1 do
 if A[i] = key then
 return i
 end if
 end for
 return -1
```

**Analysis**:

- Input size parameter: n (number of elements)
- Basic operation: comparison A[i] = key
- Frequency analysis:
- Best case: 1 comparison (element at index 0) → Ω(1)
- Worst case: n comparisons (element not found or at last position) → O(n)
- Average case: Assuming element is present with probability p and uniformly distributed: (n+1)/2 comparisons → Θ(n)

The summation for worst case: T(n) = Σᵢ₌₀ⁿ⁻¹ 1 = n

### Example 2: Nested Independent Loops - Selection Sort

Selection sort repeatedly finds the minimum element from the unsorted portion:

```
Algorithm SelectionSort(A[0..n-1])
 for i ← 0 to n-2 do
 min ← i
 for j ← i+1 to n-1 do
 if A[j] < A[min] then
 min ← j
 end if
 end for
 swap A[i] and A[min]
 end for
```

**Analysis**:

- Basic operation: comparison A[j] < A[min]
- Outer loop executes (n-1) times
- Inner loop executes: (n-1) + (n-2) + ... + 1 = n(n-1)/2 times

**Summation setup**:
T(n) = Σᵢ₌₀ⁿ⁻² Σⱼ₌ᵢ₊₁ⁿ⁻¹ 1

**Evaluation**:
T(n) = Σᵢ₌₀ⁿ⁻² (n - 1 - i) = Σᵢ₌₁ⁿ⁻¹ i = n(n-1)/2 = (n² - n)/2

**Asymptotic notation**: Θ(n²)

### Example 3: Logarithmic Loop Analysis

Consider an algorithm with a loop where the counter decreases by a factor:

```
Algorithm LogLoop(n)
 i ← n
 while i > 1 do
 process(i)
 i ← i/2
 end while
```

**Analysis**:

- Basic operation: process(i)
- The loop executes while i > 1, with i taking values: n, n/2, n/4, ..., until 1
- Number of iterations: ⌊log₂ n⌋ + 1

**Summation**: T(n) = Σₖ₌₀^⌊log₂ n⌋ 1 = ⌊log₂ n⌋ + 1

**Asymptotic notation**: Θ(log n)

### Example 4: Nested Dependent Loops

Analysis of nested loops where the inner loop bound depends on the outer loop variable:

```
Algorithm DependentLoops(n)
 for i ← 1 to n do
 for j ← 1 to i do
 operation
 end for
 end for
```

**Summation setup**:
T(n) = Σᵢ₌₁ⁿ Σⱼ₌₁ⁱ 1 = Σᵢ₌₁ⁱ i

**Evaluation**:
T(n) = n(n+1)/2 = (n² + n)/2

**Asymptotic notation**: Θ(n²)

## Common Summation Formulas

The analysis of algorithms frequently employs the following summation identities:

1. **Arithmetic series**: Σᵢ₌₁ⁿ i = n(n+1)/2 = Θ(n²)
2. **Sum of squares**: Σᵢ₌₁ⁿ i² = n(n+1)(2n+1)/6 = Θ(n³)
3. **Geometric series**: Σᵢ₌₀ⁿ rⁱ = (rⁿ⁺¹ - 1)/(r - 1) for r ≠ 1

- When 0 < r < 1: Θ(1)
- When r > 1: Θ(rⁿ)

4. **Harmonic series**: Σᵢ₌₁ⁿ 1/i = Hₙ = ln n + γ + O(1/n) = Θ(log n)

## Case Analysis

### Best, Worst, and Average Case

Algorithm performance varies based on input characteristics:

- **Best Case**: Input arrangement yielding minimum running time. For linear search, best case occurs when target is at first position: Ω(1)
- **Worst Case**: Input arrangement yielding maximum running time. For linear search, worst case occurs when element is absent: O(n)
- **Average Case**: Expected performance over all possible inputs, typically assuming uniform distribution

### Space Complexity

Space complexity S(n) measures memory requirements as a function of input size, including:

- Input data storage
- Auxiliary space for variables and data structures
- Stack space (for recursive algorithms, though not applicable here)

## Complexity Hierarchy

The following hierarchy organizes complexity classes by growth rate:

| Complexity   | Notation   | Example Algorithm           |
| ------------ | ---------- | --------------------------- |
| Constant     | Θ(1)       | Array index access          |
| Logarithmic  | Θ(log n)   | Binary search               |
| Linear       | Θ(n)       | Linear search, traversal    |
| Linearithmic | Θ(n log n) | Merge sort, heap sort       |
| Quadratic    | Θ(n²)      | Bubble sort, selection sort |
| Cubic        | Θ(n³)      | Naive matrix multiplication |
| Exponential  | Θ(2ⁿ)      | Subset generation           |
| Factorial    | Θ(n!)      | Permutation generation      |

## Conclusion

The mathematical analysis of non-recursive algorithms provides the rigorous foundation for algorithm performance evaluation. Mastery of step-count methods, summation techniques, and asymptotic notation enables systematic quantification of time and space requirements. This analytical framework empowers practitioners to make informed decisions regarding algorithm selection and optimization strategies for real-world computational problems.
