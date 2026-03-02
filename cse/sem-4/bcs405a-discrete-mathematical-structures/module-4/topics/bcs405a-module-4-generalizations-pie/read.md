# Generalizations of the Principle of Inclusion-Exclusion

## Table of Contents

- [Generalizations of the Principle of Inclusion-Exclusion](#generalizations-of-the-principle-of-inclusion-exclusion)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Basic Principle of Inclusion-Exclusion (For 2 and 3 Sets)](#basic-principle-of-inclusion-exclusion-for-2-and-3-sets)
  - [Generalization to n Sets](#generalization-to-n-sets)
  - [Alternative Formulation Using Complement](#alternative-formulation-using-complement)
  - [Sieve Method (Derangements)](#sieve-method-derangements)
  - [Generalizations: Restricted Positions and Rook Polynomials](#generalizations-restricted-positions-and-rook-polynomials)
- [Examples](#examples)
  - [Example 1: Counting Numbers Not Divisible by 2, 3, or 5](#example-1-counting-numbers-not-divisible-by-2-3-or-5)
  - [Example 2: Counting Derangements (Subfactorials)](#example-2-counting-derangements-subfactorials)
  - [Example 3: Onto Functions](#example-3-onto-functions)
- [Exam Tips](#exam-tips)

## Introduction

The Principle of Inclusion-Exclusion (PIE) is a fundamental counting technique in combinatorics that allows us to count the number of elements in the union of finite sets by systematically adding and subtracting intersections. While the basic principle works well for two and three sets, real-world combinatorial problems often require counting unions of many sets, making generalizations essential. This topic explores the extensions of PIE to n sets, applications to complex counting problems, and alternative formulations that make calculations more tractable.

Generalizations of the Principle of Inclusion-Exclusion have significant applications in number theory (counting numbers not divisible by certain integers), combinatorics (derangements, surjections), and probability theory. Understanding these generalizations equips students with powerful tools to solve problems that would otherwise seem intractable using elementary counting methods.

## Key Concepts

### Basic Principle of Inclusion-Exclusion (For 2 and 3 Sets)

For two sets A and B:
|A ∪ B| = |A| + |B| - |A ∩ B|

For three sets A, B, and C:
|A ∪ B ∪ C| = |A| + |B| + |C| - |A ∩ B| - |A ∩ C| - |B ∩ C| + |A ∩ B ∩ C|

The pattern involves alternately adding and subtracting intersections of increasing cardinality.

### Generalization to n Sets

For n sets A₁, A₂, ..., Aₙ, the Principle of Inclusion-Exclusion states:

|A₁ ∪ A₂ ∪ ... ∪ Aₙ| = Σ|Aᵢ| - Σ|Aᵢ ∩ Aⱼ| + Σ|Aᵢ ∩ Aⱼ ∩ Aₖ| - ... + (-1)ⁿ⁻¹|A₁ ∩ A₂ ∩ ... ∩ Aₙ|

In summation notation:
|A₁ ∪ ... ∪ Aₙ| = Σ(k=1 to n) (-1)ᵏ⁻¹ × (sum of sizes of all k-wise intersections)

The number of terms in the k-th summation equals C(n, k), the binomial coefficient.

### Alternative Formulation Using Complement

Let U be the universal set. The number of elements in the complement of the union (elements not in any Aᵢ) is:

|N| = |U| - |A₁ ∪ ... ∪ Aₙ| = |U| + Σ(k=1 to n) (-1)ᵏ × (sum of sizes of all k-wise intersections)

This formulation is often more useful when counting elements satisfying none of the properties.

### Sieve Method (Derangements)

The inclusion-exclusion principle is also called the sieve method. The term "sieve" comes from the ancient Greek Eratosthenes' sieve for finding prime numbers. The method "sifts out" unwanted elements by successively removing intersections.

If we define:

- Sᵢ = set of elements having property Pᵢ
- N(Pᵢ) = number of elements with property Pᵢ
- N(PᵢPⱼ) = number of elements with both properties Pᵢ and Pⱼ

Then the number of elements with none of the n properties is:
N(0) = N - ΣN(Pᵢ) + ΣN(PᵢPⱼ) - ΣN(PᵢPⱼPₖ) + ... + (-1)ⁿN(P₁P₂...Pₙ)

### Generalizations: Restricted Positions and Rook Polynomials

When counting becomes complex due to restrictions, rook polynomials provide an alternative approach. A rook on a chessboard attacks all squares in its row and column. Counting placements of non-attacking rooks is equivalent to counting permutations with forbidden positions.

The rook polynomial of a board B is:
R(B, x) = Σ(k=0 to n) rₖ(B)xᵏ

where rₖ(B) is the number of ways to place k non-attacking rooks on board B.

The relationship with inclusion-exclusion: If rₖ represents the number of ways to place k non-attacking rooks, the number of ways to place n non-attacking rooks (complete matchings) equals Σ(k=0 to n) (-1)ᵏrₖ × (n-k)!.

## Examples

### Example 1: Counting Numbers Not Divisible by 2, 3, or 5

Find how many integers from 1 to 100 are not divisible by 2, 3, or 5.

**Solution:**
Let U = {1, 2, ..., 100}, so N = |U| = 100
Let A = numbers divisible by 2
Let B = numbers divisible by 3
Let C = numbers divisible by 5

Using floor division:

- |A| = ⌊100/2⌋ = 50
- |B| = ⌊100/3⌋ = 33
- |C| = ⌊100/5⌋ = 20

Intersections:

- |A ∩ B| = ⌊100/6⌋ = 16 (divisible by LCM(2,3) = 6)
- |A ∩ C| = ⌊100/10⌋ = 10
- |B ∩ C| = ⌊100/15⌋ = 6
- |A ∩ B ∩ C| = ⌊100/30⌋ = 3

Using PIE:
|A ∪ B ∪ C| = 50 + 33 + 20 - 16 - 10 - 6 + 3 = 74

Therefore, numbers NOT divisible by 2, 3, or 5:
= 100 - 74 = 26

### Example 2: Counting Derangements (Subfactorials)

Find the number of permutations of {1, 2, 3, 4} with no element in its original position (derangements).

**Solution:**
Let Pᵢ be the property that element i is in position i.
We want elements with none of these properties.

Total permutations: N = 4! = 24

Using inclusion-exclusion:

- N(Pᵢ) = (n-1)! = 3! = 6 for each i, so ΣN(Pᵢ) = 4 × 6 = 24
- N(PᵢPⱼ) = (n-2)! = 2! = 2 for each pair, and C(4,2) = 6 pairs, so ΣN(PᵢPⱼ) = 6 × 2 = 12
- N(PᵢPⱼPₖ) = (n-3)! = 1! = 1 for each triple, and C(4,3) = 4, so Σ = 4 × 1 = 4
- N(P₁P₂P₃P₄) = (n-4)! = 0! = 1

Derangements D₄ = 24 - 24 + 12 - 4 + 1 = 9

Formula: Dₙ = n! × Σ(k=0 to n) (-1)ᵏ/k! ≈ n!/e

### Example 3: Onto Functions

Find the number of surjective functions from a set of 4 elements to a set of 3 elements.

**Solution:**
We want functions f: A → B where |A| = 4, |B| = 3, and f is onto.

Total functions: 3⁴ = 81

Let Pᵢ = property that element i ∈ B is not in the image of f.
We need functions with none of these properties (i.e., all B elements appear).

For each element of B excluded, remaining choices: 2⁴ = 16
For each pair of B elements excluded: 1⁴ = 1
For all three excluded: 0⁴ = 0

Using inclusion-exclusion:
Number of onto functions = 3⁴ - C(3,1) × 2⁴ + C(3,2) × 1⁴ - C(3,3) × 0⁴
= 81 - 3 × 16 + 3 × 1 - 1 × 0
= 81 - 48 + 3 = 36

Formula: For m elements to n elements (m ≥ n):
S(m, n) × n! where S(m,n) is the Stirling number of the second kind

## Exam Tips

1. **Remember the alternating sign pattern**: Always start with addition for single sets, subtraction for double intersections, addition for triple intersections, and so on. The sign for k-wise intersections is (-1)ᵏ⁻¹.

2. **Use the complement form when convenient**: When counting elements that avoid certain properties, the complement formulation |A'| = |U| - |A| often simplifies calculations.

3. **For derangements, memorize the formula**: Dₙ = n! × (1 - 1/1! + 1/2! - 1/3! + ... + (-1)ⁿ/n!) or use the recurrence Dₙ = (n-1)(Dₙ₋₁ + Dₙ₋₂).

4. **Apply onto functions formula correctly**: Number of onto functions from m-element set to n-element set is nᵐ - C(n,1)(n-1)ᵐ + C(n,2)(n-2)ᵐ - ... + (-1)ⁿ⁻¹C(n,n-1)(1)ᵐ.

5. **Set up intersections carefully**: When dealing with divisibility problems, find the LCM of the divisors to compute intersections correctly.

6. **Don't forget the last term**: In inclusion-exclusion, the last term is always added when n is odd and subtracted when n is even (for union counting).

7. **Use rook polynomials for forbidden position problems**: When direct inclusion-exclusion becomes complex, the rook polynomial method provides an alternative combinatorial approach.

8. **Verify your answer**: Check that your result is reasonable—derangements must be less than n!, and union counts cannot exceed the universal set size.
