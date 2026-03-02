# Cryptographic Primitives

## Overview

Cryptographic primitives are the fundamental building blocks of blockchain security, including hash functions, digital signatures, symmetric/asymmetric encryption, and Merkle trees. These primitives work synergistically to enable secure, verifiable, and trustless transactions in decentralized systems.

## Key Points

- **Hash Functions**: Create fixed-length fingerprints with properties: deterministic, quick, one-way, avalanche effect, collision-resistant
- **Digital Signatures**: ECDSA proves authenticity, integrity, and non-repudiation by signing message hashes
- **Symmetric Cryptography**: Single shared key; fast but has key distribution problem (AES for wallet encryption)
- **Asymmetric Cryptography**: Public-private key pairs; solves key distribution, enables signatures (ECC/ECDSA)
- **Merkle Trees**: Hierarchical hash structure enabling efficient transaction verification via Merkle proofs
- **SHA-256**: Bitcoin's hash function for block hashing and address generation
- **ECDSA Advantage**: Smaller key sizes (256-bit ECC vs 3072-bit RSA) for equivalent security

## Important Concepts

- Hash function properties critical for block chaining and data integrity
- Digital signature: sign hash with private key, verify with public key
- Merkle root in block header allows SPV (Simple Payment Verification) for light clients
- Any transaction change cascades up Merkle tree changing root hash
- Transaction flow combines all primitives: hash → sign → broadcast → verify → Merkle tree → mine

## Notes

- Memorize five hash function properties and explain each
- Understand why message is hashed first, then hash is signed
- Know how Merkle trees enable efficient verification without full blockchain download
- Be able to trace complete transaction lifecycle using all cryptographic primitives
