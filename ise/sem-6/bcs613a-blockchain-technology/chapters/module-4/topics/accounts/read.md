# Module 4: Blockchain Accounts

## Introduction

In traditional financial systems, your identity is managed by a bank, which holds your account information and transaction history. Blockchain technology, particularly in platforms like Ethereum, fundamentally reimagines this concept through a user-centric model known as **accounts**. Understanding blockchain accounts is crucial for grasping how users interact with a decentralized network, hold assets, and execute smart contracts. This module delves into the two primary types of accounts: Externally Owned Accounts (EOAs) and Contract Accounts.

## Core Concepts

Blockchain accounts are the entry points for interacting with a blockchain network. They are identified by a unique address and hold a balance of the native cryptocurrency (e.g., ETH). There are two distinct types:

### 1. Externally Owned Accounts (EOAs)

An Externally Owned Account (EOA) is an account controlled by a private key, which is typically owned by a human user or an external entity.

*   **Control:** Controlled by a **private key**. Whoever possesses the private key has absolute control over the account and its funds.
*   **Creation:** Created by a user using a wallet application (e.g., MetaMask). The wallet generates a cryptographically linked **private key** and **public key**. The account's **address** is derived from the public key (often the last 20 bytes of the Keccak-256 hash of the public key).
*   **Functionality:**
    *   Can hold a balance of cryptocurrency.
    *   Can send transactions (transfer value) to other EOAs.
    *   Can send transactions that trigger or interact with smart contract code (Contract Accounts). This is how users initiate actions on dApps (decentralized applications).
*   **No Code:** EOAs do not have any associated code or smart contract logic.

**Example:** Imagine Alice wants to send 1 ETH to Bob.
1.  Alice's wallet software (holding her private key) creates a transaction specifying Bob's address and the amount.
2.  The transaction is signed with her private key to prove ownership.
3.  The signed transaction is broadcast to the Ethereum network.
4.  Miners/Validators execute the transaction, deducting 1 ETH from Alice's EOA and crediting it to Bob's EOA.

### 2. Contract Accounts (CAs)

A Contract Account is an account that is controlled by its own internal code (a smart contract), not by a private key.

*   **Control:** Controlled by its **smart contract code**. The logic embedded within the code dictates what the account can do. It can only act when triggered by a transaction from an EOA (or another CA).
*   **Creation:** Created through a special transaction from an EOA. When a user deploys a smart contract to the blockchain, a new Contract Account is generated at a new address.
*   **Functionality:**
    *   Can hold a balance of cryptocurrency, just like an EOA.
    *   Has associated smart contract code.
    *   Can send transactions in response to receiving a transaction. This allows smart contracts to call other smart contracts, creating complex, automated workflows.
*   **Key Differentiator:** The presence of code. The behavior of a CA is predetermined by its deployed code.

**Example:** Consider a simple `Crowdfunding` smart contract.
1.  An EOA deploys the `Crowdfunding` contract, creating a new Contract Account (CA) at address `0x123...`.
2.  Users (EOAs) send ETH to the CA's address (`0x123...`) by triggering a function in its code (e.g., `contribute()`).
3.  The CA's code automatically executes: it records each contributor's address and amount, and holds the funds.
4.  Once a funding goal is met, the project owner (an EOA) can trigger a `payout()` function. The CA's code then automatically sends the collected funds to the owner's address. All this logic is executed autonomously based on the pre-written code.

### Interaction Between Accounts

The power of blockchain is unlocked through the interaction between EOAs and CAs.
*   An **EOA** can send a transaction to a **CA**, invoking one of its functions.
*   During execution, a **CA** can send a transaction to another **CA**, creating a chain of calls.
*   All state changes resulting from these interactions are recorded immutably on the blockchain.

## Key Points / Summary

| Feature | Externally Owned Account (EOA) | Contract Account (CA) |
| :--- | :--- | :--- |
| **Control** | Private Key | Smart Contract Code |
| **Creation** | Via Wallet (Free) | Via Deployment Transaction (Costs Gas) |
| **Contains Code?** | No | Yes |
| **Can Initiate a Transaction?** | **Yes** | No (only react to transactions) |
| **Purpose** | Represent users, hold funds, initiate actions | Execute predefined logic, power dApps |

*   **Accounts** are the fundamental entities for interaction on a blockchain.
*   The two types are **Externally Owned Accounts (EOAs)** (user-controlled) and **Contract Accounts (CAs)** (code-controlled).
*   **EOAs** are created for free and are needed to initiate any transaction on the network.
*   **CAs** are created by deploying smart contracts, which costs gas, and their behavior is governed by their code.
*   **dApps** are built by designing interactions between EOAs and one or more smart contracts (CAs).