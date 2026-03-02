# Computational Aspects in Cryptography & Network Security


## Table of Contents

- [Computational Aspects in Cryptography & Network Security](#computational-aspects-in-cryptography--network-security)
- [Introduction](#introduction)
- [Core Concepts](#core-concepts)
  - [1. Computational Complexity & "Hard" Problems](#1-computational-complexity--hard-problems)
  - [2. Efficiency of Cryptographic Operations](#2-efficiency-of-cryptographic-operations)

## Introduction

Cryptography is not just a theoretical science; its practical application relies heavily on computational feasibility. This module explores the **computational aspects** that underpin modern cryptographic algorithms. We will examine why certain mathematical problems are considered "hard" and are suitable for building secure systems, and how the efficiency of algorithms for encryption, decryption, and key generation directly impacts real-world security implementations.

## Core Concepts

### 1. Computational Complexity & "Hard" Problems

The security of most asymmetric (public-key) cryptosystems is based on the concept of **one-way functions**. These are functions that are easy to compute in one direction but computationally infeasible to reverse without special information (a trapdoor).

- **Easy to Compute:** Forward computation (e.g., multiplying two large primes) is fast.
- **Hard to Invert:** Reverse computation (e.g., factoring the resulting large product) is, for all known algorithms, incredibly slow for large numbers.

The study of how the time and resources needed to solve a problem grow as the input size increases is called **computational complexity**. Problems are classified into classes like P (solvable in polynomial time) and NP (verifiable in polynomial time). Cryptographic security often relies on problems believed to be outside of P.

**Key "Hard" Problems:**

- **Integer Factorization Problem (IFP):** Basis for **RSA**. Given a large composite number `n = p * q` (where `p` and `q` are large primes), finding `p` and `q` is computationally infeasible.
- **Discrete Logarithm Problem (DLP):** Basis for **Diffie-Hellman** and **DSA**. Given `g`, `y`, and `p` (a prime), finding the exponent `x` in `y = g^x mod p` is extremely difficult.
- **Elliptic Curve Discrete Logarithm Problem (ECDLP):** A more complex variant of DLP that allows for smaller keys with equivalent security, used in **ECC**.

### 2. Efficiency of Cryptographic Operations

The practical deployment of cryptography depends on the efficiency of its operations:

- **Encryption/Decryption Speed:** Symmetric algorithms like AES are designed to be very fast for bulk data encryption. Asymmetric algorithms are slower and are typically used for securely establishing symmetric session keys (e.g., in SSL/TLS).
- **Key Generation:** Generating strong, random keys (and primes for RSA) must be efficient but also secure.
- **Digital Signature Generation/Verification:** Signing a message should be efficient, and verification (which might be done by many parties) should be even faster.

**Example: RSA Encryption/Decryption**
The core operations are modular exponentiation: `C = M^e mod n` (encryption) and `M = C^d mod n` (decryption). While exponentiation seems slow, algorithms like **Square-and-Multiply** make it efficient by breaking the exponentiation into a series of squarings and multiplications modulo `n`.
