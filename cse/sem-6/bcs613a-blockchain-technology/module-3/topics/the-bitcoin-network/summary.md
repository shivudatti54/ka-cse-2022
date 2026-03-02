# The Bitcoin Network

## Overview

The Bitcoin network is a peer-to-peer distributed system of nodes that maintain consensus on a shared ledger through the Bitcoin protocol. Nodes validate transactions, propagate blocks, and participate in achieving network consensus without central coordination.

## Key Points

- **P2P Architecture**: Direct node-to-node communication without centralized servers
- **Node Types**: Full nodes (store complete blockchain), SPV nodes (lightweight clients), mining nodes
- **Network Propagation**: Gossip protocol spreads transactions and blocks across network
- **Port 8333**: Default Bitcoin protocol port for node communication
- **Node Discovery**: DNS seeds and peer exchange for finding network participants
- **Block Relay**: Miners broadcast new blocks, nodes verify and propagate to peers

## Important Concepts

- Full nodes validate all transactions and blocks independently
- Network topology is dynamic as nodes join and leave
- Block propagation time affects orphan block rate
- Mempool stores unconfirmed transactions awaiting mining
- Network resilience through geographical distribution and redundancy

## Notes

- Understand difference between full nodes, SPV nodes, and mining nodes
- Know how gossip protocol enables decentralized communication
- Remember that network consensus emerges from individual node validation
