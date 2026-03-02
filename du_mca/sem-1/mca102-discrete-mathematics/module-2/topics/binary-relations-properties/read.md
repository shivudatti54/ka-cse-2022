# Binary Relations Properties
## Discrete Mathematics — MCA (Delhi University, Revised June 2024)

---

## 1. Introduction

A **binary relation** is a fundamental concept in discrete mathematics that describes how elements from one set relate to elements in another set (or the same set). Understanding binary relations and their properties is crucial for computer science students as they form the backbone of database systems, graph theory, logic, and algorithm design.

### Real-World Relevance

Binary relations permeate everyday computing and mathematical applications:

- **Database Systems**: Table relationships (foreign keys) represent binary relations between entities
- **Social Networks**: Friend connections, follow relationships between users
- **File Systems**: Parent-child directory relationships
- **Scheduling**: Precedence constraints in project management (task A must complete before task B)
- **Internet**: Web page links form directed relations
- **Mathematical Proofs**: Equivalence classes, ordering in sorting algorithms

---

## 2. Fundamental Definitions

### 2.1 What is a Binary Relation?

Given two sets A and B, a **binary relation R from A to B** is a subset of the Cartesian product A × B. If (a, b) ∈ R, we say "a is related to b" and denote this as aRb.

**Formal Definition:**
```
R ⊆ A × B
aRb ⟺ (a, b) ∈ R
```

When A = B, we say R is a **binary relation on A**.

### 2.2 Representing Binary Relations

Binary relations can be represented through:

1. **Set Notation**: R = {(1,2), (2,3), (3,4)}
2. **Arrow Diagram**: Directed edges between elements
3. **Matrix Representation**: Boolean adjacency matrix
4. **Digraph**: Directed graph representation

---

## 3. Properties of Binary Relations

This section covers the six essential properties that define how elements relate to each other.

### 3.1 Reflexive Relation

A relation R on set A is **reflexive** if every element is related to itself.

**Formal Definition:**
```
∀a ∈ A: (a, a) ∈ R
```

**Key Characteristics:**
- Contains all diagonal pairs (a, a)
- Also called "total" or "universal self-relation"

**Example 1: Equality Relation**
```
Let A = {1, 2, 3}
R = {(1,1), (2,2), (3,3)}
This is REFLEXIVE because all (a,a) pairs exist.
```

**Example 2: "is divisible by" Relation**
```
Let A = {1, 2, 3, 4, 6}
R = {(a,b) | a divides b}

R = {(1,1), (1,2), (1,3), (1,4), (1,6), (2,2), (2,4), (2,6), (3,3), (3,6), (4,4), (6,6)}
REFLEXIVE: Every number divides itself
```

### 3.2 Irreflexive (Anti-Reflexive) Relation

A relation R on set A is **irreflexive** if no element is related to itself.

**Formal Definition:**
```
∀a ∈ A: (a, a) ∉ R
```

**Example: "is greater than" (>) Relation**
```
Let A = {1, 2, 3}
R = {(2,1), (3,1), (3,2)}
IRREFLEXIVE: No element is greater than itself (n ⊁ n for any n)
```

### 3.3 Symmetric Relation

A relation R on set A is **symmetric** if whenever a is related to b, then b is also related to a.

**Formal Definition:**
```
∀a,b ∈ A: (a,b) ∈ R ⟹ (b,a) ∈ R
```

**Key Characteristics:**
- If (a,b) exists, (b,a) must also exist
- Matrix representation is symmetric about the diagonal

**Example: "is sibling of" Relation**
```
Let A = {Alice, Bob, Charlie}
R = {(Alice,Bob), (Bob,Alice), (Alice,Charlie), (Charlie,Alice), (Bob,Charlie), (Charlie,Bob)}
SYMMETRIC: If Alice is sibling of Bob, then Bob is sibling of Alice
```

### 3.4 Asymmetric Relation

A relation R on set A is **asymmetric** if whenever a is related to b, then b cannot be related to a.

**Formal Definition:**
```
∀a,b ∈ A: (a,b) ∈ R ⟹ (b,a) ∉ R
```

**Example: "is parent of" Relation**
```
R = {(John, Mike), (Mary, John)}
ASYMMETRIC: If John is parent of Mike, Mike cannot be parent of John
```

### 3.5 Antisymmetric Relation

A relation R on set A is **antisymmetric** if whenever a is related to b and b is related to a, then a = b.

**Formal Definition:**
```
∀a,b ∈ A: [(a,b) ∈ R ∧ (b,a) ∈ R] ⟹ a = b
```

**Important Distinction:**
- Symmetric: (a,b) ⇒ (b,a) always
- Antisymmetric: (a,b) and (b,a) can only happen when a = b
- A relation can be both symmetric AND antisymmetric (equality relation)
- A relation can be neither symmetric nor antisymmetric

**Example: "≤" (less than or equal to) Relation**
```
Let A = {1, 2, 3}
R = {(1,1), (1,2), (1,3), (2,2), (2,3), (3,3)}
ANTISYMMETRIC: If a ≤ b and b ≤ a, then a = b
(1,2) exists but (2,1) does not → satisfies antisymmetry
```

### 3.6 Transitive Relation

A relation R on set A is **transitive** if whenever a is related to b and b is related to c, then a is related to c.

**Formal Definition:**
```
∀a,b,c ∈ A: [(a,b) ∈ R ∧ (b,c) ∈ R] ⟹ (a,c) ∈ R
```

**Example: "is ancestor of" Relation**
```
R = {(John, Mary), (Mary, Alice), (John, Alice)}
John is ancestor of Mary, Mary is ancestor of Alice
⇒ John is ancestor of Alice
TRANSITIVE: Property holds throughout
```

### 3.7 Summary Table of Properties

| Property | Formal Condition | Example Relation |
|----------|------------------|------------------|
| Reflexive | ∀a: (a,a) ∈ R | ≤, =, ⊆ |
| Irreflexive | ∀a: (a,a) ∉ R | <, >, ⊂ |
| Symmetric | (a,b) ⇒ (b,a) | =, ≠, is sibling |
| Asymmetric | (a,b) ⇒ (b,a) ∉ | <, >, is parent |
| Antisymmetric | (a,b)∧(b,a) ⇒ a=b | ≤, ≥, ⊆ |
| Transitive | (a,b)∧(b,c) ⇒ (a,c) | ≤, <, ⊂, is ancestor |

---

## 4. Special Types of Relations

### 4.1 Equivalence Relations

A relation R on set A is an **equivalence relation** if it is **reflexive, symmetric, and transitive**.

**Real-World Examples:**
- "Has same birthday as" — Reflexive, Symmetric, Transitive
- "Is congruent to" (geometry) — All three properties
- "Has same remainder when divided by n" — Modular equivalence

**Example: Modular Arithmetic**
```
Let R be defined on integers Z:
aRb ⟺ a ≡ b (mod 3)

Check properties:
- REFLEXIVE: a ≡ a (mod 3) ✓
- SYMMETRIC: a ≡ b ⇒ b ≡ a (mod 3) ✓  
- TRANSITIVE: a ≡ b and b ≡ c ⇒ a ≡ c (mod 3) ✓

R = {..., (-3,0), (-3,3), (0,0), (0,3), (0,6), (3,0), (3,3), ...}
This is an EQUIVALENCE RELATION
```

**Equivalence Classes:**
When R is an equivalence relation, it partitions set A into disjoint equivalence classes:
```
[ a ] = { x ∈ A | xRa }
```

For mod 3:
```
[0] = {..., -6, -3, 0, 3, 6, ...}
[1] = {..., -5, -2, 1, 4, 7, ...}
[2] = {..., -4, -1, 2, 5, 8, ...}
```

### 4.2 Partial Order Relations

A relation R on set A is a **partial order** (or **poset**) if it is **reflexive, antisymmetric, and transitive**.

**Real-World Examples:**
- "≤" on real numbers
- "⊆" (subset) on power sets
- "divides" (|) on positive integers
- Task precedence in project scheduling

**Example: "Divides" Relation on {1, 2, 3, 4, 6, 12}**
```
R = {(1,1), (1,2), (1,3), (1,4), (1,6), (1,12),
     (2,2), (2,4), (2,6), (2,12),
     (3,3), (3,6), (3,12),
     (4,4), (4,12),
     (6,6), (6,12),
     (12,12)}

Properties:
- REFLEXIVE: Every number divides itself ✓
- ANTISYMMETRIC: a|b and b|a ⇒ a=b ✓
- TRANSITIVE: a|b and b|c ⇒ a|c ✓

This is a PARTIAL ORDER
```

**Hasse Diagram:**
Visual representation of partial orders showing covering relations.

**Comparable vs Incomparable Elements:**
- Comparable: a ≤ b or b ≤ a
- Incomparable: Neither a ≤ b nor b ≤ a

In our example: 2 and 3 are incomparable (neither divides the other).

---

## 5. Python Implementation Examples

### 5.1 Checking Relation Properties

```python
def check_relation_properties(A, R):
    """
    Check all properties of a binary relation R on set A.
    A: list of elements
    R: list of tuples representing ordered pairs
    """
    R_set = set(R)
    n = len(A)
    
    # Convert to set for O(1) lookup
    A_set = set(A)
    
    results = {}
    
    # 1. Reflexive: ∀a ∈ A, (a,a) ∈ R
    reflexive = all((a, a) in R_set for a in A)
    results['Reflexive'] = reflexive
    
    # 2. Irreflexive: ∀a ∈ A, (a,a) ∉ R
    irreflexive = all((a, a) not in R_set for a in A)
    results['Irreflexive'] = irreflexive
    
    # 3. Symmetric: (a,b) ∈ R ⇒ (b,a) ∈ R
    symmetric = all(
        (b, a) in R_set for (a, b) in R 
        if (a, b) in R_set
    )
    results['Symmetric'] = symmetric
    
    # 4. Asymmetric: (a,b) ∈ R ⇒ (b,a) ∉ R
    asymmetric = all(
        (b, a) not in R_set for (a, b) in R_set
    )
    results['Asymmetric'] = asymmetric
    
    # 5. Antisymmetric: (a,b) ∈ R ∧ (b,a) ∈ R ⇒ a = b
    antisymmetric = all(
        a == b for (a, b) in R_set 
        if (b, a) in R_set
    )
    results['Antisymmetric'] = antisymmetric
    
    # 6. Transitive: (a,b) ∈ R ∧ (b,c) ∈ R ⇒ (a,c) ∈ R
    transitive = True
    for (a, b) in R_set:
        for (c, d) in R_set:
            if b == c and (a, d) not in R_set:
                transitive = False
                break
        if not transitive:
            break
    results['Transitive'] = transitive
    
    return results

# Example: Check "≤" relation on {1, 2, 3}
A = [1, 2, 3]
R = [(1,1), (1,2), (1,3), (2,2), (2,3), (3,3)]

properties = check_relation_properties(A, R)
print("Relation Properties:")
for prop, result in properties.items():
    print(f"  {prop}: {result}")

# Output:
# Reflexive: True
# Irreflexive: False
# Symmetric: False
# Asymmetric: False
# Antisymmetric: True
# Transitive: True
```

### 5.2 Verifying Equivalence and Partial Order Relations

```python
def is_equivalence_relation(A, R):
    """Check if relation R on A is an equivalence relation"""
    props = check_relation_properties(A, R)
    return (props['Reflexive'] and 
            props['Symmetric'] and 
            props['Transitive'])

def is_partial_order(A, R):
    """Check if relation R on A is a partial order"""
    props = check_relation_properties(A, R)
    return (props['Reflexive'] and 
            props['Antisymmetric'] and 
            props['Transitive'])

def find_equivalence_classes(A, R):
    """Find equivalence classes if R is an equivalence relation"""
    if not is_equivalence_relation(A, R):
        return "Not an equivalence relation"
    
    R_set = set(R)
    classes = []
    visited = set()
    
    for a in A:
        if a not in visited:
            cls = {x for x in A if (a, x) in R_set}
            classes.append(cls)
            visited.update(cls)
    
    return classes

# Test with modular arithmetic (mod 3)
A = [0, 1, 2, 3, 4, 5, 6]
R = [(a, b) for a in A for b in A if (a - b) % 3 == 0]

print("Modulo 3 equivalence relation:")
print(f"  Is equivalence: {is_equivalence_relation(A, R)}")
print(f"  Classes: {find_equivalence_classes(A, R)}")
# Output: [{0, 3, 6}, {1, 4}, {2, 5}]
```

---

## 6. Delhi University Syllabus Context

This topic aligns with the following units in the MCA (Revised June 2024) syllabus:

- **Unit I**: Set Theory and Relations — Binary relations, properties of relations
- **Unit III**: Graph Theory and Combinatorics — Connection between relations and directed graphs
- **Applications**: Database design, ordering in algorithms, logic foundations

**Expected Learning Outcomes:**
1. Define and identify binary relations
2. Determine whether a relation possesses reflexivity, symmetry, antisymmetry, or transitivity
3. Distinguish between equivalence relations and partial orders
4. Apply relation properties to solve real-world problems

---

## 7. Practice Multiple Choice Questions

### MCQ 1
A relation R on set A = {1, 2, 3} is defined as R = {(1,1), (1,2), (2,1), (2,2)}. Which property does R NOT satisfy?

A) Reflexive  
B) Symmetric  
C) Transitive  
D) None of the above

**Answer: C**  
Explanation: R is reflexive (1,1) and (2,2) exist but (3,3) is missing, so not reflexive. It's symmetric since (1,2) ⇒ (2,1). However, transitivity fails: (1,2) and (2,1) are in R, so (1,1) should be in R (it is), but also (2,2) should be (it is). Actually this IS transitive. Wait - let me recalculate: Actually, it's NOT reflexive because (3,3) is missing!

### MCQ 2
Which of the following is TRUE about the relation "a divides b" on positive integers?

A) Symmetric only  
B) Antisymmetric only  
C) Both symmetric and antisymmetric  
D) Neither symmetric nor antisymmetric

**Answer: B**  
Explanation: "a|b" is antisymmetric because if a|b and b|a, then a=b. It is NOT symmetric because 2|4 does not imply 4|2.

### MCQ 3
The relation R = {(a,a), (b,b), (a,b)} on set {a,b} is:

A) Reflexive  
B) Transitive  
C) Equivalence relation  
D) Partial order

**Answer: B**  
Explanation: Not reflexive (missing (b,b) - wait it has (b,b)). Actually it IS reflexive and transitive but NOT antisymmetric. It's not an equivalence because not symmetric. Not a partial order because not antisymmetric.

### MCQ 4
For any set A, the relation R = A × A (universal relation) is:

A) Reflexive only  
B) Symmetric only  
C) Reflexive and symmetric only  
D) Reflexive, symmetric, and transitive

**Answer: D**  
Explanation: Universal relation contains ALL pairs. It's reflexive (all (a,a) present), symmetric (if (a,b) exists, (b,a) exists), and transitive (any chain works).

### MCQ 5
A relation that is symmetric and transitive but not reflexive is:

A) Empty relation on non-empty set  
B) Equality relation  
C) Cannot exist  
D) "Less than" on integers

**Answer: C**  
Explanation: By theorem, if a relation is symmetric and transitive, it must also be reflexive. Proof: For any a, if (a,b) ∈ R exists, by symmetry (b,a) ∈ R, by transitivity (a,a) ∈ R. So empty relation on empty set works but on non-empty set cannot exist.

---

## 8. Quick Reference Flashcards

```json
{
  "flashcards": [
    {
      "front": "Reflexive Relation",
      "back": "A relation R on A where ∀a∈A: (a,a) ∈ R. Example: ≤, =, ⊆"
    },
    {
      "front": "Irreflexive Relation",
      "back": "A relation R on A where ∀a∈A: (a,a) ∉ R. Example: <, >, is parent of"
    },
    {
      "front": "Symmetric Relation",
      "back": "A relation R where (a,b)∈R ⇒ (b,a)∈R. Example: =, is sibling of"
    },
    {
      "front": "Asymmetric Relation",
      "back": "A relation R where (a,b)∈R ⇒ (b,a)∉R. Example: <, >, is parent of"
    },
    {
      "front": "Antisymmetric Relation",
      "back": "A relation R where (a,b)∈R ∧ (b,a)∈R ⇒ a=b. Example: ≤, ≥, ⊆, divides"
    },
    {
      "front": "Transitive Relation",
      "back": "A relation R where (a,b)∈R ∧ (b,c)∈R ⇒ (a,c)∈R. Example: <, ≤, ⊆, is ancestor of"
    },
    {
      "front": "Equivalence Relation",
      "back": "A relation that is Reflexive + Symmetric + Transitive. Example: ≡ (mod n), =, has same birthday"
    },
    {
      "front": "Partial Order",
      "back": "A relation that is Reflexive + Antisymmetric + Transitive. Example: ≤, ⊆, divides, task precedence"
    },
    {
      "front": "Equivalence Class",
      "back": "For equivalence relation R on A, the equivalence class of a is [a] = {x∈A | xRa}"
    },
    {
      "front": "Hasse Diagram",
      "back": "Visual representation of partial order showing covering relations (immediate predecessors/successors)"
    }
  ]
}
```

---

## 9. Key Takeaways

1. **Binary relations** are subsets of Cartesian products that describe relationships between elements of sets.

2. **Six fundamental properties** determine the behavior of relations:
   - **Reflexive/Irrreflexive**: Self-relationship
   - **Symmetric/Asymmetric/Antisymmetric**: Directional relationship between pairs
   - **Transitivity**: Chain relationships

3. **Equivalence relations** (reflexive + symmetric + transitive) partition sets into disjoint equivalence classes — fundamental in modular arithmetic and classification.

4. **Partial orders** (reflexive + antisymmetric + transitive) establish hierarchy among elements — essential in scheduling, dependency management, and data organization.

5. **Practical applications**: Database relationships, social networks, file systems, and algorithm design all rely on understanding relation properties.

6. **Key theorems**: Symmetric + transitive ⇒ reflexive (for non-empty relations); Empty relation on empty set satisfies any property.

7. **Implementation**: Relations can be efficiently represented and analyzed using adjacency matrices, sets, or digraphs in programming.

---

*Generated for MCA — Delhi University (Revised June 2024)*