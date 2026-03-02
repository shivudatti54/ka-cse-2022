# The World State

## Overview

Ethereum's world state is a mapping of all account addresses to their account states, implemented as Modified Merkle Patricia Trie (MPT) for efficient storage and verification. The state root hash in each block header represents the complete global state snapshot, enabling light clients to verify state without downloading entire blockchain.

## Key Points

- **State Trie**: Modified Merkle Patricia Trie mapping account addresses (160-bit) to account state objects
- **Account State**: Balance, nonce, storage hash (contract storage root), code hash (contract bytecode hash)
- **State Root**: 32-byte Keccak-256 hash representing entire world state, included in block header
- **Storage Trie**: Each contract account has separate MPT for persistent storage variables
- **State Transition**: Transaction execution modifies state, creating new state root for next block
- **Merkle Proof**: Allows proving account state without entire state trie (SPV verification)
- **State Size**: Grows continuously as new accounts created and contract storage expands

## Important Concepts

- MPT combines Merkle tree security with Patricia trie efficiency
- State root in block header commits to entire world state deterministically
- Contract storage separated into individual tries for each contract
- State transitions must be deterministic across all nodes for consensus
- Light clients verify state using Merkle proofs against state root

## Notes

- Understand MPT structure and advantages for Ethereum state management
- Know account state components: balance, nonce, storage hash, code hash
- Be able to explain state root role in block header
- Remember state transitions occur through transaction execution
