# Information and Network Security Revision Notes

==============================================

### Random Number Generation

- Random number generation (RNG) is essential for generating unpredictable numbers.
- Types of RNG:
  - Pseudorandom Number Generators (PRNGs)
  - Hardware-based RNGs
- PRNGs:
  - Pseudocode: `x = (a * x + c) mod m`, where `x` is the generated number and `a`, `c`, and `m` are constants.
- Secure RNGs:
  - Entropy-based methods (e.g., thermal noise, photon arrival times)
  - Cryptographically secure PRNGs (e.g., Fortuna, Yarrow-Ulam)

### Providing Freshness

- Freshness refers to the uniqueness of random numbers.
- Key concepts:
  - Entropy: a measure of the unpredictability of a random number.
  - Collision resistance: the ability to prevent two different inputs from producing the same output.

### Fundamentals of Entity Authentication

- Entity authentication: the process of verifying the identity of a user or entity.
- Types of authentication:
  - Password authentication
  - Challenge-response authentication
  - Public key authentication
- Security considerations:
  - Password storage (e.g., hashing, salting)
  - Session management

### Passwords

- Passwords are a common authentication mechanism.
- Key concepts:
  - Password strength (e.g., entropy, complexity)
  - Password cracking (e.g., brute force, rainbow tables)
  - Password policies (e.g., password length, history)

### Dynamic Password Schemes

- Dynamic password schemes: methods for generating and managing passwords.
- Key concepts:
  - One-time passwords (OTPs)
  - Time-based one-time passwords (TOTPs)
  - Password-based key derivation functions (PBKDFs)

### Zero-Knowledge Mechanisms

- Zero-knowledge mechanisms: methods for verifying the truth of a statement without revealing any information.
- Key concepts:
  - Zero-knowledge proofs (ZKPs)
  - Zero-knowledge SNarks (ZK-SNARKs)
  - Fully homomorphic encryption (FHE)

Important Formulas and Definitions:

- **Entropy**: `H(X) = - ∑ p(x) log2 p(x)`, where `H(X)` is the entropy of a random variable `X` and `p(x)` is the probability distribution of `X`.
- **Collision resistance**: a hash function `h(x)` is collision-resistant if, for any two distinct inputs `x` and `y`, `h(x) ≠ h(y)`.
- **Zero-knowledge proof**: a proof that a statement is true without revealing any information about the statement.

Important Theorems:

- **Shannon's Entropy Theorem**: `H(X) = - ∑ p(x) log2 p(x)`, where `H(X)` is the entropy of a random variable `X` and `p(x)` is the probability distribution of `X`.
- **Goldwasser's Zero-Knowledge Theorem**: a zero-knowledge proof can be constructed for any statement, given a suitable hash function and a random number generator.

Note: This summary focuses on key concepts and formulas, and is intended to be a quick revision guide for the topic of random number generation, providing freshness, fundamentals of entity authentication, passwords, dynamic password schemes, and zero-knowledge mechanisms.
