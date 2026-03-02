# Principles of Public Key Cryptosystems

## Introduction

Public key cryptography represents a fundamental paradigm shift in cryptographic practice, introducing the revolutionary concept of asymmetric encryption where the encryption and decryption keys are distinct. Unlike symmetric cryptography, which relies on a shared secret key, public key cryptosystems employ a pair of mathematically related keys: a public key that can be freely distributed and used for encryption or signature verification, and a private key that must remain confidential and is used for decryption or signature generation. This asymmetry addresses the critical key distribution problem inherent in symmetric systems and enables new cryptographic capabilities such as digital signatures and key exchange protocols.

The mathematical foundations of public key cryptography rest upon computational problems that are believed to be intractable for classical computers, including integer factorization, discrete logarithm computation, and elliptic curve discrete logarithm problems. These problems exhibit a crucial property: while they are computationally hard to solve in the forward direction, they become efficiently solvable when additional mathematical information (the trapdoor) is known. This asymmetry in computational complexity is what makes public key cryptosystems both possible and secure.

## Key Concepts

### The Asymmetric Key Pair

A public key cryptosystem operates using two mathematically related keys generated simultaneously through a key generation algorithm. The public key (e, n) in RSA, for instance, consists of a modulus n (the product of two large primes) and a public exponent e, while the corresponding private key (d, n) comprises the same modulus and a private exponent d. The mathematical relationship between e and d is such that encryption followed by decryption (or vice versa) restores the original message, but computing d from e and n is computationally infeasible without knowledge of the prime factorization of n.

**Key Generation Process:** The process of generating key pairs involves selecting appropriate cryptographic parameters. For RSA, this includes generating two large prime numbers p and q of approximately equal length, computing n = pq, and selecting an encryption exponent e that is coprime to φ(n) = (p-1)(q-1). The private exponent d is then computed as the modular multiplicative inverse of e modulo φ(n). The security of RSA fundamentally depends on the difficulty of factoring n back into its prime components.

### One-Way Functions and Trapdoor Properties

The security of public key cryptosystems relies on one-way functions—mathematical transformations that are easy to compute in one direction but computationally infeasible to invert without additional information. A trapdoor one-way function is a special type that becomes easy to invert when a specific piece of secret information (the trapdoor) is known. Formally, a function f: {0,1}_ → {0,1}_ is a one-way function if there exists a polynomial-time algorithm to compute f(x) for any x, but for every probabilistic polynomial-time algorithm A, the probability that A inverts f(y) on a random y in the range of f is negligible.

In RSA, the one-way function f(x) = x^e mod n is easy to compute but hard to invert without knowing d. However, with the trapdoor d, the inverse function f⁻¹(y) = y^d mod n can be computed efficiently. This trapdoor property is essential—it enables the legitimate owner to decrypt messages or create signatures while preventing adversaries from doing the same.

### Confidentiality and Authentication

Public key cryptography provides two fundamental security services: confidentiality and authentication. Confidentiality is achieved through encryption: the sender uses the recipient's public key to encrypt the message, ensuring that only the recipient, possessing the corresponding private key, can decrypt and read it. The encryption operation is computationally easy using the public key, but decryption without the private key is computationally infeasible.

Authentication through digital signatures provides message integrity and non-repudiation. The signer creates a signature by applying a cryptographic hash function to the message and then encrypting the hash value using their private key. Any recipient can verify the signature using the signer's public key, confirming both that the message originated from the claimed sender and that it has not been altered since signing. This mechanism is fundamental to secure communication and electronic commerce.

### Requirements for Public Key Cryptography

For a public key cryptosystem to be practically useful, it must satisfy several essential requirements. First, key generation must be efficient—it should be computationally easy to generate a key pair given a security parameter. Second, encryption and decryption operations must be computationally feasible for the legitimate parties. Third, the system must be provably or conjecturally secure under well-studied computational assumptions. Additionally, the public key must be easily distributable without compromising security, and the private key must be computable from the public key within a reasonable timeframe using the trapdoor information.

The security of public key systems depends critically on the hardness of underlying mathematical problems. RSA's security rests on the integer factorization problem, while Diffie-Hellman and DSA rely on the discrete logarithm problem. Elliptic curve cryptography bases its security on the elliptic curve discrete logarithm problem, which offers comparable security with significantly smaller key sizes.

## Examples

### Example 1: RSA Encryption and Decryption

Consider a simplified RSA setup with small primes for demonstration. Let p = 11 and q = 13, so n = 143 and φ(n) = 120. Choose e = 7 (coprime to 120), and compute d = e⁻¹ mod 120 = 103 (since 7 × 103 = 721 ≡ 1 mod 120).

For message m = 42, encryption: c = m^e mod n = 42^7 mod 143 = 63.
For ciphertext c = 63, decryption: m = c^d mod n = 63^103 mod 143 = 42.

This demonstrates that encryption with the public key (e=7, n=143) followed by decryption with the private key (d=103, n=143) recovers the original message. The security depends on an adversary not being able to compute d = 103 from e = 7 and n = 143 without factoring n.

### Example 2: Digital Signature Creation and Verification

Using the same RSA parameters, suppose Alice wants to sign a message m = "Hello". First, compute hash h = H("Hello") = 127 (simplified). To sign, Alice computes s = h^d mod n = 127^103 mod 143 = 67.

To verify, Bob computes h' = s^e mod n = 67^7 mod 143 = 127, which matches h = 127. Bob accepts the signature since the hash values match, confirming the message originated from Alice and remains unchanged.

### Example 3: Key Encapsulation for Key Exchange

In hybrid encryption systems, public key cryptography encapsulates a symmetric session key. Suppose Bob wants to send a 256-bit AES key K to Alice. Bob encrypts K using Alice's public key: c = K^e mod n. Alice decrypts using her private key: K = c^d mod n. The symmetric key K then encrypts the actual message data. This approach combines the efficiency of symmetric encryption with the key distribution advantages of public key cryptography.

## Exam Tips

1. **Understand the mathematical relationship:** Focus on how the public and private keys are mathematically related in RSA, particularly the role of Euler's totient function φ(n) and the modular multiplicative inverse.

2. **Distinguish between encryption and signatures:** Remember that encryption uses the recipient's public key, while digital signatures use the signer's private key. The verification process always uses the complementary key.

3. **Know the security assumptions:** Be clear about the computational problems underlying each cryptosystem (factorization for RSA, discrete logarithm for Diffie-Hellman, ECDLP for elliptic curve cryptography).

4. **Remember trapdoor concepts:** The essence of public key cryptography is the trapdoor one-way function—easy to compute forward, hard to invert unless you have the secret trapdoor.

5. **Key size considerations:** Understand why elliptic curve cryptography achieves similar security to RSA with much smaller key sizes due to the hardness of ECDLP compared to integer factorization.

6. **Practical limitations:** Public key operations are significantly slower than symmetric operations—know why hybrid systems are used in practice.

7. **Certificate authorities:** Understand how public key infrastructure (PKI) addresses the challenge of binding public keys to identities through digital certificates.
