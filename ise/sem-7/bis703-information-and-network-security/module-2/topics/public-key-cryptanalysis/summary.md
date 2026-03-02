# Public Key Cryptanalysis

=====================================

### Overview

Public key cryptanalysis involves breaking asymmetric cryptosystems by exploiting mathematical weaknesses, implementation flaws, or protocol vulnerabilities. Unlike symmetric cryptanalysis, attackers have access to the public key, providing additional information to exploit. Understanding these attacks is essential for designing and deploying secure systems.

### Key Points

- **Brute Force Attack:** Try all possible private keys; infeasible for 2048+ bit RSA keys.
- **Integer Factorization (RSA):** Factor n = p \* q using methods like General Number Field Sieve (GNFS); 829-bit RSA factored in 2020.
- **Discrete Logarithm Attack:** Targets Diffie-Hellman, DSA, ECC; methods include Baby-step Giant-step and Index Calculus.
- **Small Exponent Attack:** When e = 3, same message sent to three recipients can be recovered via Chinese Remainder Theorem.
- **Timing Attack (Side-Channel):** Measures computation time variations to deduce private key bits; defense is constant-time implementation.
- **Chosen Ciphertext Attack (CCA):** Attacker manipulates ciphertexts to extract plaintext; defense is OAEP padding.
- **Man-in-the-Middle (MITM):** Attacker intercepts key exchange; defense is PKI with digital certificates.
- **Wiener's Attack:** Recovers small private exponent d < n^0.25 using continued fractions.

### Important Concepts

- GNFS is the most efficient known factoring algorithm for large numbers (sub-exponential complexity).
- Recommended key sizes: 2048-bit RSA minimum, 256-bit ECC minimum (2020s standards).
- Never use "raw RSA" without padding; always use OAEP for encryption and PSS for signatures.
- Shor's Algorithm (quantum): would break RSA, DH, and ECC in polynomial time; post-quantum cryptography is being standardized.
- Defense in depth: large keys + proper padding + constant-time code + certificate validation.

### Notes

- Know the comparison table of attack types, targets, defenses, and current status for exam answers.
- Always mention OAEP/PSS padding as the defense against CCA when discussing RSA security.
- Quantum computing threat (Shor's algorithm) is a common theory question; mention NIST post-quantum standardization.
