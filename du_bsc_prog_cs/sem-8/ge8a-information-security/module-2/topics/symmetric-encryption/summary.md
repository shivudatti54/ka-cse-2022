# Symmetric Encryption - Summary

## Key Definitions and Concepts

- **Symmetric Encryption**: A cryptographic method using a single secret key for both encryption (converting plaintext to ciphertext) and decryption (converting ciphertext back to plaintext).

- **Block Cipher**: Encryption algorithm that processes fixed-size blocks of data (typically 64 or 128 bits) at a time; examples include DES, 3DES, and AES.

- **Stream Cipher**: Encryption algorithm that encrypts data bit-by-bit or byte-by-byte by XORing with a pseudorandom keystream.

- **Key Distribution Problem**: The fundamental challenge of securely sharing secret keys between communicating parties without interception.

- **Initialization Vector (IV)**: A random value used in certain encryption modes to ensure different ciphertexts for identical plaintexts.

- **Modes of Operation**: Methods (ECB, CBC, CTR, GCM) that extend block cipher encryption to variable-length data while providing security properties.

## Important Formulas and Theorems

- **Encryption**: C = E(K, P) — Ciphertext equals encryption function applied to plaintext with key
- **Decryption**: P = D(K, C) — Plaintext equals decryption function applied to ciphertext with key
- **XOR Property**: P = K ⊕ C (for one-time pad where C = P ⊕ K)
- **Shannon's Cipher Properties**: Confusion (key-ciphertext relationship complex) + Diffusion (plaintext changes spread widely)

## Key Points

- AES (128/192/256-bit key, 128-bit block) is the current gold standard for symmetric encryption
- DES (56-bit key) is obsolete; 3DES is deprecated but still found in legacy systems
- ECB mode reveals patterns and should never be used for real data
- CBC mode provides confidentiality but requires random IVs and is vulnerable to padding oracle attacks
- CTR mode offers parallelizable encryption with good security properties
- GCM provides both confidentiality and authentication (authenticated encryption)
- Hybrid encryption (asymmetric key exchange + symmetric bulk encryption) is standard practice
- Key management, not algorithm strength, is often the weakest link in cryptographic systems

## Common Mistakes to Avoid

1. **Using ECB mode** for encrypting multiple blocks — reveals patterns in ciphertext
2. **Reusing keystreams** in stream cipher modes — allows trivial decryption attacks
3. **Using predictable IVs** in CBC mode — compromises security
4. **Confusing key sizes** — thinking longer keys always mean better security without considering performance trade-offs
5. **Ignoring key distribution** — the biggest practical challenge in symmetric cryptography

## Revision Tips

1. **Practice with simple examples** — manually work through XOR encryption and understand why the one-time pad is perfectly secure
2. **Compare modes side-by-side** — create a table contrasting ECB, CBC, CTR, and GCM security properties
3. **Remember the evolution**: DES → 3DES → AES, understanding why each transition occurred
4. **Focus on real-world relevance** — most practical systems use AES-GCM; know why
5. **Review past exam questions** on key distribution and mode of operation security analysis