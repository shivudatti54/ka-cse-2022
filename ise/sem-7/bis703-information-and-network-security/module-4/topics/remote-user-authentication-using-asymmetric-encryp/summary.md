# Remote User Authentication using Asymmetric Encryption

### Key Points

- **Definition**: Asymmetric encryption is a type of encryption that uses a pair of keys: a public key for encryption and a private key for decryption.
- **Key Concepts**:
  - RSA (Rivest-Shamir-Adleman) algorithm
  - Digital Certificates
  - Public Key Infrastructure (PKI)
- **Authentication Process**:
  1.  User requests authentication
  2.  Server sends public key to client
  3.  Client encrypts username and password with server's public key
  4.  Server decrypts message with private key and verifies authenticity

### Important Formulas and Theorems

- **Public Key Cryptography**:
  - $E_k(M) = C$, where $M$ is the message, $k$ is the public key, and $C$ is the ciphertext
  - $D_k(C) = M$, where $D_k$ is the private key and $C$ is the ciphertext
- **RSA Algorithm**:
  - $n = p \cdot q$, where $p$ and $q$ are prime numbers
  - $\phi(n) = (p-1) \cdot (q-1)$

### Important Definitions

- **Asymmetric Encryption**: encryption that uses a pair of keys for encryption and decryption
- **Symmetric Encryption**: encryption that uses the same key for encryption and decryption
- **Digital Certificate**: a self-contained set of data that includes a public key and identity information
- **Public Key Infrastructure (PKI)**: a system that manages the distribution of public keys and digital certificates

### Important Theorems

- **RSA Theorem**: if $n$ is the product of two large prime numbers $p$ and $q$, then $n$ is a secure modulus for RSA encryption
- **Diffie-Hellman Key Exchange**: a key exchange protocol that allows two parties to establish a shared secret key over an insecure channel

Note: This summary is a condensed version of the topic and is intended for quick revision purposes.
