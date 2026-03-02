# Mathematical Analysis of Recursive Algorithms

## Table of Contents

- [Mathematical Analysis of Recursive Algorithms](#mathematical-analysis-of-recursive-algorithms)
- [Introduction](#introduction)
- [Recurrence Relations](#recurrence-relations)
  - [Definition and Structure](#definition-and-structure)
  - [Examples of Common Recurrences](#examples-of-common-recurrences)
- [The Substitution Method](#the-substitution-method)
  - [Overview and Procedure](#overview-and-procedure)
  - [Worked Example: Proving $T(n) = 2T(n/2) + n = O(n \log n)$](#worked-example-proving-tn--2tn2--n--on-log-n)
  - [Subtleties in Substitution Method](#subtleties-in-substitution-method)
- [The Recursion Tree Method](#the-recursion-tree-method)
  - [Conceptual Framework](#conceptual-framework)
  - [Analysis Procedure](#analysis-procedure)
  - [Worked Example: $T(n) = 3T(n/4) + n^2$](#worked-example-tn--3tn4--n2)
- [The Master Theorem](#the-master-theorem)
  - [Statement of the Theorem](#statement-of-the-theorem)
  - [Intuition and Proof Sketch](#intuition-and-proof-sketch)
  - [Worked Examples](#worked-examples)
  - [Limitations of the Master Theorem](#limitations-of-the-master-theorem)
- [Space Complexity of Recursive Algorithms](#space-complexity-of-recursive-algorithms)
- [Summary Table: Common Recurrence Patterns](#summary-table-common-recurrence-patterns)
- [Conclusion](#conclusion)

## Introduction

Recursive algorithms constitute fundamental computational constructs wherein a function calls itself to solve progressively smaller instances of the same problem. The mathematical analysis of recursive algorithms is essential for understanding their time and space complexity, enabling practitioners to design efficient software systems. Unlike iterative algorithms where complexity can be directly observed from loop structures, recursive algorithms require specialized mathematical techniques to analyze their computational behavior accurately.

The analysis of recursive algorithms involves formulating recurrence relations that capture the relationship between problem size and the computational resources required to solve it. This analysis builds upon asymptotic notation concepts (Big-O, Big-Ω, Θ) and provides practical tools for determining the computational complexity of recursive algorithms. Understanding these analysis techniques is particularly important for computer science students, as recursive algorithms appear frequently in sorting algorithms (merge sort, quicksort), searching algorithms (binary search), tree traversals, graph algorithms, and divide-and-conquer paradigms.

This module covers several powerful methods for solving recurrence relations: the substitution method, the recursion-tree method, and the Master Theorem. Each technique possesses distinct strengths and is suited for different types of recurrences. Mastery of these methods enables programmers to make informed decisions regarding algorithm selection and optimization.

## Recurrence Relations

### Definition and Structure

A recurrence relation is a mathematical equation that defines a sequence recursively, where each term is defined in terms of previous terms. In algorithm analysis, we express the running time $T(n)$ as a function of the input size $n$, capturing how the computational cost grows with problem dimensions.

A typical recurrence relation follows a two-part structure:

**Base Case:** $T(n) = \Theta(1)$ for sufficiently small $n$, representing the cost of solving the smallest detectable problem directly without further recursion.

**Recursive Case:** $T(n) = aT(n/b) + f(n)$, where $a \geq 1$ denotes the number of subproblems, $b > 1$ represents the factor by which the problem size is divided, and $f(n)$ denotes the cost of dividing the problem and combining results.

This canonical form is known as the divide-and-conquer recurrence, where $a$ subproblems, each of size $n/b$, are solved recursively, and the cost of combining their solutions is given by $f(n)$.

### Examples of Common Recurrences

- **Binary Search:** $T(n) = T(n/2) + \Theta(1)$ — one subproblem of half the size with constant overhead
- **Merge Sort:** $T(n) = 2T(n/2) + \Theta(n)$ — two subproblems of half size with linear merging cost
- **QuickSort (average case):** $T(n) = 2T(n/2) + \Theta(n)$ — identical to merge sort
- **Binary Search Tree Construction:** $T(n) = 2T(n/2) + \Theta(1)$ — two subproblems with constant overhead
- **Strassen's Matrix Multiplication:** $T(n) = 7T(n/2) + \Theta(n^2)$ — seven subproblems with quadratic combining cost

## The Substitution Method

### Overview and Procedure

The substitution method, also known as the method of guessing and verifying, provides a powerful technique for establishing asymptotic bounds on recurrence relations. This method involves two distinct phases: first, guessing the form of the solution based on intuition or pattern recognition, and second, employing mathematical induction to prove the correctness of this guess.

**Step 1: Guess the form of the solution** — Based on the structure of the recurrence or by analyzing a few initial terms, hypothesize an asymptotic bound such as $T(n) = O(n \log n)$ or $T(n) = \Theta(n^2)$.

**Step 2: Verify through induction** — Assume the bound holds for all values smaller than $n$, substitute this assumption into the recurrence, and demonstrate that the resulting expression satisfies the proposed bound.

### Worked Example: Proving $T(n) = 2T(n/2) + n = O(n \log n)$

**Problem:** Prove that the recurrence $T(n) = 2T(n/2) + n$ with $T(1) = \Theta(1)$ has solution $T(n) = O(n \log n)$ using the substitution method.

**Proof by Induction:**

We claim there exists a constant $c > 0$ such that $T(n) \leq c n \log_2 n$ for all $n \geq 2$.

**Base Case:** For $n = 2$, we require $T(2) \leq c \cdot 2 \cdot \log_2 2 = 2c$. Since $T(2) = 2T(1) + 2 = \Theta(1) + 2 = O(1)$, we can choose a sufficiently large $c$ to satisfy this inequality.

**Inductive Hypothesis:** Assume $T(m) \leq c m \log_2 m$ holds for all $m$ where $2 \leq m < n$.

**Inductive Step:** Consider $T(n)$:

$$T(n) = 2T(n/2) + n$$
$$\leq 2 \cdot c \cdot (n/2) \cdot \log_2(n/2) + n \quad \text{(by inductive hypothesis)}$$
$$= cn \cdot (\log_2 n - \log_2 2) + n$$
$$= cn \log_2 n - cn + n$$
$$\leq cn \log_2 n \quad \text{(for any } c \geq 1\text{)}$$

Thus, by mathematical induction, $T(n) \leq c n \log_2 n$, establishing that $T(n) = O(n \log n)$.

### Subtleties in Substitution Method

The substitution method requires careful handling of several technical aspects. Establishing tight upper bounds often necessitates subtracting lower-order terms from the guessed solution. For recurrences with floors or ceilings, additional care must be taken to handle the boundary conditions correctly. When proving $\Omega$-bounds, the inequality direction reverses, requiring different manipulation strategies.

## The Recursion Tree Method

### Conceptual Framework

The recursion tree method provides an intuitive visualization of recursive algorithm execution by modeling each level of the recursion as a node in a tree structure. This approach decomposes the total cost of a recurrence into the sum of costs incurred at each level of the recursion, enabling systematic analysis through level-by-level cost aggregation.

**Structure of a Recursion Tree:**

- **Root Node:** Represents the cost $f(n)$ at the original problem size $n$
- **Internal Nodes:** Represent the cost of dividing the problem at each recursive call
- **Leaves:** Represent the base cases where recursion terminates
- **Total Cost:** The sum of costs at all levels of the tree

### Analysis Procedure

For a recurrence $T(n) = aT(n/b) + f(n)$, the recursion tree analysis proceeds as follows:

1. **Determine the number of levels:** The recursion terminates when the problem size reaches the base case. Since each level reduces the problem size by a factor of $b$, the number of levels $L$ satisfies $n/b^L = 1$, yielding $L = \log_b n$.

2. **Compute the cost at each level:** At level $i$ (where $i = 0$ is the root), there are $a^i$ nodes, each handling a subproblem of size $n/b^i$. The cost at level $i$ equals $a^i \cdot f(n/b^i)$.

3. **Sum the costs across all levels:** The total cost is $\sum_{i=0}^{L-1} a^i \cdot f(n/b^i)$ plus the cost at the leaves.

### Worked Example: $T(n) = 3T(n/4) + n^2$

**Problem:** Solve $T(n) = 3T(n/4) + n^2$ using the recursion tree method.

**Level-by-Level Analysis:**

At level $i$, there are $3^i$ subproblems, each of size $n/4^i$. The cost at level $i$ equals:

$$\text{Cost at level } i = 3^i \cdot \left(\frac{n}{4^i}\right)^2 = 3^i \cdot \frac{n^2}{16^i} = n^2 \cdot \left(\frac{3}{16}\right)^i$$

The recursion terminates when $n/4^k = 1$, giving $k = \log_4 n$ levels.

**Total Cost Calculation:**

$$T(n) = n^2 \sum_{i=0}^{\log_4 n - 1} \left(\frac{3}{16}\right)^i$$

This is a geometric series with ratio $r = 3/16 < 1$. For a geometric series with $|r| < 1$:

$$\sum_{i=0}^{m-1} r^i = \frac{1 - r^m}{1 - r} = O(1) \text{ as } m \to \infty$$

Therefore:

$$T(n) = n^2 \cdot O(1) = \Theta(n^2)$$

The recursion tree reveals that the total cost is dominated by the root level, yielding $\Theta(n^2)$ as the asymptotic solution.

## The Master Theorem

### Statement of the Theorem

The Master Theorem provides a direct, closed-form solution for recurrences of the standard divide-and-conquer form $T(n) = aT(n/b) + f(n)$, where $a \geq 1$, $b > 1$, and $f(n)$ is asymptotically positive.

Let $f(n) = \Theta(n^d)$ where $d \geq 0$. Then the asymptotic behavior of $T(n)$ is determined by comparing $a$ with $b^d$:

**Case 1 (Polynomial smaller):** If $a < b^d$, then $T(n) = \Theta(n^d)$

**Case 2 (Polynomial equal):** If $a = b^d$, then $T(n) = \Theta(n^d \log n)$

**Case 3 (Polynomial larger):** If $a > b^d$, then $T(n) = \Theta(n^{\log_b a})$

### Intuition and Proof Sketch

The three cases of the Master Theorem correspond to different relationships between the cost of combining solutions $f(n)$ and the cost of solving subproblems, which is proportional to $n^{\log_b a}$ (the total work performed at the leaves of the recursion tree).

- **Case 1:** When $f(n)$ grows more slowly than $n^{\log_b a}$, the leaf-level computation dominates. The total cost is determined by the leaves, yielding $\Theta(n^{\log_b a})$, which equals $\Theta(n^d)$ since $a < b^d$.

- **Case 2:** When $f(n)$ grows at the same rate as $n^{\log_b a}$, the costs are balanced across all levels. The number of levels ($\log_b n$) determines the total cost, yielding $\Theta(n^d \log n)$.

- **Case 3:** When $f(n)$ grows more rapidly than $n^{\log_b a}$, the root-level combination cost dominates. The total cost is determined by the cost at the root, yielding $\Theta(f(n)) = \Theta(n^d)$.

### Worked Examples

**Example 1: Binary Search**
$$T(n) = T(n/2) + \Theta(1)$$

- Parameters: $a = 1$, $b = 2$, $f(n) = \Theta(n^0)$ with $d = 0$
- Comparison: $a = 1$, $b^d = 2^0 = 1$, so $a = b^d$
- Application: Case 2 applies
- Conclusion: $T(n) = \Theta(n^0 \log n) = \Theta(\log n)$

**Example 2: Merge Sort**
$$T(n) = 2T(n/2) + \Theta(n)$$

- Parameters: $a = 2$, $b = 2$, $f(n) = \Theta(n)$ with $d = 1$
- Comparison: $a = 2$, $b^d = 2^1 = 2$, so $a = b^d$
- Application: Case 2 applies
- Conclusion: $T(n) = \Theta(n \log n)$

**Example 3: Strassen's Matrix Multiplication**
$$T(n) = 7T(n/2) + \Theta(n^2)$$

- Parameters: $a = 7$, $b = 2$, $f(n) = \Theta(n^2)$ with $d = 2$
- Comparison: $a = 7$, $b^d = 2^2 = 4$, so $a > b^d$
- Application: Case 3 applies
- Conclusion: $T(n) = \Theta(n^{\log_2 7}) \approx \Theta(n^{2.807})$

### Limitations of the Master Theorem

The Master Theorem does not apply when:

1. $f(n)$ is not polynomially bounded by $n^d$
2. The regularity condition for Case 3 ($af(n/b) \leq cf(n)$ for some $c < 1$) is not satisfied
3. $a$ is not a constant (e.g., $a = n$)

For such recurrences, alternative methods such as the Akra-Bazzi theorem or change of variables may be required.

## Space Complexity of Recursive Algorithms

Space complexity analysis for recursive algorithms considers both the call stack depth and auxiliary space requirements. The maximum depth of the recursion tree often determines the stack space complexity, while auxiliary space accounts for additional data structures used by the algorithm.

**Binary Search:** $O(\log n)$ stack space — the recursion depth equals the number of levels in the recursion tree, with each level maintaining only constant local variables.

**Merge Sort:** $O(n)$ auxiliary space plus $O(\log n)$ stack space — the auxiliary array for merging requires linear space, while the recursion depth contributes logarithmic stack space.

**QuickSort (worst case):** $O(n)$ stack space — when the pivot selection consistently produces highly unbalanced partitions, the recursion depth can degrade to $n$.

**Fibonacci (naive recursive):** $O(n)$ stack depth — each recursive call maintains its own frame, and the maximum depth of unevaluated calls equals $n$.

## Summary Table: Common Recurrence Patterns

| Algorithm         | Recurrence                           | Solution            | Case |
| ----------------- | ------------------------------------ | ------------------- | ---- |
| Binary Search     | $T(n) = T(n/2) + \Theta(1)$          | $\Theta(\log n)$    | 2    |
| Merge Sort        | $T(n) = 2T(n/2) + \Theta(n)$         | $\Theta(n \log n)$  | 2    |
| QuickSort (avg)   | $T(n) = 2T(n/2) + \Theta(n)$         | $\Theta(n \log n)$  | 2    |
| Heap Sort         | $T(n) = 2T(n/2) + \Theta(1)$         | $\Theta(n)$         | 1    |
| Strassen's        | $T(n) = 7T(n/2) + \Theta(n^2)$       | $\Theta(n^{2.807})$ | 3    |
| Fibonacci (naive) | $T(n) = T(n-1) + T(n-2) + \Theta(1)$ | $\Theta(\phi^n)$    | N/A  |
| Towers of Hanoi   | $T(n) = 2T(n-1) + \Theta(1)$         | $\Theta(2^n)$       | N/A  |

## Conclusion

The mathematical analysis of recursive algorithms through recurrence relations provides essential tools for algorithm design and optimization. The substitution method offers a flexible approach for establishing bounds through mathematical induction, while the recursion tree method provides intuitive visualization of recursive cost distribution. The Master Theorem enables rapid analysis of standard divide-and-conquer recurrences, yielding immediate complexity results for many practical algorithms.

Proficiency in these techniques enables computer science practitioners to analyze existing algorithms, evaluate design alternatives, and make data-driven decisions regarding algorithm selection. These skills form a foundational component of algorithmic competence and are essential for advanced study and professional practice in computer science.
