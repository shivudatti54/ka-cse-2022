# Multiplicative Group of Integers Modulo p and Permutation Groups

## Table of Contents

- [Multiplicative Group of Integers Modulo p and Permutation Groups](#multiplicative-group-of-integers-modulo-p-and-permutation-groups)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Multiplicative Group of Integers Modulo p](#multiplicative-group-of-integers-modulo-p)
  - [Cyclic Groups and Generators](#cyclic-groups-and-generators)
  - [Permutation Groups](#permutation-groups)
  - [Alternating Group A_n](#alternating-group-an)
  - [Parity of Permutations](#parity-of-permutations)
- [Examples](#examples)
  - [Example 1: Finding Orders in Z11\*](#example-1-finding-orders-in-z11)
  - [Example 2: Decomposing a Permutation](#example-2-decomposing-a-permutation)
  - [Example 3: Using Fermat's Little Theorem](#example-3-using-fermats-little-theorem)
- [Exam Tips](#exam-tips)

## Introduction

Discrete Mathematics forms the theoretical foundation of computer science, and among its most important topics are algebraic structures including groups, rings, and fields. This module explores two fundamental types of groups that appear extensively in number theory, cryptography, and algebraic computations: the multiplicative group of integers modulo p and permutation groups.

The multiplicative group of integers modulo p, denoted as Zp\* or (Z/pZ)×, consists of all nonzero integers modulo p that have multiplicative inverses. When p is a prime number, this group has remarkable properties that form the backbone of modern cryptographic systems like RSA and elliptic curve cryptography. Understanding the structure of these finite groups helps computer scientists comprehend how encryption and decryption work at a fundamental level.

Permutation groups, on the other hand, deal with the study of bijective functions from a set to itself. These groups are central to group theory and have applications in puzzle solving (like Rubik's cube), combinatorial optimization, and understanding molecular symmetries in chemistry. The symmetric group Sn, comprising all permutations of n elements, serves as a fundamental example that illustrates many important group-theoretic concepts.

## Key Concepts

### Multiplicative Group of Integers Modulo p

**Definition:** Let p be a prime number. The multiplicative group modulo p, denoted Zp* or (Z/pZ)×, is defined as:
$$Z_p^* = \{[a]\_p \in Z_p : gcd(a, p) = 1\} = \{1, 2, 3, ..., p-1\}$$

Since p is prime, every nonzero element modulo p has a multiplicative inverse (this follows from Euclid's lemma). Therefore, Zp\* contains exactly p-1 elements.

**Group Properties of Zp\*:**

1. **Closure:** If a, b ∈ Zp*, then ab ∈ Zp* (the product of two integers coprime to p is also coprime to p)
2. **Associativity:** Multiplication modulo p is associative
3. **Identity:** The element 1 serves as the identity element
4. **Inverses:** Every element a ∈ Zp\* has a unique inverse a⁻¹ such that aa⁻¹ ≡ 1 (mod p)

**Order of the Group:** The order of Zp* is |Zp*| = p - 1. This is a fundamental result that follows from the definition.

**Euler's Theorem:** For any integer a coprime to n, we have:
$$a^{\phi(n)} \equiv 1 \pmod{n}$$
where φ(n) is Euler's totient function, counting integers from 1 to n that are coprime to n.

**Fermat's Little Theorem (Special Case):** For any integer a not divisible by prime p:
$$a^{p-1} \equiv 1 \pmod{p}$$

This theorem is a direct consequence of Euler's theorem since φ(p) = p - 1 for prime p.

### Cyclic Groups and Generators

**Definition:** A group G is called cyclic if there exists an element g ∈ G such that every element of G can be expressed as g^k for some integer k. The element g is called a generator or primitive root.

**Theorem:** The multiplicative group Zp* is cyclic for every prime p. This means there exists at least one generator g ∈ Zp* such that:
$$Z_p^* = \{g^1, g^2, g^3, ..., g^{p-1}\}$$

**Order of an Element:** The order of an element a ∈ Zp\* is the smallest positive integer k such that a^k ≡ 1 (mod p). We denote this as ord(a) = k.

**Lagrange's Theorem Application:** The order of any element in Zp\* divides p - 1. This is crucial for finding the order of elements and understanding the group's structure.

**Example:** For p = 7, Z7\* = {1, 2, 3, 4, 5, 6}. The element 3 is a generator because:

- 3¹ ≡ 3 (mod 7)
- 3² ≡ 2 (mod 7)
- 3³ ≡ 6 (mod 7)
- 3⁴ ≡ 4 (mod 7)
- 3⁵ ≡ 5 (mod 7)
- 3⁶ ≡ 1 (mod 7)

So ord(3) = 6 = p - 1, confirming 3 is a primitive root.

### Permutation Groups

**Definition:** A permutation of a set S is a bijective function from S to S. The set of all permutations of S, together with the operation of composition, forms a group called the symmetric group, denoted Sym(S) or S_n when S = {1, 2, ..., n}.

**Symmetric Group S_n:**

- Order: n! (factorial of n)
- Contains all possible rearrangements of n elements
- Non-abelian for n ≥ 3 (composition is not commutative)

**Cycle Notation:**
Permutations are often written in cycle notation. A cycle (a1 a2 a3 ... ak) means:

- a1 → a2
- a2 → a3
- ...
- ak → a1

Example: The permutation σ = (1 3 5)(2 4) means:

- 1 → 3, 3 → 5, 5 → 1 (3-cycle)
- 2 → 4, 4 → 2 (2-cycle)
- 6 → 6 (fixed point, often omitted)

**Disjoint Cycles:** Two cycles are disjoint if they have no elements in common. Disjoint cycles commute (can be multiplied in any order).

**Theorem:** Every permutation can be uniquely expressed (up to order) as a product of disjoint cycles.

### Alternating Group A_n

**Definition:** The alternating group A_n is the subgroup of S_n consisting of all even permutations. A permutation is even if it can be expressed as an even number of transpositions.

**Properties:**

- Order: n!/2
- Index: 2 in S_n
- A_n is normal in S_n for n ≥ 2
- A_n is abelian only for n ≤ 3

### Parity of Permutations

**Transposition:** A transposition is a permutation that swaps exactly two elements and leaves all others fixed. It is a 2-cycle.

**Parity:** Every permutation can be expressed as a product of transpositions. The parity (even or odd) is invariant—the number of transpositions needed is either always even or always odd, never both.

**Sign of a Permutation:** The sign of a permutation σ is defined as:

- sign(σ) = +1 if σ is even
- sign(σ) = -1 if σ is odd

## Examples

### Example 1: Finding Orders in Z11\*

Find the order of element 2 in Z11\*.

**Solution:**
We need to find the smallest k such that 2^k ≡ 1 (mod 11).

Compute successive powers:

- 2¹ ≡ 2 (mod 11)
- 2² ≡ 4 (mod 11)
- 2³ ≡ 8 (mod 11)
- 2⁴ ≡ 16 ≡ 5 (mod 11)
- 2⁵ ≡ 10 (mod 11)
- 2⁶ ≡ 20 ≡ 9 (mod 11)
- 2⁷ ≡ 18 ≡ 7 (mod 11)
- 2⁸ ≡ 14 ≡ 3 (mod 11)
- 2⁹ ≡ 6 (mod 11)
- 2¹⁰ ≡ 12 ≡ 1 (mod 11)

Therefore, ord(2) = 10 in Z11*. Since 10 = 11 - 1, 2 is a primitive root (generator) of Z11*.

### Example 2: Decomposing a Permutation

Express the permutation σ = (1 4 6)(2 5)(3) in cycle notation and determine its parity.

**Solution:**
The permutation σ already shows the cycle decomposition:

- (1 4 6) is a 3-cycle
- (2 5) is a 2-cycle (transposition)
- (3) is a fixed point

To determine parity: A k-cycle can be written as (k-1) transpositions.

- (1 4 6) = (1 6)(1 4) = 2 transpositions
- (2 5) = 1 transposition

Total: 2 + 1 = 3 transpositions

Since 3 is odd, σ is an odd permutation. Therefore, σ ∉ A6.

### Example 3: Using Fermat's Little Theorem

Find the remainder when 3^100 is divided by 11.

**Solution:**
By Fermat's Little Theorem, for prime p = 11 and integer 3 not divisible by 11:
3^10 ≡ 1 (mod 11)

Now, 3^100 = (3^10)^10 ≡ 1^10 ≡ 1 (mod 11)

Therefore, the remainder is 1.

## Exam Tips

1. **Remember the order of Zp\* is p-1:** This is fundamental and frequently tested. For any prime p, Zp\* has exactly p-1 elements.

2. **Apply Fermat's Little Theorem for modular arithmetic:** When computing a^(p-1) mod p, the result is always 1 (when a is not divisible by p). Use this to simplify large exponents.

3. **To check if an element is a generator:** Verify that its order equals p-1. Compute powers until you reach 1; if you don't hit 1 before p-1, it's a generator.

4. **Parity of permutations:** Count transpositions carefully. A k-cycle decomposes into (k-1) transpositions. The total parity is even if total transpositions count is even.

5. **Disjoint cycles commute:** Remember this property when multiplying permutations—it simplifies calculations significantly.

6. **A_n contains exactly half of S_n:** This is useful when determining whether a permutation belongs to the alternating group.

7. **Lagrange's Theorem:** The order of any subgroup divides the group order. Similarly, the order of any element divides the group order.

8. **Cycle notation shortcuts:** Remember that (1 2 3)³ = identity, and any cycle raised to its length gives identity.
