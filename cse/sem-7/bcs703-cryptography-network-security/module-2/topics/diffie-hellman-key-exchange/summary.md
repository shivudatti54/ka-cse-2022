# Diffie-Hellman Key Exchange

=====================================

### Overview

The Diffie-Hellman Key Exchange (1976) was the first practical method for establishing a shared secret key over an insecure public channel. It allows two parties to jointly compute a symmetric key without ever transmitting the key itself. Its security relies on the computational difficulty of the Discrete Logarithm Problem (DLP).

### Key Points

- **Public Parameters:** A large prime p and a primitive root (generator) g, shared openly.
- **Private Keys:** Alice chooses random a; Bob chooses random b (never shared).
- **Public Keys:** Alice computes A = g^a mod p; Bob computes B = g^b mod p (exchanged publicly).
- **Shared Secret:** Alice computes S = B^a mod p; Bob computes S = A^b mod p; both get S = g^(ab) mod p.
- **Discrete Logarithm Problem:** Given g, p, and A = g^a mod p, finding a is computationally infeasible for large p.
- **Man-in-the-Middle Vulnerability:** Basic DHKE lacks authentication; an attacker can intercept and substitute public keys.
- **Perfect Forward Secrecy:** Ephemeral DH (DHE) uses temporary keys per session; past sessions remain secure even if long-term keys are compromised.
- **Applications:** SSL/TLS, IPsec (IKE), SSH, PGP.

### Important Concepts

- Both parties arrive at the same secret because g^(ab) mod p = g^(ba) mod p.
- The eavesdropper sees p, g, A, B but cannot compute S without solving the DLP.
- Authentication (digital signatures or certificates) is required to prevent MITM attacks in practice.
- p should be a strong prime (p = 2q + 1, where q is also prime) for resistance against attacks.

### Notes

- Practice the complete protocol with small numbers (e.g., p=23, g=5) for exam calculations.
- Always mention the MITM vulnerability and the need for authentication in theory answers.
- Draw the Alice-Bob exchange diagram to earn full marks in descriptive questions.
