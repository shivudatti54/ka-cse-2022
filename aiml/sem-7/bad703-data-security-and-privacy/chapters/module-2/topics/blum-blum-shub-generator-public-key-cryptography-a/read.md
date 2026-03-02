# Blum Blum Shub Generator & Public Key Cryptography with RSA

## Introduction

This module explores two fundamental pillars of modern cryptography: a robust method for generating cryptographically secure pseudo-random numbers and the revolutionary concept of asymmetric, or public-key, cryptography. We begin with the **Blum Blum Shub (BBS) Generator**, a cornerstone for creating unpredictable sequences crucial for keys and nonces. We then delve into **Public Key Cryptography**, culminating in a detailed examination of the **RSA algorithm**, one of the most widely used and important cryptographic systems in the world.

## 1. Blum Blum Shub (BBS) Generator

The BBS generator is a cryptographically secure pseudo-random number generator (CSPRNG) known for its strong security guarantees, based on the computational difficulty of the **integer factorization problem**.

### Core Concepts & Algorithm

1.  **Setup:** Choose two large prime numbers, `p` and `q`, that are both congruent to `3 mod 4` (`p ≡ 3 mod 4` and `q ≡ 3 mod 4`). These are called **Blum primes**.
2.  **Compute `n`:** Compute `n = p * q`. This value `n` is made public and is part of the generator's seed.
3.  **Select Seed:** Choose a random integer `s` (the seed) such that `1 < s < n` and `gcd(s, n) = 1` (i.e., `s` is coprime with `n`).
4.  **Generate Sequence:** The random bit sequence is generated iteratively:
    *   `X₀ = s² mod n`  (Initial state)
    *   For `i = 1, 2, 3, ...`:
        *   `Xᵢ = (Xᵢ₋₁)² mod n`
        *   `Bᵢ = Xᵢ mod 2`  (The output bit is the least significant bit of `Xᵢ`)

**Security:** The security of BBS is reducible to the difficulty of factoring `n`. Given `n`, predicting the next output bit is computationally infeasible without knowing the prime factors `p` and `q`. It is provably secure, meaning breaking it is as hard as solving a known hard problem (factoring).

## 2. Public Key Cryptography

Unlike symmetric key cryptography, which uses a single shared secret key, public key cryptography uses a pair of mathematically related keys:

*   **Public Key:** Used for **encryption** or **verifying a signature**. This key can be openly distributed to everyone.
*   **Private Key:** Used for **decryption** or **creating a digital signature**. This key is kept secret by the owner.

This solves the key distribution problem inherent in symmetric systems. If Alice wants to send a confidential message to Bob, she encrypts it with Bob's public key. Only Bob, possessing the corresponding private key, can decrypt it.

## 3. The RSA Algorithm

RSA (Rivest-Shamir-Adleman) is the first practical implementation of public-key cryptography, and its security also relies on the computational intractability of factoring large integers.

### Step-by-Step Operation

#### A. Key Generation
1.  **Choose two primes:** Select two large, distinct prime numbers, `p` and `q`.
2.  **Compute `n`:** Calculate the modulus `n = p * q`. The length of `n` in bits is the **key length** (e.g., 2048, 4096).
3.  **Compute Euler's Totient Function:** `φ(n) = (p-1)(q-1)`.
4.  **Choose public exponent `e`:** Select an integer `e` such that `1 < e < φ(n)` and `gcd(e, φ(n)) = 1`. Common choice is `65537`.
5.  **Compute private exponent `d`:** Calculate `d` as the modular multiplicative inverse of `e mod φ(n)`, i.e., `d ≡ e⁻¹ mod φ(n)`. This means `(d * e) mod φ(n) = 1`.
6.  **Keys:**
    *   **Public Key:** `(e, n)`
    *   **Private Key:** `(d, n)`

#### B. Encryption
To encrypt a plaintext message `M` (represented as an integer where `0 ≤ M < n`), compute the ciphertext `C`:
`C = Mᵉ mod n`

#### C. Decryption
To decrypt the ciphertext `C` using the private key, compute:
`M = Cᵈ mod n`

### Why it Works
Euler's theorem states that if `M` and `n` are coprime, `Mᵏᵐᵒᵈ ᵠ⁽ⁿ⁾ ≡ 1 mod n`. The math ensures that `(Mᵉ)ᵈ mod n = Mᵉᵈ mod n = M`, because `e*d ≡ 1 mod φ(n)`.

**Example (Small numbers for illustration):**
1.  **Key Gen:** Let `p=61`, `q=53`.
    *   `n = 61 * 53 = 3233`
    *   `φ(n) = (60)(52) = 3120`
    *   Choose `e=17` (gcd(17, 3120)=1)
    *   Compute `d = 2753` (since `(17 * 2753) mod 3120 = 1`)
    *   **Public Key: (17, 3233), Private Key: (2753, 3233)**
2.  **Encrypt:** Let `M=65`
    *   `C = 65¹⁷ mod 3233 = 2790`
3.  **Decrypt:**
    *   `M = 2790²⁷⁵³ mod 3233 = 65`

## Key Points & Summary

*   **Blum Blum Shub (BBS):** A CSPRNG whose security is based on the integer factorization problem. It's slow but provides strong, provable security ideal for critical tasks.
*   **Public Key Cryptography:** Uses a key pair (public and private) to overcome key distribution issues, enabling secure communication without a pre-shared secret.
*   **RSA Algorithm:** The first and most widely used public-key cryptosystem.
    *   **Security Foundation:** Relies on the practical difficulty of factoring the product of two large primes (`n`).
    *   **Core Operations:** Encryption is a modular exponentiation (`Mᵉ mod n`), and decryption is another (`Cᵈ mod n`).
    *   **Key Generation** is crucial and involves computing `φ(n)` and the modular inverse `d`.
*   **Takeaway:** Both BBS and RSA derive their strength from number theory problems (factoring) that are easy to compute in one direction but intractable to reverse with current technology, forming the bedrock of modern data security.