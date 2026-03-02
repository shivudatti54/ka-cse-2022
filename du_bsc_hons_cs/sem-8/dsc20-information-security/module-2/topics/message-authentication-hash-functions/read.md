# Message Authentication and Hash Functions

## Introduction

In the digital age, ensuring the integrity and authenticity of messages is paramount for secure communication. When you send a message over the internet, how do you guarantee that it hasn't been tampered with during transmission? How can the recipient verify that the message truly came from the claimed sender? These critical questions are addressed by **Message Authentication** and **Hash Functions** — fundamental concepts in information security that form the backbone of modern cryptographic protocols.

Message authentication is a mechanism that allows the recipient to verify that a message originated from the claimed sender and was not modified in transit. Unlike confidentiality (which protects message content from eavesdroppers), authentication focuses on verifying the source and integrity of data. Hash functions serve as the mathematical engines driving many authentication schemes, providing a compact digital fingerprint of data that changes dramatically even if a single bit is modified.

This topic is essential not only for theoretical understanding but also for practical applications: secure banking transactions, digital signatures, blockchain technology, software updates verification, and password storage all rely on the principles of message authentication and cryptographic hash functions. For DU students preparing for careers in cybersecurity or software development, mastering these concepts is indispensable.

## Key Concepts

### 1. Message Authentication Code (MAC)

A **Message Authentication Code (MAC)** is a small piece of information attached to a message that allows recipients to verify both the integrity and the authenticity of the message. The key property of a MAC is that it can only be generated and verified by parties who share a secret key.

The process works as follows: The sender computes a MAC value using the message and a secret key, then sends both the message and the MAC to the recipient. The recipient, possessing the same secret key, recomputes the MAC on the received message. If the computed MAC matches the received MAC, the recipient can be confident that:
- The message has not been altered (integrity)
- The message was created by someone possessing the secret key (authenticity)

**Mathematical definition**: A MAC is a function MAC: K × M → T, where K is the key space, M is the set of possible messages, and T is the set of possible tags (typically a fixed-length string).

### 2. Properties of Cryptographic Hash Functions

A **cryptographic hash function** H takes an input (or 'message') of arbitrary length and produces a fixed-length output called the **hash value**, **digest**, or **fingerprint**. For a hash function to be cryptographically secure, it must satisfy these essential properties:

**Pre-image Resistance**: Given a hash value h, it should be computationally infeasible to find any message m such that H(m) = h. This property ensures one-wayness.

**Second Pre-image Resistance**: Given a message m1, it should be computationally infeasible to find a different message m2 such that H(m1) = H(m2). This prevents attackers from creating alternative messages with the same hash.

**Collision Resistance**: It should be computationally infeasible to find any two distinct messages m1 and m2 such that H(m1) = H(m2). This is the strongest property and implies second pre-image resistance.

### 3. Hash Function Structures

Most modern cryptographic hash functions use the **Merkle-Damgård construction**, named after Ralph Merkle and Ivan Damgård. In this structure:
- The input message is padded to a multiple of a fixed block size
- The message is divided into blocks
- A compression function f processes each block along with an intermediate hash value
- The final output is the last intermediate value

The **SHA (Secure Hash Algorithm)** family, particularly SHA-256 and SHA-3, exemplifies this construction and is widely used in modern security protocols.

### 4. HMAC (Hash-based Message Authentication Code)

**HMAC** provides a mechanism for message authentication using a cryptographic hash function and a secret key. The strength of HMAC lies in its security proof, which shows that the security of HMAC depends on the security properties of the underlying hash function.

The HMAC algorithm is defined as:
```
HMAC(K, m) = H((K ⊕ opad) || H((K ⊕ ipad) || m))
```

Where:
- K is the secret key
- m is the message
- ipad and opad are inner and outer padding constants
- ⊕ denotes XOR
- || denotes concatenation

### 5. The Birthday Attack

One of the most fascinating aspects of hash function security is the **Birthday Attack**, which exploits the birthday paradox from probability theory. The birthday paradox states that in a group of just 23 people, there's a greater than 50% chance that two people share a birthday.

Applied to hash functions with an n-bit output, this means that instead of needing to try 2^n possibilities to find a collision (as might be expected), an attacker only needs approximately 2^(n/2) attempts. This is why:
- A 128-bit hash (like MD5) requires only about 2^64 attempts to find a collision — now considered feasible
- A 256-bit hash (like SHA-256) requires about 2^128 attempts — still computationally secure

This is why collision resistance requires hash outputs sufficiently large to make birthday attacks impractical.

### 6. Digital Signatures

While MACs provide authentication using symmetric keys (shared secret), **digital signatures** use asymmetric cryptography to provide authentication with non-repudiation. With digital signatures:
- The sender signs the message using their private key
- Anyone can verify the signature using the sender's public key
- Only the holder of the private key could have created the signature (non-repudiation)

Digital signature schemes like **RSA signature** and **DSA (Digital Signature Algorithm)** rely on hash functions to efficiently sign messages of arbitrary length.

## Examples

### Example 1: Verifying Message Integrity with a Simple Hash

Consider a software company releasing an update file "update.exe" with SHA-256 hash: `a7f8... (64 hex characters)`.

**Scenario**: You download the file. How do you verify its integrity?

**Solution**: You compute the SHA-256 hash of your downloaded file and compare it to the published hash:
```python
import hashlib

def verify_file(filename, expected_hash):
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    computed = sha256_hash.hexdigest()
    return computed == expected_hash
```

If even one bit of the file is corrupted or modified by an attacker, the hash will change completely, alerting you to the tampering.

### Example 2: Computing HMAC for Authentication

Suppose Alice needs to send an authenticated message to Bob, sharing secret key `secret123`.

**Message**: "Transfer $1000 to account 98765"

**HMAC-SHA256 Computation**:
```python
import hmac
import hashlib

key = b"secret123"
message = b"Transfer $1000 to account 98765"

mac = hmac.new(key, message, hashlib.sha256).hexdigest()
print(f"HMAC: {mac}")
# Output: 3b5a8c7f2e9d1b4a6c8f0e2d5a7b3c9e1f4d6a8b2c5e7f9a1d3b5c7e9f2a4
```

Bob, possessing the same key, can independently compute the HMAC and verify both integrity and authenticity. If an attacker intercepts and modifies the message, the HMAC will not match.

### Example 3: Birthday Attack Calculation

**Problem**: How many messages must an attacker try to find two messages with the same 64-bit hash with 50% probability?

**Solution**: Using the birthday approximation:
n = 2^(k/2) where k = number of bits

For k = 64: n ≈ 2^32 ≈ 4.3 billion messages

This is computationally feasible for a well-funded attacker, demonstrating why 64-bit hashes are insecure. Modern standards require at least 128-bit outputs (SHA-256 provides 256 bits), making birthday attacks requiring 2^128 operations — practically impossible.

## Exam Tips

1. **Distinguish between MAC and Digital Signatures**: Remember that MAC uses symmetric keys (shared secret) and provides authentication but not non-repudiation, while digital signatures use asymmetric keys (private/public) and provide non-repudiation.

2. **Memorize hash function properties**: The three properties — pre-image resistance, second pre-image resistance, and collision resistance — are frequently tested. Know the differences between them.

3. **Birthday attack significance**: Understand that collisions can be found in approximately 2^(n/2) attempts for an n-bit hash. This is why MD5 (128-bit) is broken but SHA-256 remains secure.

4. **HMAC structure**: Be able to explain the double-hashing and use of two different paddings (ipad and opad) in HMAC. This provides security against certain attacks.

5. **Hash vs. MAC**: A hash alone doesn't provide authentication because anyone can compute it. MAC requires a secret key, providing authenticity.

6. **MD5 vulnerabilities**: While historically popular, MD5 is now considered completely broken for collision resistance. Know why (chosen-prefix collisions, etc.).

7. **Applications knowledge**: Be prepared to explain real-world applications like password storage (don't store passwords, store salted hashes), blockchain (proof-of-work uses hash puzzles), and file integrity verification.

8. **SHA family differences**: Know the progression from SHA-1 (160-bit, weakened) to SHA-256/384/512 (part of SHA-2 family) to SHA-3 (based on Keccak algorithm, different structure).