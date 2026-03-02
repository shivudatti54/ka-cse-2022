# Public-Key Cryptography: RSA & ECC - Summary

## Key Definitions and Concepts
- **Trapdoor Function**: Easy to compute, hard to invert without secret (e.g., factorization)
- **Semantic Security**: Ciphertext reveals no partial information about plaintext
- **Weil Pairing**: Bilinear map used in advanced ECC constructions

## Important Formulas and Theorems
- **RSA Encryption**: c ≡ mᵉ mod n
- **Fermat's Little Theorem**: a^(p-1) ≡ 1 mod p (prime p)
- **Hasse's Theorem**: |E(GF(p))| ∈ [p+1-2√p, p+1+2√p]
- **Point Addition Formula**: λ = (y₂-y₁)/(x₂-x₁) for P≠Q

## Key Points
- RSA security depends on integer factorization hardness
- ECC security relies on elliptic curve discrete logarithm problem
- 256-bit ECC ≈ 3072-bit RSA security level
- Proper padding (OAEP) is critical for RSA security
- NIST P-256 and Curve25519 are widely used ECC standards
- Quantum computers threaten both RSA and ECC via Shor's algorithm
- Isogeny-based cryptography is promising post-quantum alternative

## Common Mistakes to Avoid
- Using textbook RSA without padding
- Confusing additive vs multiplicative group structures
- Ignoring cofactor in ECC implementations
- Assuming all elliptic curves offer equivalent security

## Revision Tips
1. Practice solving RSA problems with different e values
2. Memorize point doubling formulas for Weierstrass curves
3. Compare complexity classes: FACTORING ∈ NP ∩ coNP
4. Review recent DU question papers focusing on security proofs
5. Study NIST SP 800-56B for key establishment standards

Length: 600 words