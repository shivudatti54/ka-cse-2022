# The Structure of a Block Header

## Overview

The Bitcoin block header is a compact 80-byte data structure containing six fields that collectively define a block's identity and validity. Miners repeatedly hash this header with different nonce values to find a hash below the difficulty target, achieving Proof-of-Work consensus.

## Key Points

- **Version (4 bytes)**: Block version number indicating protocol rules and feature support
- **Previous Block Hash (32 bytes)**: SHA-256 hash of parent block header, creating the chain
- **Merkle Root (32 bytes)**: Root hash of all transactions in block, enables efficient verification
- **Timestamp (4 bytes)**: Unix epoch timestamp of block creation
- **Bits/Difficulty Target (4 bytes)**: Compact encoding of difficulty threshold
- **Nonce (4 bytes)**: Number miners increment to find valid hash below target
- **Total Size**: Exactly 80 bytes, enabling efficient header transmission and storage

## Important Concepts

- Block hash is double SHA-256 of header: SHA-256(SHA-256(header))
- Valid block hash must have sufficient leading zeros (determined by difficulty)
- Merkle root allows verifying transaction inclusion without downloading full block
- Timestamp enables difficulty adjustment every 2016 blocks
- Previous block hash creates tamper-evident chain requiring massive recomputation to alter

## Notes

- Memorize all six header fields and their exact byte sizes (total 80 bytes)
- Understand mining involves finding nonce that produces valid header hash
- Know how Merkle root connects header to transaction body
- Be able to explain difficulty adjustment mechanism using timestamps
