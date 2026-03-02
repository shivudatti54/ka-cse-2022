# Module 4: Elements of the Ethereum Blockchain

## Introduction

While Bitcoin pioneered decentralized digital currency, **Ethereum** expanded the concept into a general-purpose, programmable blockchain. It is often described as a **"world computer"**—a decentralized platform that allows developers to build and deploy smart contracts and decentralized applications (dApps). Understanding its core architectural elements is fundamental for any blockchain engineer.

---

## Core Concepts of the Ethereum Blockchain

### 1. Ether (ETH) and Gas

- **Ether (ETH):** The native cryptocurrency of the Ethereum network. It is used to pay for transaction fees and computational services on the network. It is the incentive that keeps the network secure and operational.
- **Gas:** A fundamental concept representing the **cost of computation**. Every operation on the Ethereum Virtual Machine (EVM) has a gas cost. Complex transactions (like deploying a smart contract) require more gas than simple ones (like sending ETH).
- **Gas Price:** The amount of ETH (in Gwei, where 1 Gwei = 10⁻⁹ ETH) you are willing to pay per unit of gas. It is set by the user and acts like a bid; a higher gas price incentivizes miners to include your transaction faster.
- **Gas Limit:** The maximum amount of gas you are willing to spend on a transaction. This prevents runaway contracts from spending all your ETH due to an error.

**Example:** Sending ETH may cost 21,000 gas. If the gas price is 50 Gwei, the total fee is:
`21,000 gas * 50 Gwei = 1,050,000 Gwei = 0.00105 ETH`.

### 2. Accounts

Unlike Bitcoin's UTXO model, Ethereum uses an **account-based model**. There are two types of accounts:

- **Externally Owned Accounts (EOAs):** Controlled by a private key. They can:
- Hold ETH balance.
- Send transactions (transfer ETH or trigger a contract).
- Have no associated code.
- **Contract Accounts (CAs):** Controlled by their contract code. They can:
- Hold ETH balance.
- Have associated code (smart contract).
- Execute code when receiving a transaction from an EOA or another CA.
- **Cannot initiate transactions on their own;** they can only react.

Every account has a persistent **state** (balance, nonce, storage root, and code hash for CAs).

### 3. The Ethereum Virtual Machine (EVM)

The **EVM** is the heart of Ethereum. It is a decentralized, Turing-complete virtual machine that exists on every node in the network. Its purpose is to execute contract bytecode. Key properties:

- **Isolated Sandbox:** Code execution is completely isolated from the network, filesystem, or other processes of the host machine.
- **Deterministic:** The same input to the EVM will always produce the same output, ensuring all nodes can reach consensus on the state of the blockchain.
- **Stack-based:** It uses a 256-bit stack architecture, making it naturally suited for cryptographic operations.

### 4. Smart Contracts

A **smart contract** is a program stored on the blockchain that runs exactly as programmed without the possibility of censorship, downtime, or third-party interference. They are written in high-level languages like **Solidity** or **Vyper**, compiled into EVM bytecode, and deployed to the blockchain.

**Example:** A simple smart contract written in Solidity to act as a digital "piggy bank":
