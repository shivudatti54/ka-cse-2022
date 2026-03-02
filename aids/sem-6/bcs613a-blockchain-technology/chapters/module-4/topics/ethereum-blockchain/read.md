# Module 4: Ethereum Blockchain

## Introduction

While Bitcoin pioneered the concept of a decentralized digital currency, its scripting language is limited and purpose-built. **Ethereum**, proposed in 2013 by Vitalik Buterin and launched in 2015, revolutionized the blockchain space by introducing a **Turing-complete**, programmable blockchain. Think of it as a global, decentralized computer. Instead of just tracking currency transactions, Ethereum allows developers to build and deploy **Decentralized Applications (dApps)** and **smart contracts**, enabling a vast array of use cases beyond simple payments.

## Core Concepts

### 1. Smart Contracts

A smart contract is a self-executing contract with the terms of the agreement directly written into code. It automatically executes predefined actions when specific conditions are met.

*   **Analogy:** Imagine a digital vending machine. You send it the exact amount of cryptocurrency (condition), and it automatically dispenses the chosen item (action) without needing a human intermediary.
*   **Key Property:** Once deployed to the Ethereum network, a smart contract is immutable and will run exactly as programmed, providing trustlessness and censorship resistance.

### 2. Ether (ETH) and Gas

*   **Ether (ETH):** This is the native cryptocurrency of the Ethereum network. It is used to pay for transaction fees and computational services on the network. It is the "fuel" that powers the ecosystem.
*   **Gas:** Every computation on the Ethereum Virtual Machine (EVM) has a cost, measured in **Gas**. Gas is the unit that measures the computational effort required to execute operations like transactions or smart contract functions.
    *   `Total Transaction Fee = Gas Used * Gas Price (in Gwei)`
    *   **Gwei** is a denomination of ETH (1 ETH = 1,000,000,000 Gwei). Users set the `Gas Price` to incentivize miners to include their transaction in a block. This mechanism prevents network spam and allocates resources efficiently.

### 3. Ethereum Virtual Machine (EVM)

The EVM is the global, decentralized runtime environment that executes smart contracts. It is the core of Ethereum.

*   **Purpose:** Every Ethereum node runs an instance of the EVM. This ensures that regardless of the hardware or operating system, every node processes smart contracts in exactly the same way, maintaining consensus across the entire network.
*   **Sandboxed Environment:** The EVM is completely isolated from the network, filesystem, and other processes of the host system, making it a secure environment for executing untrusted code.

### 4. Accounts

Unlike Bitcoin's UTXO model, Ethereum uses an **account-based model**. There are two types of accounts:

1.  **Externally Owned Accounts (EOAs):** These are accounts controlled by private keys, owned by users. They can:
    *   Hold ETH balance.
    *   Send transactions (transfer ETH or trigger a smart contract function).
    *   They have no associated code.
2.  **Contract Accounts:** These are smart contracts deployed on the network. They:
    *   Have their own ETH balance.
    *   Have associated code (smart contract).
    *   Can only execute transactions in response to a transaction received from an EOA or another contract.

**Example:** You (an EOA) send a transaction to a DeFi lending contract (a Contract Account) to deposit ETH. This transaction triggers the contract's `deposit()` function, which updates its internal ledger to reflect your deposit.

### 5. Consensus Mechanism: From Proof-of-Work to Proof-of-Stake

Ethereum initially used a **Proof-of-Work (PoW)** consensus mechanism, much like Bitcoin. However, in September 2022, it underwent "The Merge," transitioning to **Proof-of-Stake (PoS)**.

*   **Proof-of-Stake (PoS):** In PoS, validators (instead of miners) lock up (stake) a amount of ETH (32 ETH to be an individual validator) to participate in validating transactions and creating new blocks.
*   **Benefits:** This shift drastically reduced Ethereum's energy consumption (~99.95%) and introduced greater security and scalability, paving the way for future upgrades like sharding.

### 6. dApps and ERC Standards

*   **Decentralized Applications (dApps):** These are applications that run on a P2P network of computers rather than a single central server. Their backend code (smart contracts) runs on the decentralized Ethereum blockchain. Examples include Uniswap (decentralized exchange) and Compound (lending protocol).
*   **ERC Standards:** Ethereum Request for Comments (ERC) are technical standards for Ethereum smart contracts. They ensure interoperability between contracts and dApps.
    *   **ERC-20:** The most common standard for creating fungible tokens (e.g., USDC, DAI, UNI).
    *   **ERC-721:** The standard for non-fungible tokens (NFTs), where each token is unique (e.g., CryptoPunks, Bored Ape Yacht Club).

## Key Points & Summary

| Concept | Description | Importance |
| :--- | :--- | :--- |
| **Smart Contracts** | Self-executing code deployed on the blockchain. | Enables programmable agreements and dApps. |
| **Ether (ETH) & Gas** | Native cryptocurrency and unit for measuring computational cost. | Powers the network and prevents spam. |
| **EVM** | Global, decentralized runtime environment. | Ensures consistent execution of code across all nodes. |
| **Account Model** | EOAs (user-controlled) and Contract Accounts (smart contracts). | Manages state and allows interaction with the network. |
| **Consensus (PoS)** | Validators stake ETH to secure the network and create blocks. | Makes Ethereum more energy-efficient and scalable. |
| **dApps & ERC Standards** | Applications built on Ethereum and technical standards for tokens. | Creates a rich ecosystem of interoperable applications. |

**In summary,** Ethereum is a foundational, programmable blockchain platform that extends the utility of blockchain technology far beyond cryptocurrency. Its core innovations—the EVM, smart contracts, and a robust account system—provide the infrastructure for a new wave of decentralized finance, applications, and digital ownership.