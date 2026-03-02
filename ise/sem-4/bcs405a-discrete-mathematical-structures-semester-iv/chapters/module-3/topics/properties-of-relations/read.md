# Properties of Relations

## Introduction to Relation Properties

In discrete mathematics, a **relation** R from a set A to a set B is a subset of the Cartesian product A × B. When A = B, we call R a **relation on A**. The properties of relations—specifically reflexive, symmetric, antisymmetric, and transitive—determine important classifications such as equivalence relations and partial orders, which are fundamental in computer science applications like database design, software specification, and algorithm analysis.

## Core Properties of Relations

### Reflexive Property

A relation R on a set A is **reflexive** if every element is related to itself. Formally:

∀a ∈ A, (a, a) ∈ R

**Example 1:** The relation "is equal to" (=) on the set of integers ℤ is reflexive because every integer equals itself.

**Example 2:** The relation "divides" on the set of positive integers ℤ⁺ is reflexive because every positive integer divides itself.

**Non-Example:** The relation "is greater than" (>) on ℤ is not reflexive because no integer is greater than itself.

```
Reflexive Relation Diagram:
Elements: a, b, c
Relations: (a,a), (b,b), (c,c), (a,b), (b,c)

a ---> a
b ---> b
c ---> c
a ---> b
b ---> c
```

### Symmetric Property

A relation R on a set A is **symmetric** if whenever an element a is related to b, then b is also related to a. Formally:

∀a, b ∈ A, if (a, b) ∈ R then (b, a) ∈ R

**Example 1:** The relation "is married to" on a set of people is symmetric (if person A is married to person B, then B is married to A).

**Example 2:** The relation "is a sibling of" is symmetric.

**Non-Example:** The relation "is a parent of" is not symmetric.

```
Symmetric Relation Diagram:
Elements: a, b, c
Relations: (a,b), (b,a), (b,c), (c,b)

a <---> b
b <---> c
```

### Antisymmetric Property

A relation R on a set A is **antisymmetric** if whenever both (a, b) and (b, a) are in R, then a must equal b. Formally:

∀a, b ∈ A, if (a, b) ∈ R and (b, a) ∈ R then a = b

**Example 1:** The relation "is a subset of" (⊆) on a power set is antisymmetric. If A ⊆ B and B ⊆ A, then A = B.

**Example 2:** The relation "≤" on real numbers is antisymmetric.

**Non-Example:** The relation "divides" on integers is antisymmetric, but the relation "is a friend of" might not be.

**Important Note:** Antisymmetric is not the opposite of symmetric. A relation can be both symmetric and antisymmetric (e.g., the equality relation) or neither.

### Transitive Property

A relation R on a set A is **transitive** if whenever an element a is related to b, and b is related to c, then a is related to c. Formally:

∀a, b, c ∈ A, if (a, b) ∈ R and (b, c) ∈ R then (a, c) ∈ R

**Example 1:** The relation "is an ancestor of" is transitive (if A is an ancestor of B and B is an ancestor of C, then A is an ancestor of C).

**Example 2:** The relation "is less than" (<) on real numbers is transitive.

**Non-Example:** The relation "is the mother of" is not transitive.

```
Transitive Relation Diagram:
Elements: a, b, c
Relations: (a,b), (b,c), and therefore (a,c) must exist

a ---> b ---> c
 \           /
  ---->-----
```

## Property Combinations and Special Relations

### Equivalence Relations

A relation is an **equivalence relation** if it is reflexive, symmetric, and transitive. Equivalence relations partition sets into equivalence classes.

**Example:** The relation "has the same remainder when divided by n" (congruence modulo n) on integers is an equivalence relation.

- Reflexive: a ≡ a mod n
- Symmetric: if a ≡ b mod n then b ≡ a mod n
- Transitive: if a ≡ b mod n and b ≡ c mod n then a ≡ c mod n

### Partial Orders

A relation is a **partial order** if it is reflexive, antisymmetric, and transitive. Sets with partial orders are called posets (partially ordered sets).

**Example:** The relation "is a subset of" (⊆) on a power set is a partial order.

- Reflexive: A ⊆ A
- Antisymmetric: if A ⊆ B and B ⊆ A then A = B
- Transitive: if A ⊆ B and B ⊆ C then A ⊆ C

## Property Comparison Table

| Property      | Definition                                | Example         | Counterexample      |
| ------------- | ----------------------------------------- | --------------- | ------------------- |
| Reflexive     | ∀a ∈ A, (a,a) ∈ R                         | = on ℤ          | > on ℤ              |
| Symmetric     | if (a,b) ∈ R then (b,a) ∈ R               | "is married to" | "is parent of"      |
| Antisymmetric | if (a,b) ∈ R and (b,a) ∈ R then a = b     | ⊆ on sets       | "is friend of"      |
| Transitive    | if (a,b) ∈ R and (b,c) ∈ R then (a,c) ∈ R | < on ℝ          | "is square root of" |

## Matrix Representation of Properties

Relations on finite sets can be represented by matrices, where properties have specific patterns:

- **Reflexive**: All main diagonal entries are 1
- **Symmetric**: Matrix is symmetric (M = Mᵀ)
- **Antisymmetric**: For i ≠ j, not both mᵢⱼ = 1 and mⱼᵢ = 1

## Algorithm for Checking Properties

For a relation R on a finite set A with n elements:

1. **Reflexivity**: Check if (aᵢ, aᵢ) ∈ R for all i = 1,...,n
2. **Symmetry**: For each (aᵢ, aⱼ) ∈ R, verify (aⱼ, aᵢ) ∈ R
3. **Antisymmetry**: For each pair (aᵢ, aⱼ) and (aⱼ, aᵢ) in R with i ≠ j, check if aᵢ = aⱼ
4. **Transitivity**: For each pair (aᵢ, aⱼ) ∈ R and (aⱼ, aₖ) ∈ R, verify (aᵢ, aₖ) ∈ R

## Exam Tips

1. **Memorize the formal definitions** of each property with quantifiers (∀, ∃)
2. **Create your own examples** for each property using small sets (2-3 elements)
3. **Practice with both mathematical and real-world relations**
4. **For proofs**: Use the formal definitions directly
5. **For counterexamples**: Try to find the smallest possible violation
6. **Remember**: A relation can have multiple properties simultaneously
7. **Watch for empty relations**: The empty relation is symmetric, antisymmetric, and transitive, but not reflexive (unless the set is empty)
