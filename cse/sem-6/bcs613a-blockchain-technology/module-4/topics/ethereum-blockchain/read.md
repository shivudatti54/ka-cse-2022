# Module 4: Ethereum Blockchain

## Introduction

While Bitcoin introduced the world to decentralized digital currency, Ethereum expanded the concept of blockchain far beyond simple transactions. Launched in 2015 by Vitalik Buterin and his team, Ethereum is a **decentralized, open-source blockchain** system distinguished by its built-in **Turing-complete programming language**. This critical feature allows developers to build and deploy **smart contracts** and **decentralized applications (dApps)**, transforming the blockchain from a distributed ledger into a **global, decentralized computer**.

## Core Concepts of Ethereum

### 1. Smart Contracts

A smart contract is a self-executing contract where the terms of the agreement are written directly into code. They automatically execute predefined actions when specific conditions are met, without the need for an intermediary.

- **Example:** Imagine a simple escrow service. Alice wants to pay Bob for a digital asset. They deploy a smart contract that holds Alice's funds. The contract is programmed to release the funds to Bob only if he provides a valid cryptographic proof of delivering the asset. Once the proof is verified on-chain, the contract executes the payment automatically, trustlessly, and immutably.

### 2. Ether (ETH) and Gas

- **Ether (ETH):** This is the native cryptocurrency of the Ethereum blockchain. It is used to pay for transaction fees and computational services on the network. It is the "fuel" that powers the ecosystem.
- **Gas:** Gas is the unit that measures the amount of computational effort required to execute operations, like a transaction or a smart contract function. Every operation has a fixed gas cost. The total **transaction fee** is calculated as: `Gas Used * Gas Price` (denominated in ETH).
- **Why Gas?** Gas prevents network spam and allocates resources efficiently. Complex operations (like deploying a large dApp) cost more gas than a simple ETH transfer.

### 3. Ethereum Virtual Machine (EVM)

The EVM is the heart of Ethereum. It is a **global, decentralized virtual machine** that exists on every node in the network. Its purpose is to execute smart contract code consistently and deterministically.

- **How it works:** When a smart contract is deployed or called, every node in the network runs the same code on their local EVM. This ensures that all participants reach the same consensus on the outcome of the contract's execution, maintaining the state of the blockchain. Solidity is the most popular high-level language for writing code that is compiled into EVM bytecode.

### 4. Accounts

Unlike Bitcoin's UTXO model, Ethereum uses an **account-based model**, similar to a bank account. There are two types of accounts:

1. **Externally Owned Accounts (EOAs):** Controlled by a private key. These are accounts owned by users. They can hold ETH and initiate transactions (e.g., sending ETH or triggering a smart contract).
2. **Contract Accounts:** Controlled by their own code (smart contract). They have an address, can hold ETH, and have associated code. They can't initiate transactions themselves; they only execute in response to a transaction from an EOA or another contract.

### 5. The Transition: Proof-of-Work to Proof-of-Stake

Ethereum underwent a monumental upgrade known as "The Merge" in September 2022, transitioning its consensus mechanism.

- **Old: Proof-of-Work (PoW)** - Miners used powerful computers to solve complex cryptographic puzzles to validate transactions and create new blocks. It was highly secure but incredibly energy-intensive.
- **New: Proof-of-Stake (PoS)** - Validators replace miners. To become a validator, a user must **stake** a minimum of 32 ETH. Validators are chosen algorithmically to propose and attest to new blocks based on the amount of ETH they have staked and other factors. PoS is far more energy-efficient, scalable, and secure in different ways.

### 6. Decentralized Applications (dApps)

dApps are applications that run on a P2P network of computers (the blockchain) rather than a central server. Their backend code (smart contracts) is deployed on the blockchain, making them decentralized, transparent, and censorship-resistant. Examples include DeFi platforms (Uniswap, Aave), NFT marketplaces (OpenSea), and play-to-earn games.

## Key Points / Summary

| Concept              | Description                                                                                                              |
| :------------------- | :----------------------------------------------------------------------------------------------------------------------- |
| **Core Innovation**  | A programmable blockchain that supports **smart contracts** and **dApps**.                                               |
| **Native Currency**  | **Ether (ETH)** is used to pay for transaction fees and computational services (**Gas**).                                |
| **Execution Engine** | The **Ethereum Virtual Machine (EVM)** provides a runtime environment for smart contracts on every node.                 |
| **Account Model**    | Uses **Externally Owned Accounts (user-controlled)** and **Contract Accounts (smart contracts)**.                        |
| **Consensus**        | Now uses **Proof-of-Stake (PoS)**, a highly energy-efficient mechanism where validators stake ETH to secure the network. |
| **Primary Use Case** | Serves as the foundational layer for a vast ecosystem of **decentralized applications (dApps)** and **DeFi**.            |
