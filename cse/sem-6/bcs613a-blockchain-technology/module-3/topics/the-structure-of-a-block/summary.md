# The Structure of a Block

## Overview

A Bitcoin block consists of a block header containing metadata and a block body containing the transaction list. The header includes the previous block hash, Merkle root, timestamp, difficulty target, and nonce, creating the cryptographic chain that ensures blockchain immutability.

## Key Points

- **Block Header**: 80 bytes containing version, previous block hash, Merkle root, timestamp, bits (difficulty), nonce
- **Block Body**: Variable-size list of transactions organized in Merkle tree structure
- **Previous Block Hash**: 32-byte SHA-256 hash linking to parent block, creating the chain
- **Merkle Root**: 32-byte root hash of transaction Merkle tree for efficient verification
- **Timestamp**: Unix epoch time when miner began hashing the block header
- **Difficulty Bits**: Compact representation of target threshold for valid block hash
- **Nonce**: 32-bit number miners modify to find valid block hash

## Important Concepts

- Block header hash must be below target difficulty for validity
- Changing any transaction alters Merkle root, invalidating block hash
- Previous block hash creates immutable chain backward through history
- Block size limit affects transaction throughput (originally 1MB)
- Merkle tree enables SPV clients to verify transactions without full block

## Notes

- Know exact block header structure and all field sizes
- Understand how previous block hash creates the blockchain
- Be able to explain Merkle root purpose and calculation
- Remember nonce is the variable miners change during proof-of-work
