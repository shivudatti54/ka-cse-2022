# Module 4: Blockchain Technology - The Ethereum Blockchain

## 1. Introduction

While Bitcoin pioneered decentralized digital currency, **Ethereum** expanded the concept of blockchain from a simple financial ledger to a **global, decentralized computer**. Proposed in 2013 by Vitalik Buterin and launched in 2015, Ethereum introduced the ability to execute complex logic and build applications (DApps) directly on its blockchain through **smart contracts**. It is the foundation for much of the modern Web3 ecosystem, including DeFi (Decentralized Finance) and NFTs (Non-Fungible Tokens).

---

## 2. Core Concepts

### 2.1. Smart Contracts
A smart contract is a self-executing program stored on the Ethereum blockchain. It automatically enforces and executes the terms of an agreement when predefined conditions are met. Unlike traditional contracts, they are immutable (once deployed) and run exactly as programmed without any possibility of censorship, downtime, or third-party interference.

*   **Example:** Imagine a simple escrow contract between a buyer (`A`) and a seller (`B`).
    1.  `A` sends 1 ETH to the smart contract address.
    2.  The contract holds the funds.
    3.  Once `B` delivers the digital product, `B` can call a function on the contract to release the funds.
    4.  The contract logic verifies the release condition and automatically sends 1 ETH to `B`'s address.

### 2.2. Ethereum Virtual Machine (EVM)
The EVM is the heart of the Ethereum network. It is a **global, decentralized runtime environment** that executes smart contract code. Every node in the Ethereum network runs an implementation of the EVM. This ensures that every contract runs identically on every machine, guaranteeing deterministic and consistent outcomes, which is critical for trust and security.

### 2.3. Gas and Gas Fees
Since every operation on the Ethereum network ( computation, storage, transactions) consumes computational resources, a metering mechanism called **Gas** is used. Each operation has a fixed gas cost.

*   **Gas Price:** The amount of Ether (ETH) you are willing to pay per unit of gas (measured in Gwei, where 1 Gwei = 10⁻⁹ ETH).
*   **Transaction Fee:** `Total Fee = Gas Used * Gas Price`
This fee is paid to validators for processing and securing the network. It prevents network spam and allocates resources efficiently.

### 2.4. Accounts
Ethereum has two types of accounts:

1.  **Externally Owned Accounts (EOAs):** Controlled by a private key. Used by users to hold and transfer ETH and to initiate transactions (e.g., triggering a smart contract function).
2.  **Contract Accounts:** Controlled by their own smart contract code. They have an associated balance and can send transactions. However, they can only execute code when triggered by a transaction from an EOA or another contract.

### 2.5. Consensus Mechanism: From Proof-of-Work to Proof-of-Stake
Ethereum initially used a **Proof-of-Work (PoW)** consensus mechanism, similar to Bitcoin, where miners solved complex puzzles to validate transactions and create new blocks.

In September 2022, Ethereum underwent "The Merge," transitioning to a **Proof-of-Stake (PoS)** consensus mechanism. In PoS:
*   Validators, not miners, are responsible for creating and attesting to blocks.
*   To become a validator, a user must **stake** a minimum of 32 ETH.
*   Validators are chosen algorithmically to propose new blocks based on the amount of ETH staked and other factors.
*   This shift drastically reduced Ethereum's energy consumption (~99.95%) and set the stage for future scalability upgrades like sharding.

### 2.6. Ether (ETH)
**Ether (ETH)** is the native cryptocurrency of the Ethereum blockchain. It is used primarily for two purposes:
1.  To pay gas fees for transactions and smart contract execution.
2.  As a store of value and a medium of exchange within the ecosystem.

---

## 3. Example: A Simple Transaction Flow

1.  **User Action:** You (using your EOA with MetaMask) want to send 0.1 ETH to a friend. You set a gas price of 20 Gwei. The base gas cost for a simple transfer is 21,000 units.
2.  **Transaction Creation:** Your wallet creates and signs a transaction.
3.  **Broadcast:** The transaction is broadcast to the Ethereum network.
4.  **Validation & Execution:** A validator node includes your transaction in a block. The EVM on each node processes the transaction, deducting `21,000 * 20 Gwei = 0.00042 ETH` as a fee from your balance and adding 0.1 ETH to your friend's balance.
5.  **Confirmation:** The block is added to the chain, and your transaction is confirmed.

---

## 4. Key Points & Summary

*   **Beyond Currency:** Ethereum is a **decentralized software platform** that enables smart contracts and DApps, going far beyond Bitcoin's financial use case.
*   **Smart Contracts:** Self-executing code that automates agreements and logic on the blockchain. They are immutable and tamper-proof.
*   **EVM:** The global computer that ensures all nodes run code identically, providing determinism and security.
*   **Gas Fees:** The cost of computation and storage on the network, paid in ETH. This prevents spam and pays validators.
*   **Proof-of-Stake:** Ethereum's current consensus mechanism is energy-efficient and relies on validators who stake ETH to secure the network.
*   **Ether (ETH):** The native fuel that powers the network, used for paying transaction fees and as a digital currency.

Ethereum's programmable nature has made it the bedrock of Web3 innovation, hosting a vast ecosystem of financial, social, and gaming applications.