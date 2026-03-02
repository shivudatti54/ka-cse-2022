# Pseudorandom Number Generators (PRNGs) in Cryptography


## Table of Contents

- [Pseudorandom Number Generators (PRNGs) in Cryptography](#pseudorandom-number-generators-prngs-in-cryptography)
- [Introduction to Pseudorandom Number Generators](#introduction-to-pseudorandom-number-generators)
- [Why PRNGs are Essential in Public Key Cryptography](#why-prngs-are-essential-in-public-key-cryptography)
- [Core Properties of a Cryptographically Secure PRNG (CSPRNG)](#core-properties-of-a-cryptographically-secure-prng-csprng)
- [Structure of a Typical PRNG](#structure-of-a-typical-prng)
- [Common PRNG Algorithms](#common-prng-algorithms)
  - [1. Linear Congruential Generator (LCG) - **NOT CRYPTOGRAPHICALLY SECURE**](#1-linear-congruential-generator-lcg---not-cryptographically-secure)
  - [2. Cryptographically Secure PRNGs](#2-cryptographically-secure-prngs)
- [Seed Management: The Root of All Security](#seed-management-the-root-of-all-security)
- [PRNGs vs. TRNGs: A Comparison](#prngs-vs-trngs-a-comparison)
- [Example: Generating an RSA Key](#example-generating-an-rsa-key)
- [Exam Tips](#exam-tips)

## Introduction to Pseudorandom Number Generators

A Pseudorandom Number Generator (PRNG) is a deterministic algorithm designed to produce a sequence of numbers that approximates the properties of a truly random sequence. While true random numbers are generated from unpredictable physical processes (like atmospheric noise or radioactive decay), PRNGs are algorithmic and therefore reproducible given the same initial value, known as a **seed**.

In cryptography, PRNGs are fundamental for generating keys, nonces, initialization vectors, and other values that require unpredictability. Their security is crucial because if an attacker can predict the output of a PRNG, they can often break the cryptographic system that relies on it.

## Why PRNGs are Essential in Public Key Cryptography

Public Key Cryptography algorithms often require large random numbers:

- **RSA:** Requires large random prime numbers `p` and `q` to generate the public and private keys.
- **Diffie-Hellman:** Requires a large random private exponent.
- **Elliptic Curve Cryptography (ECC):** Requires a random private key (a large integer).
- **Digital Signatures:** Many signature schemes require a random nonce for each signature to ensure security.

Using a weak or predictable PRNG in any of these applications can lead to catastrophic failure, allowing an attacker to recover private keys.

## Core Properties of a Cryptographically Secure PRNG (CSPRNG)

For a PRNG to be suitable for cryptographic applications, it must possess two key properties:

1.  **Unpredictability (Forward Secrecy):** Given a sequence of output bits `output₁, output₂, ..., outputₖ`, it must be computationally infeasible to predict the next output bit `outputₖ₊₁` with a probability significantly better than ½. This implies that even if an attacker discovers the internal state of the generator at a point in time, previous outputs should remain unpredictable.

2.  **Randomness (Statistical Properties):** The output sequence must pass standard statistical tests for randomness. These tests check for properties like:
    - **Uniform Distribution:** Each possible number is equally likely to occur.
    - **Independence:** The value of one output does not depend on the value of previous outputs (e.g., no discernible patterns or correlations).

A PRNG that satisfies these properties is called a **Cryptographically Secure Pseudorandom Number Generator (CSPRNG)**.

## Structure of a Typical PRNG

Most PRNGs follow a common internal structure, which can be visualized as a state machine.

```
+-----------------------------------+
|             Internal State         | <---+
|  (e.g., a seed value or buffer)    |     | Update
+-----------------------------------+     | Function
        |                                  |
        | Generate Output                  |
        v                                  |
+------------------+               +-----------------+
|   Output Block   |               |  Next State     |
| (Pseudorandom #) |               | (e.g., S_{i+1}) |
+------------------+               +-----------------+
```

**Components:**

1.  **Internal State:** A value, or set of values, that the generator keeps in memory. The security of the entire system often relies on keeping this state secret.
2.  **Output Function (`G`):** Takes the current internal state and generates an output block of bits. This function is often a one-way function to make state recovery from output difficult.
3.  **Update Function (`F`):** Takes the current internal state and generates a new state for the next iteration. `S_{i+1} = F(S_i)`.

**Process:**

1.  **Initialization:** The PRNG is seeded with an initial value (`S₀`). This seed should be truly random and sufficiently large (e.g., 128 or 256 bits) to prevent brute-force attacks.
2.  **Generation:** For each step `i`:
    - The output `output_i = G(S_i)` is produced.
    - The state is updated: `S_{i+1} = F(S_i)`.

## Common PRNG Algorithms

### 1. Linear Congruential Generator (LCG) - **NOT CRYPTOGRAPHICALLY SECURE**

This is a simple and fast PRNG often used in general programming (e.g., `rand()` in C) but is completely insecure for cryptography.

**Formula:** `S_{n+1} = (a * S_n + c) mod m`

Where:

- `S_n` is the current state (seed).
- `a` is the multiplier.
- `c` is the increment.
- `m` is the modulus.

**Why it's insecure:** The output is highly predictable and exhibits strong correlations. Given a few output samples, the parameters (`a`, `c`, `m`) and future outputs can be easily calculated.

### 2. Cryptographically Secure PRNGs

These are designed to withstand cryptographic analysis.

**A. Blum Blum Shub (BBS)**
A theoretically secure but slow generator based on the difficulty of integer factorization.

**Process:**

1.  Choose two large prime numbers `p` and `q`, both congruent to `3 mod 4`.
2.  Compute `n = p * q`.
3.  Select a random seed `s` coprime to `n`.
4.  For each step: `S_{i+1} = (S_i)² mod n`
5.  The output is often the least significant bit (or a few bits) of `S_i`.

**B. Designs based on Cryptographic Primitives**
Modern CSPRNGs are built using hash functions, block ciphers, or stream ciphers. This is efficient and leverages the well-studied security of these primitives.

- **Based on Hash Functions (e.g., ANSI X9.17):**

  ```
  Date = Current timestamp
  Seed_{i+1} = Hash (Date || Seed_i)
  Output_i = Hash (Date || Seed_{i+1})
  ```

  This design uses a hash function like SHA-256 in a feedback loop.

- **Based on Block Ciphers (e.g., CTR Mode PRNG):**
  Treat the internal state as a counter. Encrypt the counter using a secret key `K` to produce output. Then, increment the counter.
  ```
  Output_i = Encrypt_K(Counter_i)
  Counter_{i+1} = Counter_i + 1
  ```
  This is very efficient and secure if the underlying block cipher (e.g., AES) is secure.

## Seed Management: The Root of All Security

The security of any PRNG is entirely dependent on the quality and secrecy of its seed. A CSPRNG with a predictable or guessable seed is no longer secure.

**Best Practices:**

- The initial seed must be generated from a high-entropy source (a **True Random Number Generator - TRNG**), such as hardware noise.
- The seed must be kept secret. It is often the root key for the entire cryptographic system.
- Reseeding should be done periodically, especially after a certain number of outputs, to provide backward secrecy (if the current state is compromised, past states remain secure).

## PRNGs vs. TRNGs: A Comparison

| Feature              | Pseudorandom Number Generator (PRNG)          | True Random Number Generator (TRNG)       |
| :------------------- | :-------------------------------------------- | :---------------------------------------- |
| **Source**           | Deterministic Algorithm                       | Physical Phenomenon (e.g., thermal noise) |
| **Speed**            | Very Fast                                     | Typically Slower                          |
| **Reproducibility**  | Reproducible with same seed                   | Not Reproducible                          |
| **Predictability**   | Predictable if algorithm & seed are known     | Unpredictable                             |
| **Entropy**          | Derived from initial seed                     | Inherently high                           |
| **Primary Use Case** | Bulk key generation, cryptographic operations | Seeding PRNGs, generating master keys     |

In practice, systems use a hybrid approach: a TRNG gathers entropy to create a strong seed, which is then fed into a fast CSPRNG to generate the large amounts of random data needed.

## Example: Generating an RSA Key

The process of generating an 2048-bit RSA key highlights the importance of a CSPRNG:

1.  **Generate Candidate `p`:** The CSPRNG produces a random 1024-bit odd number.
2.  **Test for Primality:** A probabilistic test (like Miller-Rabin) uses the PRNG to choose random bases to test if `p` is probably prime.
3.  **Repeat for `q`:** The CSPRNG produces another random 1024-bit odd number and tests it.
4.  **Form the Modulus:** `n = p * q`.

If the PRNG is flawed and produces `p` and `q` from a small, predictable set, an attacker could precompute possible values and easily factor `n`.

## Exam Tips

- **Memorize the Key Properties:** Always be able to state and explain the two properties of a CSPRNG: **Unpredictability** and **Statistical Randomness**.
- **Understand the Seed's Role:** A common exam question is to explain why a PRNG is only as secure as its seed. Emphasize that the algorithm is public; the seed is the secret.
- **Know Why LCG is Bad for Crypto:** Be prepared to explain the linear relationship `S_{n+1} = (a * S_n + c) mod m` and why it makes the output predictable.
- **Recognize Secure Constructions:** Remember that modern CSPRNGs are built from cryptographic primitives like hash functions (SHA-256) and block ciphers (AES).
- **Differentiate PRNG from TRNG:** Be clear on the table of differences, especially regarding speed, reproducibility, and source.
