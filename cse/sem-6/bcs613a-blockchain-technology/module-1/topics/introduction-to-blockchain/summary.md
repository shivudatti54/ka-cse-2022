# Introduction to Blockchain

## Overview

Blockchain is a decentralized, distributed digital ledger that enables direct peer-to-peer value transfer without trusted intermediaries. It solves the Byzantine Generals Problem through consensus mechanisms and leverages cryptographic techniques to create an immutable, tamper-evident chain of transaction blocks.

## Key Points

- **Distributed System**: Network of nodes that maintain identical copies of a shared ledger without central authority
- **Byzantine Generals Problem**: Solved through consensus mechanisms enabling untrusted nodes to agree on ledger state
- **CAP Theorem Trade-off**: Blockchains prioritize Availability and Partition Tolerance (AP), accepting eventual consistency over strong consistency
- **Cryptographic Chain**: Each block contains the hash of the previous block, creating tamper-evident immutability
- **Consensus Mechanisms**: Protocols like PoW and PoS ensure network agreement on transaction validity and order
- **Decentralization**: Eliminates single points of failure and reduces censorship risk through distributed control
- **Block Structure**: Contains transaction list, timestamp, previous block hash, and nonce for mining

## Important Concepts

- Consensus is the solution to achieving trust in a trustless environment
- Immutability achieved through cryptographic hashing and chain linking
- Multiple transaction confirmations needed due to eventual consistency model
- Public blockchains are permissionless, while private/consortium are permissioned
- Smart contracts extend blockchain beyond simple value transfer to programmable applications

## Notes

- Understand the "why" behind blockchain - solving the problem of centralized trust
- Be able to explain how cryptographic hashing creates immutability
- Know the difference between public, private, and consortium blockchains
- CAP theorem is fundamental - blockchains sacrifice strong consistency for availability
