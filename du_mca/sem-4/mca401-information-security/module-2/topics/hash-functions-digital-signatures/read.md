# Hash Functions & Digital Signatures

## Introduction
Hash functions and digital signatures form the backbone of modern information security systems. A cryptographic hash function converts arbitrary-length data into a fixed-size digest, ensuring data integrity and authenticity. Digital signatures use asymmetric cryptography to provide non-repudiation and verify message origin. Together, they enable critical security services in SSL/TLS, blockchain, and document signing.

These mechanisms address three core security requirements: 
1. **Integrity**: Detecting unauthorized data modification (e.g., file downloads)
2. **Authentication**: Verifying message origin (e.g., software updates)
3. **Non-repudiation**: Preventing sender denial (e.g., financial transactions)

The global digital signature market, valued at $4.0B in 2022 (Grand View Research), underscores their commercial importance in sectors like healthcare (e-prescriptions) and legal tech (e-contracts).

## Key Concepts

### Cryptographic Hash Functions
- **Properties**:
  - Pre-image Resistance: Given h(m), finding m is computationally hard
  - Second Pre-image Resistance: Given m1, finding m2 ≠ m1 with h(m1)=h(m2) is hard
  - Collision Resistance: Finding any m1 ≠ m2 with h(m1)=h(m2) is hard
- **Algorithms**:
  - SHA-2 (FIPS 180-4): 256/512-bit outputs, used in Bitcoin
  - SHA-3 (Keccak): Sponge construction, NIST standard since 2015
  - BLAKE3: 25% faster than SHA-256 in hardware benchmarks

### Digital Signatures
- **Components**:
  - Key Generation: (PK, SK) pair using RSA/DSA/ECDSA
  - Signing: s = Sig(SK, h(m))
  - Verification: Ver(PK, s, m) → {True/False}
- **Algorithms**:
  - RSA-PSS: Probabilistic padding scheme, FIPS 186-5 compliant
  - ECDSA: Elliptic curve variant with 256-bit keys = RSA 3072-bit security
  - EdDSA: Edwards-curve based, used in TLS 1.3

### HMAC (Hash-based MAC)
- Combines secret key with hash function: HMAC(K, m) = h((K ⊕ opad) || h((K ⊕ ipad) || m))
- Prevents length-extension attacks in naive hash usage

## Examples

**Example 1: SHA-256 & RSA Signature**
1. Message: m = "Transfer ₹10,000 to A/C 1234"
2. Hash: h = SHA-256(m) = 5a4e3...c21 (256 bits)
3. Sign with RSA private key (n=2048 bits, d):
   s = h^d mod n = 8912...a3f
4. Transmit (m, s)
5. Verification:
   - Compute h' = SHA-256(m)
   - Decrypt s using public key (e, n): h'' = s^e mod n
   - If h' = h'', signature valid

**Example 2: DSA Signature**
Given public params (p=1024-bit prime, q=160-bit divisor, g=generator):
1. Choose per-message k ∈ [1,q-1]
2. Compute r = (g^k mod p) mod q
3. Compute s = k⁻¹(h(m) + x*r) mod q (x=private key)
4. Signature = (r, s)
5. Verification involves checking g^(h(m)/s mod q) * y^(r/s mod q) mod p mod q == r

**Example 3: Collision Attack on MD5**
1. Attacker creates two contracts with same MD5 hash:
   - Contract A: "Pay Alice ₹1M"
   - Contract B: "Pay Bob ₹1M"
2. Uses chosen-prefix collision (cost: ~$0.65 on AWS as per 2020 study)
3. Tricks victim into signing Contract A
4. Substitutes Contract B with valid signature

## Exam Tips
1. Always mention specific algorithms (e.g., SHA-3 vs SHA-2) when comparing properties
2. For 6-mark questions, use the "Definition-Properties-Example" structure:
   "A digital signature is... (definition). It provides non-repudiation because... (property). For example, in TLS certificates... (real-world use)"
3. Remember NIST standards: FIPS 180-4 (SHA), FIPS 186-5 (DSA/RSA)
4. Draw diagrams for signature generation/verification processes
5. When discussing attacks, specify:
   - Attack type (e.g., birthday attack on collision resistance)
   - Complexity (e.g., 2^(n/2) for n-bit hash)
   - Mitigation (e.g., switch to SHA-3)
6. Compare RSA-PSS vs ECDSA:
   - Key sizes (RSA 3072-bit ≈ ECDSA 256-bit)
   - Performance (ECDSA faster in signing)
   - Standardization (RSA in PKCS#1, ECDSA in FIPS 186-5)
7. Always note that signatures apply to message digests, not raw messages