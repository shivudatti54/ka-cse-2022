# Symmetric Encryption and Confidentiality - Summary

## Key Definitions and Concepts

- **Confidentiality**: Security goal ensuring information is accessible only to authorized parties
- **Symmetric Encryption**: Encryption method using the same secret key for encryption and decryption
- **Plaintext**: Original unencrypted data
- **Ciphertext**: Encrypted data unreadable without the key
- **Initialization Vector (IV)**: Random value used to ensure encryption randomness, never reuse with same key
- **Block Cipher**: Encrypts data in fixed-size blocks (AES uses 128-bit blocks)
- **Stream Cipher**: Encrypts data byte-by-byte or bit-by-bit

## Important Formulas and Theorems

- **AES Key Sizes**: 128, 192, or 256 bits (AES-128, AES-192, AES-256)
- **AES Block Size**: 128 bits (16 bytes)
- **DES Key Size**: 56 bits effective (64 bits with parity)
- **3DES Key Sizes**: 112 bits (two-key) or 168 bits (three-key)
- **GCM Tag Size**: 128 bits for authentication

## Key Points

1. AES (Advanced Encryption Standard) is the current global standard, replacing deprecated DES
2. ECB mode reveals patterns in encrypted data; never use for real applications
3. GCM mode provides both confidentiality AND integrity (authenticated encryption)
4. CTR mode enables parallel encryption and random access decryption
5. The fundamental challenge: securely distributing symmetric keys (key distribution problem)
6. Modern systems use hybrid cryptography: asymmetric to exchange keys, symmetric for bulk encryption
7. RC4 and 3DES are deprecated; ChaCha20 and AES-GCM are current recommendations
8. IV/nonce requirements differ by mode: CBC needs unpredictable IV; GCM needs unique nonce

## Common Mistakes to Avoid

1. **Using ECB for anything except learning purposes** — it reveals patterns and is cryptographically insecure
2. **Reusing IVs with the same key** — this completely breaks security in GCM and CTR modes
3. **Confusing DES and AES key sizes** — DES uses 56-bit keys, not 64-bit
4. **Forgetting that encryption doesn't guarantee integrity** — use GCM or add MAC for tamper protection

## Revision Tips

1. Practice drawing the differences between ECB, CBC, CTR, and GCM modes
2. Memorize why AES replaced DES (key size too small, vulnerable to brute-force)
3. Remember: Confidentiality ≠ Integrity — encryption alone doesn't prevent modification
4. Review the key distribution problem as it's the bridge to understanding public-key cryptography
5. Know which modes provide authenticated encryption (GCM) vs. confidentiality only (CBC)