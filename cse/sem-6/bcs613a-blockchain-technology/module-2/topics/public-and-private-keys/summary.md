# Public and Private Keys

## Overview

Public-key cryptography forms the foundation of blockchain security and ownership through mathematically linked key pairs. The private key signs transactions proving authorization, while the public key verifies signatures without revealing secrets, enabling trustless peer-to-peer transactions without central authority.

## Key Points

- **Private Key**: Secret 256-bit number used to sign transactions; must be kept absolutely secure
- **Public Key**: Derived from private key via one-way function; can be shared publicly
- **Mathematical Relationship**: Easy to generate public key from private key, computationally infeasible to reverse
- **Digital Signatures**: Private key creates signature, public key verifies it mathematically
- **Transaction Flow**: Sign with private key → Broadcast with public key → Network verifies signature
- **Address Generation**: Blockchain address is hashed version of public key for privacy and shorter format
- **Absolute Responsibility**: No password recovery; losing private key means losing asset access permanently

## Important Concepts

- Private key analogy: master key to safety deposit box
- Public key analogy: publicly listed box number
- Trapdoor function ensures one-way relationship security
- Digital signature proves transaction authenticity and data integrity
- Public key verification confirms signature without revealing private key
- ECDSA algorithm enables efficient signatures with small key sizes

## Notes

- Understand asymmetric relationship: derive public from private, not reverse
- Know transaction signing and verification process step-by-step
- Remember that sharing private key = giving away complete control
- Be able to explain how verification works without central authority
