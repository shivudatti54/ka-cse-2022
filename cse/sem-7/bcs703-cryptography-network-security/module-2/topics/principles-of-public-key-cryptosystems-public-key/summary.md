# Principles of Public Key Cryptosystems

=====================================

### Overview

Public key cryptography, introduced by Diffie and Hellman in 1976, uses a mathematically linked pair of keys (public and private) to solve the key distribution problem of symmetric cryptography. The public key encrypts or verifies signatures, while the private key decrypts or signs. Security relies on one-way functions with trapdoors.

### Key Points

- **Two-Key Principle:** Public key (shared openly) for encryption/verification; private key (kept secret) for decryption/signing.
- **Confidentiality:** Alice encrypts with Bob's public key: C = E(Kpub_B, P); Bob decrypts with private key: P = D(Kpriv_B, C).
- **Digital Signatures:** Bob signs with private key: S = E(Kpriv_B, Hash(P)); anyone verifies with public key.
- **One-Way Function with Trapdoor:** Easy to compute forward (multiply primes), hard to reverse (factor product) without the trapdoor (knowing one prime).
- **Solves Key Distribution:** No pre-shared secret needed; public keys can be distributed openly.
- **Slower Than Symmetric:** Computationally intensive; hybrid systems use public key for key exchange + symmetric cipher for bulk data.
- **Underlying Hard Problems:** Integer factorization (RSA), discrete logarithm (Diffie-Hellman, ECC).

### Important Concepts

- Public key contains n (product of primes); private key contains the prime factors p and q (the trapdoor).
- RSA example: Public key (e, n), Private key (d, n); C = P^e mod n, P = C^d mod n.
- Hybrid approach: public key exchanges a symmetric session key, which encrypts the actual data.
- It is computationally infeasible to derive the private key from the public key.

### Notes

- Know the comparison table: symmetric (single key, fast, key distribution problem) vs. asymmetric (key pair, slower, solves distribution).
- Be able to explain the one-way function trapdoor concept with a simple RSA numerical example.
- Hybrid systems combining RSA + AES are the standard in practice (e.g., SSL/TLS).
