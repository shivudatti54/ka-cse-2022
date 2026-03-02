# Module 4: Blockchain Accounts

## Introduction

In traditional financial systems, your identity and holdings are managed by a bank, which maintains a centralized ledger. Blockchain technology fundamentally reimagines this concept. Instead of accounts managed by a central entity, blockchains use a system of **cryptographically secure, self-sovereign accounts**. Understanding these accounts—how they are created, how they interact, and how they store state—is crucial for grasping how decentralized networks like Ethereum operate. This module delves into the two primary types of accounts and their core components.

## Core Concepts

### 1. Types of Accounts

In a blockchain like Ethereum, there are two distinct types of accounts:

#### a) Externally Owned Accounts (EOAs)

- **Control:** These are accounts controlled by a private key, which is ultimately owned by a human user. Whoever possesses the private key has absolute control over the account.
- **Purpose:** EOAs are used to initiate transactions. They can:
- Transfer native cryptocurrency (e.g., ETH) to other EOAs or Contracts.
- Trigger the code execution in a Smart Contract by sending a transaction to its address.
- **Characteristics:**
- **Have a private key.** This is their source of authority.
- **Do not have any associated code.** They are simple, passive entities.
- Can initiate transactions but cannot execute complex logic autonomously.

**Example:** Your MetaMask wallet creates an EOA. When you send ETH to a friend, you are using your EOA.

#### b) Contract Accounts (CAs)

- **Control:** These are accounts controlled by their own internal code (smart contract logic). They are not controlled by a private key.
- **Purpose:** Smart Contract Accounts execute code in response to receiving transactions or messages from other accounts. They can hold funds and data, and perform complex operations based on predefined rules.
- **Characteristics:**
- **Have associated code (smart contract).**
- **Do not have a private key.** Their actions are dictated solely by their code.
- Cannot initiate transactions on their own; they can only _react_ to transactions sent to them.

**Example:** A decentralized exchange (DEX) like Uniswap is a collection of Smart Contract Accounts. When you swap tokens, your EOA sends a transaction to a Uniswap contract account, which then executes the swap logic.

### 2. Anatomy of an Account

Every account on the Ethereum Virtual Machine (EVM) blockchain is defined by a state tuple containing four fundamental fields:

1. **Nonce:**

- For an **EOA**, this is a counter that tracks the number of transactions sent from that account. It prevents transaction replay attacks.
- For a **CA**, this represents the number of contracts _created_ by this account. It's sometimes called the "contract nonce."

2. **Balance:** The amount of Wei (the smallest denomination of ETH, where 1 ETH = 10¹⁸ Wei) owned by this account address.
3. **storageRoot:** A 256-bit hash (part of a Merkle Patricia Trie) that permanently encodes the storage contents of this account. This field is primarily used by Contract Accounts to store their persistent state variables.
4. **codeHash:** The hash of the EVM code for this account. For **EOAs**, this field is the hash of an empty string. For **Contract Accounts**, it is the immutable hash of the smart contract code that was deployed. This code cannot be changed after deployment.

### 3. Account Creation

- **Externally Owned Account (EOA):** Creation is free and happens off-chain. It involves using a cryptographic library to generate a random private key, from which a public key and finally the account address (a hash of the public key) are derived. The account only exists on the blockchain _after_ it receives funds in its first transaction.
- **Contract Account (CA):** Creation is an on-chain operation with a cost (gas). It is achieved by sending a special transaction (a "contract deployment transaction") from an EOA. This transaction contains the compiled bytecode of the smart contract and has a "null" recipient address (`0x0`). The network processes this, creates the new account, and stores its `codeHash`.

### 4. Transactions and Messages

An EOA initiates a transaction, which is a signed data package that can do one of two things:

1. **Transfer Value:** Send cryptocurrency to another address.
2. **Deploy/Interact with a Contract:** The transaction data field (`data`) contains the instructions for the EVM.

When a transaction targets a Contract Account, it triggers a **message call**. The EVM executes the contract's code, which can read from or write to its own storage, create new contracts, or send further "internal messages" to other contracts.

## Key Points & Summary

| Feature          | Externally Owned Account (EOA)  | Contract Account (CA)      |
| :--------------- | :------------------------------ | :------------------------- |
| **Control**      | Private Key                     | Smart Contract Code        |
| **Purpose**      | Initiate Transactions           | Execute Code Logic         |
| **Has Code?**    | No (`codeHash` of empty string) | Yes (Immutable `codeHash`) |
| **Initiate Tx?** | **Yes**                         | No (only reacts)           |
| **Creation**     | Free (Off-Chain)                | Costly Gas (On-Chain)      |

- Blockchain accounts are a fundamental data structure (`nonce`, `balance`, `storageRoot`, `codeHash`) that represent state and identity.
- The two types, **EOAs** (user-controlled) and **CAs** (code-controlled), serve complementary purposes in a decentralized ecosystem.
- EOAs are the entry point for all user actions, while CAs contain the business logic of decentralized applications (dApps).
- The **nonce** is critical for security, preventing double-spending and replay attacks.
- All interactions, from simple payments to complex DeFi operations, are ultimately triggered by a transaction from an EOA.
