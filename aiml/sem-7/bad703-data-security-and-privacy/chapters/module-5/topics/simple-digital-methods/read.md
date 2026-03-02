# Module 5: Simple Digital Methods for Data Security

## Introduction

In the digital age, protecting data from unauthorized access and modification is paramount. While complex cryptographic systems exist, many foundational security mechanisms are built upon simpler digital methods. This module explores these fundamental techniques, which form the building blocks for more advanced data security and privacy protocols. Understanding these methods is crucial for any engineer designing or implementing secure systems.

## Core Concepts

### 1. Hashing

A **hash function** is a one-way mathematical algorithm that takes an input (or 'message') of any length and returns a fixed-size string of bytes, known as the **hash value** or **digest**. The key properties of a cryptographic hash function are:

*   **Deterministic:** The same input will always produce the same hash.
*   **Fast to Compute:** The hash value can be calculated quickly.
*   **Pre-image Resistance (One-Way):** It is computationally infeasible to reverse the function and generate the original input from its hash value.
*   **Small Change, Big Difference (Avalanche Effect):** A tiny change in the input (even a single bit) should produce a drastically different hash value.
*   **Collision Resistance:** It is extremely difficult to find two different inputs that produce the same hash output.

**Common Algorithms:** MD5 (now considered broken), SHA-1 (deprecated), SHA-256, and SHA-3.

**Example:**
The SHA-256 hash of the word `hello` is:
`2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824`

If we change it to `Hello` (capital 'H'), the hash becomes completely different:
`185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`

**Application:** Hashing is primarily used for **data integrity verification**. For instance, when you download software, the website often provides a hash of the file. After downloading, you can generate a hash of your local file and compare it to the provided one. If they match, you can be confident the file was not corrupted or tampered with during transfer.

### 2. Message Authentication Code (MAC)

A **Message Authentication Code** is a cryptographic checksum used to provide both **data integrity** and **authenticity**. It proves that a message originated from the claimed sender (authenticity) and that it was not altered in transit (integrity).

A MAC requires a **secret key** shared between the sender and receiver.
1.  The sender computes the MAC of the message using the shared secret key.
2.  The sender transmits both the message and the MAC.
3.  The receiver independently computes the MAC of the received message using the same secret key.
4.  The receiver compares the computed MAC with the received MAC. If they match, the message is verified.

**How it differs from a simple hash:** A hash alone only verifies integrity. An attacker could alter the message *and* replace the hash. With a MAC, the attacker cannot generate a valid MAC without knowing the secret key.

**Common Types:** HMAC (Hash-based MAC), which uses a cryptographic hash function (like SHA-256) combined with a secret key.

### 3. Digital Signatures

A **digital signature** is a cryptographic technique that provides an even stronger form of authentication and non-repudiation than a MAC. While a MAC uses a symmetric (shared) key, a digital signature uses **asymmetric cryptography** (a public-key cryptosystem).

The process involves a key pair:
*   A **private key**, known only to the signer.
*   A **public key**, which is distributed openly.

**How it works:**
1.  **Signing:** The sender generates a hash of the message and then **encrypts that hash** with their **private key**. This encrypted hash is the digital signature, which is appended to the message.
2.  **Verification:** The receiver decrypts the signature using the sender's **public key** to retrieve the original hash. The receiver then independently hashes the received message. If the two hashes match, it verifies that the message was signed by the holder of the private key and was not altered.

**Application:** Digital signatures are used in software distribution, financial transactions, and legally binding e-documents. They provide **non-repudiation**, meaning the signer cannot later deny having signed the message.

---

## Key Points & Summary

| Method | Primary Purpose | Cryptography Type | Key Feature |
| :--- | :--- | :--- | :--- |
| **Hashing** | **Data Integrity** | None (One-way function) | Creates a unique fingerprint for data. Cannot be reversed. |
| **MAC** | **Integrity & Authenticity** | Symmetric (Secret Key) | Uses a shared secret key to verify the source and content of a message. |
| **Digital Signature** | **Integrity, Authenticity & Non-Repudiation** | Asymmetric (Public/Private Key) | Uses a private key to sign and a public key to verify. Provides legal non-repudiation. |

*   **Hashing** is a one-way function used to verify that data has not been accidentally altered.
*   **MAC** uses a shared secret key to verify both the integrity and the authenticity of a message.
*   **Digital Signatures** use public-key cryptography to provide integrity, authenticity, and the crucial property of **non-repudiation**, where the signer cannot deny their involvement.

These simple digital methods are the fundamental components upon which secure communication protocols (like SSL/TLS), authentication systems, and digital trust models are built.