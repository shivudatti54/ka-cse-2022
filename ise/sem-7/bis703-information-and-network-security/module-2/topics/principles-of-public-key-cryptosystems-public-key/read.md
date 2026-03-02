

## Table of Contents

- [Module 2: Principles of Public Key Cryptosystems](#module-2-principles-of-public-key-cryptosystems)
- [1. Introduction](#1-introduction)
- [2. Core Concepts](#2-core-concepts)
  - [The Two-Key Principle](#the-two-key-principle)
  - [How It Works: Confidentiality](#how-it-works-confidentiality)
  - [How It Works: Authentication & Digital Signatures](#how-it-works-authentication--digital-signatures)
  - [The One-Way Function Trapdoor](#the-one-way-function-trapdoor)
- [3. A Simple Example (RSA Concept)](#3-a-simple-example-rsa-concept)
- [4. Key Points & Summary](#4-key-points--summary)

Of course. Here is a comprehensive educational note on Public Key Cryptosystems for Engineering students.

# Module 2: Principles of Public Key Cryptosystems

## 1. Introduction

Traditional symmetric-key cryptography, which we studied in Module 1, uses a single shared secret key for both encryption and decryption. While efficient, it faces a significant challenge: **key distribution**. How do you securely share the secret key with the intended recipient over an insecure channel?

Public-key cryptography, introduced by Whitfield Diffie and Martin Hellman in 1976, revolutionized the field by solving this problem. It uses two mathematically linked keys: a public key and a private key. This foundation enables secure communication without a pre-shared secret and is the bedrock of modern internet security, including SSL/TLS, digital signatures, and cryptocurrencies.

## 2. Core Concepts

### The Two-Key Principle

A public-key cryptosystem is based on a pair of keys:

- **Public Key:** This key is made publicly available to anyone. It is used for **encryption** or for **verifying a digital signature**.
- **Private Key:** This key is kept secret by the owner. It is used for **decryption** or for **creating a digital signature**.

These keys are mathematically related, but it must be computationally infeasible to derive the private key from the public key.

### How It Works: Confidentiality

The primary application for confidentiality is as follows:

1.  **Key Generation:** A user (say, **Bob**) generates a pair of keys: a public key `Kpub_B` and a private key `Kpriv_B`.
2.  **Key Distribution:** Bob publishes his public key `Kpub_B` in a public directory. He keeps `Kpriv_B` absolutely secret.
3.  **Encryption:** Another user (say, **Alice**) who wants to send a confidential message to Bob encrypts her plaintext message `P` using Bob's public key: `C = E(Kpub_B, P)`, where `E` is the encryption algorithm.
4.  **Decryption:** Bob receives the ciphertext `C` and decrypts it using his private key to recover the original message: `P = D(Kpriv_B, C)`, where `D` is the decryption algorithm.

**Crucial Point:** Since only Bob possesses `Kpriv_B`, only he can decrypt the ciphertext `C`. Even if an eavesdropper (Eve) intercepts `C` and has access to `Kpub_B`, she cannot decrypt the message.

### How It Works: Authentication & Digital Signatures

Public-key cryptography can also provide authentication and non-repudiation through digital signatures.

1.  **Signing:** Bob can "sign" a message by encrypting it (or a hash of it) with his **private key**, creating a signature `S = E(Kpriv_B, Hash(P))`.
2.  **Verification:** Anyone who has Bob's **public key** can verify the signature by decrypting it: `Decrypted_Hash = D(Kpub_B, S)`. If this matches the hash of the received message, it proves the message originated from Bob (authentication) and has not been altered (integrity).

### The One-Way Function Trapdoor

The mathematical heart of public-key cryptography is the **one-way function with a trapdoor**.

- **One-Way Function:** A function that is easy to compute in one direction (forward) but computationally very difficult to reverse without special information.
  - _Example:_ Multiplying two large prime numbers (e.g., `p` and `q`) is easy. However, factoring the resulting product `n = p * q` back into its prime factors is extremely hard for large `n`.
- **Trapdoor:** A piece of special information that makes reversing the one-way function easy.
  - _Example:_ In the prime multiplication example, knowing one of the prime factors (`p` or `q`) is the trapdoor that makes factoring `n` trivial.

In a cryptosystem like RSA:

- The **public key`contains the product`n`**.
- The **private key`contains the prime factors`p`and`q`** (the trapdoor).

## 3. A Simple Example (RSA Concept)

Let's illustrate the confidentiality process with a highly simplified numerical example of RSA.

1.  **Key Generation (Bob):**
    - Chooses two primes: `p=3`, `q=11`. (In reality, these are 1024+ bits long).
    - Computes `n = p * q = 33`.
    - Computes Euler's totient: `φ(n) = (p-1)(q-1) = 20`.
    - Chooses a public exponent `e` coprime to φ(n); `e=7`.
    - Computes private exponent `d` such that `(d * e) mod φ(n) = 1`. Here, `d=3` because `(3*7) mod 20 = 21 mod 20 = 1`.
    - **Public Key (`Kpub_B`): (e=7, n=33)**
    - **Private Key (`Kpriv_B`): (d=3, n=33)**

2.  **Encryption (Alice):**
    - Message `P = 4` (a numerical representation of data).
    - Uses Bob's public key: `C = P^e mod n = 4^7 mod 33`.
    - `4^7 = 16384`. `16384 mod 33 = 16`. (You can compute this step-wise with modulo arithmetic).
    - Sends ciphertext `C = 16` to Bob.

3.  **Decryption (Bob):**
    - Uses his private key: `P = C^d mod n = 16^3 mod 33`.
    - `16^3 = 4096`. `4096 mod 33 = 4`. (Again, use step-wise calculation).
    - Recovers original message `P = 4`.

This demonstrates the one-way function: computing `C = 4^7 mod 33` is easy, but without the trapdoor (`d=3`), deducing `P` from `C=16` is very difficult.

## 4. Key Points & Summary

| **Aspect**            | **Symmetric-Key Cryptography**           | **Public-Key Cryptography**                            |
| :-------------------- | :--------------------------------------- | :----------------------------------------------------- |
| **Keys**              | Single, shared secret key                | Mathematically linked key pair: Public & Private       |
| **Key Distribution**  | Major challenge; requires secure channel | Solves the problem; public keys can be shared openly   |
| **Primary Functions** | Confidentiality, Data Integrity          | Confidentiality, Authentication, Digital Signatures    |
| **Speed**             | Fast                                     | Slower (computationally intensive)                     |
| **Algorithms**        | AES, DES, 3DES                           | RSA, Elliptic Curve Cryptography (ECC), Diffie-Hellman |

**Summary:**

- Public-key cryptosystems use a pair of keys: a public key for encryption/verification and a private key for decryption/signing.
- They solve the key distribution problem inherent in symmetric cryptography.
- Their security relies on the computational difficulty of solving mathematical problems like integer factorization (RSA) or discrete logarithms (ECC, Diffie-Hellman).
- They are slower than symmetric ciphers, so hybrid systems are often used: a public-key algorithm is used to securely exchange a symmetric session key, which is then used to encrypt the bulk of the data.
