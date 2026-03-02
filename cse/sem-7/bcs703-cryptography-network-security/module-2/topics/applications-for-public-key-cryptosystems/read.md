# Applications for Public Key Cryptosystems

## Introduction

Public key cryptography forms the foundation of modern secure communications, enabling confidentiality, authentication, and key exchange without requiring shared secret keys. However, the security and functionality of public key cryptosystems critically depend on pseudorandom number generators (PRNGs) for various cryptographic operations. This topic examines the essential role of PRNGs within public key cryptosystems, specifically focusing on prime number generation for key establishment, random nonce creation in digital signature schemes, probabilistic encryption padding mechanisms, and session key derivation in key exchange protocols. Understanding these applications is fundamental to comprehending why cryptographically secure PRNGs are indispensable in practical cryptographic implementations.

The relationship between PRNGs and public key cryptosystems extends beyond mere key generation; it encompasses the entire cryptographic lifecycle from system initialization to protocol execution. The hardness assumptions underlying public key systems—such as the integer factorization problem (RSA), discrete logarithm problem (Diffie-Hellman, DSA), and elliptic curve discrete logarithm problem (ECDSA)—rely on the computational infeasibility of inverting one-way functions. However, this security guarantee holds only when the random parameters used in these systems are unpredictable and statistically random. A cryptographically weak PRNG can compromise even the most robust mathematical foundations, rendering the entire system vulnerable to attack.

## Key Concepts

### Prime Number Generation in RSA Key Generation

The security of RSA rests upon the difficulty of factoring the product of two large prime numbers. The process of generating RSA key pairs requires the generation of two distinct large primes, typically 1024-4096 bits in length. Cryptographically secure PRNGs are employed to select random seeds from which these primes are derived through probabilistic primality testing algorithms such as the Miller-Rabin test or the deterministic AKS algorithm.

The prime generation process must satisfy several critical requirements. First, the primes must be sufficiently large to resist factorization attacks; current recommendations specify minimum lengths of 2048 bits for secure applications. Second, the primes should be randomly distributed within the appropriate range, ensuring that no adversary can predict or precompute them. Third, the primes must satisfy specific structural properties—for instance, both primes should be of similar bit-length, and the difference between primes should not be too small to prevent factorization by Fermat's method.

Linear Congruential Generators (LCGs), despite their simplicity, are insufficient for cryptographic prime generation due to their predictable structure. The Blum Blum Shub (BBS) generator, based on the quadratic residue problem, provides better cryptographic guarantees for this purpose. Modern implementations often utilize cryptographic hash functions (SHA-256, SHA-3) in counter mode or the hash-based DRBG (Deterministic Random Bit Generator) specified in NIST standards for generating cryptographically random primes.

### Nonce Generation in Digital Signature Schemes

Digital signature schemes such as DSA (Digital Signature Algorithm), ECDSA (Elliptic Curve Digital Signature Algorithm), and RSA-PSS require the generation of random nonces (number used once) during the signing process. The security of these signatures depends critically on the randomness of these nonces. If a nonce is even partially predictable or if the same nonce is reused across different messages, an attacker can recover the signer's private key through lattice-based attacks or the Goh-Yorgensen algorithm.

Consider the DSA signature generation: given a message hash $h$, private key $x$, and random nonce $k$, the signature is computed as $r = (g^k \mod p) \mod q$ and $s = k^{-1}(h + xr) \mod q$. If an attacker knows the nonce $k$, they can directly compute the private key as $x = r^{-1}(sk - h) \mod q$. Even partial information about $k$—such as knowing half its bits—can enable recovery of the private key through the Hidden Number Problem, which can be solved using lattice reduction techniques like Coppersmith's method.

Therefore, the nonce must be generated using a CSPRNG (Cryptographically Secure PRNG) with sufficient entropy. Standards such as FIPS 186-4 specify precise requirements for nonce generation in DSA and ECDSA, including the use of deterministic generation methods that derive the nonce from the message and private key using HMAC, thereby eliminating the need for fresh randomness in each signature operation.

### Probabilistic Encryption and OAEP

RSA encryption, as originally specified (RSA-PKCS1 v1.5), is deterministic: encrypting the same plaintext always produces the same ciphertext. This property enables various attacks, including chosen-ciphertext attacks and traffic analysis. Probabilistic encryption schemes introduce randomness into the encryption process, ensuring that encrypting the same plaintext multiple times produces different ciphertexts, thereby preventing such attacks.

Optimal Asymmetric Encryption Padding (OAEP) represents the most widely deployed probabilistic padding mechanism for RSA encryption. OAEP applies two rounds of hashing with random masks generated from a PRNG, transforming the deterministic RSA operation into a probabilistic encryption scheme. Given a message $M$ and random seed $r$, OAEP computes: $M' = (M \oplus G(r)) || (H(M' \oplus G(r)) \oplus r)$, where $G$ and $H$ are cryptographic hash functions serving as mask generation functions (MGF).

The security of OAEP can be proven under the random oracle model, demonstrating that breaking OAEP is at least as hard as breaking the underlying one-way function (in this case, RSA inversion). This padding mechanism is specified in PKCS#1 v2.2 and is mandatory for RSA encryption in TLS 1.3 and other modern protocols.

### Session Key Derivation in Key Exchange Protocols

In Diffie-Hellman key exchange and its elliptic curve variants (ECDH), the shared secret is established through exchange of public parameters. However, this raw shared secret must be processed through a Key Derivation Function (KDF) to produce cryptographically strong session keys. HKDF (HMAC-based Key Derivation Function), specified in RFC 5869, employs a two-step process: first extracting a pseudorandom key from the input key material using HMAC with a salt, then expanding this key into multiple output keys of appropriate lengths for different cryptographic purposes.

The randomness of the derived keys depends entirely on the entropy of the input key material and the proper functioning of the KDF. If the Diffie-Hellman exchange produces weak or predictable shared secrets—perhaps due to insufficient randomness in the nonce selection or improper group parameters—the KDF cannot compensate for this weakness. Therefore, the random exponents in Diffie-Hellman must be generated using CSPRNGs with sufficient entropy to ensure the computational hardness of the discrete logarithm problem.

## Examples

### Worked Example 1: Analyzing LCG Weakness for RSA Key Generation

Consider a Linear Congruential Generator with parameters $a = 1103515245$, $c = 12345$, and $m = 2^{31}$, used to generate RSA primes. Demonstrate why this is insecure.

**Solution:**
The LCG produces sequences according to $X_{n+1} = (aX_n + c) \mod m$. While this passes certain statistical tests, it exhibits severe cryptographic weaknesses. The predictability of LCG outputs allows an attacker to recover the seed after observing as few as $O(\log m)$ consecutive outputs through linear algebra. Specifically, given outputs $X_0, X_1, X_2$, we can compute $a$ and $c$ by solving the linear system:

$$X_1 - X_0 = a(X_0 - X_{-1}) \mod m$$
$$X_2 - X_1 = a(X_1 - X_0) \mod m$$

Once $a$ and $c$ are known, the attacker can predict all subsequent outputs. In RSA key generation, if the primes are generated from predictable LCG outputs, an attacker can factor the public modulus by recovering the prime generation algorithm's state and computing the same primes, thereby compromising the entire key pair.

### Worked Example 2: ECDSA Nonce Reuse Attack

Suppose a signer uses ECDSA with the secp256k1 curve and signs two different messages $m_1$ and $m_2$ using the same nonce $k$. Given the signatures $(r_1, s_1)$ and $(r_2, s_2)$ and the message hashes $h_1$ and $h_2$, derive the private key $d$.

**Solution:**
In ECDSA, the signature equations are:
$$s_1 = k^{-1}(h_1 + d \cdot r_1) \mod n$$
$$s_2 = k^{-1}(h_2 + d \cdot r_2) \mod n$$

Since the same nonce $k$ is used, $r_1 = r_2 = r$. Subtracting the equations:
$$s_1 - s_2 = k^{-1}(h_1 - h_2) \mod n$$

Solving for $k$:
$$k = (h_1 - h_2)(s_1 - s_2)^{-1} \mod n$$

Once $k$ is computed, we can recover the private key from either signature equation:
$$d = r^{-1}(k \cdot s_1 - h_1) \mod n$$

This demonstrates why nonce generation using a PRNG with sufficient randomness is critical for signature scheme security. Even if the PRNG has a small bias, repeated signatures can leak sufficient information to compromise the private key.

### Worked Example 3: OAEP Decoding Verification

Given an OAEP-encoded message with parameters: hash function SHA-256 ($h = 256$ bits), key size $n = 2048$ bits, and message length $k_0 = 256$ bits (random seed), verify the decoding process for a received padding block.

**Solution:**
OAEP encoding uses two hash functions: $G: \{0,1\}^{256} \to \{0,1\}^{1792}$ and $H: \{0,1\}^{1792} \to \{0,1\}^{256}$. For a message $M$ of length 1792 bits and random seed $r$ of 256 bits:

1. Compute $X = M \oplus G(r)$ (1792 bits)
2. Compute $Y = H(X) \oplus r$ (256 bits)
3. Output: $X || Y$ (2048 bits = key size)

Decryption reverses this process:

1. Parse input as $X$ (first 1792 bits) and $Y$ (last 256 bits)
2. Recover $r' = H(X) \oplus Y$
3. Recover $M' = X \oplus G(r')$
4. Verify padding structure; if invalid, reject (security against timing attacks requires constant-time comparison)

If either step fails validation, the ciphertext is rejected, preventing padding oracle attacks that plague simpler padding schemes like PKCS#1 v1.5.

## Exam Tips

1. **Understand the mathematical foundations**: Be able to explain why the hardness of problems like integer factorization and discrete logarithm depends on the randomness of the underlying parameters.

2. **Know the difference between CSPRNGs and statistical PRNGs**: LCGs and linear feedback shift registers fail cryptographic requirements because their outputs are predictable given sufficient observations.

3. **Remember nonce requirements in signature schemes**: The same nonce in ECDSA/DSA enables private key recovery; understand the proof of this attack mechanism.

4. **掌握OAEP security proofs**: Under the random oracle model, OAEP provides IND-CCA2 security; understand how the mask generation functions $G$ and $H$ achieve this.

5. **Key derivation functions**: Understand why raw Diffie-Hellman output cannot be used directly as a session key and how HKDF addresses this through extraction and expansion phases.

6. **Attack models**: Be familiar with chosen-ciphertext attacks (CCA1, CCA2) and how probabilistic encryption thwarts them.

7. **Standards and specifications**: Know FIPS 186-4 requirements for DSA/ECDSA, PKCS#1 v2.2 for RSA-OAEP, and NIST SP 800-90A for deterministic random bit generators.

8. **Practical implementation concerns**: Side-channel attacks, timing attacks on padding validation, and the importance of constant-time operations in cryptographic software.
