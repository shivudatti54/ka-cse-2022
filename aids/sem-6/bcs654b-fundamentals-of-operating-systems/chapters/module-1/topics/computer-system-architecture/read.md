# Ethereum Architecture

## What is Ethereum?

Ethereum is a decentralized, open-source blockchain platform that enables developers to build and deploy smart contracts and decentralized applications (dApps). Unlike Bitcoin, which is primarily a digital currency, Ethereum is a programmable blockchain that serves as a global computing platform.

## Core Components of Ethereum Architecture

### 1. Ethereum Network

The Ethereum network consists of thousands of nodes worldwide that maintain a shared state:

- **Full Nodes**: Store the complete blockchain and validate all transactions
- **Light Nodes**: Store only headers and request data when needed
- **Archive Nodes**: Store all historical states (require significant storage)
- **Validator Nodes**: Participate in consensus (Proof of Stake)

### 2. Ethereum State

Ethereum maintains a global state that includes:

| Component     | Description                                              |
| ------------- | -------------------------------------------------------- |
| Account State | Balance, nonce, code hash, storage root for each account |
| World State   | Mapping of addresses to account states                   |
| Storage       | Persistent key-value store for contract data             |
| Code          | Immutable bytecode for smart contracts                   |

### 3. Block Structure

Each Ethereum block contains:

```
Block Header:
- Parent Hash (previous block hash)
- State Root (Merkle root of world state)
- Transactions Root (Merkle root of transactions)
- Receipts Root (Merkle root of transaction receipts)
- Block Number
- Gas Limit
- Gas Used
- Timestamp
- Base Fee (EIP-1559)
```

### 4. Consensus Mechanism

After "The Merge" (September 2022), Ethereum uses **Proof of Stake (PoS)**:

- Validators stake 32 ETH to participate
- Random selection for block proposal
- Attestations from other validators
- Finality achieved through Casper FFG
- Energy-efficient compared to Proof of Work

## Ethereum Protocol Layers

### Layer 0: Network Layer

- P2P communication using devp2p protocol
- Node discovery via Kademlia DHT
- Message propagation (gossip protocol)

### Layer 1: Consensus Layer

- Beacon Chain coordination
- Validator management
- Block proposal and attestation
- Fork choice rule (LMD-GHOST)

### Layer 2: Execution Layer

- Transaction processing
- EVM execution
- State transitions
- Gas metering

## Key Architectural Concepts

### Merkle Patricia Trie

Ethereum uses Modified Merkle Patricia Tries for:

- **State Trie**: Maps addresses to account data
- **Storage Trie**: Per-contract persistent storage
- **Transaction Trie**: Block transactions
- **Receipt Trie**: Transaction receipts

Benefits:

- Efficient verification of data integrity
- Compact proofs (light client support)
- Incremental updates

### State Transition Function

```
NewState = STF(CurrentState, Transaction)
```

Each transaction triggers:

1. Validate transaction signature
2. Check sender balance for gas
3. Execute transaction (EVM or transfer)
4. Apply state changes
5. Calculate gas used and refund

## Network Types

| Network         | Purpose      | Chain ID |
| --------------- | ------------ | -------- |
| Mainnet         | Production   | 1        |
| Goerli          | Test network | 5        |
| Sepolia         | Test network | 11155111 |
| Local (Hardhat) | Development  | 31337    |

## Summary

- Ethereum is a **programmable blockchain** enabling smart contracts
- Uses **Proof of Stake** consensus for security and efficiency
- Maintains **global state** through Merkle Patricia Tries
- **Multiple node types** serve different purposes
- **Layer architecture** separates concerns (network, consensus, execution)
- Smart contracts execute deterministically on the **EVM**
