# Consensus Requirements

## Introduction

For a consensus mechanism to be effective in blockchain systems, it must satisfy several critical requirements. These requirements ensure the system remains secure, functional, and useful under various conditions.

## Core Requirements

### 1. Safety (Consistency)

**Definition**: All honest nodes agree on the same value. No two honest nodes ever commit different blocks at the same height.

**Why It Matters**:

- Prevents double-spending
- Ensures ledger consistency
- Maintains system integrity

**Formal Property**: If honest node A commits block B at height H, no honest node will ever commit a different block B' at height H.

### 2. Liveness (Progress)

**Definition**: The system eventually makes progress. Transactions submitted to the network are eventually processed.

**Why It Matters**:

- Ensures usability
- Prevents indefinite blocking
- Guarantees transaction processing

**Formal Property**: A valid transaction will eventually be included in the ledger.

### 3. Fault Tolerance

**Definition**: The system continues operating correctly despite node failures.

**Types of Tolerance**:

- **Crash Fault Tolerance (CFT)**: Tolerates f crashes with 2f+1 nodes
- **Byzantine Fault Tolerance (BFT)**: Tolerates f Byzantine with 3f+1 nodes

### 4. Sybil Resistance

**Definition**: Prevents attackers from creating multiple fake identities to gain disproportionate influence.

**Mechanisms**:

- **Proof of Work**: Requires computational resources
- **Proof of Stake**: Requires economic stake
- **Proof of Authority**: Requires verified identity

## Additional Requirements

### Decentralization

The system should not depend on a single point of failure or control.

**Metrics**:

- Number of validators
- Geographic distribution
- Stake/hash power distribution
- Nakamoto coefficient

### Scalability

The system should handle increasing transaction volume.

**Dimensions**:

- Transactions per second (TPS)
- Block size
- Network growth
- State size

### Energy Efficiency

Especially relevant post-Ethereum merge:

- PoW: High energy consumption
- PoS: 99%+ more efficient
- Environmental considerations

### Fairness

All participants should have proportional influence based on their stake/contribution.

**Aspects**:

- Block proposal fairness
- Reward distribution
- MEV (Miner Extractable Value) mitigation

## Trade-offs and Trilemmas

### The Blockchain Trilemma

You can optimize for only 2 of 3:

1. **Decentralization**: Many independent validators
2. **Security**: Resistance to attacks
3. **Scalability**: High transaction throughput

### Safety vs Liveness

Under network partitions:

- Prioritize safety: May halt
- Prioritize liveness: May fork

### Latency vs Throughput

- Fast finality: Lower throughput
- High throughput: Longer confirmation times

## Measuring Consensus Quality

### Finality Time

How long until a transaction is irreversible?

- Bitcoin: ~60 minutes (6 blocks)
- Ethereum: ~13 minutes
- Tendermint: Instant

### Throughput

Transactions per second:

- Bitcoin: ~7 TPS
- Ethereum: ~15-30 TPS
- Solana: ~65,000 TPS (claimed)

### Decentralization Metrics

- Validator count
- Stake concentration
- Geographic distribution

## Summary

- Safety and liveness are the two fundamental requirements
- Fault tolerance determines resilience to failures
- Sybil resistance prevents identity attacks
- Trade-offs exist between decentralization, security, and scalability
- Different blockchains prioritize different requirements
