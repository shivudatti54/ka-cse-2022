# Module 4: Blockchain Technology - Accounts

## Introduction

In traditional financial systems, your identity is managed by a bank; they hold your account details and transaction history. Blockchain flips this model on its head. In decentralized networks like Ethereum, the concept of an **account** is fundamental, serving as the primary point of interaction for users and smart contracts. Unlike bank accounts, they are self-sovereign, meaning you, and only you, control them using cryptographic keys. Understanding accounts is crucial for building and interacting with decentralized applications (dApps).

## Core Concepts

In Ethereum and other EVM-compatible blockchains (common in many  blockchain syllabi), there are two distinct types of accounts:

1.  **Externally Owned Accounts (EOAs)**
2.  **Contract Accounts (CAs)**

Let's break down each type.

### 1. Externally Owned Accounts (EOAs)

An EOA is an account controlled by a private key, which is typically owned by a human user. It's your gateway to the blockchain.

*   **Components:**
    *   **Address:** A 20-byte (160-bit) hexadecimal identifier derived from the public key (e.g., `0x742d35Cc6634C893292...`). This is your public identity on the network—like your bank account number, which you can share to receive funds.
    *   **Balance:** The amount of Ether (ETH) or the native cryptocurrency held by the account.
    *   **Nonce:** A counter that keeps track of the number of transactions *sent* from this account. This prevents replay attacks and ensures transaction order.

*   **Control:** Access and control are managed through a pair of cryptographic keys:
    *   **Private Key:** A secret 256-bit number kept securely by the owner. It is used to sign transactions, providing mathematical proof of ownership. **Whoever holds the private key controls the account.**
    *   **Public Key:** Derived from the private key, it is used to generate the account's address.

*   **Function:** EOAs can:
    *   Send transactions (transfer ETH/value).
    *   Trigger smart contract functions (by sending a transaction to a contract address).

**Example:** When you use MetaMask, you are creating and managing an EOA. Your public address is shared to receive funds, and your private key (or seed phrase) is stored securely in your wallet to sign outgoing transactions.

### 2. Contract Accounts (CAs)

A CA is an account associated with smart contract code, not a private key. It's deployed to the blockchain and exists at a specific address.

*   **Components:**
    *   **Address:** Also a 20-byte identifier, generated at the time of contract deployment (based on the creator's address and their nonce).
    *   **Balance:** Can hold Ether, just like an EOA.
    *   **Contract Code:** The compiled bytecode of the smart contract that defines its functions and logic.
    *   **Storage:** A permanent key-value store that persists the state of the contract's variables.

*   **Control:** A contract account has no private key. It is controlled by its own logic. It cannot initiate transactions on its own; it can only execute code in response to a transaction sent from an EOA (or another contract).

*   **Function:** Contract accounts can:
    *   Execute their programmed logic when receiving a transaction (e.g., swap tokens on a DEX, mint an NFT).
    *   Hold funds in escrow.
    *   Interact with and call other smart contracts.

**Example:** The USDT (Tether) token or a Uniswap liquidity pool are deployed as smart contracts. They each have a unique contract address. To interact with them (e.g., to transfer USDT), you send a transaction from your EOA to their contract address, triggering the appropriate function in their code.

---

### Interaction Between Accounts

The power of blockchain emerges from the interaction between these accounts:
1.  A user (using their EOA) signs and sends a transaction to a Contract Account's address.
2.  The network nodes execute the contract's code.
3.  The contract's state (its storage) is updated based on the code execution.
4.  The result is recorded immutably on the blockchain.

## Key Points & Summary

| Feature | Externally Owned Account (EOA) | Contract Account (CA) |
| :--- | :--- | :--- |
| **Control** | Private Key | Smart Contract Code |
| **Private Key?** | Yes | No |
| **Can Initiate Tx?** | **Yes** | No (only reacts) |
| **Contains Code?** | No | **Yes** |
| **Purpose** | User-owned wallet | Programmable functionality |

*   **Accounts are the fundamental entities** on the Ethereum blockchain, representing both user wallets and smart contracts.
*   **EOAs are active**; they can start transactions. They are controlled by **private keys**.
*   **CAs are passive**; they contain code and storage and only execute when called by an EOA. They have **no private key**.
*   Every transaction on the network must originate from an EOA.
*   The **nonce** is critical for maintaining transaction order and security for EOAs.
*   Both account types have a **balance** and can send/receive the native cryptocurrency.

Understanding this distinction is vital for engineering dApps, as it defines how users and applications interact with the blockchain's immutable state.