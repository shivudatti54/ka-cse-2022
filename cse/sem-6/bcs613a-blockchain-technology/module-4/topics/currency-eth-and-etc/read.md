# Module 4: Blockchain Technology - Currency (ETH and ETC)

## Introduction

In the world of blockchain, currency is often the primary application and the driving force behind a network's security and functionality. While Bitcoin pioneered digital cash, Ethereum introduced a revolutionary concept: a **programmable blockchain**. This module delves into the two primary currencies associated with the Ethereum ecosystem: **Ether (ETH)** on the Ethereum Mainnet and **Ethereum Classic (ETC)**, which originated from a significant historical event in blockchain—The DAO hack and the subsequent hard fork.

## Core Concepts

### 1. Ether (ETH) - The Fuel of Ethereum

Ether (ETH) is the native cryptocurrency of the **Ethereum Mainnet**. It is far more than just digital money; it is the essential resource that powers the entire network.

- **Function as "Gas":** Every computation, storage operation, and transaction on the Ethereum network requires computational resources. To prevent spam and allocate resources fairly, each operation has a cost, denominated in **gas**. Ether is used to pay for this gas. The total transaction fee is calculated as `Gas Units Used * Gas Price (in ETH)`. This mechanism ensures the network remains secure and efficient.
- **Store of Value and Medium of Exchange:** Like Bitcoin, ETH can be held as a store of value and used to transfer funds between parties. Its value is derived from its utility within the ecosystem.
- **Staking and Network Security:** With the transition to Ethereum 2.0 and the Proof-of-Stake (PoS) consensus mechanism, ETH took on a new critical role. Users can **stake** their ETH to become validators who propose and attest to new blocks. In return, they earn staking rewards. This process secures the network and issues new ETH, replacing the energy-intensive mining process of Proof-of-Work (PoW).

**Example:** To deploy a smart contract for a new token, a developer might pay a transaction fee of 0.05 ETH. This fee is paid to the validators who process and secure that transaction on the blockchain.

### 2. Ethereum Classic (ETC) - The Original Chain

Ethereum Classic is the original Ethereum blockchain that continued uninterrupted after a major ideological split in 2016.

- **Origin - The DAO Hack:** The split was a response to "The DAO" event. A decentralized autonomous organization (The DAO) raised a massive amount of ETH but was exploited due to a smart contract vulnerability. Millions of ETH were drained.
- **The Fork:** To recover the stolen funds, the Ethereum community proposed a **hard fork** that would effectively reverse the fraudulent transactions. This was highly controversial. The majority of the community supported the fork, which created the new chain we now know as **Ethereum (ETH)**.
- **Ideological Stance:** A minority of the community believed that "code is law" and that blockchain transactions should be immutable and irreversible, even in the case of a hack. They continued to mine the original chain, which was renamed **Ethereum Classic (ETC)**.
- **Technical Differences:** ETC has remained committed to the original **Proof-of-Work** consensus mechanism. Its development path and community are separate from ETH. While it also supports smart contracts, its ecosystem and value are significantly smaller.

**Analogy:** Imagine a book of records (the blockchain). A major error is discovered (the hack). One group decides to create a new edition of the book with the error corrected (ETH). The other group insists on preserving the original, unaltered book, errors and all, on the principle of historical record-keeping (ETC).

### Key Differences Between ETH and ETC

| Feature                   | **Ether (ETH)**                            | **Ethereum Classic (ETC)**                           |
| :------------------------ | :----------------------------------------- | :--------------------------------------------------- |
| **Blockchain**            | The forked chain (new chain)               | The original chain (continued)                       |
| **Consensus**             | **Proof-of-Stake (PoS)**                   | **Proof-of-Work (PoW)**                              |
| **Philosophy**            | Pragmatic, adaptable governance            | "Code is Law" - Immutability above all               |
| **Market Cap & Adoption** | Very high (2nd largest crypto)             | Significantly lower                                  |
| **Development**           | Large, active community and developer base | Smaller, dedicated community                         |
| **Primary Function**      | Fuel for dApps & DeFi on the mainnet       | Digital cash & smart contracts on the original chain |

## Key Points and Summary

- **Ether (ETH)** is the native currency of the forked Ethereum Mainnet. It functions as "gas" for transactions and smart contracts and is used for staking to secure the network under its current Proof-of-Stake model.
- **Ethereum Classic (ETC)** is the cryptocurrency of the original, unforked Ethereum blockchain. It continues to use Proof-of-Work and embodies the principle of **immutability**.
- The split between ETH and ETC was not a technical failure but a **philosophical and ideological** concerning governance and the response to a crisis (The DAO hack).
- The key practical difference for users and developers lies in their **consensus mechanisms** (PoS vs. PoW), **ecosystem size**, and **security models**.
- Understanding the history of ETH and ETC is crucial for grasping the broader themes of blockchain governance, immutability, and the evolution of decentralized systems.

This event remains one of the most important case studies in blockchain, demonstrating the real-world challenges of maintaining a decentralized network when community consensus breaks down.
