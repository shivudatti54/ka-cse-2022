# Public Key Encryption – Quick Revision Summary

**Information Security (Delhi University – NEP 2024 UGCF)**

## Introduction
Public Key Encryption, also known as Asymmetric Cryptography, is a fundamental concept in modern information security. Unlike symmetric encryption, it uses a pair of mathematically related keys—a **public key** for encryption and a **private key** for decryption. This innovation solved the critical key distribution problem in classical cryptography and forms the backbone of secure digital communications.

## Key Concepts

- **Asymmetric Key Pairs**
  - Public key: Shared openly, used to encrypt messages or verify digital signatures
  - Private key: Kept secret by the owner, used to decrypt messages or create signatures
  - Mathematically related but computationally infeasible to derive one from the other

- **Core Principles**
  - Confidentiality: Only the intended recipient with the private key can decrypt
  - Authentication: Verifies the sender's identity
  - Non-repudiation: Sender cannot deny sending the message
  - Key Distribution: Eliminates need for secure key exchange channels

## Important Algorithms (UGCF Syllabus)

- **RSA (Rivest-Shamir-Adleman)**
  - Most widely used public key algorithm
  - Based on difficulty of factoring large prime numbers
  - Used in SSL/TLS, digital signatures, email security

- **Diffie-Hellman Key Exchange**
  - Enables secure key exchange over insecure channels
  - Foundation for many VPN protocols

- **Elliptic Curve Cryptography (ECC)**
  - More efficient than RSA with smaller key sizes
  - Used in mobile devices and IoT applications

- **Digital Signatures**
  - RSA, DSA (Digital Signature Algorithm), ECDSA
  - Ensures message integrity and authenticity

## Applications (Delhi University Syllabus)

- Secure web browsing (HTTPS/SSL/TLS)
- Digital certificates and PKI (Public Key Infrastructure)
- Email encryption (PGP, S/MIME)
- Cryptocurrency and blockchain
- VPN and secure remote access
- Electronic banking and e-commerce

## Advantages

- Solves key distribution problem
- Enables digital signatures and authentication
- Scalable for large networks
- Supports confidentiality, integrity, and authenticity

## Limitations

- Slower than symmetric encryption (computationally intensive)
- Requires larger key sizes for equivalent security
- Vulnerable to man-in-the-middle attacks without proper authentication
- Private key compromise leads to total security breach

## Conclusion
Public Key Encryption revolutionized information security by providing robust solutions for key exchange, digital signatures, and secure communication over insecure networks. Mastery of its underlying mathematics, algorithms, and practical applications is essential for any computer science professional. Understanding its strengths and limitations enables appropriate selection of cryptographic solutions in real-world security implementations.

---
*For detailed study, refer to: Stallings (Cryptography and Network Security), Delhi University B.Sc. (H) CS UGCF Module 5 – Cryptography*