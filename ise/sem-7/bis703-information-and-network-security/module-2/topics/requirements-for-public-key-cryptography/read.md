# Requirements for Public Key Cryptography


## Table of Contents

- [Requirements for Public Key Cryptography](#requirements-for-public-key-cryptography)
- [Introduction](#introduction)
- [Fundamental Requirements](#fundamental-requirements)
  - [1. Computational Ease of Key Pair Generation](#1-computational-ease-of-key-pair-generation)
  - [2. Computational Ease of Encryption](#2-computational-ease-of-encryption)
  - [3. Computational Ease of Decryption](#3-computational-ease-of-decryption)
  - [4. Computational Infeasibility of Determining Private Key from Public Key](#4-computational-infeasibility-of-determining-private-key-from-public-key)
  - [5. Computational Infeasibility of Recovering Plaintext from Ciphertext](#5-computational-infeasibility-of-recovering-plaintext-from-ciphertext)
  - [6. Optional but Useful: Either Key Can Be Used for Encryption](#6-optional-but-useful-either-key-can-be-used-for-encryption)
- [Summary Table of Requirements](#summary-table-of-requirements)
- [Computational Feasibility vs Infeasibility](#computational-feasibility-vs-infeasibility)
  - [What Does "Computationally Easy" Mean?](#what-does-computationally-easy-mean)
  - [What Does "Computationally Infeasible" Mean?](#what-does-computationally-infeasible-mean)
- [Practical Implications](#practical-implications)
  - [For RSA (Meeting All Requirements)](#for-rsa-meeting-all-requirements)
  - [For Diffie-Hellman (Key Exchange)](#for-diffie-hellman-key-exchange)
- [Security Considerations](#security-considerations)
  - [What If Requirements Are Violated?](#what-if-requirements-are-violated)
  - [Key Sizes and Requirements](#key-sizes-and-requirements)
- [Conclusion](#conclusion)

## Introduction

Public key cryptography (asymmetric cryptography) was a revolutionary breakthrough when introduced by Diffie and Hellman in 1976. However, for a public key cryptosystem to be practical and secure, it must satisfy several critical requirements. Understanding these requirements is essential for evaluating, implementing, and deploying public key systems.

## Fundamental Requirements

For a public key cryptographic system to be viable, it must meet the following essential conditions:

### 1. Computational Ease of Key Pair Generation

**Requirement**: It must be computationally easy for a user to generate a pair of keys (public key KU and private key KR).

**Why This Matters**:

- Users need to generate keys quickly without specialized hardware
- Key generation happens frequently (user registration, key rotation, etc.)
- Should work on standard computers in reasonable time

**Example in RSA**:

- Generating a 2048-bit RSA key pair takes milliseconds on modern hardware
- Involves finding two large primes, which is efficient with probabilistic primality tests

**Failure Scenario**: If key generation took hours or required supercomputers, the system would be impractical for widespread use.

---

### 2. Computational Ease of Encryption

**Requirement**: It must be computationally easy for a sender, knowing the public key and the message to be encrypted, to generate the corresponding ciphertext.

**Mathematical Expression**:

- C = E(KU, M)
- Where C is ciphertext, M is plaintext, KU is public key, E is encryption function

**Why This Matters**:

- Encryption is a public operation, performed by anyone
- Must be fast enough for real-time communication
- Should not require excessive computational resources

**Example in RSA**:

- Encryption: C = M^e mod n
- With small public exponent (e = 65537), encryption is very fast
- Modular exponentiation can be done efficiently

**Performance**: RSA encryption with 2048-bit keys takes microseconds.

---

### 3. Computational Ease of Decryption

**Requirement**: It must be computationally easy for the receiver, knowing the private key and the ciphertext, to recover the original plaintext.

**Mathematical Expression**:

- M = D(KR, C)
- Where M is recovered plaintext, C is ciphertext, KR is private key, D is decryption function

**Why This Matters**:

- Legitimate recipient must be able to decrypt efficiently
- Decryption is performed frequently
- Should work on standard hardware

**Example in RSA**:

- Decryption: M = C^d mod n
- Even though d is large (1024+ bits), modular exponentiation is efficient
- Takes milliseconds on modern hardware

**Note**: Decryption is typically slower than encryption (due to larger exponent d vs small e), but still computationally feasible.

---

### 4. Computational Infeasibility of Determining Private Key from Public Key

**Requirement**: It must be computationally infeasible for an adversary, knowing the public key, to determine the private key.

**This is the Core Security Requirement!**

**Why This Matters**:

- Public key is published openly; anyone can access it
- If private key could be derived from public key, the entire system collapses
- Security depends on the computational asymmetry

**Example in RSA**:

- Public key: (e, n)
- Private key: (d, n)
- To find d from e and n, attacker must factor n = p × q
- Factoring large n is computationally infeasible (would take millions of years with current technology)

**Mathematical Basis**:

- RSA: Integer factorization problem
- DH/ElGamal: Discrete logarithm problem
- ECC: Elliptic curve discrete logarithm problem

**Security Margin**: With 2048-bit RSA, even with all computers on Earth working together for millions of years, factoring n is infeasible.

---

### 5. Computational Infeasibility of Recovering Plaintext from Ciphertext

**Requirement**: It must be computationally infeasible for an adversary, knowing the public key and a ciphertext, to recover the original plaintext.

**Why This Matters**:

- Attackers can intercept ciphertexts
- Public key is openly available
- System must remain secure even with both pieces of information

**Attack Scenario**:

- Attacker has: Public key (e, n) and ciphertext C
- Attacker wants: Original message M
- Without private key d, attacker cannot compute M = C^d mod n

**Why It's Hard**:

- This essentially reduces to requirement #4
- Without d, there's no efficient way to decrypt C
- Alternative attacks (factoring n, solving discrete log) are computationally infeasible

**Additional Protection**: Proper padding schemes (OAEP) prevent certain attacks even if some mathematical weaknesses exist.

---

### 6. Optional but Useful: Either Key Can Be Used for Encryption

**Requirement** (for some systems): The two keys can be used interchangeably—either can be used for encryption, with the other used for decryption.

**Mathematical Expression**:

- Encryption with public key: C = E(KU, M), Decryption: M = D(KR, C)
- OR
- Encryption with private key: C = E(KR, M), Verification: M = D(KU, C)

**Why This Matters**:

- Enables digital signatures (encrypt with private key, verify with public key)
- Provides authentication and non-repudiation
- Increases versatility of the cryptosystem

**Example in RSA**:

- Encryption: C = M^e mod n (using public key)
- Signature: S = M^d mod n (using private key)
- Both operations are mathematically symmetric

**Not All Systems Support This**: Some public key systems (like ElGamal encryption) don't have this property.

---

## Summary Table of Requirements

| Requirement                 | Operation              | Must Be                    | Why                                      |
| --------------------------- | ---------------------- | -------------------------- | ---------------------------------------- |
| 1. Key Generation           | Generate (KU, KR)      | Computationally Easy       | Users need to create keys quickly        |
| 2. Encryption               | C = E(KU, M)           | Computationally Easy       | Public operation, must be fast           |
| 3. Decryption               | M = D(KR, C)           | Computationally Easy       | Legitimate user must decrypt efficiently |
| 4. Private Key Security     | Derive KR from KU      | Computationally Infeasible | Core security requirement                |
| 5. Ciphertext Security      | Derive M from C and KU | Computationally Infeasible | Protects against eavesdroppers           |
| 6. Reversibility (optional) | Use either key first   | Either direction works     | Enables signatures                       |

---

## Computational Feasibility vs Infeasibility

### What Does "Computationally Easy" Mean?

An operation is computationally easy if it can be performed efficiently with available computing resources:

- **Polynomial time complexity**: O(n), O(n²), O(n³), O(n log n)
- **Practical time**: Milliseconds to seconds
- **Examples**: Modular exponentiation, primality testing (probabilistic)

### What Does "Computationally Infeasible" Mean?

An operation is computationally infeasible if it cannot be completed in reasonable time even with massive computing resources:

- **Exponential or sub-exponential complexity**: O(2^n), O(e^(n^1/3))
- **Impractical time**: Millions of years
- **Examples**: Factoring large composites, discrete logarithm problem

**Key Insight**: Public key cryptography exploits the gap between easy (polynomial) and infeasible (exponential) operations.

---

## Practical Implications

### For RSA (Meeting All Requirements)

✓ **Key Generation**: Fast with probabilistic primality testing (Miller-Rabin)
✓ **Encryption**: Fast with small e (65537)
✓ **Decryption**: Feasible with efficient modular exponentiation
✓ **Private Key Security**: Factoring large n is infeasible
✓ **Ciphertext Security**: Without d, decryption is infeasible
✓ **Reversibility**: RSA supports both encryption and signatures

### For Diffie-Hellman (Key Exchange)

✓ **Key Generation**: Fast modular exponentiation
✓ **Public Key Computation**: Fast
✓ **Shared Secret**: Fast for legitimate parties
✓ **Private Key Security**: Discrete log problem is infeasible
✗ **Not designed for encryption**: DH is for key exchange, not message encryption

---

## Security Considerations

### What If Requirements Are Violated?

**If Key Generation Is Too Slow**: System unusable in practice

**If Encryption/Decryption Is Too Slow**: Not practical for real-time communication; hybrid systems (RSA + AES) solve this

**If Private Key Can Be Derived**: Complete system compromise; all encrypted messages can be read, signatures can be forged

**If Ciphertext Can Be Decrypted**: Confidentiality is lost; equivalent to breaking requirement #4

### Key Sizes and Requirements

To maintain "computational infeasibility" as computers get faster:

- 1990s: 512-bit RSA adequate → Now broken
- 2000s: 1024-bit RSA standard → Now marginal
- 2020s: 2048-bit RSA minimum, 4096-bit recommended

Requirements must be re-evaluated as:

- Computing power increases
- New algorithms are discovered
- Quantum computers develop

---

## Conclusion

The six requirements for public key cryptography establish a careful balance:

- Legitimate operations (key generation, encryption, decryption) must be **computationally easy**
- Adversarial operations (deriving private key, breaking ciphertext) must be **computationally infeasible**

This asymmetry—easy for authorized users, infeasible for attackers—is the foundation of all public key cryptosystems. Systems like RSA, Diffie-Hellman, and Elliptic Curve Cryptography meet these requirements through clever use of mathematical one-way functions (factorization, discrete logarithm, ECDLP) that are easy to compute in one direction but infeasible to reverse.
