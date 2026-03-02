# Applications for Public Key Cryptosystems

=====================================

### Overview

Public key cryptosystems use a mathematically linked pair of keys (public and private) to enable several critical security applications. While slower than symmetric encryption, their true power lies in enabling digital signatures, secure key exchange, encryption of small data, and user authentication.

### Key Points

- **Digital Signatures:** Sign with private key, verify with public key; provides authentication, integrity, and non-repudiation.
- **Key Exchange:** Allows two parties to establish a shared symmetric key over an insecure channel (e.g., Diffie-Hellman).
- **Data Encryption (Confidentiality):** Encrypt with recipient's public key; only the recipient's private key can decrypt.
- **User Authentication:** Prove identity by demonstrating possession of the private key (e.g., SSH keys).
- **DSA and RSA Signatures:** Widely used digital signature algorithms.
- **Hybrid Systems:** Public key cryptography bootstraps symmetric encryption for bulk data (e.g., SSL/TLS, PGP).
- **Performance:** Asymmetric algorithms are slower; typically used for key exchange and signatures, not bulk encryption.

### Important Concepts

- Digital signatures: private key signs, public key verifies (opposite direction from encryption).
- Key exchange solves the key distribution problem of symmetric cryptography.
- Confidentiality: encrypt with public key, decrypt with private key.
- Authentication: prove possession of private key without revealing it.
- Public key crypto is the bedrock of HTTPS, online banking, email encryption, and digital identity.

### Notes

- In exams, clearly distinguish the four applications: signatures, key exchange, encryption, and authentication.
- Remember the direction of key usage: encryption uses public key; signing uses private key.
- Public key systems are rarely used for bulk encryption due to performance; hybrid systems are the standard.
