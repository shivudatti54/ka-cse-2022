# Requirements for Public Key Cryptography - Summary

## Key Definitions and Concepts

- PUBLIC KEY CRYPTOGRAPHY: Asymmetric cryptographic system using a key pair—public key for encryption, private key for decryption.
- ONE-WAY FUNCTION: Easy to compute in forward direction, computationally infeasible to invert without special information.
- TRAPDOOR FUNCTION: One-way function with secret information (private key) that enables efficient inversion.
- SEMANTIC SECURITY (IND-CPA): Property ensuring ciphertexts reveal no information about plaintexts; achieved through probabilistic encryption.
- PERFECT FORWARD SECRECY (PFS): Property ensuring past session keys remain secure even if long-term keys are compromised.

## Important Formulas and Theorems

- RSA Security: Relies on integer factorization difficulty—factoring large composite numbers into prime factors.
- Diffie-Hellman Security: Relies on discrete logarithm problem difficulty in modular arithmetic.
- Key Size Comparison: 2048-bit RSA ≈ 112-bit symmetric security; 256-bit ECC ≈ 128-bit symmetric security.

## Key Points

1. Public key cryptography solves the key distribution problem of symmetric cryptography—no need to share secret keys beforehand.

2. The private key serves as a "trapdoor" making decryption tractable while keeping encryption computationally hard without it.

3. RSA requires much larger keys than symmetric algorithms (2048+ bits vs 128-256 bits) for equivalent security.

4. Probabilistic encryption with random padding provides semantic security; deterministic encryption is vulnerable to chosen plaintext attacks.

5. Ephemeral Diffie-Hellman provides perfect forward secrecy; static RSA key exchange does not.

6. Side-channel attacks (timing, power analysis) exploit implementation flaws, not mathematical weaknesses.

7. Quantum computers threaten integer factorization and discrete logarithm problems, driving post-quantum cryptography research.

## Common Mistakes to Avoid

- Confusing symmetric and asymmetric cryptography requirements—public key systems need larger keys and more computation.
- Believing that mathematical hardness alone guarantees security—implementation flaws enable side-channel attacks.
- Assuming forward secrecy without ephemeral keys—static key exchange protocols lack PFS.
- Using small key sizes thinking they provide adequate security—modern recommendations are 2048-bit minimum for RSA.

## Revision Tips

1. Focus on understanding the "why" behind each requirement rather than memorizing definitions.

2. Practice explaining the trapdoor concept in simple terms—it frequently appears in exam questions.

3. Compare RSA and Diffie-Hellman in terms of the hardness assumptions they rely on.

4. Remember that semantic security requires randomness; deterministic encryption schemes are insecure.

5. Review which protocols provide forward secrecy and why—distinguish ephemeral from static key exchange.