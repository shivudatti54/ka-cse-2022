**Module 4: Ethereum Blockchain**
**Subject: Blockchain Technology**

### 1. Introduction to Ethereum

While Bitcoin pioneered the concept of a decentralized digital currency, Ethereum, proposed by Vitalik Buterin in 2013 and launched in 2015, expanded this idea into a general-purpose decentralized computing platform. Often termed as a **"world computer,"** Ethereum is not merely a cryptocurrency but a global, open-source platform for decentralized applications (DApps). Its native cryptocurrency, Ether (ETH), is used primarily to power these applications and compensate participants for computations.

---

### 2. Core Concepts of Ethereum

#### a. Smart Contracts
This is the foundational innovation of Ethereum. A smart contract is a self-executing contract where the terms of the agreement are written directly into code. These contracts run exactly as programmed without any possibility of downtime, censorship, fraud, or third-party interference. They automatically execute actions when predetermined conditions are met.

*   **Example:** Imagine a simple vending machine. You (the user) send it money (ETH) and specify a choice (e.g., A4 for chips). The machine's internal mechanism (the smart contract logic) automatically verifies the payment and dispenses the item. No human intervention is required.

#### b. Ethereum Virtual Machine (EVM)
The EVM is the runtime environment for smart contracts in Ethereum. It is a massive, decentralized computer comprised of all the nodes participating in the Ethereum network. Its key characteristic is **determinism**: given an input and a state, the EVM will always produce the same output. This ensures that all nodes on the network reach consensus on the results of contract execution. Every operation on the EVM has a cost, measured in "gas."

#### c. Gas and Gas Fees
Since the EVM performs computations using the resources of thousands of nodes, it must be protected from abuse (like infinite loops). **Gas** is the unit that measures the computational effort required to execute operations, like a transaction or a smart contract function.

*   Each operation (e.g., adding numbers, storing data) has a fixed gas cost.
*   Users specify a **gas price** (in Gwei, where 1 Gwei = 10⁻⁹ ETH) they are willing to pay per unit of gas.
*   **Total Fee = Gas Used * Gas Price**

This mechanism compensates miners/validators for their work and prevents network spam.

#### d. Accounts
Unlike Bitcoin's UTXO model, Ethereum uses an **account-based model**, similar to a bank account. There are two types of accounts:

1.  **Externally Owned Accounts (EOAs):** Controlled by anyone with the private keys. They can hold ETH and initiate transactions (e.g., transfer ETH, trigger a contract).
2.  **Contract Accounts:** Controlled by their contract code. They have their own address, can hold ETH, and have associated code. They only execute transactions when triggered by an EOA.

#### e. Consensus Mechanisms: From PoW to PoS
Ethereum initially used a **Proof-of-Work (PoW)** consensus mechanism, similar to Bitcoin, where miners competed to solve complex puzzles. However, in September 2022, Ethereum underwent "The Merge," a monumental upgrade transitioning its consensus mechanism to **Proof-of-Stake (PoS)**.

*   **Proof-of-Stake (PoS):** In PoS, validators (not miners) are chosen to create new blocks and validate transactions based on the amount of ETH they "stake" (lock up) as collateral. This is far more energy-efficient than PoW and allows for future scalability upgrades like sharding.

#### f. Decentralized Applications (DApps) and Tokens
Smart contracts are the backend code for DApps. These applications have their frontend (UI) built with traditional web tech (HTML/JS) but interact with the blockchain via libraries like Web3.js. Ethereum also enables the creation of other digital assets:

*   **ERC-20 Tokens:** A technical standard for creating fungible (interchangeable) tokens on Ethereum. Most cryptocurrency projects (e.g., USDT, UNI, LINK) are ERC-20 tokens.
*   **ERC-721 Tokens:** The standard for non-fungible tokens (NFTs), representing ownership of unique digital or physical assets like art, collectibles, or real estate.

---

### 3. Key Points & Summary

| Feature | Description |
| :--- | :--- |
| **Primary Innovation** | A programmable blockchain supporting **Smart Contracts** and **DApps**. |
| **Native Currency** | **Ether (ETH)**, used for paying transaction fees (gas) and as a store of value. |
| **Runtime Environment** | **Ethereum Virtual Machine (EVM)** ensures deterministic execution of code. |
| **Fee Mechanism** | **Gas** is paid to execute operations, preventing spam and compensating validators. |
| **Account Model** | **Account-based** with two types: Externally Owned Accounts (EOAs) and Contract Accounts. |
| **Consensus** | Transitioned from **Proof-of-Work (PoW)** to energy-efficient **Proof-of-Stake (PoS)**. |
| **Key Standards** | **ERC-20** (for fungible tokens) and **ERC-721** (for NFTs). |

Ethereum's transition to a Proof-of-Stake consensus mechanism marks a significant evolution, making it more scalable, secure, and sustainable. It remains the leading platform for decentralized finance (DeFi), NFTs, and a vast ecosystem of innovative DApps, forming the backbone of Web3.