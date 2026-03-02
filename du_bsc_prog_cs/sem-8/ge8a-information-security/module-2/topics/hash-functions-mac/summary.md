# Hash Functions and Message Authentication Codes (MAC) - Summary

## Key Definitions and Concepts
- **Hash Function:** A deterministic algorithm mapping arbitrary-length input to a fixed-length output (digest/fingerprint).
- **Pre-image Resistance:** Given h, infeasible to find M such that H(M) = h.
- **Second Pre-image Resistance:** Given M₁, infeasible to find M₂ ≠ M₁ with H(M₁) = H(M₂).
- **Collision Resistance:** Infeasible to find any M₁ ≠ M₂ with H(M₁) = H(M₂).
- **MAC:** A keyed function producing a fixed-length tag for message integrity and authentication.
- **HMAC:** A MAC construction using a cryptographic hash function with a secret key.

## Important Formulas and Theorems
- **HMAC:** HMAC(K, M) = H((K' ⊕ opad) || H((K' ⊕ ipad) || M))
  - ipad = 0x36 repeated; opad = 0x5C repeated
- **Birthday Bound:** Collisions expected after ≈ 2^(n/2) hashes for an n-bit hash
- **Security Level:** An n-bit hash provides n/2 bits of security against collision attacks
- **Merkle-Damgård:** Hᵢ = f(Hᵢ₋₁, Mᵢ), starting from H₀ = IV

## Key Points
- MD5 (128-bit) is **broken**; SHA-1 (160-bit) is **deprecated**; SHA-256 is **currently secure**
- SHA-3 uses sponge construction, fundamentally different from SHA-2's Merkle-Damgård
- Hash functions alone provide integrity but **not** authentication (no key involved)
- MACs provide both integrity and authentication but **not** non-repudiation
- HMAC's nested structure prevents length extension attacks
- CBC-MAC (basic) is secure only for fixed-length messages; CMAC extends it
- Encrypt-then-MAC (EtM) is the recommended authenticated encryption approach
- Collision resistance implies second pre-image resistance, but not vice versa
- The avalanche effect ensures even 1-bit input change drastically alters the hash output
- GCM (AES-GCM) is a widely adopted authenticated encryption with associated data (AEAD) mode

## Common Mistakes to Avoid
- **Confusing collision resistance with pre-image resistance:** They are distinct properties with different attack complexities (2^(n/2) vs 2^n).
- **Claiming MAC provides non-repudiation:** Since both parties share the key, either could have generated the tag. Only digital signatures provide non-repudiation.
- **Using H(K || M) as a MAC:** This is insecure for Merkle-Damgård hashes due to length extension attacks. Always use HMAC.
- **Assuming a longer hash is always better:** Security depends on the algorithm's design, not just output length. A broken 256-bit hash is worse than a secure 160-bit one.

## Revision Tips
- Create a **comparison table** of MD5, SHA-1, SHA-2, SHA-3 with columns for output size, block size, structure, and security status.
- Practice the **HMAC computation steps** on paper — examiners frequently ask to outline the process.
- Remember the **hierarchy**: Collision Resistance → Second Pre-image Resistance → Pre-image Resistance (each implies the next, not vice versa).
- Link concepts to **real-world protocols**: HMAC-SHA256 in JWT/TLS, SHA-256 in Bitcoin, bcrypt/Argon2 for passwords.