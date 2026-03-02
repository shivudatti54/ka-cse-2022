# Properties of Groups

## Table of Contents

- [Properties of Groups](#properties-of-groups)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of a Group](#definition-of-a-group)
  - [Properties of Groups](#properties-of-groups)
  - [Types of Groups](#types-of-groups)
  - [Subgroups](#subgroups)
  - [Important Theorems](#important-theorems)
- [Examples](#examples)
  - [Example 1: Verifying Group Properties](#example-1-verifying-group-properties)
  - [Example 2: Finding Order of Elements](#example-2-finding-order-of-elements)
  - [Example 3: Subgroup Verification](#example-3-subgroup-verification)
- [Exam Tips](#exam-tips)

## Introduction

Group theory is one of the most fundamental branches of abstract algebra and forms the backbone of modern algebra. A group is a mathematical structure consisting of a set equipped with a binary operation that combines any two elements to produce a third element, while satisfying four fundamental properties: closure, associativity, identity, and invertibility. The study of groups and their properties is crucial in various fields of computer science, including cryptography, coding theory, algorithm design, and formal language theory.

In this topic, we explore the essential properties of groups, which are critical for understanding more advanced algebraic structures like rings, fields, and vector spaces. For CSE students, mastering group properties is essential as they form the foundation for understanding finite state machines, automata theory, and error-correcting codes. This module covers the classification of groups, important theorems, and practical examples that are frequently tested in university examinations.

## Key Concepts

### Definition of a Group

A **group** (G, _) is a set G together with a binary operation _ such that the following four axioms are satisfied:

1. **Closure**: For all a, b ∈ G, a \* b ∈ G
2. **Associativity**: For all a, b, c ∈ G, (a _ b) _ c = a _ (b _ c)
3. **Identity Element**: There exists an element e ∈ G such that a _ e = e _ a = a for all a ∈ G
4. **Inverse Element**: For each a ∈ G, there exists an element a⁻¹ ∈ G such that a _ a⁻¹ = a⁻¹ _ a = e

### Properties of Groups

#### 1. Uniqueness of Identity Element

In any group, the identity element is unique. This is a fundamental property that must be proven.

**Proof**: Suppose e and f are both identity elements in group G. Then:

- Since e is identity: e \* f = f
- Since f is identity: e \* f = e
- Therefore, e = f

Thus, the identity element in a group is unique.

#### 2. Uniqueness of Inverse

For each element in a group, its inverse is unique.

**Proof**: Let a ∈ G and suppose b and c are both inverses of a. Then:

- a _ b = e and a _ c = e
- Multiply by a⁻¹ on the left: a⁻¹ _ a _ b = a⁻¹ \* e
- e \* b = a⁻¹, so b = a⁻¹
- Similarly, c = a⁻¹
- Therefore, b = c

#### 3. Cancellation Laws

In any group, both left and right cancellation laws hold:

- If a _ b = a _ c, then b = c (Left Cancellation)
- If b _ a = c _ a, then b = c (Right Cancellation)

**Proof**: Multiply a _ b = a _ c on the left by a⁻¹:
a⁻¹ _ (a _ b) = a⁻¹ _ (a _ c)
(a⁻¹ _ a) _ b = (a⁻¹ _ a) _ c
e _ b = e _ c
b = c

#### 4. Properties of Inverses

For any group element a ∈ G:

- (a⁻¹)⁻¹ = a (the inverse of the inverse is the original element)
- (a _ b)⁻¹ = b⁻¹ _ a⁻¹ (inverse of a product)
- a _ a = a², and more generally, aⁿ _ aᵐ = aⁿ⁺ᵐ

#### 5. Order of a Group

The **order** of a group G, denoted |G|, is the number of elements in G. A group is called:

- **Finite Group**: If it contains a finite number of elements
- **Infinite Group**: If it contains infinitely many elements

#### 6. Order of an Element

The **order** of an element a ∈ G is the smallest positive integer n such that aⁿ = e (where e is the identity). If no such n exists, the element has infinite order.

### Types of Groups

#### Abelian Groups (Commutative Groups)

A group (G, _) is called **abelian** or **commutative** if the operation is commutative:
a _ b = b \* a for all a, b ∈ G

**Examples**: (ℤ, +), (ℚ, +), (ℝ, +), (ℤₙ, +ₙ) are all abelian groups.

**Non-Example**: The symmetric group Sₙ (group of all permutations) is non-abelian for n ≥ 3.

#### Cyclic Groups

A group G is **cyclic** if there exists an element a ∈ G such that every element of G can be expressed as aⁿ for some integer n. The element a is called the **generator** of the group.

**Properties of Cyclic Groups**:

- Every cyclic group is abelian
- A cyclic group of order n is isomorphic to (ℤₙ, +ₙ)
- All subgroups of a cyclic group are cyclic
- The number of generators in a cyclic group of order n is φ(n), where φ is Euler's totient function

#### Finite and Infinite Groups

- **Finite Group**: The symmetric group S₃ has order 6
- **Infinite Group**: The group of integers (ℤ, +) is infinite

### Subgroups

A **subgroup** H of a group G is a subset of G that forms a group under the same operation as G.

**Necessary and Sufficient Conditions for Subgroup**:
For a nonempty subset H of G to be a subgroup:

1. For all a, b ∈ H, a \* b ∈ H (closure)
2. For all a ∈ H, a⁻¹ ∈ H (inverse)

Alternatively, H is a subgroup if and only if for all a, b ∈ H, a \* b⁻¹ ∈ H.

**Proper Subgroup**: A subgroup H is proper if H ≠ G.

**Trivial Subgroup**: {e} is called the trivial subgroup.

### Important Theorems

#### Lagrange's Theorem

If H is a subgroup of a finite group G, then the order of H divides the order of G. Moreover, the number of left cosets of H in G is |G|/|H|.

#### Cayley's Theorem

Every group of order n is isomorphic to a subgroup of the symmetric group Sₙ.

#### Euler's Theorem

For any integer a and n such that gcd(a, n) = 1:
a^φ(n) ≡ 1 (mod n)

#### Fermat's Little Theorem (Special Case)

For any prime p and integer a not divisible by p:
a^(p-1) ≡ 1 (mod p)

## Examples

### Example 1: Verifying Group Properties

**Problem**: Show that (ℤ₅, +₅) is an abelian group.

**Solution**:

**Step 1: Check Closure**
For any [a], [b] ∈ ℤ₅, [a] +₅ [b] = [a + b] ∈ ℤ₅ since a + b is an integer.
The result is taken modulo 5, so the sum is always in ℤ₅.

**Step 2: Check Associativity**
([a] +₅ [b]) +₅ [c] = [a + b] +₅ [c] = [(a + b) + c] = [a + (b + c)] = [a] +₅ ([b] +₅ [c])

**Step 3: Find Identity Element**
[0] is the identity element since [a] +₅ [0] = [a + 0] = [a] and [0] +₅ [a] = [a].

**Step 4: Find Inverse Elements**
For [a] ∈ ℤ₅, the inverse is [5-a] (or equivalently [-a]):
[a] +₅ [5-a] = [a + 5 - a] = [5] = [0]

**Step 5: Check Commutativity**
[a] +₅ [b] = [a + b] = [b + a] = [b] +₅ [a]

Since all group axioms are satisfied, (ℤ₅, +₅) is an abelian group.

### Example 2: Finding Order of Elements

**Problem**: In the cyclic group (ℤ₁₂, +₁₂), find the order of [8] and list all generators.

**Solution**:

The identity element is [0].

**Finding order of [8]**:

- [8]¹ = [8] ≠ [0]
- [8]² = [8] +₁₂ [8] = [16] = [4] ≠ [0]
- [8]³ = [8]² +₁₂ [8] = [4] +₁₂ [8] = [12] = [0]

Therefore, the order of [8] is 3.

**Finding generators of ℤ₁₂**:
An element [a] is a generator if gcd(a, 12) = 1.
Numbers coprime to 12: 1, 5, 7, 11

Therefore, generators are [1], [5], [7], [11].
Number of generators = φ(12) = φ(2² × 3) = 12 × (1 - 1/2) × (1 - 1/3) = 12 × 1/2 × 2/3 = 4

### Example 3: Subgroup Verification

**Problem**: Determine whether H = {0, 3, 6, 9} is a subgroup of (ℤ₁₂, +₁₂).

**Solution**:

**Method 1: Using Subgroup Criteria**

Check closure: For any a, b ∈ H, does a +₁₂ b ∈ H?

- 3 +₁₂ 3 = 6 ∈ H
- 3 +₁₂ 6 = 9 ∈ H
- 9 +₁₂ 9 = 6 ∈ H
  All possible sums are in H. Closure is satisfied.

Check inverses:

- Inverse of 0 is 0 (in H)
- Inverse of 3: 3 +₁₂ 9 = 12 ≡ 0, so 9 is inverse (in H)
- Inverse of 6: 6 +₁₂ 6 = 12 ≡ 0, so 6 is its own inverse (in H)
- Inverse of 9: 9 +₁₂ 3 = 12 ≡ 0, so 3 is inverse (in H)

Since H is nonempty and satisfies closure and inverse properties, H is a subgroup.

**Method 2: Using Lagrange's Theorem**
|H| = 4, |G| = 12, and 4 divides 12. The subgroup test confirms H is valid.

## Exam Tips

1. **Memorize the four group axioms**: Closure, Associativity, Identity, and Inverses. Most exam questions ask you to verify whether a given set with operation forms a group.

2. **Always check closure first**: Many students forget to verify closure, which is the most basic requirement. Remember to show that the operation result stays within the set.

3. **Know the difference between abelian and non-abelian groups**: Remember that (ℤ, +), (ℤₙ, +ₙ) are abelian, while Sₙ for n ≥ 3 and general linear groups GL(n) are non-abelian.

4. **Understand cyclic groups thoroughly**: Every cyclic group is abelian but not vice versa. Know how to find generators using gcd(a, n) = 1.

5. **Apply Lagrange's Theorem effectively**: Remember that subgroup order must divide group order. This is frequently tested in numerical problems.

6. **Be careful with notation**: Don't confuse a⁻¹ (inverse) with a^(-1) (reciprocal in multiplicative notation). The meaning depends on context.

7. **Practice finding orders**: The order of elements and groups are commonly asked. Remember: aⁿ = e defines the order of a.

8. **Know the identity element**: For (ℤₙ, +ₙ), identity is 0. For (ℤₙ, ×ₙ), identity is 1 (excluding 0 if we're looking at multiplicative group).
