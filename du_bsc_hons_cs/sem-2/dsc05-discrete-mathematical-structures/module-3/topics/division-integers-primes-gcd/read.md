# Division in Integers, Primes, and GCD

## Introduction

Division in integers forms one of the foundational concepts in number theory, a branch of pure mathematics that deals with the properties and relationships of integers. The Division Algorithm, often called the Fundamental Theorem of Division, establishes the relationship between dividends, divisors, quotients, and remainders when one integer is divided by another. This theorem is not merely theoretical—it serves as the backbone for numerous algorithms in computer science, including cryptographic systems, error-correcting codes, and hashing functions.

Prime numbers, often described as the "atoms" of arithmetic, are integers greater than 1 that have no positive divisors other than 1 and themselves. The study of primes has fascinated mathematicians for millennia, from Euclid's elegant proof of their infinitude to the modern RSA cryptography that secures internet transactions. Understanding primes is essential for any computer scientist, as they play a crucial role in encryption algorithms, random number generation, and computational complexity theory.

The Greatest Common Divisor (GCD) represents the largest positive integer that divides two given integers without leaving a remainder. Computing the GCD efficiently is a fundamental problem with applications ranging from simplifying fractions to solving Diophantine equations. The Euclidean algorithm, developed over two millennia ago, remains one of the most efficient methods for GCD computation and exemplifies how ancient mathematical insights continue to power modern computing.

## Key Concepts

### The Division Algorithm

The Division Algorithm states that for any integer *a* and any positive integer *b*, there exist unique integers *q* (quotient) and *r* (remainder) such that:

**a = bq + r**, where **0 ≤ r < b**

The integer *a* is called the dividend, *b* is the divisor, *q* is the quotient, and *r* is the remainder. This seemingly simple statement has profound implications. It formalizes what we learn in elementary school—that when we divide one number by another, we get a quotient and possibly a remainder. The uniqueness of *q* and *r* is crucial: for given *a* and *b*, there is exactly one pair satisfying these conditions.

**Proof Sketch**: The proof uses the Well-Ordering Principle, which states that every non-empty set of non-negative integers has a least element. Consider the set S = {a - bk : k ∈ ℤ and a - bk ≥ 0}. This set is non-empty (choose k small enough), so it has a least element r. One can then show that 0 ≤ r < b, and a = bq + r for q = (a - r)/b.

### Prime Numbers

A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers. The first few primes are 2, 3, 5, 7, 11, 13, 17, 19, 23, and 29. Note that 2 is the only even prime—all other even numbers can be divided by 2.

**Euclid's Theorem (Infinitude of Primes)**: There are infinitely many prime numbers. The classic proof by contradiction assumes there are finitely many primes p₁, p₂, ..., pₙ. Consider the number N = p₁p₂...pₙ + 1. This number is not divisible by any of the listed primes (it leaves remainder 1 when divided by any of them), so either N is prime or has a prime divisor not in our list—contradicting the assumption.

**Fundamental Theorem of Arithmetic**: Every integer greater than 1 is either prime or can be expressed as a product of primes in a way that is unique up to the order of factors. This theorem, also known as the Unique Prime Factorization theorem, is foundational for number theory. It means every integer has a "prime factorization" that is essentially unique.

### Greatest Common Divisor (GCD)

For two integers *a* and *b* (not both zero), the greatest common divisor gcd(a, b) is the largest positive integer that divides both *a* and *b*. By convention, gcd(0, 0) is undefined, while gcd(a, 0) = |a| for any non-zero integer *a*.

**Properties of GCD**:
1. gcd(a, b) = gcd(b, a) — commutative
2. gcd(a, b) = gcd(-a, b) — sign doesn't matter
3. gcd(a, b) = gcd(a, b - qa) for any integer q — the key property behind Euclidean algorithm
4. If gcd(a, b) = d, then gcd(a/d, b/d) = 1 — the numbers become coprime

Two integers *a* and *b* are said to be **coprime** or **relatively prime** if gcd(a, b) = 1. For example, 8 and 15 are coprime even though neither is prime.

### The Euclidean Algorithm

The Euclidean algorithm provides an efficient method to compute gcd(a, b) using repeated division. The algorithm is based on the principle that gcd(a, b) = gcd(b, a mod b) when b ≠ 0.

**Algorithm**:
1. If b = 0, return |a|
2. Otherwise, compute r = a mod b
3. Return gcd(b, r)

This can be implemented recursively or iteratively. The algorithm runs in O(log min(a, b)) time, making it extremely efficient even for very large numbers—a property crucial for cryptographic applications involving numbers with hundreds of digits.

### Extended Euclidean Algorithm

The Extended Euclidean Algorithm not only computes gcd(a, b) but also finds integers *x* and *y* such that:

**ax + by = gcd(a, b)**

This equation, known as Bézout's identity, has significant applications in solving linear Diophantine equations and finding modular multiplicative inverses—essential for RSA decryption and other cryptographic protocols.

## Examples

### Example 1: Applying the Division Algorithm

**Problem**: When 417 is divided by 13, find the quotient and remainder.

**Solution**:
We need to find integers q and r such that 417 = 13q + r, with 0 ≤ r < 13.

Divide 417 by 13:
- 13 × 32 = 416
- 13 × 33 = 429 (too large)

So, q = 32 and r = 417 - 416 = 1

Verification: 13 × 32 + 1 = 416 + 1 = 417 ✓

The remainder is 1.

### Example 2: Using the Euclidean Algorithm

**Problem**: Find gcd(252, 198) using the Euclidean algorithm.

**Solution**:
Step 1: 252 = 198 × 1 + 54
         remainder = 54

Step 2: 198 = 54 × 3 + 36
         remainder = 36

Step 3: 54 = 36 × 1 + 18
         remainder = 18

Step 4: 36 = 18 × 2 + 0
         remainder = 0

When we reach a remainder of 0, the last non-zero remainder is the gcd.
Therefore, gcd(252, 198) = 18.

**Verification**: 
- 252 ÷ 18 = 14 (exactly)
- 198 ÷ 18 = 11 (exactly)
18 divides both numbers, and no larger number does.

### Example 3: Extended Euclidean Algorithm

**Problem**: Find integers x and y such that 35x + 15y = gcd(35, 15).

**Solution**:
First, find gcd(35, 15):
- 35 = 15 × 2 + 5
- 15 = 5 × 3 + 0

So gcd = 5.

Now work backwards to express 5 as a linear combination:
From 35 = 15 × 2 + 5, we get:
5 = 35 - 15 × 2
5 = 35 × 1 + 15 × (-2)

Thus, x = 1 and y = -2.

**Verification**: 35(1) + 15(-2) = 35 - 30 = 5 ✓

### Example 4: Prime Factorization

**Problem**: Express 420 as a product of primes.

**Solution**:
Using systematic division:
- 420 ÷ 2 = 210
- 210 ÷ 2 = 105
- 105 ÷ 3 = 35
- 35 ÷ 5 = 7
- 7 ÷ 7 = 1

Therefore, 420 = 2 × 2 × 3 × 5 × 7 = 2² × 3 × 5 × 7

This factorization is unique (up to ordering), as guaranteed by the Fundamental Theorem of Arithmetic.

## Exam Tips

1. **Remember the Division Algorithm conditions**: Always state that for integers a and b (b > 0), there exist unique integers q and r such that a = bq + r with 0 ≤ r < b.

2. **Euclidean Algorithm steps**: When solving gcd problems in exams, show each step clearly—write out the division equation at each iteration.

3. **Coprime check**: If gcd(a, b) = 1, then a and b are coprime. This is often used to prove certain properties in number theory problems.

4. **Extended Euclidean Algorithm**: For exam questions requiring Bézout's identity, always work backwards from the second-to-last equation in the Euclidean algorithm.

5. **Properties of primes**: Remember that 1 is not prime (it's neither prime nor composite), and 2 is the only even prime.

6. **Fundamental Theorem of Arithmetic**: This theorem guarantees unique factorization—use it when proving that certain numbers are prime or when simplifying expressions.

7. **Applications**: Understand practical applications like why RSA uses large primes—this helps in conceptual understanding beyond rote memorization.

8. **Time complexity**: Remember that the Euclidean algorithm is O(log n), making it efficient for large inputs—this distinguishes it from naive approaches.