# Smart Contracts and Oracles in Bitcoin

## Introduction to Smart Contracts

A smart contract is a self-executing contract where the terms of the agreement are directly written into code. They automatically execute predefined actions when specific conditions are met, without the need for intermediaries.

While Ethereum popularized complex smart contracts, Bitcoin was the first blockchain to introduce a basic form of smart contracts through its scripting language. Bitcoin's approach is more minimalist and security-focused compared to Turing-complete platforms.

### Key Characteristics of Bitcoin Smart Contracts
- **Deterministic**: Same inputs always produce the same outputs
- **Immutable**: Cannot be changed once deployed
- **Transparent**: Code is visible on the blockchain
- **Automated**: Self-executing without human intervention

## Bitcoin Script: The Foundation of Bitcoin Smart Contracts

Bitcoin uses a stack-based scripting language called Bitcoin Script for creating smart contracts. This is a Forth-like, non-Turing complete language designed specifically for financial transactions.

### Basic Transaction Structure
```
Transaction Inputs (Previous TX) -> ScriptSig (Unlocking script)
Transaction Outputs -> ScriptPubKey (Locking script)
```

### Common Bitcoin Script Opcodes
| Opcode | Function | Description |
|--------|----------|-------------|
| OP_CHECKSIG | Check Signature | Verifies cryptographic signature |
| OP_DUP | Duplicate | Duplicates top stack item |
| OP_HASH160 | Hash | Performs SHA-256 followed by RIPEMD-160 |
| OP_EQUALVERIFY | Verify Equality | Checks if two items are equal |
| OP_CHECKMULTISIG | Check Multiple Signatures | Verifies multiple signatures |

### Example: Pay-to-Public-Key-Hash (P2PKH)
This is the most common Bitcoin transaction type:

```
Locking Script (ScriptPubKey):
OP_DUP OP_HASH160 <PublicKeyHash> OP_EQUALVERIFY OP_CHECKSIG

Unlocking Script (ScriptSig):
<Signature> <PublicKey>
```

Execution flow:
```
Stack: [Signature, PublicKey]
OP_DUP: [Signature, PublicKey, PublicKey]
OP_HASH160: [Signature, PublicKey, PublicKeyHash]
<PublicKeyHash>: [Signature, PublicKey, PublicKeyHash, StoredHash]
OP_EQUALVERIFY: [Signature, PublicKey] (verifies hashes match)
OP_CHECKSIG: [True/False] (verifies signature)
```

## Types of Bitcoin Smart Contracts

### 1. Multi-Signature Contracts (Multisig)
Requires multiple signatures to spend funds. Common configurations include 2-of-3 or 3-of-5 signatures.

Example: 2-of-3 multisig
```
ScriptPubKey: OP_2 <PubKey1> <PubKey2> <PubKey3> OP_3 OP_CHECKMULTISIG
ScriptSig: OP_0 <Sig1> <Sig2>
```

### 2. Time-Locked Contracts
Funds can only be spent after a certain time or block height.

Example: 
```
ScriptPubKey: <expiry_time> OP_CHECKLOCKTIMEVERIFY OP_DROP OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
```

### 3. Hashed Timelock Contracts (HTLC)
Enable conditional payments across different blockchains through hash preimages.

```
+----------------+       +----------------+       +----------------+
|    Alice       |       |    Contract    |       |      Bob       |
|   (Sender)     |       |    (HTLC)      |       |   (Receiver)   |
+----------------+       +----------------+       +----------------+
| 1. Creates     |       |                |       |                |
|    secret R    |       |                |       |                |
|    hash H      |------>| 2. Creates HTLC|       |                |
|                |       |    with hash H |       |                |
|                |       |    and timeout |       |                |
|                |       |----------------|------>| 3. Creates HTLC|
|                |       |                |       |    on other chain|
|                |       |                |       |                |
| 4. Reveals R   |       |                |       | 5. Uses R to   |
|    to claim    |<------| 6. Releases    |<------|    claim funds |
|    funds       |       |    funds       |       |                |
+----------------+       +----------------+       +----------------+
```

## Introduction to Oracles

Oracles are services that provide external data to blockchain smart contracts. They act as bridges between the deterministic blockchain world and the unpredictable real world.

### The Oracle Problem
Blockchains are deterministic and isolated systems, but smart contracts often need external data (price feeds, weather data, sports scores). This creates the "oracle problem" - how to trust external data sources while maintaining blockchain security properties.

### Oracle Architecture
```
+----------------+     +----------------+     +----------------+
|   Data Source  |     |    Oracle      |     | Smart Contract |
|   (External    |---->|   Service      |---->|   on Blockchain|
|   World)       |     |                |     |                |
+----------------+     +----------------+     +----------------+
```

## Bitcoin Oracle Implementations

### 1. Data Embedding Techniques
Bitcoin oracles typically work by embedding data into blockchain transactions:

**OP_RETURN Outputs:**
```python
# Example of embedding data using OP_RETURN
transaction_output = {
    "value": 0,
    "script": b"\x6a" + len(data).to_bytes(1, 'little') + data.encode()
}
```

**Coinbase Transaction Data:**
Miners can include external data in coinbase transactions.

**Multi-signature Proofs:**
Multiple trusted parties sign transactions containing specific data.

### 2. Oracle Design Patterns

**Centralized Oracle:**
```
+----------------+     +----------------+     +----------------+
|   Data Source  |     | Single Trusted |     | Bitcoin        |
|                |---->| Oracle Service |---->| Smart Contract |
+----------------+     +----------------+     +----------------+
```
- Simple but introduces centralization risk
- Single point of failure

**Federated Oracle:**
```
+----------------+     +----------------+     +----------------+
|   Data Source  |     | Multiple Oracle|     | Bitcoin        |
|                |---->| Providers      |---->| Smart Contract |
+----------------+     | (Consensus)    |     +----------------+
                       +----------------+
```
- Multiple trusted parties
- Requires consensus among oracle nodes

**Decentralized Oracle Network:**
```
+----------------+     +----------------+     +----------------+
|   Data Source  |     | Many Nodes     |     | Bitcoin        |
|                |---->| with Economic  |---->| Smart Contract |
+----------------+     | Incentives     |     +----------------+
                       +----------------+
```
- Most secure but complex
- Uses cryptographic proofs and economic incentives

## Real-World Applications

### 1. Prediction Markets
Smart contracts can create decentralized prediction markets using oracles for outcome resolution.

### 2. Insurance Contracts
Parametric insurance that automatically pays out based on oracle-provided data (weather conditions, flight delays).

### 3. Supply Chain Tracking
Oracles can provide real-world data about product location and condition.

### 4. Cross-Chain Atomic Swaps
HTLCs enable trustless exchanges between different cryptocurrencies.

## Limitations and Challenges

### Bitcoin Smart Contract Limitations
- **Non-Turing Complete**: Bitcoin Script has limited functionality
- **Block Size Limit**: Complex contracts require more space
- **Privacy Concerns**: All contract details are public
- **Development Complexity**: Lower-level language than Solidity

### Oracle Challenges
- **Data Authenticity**: How to verify external data is correct
- **Centralization Risk**: Many oracles rely on trusted parties
- **Cost**: Oracle services add transaction costs
- **Timing Issues**: Data freshness and blockchain confirmation times

## Future Developments

### Taproot and Schnorr Signatures
Recent Bitcoin upgrades improve smart contract capabilities:
- **Taproot**: Enhances privacy and efficiency of complex contracts
- **Schnorr Signatures**: Enables better multi-signature schemes

### Lightning Network
The Lightning Network enables more complex smart contracts off-chain with Bitcoin as the settlement layer.

## Exam Tips

1. **Understand the difference** between Bitcoin Script and Ethereum's Solidity - Bitcoin is intentionally limited for security.
2. **Memorize common opcodes** and their functions, especially OP_CHECKSIG, OP_CHECKMULTISIG.
3. **Draw diagrams** for HTLC and oracle workflows - visual explanations score well.
4. **Focus on the trade-offs** between different oracle designs - centralized vs decentralized.
5. **Remember that Bitcoin oracles** typically work by embedding data in transactions, unlike Ethereum's contract-based oracles.
6. **Practice explaining** how multi-signature contracts work with concrete examples.