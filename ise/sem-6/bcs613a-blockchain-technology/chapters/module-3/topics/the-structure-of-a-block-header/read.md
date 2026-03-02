# Module 3: The Structure of a Block Header in Blockchain

## Introduction

In a blockchain, data is stored in a series of units called **blocks**. Each block contains a list of transactions and, crucially, a **block header**. The block header is the metadata section of a block, a compact summary that contains all the information needed to cryptographically link the block to the chain and verify its integrity. For engineering students, understanding the header's structure is fundamental to grasping how blockchain achieves its core properties of immutability, security, and decentralization.

## Core Components of a Block Header

A standard block header, as used in Bitcoin and many other cryptocurrencies, consists of six primary fields. Together, they form an 80-byte structure (in Bitcoin) that is hashed to create a unique identifier for the block.

### 1. Version (4 bytes)
This field indicates the set of validation rules the block follows. It is a simple integer that signals which software version the miner was using. Changes to this number can indicate a soft or hard fork in the network, as it allows nodes to agree on the consensus rules for validating the block.

### 2. Previous Block Hash (32 bytes)
This is arguably the most critical field. It contains the cryptographic hash (a double SHA-256 hash in Bitcoin) of the *previous block's header*. This creates the "chain" in blockchain.
*   **Function:** It cryptographically links the current block to its parent, making it computationally infeasible to alter any block without altering all subsequent blocks. This is the primary mechanism behind blockchain's immutability.

### 3. Merkle Root Hash (32 bytes)
This field is a hash of all the transactions in the current block. However, it is not a simple concatenation of transaction hashes. The transactions are hashed together using a **Merkle Tree** (or Hash Tree) structure.
*   **Process:** Individual transaction hashes are paired, hashed together, then paired again and hashed, repeatedly, until a single final hash remains—the Merkle Root.
*   **Example:** This allows for efficient and secure verification of transactions. A "lightweight" or SPV (Simplified Payment Verification) client can verify that a specific transaction is included in a block by needing only a tiny Merkle path (a handful of hashes) rather than the entire block's data.

### 4. Timestamp (4 bytes)
This is a standard Unix epoch timestamp (seconds since January 1, 1970) indicating the approximate time the block was mined. It helps maintain a chronological order for the blocks and is involved in regulating the mining difficulty adjustment.

### 5. Difficulty Target (4 bytes)
This field encodes the **Proof-of-Work (PoW)** difficulty target that the block's hash must meet. It is a condensed representation of the threshold that the new block's hash must be equal to or less than. The network adjusts this value periodically (e.g., every 2016 blocks in Bitcoin) to ensure that the average time between blocks remains consistent (e.g., ~10 minutes), regardless of the total computational power on the network.

### 6. Nonce (4 bytes)
The **Nonce** (Number Used Once) is a 4-byte field that miners change iteratively during the mining process. Since the Previous Block Hash, Merkle Root, and other fields are essentially fixed for a given set of transactions, the miner's goal is to find a Nonce value that, when combined with the other header data and hashed, produces a result that meets the Difficulty Target.
*   **Function:** It is the core of the mining process. Miners perform quintillions of hashes per second, brute-forcing different Nonce values until one solves the cryptographic puzzle.

## The Hashing Process

The entire 80-byte block header is taken as input and run through a cryptographic hash function (SHA-256 twice in Bitcoin). The output of this function is the **Block Hash**—a unique, fixed-length identifier that represents the entire block. This block hash is what must be below the difficulty target. It is also the "Previous Block Hash" that will be included in the *next* block, creating the immutable link.

## Key Points & Summary

| Field | Size (Bytes) | Description |
| :--- | :---: | :--- |
| **Version** | 4 | Indicates the block validation rules. |
| **Previous Block Hash** | 32 | The hash of the preceding block's header. Creates the chain. |
| **Merkle Root** | 32 | The root hash of the Merkle Tree of all transactions in the block. |
| **Timestamp** | 4 | Approximate creation time (Unix epoch). |
| **Difficulty Target** | 4 | The PoW difficulty target this block's hash must meet. |
| **Nonce** | 4 | A variable number miners change to solve the PoW puzzle. |

*   The block header is an **80-byte** metadata package that summarizes a block.
*   Its primary purpose is to be **hashed** to create the block's unique identifier and to form the cryptographic link in the chain via the **Previous Block Hash**.
*   The **Merkle Root** enables efficient and secure verification of any transaction within the block without needing the entire dataset.
*   The **Nonce** and **Difficulty Target** are the core components of the Proof-of-Work consensus mechanism, which secures the network and controls the rate of new block creation.
*   Any change to a transaction in the block would alter the Merkle Root, which would change the block header's hash, breaking the chain and making the tampering evident. This is the engineering foundation of **immutability**.