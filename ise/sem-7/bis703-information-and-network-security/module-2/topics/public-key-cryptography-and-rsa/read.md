# Public Key Cryptography and RSA


## Table of Contents

- [Public Key Cryptography and RSA](#public-key-cryptography-and-rsa)
- [Introduction to Public Key Cryptography](#introduction-to-public-key-cryptography)
- [Historical Context](#historical-context)
- [Core Principles](#core-principles)
  - [The Key Distribution Problem (Solved)](#the-key-distribution-problem-solved)
  - [Mathematical Foundation](#mathematical-foundation)
- [The RSA Algorithm](#the-rsa-algorithm)
  - [Key Generation](#key-generation)
  - [RSA Encryption](#rsa-encryption)
  - [RSA Decryption](#rsa-decryption)
  - [Why It Works: Euler's Theorem](#why-it-works-eulers-theorem)
- [Numerical Example](#numerical-example)
- [RSA for Digital Signatures](#rsa-for-digital-signatures)
- [Security Considerations](#security-considerations)
  - [What Makes RSA Secure?](#what-makes-rsa-secure)
  - [Potential Vulnerabilities](#potential-vulnerabilities)
  - [Practical Implementations](#practical-implementations)
- [Applications of RSA](#applications-of-rsa)
- [RSA vs Symmetric Cryptography](#rsa-vs-symmetric-cryptography)
- [Hybrid Cryptosystems](#hybrid-cryptosystems)
- [Summary](#summary)

## Introduction to Public Key Cryptography

Public key cryptography (asymmetric cryptography) represents a revolutionary approach to encryption that solves the key distribution problem inherent in symmetric cryptography. Instead of using a single shared secret key, it employs a mathematically related pair of keys:

- **Public Key**: Used for encryption and signature verification. Can be freely distributed.
- **Private Key**: Used for decryption and signing. Must be kept absolutely secret.

The fundamental property: data encrypted with one key can only be decrypted with the other key in the pair.

## Historical Context

Public key cryptography was conceptualized by Whitfield Diffie and Martin Hellman in 1976, revolutionizing secure communication. The RSA algorithm, developed by Rivest, Shamir, and Adleman in 1977, was the first practical implementation and remains widely used today.

## Core Principles

### The Key Distribution Problem (Solved)

Traditional symmetric cryptography faces a chicken-and-egg problem: how do you securely share a secret key over an insecure channel? Public key cryptography solves this:

1. Bob generates a public-private key pair
2. Bob publishes his public key openly
3. Alice encrypts messages using Bob's public key
4. Only Bob can decrypt using his private key

No pre-shared secret needed!

### Mathematical Foundation

Public key cryptography relies on **one-way functions with trapdoors**:

- **One-way function**: Easy to compute forward, extremely hard to reverse
- **Trapdoor**: Secret information that makes reversal easy

For RSA, the one-way function is based on the difficulty of factoring large composite numbers into their prime factors.

## The RSA Algorithm

RSA is the most widely used public key cryptosystem. It can be used for both encryption and digital signatures.

### Key Generation

1. **Select two large prime numbers**: Choose random primes `p` and `q` (typically 1024+ bits each)
2. **Compute n**: Calculate `n = p × q` (this becomes the modulus, part of both keys)
3. **Compute φ(n)**: Calculate Euler's totient: `φ(n) = (p-1)(q-1)`
4. **Choose public exponent e**: Select `e` such that:
   - 1 < e < φ(n)
   - GCD(e, φ(n)) = 1 (e and φ(n) are coprime)
   - Common values: 3 or 65537 for efficiency
5. **Compute private exponent d**: Find `d` such that `(d × e) mod φ(n) = 1`
   - d is the modular multiplicative inverse of e

**Public Key**: (e, n)
**Private Key**: (d, n)

### RSA Encryption

To encrypt plaintext message M (where M < n):

**C = M^e mod n**

The ciphertext C can only be decrypted by the holder of the private key.

### RSA Decryption

To decrypt ciphertext C:

**M = C^d mod n**

This recovers the original plaintext.

### Why It Works: Euler's Theorem

The RSA algorithm works because of Euler's theorem:

- If M and n are coprime: M^φ(n) ≡ 1 (mod n)
- Since d×e ≡ 1 (mod φ(n)), we have d×e = 1 + k×φ(n) for some integer k
- Therefore: C^d = (M^e)^d = M^(ed) = M^(1+k×φ(n)) = M × (M^φ(n))^k ≡ M × 1^k ≡ M (mod n)

## Numerical Example

Let's walk through a small example (real RSA uses much larger numbers):

**Key Generation:**

1. p = 61, q = 53
2. n = 61 × 53 = 3233
3. φ(n) = 60 × 52 = 3120
4. Choose e = 17 (coprime to 3120)
5. Find d: (d × 17) mod 3120 = 1 → d = 2753

Public Key: (17, 3233)
Private Key: (2753, 3233)

**Encryption:**

- Plaintext M = 65 (ASCII 'A')
- C = 65^17 mod 3233 = 2790

**Decryption:**

- Ciphertext C = 2790
- M = 2790^2753 mod 3233 = 65 ✓

## RSA for Digital Signatures

RSA can be used in reverse for authentication and non-repudiation:

**Signing:**

1. Compute hash of message: H = Hash(M)
2. Sign with private key: S = H^d mod n

**Verification:**

1. Decrypt signature with public key: H' = S^e mod n
2. Compute hash of received message: H = Hash(M)
3. If H = H', signature is valid

This proves the message came from the holder of the private key and hasn't been altered.

## Security Considerations

### What Makes RSA Secure?

- **Integer Factorization Problem**: Given n = p×q, finding p and q is computationally infeasible for large numbers
- Current best algorithms require exponential time
- 2048-bit keys considered secure today; 4096-bit for long-term security

### Potential Vulnerabilities

1. **Small key sizes**: 512-bit keys can be factored; 1024-bit are marginal
2. **Small exponent attacks**: Very small e values can be vulnerable
3. **Timing attacks**: Measuring decryption time can leak information
4. **Chosen ciphertext attacks**: Requires proper padding schemes

### Practical Implementations

Real-world RSA uses padding schemes for security:

- **OAEP (Optimal Asymmetric Encryption Padding)**: For encryption
- **PSS (Probabilistic Signature Scheme)**: For signatures

These add randomness and prevent various attacks.

## Applications of RSA

1. **SSL/TLS**: Securing web traffic (HTTPS)
2. **Email encryption**: PGP, S/MIME
3. **Digital signatures**: Software signing, document authentication
4. **Key exchange**: Securely sharing symmetric keys
5. **VPNs**: Authenticating endpoints
6. **SSH**: Secure remote access

## RSA vs Symmetric Cryptography

| Feature          | RSA (Asymmetric)                       | AES (Symmetric)                     |
| ---------------- | -------------------------------------- | ----------------------------------- |
| Key Type         | Public/Private pair                    | Single shared key                   |
| Key Distribution | Easy (public key can be shared openly) | Difficult (requires secure channel) |
| Speed            | Slow (100-1000x slower)                | Very fast                           |
| Key Size         | 2048-4096 bits                         | 128-256 bits                        |
| Use Case         | Key exchange, signatures               | Bulk data encryption                |

## Hybrid Cryptosystems

Due to RSA's computational cost, most systems use a hybrid approach:

1. Use RSA to securely exchange a symmetric session key
2. Use that session key with AES to encrypt the actual data
3. Provides both security (from RSA) and efficiency (from AES)

This is how HTTPS works!

## Summary

- Public key cryptography uses mathematically related key pairs
- RSA security relies on the difficulty of factoring large numbers
- RSA solves the key distribution problem of symmetric cryptography
- The algorithm involves modular exponentiation with carefully chosen exponents
- RSA is used for both encryption/decryption and digital signatures
- Practical systems combine RSA (for key exchange) with symmetric ciphers (for data encryption)
- Modern implementations require proper padding and adequate key sizes (2048+ bits)
