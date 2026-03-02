# The RSA Algorithm

=====================================

### Overview

RSA is a public-key cryptosystem that uses asymmetric key pairs for encryption, decryption, and digital signatures. Its security is based on the computational difficulty of factoring the product of two large prime numbers, making it a cornerstone of modern secure communication.

### Key Points

- **Asymmetric Keys:** A public key (e, n) for encryption and a private key (d, n) for decryption
- **Key Generation:** Choose primes p, q; compute n = p\*q; compute phi(n) = (p-1)(q-1); select e coprime to phi(n); compute d as modular inverse of e
- **Encryption:** Ciphertext C = M^e mod n (using recipient's public key)
- **Decryption:** Plaintext M = C^d mod n (using recipient's private key)
- **Digital Signatures:** Sign with private key S = Hash(M)^d mod n; verify with public key
- **One-Way Function:** Multiplying primes is easy; factoring n is computationally infeasible
- **OAEP Padding:** Required in practice to prevent deterministic encryption vulnerabilities
- **Hybrid Systems:** RSA encrypts a symmetric session key; AES handles bulk data encryption

### Important Concepts

- Euler's Totient: phi(n) = (p-1)(q-1) for n = p\*q with distinct primes
- Modular inverse relationship: (d \* e) mod phi(n) = 1
- Common public exponent values: e = 3 or e = 65537 (2^16 + 1) for efficiency
- Example: p=61, q=53 -> n=3233, phi(n)=3120, e=17, d=2753
- Key sizes: 2048-bit minimum standard; 4096-bit for long-term security

### Notes

- Memorize all three formulas: key generation, encryption (C = M^e mod n), decryption (M = C^d mod n)
- Practice the full numerical example from key generation through encryption and decryption
- Be prepared to explain why hybrid cryptosystems (RSA + AES) are preferred over pure RSA
- Know the difference between encryption use and digital signature use of RSA keys
