# Requirements for Public Key Cryptography

=====================================

### Overview

For a public key cryptosystem to be practical and secure, it must satisfy six critical requirements that balance computational ease for legitimate users with computational infeasibility for attackers. These requirements define the fundamental asymmetry that all public key systems (RSA, Diffie-Hellman, ECC) must achieve.

### Key Points

- **Requirement 1 -- Easy Key Generation:** Generating a key pair (KU, KR) must be computationally efficient.
- **Requirement 2 -- Easy Encryption:** Computing C = E(KU, M) with the public key must be fast.
- **Requirement 3 -- Easy Decryption:** Computing M = D(KR, C) with the private key must be efficient.
- **Requirement 4 -- Infeasible Private Key Derivation:** Deriving the private key from the public key must be computationally infeasible (core security requirement).
- **Requirement 5 -- Infeasible Plaintext Recovery:** Recovering M from C and KU without the private key must be infeasible.
- **Requirement 6 (Optional) -- Key Reversibility:** Either key can encrypt and the other decrypts; enables digital signatures.
- **Computational Gap:** Easy operations run in polynomial time (milliseconds); infeasible operations are exponential (millions of years).

### Important Concepts

- Computationally easy = polynomial time: O(n), O(n^2), O(n log n).
- Computationally infeasible = exponential/sub-exponential: O(2^n), O(e^(n^(1/3))).
- RSA meets all six requirements; DH meets requirements 1-5 but is designed for key exchange, not encryption.
- Hard problems: Integer factorization (RSA), Discrete logarithm (DH/ECC), Elliptic Curve DLP (ECC).
- Key sizes must increase over time as computing power grows (512-bit broken -> 2048-bit minimum today).

### Notes

- Memorize all six requirements and be able to explain each with RSA examples.
- Requirement 4 (private key infeasibility) is the most important; highlight it in exam answers.
- Know how key sizes have evolved: 512-bit (broken) -> 1024-bit (marginal) -> 2048-bit (minimum) -> 4096-bit (recommended).
