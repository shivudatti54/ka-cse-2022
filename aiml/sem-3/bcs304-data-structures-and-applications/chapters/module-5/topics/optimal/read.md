# Optimal Binary Search Trees (OBST)

## Introduction

In the context of data structures, "optimal" often refers to achieving the highest efficiency for a specific operation. While a standard Binary Search Tree (BST) provides `O(log n)` time complexity for search, insertion, and deletion in the average case, this performance degrades to `O(n)` in the worst case (e.g., when data is inserted in sorted order). An **Optimal Binary Search Tree (OBST)** is designed to minimize the total search cost for a given set of keys and their known access frequencies (or probabilities), ensuring the best possible average search time.

## Core Concepts

### 1. The Problem Statement

Given:
*   A sorted sequence of `n` distinct keys: `K = <k1, k2, k3, ..., kn>`
*   A corresponding set of access probabilities: `P = <p1, p2, p3, ..., pn>`, where `pi` is the probability of searching for key `ki`.
*   (Optional) Probabilities for unsuccessful searches (i.e., for values between the keys): `Q = <q0, q1, q2, ..., qn>`, where `qi` is the probability of searching for a value between `ki` and `k(i+1)`.

**Goal:** Construct the BST that minimizes the total **expected cost** of search operations.

### 2. Expected Search Cost

The cost of a search is the number of nodes compared, which is equal to `(depth of the node + 1)`. The expected cost of a successful search for key `ki` is therefore `pi * (depth(ki) + 1)`.

The total expected cost `C` of the tree is the sum of the costs for all possible searches (both successful and unsuccessful):
`C = Σ [pi * (depth(ki) + 1)]   for i=1 to n   +   Σ [qj * (depth(dummy_j))]   for j=0 to n`

An OBST is the structure that minimizes this value `C`.

### 3. Dynamic Programming Solution

Constructing an OBST is a classic problem solved using **Dynamic Programming**. The solution involves building a cost table from the bottom up.

*   Let `e[i, j]` be the expected cost of searching an **optimal BST** built from the contiguous subset of keys `ki, k(i+1), ..., kj`.
*   Let `w[i, j]` be the sum of probabilities for the subtree `i` to `j`. This is the total probability mass of the tree and is calculated as:
    `w[i, j] = pi + p(i+1) + ... + pj + q(i-1) + qi + ... + qj`
    The `w` table helps simplify the recurrence relation.

**Recurrence Relation:**
For a subtree containing keys `i` through `j`, we try every key `r` (where `i <= r <= j`) as the root. The cost of this subtree with `r` as the root is:
`cost = e[i, r-1] + e[r+1, j] + w[i, j]`

This formula breaks down as:
1.  `e[i, r-1]`: The cost of the left subtree.
2.  `e[r+1, j]`: The cost of the right subtree.
3.  `w[i, j]`: Adding the root adds one comparison for every node in this entire subtree, which is accounted for by adding the total weight `w[i, j]`.

We choose the root `r` that minimizes this cost:
`e[i, j] = min { e[i, r-1] + e[r+1, j] + w[i, j] } for r between i and j`

**Base Case:**
The smallest possible subtree is an empty tree (`j = i-1`). The cost of an empty tree is just the probability of an unsuccessful search in that range:
`e[i, i-1] = q(i-1)`

### 4. Example Walkthrough

Let's define a simple instance with `n=2` keys.
*   Keys: `[10, 20]`
*   `P = [0.3, 0.6]`
*   `Q = [0.1, 0.2, 0.1]` (`q0`: <10, `q1`: between 10 & 20, `q2`: >20)

We compute `w` and `e` for all subtrees.

**Step 1: Compute `w[i, j]`**
*   `w[1,1] = p1 + q0 + q1 = 0.3 + 0.1 + 0.2 = 0.6`
*   `w[2,2] = p2 + q1 + q2 = 0.6 + 0.2 + 0.1 = 0.9`
*   `w[1,2] = p1 + p2 + q0 + q1 + q2 = 0.3 + 0.6 + 0.1 + 0.2 + 0.1 = 1.3`

**Step 2: Compute `e[i, j]`**
*   `e[1,0] = q0 = 0.1` (empty left subtree of `k1`)
*   `e[2,1] = q1 = 0.2` (empty left subtree of `k2`)
*   `e[3,2] = q2 = 0.1` (empty right subtree of `k2`)
*   `e[1,1]` (Subtree with only key 10): Min over `r=1`
    `= e[1,0] + e[2,1] + w[1,1] = 0.1 + 0.2 + 0.6 = 0.9`
*   `e[2,2]` (Subtree with only key 20): Min over `r=2`
    `= e[2,1] + e[3,2] + w[2,2] = 0.2 + 0.1 + 0.9 = 1.2`
*   `e[1,2]` (Subtree with keys 10 and 20): Try `r=1` and `r=2`
    *   Root `r=1`: `cost = e[1,0] + e[2,2] + w[1,2] = 0.1 + 1.2 + 1.3 = 2.6`
    *   Root `r=2`: `cost = e[1,1] + e[3,2] + w[1,2] = 0.9 + 0.1 + 1.3 = 2.3`
    *   `e[1,2] = min(2.6, 2.3) = 2.3`. The optimal root is `k2` (20).

The optimal tree has 20 at the root and 10 as its left child. Its expected search cost is 2.3, which is lower than the alternative (2.6).

## Key Points & Summary

*   **Purpose:** An OBST minimizes the average search time when the access frequencies of keys are known in advance.
*   **Prerequisites:** The algorithm requires a sorted list of keys and their access probabilities (for both successful and unsuccessful searches).
*   **Algorithm:** The solution uses a **Dynamic Programming** approach with a time complexity of **O(n³)** and a space complexity of **O(n²)**. While this is expensive, it is acceptable for static dictionaries (like a language keyword list) built once and searched frequently.
*   **Comparison with AVL/Red-Black Trees:** Self-balancing trees (AVL, Red-Black) guarantee `O(log n)` worst-case search time without prior knowledge of access patterns. OBST provides a better *average* search time if the access patterns are known and static.
*   **Application:** OBSTs are ideal for implementing static symbol tables, such as a dictionary of reserved words in a programming language compiler, where the keys are fixed and access frequencies can be profiled.