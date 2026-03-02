# Computational Aspects

=====================================

### Overview

The practical security of public key cryptosystems depends on computational complexity -- certain mathematical problems must be easy to compute in one direction but infeasible to reverse. This topic covers the "hard" problems underlying modern cryptography, the efficiency of cryptographic operations, and the algorithms that make encryption practical.

### Key Points

- **One-Way Functions:** Easy to compute forward but computationally infeasible to reverse without special information (trapdoor).
- **Integer Factorization Problem (IFP):** Basis for RSA; given n = p \* q, finding p and q is infeasible for large n.
- **Discrete Logarithm Problem (DLP):** Basis for Diffie-Hellman and DSA; given y = g^x mod p, finding x is extremely difficult.
- **Elliptic Curve DLP (ECDLP):** Allows smaller keys with equivalent security; used in ECC.
- **Computational Complexity:** Problems classified as P (polynomial time) and NP (verifiable in polynomial time); crypto relies on problems believed outside P.
- **Square-and-Multiply Algorithm:** Efficiently computes modular exponentiation (C = M^e mod n) in O(log e) operations.
- **Symmetric vs. Asymmetric Speed:** Symmetric algorithms (AES) are much faster for bulk encryption; asymmetric algorithms are used for key exchange and signatures.

### Important Concepts

- RSA core operations: C = M^e mod n (encryption) and M = C^d mod n (decryption).
- Square-and-multiply reduces exponentiation from O(e) to O(log e) multiplications.
- Factoring large composites and solving discrete logarithms are sub-exponential but super-polynomial problems.
- Key generation (finding large primes for RSA) must be both efficient and secure.

### Notes

- Understand why factoring and discrete log are considered "hard" problems and which algorithms rely on each.
- Be able to explain the square-and-multiply algorithm for modular exponentiation.
- Remember: asymmetric crypto is slower, so hybrid systems use it only for key exchange, not bulk data.
