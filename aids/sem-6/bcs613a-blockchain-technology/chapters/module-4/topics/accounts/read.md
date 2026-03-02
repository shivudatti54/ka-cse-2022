# Module 4: Blockchain Technology - Accounts

## Introduction

In traditional financial systems, your identity is managed by a central authority, like a bank, which holds your account details. Blockchain, however, offers a paradigm shift with its decentralized approach to identity and value ownership. In Ethereum and other similar blockchain platforms, this is managed through **Accounts**. Understanding accounts is fundamental to grasping how users and smart contracts interact with the blockchain network. This module delves into the types of accounts, their structure, and their role in the ecosystem.

## Core Concepts of Blockchain Accounts

Unlike Bitcoin's UTXO (Unspent Transaction Output) model, which is more like digital cash, Ethereum uses an **account-based model**, which is more akin to a bank account. This model is often considered more intuitive for developers and users. There are two primary types of accounts in Ethereum:

### 1. Externally Owned Accounts (EOAs)

*   **Definition:** An EOA is an account controlled by a private key, which is ultimately owned by a human user. This is the account you use to hold Ether (ETH) and to initiate transactions.
*   **Control:** Controlled by a cryptographic **private key**. Whoever possesses the private key has absolute control over the account and its funds. The corresponding **public key** is derived from the private key, and the **account address** is derived from the public key (specifically, the last 20 bytes of the Keccak-256 hash of the public key).
*   **Features:**
    *   **Can hold a balance** of Ether (ETH).
    *   **Can send transactions** (e.g., transfer ETH to another account).
    *   **Can trigger smart contract code** by calling a function within a contract.
    *   **Cannot contain its own code.**

**Example:** When you create a MetaMask wallet, you are generating a private key and its corresponding EOA. Your wallet address (e.g., `0x742d35Cc...`) is your EOA's identity on the blockchain.

### 2. Contract Accounts (CAs)

*   **Definition:** A CA is an account that is controlled by its own internal smart contract code. It is not owned by a user but exists autonomously on the blockchain.
*   **Control:** Controlled by its programmatic code. The code execution is triggered by a transaction received from an EOA or another CA.
*   **Features:**
    *   **Can hold a balance** of Ether.
    *   **Contains its own smart contract code.**
    *   **Can send "internal transactions"** (messages) to other contracts.
    *   **Can execute its code** when it receives a transaction, performing complex operations as defined by its programmer (e.g., swapping tokens on a DEX, lending assets).

**Example:** The Uniswap V2 Router contract (`0x7a250d...`) is a Contract Account. It has a balance and contains code that executes trades when you send a transaction to it from your EOA.

### Account State & Components

Both types of accounts share a common state structure, stored globally on the blockchain. The state of an account is a tuple containing four fields:

1.  **Nonce:** A scalar value.
    *   For an **EOA**, this is the number of transactions sent from this account. It prevents replay attacks.
    *   For a **CA**, this is the number of contracts created by this account. (Sometimes referred to as the number of times its code has been executed in a certain context).
2.  **Balance:** The number of Wei (1 Ether = 10¹⁸ Wei) owned by this account address.
3.  **storageRoot:** A 256-bit hash of the root node of a Merkle Patricia Trie. This tree encodes the internal storage contents of the contract. For EOAs, this field is empty.
4.  **codeHash:** The hash of the EVM (Ethereum Virtual Machine) code for this account.
    *   For a **Contract Account**, this is the hash of the code that is immutable and stored on-chain.
    *   For an **EOA**, this field is the hash of the empty string (`c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470`).

### How Transactions Work Between Accounts

The flow of interaction is typically initiated by an EOA.

1.  A user signs a transaction with their **private key** from their EOA.
2.  The transaction is broadcast to the network. It contains the recipient's address, the amount of ETH to send, data to call a contract function, gas limit, and gas price.
3.  A validator includes the transaction in a block and executes it.
4.  If the recipient is an **EOA**, the balance is simply transferred.
5.  If the recipient is a **Contract Account**, the data field of the transaction is interpreted as a function call, and the contract's code is executed by the EVM. This execution can change the state of the contract's storage, create new contracts, or send funds.

## Key Points & Summary

| Aspect | Description |
| :--- | :--- |
| **Two Types** | **EOAs** (user-controlled) and **Contract Accounts** (code-controlled). |
| **Control Mechanism** | EOAs are controlled by a **private key**. CAs are controlled by their **smart contract code**. |
| **Initiation** | All blockchain actions (txns, contract calls) must originate from an **EOA**. |
| **Account State** | Defined by four fields: **Nonce**, **Balance**, **storageRoot**, and **codeHash**. |
| **Nonce Purpose** | Prevents double-spending and replay attacks for EOAs; tracks creations for CAs. |
| **Address Derivation** | EOA address is the last 20 bytes of the `Keccak-256` hash of the public key. |

In summary, the account model provides a versatile framework for managing identity and state on a blockchain. EOAs represent users, while Contract Accounts represent decentralized applications and logic. This distinction is crucial for engineers developing and interacting with smart contracts and decentralized systems.