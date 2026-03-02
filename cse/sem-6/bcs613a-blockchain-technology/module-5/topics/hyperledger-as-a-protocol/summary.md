# Hyperledger as a Protocol

## Summary

Hyperledger is an open-source collaborative effort hosted by the Linux Foundation that provides enterprise-grade blockchain frameworks. Unlike public blockchains, Hyperledger operates on permissioned networks with modular architecture enabling industry-specific customization.

### Key Definitions

- **Permissioned Blockchain**: Distributed ledger with restricted consensus participation to pre-approved nodes
- **Modular Architecture**: Design principle separating consensus, ordering, and validation into interchangeable components
- **Chaincode**: Smart contracts in Hyperledger Fabric terminology
- **Channel**: Private sub-network within Fabric enabling transaction privacy between participants

### Core Components

1. **Network Layer**: Peer-to-peer communication via gRPC, gossip protocol for state synchronization
2. **Data Layer**: Block and transaction structures with World State (Fabric) or Radix Merkle Tree (Sawtooth)
3. **Consensus Layer**: Pluggable consensus including Raft, BFT, and PoET mechanisms
4. **Application Layer**: SDKs, APIs, and chaincode interfaces

### Major Frameworks

- **Fabric**: Modular architecture with channel-based privacy, execution-order-validate model
- **Sawtooth**: PoET consensus using Intel SGX, Transaction Family abstraction
- **Corda**: Transaction-by-transaction consensus, flow framework for financial workflows

### Key Advantages

- Modularity enables independent component upgrades
- Permissioned model provides higher throughput than public blockchains
- Channel-based privacy essential for enterprise applications
- Clear governance separation between operators, developers, and users

### Revision Tips

1. Memorize the four-layer protocol stack and function of each layer
2. Understand the distinction between execution-order-validate (Fabric) versus traditional models
3. Compare consensus mechanisms: Raft (CFT) versus BFT versus PoET
4. Review privacy mechanisms: channels in Fabric versus Corda's transaction privacy
5. Practice identifying appropriate framework selections for given use cases