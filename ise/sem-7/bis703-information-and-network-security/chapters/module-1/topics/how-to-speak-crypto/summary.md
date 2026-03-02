# **How to Speak Crypto Revision Notes**

### Introduction

- Cryptography is the practice and study of techniques for secure communication
- It involves the use of algorithms and protocols to protect the confidentiality, integrity, and authenticity of messages

### Key Concepts

- **Cryptographic Techniques**:
  - Symmetric-key encryption (e.g. AES)
  - Asymmetric-key encryption (e.g. RSA)
  - Hash functions (e.g. SHA-256)
  - Digital signatures (e.g. ECDSA)
- **Cryptographic Libraries and Frameworks**:
  - OpenSSL
  - NaCl
  - cryptography (Python)
- **Cryptographic Protocols**:
  - SSL/TLS
  - IPsec
  - PGP

### Definitions

- **Asymptotic Security**: the computational complexity of a cryptosystem
- **Key Exchange**: the process of securely exchanging cryptographic keys between parties
- **Pad**: padding data to ensure it is a multiple of the block size
- **Block Cipher**: a type of encryption algorithm that operates on fixed-size blocks of data

### Theorems

- **Shannon's Source Coding Theorem**: the minimum amount of entropy required to transmit a message
- **Bellman's Theorem**: the minimum number of bits required to transmit a message of a given entropy
- **Cramer's Rule**: a method for finding the values of variables in a system of equations

### Important Formulas

- **AES encryption**:
  - `C = E(K, P)`, where C is the ciphertext, K is the key, and P is the plaintext
- **RSA encryption**:
  - `C = E(d, P)`, where C is the ciphertext, d is the public key, and P is the plaintext
- **Hash function**:
  - `H(P) = h(P)`, where H is the hash function, and P is the plaintext

### Key Terms

- **Weakness**: a vulnerability in a cryptosystem
- **Side-channel attack**: an attack that exploits information about the implementation of a cryptosystem
- **Key recovery**: the process of recovering a lost or compromised key
