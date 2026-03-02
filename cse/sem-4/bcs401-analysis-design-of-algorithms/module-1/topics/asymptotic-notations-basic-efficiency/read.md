# Asymptotic Notations and Basic Efficiency Classes

## Table of Contents

- [Asymptotic Notations and Basic Efficiency Classes](#asymptotic-notations-and-basic-efficiency-classes)
- [Introduction](#introduction)
- [Formal Definitions of Asymptotic Notations](#formal-definitions-of-asymptotic-notations)
  - [Big O Notation (Upper Bound)](#big-o-notation-upper-bound)
  - [Big Omega Notation (Lower Bound)](#big-omega-notation-lower-bound)
  - [Big Theta Notation (Tight Bound)](#big-theta-notation-tight-bound)
  - [Little o Notation (Strict Upper Bound)](#little-o-notation-strict-upper-bound)
  - [Little Omega Notation (Strict Lower Bound)](#little-omega-notation-strict-lower-bound)
- [Properties of Asymptotic Notations](#properties-of-asymptotic-notations)
  - [Theorem 1: Transitivity](#theorem-1-transitivity)
  - [Theorem 2: Reflexivity](#theorem-2-reflexivity)
  - [Theorem 3: Symmetry](#theorem-3-symmetry)
  - [Theorem 4: Transpose Symmetry](#theorem-4-transpose-symmetry)
- [Basic Efficiency Classes](#basic-efficiency-classes)
- [Worked Examples](#worked-examples)
  - [Example 1: Analyzing Nested Loops](#example-1-analyzing-nested-loops)
  - [Example 2: Proving a Tight Bound](#example-2-proving-a-tight-bound)
- [Comparative Analysis of Notations](#comparative-analysis-of-notations)
- [Summary](#summary)

## Introduction

Algorithm analysis constitutes a fundamental discipline within computer science, providing systematic methodologies for evaluating algorithmic efficiency in terms of time and space requirements. Rather than measuring absolute execution time on specific hardware, asymptotic analysis examines how an algorithm's performance scales with input size n, enabling meaningful comparisons across different implementations and hardware platforms. Asymptotic notations provide the mathematical framework for expressing these growth rates precisely.

The study of asymptotic notations is essential for several reasons: it enables objective comparison between competing algorithms, guides informed design choices when solving computational problems, and establishes theoretical lower bounds on problem complexity. This knowledge forms the bedrock for understanding more advanced topics in algorithm design, including divide-and-conquer strategies, dynamic programming, and NP-completeness theory.

## Formal Definitions of Asymptotic Notations

### Big O Notation (Upper Bound)

**Definition 1 (Constant-based):** A function f(n) is said to be O(g(n)) if there exist positive constants c and n₀ such that:
$$0 \leq f(n) \leq c \cdot g(n) \quad \text{for all } n \geq n_0$$

**Definition 2 (Limit-based):** Alternatively, f(n) = O(g(n)) if:
$$\lim_{n \to \infty} \frac{f(n)}{g(n)} = c \quad \text{where } c \text{ is a finite constant}$$

**Theorem:** If f(n) = 2n² + 3n + 1, then f(n) = O(n²).

_Proof:_ We need to find constants c and n₀ such that 2n² + 3n + 1 ≤ c·n² for all n ≥ n₀.

For n ≥ 1:
2n² + 3n + 1 ≤ 2n² + 3n² + n² = 6n²

Thus, choosing c = 6 and n₀ = 1, we have f(n) ≤ 6n² for all n ≥ 1. Therefore, f(n) = O(n²). ∎

### Big Omega Notation (Lower Bound)

**Definition 1 (Constant-based):** A function f(n) is said to be Ω(g(n)) if there exist positive constants c and n₀ such that:
$$0 \leq c \cdot g(n) \leq f(n) \quad \text{for all } n \geq n_0$$

**Definition 2 (Limit-based):** f(n) = Ω(g(n)) if:
$$\lim_{n \to \infty} \frac{f(n)}{g(n)} = c \quad \text{where } c > 0 \text{ (finite or infinite)}$$

**Example:** Any algorithm performing linear search on an unsorted array has Ω(1) time complexity in the best case when the target element is found at the first position.

### Big Theta Notation (Tight Bound)

**Definition 1 (Constant-based):** A function f(n) is said to be Θ(g(n)) if there exist positive constants c₁, c₂, and n₀ such that:
$$0 \leq c_1 \cdot g(n) \leq f(n) \leq c_2 \cdot g(n) \quad \text{for all } n \geq n_0$$

**Definition 2 (Limit-based):** f(n) = Θ(g(n)) if:
$$0 < \lim_{n \to \infty} \frac{f(n)}{g(n)} < \infty$$

**Theorem:** f(n) = Θ(g(n)) if and only if f(n) = O(g(n)) and f(n) = Ω(g(n)).

### Little o Notation (Strict Upper Bound)

**Definition:** A function f(n) is said to be o(g(n)) if for any positive constant c, there exists n₀ such that:
$$0 \leq f(n) < c \cdot g(n) \quad \text{for all } n \geq n_0$$

Equivalently: f(n) = o(g(n)) iff $\lim_{n \to \infty} \frac{f(n)}{g(n)} = 0$

**Example:** n = o(n²) because lim(n/n²) = lim(1/n) = 0, but n ≠ o(n).

### Little Omega Notation (Strict Lower Bound)

**Definition:** A function f(n) is said to be ω(g(n)) if for any positive constant c, there exists n₀ such that:
$$f(n) > c \cdot g(n) \quad \text{for all } n \geq n_0$$

Equivalently: f(n) = ω(g(n)) iff $\lim_{n \to \infty} \frac{f(n)}{g(n)} = \infty$

**Example:** n² = ω(n) because lim(n²/n) = lim(n) = ∞.

## Properties of Asymptotic Notations

### Theorem 1: Transitivity

If f(n) = O(g(n)) and g(n) = O(h(n)), then f(n) = O(h(n)).
Similarly, f(n) = Ω(g(n)) and g(n) = Ω(h(n)) implies f(n) = Ω(h(n)), and f(n) = Θ(g(n)) and g(n) = Θ(h(n)) implies f(n) = Θ(h(n)).

_Proof:_ Since f(n) = O(g(n)), there exist c₁, n₁ such that f(n) ≤ c₁g(n) for n ≥ n₁. Since g(n) = O(h(n)), there exist c₂, n₂ such that g(n) ≤ c₂h(n) for n ≥ n₂. For n ≥ max(n₁, n₂):
f(n) ≤ c₁g(n) ≤ c₁c₂h(n)

Thus, choosing c = c₁c₂ and n₀ = max(n₁, n₂), we have f(n) ≤ ch(n). Therefore, f(n) = O(h(n)). ∎

### Theorem 2: Reflexivity

For any function f(n), we have f(n) = O(f(n)), f(n) = Ω(f(n)), and f(n) = Θ(f(n)).

_Proof:_ For f(n) = O(f(n)): choose c = 1 and n₀ = 1. Then 0 ≤ f(n) ≤ 1·f(n) for all n ≥ 1. The proofs for Ω and Θ follow similarly. ∎

### Theorem 3: Symmetry

f(n) = Θ(g(n)) if and only if g(n) = Θ(f(n)).

_Proof:_ By definition, f(n) = Θ(g(n)) means f(n) = O(g(n)) and f(n) = Ω(g(n)). From transpose symmetry (proved below), f(n) = Ω(g(n)) implies g(n) = O(f(n)), and f(n) = O(g(n)) implies g(n) = Ω(f(n)). Combining both gives g(n) = Θ(f(n)). ∎

### Theorem 4: Transpose Symmetry

f(n) = O(g(n)) if and only if g(n) = Ω(f(n)).
Similarly, f(n) = o(g(n)) if and only if g(n) = ω(f(n)).

_Proof:_ f(n) = O(g(n)) means ∃c, n₀ such that f(n) ≤ cg(n) for n ≥ n₀. Rearranging: g(n) ≥ (1/c)f(n) for n ≥ n₀. This is precisely the definition of g(n) = Ω(f(n)). ∎

## Basic Efficiency Classes

The following table presents the standard efficiency classes in increasing order of growth rate, along with canonical algorithmic examples:

| Complexity | Name         | Example Algorithms                                          |
| ---------- | ------------ | ----------------------------------------------------------- |
| O(1)       | Constant     | Array access, hash table lookup, stack push/pop             |
| O(log n)   | Logarithmic  | Binary search, balanced BST operations, Fibonacci heap      |
| O(n)       | Linear       | Linear search, array traversal, finding min/max             |
| O(n log n) | Linearithmic | Merge Sort, Heap Sort, Quick Sort (average case)            |
| O(n²)      | Quadratic    | Bubble Sort, Insertion Sort, Selection Sort                 |
| O(n³)      | Cubic        | Naive matrix multiplication, Floyd-Warshall algorithm       |
| O(2ⁿ)      | Exponential  | Tower of Hanoi, generating all subsets, recursive Fibonacci |
| O(n!)      | Factorial    | Generating all permutations, brute-force TSP                |

## Worked Examples

### Example 1: Analyzing Nested Loops

**Problem:** Determine the time complexity of the following code:

```python
sum = 0
for i in range(1, n+1):
 for j in range(1, i+1):
 sum = sum + 1
```

**Solution:** The outer loop runs n times. For each value of i, the inner loop runs i times. Therefore, the total number of iterations is:
$$T(n) = \sum_{i=1}^{n} i = \frac{n(n+1)}{2} = \frac{n^2 + n}{2}$$

Using limit analysis:
$$\lim_{n \to \infty} \frac{T(n)}{n^2} = \lim_{n \to \infty} \frac{n^2 + n}{2n^2} = \frac{1}{2}$$

Since the limit is a finite positive constant, T(n) = Θ(n²).

### Example 2: Proving a Tight Bound

**Problem:** Prove that 3n³ + 2n log n + 5 = Θ(n³).

**Solution:** We need to find constants c₁, c₂, and n₀ such that:
c₁n³ ≤ 3n³ + 2n log n + 5 ≤ c₂n³ for all n ≥ n₀

**Upper Bound:** For n ≥ 1:
3n³ + 2n log n + 5 ≤ 3n³ + 2n³ + 5n³ = 10n³
Thus, c₂ = 10 works with n₀ = 1.

**Lower Bound:** For n ≥ 1:
3n³ + 2n log n + 5 ≥ 3n³
Thus, c₁ = 3 works with n₀ = 1.

Therefore, 3n³ + 2n log n + 5 = Θ(n³).

## Comparative Analysis of Notations

The relationship between the five asymptotic notations can be understood through limit behavior:

| Notation | Relationship | Limit Condition  |
| -------- | ------------ | ---------------- |
| f = O(g) | f ≤ g        | lim(f/g) = c < ∞ |
| f = Ω(g) | f ≥ g        | lim(f/g) = c > 0 |
| f = Θ(g) | f ≈ g        | 0 < lim(f/g) < ∞ |
| f = o(g) | f < g        | lim(f/g) = 0     |
| f = ω(g) | f > g        | lim(f/g) = ∞     |

## Summary

Asymptotic notations provide the mathematical foundation for algorithm efficiency analysis. Big O establishes worst-case upper bounds, Big Omega provides best-case lower bounds, and Big Theta gives tight bounds when both coincide. The properties of transitivity, reflexivity, symmetry, and transpose symmetry enable systematic manipulation of these notations. Understanding efficiency classes from O(1) to O(n!) is crucial for algorithm selection and design, particularly recognizing that exponential and factorial algorithms become impractical for moderately large inputs.
