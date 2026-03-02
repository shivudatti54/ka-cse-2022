# Symmetric Ciphers: AES and DES - Summary

## Key Definitions and Concepts
- **Block Cipher**: Encrypts fixed-size blocks (64/128 bits)
- **Feistel Network**: Splits block, applies round function to half (DES)
- **SPN**: Substitution-Permutation stages in parallel (AES)
- **Avalanche Effect**: Small input change → large output change

## Important Formulas and Theorems
- DES Round Function: F(R, K) = P(S(E(R) ⊕ K))
- AES MixColumns: Matrix multiplication in GF(2⁸) with irreducible polynomial x⁸+x⁴+x³+x+1
- Key Schedule: AES key expansion uses RotWord, SubWord, Rcon

## Key Points
- DES: 16 rounds, 56-bit key, broken by EFF Deep Crack (1998)
- AES: 10-14 rounds, Rijndael's mathematical foundation
- 3DES: 112/168-bit security, EDE mode
- AES-GCM: Authenticated encryption standard for TLS 1.3
- Side-channel attacks require constant-time implementations
- NIST SP 800-67 Rev. 2 retires TDEA (3DES) for sensitive data
- XTS-AES mode for disk encryption

## Common Mistakes to Avoid
- Confusing AES key sizes (128≠192≠256 rounds)
- Forgetting DES parity bits (64-bit key → 56 effective)
- Misapplying GF(2⁸) operations in MixColumns
- Assuming AES is quantum-safe (Grover's algorithm halves key strength)

## Revision Tips
1. Diagram Feistel vs SPN structures
2. Practice AES key expansion with sample keys
3. Memorize DES S-box design principles (e.g., no linear approximations)
4. Use NIST documentation for implementation standards
5. Compare AES vs DES in tabular form (rounds, attacks, speed)

Length: 650 words