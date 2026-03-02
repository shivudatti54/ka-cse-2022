# Optimal Binary Search Trees


## Table of Contents

- [Optimal Binary Search Trees](#optimal-binary-search-trees)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Problem Formalization](#problem-formalization)
  - [Optimal Substructure Property](#optimal-substructure-property)
  - [Dynamic Programming Recurrence](#dynamic-programming-recurrence)
  - [Knuth's Optimization](#knuths-optimization)
  - [Algorithm Pseudocode](#algorithm-pseudocode)
  - [Time and Space Complexity](#time-and-space-complexity)
- [Examples](#examples)
  - [Example 1: Complete DP Table Computation](#example-1-complete-dp-table-computation)
  - [Example 2: Cost Verification](#example-2-cost-verification)
- [Exam Tips](#exam-tips)

## Introduction

The Optimal Binary Search Tree (OBST) problem is a classic dynamic programming problem that arises in the design of efficient search algorithms. In a standard Binary Search Tree (BST), the search time depends on the structure of the tree - a well-balanced tree provides O(log n) search time, while a skewed tree degrades to O(n). However, in many practical applications, we have prior knowledge about the frequency of searches for different keys. The OBST problem seeks to construct a binary search tree that minimizes the expected search cost given these access probabilities.

Unlike the optimal binary search tree problem which assumes a fixed search tree structure, OBST allows us to choose both the tree structure and which keys to store at each node. The problem assumes we have n distinct keys k₁, k₂, ..., kₙ arranged in sorted order, along with (n+1) dummy keys d₀, d₁, ..., dₙ representing unsuccessful searches. Each key kᵢ has an access probability pᵢ, and each dummy key dᵢ has a probability qᵢ of being searched. The sum of all probabilities must equal 1.

TheOBST problem has significant applications in compiler design (symbol tables), database indexing, and any system where efficient key lookup is critical. The solution employs dynamic programming due to the presence of optimal substructure - an optimal tree contains optimal subtrees.

## Key Concepts

### Problem Formalization

Given n sorted keys k₁ < k₂ < ... < kₙ with successful search probabilities p₁, p₂, ..., pₙ, and (n+1) dummy keys d₀, d₁, ..., dₙ with unsuccessful search probabilities q₀, q₁, ..., qₙ, where Σ(pᵢ + qᵢ) = 1, construct a binary search tree that minimizes the expected search cost.

**Definition 1 (Search Cost)**: The cost of accessing a key kᵢ in a binary search tree equals the number of comparisons needed, which is the depth of kᵢ plus 1. The cost of accessing a dummy key dᵢ equals the depth of dᵢ plus 1.

**Definition 2 (Weighted External Path Length)**: For a tree with keys at internal nodes and dummy keys at external positions (leaves), the weighted external path length is defined as:
E = Σ pᵢ × (depth(kᵢ) + 1) + Σ qᵢ × (depth(dᵢ) + 1)

This formula captures the total expected cost per search.

### Optimal Substructure Property

**Theorem (Optimal Substructure)**: If T is an optimal binary search tree for keys kᵢ through kⱼ (where i ≤ j), then:

1. The root of T must be some key kᵣ where i ≤ r ≤ j
2. The left subtree of T must be an optimal binary search tree for keys kᵢ through kᵣ₋₁
3. The right subtree of T must be an optimal binary search tree for keys kᵣ₊₁ through kⱼ

**Proof of Optimal Substructure**: Consider an optimal tree T with root kᵣ. Suppose the left subtree L is not optimal for keys kᵢ through kᵣ₋₁. Then there exists a better tree L' with lower cost. Replacing L with L' in T would produce a tree with lower total cost than T, contradicting the optimality of T. The same argument applies to the right subtree. ∎

### Dynamic Programming Recurrence

Let e[i][j] denote the expected search cost of an optimal binary search tree for keys kᵢ₊₁ through kⱼ (using 1-based indexing with i representing the count of keys in the left portion). Alternatively, using 0-based indexing where e[i][j] represents keys kᵢ through kⱼ₋₁, we define:

**Recurrence Relation**:

```
e[i][j] = w[i][j] + min{e[i][r-1] + e[r+1][j]} for r in [i, j]
```

Where w[i][j] = Σ(pₖ + qₖ) for k from i to j represents the sum of all probabilities in the subtree.

The base cases are:

- e[i][i-1] = qᵢ₋₁ (cost of empty tree with only dummy key dᵢ₋₁)
- w[i][i-1] = qᵢ₋₁

**Root Table**: We also maintain root[i][j] to store which key is chosen as root for the subtree keys kᵢ through kⱼ.

### Knuth's Optimization

A significant optimization was discovered by Knuth (1971) that reduces the time complexity. **Knuth's Optimization** states that for the optimal binary search tree problem, the optimal root indices satisfy:

root[i][j-1] ≤ root[i][j] ≤ root[i+1][j]

This monotonicity property allows us to restrict the search space for each subtree, reducing the time complexity from O(n³) to O(n²).

### Algorithm Pseudocode

```
OPTIMAL-BST(p, q, n)
    let e[1..n+1][0..n] and root[1..n][1..n] be new tables

    // Base case: empty tree
    for i = 1 to n+1
        e[i][i-1] = q[i-1]
        w[i][i-1] = q[i-1]

    // Length of subtree
    for length = 1 to n
        for i = 1 to n-length+1
            j = i + length - 1

            e[i][j] = ∞
            w[i][j] = w[i][j-1] + p[j] + q[j]

            // Try all possible roots
            for r = i to j
                t = e[i][r-1] + e[r+1][j] + w[i][j]
                if t < e[i][j]
                    e[i][j] = t
                    root[i][j] = r

    return e and root
```

### Time and Space Complexity

- **Time Complexity**: O(n³) for the basic dynamic programming solution
- **Time Complexity with Knuth's Optimization**: O(n²)
- **Space Complexity**: O(n²) for storing the e and root tables

## Examples

### Example 1: Complete DP Table Computation

Given n = 3 keys with probabilities:

- p₁ = 0.15, p₂ = 0.10, p₃ = 0.05
- q₀ = 0.05, q₁ = 0.10, q₂ = 0.05, q₃ = 0.05

**Step 1: Initialize base cases (length = 0)**

| i\j | j=0          | j=1          | j=2          | j=3          |
| --- | ------------ | ------------ | ------------ | ------------ |
| i=1 | e[1][0]=0.05 |              |              |              |
| i=2 |              | e[2][1]=0.10 |              |              |
| i=3 |              |              | e[3][2]=0.05 |              |
| i=4 |              |              |              | e[4][3]=0.05 |

**Step 2: Compute for length = 1 (single key subtrees)**

For i=1, j=1: w[1][1] = q₀ + p₁ + q₁ = 0.05 + 0.15 + 0.10 = 0.30

- r=1: t = e[1][0] + e[2][1] + w[1][1] = 0.05 + 0.10 + 0.30 = 0.45
- e[1][1] = 0.45, root[1][1] = 1

For i=2, j=2: w[2][2] = q₁ + p₂ + q₂ = 0.10 + 0.10 + 0.05 = 0.25

- r=2: t = e[2][1] + e[3][2] + w[2][2] = 0.10 + 0.05 + 0.25 = 0.40
- e[2][2] = 0.40, root[2][2] = 2

For i=3, j=3: w[3][3] = q₂ + p₃ + q₃ = 0.05 + 0.05 + 0.05 = 0.15

- r=3: t = e[3][2] + e[4][3] + w[3][3] = 0.05 + 0.05 + 0.15 = 0.25
- e[3][3] = 0.25, root[3][3] = 3

**Step 3: Compute for length = 2 (two-key subtrees)**

For i=1, j=2: w[1][2] = w[1][1] + p₂ + q₂ = 0.30 + 0.10 + 0.05 = 0.45

- r=1: t = e[1][0] + e[2][2] + 0.45 = 0.05 + 0.40 + 0.45 = 0.90
- r=2: t = e[1][1] + e[3][2] + 0.45 = 0.45 + 0.05 + 0.45 = 0.95
- e[1][2] = 0.90, root[1][2] = 1

For i=2, j=3: w[2][3] = w[2][2] + p₃ + q₃ = 0.25 + 0.05 + 0.05 = 0.35

- r=2: t = e[2][1] + e[3][3] + 0.35 = 0.10 + 0.25 + 0.35 = 0.70
- r=3: t = e[2][2] + e[4][3] + 0.35 = 0.40 + 0.05 + 0.35 = 0.80
- e[2][3] = 0.70, root[2][3] = 2

**Step 4: Compute for length = 3 (all three keys)**

For i=1, j=3: w[1][3] = w[1][2] + p₃ + q₃ = 0.45 + 0.05 + 0.05 = 0.55

- r=1: t = e[1][0] + e[2][3] + 0.55 = 0.05 + 0.70 + 0.55 = 1.30
- r=2: t = e[1][1] + e[3][3] + 0.55 = 0.45 + 0.25 + 0.55 = 1.25
- r=3: t = e[1][2] + e[4][3] + 0.55 = 0.90 + 0.05 + 0.55 = 1.50

**Result**: e[1][3] = 1.25 with root = 2 (key k₂ as root)

**Tree Structure**: Root is k₂. Left subtree contains k₁, right subtree contains k₃.

### Example 2: Cost Verification

For the tree from Example 1:

- Depth(k₁) = 1, Depth(k₂) = 0, Depth(k₃) = 1
- Depth(d₀) = 2, Depth(d₁) = 2, Depth(d₂) = 2, Depth(d₃) = 2

Cost = p₁(1+1) + p₂(0+1) + p₃(1+1) + q₀(2+1) + q₁(2+1) + q₂(2+1) + q₃(2+1)
= 0.15(2) + 0.10(1) + 0.05(2) + 0.05(3) + 0.10(3) + 0.05(3) + 0.05(3)
= 0.30 + 0.10 + 0.10 + 0.15 + 0.30 + 0.15 + 0.15
= 1.25

This matches e[1][3], verifying correctness.

## Exam Tips

1. **Understand the difference between internal and external nodes**: Internal nodes store actual keys (kᵢ) with probabilities pᵢ, while external nodes (leaves) store dummy keys (dᵢ) with probabilities qᵢ representing unsuccessful searches.

2. **Remember the recurrence relation**: The key formula is e[i][j] = w[i][j] + min(e[i][r-1] + e[r+1][j]) for r in [i, j], where w[i][j] accumulates the probability sums.

3. **Know the base cases**: e[i][i-1] = qᵢ₋₁ for empty subtrees, representing the cost of accessing only the dummy key at that boundary.

4. **Apply Knuth's Optimization**: In exams, when n is large, applying the monotonicity property root[i][j-1] ≤ root[i][j] ≤ root[i+1][j] can simplify finding the optimal root.

5. **Practice table construction**: The DP table is filled diagonally - first all subtrees of length 1, then length 2, and so on. Understand how to trace through the algorithm.

6. **Verify your answer**: After constructing the tree, calculate the expected cost manually using the depth formula to verify it matches the DP result.

7. **Time complexity matters**: Remember that basic OBST is O(n³), but with Knuth's optimization it becomes O(n²). This distinction is often tested.
