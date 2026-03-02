# Set Operations and Computer Representation

## Introduction

Set theory forms the foundation of discrete mathematics and computer science. Sets are collections of distinct objects, and understanding how to manipulate them is essential for database systems, data structures, algorithm design, and boolean algebra. In this topic, we explore the fundamental set operations—union, intersection, difference, and complement—and their computer representations using bit vectors, which are crucial for efficient information processing in computing systems.

The study of set operations has profound practical applications. In database management systems, set operations form the basis of SQL queries (UNION, INTERSECT, EXCEPT). Search engines use set theory to process queries and retrieve relevant documents. In networking, set operations help in IP address filtering and firewall rule management. The bit-vector representation of sets enables fast processing in compilers, operating systems, and cryptography. This topic bridges mathematical theory with computational practice, making it indispensable for computer science students at Delhi University.

## Key Concepts

### Basic Set Operations

**Union (∪):** The union of two sets A and B, denoted A ∪ B, is the set containing all elements that belong to A, or B, or both. Formally: A ∪ B = {x | x ∈ A or x ∈ B}.

**Intersection (∩):** The intersection of two sets A and B, denoted A ∩ B, is the set containing only elements that belong to both A and B. Formally: A ∩ B = {x | x ∈ A and x ∈ B}.

**Difference (−):** The difference of sets A and B, denoted A − B, is the set of elements that belong to A but not to B. Formally: A − B = {x | x ∈ A and x ∉ B}.

**Complement (Ā or Aᶜ):** The complement of a set A with respect to the universal set U is the set of all elements in U that are not in A. Formally: Aᶜ = {x ∈ U | x ∉ A}.

### Set Identities and Laws

The following identities hold for all sets A, B, and C within universal set U:

- **Idempotent Laws:** A ∪ A = A and A ∩ A = A
- **Identity Laws:** A ∪ ∅ = A and A ∩ U = A
- **Domination Laws:** A ∪ U = U and A ∩ ∅ = ∅
- **Commutative Laws:** A ∪ B = B ∪ A and A ∩ B = B ∩ A
- **Associative Laws:** (A ∪ B) ∪ C = A ∪ (B ∪ C) and (A ∩ B) ∩ C = A ∩ (B ∩ C)
- **Distributive Laws:** A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) and A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
- **De Morgan's Laws:** (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ and (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ
- **Complement Laws:** A ∪ Aᶜ = U and A ∩ Aᶜ = ∅
- **Double Complement Law:** (Aᶜ)ᶜ = A

### Computer Representation of Sets

**Bit Vector (Bit String) Representation:**

When the universal set U is finite and can be enumerated as U = {u₁, u₂, ..., uₙ}, a set A ⊆ U is represented by an n-bit string called a **bit vector**. The i-th bit is 1 if uᵢ ∈ A, and 0 otherwise.

For example, if U = {a, b, c, d, e}, then:
- Set A = {a, c, e} is represented as bit vector: 10101
- Set B = {b, d} is represented as bit vector: 01010

**Operations on Bit Vectors:**

- **Union:** Use bitwise OR (∨) operation
- **Intersection:** Use bitwise AND (∧) operation  
- **Complement:** Use bitwise NOT (¬) operation on all bits

**Example:** Let U = {1, 2, 3, 4, 5}
- A = {1, 3, 5} → bit vector: 10101
- B = {2, 3, 4} → bit vector: 01110

- A ∪ B = {1, 2, 3, 4, 5} → 10101 ∨ 01110 = 11111
- A ∩ B = {3} → 10101 ∧ 01110 = 00100
- Aᶜ = {2, 4} → ¬10101 = 01010

## Examples

### Example 1: Verifying De Morgan's Law

**Problem:** Verify (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ using Venn diagram reasoning where U = {1,2,3,4,5,6}, A = {2,4,6}, B = {1,2,3}.

**Solution:**

Step 1: Find A ∩ B = {2}
Step 2: (A ∩ B)ᶜ = U − {2} = {1,3,4,5,6}

Now compute right side:
- Aᶜ = U − A = {1,3,5}
- Bᶜ = U − B = {4,5,6}
- Aᶜ ∪ Bᶜ = {1,3,5} ∪ {4,5,6} = {1,3,4,5,6}

Both sides equal {1,3,4,5,6}, verifying De Morgan's Law.

### Example 2: Bit Vector Operations

**Problem:** Let U = {w, x, y, z} (positions 1-4). Given A = {w, z} and B = {x, y, z}, find A ∪ B, A ∩ B, and A − B using bit vectors.

**Solution:**

First, establish bit positions: w→bit₁, x→bit₂, y→bit₃, z→bit₄

- A = {w, z} → 1001 (binary)
- B = {x, y, z} → 0111 (binary)

**Union (A ∪ B):** 1001 ∨ 0111 = 1111 → {w, x, y, z}

**Intersection (A ∩ B):** 1001 ∧ 0111 = 0001 → {z}

**Difference (A − B):** Elements in A not in B = {w}
To compute using bit vectors: A ∧ (NOT B) = 1001 ∧ 1000 = 1000 → {w}

### Example 3: Applying Distributive Law

**Problem:** If A = {1,2,3}, B = {2,3,4}, C = {3,4,5}, verify A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C).

**Solution:**

Compute B ∪ C = {2,3,4} ∪ {3,4,5} = {2,3,4,5}
Left side: A ∩ (B ∪ C) = {1,2,3} ∩ {2,3,4,5} = {2,3}

Compute individually:
- A ∩ B = {1,2,3} ∩ {2,3,4} = {2,3}
- A ∩ C = {1,2,3} ∩ {3,4,5} = {3}
Right side: {2,3} ∪ {3} = {2,3}

Both sides equal {2,3}, verifying the distributive law.

## Exam Tips

1. **Memorize all set identities:** De Morgan's Laws and Distributive Laws are frequently tested in DU semester exams. Practice proving these using element-to-element method.

2. **Understand bit vector operations:** When representing sets with bit vectors, remember: Union = OR, Intersection = AND, Complement = NOT. This is a favourite for 5-mark questions.

3. **Venn Diagram Approach:** For problems involving three sets, draw Venn diagrams to visualize A ∩ B, B ∩ C, A ∩ C, and A ∩ B ∩ C. This helps avoid confusion in complex problems.

4. **Compliment of Finite Sets:** When U is given explicitly, always list it completely. Remember: Aᶜ = U − A. This is crucial for complement operations.

5. **Distinguish Between − and ᶜ:** The difference A − B is not the same as complement unless B = Aᶜ. Many students lose marks by confusing these operations.

6. **Proof by Contradiction:** For showing set equality (A = B), prove A ⊆ B and B ⊆ A separately, or use algebraic manipulation with known identities.

7. **Symmetric Difference:** Remember the operation A ⊕ B = (A − B) ∪ (B − A) = (A ∪ B) − (A ∩ B). This operation appears in networking and error detection contexts.

8. **Practical Applications:** Be prepared to answer how sets are used in databases, search engines, or programming languages. This connects theory to real-world applications.