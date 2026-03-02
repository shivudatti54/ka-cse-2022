# **Public-Key Management: Revision Notes**

### Definitions and Key Concepts

- **Public-Key**: A pair of keys, one public and one private, used for encryption and decryption.
- **Certificate**: A document that binds a public key to an entity's identity.
- **Certificate Authority (CA)**: An entity that issues digital certificates.
- **Certificate Lifecycle**: The process of issuing, managing, and revoking certificates.

### Certification of Public Keys

- **Public Key Infrastructure (PKI)**: A system that uses certificates to manage public keys.
- **X.509 Certificate**: A standard certificate format used in PKI.
- **Certificate Signing Algorithm (DSA)**: An algorithm used to sign certificates.
- **Key Pair Generation Algorithm (RSA)**: An algorithm used to generate public and private key pairs.

### The Certificate Lifecycle

- **Certificate Issuance**:
  - Entity requests a certificate from a CA.
  - CA verifies the entity's identity and issues a certificate.
- **Certificate Revocation**:
  - Entity's certificate is compromised or no longer valid.
  - CA revokes the certificate and issues a revocation certificate.
- **Certificate Renewal**:
  - Entity's certificate is near expiration.
  - CA issues a new certificate.

### Public-Key Management Models

- **Traditional PKI Model**: A centralized model where a CA issues certificates.
- ** Hierarchical PKI Model**: A decentralized model where multiple CAs issue certificates.
- **Open PKI Model**: A decentralized model where any entity can issue certificates.

### Alternative Approaches

- **Elliptic Curve Cryptography (ECC)**: A cryptographic technique that uses elliptic curves to generate public and private key pairs.
- **Quantum Key Distribution (QKD)**: A method of secure key exchange using quantum mechanics.
- **Hybrid PKI Model**: A combination of traditional and hierarchical PKI models.

### Important Formulas and Theorems

- **RSA Algorithm**: `c = m^e mod n`, where `c` is the ciphertext, `m` is the plaintext, `e` is the public exponent, and `n` is the modulus.
- **Diffie-Hellman Key Exchange**: `a^b mod n = c`, where `a` is the private key, `b` is the private key of the other party, and `c` is the shared secret key.
- **Elliptic Curve Discrete Logarithm Problem (ECDLP)**: A problem used to secure ECC.
