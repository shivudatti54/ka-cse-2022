# The Security of RSA

## Introduction

The security of the RSA cryptosystem rests upon the computational hardness of two fundamental mathematical problems: the integer factorization problem and the RSA problem. Understanding the precise relationship between these problems and the security of RSA is essential for proper implementation and usage of the cryptosystem. This document provides a rigorous analysis of RSA security, including the theoretical foundations, known attacks, padding requirements, and practical implementation considerations.

The RSA algorithm, developed by Rivest, Shamir, and Adleman in 1977, remains one of the most widely deployed public-key cryptosystems. Its security stems from the computational difficulty of factoring large composite numbers into their prime factors. However, this relationship between factoring and RSA security is more nuanced than commonly assumed. The cryptosystem's security depends not only on factoring but also on proper implementation, key selection, and the use of appropriate padding schemes.

This analysis examines the formal security definitions, the mathematical foundations, known cryptanalytic attacks, and the essential padding mechanisms required for secure RSA usage. The goal is to provide a comprehensive understanding that enables informed decisions about RSA parameter selection and implementation choices.

## Mathematical Foundations

### The RSA Problem and Its Relationship to Factoring

The RSA problem is defined as follows: given a composite integer $n = pq$ where $p$ and $q$ are distinct large primes, a public exponent $e$, and a ciphertext $c \equiv m^e \pmod{n}$, compute the plaintext $m$. This problem is believed to be computationally hard, but its precise relationship to integer factorization has been a subject of extensive research.

**Theorem 1**: If an adversary can efficiently factor the RSA modulus $n$, then they can break RSA completely by computing the private exponent $d$.

_Proof_: Given $n = pq$, the adversary computes $\phi(n) = (p-1)(q-1) = pq - p - q + 1$. Using the extended Euclidean algorithm, the adversary finds $d$ such that $ed \equiv 1 \pmod{\phi(n)}$. This $d$ is the private exponent satisfying $m^{ed} \equiv m \pmod{n}$ for all $m$ by Euler's theorem. The adversary can then decrypt any ciphertext using $c^d \pmod{n}$. $\square$

The converse—whether breaking RSA is equivalent to factoring—remains an open question. However, under certain conditions, a reduction can be established. If the RSA problem is easy, then factoring is also easy in certain scenarios.

**Theorem 2** (Boneh et al.): If an adversary can recover even a single bit of the plaintext from the ciphertext for a fixed public exponent $e$ with non-negligible probability, then the adversary can factor $n$ with high probability.

This result establishes that breaking RSA (even partially) is computationally equivalent to factoring under standard assumptions. The proof relies on constructing a decision algorithm that distinguishes quadratic residues, which can be used to extract the prime factors.

### Key Generation and Security Parameters

The security of RSA fundamentally depends on the difficulty of factoring the modulus $n$. The best known factoring algorithm for large integers is the General Number Field Sieve (GNFS), whose complexity is sub-exponential but super-polynomial:

$$L_n\left[\frac{1}{3}, \sqrt[3]{\frac{64}{9}}\right] \approx \exp\left(\left(\sqrt[3]{\frac{64}{9}} + o(1)\right)(\ln n)^{1/3}(\ln\ln n)^{2/3}\right)$$

Current security standards recommend minimum key sizes based on this complexity. For RSA, a 2048-bit modulus provides approximately 112 bits of security, while a 4096-bit modulus provides approximately 140 bits. These recommendations account for advances in factoring algorithms and computing power.

**Key Generation Requirements**:

- Both primes $p$ and $q$ should be of similar bit-length (within a few digits) to maximize the difficulty of factoring algorithms
- The primes should be randomly generated using a cryptographically secure random number generator
- The primes should not be "weak"—they should not share small factors with $e$ or satisfy special mathematical relationships
- The private exponent $d$ should be large (specifically, $d > n^{1/4}$ to resist Wiener's attack)

## Known Attacks on RSA

### Classical Cryptanalytic Attacks

**Wiener's Attack**: This attack exploits small private exponents. Wiener's theorem states that if $d < n^{1/4}$, the private exponent can be recovered from the public key $(e, n)$ using continued fractions.

_Proof Sketch_: From $ed \equiv 1 \pmod{\phi(n)}$, we have $ed - k\phi(n) = 1$ for some integer $k$. Dividing by $d\phi(n)$ gives $\frac{e}{\phi(n)} - \frac{k}{d} = \frac{1}{d\phi(n)}$. Since $\phi(n) = n - p - q + 1$ and $p + q$ is much smaller than $n$, $\frac{e}{d}$ is a close approximation to $\frac{k}{\phi(n)}$. Using the theory of continued fractions, one can recover $\frac{k}{d}$ from $\frac{e}{n}$, and subsequently compute $\phi(n)$ and $d$.

**Håstad's Broadcast Attack**: If the same message $m$ is encrypted to $e$ different recipients using the same public exponent $e$ (typically $e = 3$) but different moduli $n_i$, and all ciphertexts are available, the Chinese Remainder Theorem can recover $m$ directly when $e$ ciphertexts are available. This attack demonstrates the danger of using small public exponents without proper padding.

**Low Exponent Attacks**: Using small public exponents (like $e = 3$) without padding leads to vulnerabilities. If $m^e < n$, then $c = m^e$ directly, and taking the $e$-th root reveals $m$. The Cube Root Attack extends this to cases where $m^e$ is slightly larger than $n$.

### Side-Channel Attacks

Implementation vulnerabilities can compromise RSA even when the mathematical structure is sound:

**Timing Attacks**: These attacks exploit variations in computation time during modular exponentiation. The standard left-to-right binary exponentiation method leaks information about the private key through timing differences. The attack can recover the entire private key bit-by-bit by measuring execution times for different ciphertexts.

_Countermeasure_: Use constant-time modular exponentiation algorithms or implement blinding techniques where a random value is multiplied with the ciphertext before decryption.

**Power Analysis Attacks**: Differential Power Analysis (DPA) and Simple Power Analysis (SPA) measure power consumption during cryptographic operations. Patterns in power consumption can reveal key bits, particularly during the modular exponentiation process.

_Countermeasure_: Use power-analysis-resistant implementations, randomize execution order, or employ hardware countermeasures.

**Fault Injection Attacks**: Inducing computational faults during decryption can leak information about the private key. The Bellcore attack demonstrates how a single faulty signature reveals the private key through gcd computation.

## Padding Schemes and Their Security

### Why Padding is Essential

Raw RSA encryption ($c = m^e \pmod{n}$) is not IND-CPA secure. An adversary can perform deterministic encryption oracle attacks. More critically, RSA without padding is vulnerable to chosen ciphertext attacks. Therefore, all modern RSA standards require padding for both encryption and signatures.

### OAEP (Optimal Asymmetric Encryption Padding)

OAEP provides IND-CPA secure encryption and is the standard padding scheme for RSA encryption (RSA-OAEP). It uses a trapdoor permutation with the following structure:

```
         n bits
    ┌──────────────┐
    │   M || G    │  (message || garbage)
    │    k₁ │ k₀  │
    └────┬───────┘
         │
         ▼
    ┌──────────────┐
    │   X = M⊕G   │  ← hash output masked
    │   Y = G⊕H(X)│  ← hash of X masked
    └────┬───────┘
         │
         ▼
    RSA encryption: c = (X||Y)^e mod n
```

**Security Proof Outline**: OAEP's security can be proven under the RSA assumption and the random oracle model. The proof involves showing that any adversary breaking IND-CPA security can be used to break the underlying RSA problem or find collisions in the hash functions. The transformation from a basic RSA trapdoor permutation to OAEP provides semantic security against chosen plaintext attacks.

### PSS (Probabilistic Signature Scheme)

For RSA signatures, PSS provides provable security in the random oracle model. PSS was standardized by RSA Laboratories and later adopted in PKCS#1 v2.1. It incorporates cryptographic hashing and salt to provide existential unforgeability under chosen message attacks (EUF-CMA).

### PKCS#1 v1.5 Padding

Despite known vulnerabilities to Bleichenbacher's chosen ciphertext attack, PKCS#1 v1.5 remains widely deployed. The attack exploits the specific error messages returned by servers during TLS handshakes. Modern implementations use countermeasures like random padding, error message standardization, and DSA/ECDSA alternatives.

## Implementation Security

### Key Size Selection Guidelines

| Security Level | RSA Key Size | Equivalent Symmetric | Recommendation |
| -------------- | ------------ | -------------------- | -------------- |
| Legacy         | 1024 bits    | 80 bits              | Discontinue    |
| Standard       | 2048 bits    | 112 bits             | Current use    |
| High           | 3072 bits    | 128 bits             | Long-term      |
| Very High      | 4096 bits    | 140 bits             | Extended       |

### Common Implementation Mistakes

1. **Using deterministic encryption**: Failing to incorporate random padding allows pattern recognition
2. **Not validating padding**: Insufficient validation enables oracle attacks
3. **Weak random number generation**: Compromised PRNGs undermine all cryptographic security
4. **Ignoring error side-channels**: Detailed error messages leak information
5. **Improper key generation**: Biased or predictable primes enable factorization

## Exam Tips

1. **Key Relationship**: Remember that factoring implies breaking RSA, but the converse is not proven. Focus on understanding the conditions under which RSA security reduces to factoring.

2. **Attack Prerequisites**: For each attack (Wiener's, Håstad's, timing attacks), clearly identify the conditions required for the attack to succeed. Wiener's attack specifically requires $d < n^{1/4}$.

3. **Padding is Mandatory**: Never suggest using raw RSA for encryption. Be prepared to explain why OAEP and PSS are necessary and how they provide security.

4. **Side-Channel Countermeasures**: Understand not just the attacks but their specific countermeasures—blinding, constant-time operations, power analysis resistance.

5. **Security Proofs**: Be able to sketch the proof that factoring enables breaking RSA, and understand the high-level proof structure for OAEP security.

6. **Parameter Selection**: Know why $p$ and $q$ should be similar size, why $d$ must be large, and why small $e$ without padding is dangerous.

7. **Attack Complexity**: Associate each attack with its complexity class and the mathematical principle it exploits (continued fractions for Wiener, CRT for Håstad's).
