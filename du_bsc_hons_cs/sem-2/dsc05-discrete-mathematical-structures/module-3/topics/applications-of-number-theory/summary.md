# Applications of Number Theory - Summary

## Key Definitions and Concepts

- **Modular Arithmetic:** a ≡ b (mod n) means n divides (a - b), forming the foundation of cryptographic operations.

- **Greatest Common Divisor (GCD):** The largest positive integer dividing both numbers; gcd(a, b) = 1 indicates a and b are coprime.

- **Modular Multiplicative Inverse:** Integer x such that ax ≡ 1 (mod n), existing only when gcd(a, n) = 1.

- **Euler's Totient Function φ(n):** Counts integers ≤ n that are coprime to n; for prime p, φ(p) = p - 1.

- **Chinese Remainder Theorem:** Provides unique solution modulo N for simultaneous congruences with pairwise coprime moduli.

## Important Formulas and Theorems

- **Extended Euclidean Algorithm:** Finds integers x, y such that ax + by = gcd(a, b)

- **Euler's Theorem:** a^φ(n) ≡ 1 (mod n) when gcd(a, n) = 1

- **Fermat's Little Theorem:** a^(p-1) ≡ 1 (mod p) for prime p when p ∤ a

- **RSA Key Generation:** n = pq, φ(n) = (p-1)(q-1), choose e, compute d such that ed ≡ 1 (mod φ(n))

## Key Points

- Number theory provides the mathematical foundation for modern cryptography and computer security.

- The integer factorization problem (factoring large composites) and discrete logarithm problem form the basis of cryptographic security assumptions.

- The Euclidean algorithm is highly efficient with O(log n) time complexity, suitable for large cryptographic keys.

- RSA security relies on the computational difficulty of reversing the multiplication of two large primes.

- Chinese Remainder Theorem enables parallel computation and efficient processing in modular systems.

- For RSA with primes p and q, knowing φ(n) allows computation of private key from public key, emphasizing need to protect prime factors.

## Common Mistakes to Avoid

- Forgetting to check gcd(a, n) = 1 before claiming modular inverse exists.

- Using non-coprime moduli in Chinese Remainder Theorem applications.

- Confusing Euler's totient function φ(n) with other counting functions.

- Incorrectly applying modular exponentiation without using proper reduction at each step.

## Revision Tips

- Practice the extended Euclidean algorithm until it becomes automatic—it's tested frequently.

- Work through RSA with different small prime pairs to understand the complete process.

- Solve at least 3-4 CRT problems to gain confidence in handling simultaneous congruations.

- Remember that cryptographic security is based on computational assumptions, not mathematical proofs.