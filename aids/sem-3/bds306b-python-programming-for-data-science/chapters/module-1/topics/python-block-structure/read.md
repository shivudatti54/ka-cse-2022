# Bitcoin Block Structure

A Bitcoin block is the fundamental data structure that forms the blockchain. It is a container that holds a batch of valid transactions, along with a header containing metadata used to link it to the previous block and secure the network through proof-of-work.

## Block Header

The block header is an 80-byte segment that contains the summary information for the entire block. It is the component that is hashed repeatedly during the mining process. The header consists of six fields:

| Field | Size (Bytes) | Description |
| :--- | :--- | :--- |
| **Version** | 4 | The block version number that dictates which rules to follow. |
| **Previous Block Hash** | 32 | A double SHA-256 hash of the previous block's header. This creates the chain. |
| **Merkle Root** | 32 | A hash derived from all the transactions in the block. |
| **Timestamp** | 4 | The current Unix epoch time when the miner started hashing the header. |
| **Bits (nBits)** | 4 | The compressed form of the **target threshold** for this block. |
| **Nonce** | 4 | A 32-bit (4-byte) number that miners change to try to get a hash of the block header that is below the target. |

### The Mining Process (Proof-of-Work)
Miners take the block header and repeatedly hash it using the SHA-256 algorithm. They vary the **Nonce** and other fields (like the timestamp and the coinbase transaction) to try to find a hash that is numerically lower than the **target** defined by the **Bits** field.

```
Block Header Hash = SHA256(SHA256(Version + PrevHash + MerkleRoot + Timestamp + Bits + Nonce))
```

If the resulting hash is below the target, the miner has found a valid block and broadcasts it to the network. Other nodes can easily verify the proof by hashing the provided header once and checking it against the target.

## Block Body (Transactions)

The body of the block contains the list of transactions. The first transaction in any block is always the **coinbase transaction**, which creates new bitcoin and pays the block reward (subsidy + transaction fees) to the miner.

### Merkle Trees
The **Merkle Root** in the header is a critical component that efficiently and securely summarizes all the transactions. Transactions are hashed, then paired, hashed again, and so on, until a single hash remains: the Merkle Root.

```
Diagram of a Merkle Tree:

Transaction Hashes:   TxA       TxB       TxC       TxD
                       |          |         |          |
First Hash Pair:    Hash(HashA + HashB)   Hash(HashC + HashD)
                         |                     |
Final Hash:        Hash( Hash(HashA+HashB) + Hash(HashC+HashD) ) = Merkle Root
```

This structure allows for **Merkle Proofs**: a method to prove that a specific transaction (TxC) is included in a block without needing to download the entire block. A node only needs the block header and a small path of hashes (a "Merkle path") to verify inclusion.

## Block Size and Weight
Initially, Bitcoin had a simple 1 MB limit on block size. With the introduction of Segregated Witness (SegWit), a new measure called **block weight** was introduced.

*   **Non-SegWit data** (witness data) is counted as 1 "weight unit" per byte.
*   **SegWit data** (signature data) is counted as 4 "weight units" per byte.

The maximum block weight is 4,000,000 weight units, which effectively allows for blocks larger than 1 MB (typically around 1.3-1.8 MB, though theoretically up to 4 MB if filled only with witness data).

## Connecting Blocks: The Blockchain

The **Previous Block Hash** field is what cryptographically links each block to its predecessor. Changing any transaction in a past block would change its Merkle Root, thus changing its header hash. This would break the link to the next block, forcing a recalculation of that block's proof-of-work, and every block after it. This is what makes the blockchain **immutable**.

```
Block 1: Header_Hash_001
          |
Block 2: Prev_Hash = Header_Hash_001 -> Header_Hash_002
          |
Block 3: Prev_Hash = Header_Hash_002 -> Header_Hash_003
```

## Genesis Block
The first block in the Bitcoin blockchain, mined by Satoshi Nakamoto in January 2009. It is hardcoded into the software. Its previous block hash is all zeros, as there was no block before it.

### Key Takeaways:
*   A **block** is a **header** + a list of **transactions**.
*   The **header** contains the link to the previous block and the **Merkle Root** which summarizes all transactions.
*   The **Nonce** and **Target (Bits)** are central to the **proof-of-work** mining process.
*   **Merkle Trees** enable efficient and secure verification of transaction inclusion in a block.
*   The **Previous Block Hash** field creates the cryptographic chain that ensures immutability.

**Exam Tip:** Be able to draw and label the structure of the block header. Understand the role of each field, especially how the Previous Block Hash and Merkle Root work. You will almost certainly be asked to explain proof-of-work and how the Nonce and Target are used.