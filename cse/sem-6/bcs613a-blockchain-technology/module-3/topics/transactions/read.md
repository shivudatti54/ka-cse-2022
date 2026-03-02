# Bitcoin Transaction Structure

## Introduction

A **Bitcoin transaction** is a signed data structure that transfers value from one or more inputs to one or more outputs. Transactions are the fundamental building blocks of the Bitcoin blockchain, representing the transfer of bitcoin ownership.

## What is a Transaction?

**Definition**: A transaction is a digitally signed message that authorizes the transfer of bitcoin from one address to another. It consists of inputs (sources of funds) and outputs (destinations of funds).

**Key Properties**:

- **Irreversible**: Once confirmed in blockchain, cannot be reversed
- **Transparent**: Publicly visible on the blockchain
- **Pseudonymous**: Addresses don't directly reveal identity
- **Atomic**: Either entirely succeeds or entirely fails

## Transaction Components

A Bitcoin transaction has three main parts:

```
Transaction:
├── Version (4 bytes)
├── Inputs (variable)
│ ├── Previous Transaction Hash
│ ├── Output Index
│ ├── ScriptSig (Signature Script)
│ └── Sequence Number
├── Outputs (variable)
│ ├── Value (amount in satoshis)
│ └── ScriptPubKey (Locking Script)
└── Locktime (4 bytes)
```

### 1. Version

**Purpose**: Indicates transaction format version.

**Example**: `0x00000001` (version 1) or `0x00000002` (version 2, enables BIP68)

### 2. Input Count

**Purpose**: Number of inputs in the transaction.

**Encoding**: Variable-length integer (VarInt)

### 3. Inputs (Vin)

Each input specifies:

#### a) Previous Transaction Hash (32 bytes)

- Hash of the transaction containing the UTXO being spent
- Example: `8c7e252f8d64b0b6e313985915951a8c9c5cebe52f24683f84e69bcf1d0f0c7f`

#### b) Output Index (4 bytes)

- Index of the specific output in the previous transaction (vout)
- Example: `0` (first output)

#### c) ScriptSig / Signature Script (variable)

- Provides proof of ownership (signature + public key)
- Unlocks the UTXO specified in the previous transaction output

**Example**:

```
ScriptSig: <Signature> <Public Key>
```

#### d) Sequence Number (4 bytes)

- Originally for transaction replacement (disabled)
- Now used for relative timelocks (BIP68)
- Default: `0xFFFFFFFF`

### 4. Output Count

**Purpose**: Number of outputs in the transaction.

### 5. Outputs (Vout)

Each output specifies:

#### a) Value (8 bytes)

- Amount of bitcoin in satoshis (1 BTC = 100,000,000 satoshis)
- Example: `10000000` (0.1 BTC)

#### b) ScriptPubKey / Locking Script (variable)

- Defines conditions for spending the output
- Most common: Pay-to-Public-Key-Hash (P2PKH)

**Example P2PKH**:

```
ScriptPubKey: OP_DUP OP_HASH160 <PubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
```

**Types of ScriptPubKey**:

1. **P2PKH** (Pay-to-Public-Key-Hash): Most common, starts with '1'
2. **P2SH** (Pay-to-Script-Hash): For multisig, starts with '3'
3. **P2WPKH** (Pay-to-Witness-Public-Key-Hash): SegWit, starts with 'bc1'
4. **P2WSH** (Pay-to-Witness-Script-Hash): SegWit multisig

### 6. Locktime (4 bytes)

**Purpose**: Earliest time/block when transaction can be added to blockchain.

**Values**:

- `0`: Transaction valid immediately
- `< 500,000,000`: Block height
- `≥ 500,000,000`: Unix timestamp

## Transaction Example

```
Transaction ID: 8c7e252f8d64b0b6e313985915951a8c9c5cebe52f24683f84e69bcf1d0f0c7f

Version: 1

Inputs (1):
 [0] Previous TX: f2b3c4d5...
 Output Index: 0
 ScriptSig: 304402...ab12 (Signature) 03ef6a... (Public Key)
 Sequence: 0xFFFFFFFF

Outputs (2):
 [0] Value: 50000000 satoshis (0.5 BTC)
 ScriptPubKey: OP_DUP OP_HASH160 ab68...cd24 OP_EQUALVERIFY OP_CHECKSIG
 (Pay to: 1AbCd...Xyz)

 [1] Value: 49990000 satoshis (0.4999 BTC)
 ScriptPubKey: OP_DUP OP_HASH160 12ab...ef89 OP_EQUALVERIFY OP_CHECKSIG
 (Pay to: 1ChangeAddr...123 - Change address)

Locktime: 0

Transaction Fee: 10000 satoshis (0.0001 BTC)
 = Sum(Inputs) - Sum(Outputs)
 = 100000000 - (50000000 + 49990000)
```

## UTXO Model

Bitcoin uses the **Unspent Transaction Output (UTXO)** model, not an account balance model.

**Account Model (e.g., Bank)**:

```
Alice's Account: $1000
Bob's Account: $500

Alice sends $300 to Bob:
 Alice: $1000 - $300 = $700
 Bob: $500 + $300 = $800
```

**UTXO Model (Bitcoin)**:

```
Alice has:
 UTXO1: 0.5 BTC (from Transaction A)
 UTXO2: 0.3 BTC (from Transaction B)
 Total: 0.8 BTC

Alice sends 0.6 BTC to Bob:
 Inputs: UTXO1 (0.5 BTC) + UTXO2 (0.3 BTC) = 0.8 BTC
 Outputs:
 - Bob: 0.6 BTC (new UTXO for Bob)
 - Alice (change): 0.19 BTC (new UTXO for Alice)
 - Fee: 0.01 BTC (to miner)

 Alice's old UTXOs are "spent" (destroyed)
 Two new UTXOs are created
```

**Key Point**: You must spend entire UTXOs. Any leftover goes to a change address.

## Transaction Types

### 1. Standard Transaction (P2PKH)

Alice sends bitcoin to Bob's address.

```
Input: Alice's UTXO (signed with her private key)
Output: Bob's address
```

### 2. Coinbase Transaction

First transaction in every block, creates new bitcoins.

```
Input: None (coinbase input)
Output: Miner's address (block reward + fees)

Special Properties:
- No previous transaction hash
- Creates new bitcoins from nothing
- Must mature for 100 blocks before spending
```

### 3. Multi-Signature Transaction

Requires multiple signatures to spend.

```
Example: 2-of-3 multisig
- Alice, Bob, Charlie create shared address
- Any 2 of 3 must sign to spend

Use Cases:
- Escrow services
- Company funds (requires multiple executives)
- Enhanced security
```

### 4. SegWit Transaction

Segregated Witness - separates signature data from transaction data.

```
Benefits:
- Smaller transaction size
- Lower fees
- Fixes transaction malleability
- Enables Lightning Network
```

## Transaction Lifecycle

```
1. Creation:
 User creates transaction with wallet software
 ↓
2. Signing:
 User signs with private key
 ↓
3. Broadcasting:
 Transaction broadcast to network
 ↓
4. Mempool:
 Unconfirmed transactions wait in mempool
 Miners select highest-fee transactions
 ↓
5. Mining:
 Miner includes transaction in block
 ↓
6. Confirmation 1:
 Block added to blockchain
 ↓
7. Confirmations 2-6:
 More blocks added on top
 ↓
8. Finality:
 After 6 confirmations (~1 hour), considered final
```

## Transaction Fees

**Calculation**:

```
Fee = Sum(Inputs) - Sum(Outputs)
```

**Fee Rate**:

```
Fee Rate = Fee / Transaction Size (in bytes)
Measured in satoshis per byte (sat/byte)
```

**Example**:

```
Transaction Size: 250 bytes
Desired Fee Rate: 50 sat/byte
Total Fee: 250 × 50 = 12,500 satoshis (0.000125 BTC)
```

**Fee Priorities**:

- **High Fee**: Faster confirmation (~10-30 minutes)
- **Medium Fee**: Normal confirmation (~1-3 hours)
- **Low Fee**: Slow confirmation (hours to days)

## Transaction Verification

Nodes verify transactions by checking:

1. **Valid Inputs**:

- Referenced UTXOs exist and are unspent
- No double-spending

2. **Valid Signatures**:

- ScriptSig correctly unlocks ScriptPubKey
- Signatures match public keys

3. **Sufficient Funds**:

- Sum(Outputs) + Fee ≤ Sum(Inputs)

4. **Script Validation**:

- Locking and unlocking scripts execute successfully

5. **Size Limits**:

- Transaction size within limits

## Script Execution

Bitcoin uses a stack-based scripting language.

**Example: P2PKH Verification**

```
ScriptPubKey: OP_DUP OP_HASH160 <PubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
ScriptSig: <Signature> <Public Key>

Execution:
1. Push <Signature> to stack
2. Push <Public Key> to stack
3. OP_DUP: Duplicate <Public Key>
4. OP_HASH160: Hash duplicated public key
5. Push <PubKeyHash> to stack
6. OP_EQUALVERIFY: Verify hash matches expected hash
7. OP_CHECKSIG: Verify signature with public key

Result: TRUE (transaction valid) or FALSE (invalid)
```

## Transaction Malleability

**Problem**: Transaction ID could be changed before confirmation without invalidating transaction.

**Cause**: Signature data was part of transaction hash.

**Solution**: SegWit (Segregated Witness)

- Removes signature data from transaction ID calculation
- Enables second-layer solutions like Lightning Network

## Exam Tips

1. **Know transaction components**: Version, inputs, outputs, locktime
2. **Understand UTXO model**: Not account balances, entire UTXOs must be spent
3. **Input structure**: Previous TX hash, output index, ScriptSig, sequence
4. **Output structure**: Value (in satoshis), ScriptPubKey
5. **Transaction fee**: Sum(Inputs) - Sum(Outputs), goes to miner
6. **Coinbase transaction**: First in block, creates new bitcoins, no inputs
7. **Script types**: P2PKH, P2SH, P2WPKH (SegWit)
8. **Confirmation**: 1 confirmation = in blockchain, 6 confirmations = final
9. **Transaction ID**: Double SHA-256 hash of transaction data
10. **Verification**: Check inputs exist, signatures valid, no double-spend
