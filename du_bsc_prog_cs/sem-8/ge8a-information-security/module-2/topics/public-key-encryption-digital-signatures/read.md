# Public-Key Encryption and Digital Signatures

## Introduction

Public-key cryptography represents one of the most profound innovations in the history of information security, fundamentally transforming how we protect digital communications. Unlike symmetric cryptography, where the same key is used for both encryption and decryption, public-key cryptography employs a pair of mathematically related keys: a public key for encryption (or signature verification) and a private key for decryption (or signature creation). This elegant solution addresses the critical key distribution problem that plagued symmetric cryptography for centuries.

The concept was first proposed by Whitfield Diffie and Martin Hellman in 1976, revolutionizing the field of cryptography. Their groundbreaking paper "New Directions in Cryptography" introduced the notion of asymmetric cryptography and the concept of digital signatures. This breakthrough enabled secure communication between parties who had never met or shared a secret key beforehand, making modern e-commerce, online banking, and secure messaging possible.

Digital signatures, built upon public-key cryptographic principles, provide authentication, integrity, and non-repudiation in digital communications. When you sign a digital document, you use your private key to create a unique mathematical proof that only you could have generated. Anyone with access to your public key can verify that signature, confirming both your identity and that the document hasn't been altered. This mechanism forms the backbone of modern digital trust infrastructure, from SSL/TLS certificates securing websites to blockchain transactions.

## Key Concepts

### Public-Key Encryption Fundamentals

Public-key encryption, also known as asymmetric encryption, uses two mathematically related keys. The public key can be freely distributed and is used by anyone who wants to send you an encrypted message. The private key must be kept absolutely secret and is used to decrypt messages encrypted with your public key.

The security of public-key systems relies on computationally hard mathematical problems. The most widely used problem is integer factorization: given a large composite number, it's computationally infeasible to determine its prime factors. This forms the foundation of the RSA algorithm, named after its inventors Rivest, Shamir, and Adleman.

**Mathematical Foundation of RSA:**

The RSA algorithm operates as follows:

1. Select two large prime numbers, p and q
2. Compute n = p × q (the modulus)
3. Calculate φ(n) = (p-1)(q-1) (Euler's totient)
4. Choose an encryption exponent e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
5. Compute the decryption exponent d such that e × d ≡ 1 (mod φ(n))
6. Public key: (e, n), Private key: (d, n)

Encryption: C = M^e mod n
Decryption: M = C^d mod n

Where M is the plaintext message and C is the ciphertext.

### Digital Signatures

A digital signature is a mathematical scheme for verifying the authenticity and integrity of digital messages or documents. It provides three critical security properties:

1. **Authentication**: Confirms the identity of the signer
2. **Integrity**: Verifies the message hasn't been altered
3. **Non-repudiation**: The signer cannot deny having signed the document

**Digital Signature Process:**

The sender creates a hash of the message using a hash function (like SHA-256), then encrypts this hash with their private key. This encrypted hash, along with the original message, is sent to the recipient. The recipient decrypts the hash using the sender's public key, computes their own hash of the message, and compares the two hashes. If they match, the signature is valid.

### Hash Functions in Digital Signatures

Hash functions are crucial components in digital signature schemes. A cryptographic hash function takes an input of arbitrary length and produces a fixed-length output (hash or message digest). Key properties include:

- **One-way**: Computationally infeasible to reverse
- **Collision-resistant**: Difficult to find two different inputs producing the same hash
- **Deterministic**: Same input always produces same output
- **Avalanche effect**: Small changes in input produce significantly different outputs

Common hash functions include MD5 (deprecated due to vulnerabilities), SHA-1 (deprecated), SHA-256, and SHA-3.

### Public Key Infrastructure (PKI)

PKI is the framework of roles, policies, hardware, software, and procedures needed to create, manage, distribute, use, store, and revoke digital certificates and manage public-key encryption. It addresses the fundamental problem of binding public keys to entities (individuals, organizations, devices).

A Digital Certificate is an electronic document that uses a digital signature to bind a public key with an identity. The X.509 standard is the most common format for certificates, containing the holder's public key, identity information, and the certificate authority's digital signature.

Certificate Authorities (CAs) are trusted third parties that issue and manage digital certificates. When you visit a secure website, your browser verifies the server's certificate by checking if it was signed by a trusted CA in your root certificate store.

## Examples

### Example 1: RSA Encryption and Decryption

Let's work through a simplified RSA example with small prime numbers for illustration:

**Setup:**
- Select primes: p = 3, q = 11
- n = p × q = 33
- φ(n) = (3-1)(11-1) = 2 × 10 = 20
- Choose e = 3 (gcd(3, 20) = 1)
- Compute d: Find d such that 3 × d ≡ 1 (mod 20)
  - d = 7 (since 3 × 7 = 21 ≡ 1 mod 20)

**Public Key:** (e, n) = (3, 33)
**Private Key:** (d, n) = (7, 33)

**Encryption:**
Message M = 5
C = M^e mod n = 5^3 mod 33 = 125 mod 33 = 26

**Decryption:**
M = C^d mod n = 26^7 mod 33

Using modular exponentiation:
26^2 = 676 ≡ 16 mod 33
26^4 ≡ 16^2 = 256 ≡ 7 mod 33
26^7 = 26^4 × 26^2 × 26^1 ≡ 7 × 16 × 26 ≡ 7 × 416 ≡ 7 × 2 ≡ 14 mod 33

Wait, let me recalculate: 26^1 ≡ 26
7 × 16 = 112 ≡ 13 mod 33
13 × 26 = 338 ≡ 5 mod 33

Decrypted message = 5 ✓ (matches original)

### Example 2: Digital Signature Creation and Verification

**Scenario:** Alice wants to sign a message "PAY 1000" to send to Bob.

**Step 1: Hash the message**
Using SHA-256 (simplified representation):
Hash("PAY 1000") = h = a1b2c3d4... (256-bit value)

**Step 2: Sign with private key**
Alice's private key: d = 7, n = 33 (from Example 1)
Signature = h^d mod n = a1b2c3d4...^7 mod 33

**Step 3: Send message + signature to Bob**

**Verification at Bob's end:**
- Bob receives message "PAY 1000" and signature
- Bob computes his own hash of the message
- Bob uses Alice's public key (e=3, n=33) to decrypt the signature
- If decrypted hash equals computed hash, signature is valid

### Example 3: Real-World Application - HTTPS

When you visit https://www.example.com:

1. Browser initiates connection to the server
2. Server sends its digital certificate containing its public key
3. Browser verifies the certificate (checks CA signature, validity dates, domain name)
4. Browser generates a random symmetric session key
5. Browser encrypts this session key with the server's public key
6. Server decrypts using its private key to obtain the session key
7. Both parties now share a symmetric key for efficient bulk encryption of data

This hybrid approach combines the advantages of both asymmetric (secure key exchange) and symmetric (fast encryption) cryptography.

## Exam Tips

1. **Understand the difference between public and private keys**: Remember that the public key encrypts/verifies while the private key decrypts/signs. This is a frequently tested concept.

2. **RSA security relies on integer factorization**: Know that the security of RSA depends on the computational difficulty of factoring large composite numbers into their prime factors.

3. **Digital signatures provide non-repudiation**: Unlike symmetric authentication, digital signatures allow a third party to verify who signed the document, making it legally binding in many jurisdictions.

4. **Hash functions are essential in digital signatures**: Digital signatures are applied to the hash of the message, not the message itself, for efficiency and security reasons.

5. **Key sizes matter**: Modern RSA uses 2048-bit or 4096-bit keys. 1024-bit keys are considered insecure. This is important for exam questions on security strength.

6. **PKI solves the key distribution problem**: In exam questions, when asked about trust models and certificate verification, remember that CAs create a chain of trust from root certificates.

7. **Hybrid cryptography in practice**: Real systems use public-key encryption only for key exchange, then use symmetric encryption for bulk data. Know why (public-key is slower).

8. **Common vulnerabilities**: Be aware of practical attacks like man-in-the-middle (mitigated by certificates), chosen ciphertext attacks, and the importance of proper padding (OAEP, PKCS#1).