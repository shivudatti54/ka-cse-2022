# Modular Exponentiation

## Introduction

Modular exponentiation is a fundamental operation in number theory and computer science that combines exponentiation with modular arithmetic. In essence, it computes the remainder when a base raised to an exponent is divided by a modulus. Formally, given integers a, b, and n (with n > 0), modular exponentiation finds the value of a^b mod n.

This operation forms the backbone of modern cryptographic systems, particularly in public-key cryptography. The RSA encryption algorithm, elliptic curve cryptography, and Diffie-Hellman key exchange all rely heavily on the computational difficulty of modular exponentiation for their security. Beyond cryptography, modular exponentiation appears in hash functions, digital signatures, and various algorithmic techniques like modular multiplicative inverse computation.

The mathematical foundation of modular exponentiation lies in Euler's theorem and Fermat's little theorem, which provide properties that make large-scale computations tractable while maintaining security guarantees. Understanding this topic is essential for any computer science student, as it bridges pure mathematics with practical applications in security and algorithm design.

## Key Concepts

### Basic Definition
For integers a, b, and n (with n > 0), modular exponentiation is defined as:
a^b mod n = remainder when a^b is divided by n

The result always lies in the range [0, n-1].

### Properties of Modular Arithmetic
1. **Modular Addition/Subtraction**: (a ± b) mod n = ((a mod n) ± (b mod n)) mod n
2. **Modular Multiplication**: (a × b) mod n = ((a mod n) × (b mod n)) mod n
3. **Modular Exponentiation**: a^b mod n = ((a mod n)^b) mod n

### Euler's Totient Function
The Euler's totient function φ(n) counts the number of positive integers less than n that are coprime to n. For a prime number p, φ(p) = p-1. For two primes p and q, φ(pq) = (p-1)(q-1).

### Euler's Theorem
If gcd(a, n) = 1, then a^φ(n) ≡ 1 (mod n)

This theorem is crucial because it allows reduction of large exponents modulo φ(n).

### Fermat's Little Theorem
If p is prime and gcd(a, p) = 1, then a^(p-1) ≡ 1 (mod p)

This is a special case of Euler's theorem when n is prime.

### Modular Multiplicative Inverse
The modular multiplicative inverse of a modulo n is an integer x such that ax ≡ 1 (mod n). It exists if and only if gcd(a, n) = 1. The inverse can be found using the Extended Euclidean Algorithm.

## Examples

### Example 1: Basic Modular Exponentiation
**Problem**: Compute 3^13 mod 7

**Solution using repeated squaring**:
- 3^1 mod 7 = 3
- 3^2 mod 7 = 9 mod 7 = 2
- 3^4 mod 7 = (3^2)^2 mod 7 = 2^2 mod 7 = 4
- 3^8 mod 7 = (3^4)^2 mod 7 = 4^2 mod 7 = 16 mod 7 = 2

Now express 13 = 8 + 4 + 1:
- 3^13 mod 7 = 3^(8+4+1) mod 7 = (3^8 × 3^4 × 3^1) mod 7
- = (2 × 4 × 3) mod 7 = 24 mod 7 = 3

**Answer: 3**

### Example 2: Using Fermat's Little Theorem
**Problem**: Compute 3^100 mod 11

**Solution**:
Since 11 is prime, by Fermat's Little Theorem: 3^10 ≡ 1 (mod 11)

Reduce the exponent: 100 = 10 × 10 + 0
So, 3^100 = (3^10)^10 ≡ 1^10 ≡ 1 (mod 11)

**Answer: 1**

### Example 3: Cryptographic Application
**Problem**: In RSA, if p = 5, q = 11, and e = 3, compute the encryption of message M = 2. (n = p × q = 55)

**Solution**:
RSA encryption: C ≡ M^e mod n
C ≡ 2^3 mod 55 = 8 mod 55 = 8

For decryption, we need d such that d × e ≡ 1 (mod φ(n))
φ(55) = φ(5) × φ(11) = 4 × 10 = 40
Find d: 3d ≡ 1 (mod 40)
3d = 40k + 1, trying k = 2: 3d = 81, d = 27

Decryption: M ≡ C^d mod n = 8^27 mod 55
Using modular exponentiation: 8^27 mod 55 = 2

**Verification: The decrypted message equals the original message 2.**

### Example 4: Finding Modular Inverse
**Problem**: Find the modular inverse of 17 modulo 43

**Solution**:
We need x such that 17x ≡ 1 (mod 43)

Using Extended Euclidean Algorithm:
43 = 2 × 17 + 9
17 = 1 × 9 + 8
9 = 1 × 8 + 1
8 = 8 × 1 + 0

Back-substituting:
1 = 9 - 1 × 8
1 = 9 - 1 × (17 - 1 × 9) = 2 × 9 - 1 × 17
1 = 2 × (43 - 2 × 17) - 1 × 17 = 2 × 43 - 5 × 17

So, -5 × 17 ≡ 1 (mod 43)
17 × (-5) ≡ 1 (mod 43)
17 × 38 ≡ 1 (mod 43) since -5 ≡ 38 (mod 43)

**The modular inverse is 38.**

## Exam Tips

1. **Always reduce the base modulo n first**: Before computing a^b mod n, reduce a modulo n to keep numbers small. This follows directly from the property (a mod n)^b mod n.

2. **Use repeated squaring for large exponents**: Instead of computing a^b directly, decompose b into powers of 2. This reduces time complexity from O(b) to O(log b).

3. **Apply Fermat's Little Theorem for prime moduli**: When the modulus is prime and the base is coprime to it, reduce the exponent modulo (p-1).

4. **Remember Euler's theorem for composite moduli**: For gcd(a, n) = 1, reduce exponents modulo φ(n). This is essential for RSA calculations.

5. **Verify inverse existence before computing**: The modular inverse exists only when gcd(a, n) = 1. Always check this first.

6. **Practice the Extended Euclidean Algorithm**: This is crucial for finding modular inverses and is a frequently tested concept in DU exams.

7. **Understand the connection to cryptography**: Be prepared to explain how modular exponentiation enables RSA and other cryptographic protocols.

8. **Watch for edge cases**: When b = 0, a^0 mod n = 1 (provided n > 1). Also note that 0^0 is undefined.

9. **Use proper notation**: Write a ≡ b (mod n) to denote congruence, not a = b mod n. This distinction matters in formal solutions.

10. **Double-check final answers**: The result of modular exponentiation must always be in the range [0, n-1].