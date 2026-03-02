# The Transaction Life Cycle

## Overview

A Bitcoin transaction progresses through distinct stages from creation to final confirmation: wallet creation, signing, broadcasting, mempool queuing, mining inclusion, initial confirmation, and accumulating additional confirmations for finality. This lifecycle ensures security through multiple validation points and increasing immutability.

## Key Points

- **Creation**: User constructs transaction with inputs, outputs, and fee using wallet software
- **Signing**: Transaction signed with private key, creating digital signature proving authorization
- **Broadcasting**: Signed transaction propagated to network nodes via P2P gossip protocol
- **Mempool**: Unconfirmed transactions stored in memory pool, awaiting miner selection
- **Mining**: Miners select highest-fee transactions from mempool for inclusion in blocks
- **First Confirmation**: Transaction included in block added to blockchain (1 confirmation)
- **Additional Confirmations**: Each subsequent block adds confirmation, increasing finality (6 confirmations ≈ 1 hour)

## Important Concepts

- Transaction remains unconfirmed while in mempool, can theoretically be replaced
- Miners prioritize transactions by fee rate (satoshis per byte)
- First confirmation means transaction is in blockchain but not yet final
- Six confirmations considered final due to computational infeasibility of reorganization
- Replace-by-Fee (RBF) allows updating unconfirmed transaction with higher fee

## Notes

- Know all lifecycle stages in order: create → sign → broadcast → mempool → mine → confirm → finality
- Understand why 6 confirmations (~1 hour) considered final
- Be able to explain fee rate impact on confirmation time
- Remember mempool state is local to each node, not global consensus
