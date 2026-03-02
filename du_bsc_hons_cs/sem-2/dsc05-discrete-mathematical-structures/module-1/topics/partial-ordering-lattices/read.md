# Partial Ordering and Lattices

## Introduction

Partial ordering and lattices form fundamental concepts in discrete mathematics with profound applications in computer science, particularly in areas such as database theory, concurrency control, algorithm design, and formal semantics. A partial order generalizes the familiar notion of ordering by allowing elements to be incomparable under certain conditions, unlike total orders where every pair of elements is comparable.

The study of lattices, which are special types of partially ordered sets, provides powerful tools for understanding hierarchical structures, optimization problems, and algebraic manipulations. In the context of the University of Delhi's Computer Science curriculum, these concepts are essential for understanding data structures like heaps, understanding dependency graphs, and grasping the theoretical foundations of type systems in programming languages.

This topic connects abstract mathematical theory with practical computing applications, making it indispensable for any serious computer science undergraduate. The elegance of lattice theory lies in its ability to model both mathematical structures and real-world scenarios where elements have varying degrees of influence, importance, or dependency.

## Key Concepts

### 1. Partially Ordered Set (Poset)

A **partially ordered set** (or **poset**) is a pair (P, ≤) where P is a set and ≤ is a binary relation on P satisfying three properties:

- **Reflexivity**: For all a ∈ P, a ≤ a
- **Antisymmetry**: If a ≤ b and b ≤ a, then a = b
- **Transitivity**: If a ≤ b and b ≤ c, then a ≤ c

The relation ≤ is called a **partial order** or **poset order**. When (P, ≤) is a poset, we say that P is partially ordered by ≤.

**Example**: The power set of a set, ordered by set inclusion (⊆), forms a poset. For instance, with set {a, b, c}, we have {a} ⊆ {a, b} ⊆ {a, b, c}.

### 2. Comparable and Incomparable Elements

Two elements a and b in a poset (P, ≤) are **comparable** if either a ≤ b or b ≤ a holds. If neither condition is true, the elements are **incomparable**, denoted a || b.

In the poset (P({1,2,3}), ⊆), elements {1} and {2} are incomparable, while {1} and {1,2} are comparable.

### 3. Hasse Diagram

A **Hasse diagram** is a graphical representation of a finite poset where:
- Each element is represented as a vertex
- If a ≤ b and a ≠ b, then a appears below b
- If b covers a (meaning a < b and no element c exists such that a < c < b), a line connects a and b

Hasse diagrams eliminate the need to show transitive edges, making visualization cleaner. They are essential tools for understanding the structure of posets.

### 4. Maximal and Minimal Elements

An element m in a poset (P, ≤) is **maximal** if there is no element x ∈ P such that m < x. Similarly, an element m is **minimal** if there is no element x ∈ P such that x < m.

A poset can have multiple maximal or minimal elements, unlike total orders where at most one of each exists.

### 5. Greatest and Least Elements

An element g in a poset (P, ≤) is the **greatest element** (or **top**, denoted ⊤) if for all x ∈ P, x ≤ g. An element l is the **least element** (or **bottom**, denoted ⊥) if for all x ∈ P, l ≤ x.

If a greatest or least element exists, it is unique due to antisymmetry.

### 6. Upper and Lower Bounds

For a subset A of a poset (P, ≤):
- An **upper bound** of A is an element u ∈ P such that a ≤ u for all a ∈ A
- A **lower bound** of A is an element l ∈ P such that l ≤ a for all a ∈ A

The **least upper bound** (lub) or **supremum** of A is the least element among all upper bounds. The **greatest lower bound** (glb) or **infimum** of A is the greatest element among all lower bounds.

### 7. Lattice

A **lattice** is a poset (L, ≤) where every pair of elements has both a least upper bound and a greatest lower bound. For elements a, b ∈ L:
- The join (a ∨ b) is the least upper bound
- The meet (a ∧ b) is the greatest lower bound

A lattice is **bounded** if it has both a greatest element (⊤) and a least element (⊥).

### 8. Complete Lattice

A lattice L is **complete** if every subset of L has both a supremum and an infimum in L. Every finite lattice is complete, but infinite lattices may not be.

### 9. Distributive Lattice

A lattice (L, ≤, ∨, ∧) is **distributive** if for all a, b, c ∈ L:
- a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c)
- a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c)

The lattice of subsets of a set (power set) under union and intersection is distributive.

### 10. Complemented Lattice

A bounded lattice L is **complemented** if every element a ∈ L has a complement a' such that a ∨ a' = ⊤ and a ∧ a' = ⊥.

## Examples

### Example 1: Analyzing a Poset from Hasse Diagram

Consider the poset with elements {a, b, c, d, e, f} with covering relations: a < c, a < d, b < c, b < e, c < f, d < f, e < f.

**Step 1: Draw the Hasse Diagram**
- Level 0: a, b (minimal elements)
- Level 1: c, d, e
- Level 2: f (maximal element)

**Step 2: Find maximal and minimal elements**
- Minimal: a, b (no elements below them)
- Maximal: f (no element above it)

**Step 3: Check for greatest and least elements**
- No greatest element (a and b are incomparable, both below f)
- No least element (a and b are both minimal)

**Step 4: Find bounds for subset {c, d}**
- Upper bounds: f (since c < f and d < f)
- Lower bounds: a (since a < c and a < d)
- Least upper bound: f
- Greatest lower bound: a

### Example 2: Proving a Lattice

Show that the interval [0, 1] of real numbers with usual ordering is a complete bounded lattice.

**Solution:**
- **Bounded**: 0 ≤ x ≤ 1 for all x ∈ [0,1], so ⊥ = 0 and ⊥ = 1 exist
- **Every pair has meet and join**: For any a, b ∈ [0,1]:
  - meet = min(a, b) ∈ [0,1]
  - join = max(a, b) ∈ [0,1]
- **Complete**: For any subset S ⊆ [0,1]:
  - sup(S) exists (either maximum if finite, or least upper bound in reals)
  - inf(S) exists (similar argument)
- Therefore, [0,1] is a complete bounded lattice.

### Example 3: Non-Distributive Lattice

Consider the lattice M₃ (the "diamond" with middle elements) shown below:

```
      ⊤
     /|\
    a b c
     \|/
      ⊥
```

With a ∨ b = a ∨ c = b ∨ c = ⊤ and a ∧ b = a ∧ c = b ∧ c = ⊥.

**Check distributivity**: Take a, b, c:
- a ∧ (b ∨ c) = a ∧ ⊤ = a
- (a ∧ b) ∨ (a ∧ c) = ⊥ ∨ ⊥ = ⊥
- Since a ≠ ⊥, distributivity fails.

This is the famous M₃ non-distributive lattice, one of the two minimal non-distributive lattices (the other being N₅, the pentagon lattice).

## Exam Tips

1. **Understand the difference between maximal/minimal and greatest/least elements**: This is a common exam question. Remember: greatest/least elements must compare with ALL elements, while maximal/minimal only need no element greater/less than them.

2. **Practice drawing Hasse diagrams**: Many questions ask you to draw or interpret Hasse diagrams. Remember the rules: no arrows, transitive edges implied, minimal elements at bottom.

3. **Know the criteria for lattice property**: To verify a poset is a lattice, check that every pair has both supremum and infimum. For finite sets, you can often determine this from the Hasse diagram.

4. **Remember the two minimal non-distributive lattices**: M₃ (diamond) and N₅ (pentagon) are counterexamples in many proofs. Know their structures.

5. **Application-based questions**: Be prepared for questions connecting lattices to real scenarios like dependency graphs, version control, or database schemas.

6. **Theorems to remember**: Every finite poset has maximal and minimal elements; every finite lattice is complete; in a distributive lattice, complements (if they exist) are unique.

7. **Time management in exams**: For proof questions, clearly state which properties (reflexivity, antisymmetry, transitivity) you are verifying.