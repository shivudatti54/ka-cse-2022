# Ethereum Blockchain

## Overview

The Ethereum blockchain extends Bitcoin's concept by storing not just transactions but also contract code and state data. Each block contains transaction receipts, state roots, and uncle blocks, forming a comprehensive record of all account states and smart contract executions.

## Key Points

- **Block Structure**: Header (parent hash, state root, transactions root, receipts root, timestamp, difficulty, nonce) and body (transactions, ommers)
- **Three Merkle Trees**: Transactions trie, receipts trie, state trie providing efficient verification
- **State Root**: Root hash of account state trie, capturing entire world state at block
- **Uncle/Ommer Blocks**: Valid blocks not on main chain receive partial rewards, reducing centralization
- **Block Reward**: Initially 5 ETH, reduced over time, plus transaction fees
- **Chain Selection**: GHOST protocol initially, later adapted for PoS finality
- **Block Size**: No fixed size limit, but gas limit constrains computational work per block

## Important Concepts

- Three trie roots in header enable efficient state, transaction, and receipt verification
- State root captures complete snapshot of all account balances and contract storage
- Uncle blocks compensate for network propagation delays
- Ethereum blocks store more complex data than Bitcoin blocks
- Gas limit per block controls network throughput and prevents spam

## Notes

- Understand three Merkle tree roots and their purposes
- Know block header fields and their roles
- Be able to explain uncle/ommer block concept and rewards
- Remember state root is key innovation enabling light client state verification
