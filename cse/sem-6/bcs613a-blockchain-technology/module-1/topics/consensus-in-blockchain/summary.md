# Consensus in Blockchain

## Overview

Consensus mechanisms are the core protocols enabling decentralized blockchain nodes to unanimously agree on ledger state without central authority. They solve the Byzantine Generals Problem through cryptographic proofs and economic incentives, ensuring agreement, security, fault tolerance, and liveness across the network.

## Key Points

- **Proof of Work (PoW)**: Miners compete to solve computational puzzles; extremely secure but energy-intensive (Bitcoin, Litecoin)
- **Proof of Stake (PoS)**: Validators selected based on staked cryptocurrency; energy-efficient and scalable (Ethereum 2.0, Cardano)
- **Practical Byzantine Fault Tolerance (PBFT)**: Voting-based consensus for permissioned networks; fast with immediate finality (Hyperledger Fabric)
- **Core Goals**: Agreement among honest nodes, security against attacks, fault tolerance, and network liveness
- **Security Model Differences**: PoW relies on computational power, PoS on economic stake, PBFT on identity and voting
- **Blockchain Trilemma**: Consensus choice represents trade-offs between decentralization, security, and scalability
- **Double-Spending Prevention**: Consensus mechanisms prevent spending same coins twice without central authority

## Important Concepts

- Consensus is the solution to the Byzantine Generals Problem in blockchain context
- PoW verification is computationally easy despite difficult mining (asymmetric difficulty)
- PoS slashing mechanism punishes malicious validators by destroying staked funds
- PBFT requires ⅔ majority agreement and doesn't scale well to large open networks
- Delegated PoS (DPoS) and Proof of Authority (PoA) are alternative mechanisms with different trade-offs

## Notes

- Understand the comparison table: energy use, speed, decentralization, security model
- PoW is battle-tested but energy-intensive; PoS is modern and efficient
- PBFT ideal for enterprise/permissioned blockchains with known participants
- Be able to explain how each mechanism prevents Byzantine attacks
