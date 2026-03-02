# Fundamentals of Algorithmic Problem Solving

## Table of Contents

- [Fundamentals of Algorithmic Problem Solving](#fundamentals-of-algorithmic-problem-solving)
- [1. Introduction](#1-introduction)
- [2. Problem Specification and Classification](#2-problem-specification-and-classification)
  - [2.1 Formal Problem Definition](#21-formal-problem-definition)
  - [2.2 Problem Classification](#22-problem-classification)
- [3. Algorithm Specification](#3-algorithm-specification)
  - [3.1 Formal Definition and Properties](#31-formal-definition-and-properties)
  - [3.2 Pseudo-code Conventions](#32-pseudo-code-conventions)
- [4. Algorithm Design Paradigms](#4-algorithm-design-paradigms)
  - [4.1 Brute Force Approach](#41-brute-force-approach)
  - [4.2 Divide and Conquer](#42-divide-and-conquer)
  - [4.3 Greedy Method](#43-greedy-method)
  - [4.4 Dynamic Programming](#44-dynamic-programming)
- [5. Algorithm Verification and Correctness](#5-algorithm-verification-and-correctness)
  - [5.1 Testing Methodology](#51-testing-methodology)
  - [5.2 Formal Verification through Invariants](#52-formal-verification-through-invariants)
  - [5.3 Mathematical Induction Proof](#53-mathematical-induction-proof)
- [6. Complexity Analysis](#6-complexity-analysis)
  - [6.1 Asymptotic Notation](#61-asymptotic-notation)
  - [6.2 Common Complexity Classes](#62-common-complexity-classes)
  - [6.3 Recurrence Relations](#63-recurrence-relations)
- [7. Problem-Solving Strategies](#7-problem-solving-strategies)
  - [7.1 Incremental Approach](#71-incremental-approach)
  - [7.2 Recursive Decomposition](#72-recursive-decomposition)
  - [7.3 Backtracking](#73-backtracking)
  - [7.4 Branch and Bound](#74-branch-and-bound)
- [8. Illustrative Example](#8-illustrative-example)
  - [8.1 Maximum Subarray Problem](#81-maximum-subarray-problem)
- [Assessment](#assessment)
  - [Multiple Choice Questions](#multiple-choice-questions)
- [Flashcard](#flashcard)

## 1. Introduction

Algorithmic problem solving constitutes the systematic methodology for designing computational solutions through well-defined sequences of steps. It represents the foundational pillar of computer science and software engineering, providing the intellectual framework for transforming abstract problem statements into executable computational procedures. Within the Analysis and Design of Algorithms curriculum, this domain establishes the theoretical and practical foundations essential for rigorous algorithm development.

The significance of algorithmic competence extends substantially beyond curricular requirements. Efficient algorithm design determines the performance characteristics of computational systems across diverse applications, from embedded systems to distributed computing platforms. The ability to decompose complex problems into tractable subproblems and construct optimal or near-optimal solutions distinguishes professional software engineers from novice programmers. Furthermore, algorithmic reasoning forms the basis of technical interviews and competitive programming, making mastery essential for career advancement in the software industry.

## 2. Problem Specification and Classification

### 2.1 Formal Problem Definition

A computational problem comprises three essential components: the input specification (the set of valid instances), the output specification (the required relationship between input and output), and the constraint specification (limitations on computational resources). Formally, a problem P is defined as a relation P ⊆ I × O, where I represents the input space and O represents the output space. An algorithm A solves problem P if ∀i ∈ I, A(i) = p(i) where p(i) is the correct output for input i.

**Instance**: A specific input chosen from the input space. **Problem Size**: A measure of the input magnitude, typically denoted by n, which may represent the number of elements, vertices, or bits required to represent the instance.

### 2.2 Problem Classification

Problems are categorized based on their structural characteristics and computational complexity:

| Category     | Description                           | Representative Problems        |
| ------------ | ------------------------------------- | ------------------------------ |
| Sorting      | Arranging elements in specified order | Merge Sort, Quick Sort         |
| Searching    | Finding elements satisfying criteria  | Binary Search, BFS/DFS         |
| Graph        | Operations on graph structures        | Shortest Path, MST             |
| String       | Text processing and pattern matching  | KMP, Rabin-Karp                |
| Mathematical | Numerical computations                | Matrix multiplication, FFT     |
| Geometric    | Spatial relationships                 | Convex Hull, Line Intersection |

**Complexity Classification**: Problems are classified as tractable (solvable in polynomial time P), intractable (NP-complete/NP-hard), or unsolvable (undecidable). This classification guides algorithm selection and informs expectations regarding optimal solution availability.

## 3. Algorithm Specification

### 3.1 Formal Definition and Properties

An algorithm is a finite sequence of well-defined instructions that transforms any valid input instance into a corresponding output. Algorithms must satisfy five fundamental properties:

1. **Finiteness**: The algorithm must terminate after executing a finite number of steps for every valid input.
2. **Definiteness**: Each instruction must be precisely defined and unambiguous.
3. **Input**: An algorithm accepts zero or more inputs from specified domains.
4. **Output**: An algorithm produces one or more outputs that satisfy the problem specification.
5. **Effectiveness**: Each operation must be basic enough to be executed directly.

### 3.2 Pseudo-code Conventions

Pseudo-code provides a language-independent representation combining programming constructs with natural language clarity. Standard conventions include assignment (←), loops (for, while), conditionals (if-then-else), and function definitions. The following pseudo-code illustrates the structure:

```
ALGORITHM Binary-Search(A[low..high], target)
 while low ≤ high do
 mid ← ⌊(low + high) / 2⌋
 if A[mid] = target then
 return mid
 else if A[mid] < target then
 low ← mid + 1
 else
 high ← mid - 1
 end if
 end while
 return NOT-FOUND
```

## 4. Algorithm Design Paradigms

### 4.1 Brute Force Approach

The brute force method systematically enumerates all candidate solutions and selects the optimal one. While conceptually straightforward, brute force solutions guarantee correctness but may prove computationally infeasible for large instances. The time complexity typically equals the size of the solution space.

**Applicability**: Small problem instances, when alternative approaches prove unavailable, or as baseline for optimization.

### 4.2 Divide and Conquer

The divide and conquer paradigm recursively decomposes problems into smaller, independent subproblems, solves each subproblem, and combines their solutions. Formally, given problem P with instance I:

1. **Divide**: Split I into sub-instances I₁, I₂, ..., Iₖ
2. **Conquer**: Recursively solve each subproblem
3. **Combine**: Merge solutions into unified result

**Complexity Analysis**: Using the Master Theorem, if T(n) = aT(n/b) + f(n) where a ≥ 1 and b > 1, then T(n) ∈ Θ(n^log_b a) when f(n) = O(n^log_b a - ε).

### 4.3 Greedy Method

Greedy algorithms make locally optimal choices at each step, hoping to achieve global optimality. This approach applies when the problem exhibits the **greedy-choice property** (optimal solution can be constructed from optimal sub-solutions) and **optimal substructure**.

**Proof Framework**: Greedy correctness requires demonstrating that any optimal solution contains the greedy choice as its initial decision. Counterexamples exist when local optimality fails to guarantee global optimality (e.g., fractional knapsack versus 0/1 knapsack).

### 4.4 Dynamic Programming

Dynamic programming optimizes recursive solutions by storing computed results, eliminating redundant calculations. Applicable when problems exhibit **optimal substructure** and **overlapping subproblems**. Two implementation approaches exist:

- **Top-down with Memoization**: Recursive computation with result caching
- **Bottom-up Tabulation**: Iterative building of solution table

**Time-Space Tradeoff**: DP typically reduces exponential time to polynomial time at the cost of additional space.

## 5. Algorithm Verification and Correctness

### 5.1 Testing Methodology

Testing validates algorithm behavior across representative input instances. **Exhaustive testing** examines all inputs (feasible only for small input spaces), while **randomized testing** samples inputs according to probability distributions. **Boundary testing** specifically targets edge cases.

Testing can reveal bugs but cannot guarantee correctness for all inputs.

### 5.2 Formal Verification through Invariants

**Loop Invariant**: A condition that holds true before and after each iteration of a loop, enabling formal correctness proofs.

**Proof Structure for Binary Search Invariants**:

- **Initialization**: Before first iteration, the invariant states: if target exists in A, it lies within A[low..high]. This holds because low=1, high=n initially.

- **Maintenance**: Assuming invariant holds at iteration start, three cases exist:
- If A[mid] = target, algorithm terminates correctly
- If A[mid] < target, target (if present) must be in upper half; low updates to mid+1 maintains invariant
- If A[mid] > target, target (if present) must be in lower half; high updates to mid-1 maintains invariant

- **Termination**: Loop terminates when low > high. By invariant, if target exists, it must be in empty range, proving target is absent. Otherwise, invariant guarantees search exhausted all possibilities.

### 5.3 Mathematical Induction Proof

For recursive algorithms, mathematical induction provides powerful correctness guarantees:

**Theorem**: Merge Sort produces a sorted output for any input array of length n.

**Proof by Induction**:

- **Base Case**: n = 1. Single element array is trivially sorted.
- **Inductive Hypothesis**: Assume Merge Sort correctly sorts all arrays of length less than n.
- **Inductive Step**: For array of length n, divide splits into subarrays of length ⌈n/2⌉ and ⌊n/2⌋. By hypothesis, recursive calls sort both subarrays. The merge procedure combines two sorted subarrays into a single sorted array by repeatedly selecting the smaller front element. This maintains sorted order, proving correctness for length n.

## 6. Complexity Analysis

### 6.1 Asymptotic Notation

Asymptotic notation provides theoretical bounds on algorithm performance independent of implementation details:

- **Big-O (Upper Bound)**: f(n) = O(g(n)) if ∃c, n₀ such that 0 ≤ f(n) ≤ cg(n) for all n ≥ n₀
- **Big-Ω (Lower Bound)**: f(n) = Ω(g(n)) if ∃c, n₀ such that 0 ≤ cg(n) ≤ f(n) for all n ≥ n₀
- **Big-Θ (Tight Bound)**: f(n) = Θ(g(n)) if f(n) = O(g(n)) and f(n) = Ω(g(n))

### 6.2 Common Complexity Classes

| Complexity Class | Notation   | Example Algorithm      | Growth Rate |
| ---------------- | ---------- | ---------------------- | ----------- |
| Constant         | O(1)       | Array index access     | 1           |
| Logarithmic      | O(log n)   | Binary search          | log n       |
| Linear           | O(n)       | Linear search          | n           |
| Linearithmic     | O(n log n) | Merge sort             | n log n     |
| Quadratic        | O(n²)      | Bubble sort            | n²          |
| Cubic            | O(n³)      | Floyd-Warshall         | n³          |
| Exponential      | O(2ⁿ)      | Power set enumeration  | 2ⁿ          |
| Factorial        | O(n!)      | Permutation generation | n!          |

### 6.3 Recurrence Relations

Solving recurrence relations determines time complexity for recursive algorithms:

**Substitution Method**: Guess solution and prove by induction

**Recursion Tree Method**: Expand recurrence to sum form

**Master Theorem**: For T(n) = aT(n/b) + f(n):

- If f(n) = O(n^log_b a - ε), then T(n) = Θ(n^log_b a)
- If f(n) = Θ(n^log_b a), then T(n) = Θ(n^log_b a log n)
- If f(n) = Ω(n^log_b a + ε) and regularity condition holds, T(n) = Θ(f(n))

## 7. Problem-Solving Strategies

### 7.1 Incremental Approach

The incremental strategy builds solutions by processing elements sequentially, maintaining an invariant state. This approach suits problems where partial solutions can be extended systematically.

**Example**: Insertion Sort maintains a sorted prefix, iteratively inserting each new element into its correct position.

### 7.2 Recursive Decomposition

Recursive strategies express solutions in terms of smaller instances of the same problem. Design requires identifying:

- **Base Case**: Smallest instance with direct solution
- **Recursive Case**: Reduction to smaller subproblems with solution combination

### 7.3 Backtracking

Backtracking systematically explores solution spaces by constructing partial solutions and abandoning paths that cannot lead to valid completions. The algorithm maintains feasibility constraints and prunes branches violating these constraints.

**N-Queens Problem**: Place n queens on n×n board with no attacks. Backtracking places queens column by column, backtracking when conflict arises.

### 7.4 Branch and Bound

Branch and bound extends backtracking by computing bounds on partial solutions, eliminating subspaces that cannot yield optimal solutions. Particularly effective for optimization problems with quantifiable solution quality measures.

## 8. Illustrative Example

### 8.1 Maximum Subarray Problem

**Problem**: Given array A[1..n], find contiguous subarray with maximum sum.

**Kadane's Algorithm (Dynamic Programming)**:

```
ALGORITHM Max-Subarray(A[1..n])
 max-sum ← -∞
 current-sum ← 0
 for i ← 1 to n do
 current-sum ← max(A[i], current-sum + A[i])
 max-sum ← max(max-sum, current-sum)
 end for
 return max-sum
```

**Correctness Proof**: Let DP[i] represent maximum subarray sum ending at position i. Recurrence: DP[i] = max(A[i], DP[i-1] + A[i]). The algorithm computes this recurrence iteratively, maintaining current-sum = DP[i] and max-sum = max(DP[1..i]). By induction on i, both variables correctly represent their definitions, proving correctness.

**Complexity**: O(n) time, O(1) space.

---

## Assessment

### Multiple Choice Questions

**Question 1**: Consider an algorithm with T(n) = 2T(n/2) + n². Using the Master Theorem, the asymptotic complexity is:

- A) Θ(n²)
- B) Θ(n² log n)
- C) Θ(n³)
- D) Θ(n)

**Correct Answer**: A
**Explanation**: Here a=2, b=2, f(n)=n². n^log_b a = n^log_2 2 = n. Since f(n) = Ω(n^(1+ε)) where ε=1, and the regularity condition a f(n/b) ≤ cf(n) holds (2 × (n/2)² = n²/2 ≤ cn² for c=1), Case 3 applies: T(n) = Θ(f(n)) = Θ(n²).

**Question 2**: Which algorithm design paradigm is most appropriate for the fractional knapsack problem but NOT for the 0/1 knapsack problem?

- A) Dynamic Programming
- B) Divide and Conquer
- C) Greedy Approach
- D) Brute Force

**Correct Answer**: C
**Explanation**: The greedy approach works optimally for fractional knapsack because the greedy-choice property holds—selecting items by value-to-weight ratio ensures global optimality. However, for 0/1 knapsack, greedy choices can lead to suboptimal solutions because items cannot be split, requiring DP for exact solutions.

**Question 3**: In the binary search algorithm, which loop invariant guarantees correctness?

- A) The target is always in the middle position of the search range
- B) If the target exists in the array, it is always within the current search range [low, high]
- C) The search range always contains exactly half the remaining elements
- D) The array is always sorted

**Correct Answer**: B
**Explanation**: The loop invariant for binary search states that if the target element exists in the array, it must lie within the current search range [low, high]. This invariant is established initially (low=1, high=n contains all elements) and maintained through updates to low and high based on comparison with A[mid]. When the loop terminates with low > high, the invariant guarantees the target is absent if not found earlier.

**Question 4**: An algorithm solves a problem of size n by dividing it into 4 subproblems of size n/2, combining solutions in O(n²) time. The total time complexity is:

- A) O(n²)
- B) O(n² log n)
- C) O(n^log₂⁴) = O(n²)
- D) O(n³)

**Correct Answer**: B
**Explanation**: Using the Master Theorem: T(n) = 4T(n/2) + n². Here a=4, b=2, so n^log_b a = n^log_2 4 = n². Since f(n) = Θ(n^log_b a), we are in Case 2, giving T(n) = Θ(n² log n).

**Question 5**: Which property is NOT required for dynamic programming to be applicable?

- A) Optimal Substructure
- B) Overlapping Subproblems
- C) Greedy-Choice Property
- C) The problem must be an optimization problem

**Correct Answer**: C
**Explanation**: Dynamic programming requires optimal substructure and overlapping subproblems, not greedy-choice property. Greedy-choice property is specifically required for greedy algorithms. DP can apply to both optimization and decision problems, so being an optimization problem is not strictly required.

---

## Flashcard

**Term**: Loop Invariant
**Definition**: A condition that holds true before loop initialization, is preserved through each iteration (maintenance), and provides useful information upon loop termination. Loop invariants enable formal correctness proofs for iterative algorithms by establishing the relationship between algorithm state and problem specification throughout execution.
