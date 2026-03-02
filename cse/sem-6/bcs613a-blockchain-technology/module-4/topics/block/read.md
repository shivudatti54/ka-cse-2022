# Block

## Introduction

In the context of Ethereum, a block is a collection of transactions that are verified and validated by the network. It is a fundamental component of the Ethereum blockchain, which is a decentralized, distributed ledger that records all transactions on the network. In this chapter, we will delve into the concept of a block, its structure, and its significance in the Ethereum ecosystem.

## Block Structure

A block in Ethereum consists of several key components:

### 1. Block Header

The block header contains metadata about the block, such as:

- Block number: a unique identifier for the block
- Parent hash: the hash of the previous block in the chain
- Timestamp: the time at which the block was created
- Gas limit: the maximum amount of gas that can be spent in the block
- Gas used: the amount of gas actually used in the block
- Hash: a unique identifier for the block

### 2. Transaction List

The transaction list contains a list of transactions that are included in the block. Each transaction is represented by a transaction hash, which is a unique identifier for the transaction.

### 3. Block Body

The block body contains the actual data for each transaction in the block. This includes the sender, recipient, value, and any additional data that is required for the transaction.

## Block Creation

Blocks are created by miners, who are responsible for validating and verifying transactions on the network. The process of creating a block is as follows:

1. Miners collect a list of unconfirmed transactions from the network.
2. Miners verify the transactions to ensure that they are valid and follow the rules of the network.
3. Miners create a new block and add the verified transactions to it.
4. Miners calculate the hash of the block header and add it to the block.
5. Miners broadcast the new block to the network.

## Block Validation

When a new block is broadcast to the network, it must be validated by other nodes on the network. This involves verifying the following:

- The block header is valid and correctly formatted.
- The transactions in the block are valid and follow the rules of the network.
- The block hash is correct and matches the hash of the block header.

## Block Chain

The block chain is the sequence of blocks that make up the Ethereum blockchain. Each block is linked to the previous block through its parent hash, which creates a permanent and unalterable record of all transactions on the network.

## Exam Tips

- A block is a collection of transactions that are verified and validated by the network.
- The block header contains metadata about the block, such as the block number, parent hash, and timestamp.
- The transaction list contains a list of transactions that are included in the block.
- Blocks are created by miners, who are responsible for validating and verifying transactions on the network.
- The block chain is the sequence of blocks that make up the Ethereum blockchain.
- Each block is linked to the previous block through its parent hash.
