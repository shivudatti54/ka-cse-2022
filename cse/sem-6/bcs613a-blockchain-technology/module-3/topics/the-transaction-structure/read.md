# Module 3: The Transaction Structure in Blockchain

## Introduction

In the world of blockchain, a transaction is far more than just a payment. It is the fundamental unit of operation that represents any state change on the distributed ledger. For Bitcoin, this means the transfer of value (coins) between parties. For Ethereum or other smart contract platforms, a transaction could involve deploying a smart contract or executing a function within one. Understanding the intricate structure of a transaction is crucial for grasping how blockchain achieves its core properties of decentralization, transparency, and immutability.

## Core Concepts of a Transaction Structure

A transaction is a cryptographically signed data structure that is broadcast to the network and, if valid, included in a block. While the exact structure can vary between blockchains (e.g., Bitcoin vs. Ethereum), they share common foundational components.

### 1. Transaction Input(s)

Think of an input as a pointer to the source of the funds or data you want to spend. You cannot create value out of thin air; you must prove you possess unspent coins from a previous transaction.

- **Previous Transaction Hash (Txid):** The unique hash (identifier) of the transaction where you previously received the coins you now wish to spend.
- **Output Index (Vout):** A transaction can have multiple outputs (e.g., sending to multiple addresses). The output index specifies _which_ output from the previous transaction you are using.
- **Unlocking Script (ScriptSig):** This is the most critical part. It contains the cryptographic proof that you are the owner of the funds you are trying to spend. Typically, this includes your digital signature and your public key. It "unlocks" the funds held in the previous output.

### 2. Transaction Output(s)

An output defines the destination and conditions for spending the coins or data in the future. It essentially creates new unspent funds (UTXOs - Unspent Transaction Outputs).

- **Amount:** The quantity of cryptocurrency (e.g., Satoshis for Bitcoin, Wei for Ether) being sent to this output.
- **Locking Script (ScriptPubKey):** This script sets the rules for how the output can be spent later. It is a puzzle that must be solved by the future spender. Most commonly, it contains the recipient's public key hash (address), meaning only the holder of the corresponding private key can create a signature to unlock it.

### 3. Transaction Metadata

This is additional data required to process and validate the transaction.

- **Transaction Version:** Specifies which set of rules the transaction follows.
- **Input Count & Output Count:** The number of inputs and outputs in the transaction.
- **Locktime:** An optional field that defines the earliest time or block number at which the transaction can be added to the blockchain.

## The Lifecycle of a Transaction: A Simplified Example

Let's follow a simple Bitcoin transaction from **Alice** to **Bob** for **0.5 BTC**.

1. **Reference:** Alice's wallet finds a previous transaction where she received 1.0 BTC (Txid: `abc123...`, Output Index: `0`). This is her input.
2. **Construction:**

- **Input:** `Txid: abc123..., Index: 0, ScriptSig: [Alice's Signature + Public Key]`
- **Outputs:** The transaction creates two new outputs.
- **Output 1:** `Amount: 0.5 BTC, ScriptPubKey: [Bob's Public Key Hash]` (Payment to Bob)
- **Output 2:** `Amount: 0.4995 BTC, ScriptPubKey: [Alice's Public Key Hash]` (Change back to Alice; the small difference is the network fee).

3. **Signing:** Alice cryptographically signs the entire transaction with her private key, proving she owns the input.
4. **Propagation:** The signed transaction is broadcast to the Bitcoin network.
5. **Validation:** Network nodes (miners) verify the transaction:

- Is the signature valid?
- Does the input exist and is it unspent?
- Does the sum of inputs (1.0 BTC) equal the sum of outputs (0.5 + 0.4995 + 0.0005 fee)?

6. **Mining:** Once validated, miners include it in a new block. After the block is mined and added to the chain, the transaction is considered confirmed. The original input (`abc123..., index 0`) is now marked as spent, and the new outputs to Bob and Alice become new UTXOs available for future transactions.

## Ethereum's Account-Based Model

It's important to note that Ethereum uses an **account-based model** instead of Bitcoin's UTXO model. An Ethereum transaction has a different structure, including fields like:

- `nonce`: A count of transactions sent from the account to prevent replay attacks.
- `gasPrice`: Price per unit of computational effort.
- `gasLimit`: Maximum computational effort allowed.
- `to`: The recipient address (or a zero-address for contract creation).
- `data`: Used for smart contract function calls.

## Key Points & Summary

| Feature              | Description                                                                                                                                                                       |
| :------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Purpose**          | A transaction is a signed data structure that initiates a state change on the blockchain ledger.                                                                                  |
| **Core Components**  | **Inputs** (source of funds), **Outputs** (destination of funds + spending conditions), and **Metadata**.                                                                         |
| **Immutability**     | Once confirmed in a block, a transaction cannot be altered or reversed, ensuring a permanent record.                                                                              |
| **Verification**     | Nodes validate transactions by checking cryptographic signatures and ensuring no double-spending occurs.                                                                          |
| **UTXO vs. Account** | **Bitchain (UTXO):** Transactions chain together inputs and outputs like links. **Ethereum (Account):** Transactions update account balances and state, similar to a bank ledger. |
| **Transparency**     | All transaction data (except the content of certain scripts) is public and auditable by anyone on the network.                                                                    |

In summary, the transaction is the atomic building block of any blockchain. Its structured design, combining cryptographic proofs with a clear definition of value movement, is what enables trustless peer-to-peer interactions without the need for a central authority.
