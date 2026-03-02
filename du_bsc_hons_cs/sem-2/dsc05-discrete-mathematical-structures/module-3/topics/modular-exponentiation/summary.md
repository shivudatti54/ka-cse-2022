# Modular Exponentiation - Summary

## Key Definitions and Concepts
- **Modular Exponentiation**: Computing a^b mod n, the remainder when a^b is divided by n
- **Congruence**: a ≡ b (mod n) means n divides (a - b)
- **Euler's Totient Function φ(n)**: Count of integers coprime to n in [1, n]
- **Modular Inverse**: Integer x such that ax ≡ 1 (mod n), exists iff gcd(a, n) = 1

## Important Formulas and Theorems
- **Modular Properties**: (a × b) mod n = ((a mod n) × (b mod n)) mod n
- **Fermat's Little Theorem**: If p is prime and gcd(a, p) = 1, then a^(p-1) ≡ 1 (mod p)
- **Euler's Theorem**: If gcd(a, n) = 1, then a^φ(n) ≡ 1 (mod n)
- **RSA Key Generation**: n = p × q, φ(n) = (p-1)(q-1), d × e ≡ 1 (mod φ(n))

## Key Points
- Always reduce the base modulo n first to keep computations manageable
- Repeated squaring reduces complexity from O(b) to O(log b)
- For prime modulus p: reduce exponent modulo (p-1) using Fermat's theorem
- For composite modulus n: reduce exponent modulo φ(n) using Euler's theorem
- Modular inverse exists only when gcd(a, n) = 1
- Extended Euclidean Algorithm finds modular inverses efficiently
- RSA encryption: C = M^e mod n, decryption: M = C^d mod n

## Common Mistakes to Not Avoid
- Forgetting to check gcd(a, n) = 1 before claiming inverse exists
- Using Fermat's theorem when modulus is not prime
- Confusing congruence notation (=) with equality (=)
- Not reducing the exponent properly when applying theorems

## Revision Tips
- Practice 5-10 problems using repeated squaring method
- Memorize the conditions for Fermat and Euler's theorems
- Practice finding modular inverses with the Extended Euclidean Algorithm
- Understand the complete RSA encryption/decryption process
- Solve previous year DU exam questions on this topic