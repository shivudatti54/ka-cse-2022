# Functions: One-to-One and Onto

## Introduction

Functions are one of the most fundamental concepts in mathematics and computer science. In discrete mathematics, functions serve as the backbone for understanding relations, mappings, and transformations between sets. A function defines a specific type of relationship where every element from the domain is associated with exactly one element in the codomain. This precise definition makes functions essential for modeling computational processes, algorithms, and data structures.

In the context of computer science, functions (also called mappings or transformations) appear everywhere—from hash functions in databases to encryption algorithms in cryptography, from function calls in programming to state transitions in finite automata. Understanding whether a function is one-to-one (injective) or onto (surjective) helps us determine important properties like whether a function can be inverted, whether it preserves distinctness, and how it maps elements between sets of different sizes.

This topic becomes particularly crucial when studying inverse functions, function composition, and cardinality of sets—concepts that form the foundation for understanding computational complexity and algorithmic efficiency. In this module, we will explore the formal definitions of functions, examine the properties of one-to-one and onto functions, and develop the skills needed to analyze these properties in various contexts.

## Key Concepts

### Definition of a Function

A **function** f from set A (called the **domain**) to set B (called the **codomain**) is a relation such that every element of A is associated with exactly one element of B. We denote this as f: A → B.

For each a ∈ A, we denote f(a) as the **image** of a under f. The set of all images is called the **range** (or **image**) of f, denoted as f(A) = {f(a) : a ∈ A}. Note that the range is always a subset of the codomain.

**Important**: For a relation to be a function:
1. Every element in the domain must have an image (no element is left unmapped)
2. Each element in the domain maps to exactly one element in the codomain (uniqueness)

### One-to-One (Injective) Functions

A function f: A → B is called **one-to-one** (or **injective**) if different elements in the domain map to different elements in the codomain. Formally:

f is one-to-one if for all a₁, a₂ ∈ A, if a₁ ≠ a₂ then f(a₁) ≠ f(a₂).

Equivalently, f is one-to-one if for all a₁, a₂ ∈ A, if f(a₁) = f(a₂) then a₁ = a₂.

This property ensures that no two distinct domain elements share the same image. Think of it like a one-way street where each house (domain element) has a unique mailbox (codomain element).

**One-to-one functions** are also called **injective functions** or **injections**.

### Onto (Surjective) Functions

A function f: A → B is called **onto** (or **surjective**) if every element in the codomain has at least one preimage in the domain. Formally:

f is onto if for every b ∈ B, there exists an a ∈ A such that f(a) = b.

In other words, the range of f equals its codomain: f(A) = B.

This property ensures that the function "covers" all elements in the codomain. Think of it like every mailbox (codomain element) must have at least one letter (domain element mapped to it).

**Onto functions** are also called **surjective functions** or **surjections**.

### Bijective Functions

A function f: A → B that is both one-to-one and onto is called **bijective** (or a **bijection**). For a bijective function:

- Every element in B is mapped to by exactly one element in A
- The domain and codomain have the same cardinality
- An inverse function f⁻¹: B → A exists

Bijections are extremely important in computer science because they establish a perfect "pairing" between two sets, enabling reversible transformations—crucial for encryption, compression, and many algorithms.

### Inverse Functions

If f: A → B is a bijective function, then its **inverse function** f⁻¹: B → A is defined by f⁻¹(b) = a if and only if f(a) = b.

For the inverse to exist, f must be bijective—it must be both one-to-one (to ensure uniqueness) and onto (to ensure every element in B has a preimage).

### Function Composition

If f: A → B and g: B → C are functions, the **composition** g ∘ f: A → C is defined by (g ∘ f)(a) = g(f(a)) for all a ∈ A.

An important theorem: If f and g are both one-to-one, then g ∘ f is one-to-one. If f and g are both onto, then g ∘ f is onto. Consequently, if both are bijective, then g ∘ f is bijective.

## Examples

### Example 1: Identifying One-to-One Functions

Let f: ℤ → ℤ be defined by f(x) = 3x + 1. Is f one-to-one?

**Solution:**

To prove f is one-to-one, we assume f(a₁) = f(a₂) and show that this implies a₁ = a₂.

Assume: f(a₁) = f(a₂)

Substituting the definition:
3a₁ + 1 = 3a₂ + 1

Subtract 1 from both sides:
3a₁ = 3a₂

Divide by 3:
a₁ = a₂

Since a₁ = a₂ follows from f(a₁) = f(a₂), the function f is one-to-one.

**Verification**: Let a₁ = 2, a₂ = 5
- f(2) = 3(2) + 1 = 7
- f(5) = 3(5) + 1 = 16
Different inputs give different outputs, confirming injectivity.

### Example 2: Identifying Onto Functions

Let f: ℤ → ℤ be defined by f(x) = 3x + 1. Is f onto?

**Solution:**

To check if f is onto, we need to determine if for every integer y in the codomain, there exists an integer x in the domain such that f(x) = y.

Solve y = 3x + 1 for x:
x = (y - 1)/3

For x to be an integer, y - 1 must be divisible by 3. But not every integer y satisfies this!

For example, let y = 2:
- x = (2 - 1)/3 = 1/3, which is not an integer

Therefore, f is NOT onto because y = 2 in the codomain has no preimage in the domain.

### Example 3: Analyzing a Bijection with Inverse

Let f: ℝ → ℝ be defined by f(x) = 2x + 5. Show that f is bijective and find f⁻¹.

**Solution:**

**Step 1: Prove one-to-one**
Assume f(a₁) = f(a₂)
2a₁ + 5 = 2a₂ + 5
2a₁ = 2a₂
a₁ = a₂
∴ f is one-to-one

**Step 2: Prove onto**
Let y ∈ ℝ (codomain). We need x ∈ ℝ such that f(x) = y.
2x + 5 = y
2x = y - 5
x = (y - 5)/2

Since y ∈ ℝ, (y - 5)/2 ∈ ℝ. Thus for every y, we can find x.
∴ f is onto

**Step 3: Find inverse**
Since f is bijective, f⁻¹ exists:
f⁻¹(y) = (y - 5)/2

Or in terms of x: f⁻¹(x) = (x - 5)/2

**Verification**: f(f⁻¹(x)) = 2((x - 5)/2) + 5 = (x - 5) + 5 = x ✓

### Example 4: Practical Computer Science Application

Consider a hash function h: {0,1}⁴ → {0,1}² that maps 4-bit keys to 2-bit bucket indices. Determine the nature of this function.

**Solution:**

- Domain size: 2⁴ = 16 possible keys
- Codomain size: 2² = 4 possible buckets

Since |domain| > |codomain|, by the pigeonhole principle, the function cannot be one-to-one. At least two keys must map to the same bucket.

This is a fundamental concept in hash tables—we accept collisions because we cannot have a one-to-one mapping when the domain is larger than the codomain. Good hash functions aim to be "as onto as possible" to minimize collisions.

## Exam Tips

1. **Memorize the formal definitions**: For one-to-one: f(a₁) = f(a₂) ⇒ a₁ = a₂. For onto: ∀b ∈ B, ∃a ∈ A such that f(a) = b. These are frequently tested in DU exams.

2. **Use counterexamples wisely**: To show a function is NOT one-to-one, find two distinct elements with the same image. To show NOT onto, find an element in the codomain with no preimage.

3. **Pigeonhole Principle applications**: If |domain| > |codomain|, the function cannot be one-to-one. If |domain| < |codomain|, the function cannot be onto. This saves calculation time.

4. **Linear functions f(x) = ax + b**: These are one-to-one if a ≠ 0. They are onto if the domain and codomain are both ℝ (or both ℤ to ℤ).

5. **Inverse exists only for bijections**: Always check both one-to-one AND onto before claiming an inverse exists.

6. **Composition preserves properties**: If f and g are both one-to-one, g∘f is one-to-one. Same for onto. This is an important theorem.

7. **Draw mapping diagrams**: For small finite sets, visualizing the mapping helps quickly determine injectivity and surjectivity.

8. **Practice with different number sets**: Be comfortable with functions between ℕ, ℤ, ℚ, ℝ, and finite sets.