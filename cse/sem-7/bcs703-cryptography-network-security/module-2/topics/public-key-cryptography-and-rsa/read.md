# Public Key Cryptography and RSA

## 1. Introduction and Historical Context

Public key cryptography, also known as asymmetric cryptography, represents a fundamental paradigm shift in secure communication. Unlike symmetric cryptography, which relies on a single shared secret key, asymmetric cryptography employs a mathematically related pair of keys: a public key for encryption and signature verification, and a private key for decryption and signing. This revolutionary approach was conceptualized by Whitfield Diffie and Martin Hellman in their seminal 1976 paper "New Directions in Cryptography," addressing the inherent key distribution problem in symmetric systems.

The RSA algorithm, developed by Ronald Rivest, Adi Shamir, and Leonard Adleman at MIT in 1977, became the first practical implementation of public key cryptography. It remains one of the most widely used cryptosystems today, underpinning security in web browsers, email systems, and numerous communication protocols.

## 2. Fundamental Principles

### 2.1 The Key Distribution Problem

Traditional symmetric cryptography faces a fundamental challenge: the key distribution problem. Before secure communication can begin, both parties must possess the same secret key. This creates a circular dependency—how do parties securely exchange a key when they have no pre-shared secret? Public key cryptography resolves this elegantly:

1. Bob generates a public-private key pair (d, n) and (e, n)
2. Bob publishes his public key (e, n) openly
3. Alice encrypts her message M using Bob's public key: C = M^e mod n
4. Bob decrypts using his private key: M = C^d mod n

No pre-shared secret is required.

### 2.2 One-Way Functions with Trapdoors

Public key cryptography relies on mathematical functions that are easy to compute in one direction but computationally infeasible to reverse without special knowledge (the trapdoor):

- **One-way function**: Given x, easy to compute f(x); given f(x), computationally infeasible to determine x
- **Trapdoor**: Secret information that makes reverse computation tractable

For RSA, the one-way function is based on the integer factorization problem—multiplying two large primes is computationally easy, but recovering the primes from their product is believed to be hard.

## 3. RSA Algorithm: Mathematical Foundation

### 3.1 Key Generation

**Step 1**: Select two large prime numbers p and q. For security, each prime should be randomly chosen and typically be 1024-2048 bits in length. The primes should be of similar magnitude but not too close together.

**Step 2**: Compute the modulus n = p × q. This becomes part of both the public and private keys. The bit length of n determines the security level.

**Step 3**: Compute Euler's totient function φ(n) = (p-1)(q-1). This counts the number of integers in {1, 2, ..., n-1} that are coprime to n.

**Step 4**: Choose the public exponent e such that:

- 1 < e < φ(n)
- gcd(e, φ(n)) = 1 (e and φ(n) are coprime)

Commonly used values are e = 65537 (2^16 + 1) for efficiency, or e = 3 for faster encryption. However, very small values require proper padding to prevent attacks.

**Step 5**: Compute the private exponent d, the modular multiplicative inverse of e modulo φ(n):

```
d ≡ e^(-1) (mod φ(n))
```

This satisfies: d × e ≡ 1 (mod φ(n)), or equivalently, d × e = 1 + k × φ(n) for some integer k.

**Result**:

- Public Key: (e, n)
- Private Key: (d, n)

### 3.2 Encryption and Decryption

**Encryption** (given plaintext M, where 0 ≤ M < n):

```
C = M^e mod n
```

**Decryption** (given ciphertext C):

```
M = C^d mod n
```

## 4. Proof of Correctness

The correctness of RSA rests on Euler's theorem and properties of the totient function.

### 4.1 Euler's Theorem

**Theorem**: If gcd(a, n) = 1, then a^φ(n) ≡ 1 (mod n).

**Proof**: Consider the set of integers relatively prime to n: S = {x₁, x₂, ..., x*φ(n)}. Multiply each element by a (where gcd(a, n) = 1) to form aS = {ax₁, ax₂, ..., ax*φ(n)}. Since multiplication by a permutes S modulo n (a has a multiplicative inverse modulo n), the product of all elements in aS equals the product of all elements in S modulo n:

∏(ax_i) ≡ ∏(x_i) (mod n)

a^φ(n) × ∏(x_i) ≡ ∏(x_i) (mod n)

Since ∏(x_i) is invertible modulo n, we obtain a^φ(n) ≡ 1 (mod n). ∎

### 4.2 RSA Correctness Proof

**Theorem**: For any plaintext M where 0 ≤ M < n and gcd(M, n) = 1, decryption recovers the original message: (M^e)^d ≡ M (mod n).

**Proof**: Since d × e ≡ 1 (mod φ(n)), we can write:
d × e = 1 + k × φ(n) for some integer k.

Now consider:
(M^e)^d = M^(e×d) = M^(1 + k×φ(n)) = M × (M^φ(n))^k

By Euler's theorem, M^φ(n) ≡ 1 (mod n), assuming gcd(M, n) = 1:
M × (M^φ(n))^k ≡ M × 1^k ≡ M (mod n)

Therefore, decryption correctly recovers M. ∎

**Note**: When gcd(M, n) ≠ 1 (i.e., M is a multiple of p or q), the theorem still holds with minor modifications, as M^e^d ≡ M (mod n) can be proven using the Chinese Remainder Theorem.

## 5. Numerical Worked Example

**Key Generation with small primes:**

1. p = 61, q = 53
2. n = 61 × 53 = 3233
3. φ(n) = 60 × 52 = 3120
4. Choose e = 17 (gcd(17, 3120) = 1)
5. Find d: solve d × 17 ≡ 1 (mod 3120)
   Using extended Euclidean algorithm: d = 2753

Public Key: (e=17, n=3233)
Private Key: (d=2753, n=3233)

**Encryption:**

- Plaintext M = 65 (representing 'A' in ASCII)
- Ciphertext C = 65^17 mod 3233 = 2790

**Decryption:**

- M = 2790^2753 mod 3233 = 65 ✓

## 6. Digital Signatures with RSA

RSA provides authentication and non-repudiation through digital signatures:

**Signing:**

1. Compute hash: H = Hash(M)
2. Sign: S = H^d mod n

**Verification:**

1. Recover hash: H' = S^e mod n
2. Compute H = Hash(M)
3. Verify: if H' = H, signature is valid

This proves the message originated from the private key holder and was not modified.

## 7. Security Considerations

### 7.1 Security Assumption

RSA security relies on the **integer factorization problem**: given n = p × q, computing p and q is computationally infeasible for sufficiently large n. No polynomial-time algorithm is known for general integer factorization, though this remains an unproven assumption.

### 7.2 Complexity Analysis

- **Key Generation**: O(n²) for naive primality testing; O(n log n) with Miller-Rabin
- **Encryption/Decryption**: O(n³) for naive modular exponentiation; O(n² log n) with square-and-multiply
- **Using Chinese Remainder Theorem (CRT)**: Decryption can be accelerated by a factor of 4 by computing modulo p and q separately

### 7.3 Attack Vectors

**1. Integer Factorization Attacks:**

- Trial division: O(√n) - exponential in key size
- Quadratic Sieve: Sub-exponential complexity
- General Number Field Sieve: Currently fastest for large keys
- 512-bit keys have been factored; 1024-bit keys are considered marginally secure

**2. Small Exponent Attacks:**

- When e = 3, certain padding vulnerabilities exist
- Hastad's broadcast attack: If same message sent to multiple recipients with e=3, can be recovered

**3. Timing Attacks:**

- Measure execution time of decryption operation
- Can leak information about private exponent d
- Mitigation: constant-time operations, RSA with random padding

**4. Chosen Ciphertext Attacks (CCA):**

- Without proper padding, attacker can transform ciphertexts
- Adaptively chosen ciphertext attack (CCA2) particularly dangerous

### 7.4 Padding Schemes

Raw RSA is vulnerable to various attacks; padding is essential:

**OAEP (Optimal Asymmetric Encryption Padding):**

- Adds randomness and redundancy
- Transforms plaintext before encryption
- Provides semantic security (indistinguishability under chosen plaintext attack)

**PSS (Probabilistic Signature Scheme):**

- Adds salt for signature randomization
- Provides provable security properties
- Recommended for digital signatures

**PKCS#1 v1.5**: Legacy padding for encryption; vulnerable to Bleichenbacher's attack

## 8. Comparative Analysis

| Property            | RSA (Asymmetric)                | AES (Symmetric)         |
| ------------------- | ------------------------------- | ----------------------- |
| Key Type            | Public/Private pair             | Single shared key       |
| Key Distribution    | Easy (public key shared openly) | Requires secure channel |
| Computational Speed | Slow (100-1000× slower)         | Very fast               |
| Key Size            | 2048-4096 bits                  | 128-256 bits            |
| Primary Use         | Key exchange, authentication    | Bulk data encryption    |

## 9. Hybrid Cryptosystems

Due to RSA's computational overhead, practical systems employ hybrid approaches:

1. Generate random symmetric session key K
2. Encrypt K with recipient's RSA public key: C_K = K^e mod n
3. Encrypt data with symmetric key: C_Data = E_K(Data)
4. Transmit (C_K, C_Data)
5. Recipient decrypts K using RSA private key, then decrypts data

This approach combines RSA's key distribution advantages with AES's efficiency.
