# Hands-on: Clients and wallets – Geth

### Introduction

- Geth is an open-source Ethereum client written in Go.
- It's the default client for the Ethereum network.

### Key Features

- **Protocols**
  - Web3.js API for JavaScript
  - RPC (Remote Procedure Call) protocol
  - WebSocket protocol
- **Wallet Integration**
  - Supports wallet providers (e.g., MetaMask, Ledger)
  - Allows users to interact with Ethereum blockchain

### Geth Architecture

- **Components**
  - **Node**: Ethereum protocol implementation
  - **Database**: Stores blockchain data
  - **Web Interface**: Handles user interactions
- **Data Structures**
  - **Block**: Ethereum block data structure
  - **Transaction**: Ethereum transaction data structure

### Geth Commands

- **`geth --help`**: Displays Geth command-line options
- **`geth --syncmode`**: Synchronization mode for Geth
- **`geth --datadir`**: Specifies data directory for Geth

### Important Formulas and Definitions

- **Hash function**: SHA-256 (Secure Hash Algorithm 256)
- **Keccak-256**: Hash function used for Ethereum blockchain
- **Block reward**: 2 ETH per block (before hard fork)
- **Gas**: Unit of measurement for Ethereum transactions

### Theorems and Concepts

- **Byzantine Fault Tolerance (BFT)**: Ethereum's consensus algorithm
- **Proof of Work (PoW)**: Ethereum's consensus algorithm (Legacy)
- **Proof of Stake (PoS)**: Ethereum's consensus algorithm (Ethereum 2.0)
