# Branch and Bound: An Algorithmic Strategy for NP-Hard Problems

## Table of Contents

- [Branch and Bound: An Algorithmic Strategy for NP-Hard Problems](#branch-and-bound-an-algorithmic-strategy-for-np-hard-problems)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Fundamental Principles](#1-fundamental-principles)
  - [2. Decision Tree Perspective](#2-decision-tree-perspective)
  - [3. Search Strategies](#3-search-strategies)
  - [4. Bounding Functions](#4-bounding-functions)
  - [5. Complexity Analysis](#5-complexity-analysis)
- [Examples](#examples)
  - [Example 1: 0/1 Knapsack via Branch and Bound](#example-1-01-knapsack-via-branch-and-bound)
  - [Example 2: Comparison with Exhaustive Search](#example-2-comparison-with-exhaustive-search)
  - [Example 3: TSP Branch and Bound](#example-3-tsp-branch-and-bound)
- [Exam Tips](#exam-tips)

## Introduction

In the study of algorithmic power limitations, we encounter problems for which no polynomial-time algorithms are known. The classes P, NP, and NP-Complete provide a framework for understanding these limitations. Within this context, **Branch and Bound** emerges as a fundamental algorithmic paradigm for tackling NP-hard optimization problems that are otherwise intractable through exhaustive enumeration.

The theoretical foundation of NP-completeness, established by Cook (1971) and Karp (1972), demonstrates that thousands of practical optimization problems—including the Traveling Salesperson Problem (TSP), 0/1 Knapsack, and Integer Programming—belong to the class NP-hard. These problems share a critical characteristic: no known polynomial-time algorithm exists to solve them exactly. Branch and Bound addresses this computational limitation by intelligently exploring the solution space through systematic enumeration augmented with bounding operations, thereby avoiding examination of infeasible or suboptimal solutions.

This technique represents a strategic compromise between brute-force exhaustive search and purely heuristic approaches. While it does not circumvent the theoretical intractability of NP-hard problems (the worst-case complexity remains exponential), Branch and Bound provides a practical framework that often solves real-world instances of moderate size within reasonable time bounds. The method's effectiveness hinges critically on the design of efficient bounding functions and search strategies.

## Key Concepts

### 1. Fundamental Principles

**Branch and Bound (B&B)** is an exact optimization algorithm that systematically enumerates candidate solutions by means of state space search. The algorithm employs two primary operations:

- **Branching**: Dividing a problem into smaller subproblems. Each subproblem represents a subset of the solution space, forming what is conceptually a decision tree where each node corresponds to a partial solution.

- **Bounding**: Computing bounds on the optimal solution value within each subproblem. The lower bound (LB) represents the best possible solution achievable in that subspace, while the upper bound (UB) represents the worst-case solution value.

- **Pruning**: Eliminating subproblems whose bounds indicate they cannot contain an optimal solution. If LB ≥ UB (current best known solution), the subproblem is discarded.

### 2. Decision Tree Perspective

From the decision tree viewpoint, Branch and Bound addresses the exponential blowup inherent in exhaustive enumeration. A complete decision tree for an n-variable 0/1 problem contains 2ⁿ leaves. B&B reduces this tree through pruning based on computed bounds. The effectiveness of the algorithm directly correlates with the quality of bounding functions—tighter bounds enable more aggressive pruning, dramatically reducing the explored portion of the tree.

**Theorem (Pruning Correctness)**: If for a subproblem P, the lower bound LB(P) ≥ Z\* (the best solution found so far), then no optimal solution exists within P.

_Proof_: By definition, LB(P) ≤ optimal solution value within P. If LB(P) ≥ Z*, then any solution within P has value ≤ LB(P) ≤ Z*, contradicting optimality unless the optimal equals Z\*. Therefore, P cannot contain a strictly better solution and may be safely pruned. ∎

### 3. Search Strategies

The order in which subproblems are explored significantly impacts practical performance:

- **Breadth-First Search (FIFO)**: Explores nodes level by level. Guarantees finding optimal solution but may explore many nodes before reaching promising regions.

- **Depth-First Search (LIFO)**: Explores as far as possible along each branch before backtracking. Memory-efficient but may explore suboptimal regions extensively before finding good solutions.

- **Best-First Search**: Always explores the node with the best lower bound. Generally most efficient but requires priority queue maintenance.

- **Least-Cost Search**: Variant prioritizing nodes with best potential for improvement.

### 4. Bounding Functions

The efficacy of Branch and Bound depends critically on bounding function design:

**For 0/1 Knapsack**:

- Upper bound via fractional relaxation: UB = Σ(pᵢxᵢ) + (capacity - Σ(wᵢxᵢ)) × (pⱼ/wⱼ) where item j has best value-to-weight ratio among unpicked items.
- This bound is _admissible_ (never underestimates the true optimum), ensuring optimality.

**For Traveling Salesperson Problem**:

- Lower bound via minimum spanning tree (MST) or Held-Karp bound.
- Reduced cost matrix computation provides effective pruning.

### 5. Complexity Analysis

The worst-case time complexity of Branch and Bound remains exponential O(b^d) where b is branching factor and d is depth to optimal solution. However:

- **Best Case**: O(n^c) for problems where bounds effectively prune early, though such bounds are problem-specific.
- **Space Complexity**: O(d) for depth-first, O(b^d) for breadth-first or best-first strategies.
- The algorithm's practical success stems from the fact that "average" instances often admit substantial pruning.

## Examples

### Example 1: 0/1 Knapsack via Branch and Bound

Consider n=4 items with weights [2, 3, 4, 5] and profits [10, 12, 18, 25], capacity W=8.

**Step 1**: Compute profit-to-weight ratios: [5, 4, 4.5, 5]. Sort by ratio: items 1, 4, 3, 2.

**Step 2**: Initial solution via greedy: take items 1, 4 (weight 7, profit 35). Z\* = 35.

**Step 3**: Branch on first item (include/exclude). For the "exclude" branch:

- Remaining capacity: 8, remaining items: 4, 3, 2
- Fractional solution: take 4 (weight 5, profit 25), remaining capacity 3, take 2 (weight 3, profit 12), remaining capacity 0
- UB = 25 + 12 + 0×4.5 = 37

Since UB (37) > Z\* (35), this node requires exploration.

**Step 4**: Continue branching with tighter bounds, pruning branches where UB ≤ 35.

The algorithm ultimately finds optimal solution: items 1 and 4 (profit 35) which matches the initial bound, confirming optimality.

### Example 2: Comparison with Exhaustive Search

For a 20-variable 0/1 problem:

- Exhaustive search explores 2²⁰ = 1,048,576 nodes
- With effective bounding (90% prune rate): approximately 100,000 nodes
- This represents a 10× improvement in practice, though theoretical complexity remains exponential

### Example 3: TSP Branch and Bound

For a 5-city TSP with distance matrix, B&B:

1. Computes initial upper bound via nearest neighbor heuristic
2. Uses reduced cost matrix for lower bounds
3. Prunes paths exceeding current best tour length
4. Explores promising paths first (best-first strategy)

## Exam Tips

1. **Connection to NP-Completeness**: Understand that Branch and Bound addresses NP-hard problems but does NOT solve the P vs NP problem—it provides practical exact solutions within exponential worst-case bounds.

2. **Pruning Condition Mastery**: Remember: prune if Lower Bound ≥ Current Best Solution (for maximization) or Lower Bound ≤ Current Best (for minimization).

3. **Bounding Function Quality**: Recognize that tighter bounds yield more pruning. The fractional relaxation bound for knapsack is optimal because it provides the closest admissible estimate to the integer optimum.

4. **Search Strategy Selection**: For memory-constrained environments, use depth-first (LIFO). For fastest convergence to optimal solution, prefer best-first search.

5. **Proof of Correctness**: Be prepared to explain or apply the pruning correctness theorem—understanding why LB ≥ Z\* guarantees no better solution exists in that subspace.

6. **Complexity Awareness**: The worst-case remains exponential. Branch and Bound is a heuristic improvement over brute force, not a polynomial-time guarantee.

7. **Decision Tree Reduction**: Articulate how B&B reduces decision tree size through pruning—quantify this reduction using bound quality metrics.
