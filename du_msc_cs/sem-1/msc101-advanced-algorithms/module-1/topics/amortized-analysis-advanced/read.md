# Amortized Analysis Advanced

## A Comprehensive Study Material for MSc CS Students

---

## Table of Contents

1. [Introduction and Real-World Relevance](#1-introduction-and-real-world-relevance)
2. [Fundamentals of Amortized Analysis](#2-fundamentals-of-amortized-analysis)
3. [The Three Principal Methods](#3-the-three-principal-methods)
4. [Formal Mathematical Framework](#4-formal-mathematical-framework)
5. [Advanced Algorithms and Data Structures](#5-advanced-algorithms-and-data-structures)
6. [Dynamic Tables: A Comprehensive Case Study](#6-dynamic-tables-a-comprehensive-case-study)
7. [Fibonacci Heaps: Amortized Excellence](#7-fibonacci-heaps-amortized-excellence)
8. [Splay Trees: Self-Adjusting with Amortized Bounds](#8-splay-trees-self-adjusting-with-amortized-bounds)
9. [Comparative Analysis of Methods](#9-comparative-analysis-of-methods)
10. [Challenging Multiple Choice Questions](#10-challenging-multiple-choice-questions)
11. [Key Takeaways](#11-key-takeaways)
12. [References and Further Reading](#12-references-and-further-reading)

---

## 1. Introduction and Real-World Relevance

### What is Amortized Analysis?

Amortized analysis is a sophisticated technique in algorithm design that provides a worst-case guarantee on the **average cost** of a sequence of operations, rather than analyzing each operation in isolation. Unlike average-case analysis, which requires knowledge of input distribution, amortized analysis guarantees performance **deterministically** across any sequence of operations.

### Why This Matters in Real-World Systems

Consider these practical scenarios:

| Application | Operation | Individual Worst-Case | Amortized Cost | Impact |
|-------------|-----------|----------------------|----------------|--------|
| Dynamic Arrays | Insert | O(n) | O(1) | Language implementations (Python lists, Java ArrayList) |
| Database Indexing | B-Tree insert | O(log n) with splits | O(log n) | Database query performance guarantees |
| Memory Management | Garbage collection | Pause could be large | Bounded | Real-time systems, game engines |
| Network Routing | Dijkstra with Fibonacci heaps | O(V²) naive | O(E + V log V) | GPS navigation, network protocols |

For the Delhi University MSc CS syllabus (July 2025), this topic appears in the Advanced Algorithms paper, emphasizing the bridge between theoretical analysis and practical system design.

---

## 2. Fundamentals of Amortized Analysis

### 2.1 Key Distinctions

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ANALYSIS TYPE COMPARISON                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  WORST-CASE:   max{T(i)} for any input of size n                   │
│                → Guarantees upper bound                            │
│                → Often pessimistic for practical sequences        │
│                                                                     │
│  AVERAGE-CASE: E[T(i)] assuming probability distribution           │
│                → Requires knowledge of input distribution          │
│                → May not reflect real usage patterns               │
│                                                                     │
│  AMORTIZED:    T(1) + T(2) + ... + T(n) ≤ n · a(n)                │
│                → Guarantees average per operation                  │
│                → Works for any sequence of operations              │
│                → Deterministic, no probability needed             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2 The Three Crucial Methods

#### Method 1: Aggregate Analysis

The simplest approach—prove that for **any** sequence of n operations, the total work is O(n) or similar. The amortized cost is this total divided by n.

**Theorem**: If n operations take T(n) total time in the worst case, the amortized cost per operation is T(n)/n.

#### Method 2: Accounting Method (Bank Account Analogy)

Assign varying "charges" to different operations:
- **Overcharge**: Some cheap operations are charged more than their actual cost
- **Save surplus**: The surplus is stored as "credits"
- **Undercharge**: Expensive operations use stored credits

**Invariant**: Credit balance never goes negative.

#### Method 3: Potential Method (Energy Function)

Define a **potential function** Φ that maps each data structure state to a non-negative value:
- **Amortized cost** of operation = actual cost + ΔΦ (change in potential)
- If Φ(start) is bounded and Φ never goes negative, total amortized cost ≤ initial potential + sum of actual costs

---

## 3. Formal Mathematical Framework

### 3.1 Rigorous Definitions

**Definition 1 (Amortized Time)**: An operation O_i has amortized cost Â_i if for any sequence of n operations O_1, O_2, ..., O_n:

$$\sum_{i=1}^{n} \hat{O}_i \geq \sum_{i=1}^{n} O_i$$

and we say the sequence runs in O(n) amortized time.

**Definition 2 (Potential Function)**: For a data structure D with state s_i after i operations, a potential function Φ: States → ℝ satisfies:
- Φ(s_i) ≥ 0 for all i
- Φ(s_0) (initial state) is bounded by a constant

The amortized cost of operation that transforms s_{i-1} to s_i is:

$$\hat{c}_i = c_i + \Phi(s_i) - \Phi(s_{i-1})$$

**Theorem (Potential Method Bound)**: For any sequence of n operations:

$$\sum_{i=1}^{n} c_i = \sum_{i=1}^{n} \hat{c}_i + \Phi(s_0) - \Phi(s_n) \leq \sum_{i=1}^{n} \hat{c}_i + \Phi(s_0)$$

### 3.2 Proof Framework

To prove amortized bounds using the potential method:

1. **Define Φ** carefully—often based on some measure of "disorder" or "work remaining"
2. **Verify** Φ ≥ 0 always
3. **Compute** amortized cost for each operation type using the formula
4. **Sum** to get total bound

---

## 4. Advanced Algorithms and Data Structures

### 4.1 Why These Data Structures Matter

The following three data structures are **canonical examples** where amortized analysis is essential:

1. **Dynamic Tables**: Demonstrate all three methods elegantly
2. **Fibonacci Heaps**: Achieve optimal amortized bounds for priority queue operations
3. **Splay Trees**: Achieve amortized O(log n) without explicit balancing

---

## 5. Dynamic Tables: A Comprehensive Case Study

### 5.1 Problem Statement

A dynamic table (like a vector/array list) must expand when it becomes full. The naive approach: allocate new array of size 2n, copy all n elements. This is O(n) for one insert!

### 5.2 The Table-Insert Operation

```c
// Dynamic Table Insertion Pseudocode
typedef struct {
    int *array;      // The data storage
    int size;        // Current number of elements
    int capacity;   // Total allocated slots
} DynamicTable;

// Insert operation
void tableInsert(DynamicTable *T, int key) {
    if (T->size == T->capacity) {
        // Table is full - expand
        int newCapacity = (T->capacity == 0) ? 1 : 2 * T->capacity;
        int *newArray = malloc(newCapacity * sizeof(int));
        
        // Copy existing elements - O(size) operation!
        for (int i = 0; i < T->size; i++) {
            newArray[i] = T->array[i];
        }
        
        free(T->array);
        T->array = newArray;
        T->capacity = newCapacity;
    }
    
    T->array[T->size++] = key;
}
```

### 5.3 Aggregate Analysis

**Theorem**: Starting from an empty table, any sequence of n insertions causes at most O(n) element moves.

**Proof by Induction on i (number of insertions)**:

Let m(i) = total number of elements moved after i insertions.

- When i = 1: We allocate initial capacity 1, move 0 elements (initial insertion). m(1) = 0
- Assume m(i) ≤ 2i - 2 for i ≥ 1
- For insertion i+1:
  - If table not full: move 0, m(i+1) = m(i) ≤ 2i - 2 < 2(i+1) - 2 ✓
  - If table full at size i: We double capacity, move i elements
    - m(i+1) = m(i) + i ≤ (2i - 2) + i = 3i - 2 < 2(i+1) - 2 for i ≥ 2 ✓
    - For i = 1: m(2) = 0 + 1 = 1 < 2(2) - 2 = 2 ✓

By induction, total moves ≤ 2n - 2, so **amortized cost per insert is O(1)**.

### 5.4 Accounting Method Analysis

Assign amortized costs:

| Operation | Actual Cost | Amortized Cost | Credit Balance Change |
|-----------|-------------|----------------|----------------------|
| Insert (table not full) | 1 | 2 | +1 credit saved |
| Insert (table full) | k+1 (k elements copied + 1) | 2 | - (k-1) credits used |

**Invariant**: Always maintain at least 0 credits.

**Verification**: Each non-expanding insert "saves" 1 credit. When expanding, we have credits from previous inserts equal to the current table size, paying for the copies.

### 5.5 Potential Method Analysis

Define potential function:

$$\Phi(T) = 2 \cdot \text{size} - \text{capacity}$$

**Properties**:
- Initially: size = 0, capacity = 0 or 1 → Φ = -1 or 0 ≥ -1 (let's handle carefully)
- After expansion: size = capacity/2 → Φ = 2(capacity/2) - capacity = 0
- Before expansion: size = capacity → Φ = 2·capacity - capacity = capacity ≥ 0

**Amortized Cost Computation**:

*Case 1: Table not full (no expansion)*
- Actual cost: c_i = 1
- ΔΦ = 2·size_new - capacity_new - (2·size_old - capacity_old)
       = 2(size+1) - capacity - (2·size - capacity)
       = 2
- Â = 1 + 2 = 3

*Case 2: Table full (expansion)*
- Actual cost: c_i = size + 1 (copying all elements + 1)
- After expansion: size_new = size + 1, capacity_new = 2·capacity
- ΔΦ = 2(size+1) - 2·capacity - (2·size - capacity)
     = 2size + 2 - 2capacity - 2size + capacity
     = 2 - capacity
- Since expansion happens when size = capacity:
  - ΔΦ = 2 - capacity
- Â = (size + 1) + (2 - capacity) = size + 3 - capacity

When size = capacity, Â = 3 (since capacity = size).

**Result**: Amortized cost is O(1) per insertion!

---

## 6. Fibonacci Heaps: Amortized Excellence

### 6.1 Background and Motivation

Fibonacci heaps, invented by Fredman and Tarjan (1987), achieve better amortized running times for priority queue operations than previously known data structures.

| Operation | Binary Heap | Fibonacci Heap (Amortized) |
|-----------|-------------|---------------------------|
| Insert | O(log n) | O(1) |
| Find-min | O(1) | O(1) |
| Extract-min | O(log n) | O(log n) |
| Decrease-key | O(log n) | O(1) |
| Union | O(log n) | O(1) |

This is **asymptotically optimal** for all these operations!

### 6.2 Structure Overview

```python
# Fibonacci Heap Node Structure
class FibonacciNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0          # Number of children
        self.marked = False      # For decrease-key
        self.parent = None
        self.child = None        # Any one child (circular list)
        self.next = None         # Sibling (circular doubly-linked)
        self.prev = None
```

**Key innovations**:
1. **Lazy consolidation**: Don't do work until necessary
2. **Degree bound**: Ensures O(log n) for extract-min
3. **Cascading cuts**: Maintains heap properties efficiently

### 6.3 Amortized Analysis of Fibonacci Heaps

Let n be the number of items in the heap, and let t(H) = number of trees in root list.

**Potential Function**:
$$\Phi(H) = t(H) + 2 \cdot m(H)$$

where m(H) = number of marked nodes.

### 6.4 Operation Costs (Amortized)

#### Insert: O(1) amortized

- Actual cost: O(1) - create node, add to root list
- ΔΦ: t increases by 1 → ΔΦ = 1
- Â = 1 + 1 = 2 = O(1)

#### Find-Min: O(1) amortized

- Actual cost: O(1) - just return pointer
- No structure change → ΔΦ = 0
- Â = O(1)

#### Extract-Min: O(log n) amortized

This is the complex operation:

1. Remove min root, add its children to root list (actual: O(degree))
2. Consolidate trees of equal degree using a degree table (actual: O(n) worst, but amortized better)

**Degree Bound Lemma**: After consolidation, any node of degree k has at least F_k+2 nodes in its subtree, where F_k is the k-th Fibonacci number.

This implies the maximum degree is O(log n).

**Amortized cost analysis**:

Let D = max degree = O(log n)

- Actual cost: O(D + t(H)) for consolidation
- Number of trees reduces significantly
- Â = O(D) = O(log n)

#### Decrease-Key: O(1) amortized

When we decrease a key and violate heap property:

```
decreaseKey(x, newVal):
    if newVal < x.parent.key:
        cut(x)           # Cut x from parent
        addToRootList(x)
        if x.parent.marked:
            cascadingCut(x.parent)
        else:
            x.parent.marked = True
```

- **Cut**: Actual O(1), increases t(H) by 1 → +1 potential
- **Cascading cut**: Each cut (except possibly first) adds 1 to t but decreases m by 1 (unmarking)
- Total: O(1) amortized

---

## 7. Splay Trees: Self-Adjusting with Amortized Bounds

### 7.1 The Splay Operation

Splay trees achieve O(log n) amortized access time through repeated splaying—moving accessed nodes to the root via rotations.

```python
# Simplified splay operation (zig-zig case)
def splay(tree, node):
    while node.parent is not None:
        if node.parent.parent is None:
            # Zig case - single rotation
            rotate(node)
        elif (node == node.parent.left and 
              node.parent == node.parent.parent.left):
            # Zig-zig case
            rotate(node.parent)
            rotate(node)
        elif (node == node.parent.right and 
              node.parent == node.parent.parent.right):
            # Zig-zig case
            rotate(node.parent)
            rotate(node)
        else:
            # Zig-zag case
            rotate(node)
            rotate(node)
```

### 7.2 Potential Function for Splay Trees

The key insight is the **weighted potential function**:

$$\Phi(T) = \sum_{x \in T} \text{rank}(x)$$

where rank(x) = ⌊log₂(size(x))⌋, the number of bits needed to represent the subtree size.

**Properties**:
- rank(x) ≥ 0 for all nodes
- rank is subadditive: rank(x) + rank(y) ≥ rank(parent)

### 7.3 Amortized Cost of Splaying

**Theorem (Splay Theorem)**: The amortized cost of splaying a node x to the root is O(log n + log(1/s_x)), where s_x is the weight of x.

For the standard version with equal weights, this gives O(log n) amortized per operation.

**Key lemma (Access Lemma)**:
For any sequence of m accesses, total time for splaying is O(m log n + n log n).

### 7.4 Why Splay Trees Matter

1. **No explicit balance information**: No height field needed
2. **Locality**: Frequently accessed items move closer to root (working set property)
3. **Competitive**: O(log n) amortized, competitive with static optimal BSTs

---

## 8. Comparative Analysis of Methods

### 8.1 When to Use Each Method

| Method | Best For | Advantages | Disadvantages |
|--------|----------|------------|---------------|
| Aggregate | Simple bounds, when total cost is obvious | Easiest to apply | Can't assign different costs to different operations |
| Accounting | Intuitive scenarios, "saving for later" | Very intuitive, credit balance visualization | Need careful credit management |
| Potential | Complex data structures, tight bounds | Most flexible, powerful | Requires clever potential function design |

### 8.2 Decision Tree for Analysis Approach

```
START: Analyze sequence of operations
│
├─► Can we easily compute total cost?
│   YES → Use Aggregate Analysis
│   NO  → Continue
│
├─► Can we assign "charges" with credit tracking?
│   YES → Use Accounting Method
│   NO  → Continue  
│
└─► Need flexible bounds or complex structure?
    YES → Use Potential Method
```

---

## 9. Challenging Multiple Choice Questions

### Level 1: Conceptual Basics

**Q1**. In amortized analysis, the guarantee applies to:
- (a) Average input distribution
- (b) Any sequence of operations
- (c) Randomly selected operations
- (d) Worst-case single operation

**Answer**: (b) — Amortized analysis guarantees bounds on any sequence.

### Level 2: Method Application

**Q2**. Consider a binary counter that starts at 0 and is incremented n times. Using aggregate analysis, what is the amortized cost per increment?
- (a) O(1)
- (b) O(log n)
- (c) O(n)
- (d) O(n log n)

**Answer**: (a) — Total bit flips = n + n/2 + n/4 + ... < 2n, so O(1) amortized.

### Level 3: Potential Functions

**Q3**. For dynamic tables with the potential function Φ = 2·size - capacity, when does Φ = 0?
- (a) Always
- (b) When table is half full
- (c) When table is completely full
- (d) After every expansion

**Answer**: (b) — At expansion time, size = capacity/2, so Φ = 2(capacity/2) - capacity = 0.

### Level 4: Advanced Reasoning

**Q4**. Fibonacci heaps achieve O(1) amortized insert but O(log n) worst-case extract-min. This is an example of:
- (a) Worst-case analysis failure
- (b) Amortization trading time between operations
- (c) Incorrect implementation
- (d) Probability-based optimization

**Answer**: (b) — Amortization allows cheap operations to "subsidize" expensive ones.

### Level 5: Proof-Based

**Q5**. In Fibonacci heap decrease-key, the potential function includes 2·m(H) where m(H) is marked nodes. What is the purpose of the factor 2?
- (a) Historical accident
- (b) To balance tree count changes
- (C) To ensure potential is always positive
- (d) To account for cascading cuts (2 credits per marked node)

**Answer**: (d) — Each marked node can cause at most one cascading cut, requiring 2 potential units to pay for cut + potential change.

### Level 6: Algorithm Design

**Q6**. Which data structure achieves the best (asymptotically optimal) amortized time for ALL five priority queue operations (insert, find-min, extract-min, decrease-key, union)?
- (a) Binary Heap
- (b) Binomial Heap
- (c) Fibonacci Heap
- (d) Pairing Heap

**Answer**: (c) — Fibonacci heaps achieve O(1) for insert, find-min, decrease-key, union, and O(log n) for extract-min.

### Level 7: Mathematical Rigor

**Q7**. Let Φ be a valid potential function with Φ(s₀) = 0 and Φ(s) ≥ 0 for all states. For a sequence of operations with actual costs c₁, c₂, ..., cₙ and amortized costs ĉ₁, ĉ₂, ..., ĉₙ, which inequality always holds?

- (a) Σcᵢ ≤ Σĉᵢ
- (b) Σcᵢ ≥ Σĉᵢ
- (c) Σcᵢ = Σĉᵢ
- (d) Σcᵢ < Σĉᵢ always

**Answer**: (a) — By definition, amortized costs overcount to provide guarantees: Σcᵢ = Σ(ĉᵢ + Φ(sᵢ₋₁) - Φ(sᵢ)) = Σĉᵢ + Φ(s₀) - Φ(sₙ) ≤ Σĉᵢ.

### Level 8: Complex Analysis

**Q8**. A queue with two stacks supports enqueue and dequeue. The amortized cost per operation using the accounting method with appropriate charges is:
- (a) O(1) for enqueue, O(n) for dequeue
- (b) O(n) for enqueue, O(1) for dequeue  
- (c) O(1) for both
- (d) O(log n) for both

**Answer**: (c) — Classic example: Amortized O(1) using 2 credits per enqueue, 0 for dequeue when transferring.

### Level 9: Synthesis

**Q9**. Which statement about splay trees is FALSE?
- (a) They achieve O(log n) amortized access
- (b) They are guaranteed O(log n) worst-case per operation
- (c) They have a working-set property
- (d) They require no extra balance information

**Answer**: (b) — Splay trees have O(log n) amortized but not worst-case guarantees; individual operations can be Θ(n).

### Level 10: Research-Level

**Q10**. The "potential method" in amortized analysis is most closely related to which branch of mathematics/physics?
- (a) Linear algebra
- (b) Thermodynamics (energy functions)
- (C) Number theory
- (d) Graph theory

**Answer**: (b) — The potential function is analogous to energy in physics, storing "energy" (credits) for later use, similar to how thermodynamic potentials work.

---

## 10. Key Takeaways

### Core Concepts

1. **Amortized ≠ Average-case**: Amortized analysis provides deterministic guarantees on sequences, unlike probabilistic average-case analysis.

2. **Three Methods, One Goal**: Aggregate, Accounting, and Potential methods all prove the same bounds—they offer different perspectives and flexibility.

3. **Potential Function Design**: The key to complex amortized analysis is finding a potential function that captures "work remaining" in the data structure.

### Algorithmic Insights

4. **Dynamic Tables**: Allocating in geometric progression (doubling) ensures O(1) amortized insert despite O(n) copies during expansion.

5. **Fibonacci Heaps**: Through lazy consolidation and cascading cuts, achieve optimal amortized priority queue bounds—O(1) insert/decrease-key/union.

6. **Splay Trees**: Self-adjusting trees achieve O(log n) amortized access with no explicit balance information, exploiting locality.

### Delhi University Syllabus Alignment

This material covers:
- ✓ All three amortized analysis methods with formal treatment
- ✓ Dynamic table expansion (mandatory example)
- ✓ Fibonacci heaps (priority queue operations)
- ✓ Splay trees (self-adjusting data structures)
- ✓ Mathematical rigor suitable for MSc level

### Practical Applications

7. **System Design**: Understanding amortization helps design efficient data structures in databases, compilers, and runtime systems.

8. **Trade-offs**: Real systems often prefer amortized guarantees over worst-case for better practical performance.

---

## 11. References and Further Reading

### Primary References

1. **Cormen, T. H., et al.** *Introduction to Algorithms* (4th ed.) — Chapters 17 and 19
2. **Fredman, M. T., & Tarjan, R. E.** "Fibonacci heaps and their uses in improved network optimization algorithms" — *JACM*, 1987
3. **Sleator, D. D., & Tarjan, R. E.** "Self-Adjusting Binary Search Trees" — *JACM*, 1985

### Additional Resources

4. **Tarjan, R. E.** *Data Structures and Network Algorithms* — CBMS Regional Conference Series
5. **MIT OpenCourseWare** — 6.046J Design and Analysis of Algorithms (Amortized Analysis lectures)
6. **Stanford CS166** — Data Structures (Advanced amortized analysis)

### Delhi University Recommended Texts

- **Aho, Hopcroft, Ullman** — *The Design and Analysis of Computer Algorithms*
- **Sen, A. K.** — *Algorithms* (for Delhi University syllabus coverage)

---

*Document prepared for MSc CS, Delhi University — Advanced Algorithms*
*Last Updated: July 2025*