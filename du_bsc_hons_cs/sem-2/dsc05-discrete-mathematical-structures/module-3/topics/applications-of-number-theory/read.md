# Applications of Number Theory

## Introduction

Number theory, often described as the "queen of mathematics," has emerged as one of the most practically significant branches of mathematics in the modern digital age. While historically studied for its pure mathematical elegance and theoretical beauty, number theory now forms the cryptographic foundation that secures virtually every aspect of our digital lives. From online banking and e-commerce to secure messaging and digital signatures, the applications of number theory are ubiquitous in computer science and information technology.

In this topic, we explore how classical results in number theory—particularly those concerning prime numbers, modular arithmetic, and the Euclidean algorithm—are harnessed to solve real-world problems in cryptography, computer security, and algorithm design. For students of Computer Science at the University of Delhi, understanding these applications is essential, as they form the theoretical basis for many security protocols and systems encountered in professional practice. The elegance of number theory lies in how seemingly abstract mathematical results find profound practical utility in protecting information and enabling secure communication.

## Key Concepts

### 1. Modular Arithmetic in Cryptography

Modular arithmetic serves as the foundation of modern cryptographic systems. In modular arithmetic, we work with congruence relations where two integers are considered equivalent if they leave the same remainder when divided by a modulus n. This can be expressed as: a ≡ b (mod n) if n divides (a - b).

The security of many cryptographic systems relies on the computational difficulty of certain mathematical problems in modular arithmetic. For instance, while it is computationally easy to compute a^b mod n using fast exponentiation, the reverse operation—finding the discrete logarithm (finding b given a, b ≡ g^x mod n)—is believed to be computationally infeasible for large numbers. This asymmetry between computation and inversion forms the basis of cryptographic security.

### 2. The Euclidean Algorithm and Its Extensions

The Euclidean algorithm, dating back to ancient Greece, provides an efficient method for computing the greatest common divisor (GCD) of two integers. For integers a and b, gcd(a, b) can be computed using the recurrence gcd(a, b) = gcd(b, a mod b) until b becomes zero. The algorithm runs in O(log min(a, b)) time, making it extremely efficient.

The extended Euclidean algorithm goes further by computing integers x and y such that ax + by = gcd(a, b). This result is crucial in cryptography because it allows us to compute modular multiplicative inverses. If gcd(a, n) = 1, there exists an integer x such that ax ≡ 1 (mod n), and this x is the multiplicative inverse of a modulo n.

### 3. Euler's Theorem and Euler's Totient Function

Euler's totient function φ(n) counts the number of positive integers less than n that are relatively prime to n. For a prime number p, φ(p) = p - 1. For the product of two primes p and q, φ(pq) = (p-1)(q-1).

Euler's theorem states that if gcd(a, n) = 1, then a^φ(n) ≡ 1 (mod n). This theorem has profound implications in cryptography, particularly in the RSA algorithm, where the totient function is used to compute public and private keys.

### 4. Prime Numbers and Their Properties

Prime numbers are the building blocks of number theory. The Fundamental Theorem of Arithmetic states that every integer greater than 1 can be uniquely expressed as a product of prime numbers. In cryptography, large prime numbers are essential for key generation in public-key cryptosystems.

The difficulty of factoring large composite numbers into their prime factors (the integer factorization problem) provides the security basis for RSA encryption. While multiplying two large primes is computationally trivial, recovering the original primes from their product is believed to require superpolynomial time, making it computationally infeasible for sufficiently large keys.

### 5. Chinese Remainder Theorem

The Chinese Remainder Theorem (CRT) provides a method for solving systems of simultaneous congruences with pairwise coprime moduli. If we have congruences x ≡ a_i (mod n_i) for i = 1, 2, ..., k where all n_i are pairwise coprime, CRT guarantees a unique solution modulo N = n_1 × n_2 × ... × n_k.

In computer science, CRT finds applications in parallel computation, where a large computation can be decomposed into smaller independent computations modulo various moduli, and then combined using CRT. It also appears in hash functions and error-correcting codes.

### 6. Hash Functions and Number Theory

Cryptographic hash functions are one-way functions that map arbitrary-length inputs to fixed-length outputs. Number theory contributes to hash function design through modular arithmetic and prime field operations. Properties like collision resistance and pre-image resistance are analyzed using number-theoretic techniques.

## Examples

### Example 1: Computing Modular Multiplicative Inverse using Extended Euclidean Algorithm

**Problem:** Find the multiplicative inverse of 17 modulo 43, i.e., find x such that 17x ≡ 1 (mod 43).

**Solution:**

We need to solve 17x + 43y = 1 (since gcd(17, 43) = 1).

Using the extended Euclidean algorithm:

Step 1: 43 = 17 × 2 + 9
Step 2: 17 = 9 × 1 + 8
Step 3: 9 = 8 × 1 + 1
Step 4: 8 = 1 × 8 + 0

Now working backwards:
1 = 9 - 8 × 1
1 = 9 - (17 - 9 × 1) × 1 = 9 × 2 - 17
1 = (43 - 17 × 2) × 2 - 17 = 43 × 2 - 17 × 5

Thus, 17 × (-5) + 43 × 2 = 1

So, x = -5 ≡ 43 - 5 = 38 (mod 43)

Therefore, the multiplicative inverse of 17 modulo 43 is 38.

**Verification:** 17 × 38 = 646 = 43 × 15 + 1 ≡ 1 (mod 43) ✓

### Example 2: RSA Key Generation

**Problem:** Demonstrate RSA key generation with small primes p = 5 and q = 11.

**Solution:**

Step 1: Compute n = p × q = 5 × 11 = 55
Step 2: Compute φ(n) = (p-1)(q-1) = 4 × 10 = 40
Step 3: Choose public exponent e such that 1 < e < 40 and gcd(e, 40) = 1. Choose e = 7.
Step 4: Compute private exponent d such that ed ≡ 1 (mod 40).

Using extended Euclidean algorithm: 7d ≡ 1 (mod 40)

We find d = 23 (since 7 × 23 = 161 = 40 × 4 + 1)

Public key: (e, n) = (7, 55)
Private key: (d, n) = (23, 55)

**Encryption:** For message m = 13, compute c = m^e mod n = 13^7 mod 55
13^2 = 169 ≡ 4 (mod 55)
13^4 ≡ 4^2 = 16 (mod 55)
13^7 = 13^4 × 13^2 × 13 ≡ 16 × 4 × 13 = 832 ≡ 7 (mod 55)
So ciphertext c = 7.

**Decryption:** Compute m = c^d mod n = 7^23 mod 55
7^2 = 49 ≡ -6 (mod 55)
7^4 ≡ 36 (mod 55)
7^8 ≡ 36^2 = 1296 ≡ 41 (mod 55)
7^16 ≡ 41^2 = 1681 ≡ 6 (mod 55)
7^23 = 7^16 × 7^4 × 7^2 × 7 ≡ 6 × 36 × (-6) × 7 ≡ 6 × 36 × 1 ≡ 6 × 36 = 216 ≡ 41 (mod 55)

Wait, let me recalculate: 7^23 = 7^16 × 7^4 × 7^2 × 7^1
7^16 ≡ 6, 7^4 ≡ 36, 7^2 ≡ 49 ≡ -6, 7^1 ≡ 7
Product: 6 × 36 × (-6) × 7 = 6 × 36 × 1 × 7 (since -6 × 7 = -42 ≡ 13, no wait...)
6 × 36 = 216 ≡ 216 - 55 × 3 = 216 - 165 = 51
51 × (-6) = -306 ≡ 55 × (-6) + (-306 + 330) = 24
24 × 7 = 168 ≡ 168 - 55 × 3 = 168 - 165 = 3 ≠ 13

Let me compute more carefully: 7^23 mod 55 using repeated squaring:
7^1 = 7
7^2 = 49 ≡ -6
7^4 = (-6)^2 = 36
7^8 = 36^2 = 1296 ≡ 1296 - 55 × 23 = 1296 - 1265 = 31
7^16 = 31^2 = 961 ≡ 961 - 55 × 17 = 961 - 935 = 26

7^23 = 7^16 × 7^4 × 7^2 × 7 = 26 × 36 × 49 × 7
26 × 36 = 936 ≡ 936 - 55 × 17 = 936 - 935 = 1
1 × 49 × 7 = 343 ≡ 343 - 55 × 6 = 343 - 330 = 13 ✓

Message recovered: m = 13

### Example 3: Solving Simultaneous Congruences using Chinese Remainder Theorem

**Problem:** Find the smallest positive integer x such that:
x ≡ 2 (mod 3)
x ≡ 3 (mod 5)
x ≡ 2 (mod 7)

**Solution:**

Here, moduli are 3, 5, 7 (pairwise coprime), and N = 3 × 5 × 7 = 105

For each congruence, compute N_i = N/n_i and its inverse:

For n_1 = 3: N_1 = 105/3 = 35, find y_1 such that 35y_1 ≡ 1 (mod 3)
35 ≡ 2 (mod 3), so 2y_1 ≡ 1 ⇒ y_1 ≡ 2 (since 2 × 2 = 4 ≡ 1)

For n_2 = 5: N_2 = 105/5 = 21, find y_2 such that 21y_2 ≡ 1 (mod 3)
21 ≡ 1 (mod 5), so y_2 ≡ 1

For n_3 = 7: N_3 = 105/7 = 15, find y_3 such that 15y_3 ≡ 1 (mod 7)
15 ≡ 1 (mod 7), so y_3 ≡ 1

Now compute x = a_1N_1y_1 + a_2N_2y_2 + a_3N_3y_3 (mod N)
x = 2 × 35 × 2 + 3 × 21 × 1 + 2 × 15 × 1 = 140 + 63 + 30 = 233
x ≡ 233 mod 105 = 233 - 105 × 2 = 233 - 210 = 23

Therefore, x = 23 is the smallest positive solution.

## Exam Tips

1. **Memorize the key theorems:** Euler's theorem, Fermat's little theorem, and Chinese Remainder Theorem are frequently tested. Know their statements and conditions for applicability.

2. **Practice the extended Euclidean algorithm:** This is essential for computing modular multiplicative inverses, a skill tested in almost every examination.

3. **Understand RSA thoroughly:** Be able to explain key generation, encryption, and decryption processes. Know why the algorithm works based on number theory.

4. **Know the conditions for inverses to exist:** A modular multiplicative inverse of a modulo n exists if and only if gcd(a, n) = 1.

5. **CRT applications:** Be prepared to solve simultaneous congruences and understand the uniqueness condition (pairwise coprime moduli).

6. **Time complexity matters:** Know that Euclidean algorithm runs in O(log n) time, making it efficient for large numbers used in cryptography.

7. **Security assumptions:** Understand that RSA security relies on the difficulty of integer factorization, and this is an assumption, not a proven result.