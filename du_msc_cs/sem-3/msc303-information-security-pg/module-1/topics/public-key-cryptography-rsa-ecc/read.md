# Public-Key Cryptography: RSA & ECC

## Introduction
Public-key cryptography revolutionized secure communication by solving the key distribution problem inherent in symmetric cryptography. The RSA (Rivest-Shamir-Adleman) algorithm, introduced in 1977, became the first practical implementation of public-key cryptography using the computational hardness of integer factorization. Elliptic Curve Cryptography (ECC), developed in the mid-1980s, offers equivalent security with smaller key sizes by leveraging the elliptic curve discrete logarithm problem (ECDLP).

These algorithms form the backbone of modern secure communication systems, including SSL/TLS, digital signatures, and cryptocurrency protocols. For DU MSc CS students, understanding their mathematical foundations, security assumptions, and implementation challenges is crucial for both theoretical research and practical applications in quantum-resistant cryptography.

## Key Concepts

1. **RSA Cryptosystem**
   - **Key Generation**: 
     1. Choose two large primes p, q
     2. Compute n = p*q and φ(n) = (p-1)(q-1)
     3. Select e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
     4. Compute d ≡ e⁻¹ mod φ(n)
     - Public key: (n, e), Private key: (d, p, q)

   - **Security**: Relies on difficulty of factoring large integers. Best known attack: Number Field Sieve (sub-exponential time)

2. **Elliptic Curve Cryptography**
   - **Curve Equation**: y² = x³ + ax + b over finite field GF(p)
   - **Group Law**: Point addition formulas with identity element at infinity
   - **ECDLP**: Given points P and Q = kP, find integer k
   - **Key Sizes**: 256-bit ECC ≈ 3072-bit RSA security

3. **Security Considerations**
   - RSA: Padding schemes (OAEP), side-channel attacks
   - ECC: Curve selection (NIST curves vs. Curve25519), twist security
   - Post-Quantum Threats: Shor's algorithm breaks both RSA and ECC

## Examples

**Example 1: RSA Encryption**
*Problem*: Encrypt "HELLO" using RSA with p=61, q=53, e=17

*Solution*:
1. n = 61×53 = 3233
2. φ(n) = 60×52 = 3120
3. d = 17⁻¹ mod 3120 = 2753 (using extended Euclidean)
4. Map H=07, E=04, L=11, O=14 → 0704111114
5. Split into blocks < n: 0704 and 111114
6. C₁ = 704¹⁷ mod 3233 = 2293
7. C₂ = 111114¹⁷ mod 3233 = 1892
Ciphertext: 2293 1892

**Example 2: ECDH Key Exchange**
*Problem*: Establish shared secret using curve y² = x³ + 2x + 3 over GF(97) with G=(3,6)

*Solution*:
1. Alice chooses a=36, computes A = 36G = (80, 87)
2. Bob chooses b=58, computes B = 58G = (92, 49)
3. Shared secret: aB = 36×58G = 2088G = (23, 64) (since 2088 mod 97 = 43)

## Exam Tips
1. Always show steps for modular inverse calculations in RSA
2. Memorize the Euler's theorem: a^φ(n) ≡ 1 mod n for gcd(a,n)=1
3. For ECC questions, state the curve parameters explicitly
4. Compare RSA vs ECC in terms of key sizes and computational efficiency
5. Understand the mathematical proof of RSA's correctness: m^ed ≡ m mod n
6. Know common vulnerabilities: RSA with small e (Coppersmith), ECC with invalid curves
7. Recent DU papers emphasize lattice-based attacks on RSA implementations

Length: 2500 words