# Number Theory for Cryptography

## Introduction
Number theory forms the mathematical backbone of modern cryptography. This branch of pure mathematics, once considered abstract and impractical, now underpins secure communication systems, digital signatures, and blockchain technologies. From RSA encryption to elliptic curve cryptography, number-theoretic concepts like prime factorization and modular arithmetic enable secure data transmission in adversarial environments.

The importance of number theory in cryptography stems from its computational asymmetry - problems that are easy to compute in one direction but computationally infeasible to reverse. For instance, multiplying two large primes is trivial, but factoring the product back into primes remains intractable for classical computers. This property enables public-key cryptosystems that secure internet communications, financial transactions, and government systems.

Recent advancements in quantum computing have intensified research in post-quantum cryptography, driving innovations in lattice-based cryptography and isogeny-based systems. Understanding foundational number theory is crucial for developing and analyzing next-generation cryptographic protocols resistant to quantum attacks.

## Key Concepts
1. **Modular Arithmetic**: 
   - Fundamental system for congruence relations: a ≡ b (mod n) iff n divides (a-b)
   - Enables cyclic structures essential in key exchange protocols
   - Multiplicative inverses exist iff gcd(a,n) = 1 (Bezout's identity)

2. **Euler's Theorem**:
   - a^φ(n) ≡ 1 mod n for a and n coprime
   - φ(n) (Euler's totient function) counts integers < n coprime to n
   - Generalizes Fermat's Little Theorem (when n is prime)

3. **Discrete Logarithm Problem (DLP)**:
   - Given g^x ≡ h mod p, find x
   - Basis of Diffie-Hellman key exchange and DSA
   - Quantum-vulnerable (Shor's algorithm)

4. **Chinese Remainder Theorem (CRT)**:
   - System of congruences with pairwise coprime moduli has unique solution mod product
   - Optimizes RSA decryption and signature schemes

5. **Elliptic Curve Cryptography (ECC)**:
   - Algebraic structure: y² = x³ + ax + b over finite field
   - EC-DLP considered harder than classical DLP
   - Enables shorter keys with equivalent security to RSA

## Examples

**Example 1: RSA Key Generation**
1. Choose primes p=61, q=53
2. Compute n=pq=3233
3. φ(n)=(61-1)(53-1)=3120
4. Select e=17 (coprime to 3120)
5. Find d ≡ e⁻¹ mod φ(n): 
   - Solve 17d ≡ 1 mod 3120 using Extended Euclidean Algorithm
   - d = 2753 (since 17*2753 = 46801 ≡ 1 mod 3120)
Public key: (3233,17), Private key: (3233,2753)

**Example 2: Solving Linear Congruence**
Solve 7x ≡ 3 mod 12
1. gcd(7,12)=1 → unique solution
2. Find inverse of 7 mod 12: 7*7 = 49 ≡ 1 mod 12
3. x ≡ 3*7⁻¹ ≡ 3*7 ≡ 21 ≡ 9 mod 12

**Example 3: Elliptic Curve Point Addition**
Given curve y² = x³ + 2x + 3 over F_7:
1. Points P=(3,1) and Q=(5,4)
2. Compute slope m = (y_Q - y_P)(x_Q - x_P)⁻¹ mod 7
   - m = (4-1)(5-3)⁻¹ = 3*2⁻¹ = 3*4 = 12 ≡ 5 mod 7
3. x_R = m² - x_P - x_Q = 25 -3 -5 = 17 ≡ 3 mod 7
4. y_R = m(x_P - x_R) - y_P = 5(3-3) -1 = -1 ≡ 6 mod 7
Resultant point: (3,6)

## Exam Tips
1. Memorize Euler's theorem and its relationship to Fermat's Little Theorem
2. Practice Extended Euclidean Algorithm for finding modular inverses
3. Understand CRT applications in optimizing cryptographic operations
4. Distinguish between computational hardness assumptions: FACT vs DLP vs ECDLP
5. Learn step-by-step RSA key generation and encryption/decryption
6. Study differences between classical DH and ECDH key exchange
7. Analyze time complexity of number-theoretic algorithms (e.g., Pollard's rho)

Length: 1500-3000 words, MSc CS (research-oriented) postgraduate level