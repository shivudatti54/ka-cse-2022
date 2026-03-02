# Symmetric Cipher Model

=====================================

### Overview

The Symmetric Cipher Model is the foundational encryption framework where the same secret key is used for both encryption and decryption. It defines the core components and process of classical cryptography and underpins modern symmetric algorithms like DES, 3DES, and AES.

### Key Points

- **Five Components:** Plaintext (P), Encryption Algorithm (E), Secret Key (K), Ciphertext (C), Decryption Algorithm (D).
- **Encryption:** C = E(K, P) -- plaintext and key are fed into the encryption algorithm to produce ciphertext.
- **Decryption:** P = D(K, C) -- ciphertext and the same key are used to recover the original plaintext.
- **Symmetric Property:** The same secret key K is shared between sender and receiver.
- **Kerckhoffs's Principle:** Security depends only on the secrecy of the key, not the secrecy of the algorithm.
- **Strong Algorithm Requirement:** Must be computationally infeasible to break even if the attacker knows the algorithm.
- **Key Distribution Problem:** Securely sharing the secret key before communication is the primary challenge.

### Important Concepts

- C = E(K, P) and P = D(K, C) are the fundamental symmetric encryption/decryption functions.
- Kerckhoffs's Principle: algorithm can be public; only the key must remain secret.
- Two requirements for secure use: (1) strong encryption algorithm, (2) secure key distribution.
- Symmetric ciphers are the basis for DES, 3DES, and AES studied in later modules.

### Notes

- Always mention Kerckhoffs's Principle when discussing cryptographic security in exams.
- The key distribution problem is the main limitation of symmetric cryptography; this motivates public-key cryptography.
- Be able to draw and label the symmetric cipher model diagram with all five components.
