# Digital Signatures and Key Management - Summary

## Key Definitions and Concepts

- **Digital Signature**: A mathematical scheme using asymmetric cryptography to verify authenticity, integrity, and non-repudiation of digital messages or documents.
- **Key Management**: The comprehensive process of generating, storing, distributing, using, rotating, and destroying cryptographic keys securely.
- **PKI (Public Key Infrastructure)**: Framework of roles, policies, hardware, and software for managing digital certificates and public-key encryption.
- **Certificate Authority (CA)**: Trusted entity that issues and manages digital certificates.
- **Cryptoperiod**: Time span during which a cryptographic key is authorized for use.

## Important Formulas and Theorems

- **RSA Signing**: S = M^d mod n (encrypt hash with private key)
- **RSA Verification**: M' = S^e mod n (decrypt with public key, compare with hash)
- **Key Relationship**: e × d ≡ 1 (mod φ(n)) where φ(n) = (p-1)(q-1)
- **Security Basis**: RSA relies on integer factorization; DSA relies on discrete logarithm; ECDSA relies on elliptic curve discrete logarithm.

## Key Points

- Digital signatures provide three guarantees: sender authenticity, message integrity, and non-repudiation.
- Hash-then-sign is the standard approach: hash the message first, then sign the hash with private key.
- RSA can perform both encryption and signatures; DSA is signature-only but government-standardized.
- ECDSA provides equivalent security to RSA with much smaller key sizes (256-bit vs 3072-bit).
- Keys must be generated using cryptographically secure random number generators (CSPRNGs).
- Key storage should use hardware security modules (HSMs) for high-security applications.
- Certificate chains must be validated from root CA to end-entity certificate.
- Key rotation (cryptoperiod) limits exposure from key compromise.
- Certificate revocation uses CRL or OCSP to invalidate compromised certificates.

## Common Mistakes to Avoid

- Confusing digital signatures with encryption—they serve different purposes.
- Using insufficient key lengths (minimum 2048-bit RSA, 256-bit ECDSA recommended).
- Neglecting key expiration and rotation—using same keys indefinitely increases risk.
- Not verifying certificate chains properly—accepting certificates without full validation.
- Storing private keys in plain text—always use encryption or hardware protection.

## Revision Tips

- Practice RSA signature computation with small numbers to understand the mathematical process.
- Draw the complete PKI hierarchy and certificate validation flow.
- Create comparison tables for RSA vs DSA vs ECDSA (key size, security, use cases).
- Remember: In key management, "the chain is only as strong as its weakest link"—prioritize securing the private key.