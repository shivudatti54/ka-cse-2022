# Key Exchange Protocols

=====================================

### Overview

Key exchange protocols solve the fundamental problem of securely establishing a shared symmetric key over an insecure network. The Diffie-Hellman Key Exchange (DHKE) was the first practical solution, while the Station-to-Station (STS) protocol extends it with mutual authentication to prevent man-in-the-middle attacks.

### Key Points

- **Key Distribution Problem:** How do two parties agree on a shared symmetric key without a pre-existing secure channel?
- **Diffie-Hellman (DHKE):** First practical key exchange; based on the Discrete Logarithm Problem (DLP).
- **DHKE Protocol:** Public parameters (p, g) -> private keys (a, b) -> public keys (A = g^a mod p, B = g^b mod p) -> shared secret S = g^(ab) mod p.
- **DHKE Strength:** Provides Perfect Forward Secrecy (PFS); past sessions remain secure even if long-term keys are later compromised.
- **DHKE Weakness:** Vulnerable to Man-in-the-Middle (MITM) attacks because it lacks authentication.
- **Station-to-Station (STS):** Extends DHKE by adding digital signatures for mutual authentication, preventing MITM.
- **STS Process:** Exchange DH public keys, compute shared secret, sign exchanged messages, encrypt signatures with derived key.
- **Real-World Usage:** DHKE is foundational for SSL/TLS, SSH, and IPsec, always combined with certificate-based authentication.

### Important Concepts

- DLP: Given g^x mod p, finding x is computationally infeasible for large p.
- MITM attack: attacker intercepts and replaces public keys, establishing separate keys with each party.
- STS combines DHKE with digital signatures to authenticate both parties and prevent MITM.
- DHKE must always be combined with an authentication mechanism for secure real-world use.

### Notes

- Always mention both the strength (PFS) and weakness (MITM) of basic DHKE in exam answers.
- The STS protocol is the authenticated version of DHKE; know how digital signatures are integrated.
- Be prepared to explain how DHKE fits into TLS/IPsec with certificates for authentication.
