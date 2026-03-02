# Distributed Systems

## Overview

Blockchain is fundamentally a distributed system where multiple independent nodes maintain a synchronized shared ledger through peer-to-peer communication and consensus protocols. Understanding blockchain through the lens of distributed systems reveals its architecture, Byzantine fault tolerance, CAP theorem trade-offs, and challenges in achieving consensus, consistency, and scalability.

## Key Points

- **P2P Architecture**: Equal-status nodes communicate directly without central servers, ensuring decentralization and resilience
- **Replication**: Every full node maintains complete blockchain copy providing fault tolerance and high availability
- **Byzantine Fault Tolerance**: System tolerates malicious nodes through consensus mechanisms (PoW, PoS, PBFT)
- **CAP Theorem Choice**: Blockchains prioritize Availability and Partition Tolerance, accepting eventual consistency
- **Consensus Mechanisms**: Enable distributed agreement despite network delays, clock differences, and malicious actors
- **Network Propagation**: Transaction and block spreading through gossip protocols affects fork rates and security
- **Fork Types**: Temporary forks (orphan blocks), hard forks (incompatible protocol changes), soft forks (backward compatible)
- **Scalability Challenges**: Storage (full history), bandwidth (broadcasting), and computation (validation) limitations

## Important Concepts

- Eventual consistency model: temporary forks resolved by longest chain rule
- Byzantine Generals Problem solved through economic incentives and cryptographic proofs
- Network partition tolerance critical for global distributed operation
- Trade-offs between decentralization, performance, and energy consumption
- Layer 2 solutions (Lightning Network, rollups) address scalability while maintaining L1 security

## Notes

- Understand difference between crash faults (nodes stop) and Byzantine faults (malicious behavior)
- Know how Bitcoin exemplifies distributed system principles with ~15,000 global nodes
- Be able to explain fork resolution and why temporary forks are normal
- Compare public blockchain (high decentralization, low performance) vs private (low decentralization, high performance)
