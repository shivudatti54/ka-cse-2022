# Hash Functions & Digital Signatures - Summary

## Key Definitions and Concepts
- **Hash Function**: Deterministic function mapping arbitrary data to fixed-size digest
- **Avalanche Effect**: Small input change ⇒ drastic output change
- **Digital Signature**: Cryptographic proof linking signer to message via asymmetric crypto
- **Non-repudiation**: Legal concept enforced via exclusive private key control

## Important Formulas and Theorems
- **SHA-256 Rounds**: 64 rounds of Σ₀, Σ₁, Maj, Ch functions on 512-bit blocks
- **RSA Signature**: s = h(m)^d mod n; Verification: h(m) ≡ s^e mod n
- **DSA Parameters**: Prime p (1024-bit), q (160-bit divisor of p-1), g = h^((p-1)/q) mod p
- **Birthday Bound**: Collision probability ≈ √(2^n) for n-bit hash

## Key Points
- SHA-3 uses Keccak's sponge construction with 24 rounds of θ, ρ, π, χ, ι steps
- ECDSA signatures are probabilistic—same message ⇒ different signatures
- HMAC provides integrity + authentication without non-repudiation
- Post-quantum risk: Shor's algorithm breaks RSA/ECDSA; hash functions need doubling length
- RFC 6979: Deterministic DSA eliminates k reuse risks
- X.509 certificates use SHA-256/RSA signatures for web trust
- GOST R 34.11-2012: Russian standard using Streebog hash

## Common Mistakes to Avoid
- Using MD5/SHA-1 for new systems despite known collisions
- Confusing HMAC (symmetric) with digital signatures (asymmetric)
- Storing private keys without HSMs (Hardware Security Modules)
- Forgetting to pad messages in RSA-PSS implementations
- Assuming all hash functions are suitable for passwords (need PBKDF2/scrypt)

## Revision Tips
1. Practice manual DSA signature steps using small primes
2. Memorize NIST SP 800-57 key length recommendations (e.g., RSA 2048-bit until 2030)
3. Create attack trees for digital signature systems (e.g., key compromise vs algorithm break)
4. Use Python's hashlib and cryptography modules to experiment with real implementations
5. Study RFC 8017 (PKCS #1) for RSA signature encoding details