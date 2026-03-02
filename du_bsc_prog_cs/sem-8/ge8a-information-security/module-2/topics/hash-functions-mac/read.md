# Hash Functions and Message Authentication Codes (MAC)

## Introduction

In the realm of information security, ensuring **data integrity** and **authentication** is as critical as maintaining confidentiality. While encryption protects data from unauthorized access, it does not inherently guarantee that the data has not been tampered with during transmission. This is precisely where **hash functions** and **Message Authentication Codes (MACs)** play a pivotal role. They form the backbone of modern digital security systems — from verifying software downloads to securing online banking transactions.

A **hash function** is a mathematical algorithm that maps an arbitrary-length input to a fixed-length output (called a **hash value**, **digest**, or **fingerprint**). The function is deterministic, meaning the same input always produces the same output, yet it is computationally infeasible to reverse the process. A **Message Authentication Code (MAC)** extends this concept by incorporating a secret key into the hashing process, thereby providing not just integrity verification but also **origin authentication**. Together, these mechanisms ensure that a message has not been altered and that it genuinely originates from the claimed sender.

Understanding hash functions and MACs is essential for any computer science student because they underpin critical security protocols such as TLS/SSL, IPSec, digital signatures, password storage systems, and blockchain technology. For DU students preparing for information security examinations, this topic carries significant weight as it bridges the theoretical foundations of cryptography with practical, real-world security applications.

## Key Concepts

### 1. Cryptographic Hash Functions

A **cryptographic hash function** H takes an input message M of arbitrary length and produces a fixed-size output h = H(M). Unlike general-purpose hash functions used in data structures (e.g., hash tables), cryptographic hash functions must satisfy stringent security properties.

#### Properties of Cryptographic Hash Functions

| Property | Description |
|----------|-------------|
| **Pre-image Resistance** (One-way property) | Given a hash value h, it should be computationally infeasible to find any message M such that H(M) = h |
| **Second Pre-image Resistance** (Weak collision resistance) | Given a message M₁, it should be computationally infeasible to find a different message M₂ (M₂ ≠ M₁) such that H(M₁) = H(M₂) |
| **Collision Resistance** (Strong collision resistance) | It should be computationally infeasible to find any two distinct messages M₁ and M₂ such that H(M₁) = H(M₂) |
| **Avalanche Effect** | A small change in input (even a single bit) should produce a drastically different hash output |
| **Deterministic** | The same input always yields the same output |
| **Efficiency** | H(M) should be easy and fast to compute for any given M |

**Important Note:** Collision resistance implies second pre-image resistance, but the converse is not necessarily true. This hierarchy is crucial for exam questions.

#### The Birthday Paradox and Collision Resistance

The **birthday paradox** (or birthday attack) is fundamental to understanding collision resistance. In a room of just 23 people, the probability of two sharing a birthday exceeds 50%. Analogously, for a hash function producing an n-bit digest, a collision can be found with approximately **2^(n/2)** random hashing attempts, not 2^n. This means:

- A 128-bit hash requires only ~2^64 operations to find a collision — considered **insecure** today.
- A 256-bit hash requires ~2^128 operations — considered secure.

This is why modern hash functions like SHA-256 use at least 256-bit outputs.

### 2. Popular Hash Algorithms

#### MD5 (Message Digest 5)
- **Designer:** Ron Rivest (1991)
- **Output:** 128-bit digest
- **Block size:** 512 bits
- **Status:** **Broken** — practical collision attacks demonstrated in 2004 by Wang et al.
- **Usage:** Legacy systems, non-security checksum verification only

#### SHA-1 (Secure Hash Algorithm 1)
- **Designer:** NSA / NIST (1995)
- **Output:** 160-bit digest
- **Block size:** 512 bits
- **Status:** **Deprecated** — collision found by Google's SHAttered project (2017)
- **Usage:** Being phased out; certificates using SHA-1 are no longer trusted by browsers

#### SHA-2 Family
- **Variants:** SHA-224, SHA-256, SHA-384, SHA-512
- **Output:** 224, 256, 384, or 512 bits respectively
- **Block size:** 512 bits (SHA-224/256) or 1024 bits (SHA-384/512)
- **Status:** **Currently Secure** and widely used
- **Structure:** Based on the **Merkle-Damgård construction**

#### SHA-3 (Keccak)
- **Designer:** Guido Bertoni, Joan Daemen, Michaël Peeters, Gilles Van Assche
- **Selected:** NIST competition winner (2012)
- **Output:** 224, 256, 384, or 512 bits
- **Structure:** Based on the **Sponge construction** (fundamentally different from SHA-2)
- **Status:** Secure; provides an alternative if SHA-2 is ever compromised

### 3. Merkle-Damgård Construction

Most classical hash functions (MD5, SHA-1, SHA-2) follow the **Merkle-Damgård** iterative structure:

1. **Padding:** The message M is padded so its length is a multiple of the block size. Padding includes appending the original message length (length strengthening).
2. **Splitting:** The padded message is divided into blocks M₁, M₂, ..., Mₙ.
3. **Iterative Compression:** Starting with an **Initialization Vector (IV)**, each block is processed through a **compression function f**:
   - H₀ = IV
   - Hᵢ = f(Hᵢ₋₁, Mᵢ) for i = 1 to n
   - Output = Hₙ

**Theorem:** If the compression function f is collision-resistant, then the overall hash function H built using Merkle-Damgård construction is also collision-resistant.

**Known Weakness:** Susceptible to **length extension attacks** — given H(M), an attacker can compute H(M || padding || M') without knowing M. This directly motivates the need for HMAC.

### 4. Message Authentication Code (MAC)

A **MAC** is a short piece of information used to authenticate a message and verify its integrity. It involves a **shared secret key K** between sender and receiver.

**MAC Generation:** Tag T = MAC(K, M)
**MAC Verification:** Receiver computes MAC(K, M) and compares with received T

#### Properties of MAC:
- **Unforgeability:** Without knowing K, an adversary cannot produce a valid (M, T) pair
- **Key-dependent:** Different keys produce different tags for the same message
- **Fixed-length output:** Regardless of message length

#### MAC vs. Hash Function:

| Feature | Hash Function | MAC |
|---------|--------------|-----|
| Key required | No | Yes |
| Provides integrity | Yes | Yes |
| Provides authentication | No | Yes |
| Provides non-repudiation | No | No (both parties share key) |

### 5. HMAC (Hash-based MAC)

**HMAC** is the most widely used MAC construction, defined in RFC 2104. It uses a cryptographic hash function H and a secret key K.

**HMAC Formula:**

```
HMAC(K, M) = H((K' ⊕ opad) || H((K' ⊕ ipad) || M))
```

Where:
- **K'** = K padded with zeros to the block size of H (or H(K) if K is longer than block size)
- **opad** = outer padding = 0x5C repeated to block size
- **ipad** = inner padding = 0x36 repeated to block size
- **⊕** = XOR operation
- **||** = concatenation

#### Why HMAC and not simply H(K || M)?

Naive constructions like H(K || M) are vulnerable to **length extension attacks** in Merkle-Damgård-based hash functions. HMAC's nested structure with two distinct padding constants (ipad and opad) provides provable security — if the underlying hash function's compression function is a **PRF (Pseudo-Random Function)**, then HMAC is also a PRF.

#### Security of HMAC:
- Security depends on the underlying hash function
- HMAC-SHA256 is considered very secure and is widely used in TLS, IPSec, JWT tokens, and API authentication

### 6. CBC-MAC (Cipher Block Chaining MAC)

An alternative to HMAC that uses a **block cipher** (like AES) instead of a hash function:

1. Encrypt message blocks using CBC mode with a secret key K
2. The MAC tag is the **final ciphertext block** (or a portion of it)

**Limitation:** Basic CBC-MAC is only secure for **fixed-length messages**. For variable-length messages, variants like **CMAC** (Cipher-based MAC, NIST SP 800-38B) or **EMAC** are used.

### 7. Authenticated Encryption

Modern cryptographic practice often combines encryption with MAC to provide both **confidentiality** and **integrity/authentication**. Three approaches exist:

- **Encrypt-then-MAC (EtM):** Encrypt M, then compute MAC on ciphertext. **(Recommended — used in IPSec)**
- **MAC-then-Encrypt (MtE):** Compute MAC on M, then encrypt (M || MAC). (Used in older TLS versions)
- **Encrypt-and-MAC (E&M):** Encrypt M and independently compute MAC on M. (Used in SSH)

**GCM (Galois/Counter Mode)** with AES is a widely used authenticated encryption mode that combines CTR-mode encryption with a GHASH-based MAC.

## Examples

### Example 1: Understanding Hash Properties

**Problem:** Alice sends a file with hash h = SHA-256(file) to Bob over an insecure channel. Mallory intercepts and modifies the file. Can Bob detect the tampering? Can Mallory forge a valid hash?

**Solution:**

**Step 1:** Bob receives the (potentially modified) file and computes SHA-256(received_file).

**Step 2:** Bob compares his computed hash with the received hash h.

**Step 3 — Attack Analysis:**
- If Mallory modifies the file but not the hash → Bob's computed hash ≠ h → **tampering detected** (due to collision resistance).
- If Mallory modifies both the file and the hash → Mallory computes a new valid hash → **tampering goes undetected!**

**Conclusion:** A plain hash function provides integrity only if the hash itself is transmitted over a **secure/authenticated channel**. This limitation motivates the use of **MAC** or **digital signatures** where the hash is protected by a secret key or private key.

### Example 2: HMAC Computation (Conceptual)

**Problem:** Given a key K = "secret" and message M = "Hello DU", demonstrate the conceptual steps of HMAC-SHA256 computation.

**Solution:**

**Step 1: Key Preparation**
- SHA-256 block size = 512 bits (64 bytes)
- K = "secret" = 6 bytes < 64 bytes
- K' = "secret" padded with 58 zero bytes to make 64 bytes

**Step 2: Inner Hash**
- Compute K' ⊕ ipad (XOR each byte of K' with 0x36)
- Concatenate result with message M: (K' ⊕ ipad) || "Hello DU"
- Compute inner hash: H_inner = SHA-256((K' ⊕ ipad) || M)

**Step 3: Outer Hash**
- Compute K' ⊕ opad (XOR each byte of K' with 0x5C)
- Concatenate with inner hash: (K' ⊕ opad) || H_inner
- Compute HMAC = SHA-256((K' ⊕ opad) || H_inner)

**Step 4: Output**
- Result is a 256-bit (32-byte) HMAC tag that both authenticates the sender (who knows K) and ensures integrity of M.

### Example 3: Birthday Attack Calculation

**Problem:** How many messages must an attacker hash to find a collision with probability ≥ 0.5 for (a) a 64-bit hash and (b) a 256-bit hash?

**Solution:**

Using the birthday bound approximation: **n ≈ 1.17 × 2^(L/2)**, where L is the hash output length in bits.

**(a) L = 64 bits:**
- n ≈ 1.17 × 2^32 ≈ 5.02 × 10^9 (about 5 billion attempts)
- This is easily feasible with modern computing → **insecure**

**(b) L = 256 bits:**
- n ≈ 1.17 × 2^128 ≈ 3.98 × 10^38
- Even at 10^15 hashes/second, this would take ~10^16 years → **computationally infeasible**

**Key Takeaway:** The security of a hash function against birthday attacks is **half the bit length** of its output. A 256-bit hash provides 128-bit security against collision attacks.

## Exam Tips

1. **Differentiate the three resistance properties clearly:** Pre-image, second pre-image, and collision resistance are frequently asked. Remember: collision resistance ⇒ second pre-image resistance, but NOT vice versa.

2. **Birthday paradox is a favourite:** Be prepared to calculate the number of attempts needed for a collision given the hash length. Use the formula n ≈ 2^(L/2).

3. **MAC vs. Digital Signature:** MACs use symmetric (shared) keys and do NOT provide non-repudiation. Digital signatures use asymmetric keys and DO provide non-repudiation. This distinction is commonly tested.

4. **Know the HMAC formula by heart:** Be able to write HMAC(K, M) = H((K' ⊕ opad) || H((K' ⊕ ipad) || M)) and explain each component. Understand why double hashing with different pads prevents length extension attacks.

5. **Compare hash algorithms in tabular form:** MD5 (128-bit, broken), SHA-1 (160-bit, deprecated), SHA-256 (256-bit, secure), SHA-3 (sponge construction). Know the key historical attacks.

6. **Encrypt-then-MAC vs. MAC-then-Encrypt:** Know the three composition approaches and which protocols use which. EtM is generally preferred and considered the most secure.

7. **Length extension attack:** Understand why H(K || M) is insecure for Merkle-Damgård hashes and how HMAC's construction mitigates this. This demonstrates deep conceptual understanding that earns top marks.