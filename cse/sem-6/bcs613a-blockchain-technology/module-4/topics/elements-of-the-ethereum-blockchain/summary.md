# Elements of the Ethereum Blockchain

## Overview

The Ethereum blockchain comprises interconnected elements including blocks, transactions, accounts, world state, receipts, and consensus mechanism. These components work together to form a decentralized state machine where transactions trigger deterministic state transitions verified by network consensus.

## Key Points

- **Blocks**: Contain header (parent hash, state root, transactions root, receipts root, beneficiary, difficulty, number, gas limit, timestamp, nonce) and body (transactions, ommers)
- **Transactions**: State transition triggers carrying nonce, gas price/limit, recipient, value, data, signature
- **Accounts**: EOAs (externally owned) and contract accounts storing balance, nonce, code, storage
- **World State**: Global account state mapping implemented as Modified Merkle Patricia Trie
- **Receipts**: Transaction execution results containing status, gas used, logs (events), cumulative gas
- **Three Tries**: State trie (accounts), transactions trie (block txs), receipts trie (execution results)
- **Consensus**: PoS validators proposing and attesting blocks, achieving finality through Casper FFG

## Important Concepts

- Three Merkle trie roots in header enable efficient verification
- Receipts provide execution outcomes and event logs for applications
- State root captures complete world state snapshot at each block
- Ommer blocks compensate network propagation delays
- Atomic transaction execution ensures state consistency

## Notes

- Know all block header fields and their purposes
- Understand relationship between blocks, transactions, state, and receipts
- Be able to explain three trie roots and what they represent
- Remember Ethereum is state machine transitioning through transactions
