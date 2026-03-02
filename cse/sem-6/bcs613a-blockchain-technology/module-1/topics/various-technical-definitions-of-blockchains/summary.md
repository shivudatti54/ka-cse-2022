# Various Technical Definitions of Blockchains

## Overview

Blockchain is not a single technology but a convergence of multiple computer science concepts. It can be technically defined from several perspectives: as a distributed ledger, P2P network, cryptographic data structure, replicated state machine, and decentralized compute platform.

## Key Points

- **Distributed Digital Ledger**: Replicated transaction record shared across network nodes without central storage
- **Peer-to-Peer Network**: Direct node-to-node communication eliminating intermediaries and single points of failure
- **Cryptographic Chain**: Blocks linked via hash functions creating tamper-evident immutability
- **Replicated State Machine**: All nodes apply identical transactions in same order, maintaining consistent global state
- **Decentralized Platform**: Executes smart contracts deterministically across the entire network (Ethereum model)
- **Hash Function Properties**: One-way, unique output for each input, any input change produces completely different hash
- **Immutability Mechanism**: Changing one block invalidates all subsequent blocks through hash chain breaking

## Important Concepts

- Each definition highlights different architectural aspects of blockchain
- Immutability achieved through computational infeasibility of recalculating entire chain
- State transitions occur identically on all nodes through consensus
- Smart contract platforms (like Ethereum) extend basic ledger functionality
- P2P architecture ensures decentralization and resilience

## Notes

- Understand how cryptographic hashing creates the "chain" in blockchain
- Be able to explain blockchain from multiple technical perspectives
- Know why changing historical data requires recalculating all subsequent blocks
- Remember that not all blockchains support smart contracts (Bitcoin vs Ethereum)
