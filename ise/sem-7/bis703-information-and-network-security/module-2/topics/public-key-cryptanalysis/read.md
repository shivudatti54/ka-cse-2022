# Public Key Cryptanalysis


## Table of Contents

- [Public Key Cryptanalysis](#public-key-cryptanalysis)
- [Introduction](#introduction)
- [Categories of Public Key Attacks](#categories-of-public-key-attacks)
  - [1. Brute Force Attack](#1-brute-force-attack)
  - [2. Mathematical Attacks](#2-mathematical-attacks)
  - [3. Timing Attacks (Side-Channel Attacks)](#3-timing-attacks-side-channel-attacks)
  - [4. Chosen Ciphertext Attack (CCA)](#4-chosen-ciphertext-attack-cca)
  - [5. Man-in-the-Middle (MITM) Attack](#5-man-in-the-middle-mitm-attack)
  - [6. Common Modulus Attack](#6-common-modulus-attack)
  - [7. Low Private Exponent Attack (Wiener's Attack)](#7-low-private-exponent-attack-wieners-attack)
- [Comparison of Attack Methods](#comparison-of-attack-methods)
- [Practical Implications](#practical-implications)
  - [What This Means for System Security](#what-this-means-for-system-security)
  - [Evolution of Recommended Key Sizes](#evolution-of-recommended-key-sizes)
- [Quantum Computing Threat](#quantum-computing-threat)
- [Summary](#summary)

## Introduction

Cryptanalysis is the science of breaking cryptographic systems without having direct access to the secret key. While public key cryptosystems like RSA have revolutionized secure communication, they are not immune to attack. Understanding cryptanalytic techniques is crucial for both attacking weak systems and defending strong ones.

Public key cryptanalysis differs from symmetric key cryptanalysis due to the availability of the public key—attackers have additional information to exploit.

## Categories of Public Key Attacks

Public key cryptanalysis can be broadly categorized into several attack types:

### 1. Brute Force Attack

**Description**: Systematically trying all possible private keys until the correct one is found.

**Feasibility**:

- For RSA with 512-bit keys: Feasible (broken in 1999)
- For RSA with 768-bit keys: Broken in 2009
- For RSA with 1024-bit keys: Marginal security
- For RSA with 2048-bit keys: Currently secure (would take millions of years with current technology)
- For RSA with 4096-bit keys: Secure for long-term use

**Defense**: Use sufficiently large key sizes (minimum 2048 bits for RSA, preferably 4096 bits for sensitive long-term data).

**Complexity**: O(2^(n/2)) for n-bit keys due to birthday paradox considerations.

### 2. Mathematical Attacks

These exploit the mathematical structure of the algorithm rather than trying all keys.

#### A. Integer Factorization (RSA-Specific)

**Target**: Factor n = p × q to discover the private key

**Methods**:

- **Trial Division**: Test all primes up to √n (inefficient for large n)
- **Pollard's Rho Algorithm**: More efficient than trial division
- **Quadratic Sieve**: Practical for numbers up to 100 digits
- **General Number Field Sieve (GNFS)**: Currently most efficient for large numbers
  - Used to factor 768-bit RSA in 2009 (2 years of computing)
  - Theoretical complexity: sub-exponential but super-polynomial

**Current Records**:

- 829-bit (250 digits) RSA modulus factored in 2020
- 1024-bit keys considered at risk
- 2048-bit keys still secure

**Defense**: Use larger keys; transition to 2048+ bits

#### B. Discrete Logarithm Problem

**Relevance**: Attacks Diffie-Hellman, ElGamal, DSA, and Elliptic Curve systems

**Problem**: Given g^x mod p, find x

**Methods**:

- **Baby-step Giant-step**: Time and space complexity O(√p)
- **Pollard's Rho for Logarithms**: Similar to integer factorization version
- **Index Calculus**: Most efficient for finite field discrete logarithms

**Impact**: Breaking discrete logarithm breaks key exchange and signature schemes

#### C. Small Exponent Attack (RSA)

**Scenario**: When public exponent e is very small (e.g., e = 3)

**Attack**: If the same message is encrypted to three different recipients with e = 3, an attacker can use the Chinese Remainder Theorem to recover the plaintext without factoring n.

**Defense**:

- Use proper padding (OAEP)
- Use larger e values (e.g., 65537)
- Never send identical messages to multiple recipients without padding

### 3. Timing Attacks (Side-Channel Attacks)

**Description**: Measure the time taken to perform cryptographic operations to deduce information about the private key.

**How It Works**:

- RSA decryption time varies slightly based on the values of the private key bits
- By measuring thousands/millions of decryption times, attackers can statistically determine the private key
- First demonstrated by Paul Kocher in 1996

**Example**:

- If a particular bit in the private key is 1, a multiplication occurs (takes longer)
- If the bit is 0, only squaring occurs (faster)
- Attackers measure these differences to extract the key bit by bit

**Defense**:

- **Constant-time implementations**: Ensure operations take the same time regardless of key values
- **Blinding**: Add random values before decryption, remove after
- **Timing noise**: Add random delays

### 4. Chosen Ciphertext Attack (CCA)

**Description**: Attacker can choose ciphertexts and obtain their decryptions, then use this information to break the system.

**Against RSA**:

- **Attack scenario**: Attacker wants to decrypt ciphertext C
- Attacker chooses random r, computes C' = C × r^e mod n
- Tricks the system into decrypting C', getting M' = M × r mod n
- Divides by r to recover M

**Types**:

- **CCA1 (Lunchtime attack)**: Attacker gets access to decryption oracle before receiving challenge ciphertext
- **CCA2 (Adaptive)**: Attacker can query decryption oracle even after receiving challenge ciphertext (except for the challenge itself)

**Defense**:

- Use proper padding schemes (OAEP for encryption, PSS for signatures)
- These schemes make the ciphertext non-malleable
- Never implement "raw RSA"

### 5. Man-in-the-Middle (MITM) Attack

**Description**: Attacker intercepts communication and impersonates both parties

**Scenario**:

1. Alice wants to communicate with Bob
2. Attacker intercepts Alice's request for Bob's public key
3. Attacker sends their own public key to Alice (pretending to be Bob)
4. Attacker intercepts messages from Alice, decrypts with their private key, re-encrypts with Bob's real public key, and forwards to Bob

**Defense**:

- **Public Key Infrastructure (PKI)**: Use certificates signed by trusted Certificate Authorities
- **Certificate pinning**: Pre-configure trusted public keys
- **Web of Trust**: PGP model where users sign each other's keys

### 6. Common Modulus Attack

**Scenario**: Two users share the same modulus n but have different public/private key pairs (e₁, d₁) and (e₂, d₂)

**Attack**: If GCD(e₁, e₂) = 1, anyone can decrypt messages without knowing either private key

**Defense**: Never reuse modulus n between different users

### 7. Low Private Exponent Attack (Wiener's Attack)

**Scenario**: When private exponent d is chosen to be small for computational efficiency

**Attack**: If d < n^0.25, Wiener's attack can efficiently recover d using continued fractions

**Defense**: Ensure d is sufficiently large (at least half the size of n in bits)

## Comparison of Attack Methods

| Attack Type          | Target         | Complexity      | Current Status            | Defense                   |
| -------------------- | -------------- | --------------- | ------------------------- | ------------------------- |
| Brute Force          | All systems    | O(2^n)          | Infeasible for 2048+ bits | Large keys                |
| Factorization (GNFS) | RSA            | Sub-exponential | 829 bits broken           | 2048+ bit keys            |
| Discrete Log         | DH, DSA, ECC   | Sub-exponential | ~768 bits broken          | 2048+ bits or 256-bit ECC |
| Timing Attack        | Implementation | Polynomial      | Practical                 | Constant-time code        |
| CCA                  | Raw RSA        | Polynomial      | Practical                 | Padding (OAEP/PSS)        |
| MITM                 | Key exchange   | N/A             | Practical                 | PKI, certificates         |

## Practical Implications

### What This Means for System Security

1. **Key Sizes Matter**: Use minimum 2048-bit RSA or 256-bit ECC
2. **Padding is Essential**: Never use raw RSA; always use OAEP/PSS
3. **Implementation Security**: Protect against timing attacks with constant-time code
4. **Certificate Validation**: Always verify certificates to prevent MITM
5. **Regular Updates**: Migrate to stronger algorithms as attacks improve

### Evolution of Recommended Key Sizes

| Year  | RSA Minimum | RSA Recommended | ECC Equivalent |
| ----- | ----------- | --------------- | -------------- |
| 2000  | 1024 bits   | 2048 bits       | 160 bits       |
| 2010  | 2048 bits   | 2048 bits       | 224 bits       |
| 2020+ | 2048 bits   | 3072-4096 bits  | 256-384 bits   |

## Quantum Computing Threat

**Shor's Algorithm (1994)**: A quantum algorithm that can factor integers and solve discrete logarithms in polynomial time.

**Impact**:

- Would break RSA, DSA, Diffie-Hellman, and ECC
- Requires large-scale quantum computers (not yet available)
- Estimated time to break 2048-bit RSA: hours on a sufficiently large quantum computer

**Post-Quantum Cryptography**:

- NIST is standardizing quantum-resistant algorithms
- Lattice-based, code-based, and hash-based cryptography
- Migration should begin now for long-term security

## Summary

- Public key cryptanalysis exploits mathematical weaknesses, implementation flaws, or protocol vulnerabilities
- Brute force attacks are infeasible for properly sized keys (2048+ bits for RSA)
- Mathematical attacks (factorization, discrete log) improve over time; key sizes must increase
- Timing attacks exploit implementation details; constant-time code is essential
- Chosen ciphertext attacks break raw RSA; proper padding (OAEP) is mandatory
- MITM attacks break key exchange; PKI and certificates provide defense
- Quantum computing poses a future threat; post-quantum cryptography is under development
- Defense in depth: use large keys, proper padding, secure implementations, and certificate validation
