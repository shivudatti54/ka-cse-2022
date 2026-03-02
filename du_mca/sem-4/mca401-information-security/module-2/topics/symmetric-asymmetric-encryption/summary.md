# Symmetric and Asymmetric Encryption - Summary

## Key Definitions and Concepts

- **Encryption:** The process of converting plaintext into unreadable ciphertext using an algorithm and key
- **Symmetric Encryption:** Uses the same secret key for encryption and decryption (AES, DES, 3DES)
- **Asymmetric Encryption:** Uses a key pair—public key for encryption, private key for decryption (RSA, ECC)
- **Hybrid Encryption:** Combines both approaches, using asymmetric encryption for key exchange and symmetric for bulk data encryption

## Important Formulas and Theorems

- **RSA Key Generation:** n = p × q, where p and q are large primes; φ(n) = (p-1)(q-1); d ≡ e⁻¹ (mod φ(n))
- **RSA Encryption:** c = m^e mod n
- **RSA Decryption:** m = c^d mod n
- **AES Key Sizes:** 128, 192, or 256 bits with 10, 12, or 14 rounds respectively

## Key Points

- Symmetric encryption offers fast processing but faces the key distribution problem; asymmetric encryption solves this but is computationally slower
- AES replaced DES as the federal standard, offering key sizes of 128/192/256 bits with stronger security
- RSA security relies on the difficulty of factoring large composite numbers into prime factors
- Hybrid systems (e.g., SSL/TLS, PGP) combine advantages of both approaches
- Diffie-Hellman enables secure key exchange over insecure channels without prior shared secrets
- ECC provides equivalent security to RSA with significantly smaller key sizes
- Key management is critical—in practice, most systems use asymmetric crypto to exchange symmetric session keys

## Common Mistakes to Avoid

- Confusing which algorithms are symmetric versus asymmetric
- Assuming DES is still secure (56-bit key is cryptographically broken)
- Using the same key for encryption and signature operations in RSA
- Overlooking that RSA with small primes (as in textbook examples) is trivially breakable

## Revision Tips

- Practice RSA key generation with small primes to understand the mathematical process
- Remember the AES round operations sequence: SubBytes → ShiftRows → MixColumns → AddRoundKey
- Focus on why hybrid systems are preferred in real-world applications
- Review the security assumptions underlying each algorithm (factorization, discrete log, elliptic curve)