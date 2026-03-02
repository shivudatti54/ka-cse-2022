# The RSA Algorithm

=====================================

### Overview

The RSA algorithm is the most widely used public-key cryptosystem, invented by Rivest, Shamir, and Adleman in 1977. It uses a pair of mathematically related keys (public and private) to provide encryption, decryption, and digital signatures, solving the key distribution problem of symmetric ciphers.

### Key Points

- **Public Key (e, n):** Used for encryption; can be freely distributed to anyone
- **Private Key (d, n):** Used for decryption; must be kept secret by the owner
- **Modulus n:** Computed as n = p \* q, where p and q are two large prime numbers
- **Euler's Totient:** phi(n) = (p-1)(q-1), counts integers less than n coprime to n
- **Public Exponent e:** Chosen such that 1 < e < phi(n) and GCD(e, phi(n)) = 1; commonly 65537
- **Private Exponent d:** Modular multiplicative inverse of e mod phi(n), i.e., (d \* e) mod phi(n) = 1
- **Integer Factorization Problem:** Security relies on the difficulty of factoring large n back into p and q
- **Hybrid Cryptosystem:** RSA is slow, so it is typically used to exchange a symmetric session key (e.g., AES)

### Important Concepts

- Encryption formula: **C = M^e mod n**
- Decryption formula: **M = C^d mod n**
- Digital Signature: S = Hash(M)^d mod n; Verification: Hash(M) == S^e mod n
- Key generation steps: select p, q -> compute n -> compute phi(n) -> choose e -> find d
- Minimum recommended key size: 2048 bits; 4096 bits for long-term security

### Notes

- Practice numerical examples (e.g., p=61, q=53) to quickly compute n, phi(n), e, and d in exams
- Always mention OAEP padding when discussing practical RSA security
- Understand why RSA is used for key exchange and signatures, not bulk encryption
- Be ready to compare RSA (asymmetric, slow, 2048+ bits) vs AES (symmetric, fast, 128/256 bits)
