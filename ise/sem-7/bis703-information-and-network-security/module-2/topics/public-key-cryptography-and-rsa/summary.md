# Public Key Cryptography and RSA

=====================================

### Overview

Public key cryptography (asymmetric cryptography) uses a mathematically related key pair -- a public key for encryption/verification and a private key for decryption/signing -- to solve the key distribution problem. RSA, the most widely used public key algorithm, relies on the difficulty of factoring the product of two large primes.

### Key Points

- **Key Pair:** Public key (e, n) is shared openly; private key (d, n) is kept secret.
- **RSA Key Generation:** Choose primes p, q; compute n = p\*q, phi(n) = (p-1)(q-1); choose e coprime to phi(n); compute d = e^-1 mod phi(n).
- **Encryption:** C = M^e mod n (using public key).
- **Decryption:** M = C^d mod n (using private key).
- **Digital Signatures:** Sign: S = H^d mod n; Verify: H' = S^e mod n; valid if H' = Hash(M).
- **One-Way Trapdoor Function:** Multiplying primes is easy; factoring the product is infeasible without the trapdoor (knowing p, q).
- **Euler's Theorem:** M^phi(n) = 1 mod n; proves that decryption recovers the original message.
- **Hybrid Systems:** RSA exchanges a symmetric session key; AES encrypts the actual data (used in HTTPS).

### Important Concepts

- Security based on Integer Factorization Problem: factoring n = p\*q is infeasible for 2048+ bit keys.
- RSA is 100-1000x slower than symmetric ciphers; used for key exchange and signatures, not bulk encryption.
- Padding schemes: OAEP for encryption, PSS for signatures; prevent attacks on raw RSA.
- Applications: SSL/TLS, PGP, SSH, VPNs, digital signatures, software signing.

### Notes

- Practice the complete RSA workflow (key generation, encryption, decryption) with small numbers for exam problems.
- Understand why RSA works mathematically (Euler's theorem proof: M^(ed) = M mod n).
- Always mention hybrid cryptosystems (RSA + AES) when asked about practical RSA deployment.
