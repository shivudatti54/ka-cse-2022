# Number Theory for Cryptography - Summary

## Key Definitions and Concepts
- **Modular Arithmetic**: Arithmetic system for integers where numbers wrap around after reaching modulus
- **Primitive Root**: Integer g where every number coprime to n is congruent to power of g mod n
- **Smooth Number**: Integer whose prime factors are all ≤ specified bound (crucial in factoring algorithms)
- **Tate Pairing**: Bilinear map on elliptic curves used in identity-based encryption

## Important Formulas and Theorems
- **Fermat's Little Theorem**: a^(p-1) ≡ 1 mod p (p prime, a ≠ 0 mod p)
- **Euler's Totient Function**: φ(n) = nΠ(1-1/p_i) for prime factors p_i of n
- **Bezout's Identity**: ∃x,y∈ℤ s.t. ax + by = gcd(a,b)
- **RSA Encryption**: C ≡ M^e mod n, Decryption: M ≡ C^d mod n where ed ≡ 1 mod φ(n)
- **Hasse's Theorem**: |E(F_q)| ∈ [q+1-2√q, q+1+2√q] (bounds EC points)

## Key Points
- Modular exponentiation enables efficient computation of large powers
- Difficulty of integer factorization protects RSA cryptosystems
- Discrete logarithm hardness varies by mathematical structure (multiplicative groups vs EC)
- Chinese Remainder Theorem accelerates RSA decryption by factor of 4
- Quantum computers threaten DLP/FACT-based systems but not lattice-based alternatives
- Pairing-based cryptography enables novel protocols like short signatures
- Smooth numbers are crucial in index calculus attacks on DLP

## Common Mistakes to Avoid
- Assuming all elements have inverses in modular arithmetic (only coprime elements do)
- Confusing φ(n) for prime powers: φ(p^k) = p^k - p^(k-1)
- Misapplying CRT to non-coprime moduli systems
- Neglecting proper randomness in prime generation for RSA

## Revision Tips
- Create flashcards for theorems with their cryptographic applications
- Practice solving congruence equations with composite moduli
- Implement RSA from scratch in Python (using large primes)
- Study NIST post-quantum standardization process for current research context
- Solve past DU papers focusing on computational number theory problems

Length: 400-800 words