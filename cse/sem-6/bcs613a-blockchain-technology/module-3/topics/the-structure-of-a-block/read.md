# The Structure of a Block in Blockchain

## Introduction

A **block** is the fundamental data structure in a blockchain. Each block contains a collection of transactions and metadata that links it to the previous block, forming a chain. Understanding the structure of a block is essential to understanding how blockchains maintain integrity, security, and immutability.

## Components of a Block

Every block consists of two main parts:

1. **Block Header**: Metadata about the block
2. **Block Body**: Transaction data

```
┌─────────────────────────────────┐
│ BLOCK HEADER │
│ - Version │
│ - Previous Block Hash │
│ - Merkle Root │
│ - Timestamp │
│ - Difficulty Target (nBits) │
│ - Nonce │
├─────────────────────────────────┤
│ BLOCK BODY │
│ - Transaction Counter │
│ - Transactions │
│ • Transaction 1 │
│ • Transaction 2 │
│ • ... │
│ • Transaction N │
└─────────────────────────────────┘
```

## Block Header (80 bytes in Bitcoin)

The block header contains crucial metadata used for validation and mining.

### 1. Version (4 bytes)

**Purpose**: Indicates the block validation rules to follow.

**Example**: `0x20000000` (version 2)

**Why it matters**:

- Allows protocol upgrades
- Different versions may have different validation rules
- Nodes can determine which software version created the block

### 2. Previous Block Hash (32 bytes)

**Purpose**: Hash of the previous block's header, creating the "chain" in blockchain.

**Example**: `000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f`

**Structure**:

```
Block N-1 Hash → Block N → Block N+1
(Previous) (Current) (Next)
```

**Why it matters**:

- Links blocks together chronologically
- Any change to a previous block changes all subsequent hashes
- Ensures immutability (tampering is detectable)

**Security**:

```
If attacker modifies Block 100:
 Block 100 hash changes
 → Block 101's "previous hash" no longer matches
 → Block 101 becomes invalid
 → Entire chain from Block 101 onwards becomes invalid
```

### 3. Merkle Root (32 bytes)

**Purpose**: Hash of all transactions in the block, computed using a Merkle tree.

**Example**: `f3e94742aca4b5ef85488dc37c06c3282295ffec960994b2c0d5ac2a25a95766`

**Merkle Tree Structure**:

```
 Merkle Root
 / \
 Hash_AB Hash_CD
 / \ / \
 Hash_A Hash_B Hash_C Hash_D
 | | | |
 Tx A Tx B Tx C Tx D
```

**Why it matters**:

- Efficiently summarizes all transactions
- Enables Simplified Payment Verification (SPV)
- Any transaction modification changes the Merkle root
- Allows proof of transaction inclusion without downloading entire block

**SPV Example**:

```
Light client wants to verify Tx A:
 Needs: Hash_B, Hash_CD, Merkle Root
 Can verify without downloading Tx B, C, D
```

### 4. Timestamp (4 bytes)

**Purpose**: Approximate time when the block was mined (Unix timestamp).

**Example**: `1231006505` (January 3, 2009, 18:15:05 GMT - Bitcoin Genesis Block)

**Format**: Seconds since January 1, 1970 00:00 UTC

**Why it matters**:

- Establishes chronological order
- Used in difficulty adjustment calculations
- Prevents miners from artificially creating blocks in the past
- Network rejects blocks with timestamps > 2 hours in the future

### 5. Difficulty Target / nBits (4 bytes)

**Purpose**: The target value that the block hash must be less than for the block to be valid (Proof of Work difficulty).

**Example**: `0x1d00ffff`

**Encoding**: Compact representation of target

```
nBits = 0x1d00ffff
Expanded target = 0x00ffff * 2^(8*(0x1d - 3))
 = 0x00000000ffff0000000000000000000000000000000000000000000000000000
```

**Why it matters**:

- Adjusts mining difficulty
- Ensures blocks are mined approximately every 10 minutes (Bitcoin)
- Difficulty recalculates every 2016 blocks (~2 weeks)

**Difficulty Adjustment**:

```
New Difficulty = Old Difficulty × (2 weeks / Actual Time)

Example:
- If blocks mined too fast: Difficulty increases
- If blocks mined too slow: Difficulty decreases
```

### 6. Nonce (4 bytes)

**Purpose**: A 32-bit number that miners increment to find a valid hash.

**Example**: `2083236893`

**Mining Process**:

```
1. Construct block with transactions
2. Set nonce = 0
3. Calculate block hash
4. If hash < target:
 Valid block found! Broadcast to network.
 Else:
 Increment nonce and repeat from step 3
```

**Why it matters**:

- The "work" in Proof of Work
- Miners try billions of nonce values to find valid hash
- Provides randomness in hash computation
- No shortcuts - must be solved by brute force

**Hash Requirement**:

```
Valid Hash: 0000000000000000000a4f8b2c9e1d3f7b6a5c4e3d2f1a0b9c8d7e6f5a4b3c2d1
 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ Leading zeros
Target: 0000000000000000000fffffffffffffffffffffffffffffffffffffffffffff
 Hash must be less than target
```

## Block Body

The block body contains the actual transaction data.

### Transaction Counter (Variable size, 1-9 bytes)

**Purpose**: Indicates the number of transactions in the block.

**Example**: `0x02` (2 transactions)

**Encoding**: Variable-length integer (VarInt)

```
1-252: 1 byte
253-65535: 3 bytes (0xfd + 2 bytes)
65536-4294967295: 5 bytes (0xfe + 4 bytes)
>4294967295: 9 bytes (0xff + 8 bytes)
```

### Transactions (Variable size)

**Structure**: List of all transactions included in the block.

**First Transaction**: Always the **Coinbase transaction**

- Creates new bitcoins (block reward)
- Pays the miner
- No inputs (created from nothing)

**Remaining Transactions**: Regular transactions

- Transfer bitcoins between addresses
- Validated by miners before inclusion

**Example Block**:

```
Block 680000:
- Transaction 0 (Coinbase): Miner receives 6.25 BTC + fees
- Transaction 1: Alice sends 0.5 BTC to Bob
- Transaction 2: Charlie sends 1.2 BTC to Dave
- ...
- Transaction 2319: Final transaction
```

## Complete Block Example (Simplified)

```
Block #680000
─────────────────────────────────────────
HEADER (80 bytes):
 Version: 0x20000000
 Previous Hash: 00000000000000000009f9b170fa4...
 Merkle Root: f3e94742aca4b5ef85488dc37c06c...
 Timestamp: 1610640000 (Jan 14, 2021 12:00:00 GMT)
 nBits: 0x170d21b9
 Nonce: 2738345654

BODY (Variable size):
 Transaction Count: 2320
 Transactions:
 [0] Coinbase: → miner_address (6.35 BTC)
 [1] Alice → Bob (0.5 BTC)
 [2] Charlie → Dave (1.2 BTC)
 ...
 [2319] Final transaction
─────────────────────────────────────────
Block Hash: 0000000000000000000a4f8b2c9e1d3...
Block Size: 1,234,567 bytes (~1.2 MB)
```

## Block Hash Calculation

The **block hash** is computed by double SHA-256 hashing the block header:

```
Block Hash = SHA256(SHA256(Block Header))
```

**Important**: Only the header is hashed, not the entire block!

**Example**:

```
Header (80 bytes):
 [Version][Prev Hash][Merkle Root][Timestamp][nBits][Nonce]

First SHA256:
 Intermediate Hash = SHA256(Header)

Second SHA256:
 Block Hash = SHA256(Intermediate Hash)

Result:
 00000000000000000009f9b170fa4d72f6e62a94c5b3a52c1c3e4d5f6a7b8c9d
```

## Block Size Limits

Different blockchains have different block size limits:

| Blockchain       | Block Size Limit                 | Block Time | Transactions/Block (approx) |
| ---------------- | -------------------------------- | ---------- | --------------------------- |
| **Bitcoin**      | 1 MB (base) / 4 MB (with SegWit) | ~10 min    | 2,000-3,000                 |
| **Bitcoin Cash** | 32 MB                            | ~10 min    | 60,000+                     |
| **Ethereum**     | Variable (gas limit ~30M)        | ~12 sec    | 150-300                     |
| **Litecoin**     | 1 MB                             | ~2.5 min   | 2,000-3,000                 |

## Block Validation

Nodes validate blocks by checking:

1. **Header Validation**:

- Version is recognized
- Previous block hash exists in the chain
- Timestamp is reasonable (not too far in future)
- Difficulty target is correct
- Nonce produces valid hash (hash < target)

2. **Body Validation**:

- Merkle root matches calculated root from transactions
- All transactions are valid
- No double-spending
- Coinbase reward is correct
- Block size within limits

## Block Propagation

Once mined, blocks propagate through the network:

```
Miner finds valid block
 ↓
Broadcast to peer nodes (~50-200 ms)
 ↓
Peers validate block
 ↓
Peers relay to their peers
 ↓
Entire network knows within seconds (~6-12 sec for Bitcoin)
 ↓
Nodes add block to their blockchain
```

## Orphan Blocks

**Orphan Block**: A valid block that is not part of the main chain.

**Scenario**:

```
Two miners find valid blocks simultaneously:

 ... → Block 100 → Block 101a (Miner A finds first)
 ↘ Block 101b (Miner B finds second)

Network splits temporarily:
 50% of nodes see Block 101a first
 50% of nodes see Block 101b first

Next block (102) determines winner:
 ... → Block 100 → Block 101a → Block 102 ← Longest chain wins
 ↘ Block 101b (orphaned)

All nodes converge to longest chain.
```

**Orphan Rate**: Bitcoin ~1-2% of blocks

## Exam Tips

1. **Know the six header fields**: Version, Previous Hash, Merkle Root, Timestamp, nBits, Nonce
2. **Understand Merkle trees**: How they efficiently summarize transactions
3. **Block hash calculation**: Double SHA-256 of header only (not full block)
4. **Nonce purpose**: Mining variable, incremented to find valid hash
5. **Previous hash linkage**: Creates the chain, ensures immutability
6. **Difficulty target**: Controls mining difficulty, adjusts every 2016 blocks
7. **Coinbase transaction**: First transaction, rewards miner
8. **Block validation**: Header and body checks
9. **Orphan blocks**: Temporary forks resolved by longest chain
10. **Block size limits**: Bitcoin 1 MB base, varies by blockchain
