# Symmetric Cryptography

## Overview

Symmetric cryptography uses a single shared secret key for both encryption and decryption. While blockchain primarily relies on asymmetric cryptography, symmetric encryption plays crucial supporting roles in wallet encryption, secure node communication, and data protection in private blockchains due to its superior speed and efficiency.

## Key Points

- **Single Key Model**: Same secret key encrypts and decrypts data; both parties must share key securely beforehand
- **Block Ciphers**: Encrypt fixed-size blocks (AES-128/192/256 most common with 128-bit blocks)
- **Stream Ciphers**: Encrypt data bit-by-bit or byte-by-byte (ChaCha20 used in modern applications)
- **AES Structure**: SubBytes, ShiftRows, MixColumns, AddRoundKey operations in each round
- **Modes of Operation**: ECB (insecure), CBC (secure but sequential), CTR (parallelizable)
- **Speed Advantage**: 100-1000x faster than asymmetric cryptography for bulk data
- **Key Distribution Problem**: Fundamental challenge requiring secure channel for sharing secret keys

## Important Concepts

- Wallet encryption uses AES-256 with user password-derived keys (PBKDF2/scrypt)
- TLS/SSL uses symmetric encryption after asymmetric key exchange
- Symmetric keys are 128-256 bits vs 2048-4096 bits for RSA
- Different key sizes provide different security levels: AES-128 (10 rounds), AES-192 (12 rounds), AES-256 (14 rounds)
- ECB mode reveals patterns in data, making it insecure for real applications

## Notes

- Understand comparison with asymmetric crypto: speed vs key distribution trade-offs
- Know AES key sizes and corresponding number of rounds
- Be able to explain modes of operation and why ECB is insecure
- Remember blockchain use cases: wallet encryption, TLS communication, private blockchain data
