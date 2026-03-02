# Ethereum Transactions

## Introduction

An **Ethereum transaction** is a cryptographically signed instruction from an account that changes the state of the Ethereum blockchain. Unlike Bitcoin's UTXO model, Ethereum uses an account-based model and supports both simple value transfers and complex smart contract interactions.

## Ethereum Account Model vs Bitcoin UTXO

| Aspect               | Bitcoin (UTXO)         | Ethereum (Account)                          |
| -------------------- | ---------------------- | ------------------------------------------- |
| **Balance Storage**  | Sum of unspent outputs | Single account balance                      |
| **State**            | Stateless (UTXOs)      | Stateful (accounts with balances and state) |
| **Transaction Type** | Transfer of UTXOs      | State transitions                           |
| **Complexity**       | Simple value transfers | Value transfers + smart contract execution  |

**Ethereum Account Model**:

```
Alice's Account:
 Address: 0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb
 Balance: 10 ETH
 Nonce: 5
 Code: (empty for EOA)
 Storage: (empty for EOA)

Alice sends 2 ETH to Bob:
 Alice: 10 - 2 = 8 ETH (balance updated)
 Bob: 5 + 2 = 7 ETH (balance updated)
```

## Types of Ethereum Accounts

### 1. Externally Owned Account (EOA)

**Controlled by**: Private key

**Properties**:

- Has ether balance
- Can send transactions
- No associated code
- Created by generating key pair

**Address Format**: `0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb` (20 bytes, 40 hex characters)

### 2. Contract Account

**Controlled by**: Smart contract code

**Properties**:

- Has ether balance
- Has associated code (smart contract)
- Has storage (persistent state)
- Can only send transactions when triggered by EOA or another contract

**Creation**: Deployed via special transaction from EOA

## Transaction Structure

Ethereum transaction components:

```
Transaction:
├── Nonce (transaction count from sender)
├── Gas Price (wei per gas unit)
├── Gas Limit (max gas for transaction)
├── To (recipient address, 20 bytes)
├── Value (amount of ETH in wei)
├── Data (optional, for smart contract calls)
├── v, r, s (signature components)
└── (EIP-1559) Max Fee Per Gas, Max Priority Fee
```

### Transaction Fields Explained

#### 1. Nonce

**Purpose**: Sequential number tracking transactions from an account.

**Example**: If Alice has sent 5 transactions, her next transaction has nonce = 5

**Why it matters**:

- Prevents replay attacks
- Ensures transaction ordering
- Must be sequential (nonce 6 can't be processed before nonce 5)

#### 2. Gas Price (Legacy) / Max Fee Per Gas (EIP-1559)

**Gas Price (Legacy)**:

```
Amount in wei you're willing to pay per unit of gas
Example: 20 Gwei (20,000,000,000 wei)
```

**EIP-1559 (London Hard Fork)**:

```
Max Fee Per Gas: Maximum total fee per gas (includes base fee + tip)
Max Priority Fee: Tip to miner (priority fee)

Base Fee: Algorithmically determined, burned
Priority Fee: Goes to miner
```

#### 3. Gas Limit

**Purpose**: Maximum gas units you're willing to spend.

**Example**: `21,000` (minimum for simple ETH transfer)

**Smart Contract Call**: May require 100,000+ gas depending on complexity

**Refund**: Unused gas is refunded

#### 4. To

**Purpose**: Recipient address.

**Cases**:

- **EOA Address**: Simple ETH transfer
- **Contract Address**: Smart contract interaction
- **Empty (null)**: Contract creation transaction

#### 5. Value

**Purpose**: Amount of ETH to send (in wei).

**Conversion**:

```
1 ETH = 1,000,000,000,000,000,000 wei (10^18)
1 ETH = 1,000,000,000 Gwei (10^9)
```

**Example**: Sending 0.1 ETH = `100000000000000000` wei

#### 6. Data (Input Data)

**Purpose**: Additional information for contract interactions.

**Cases**:

- **Empty**: Simple ETH transfer
- **Function Call**: Encoded function name + parameters
- **Contract Deployment**: Bytecode of the contract

**Example Function Call**:

```
Function: transfer(address recipient, uint256 amount)

Encoded Data:
0xa9059cbb (Function selector, first 4 bytes of keccak256("transfer(address,uint256)"))
000000000000000000000000742d35Cc... (Recipient address, padded to 32 bytes)
0000000000000000000000000000000000000000000000056bc75e2d63100000 (Amount: 100 tokens)
```

#### 7. v, r, s (Signature)

**Purpose**: Cryptographic signature proving transaction authorization.

**Components**:

- **r**: First 32 bytes of signature
- **s**: Second 32 bytes of signature
- **v**: Recovery ID (27 or 28 for legacy, 0 or 1 for EIP-155)

**Generation**:

```
1. Hash transaction data
2. Sign hash with private key (ECDSA)
3. Extract r, s, v from signature
```

## Transaction Types

### 1. Simple ETH Transfer

**Purpose**: Send ETH from one account to another.

```
From: 0xAlice...
To: 0xBob...
Value: 1 ETH
Gas Limit: 21,000
Gas Price: 20 Gwei
Data: (empty)

Total Cost: 21,000 × 20 Gwei = 0.00042 ETH (gas fee)
 + 1 ETH (transfer amount)
 = 1.00042 ETH
```

### 2. Contract Deployment

**Purpose**: Deploy a new smart contract.

```
From: 0xAlice...
To: (null/empty)
Value: 0 ETH
Gas Limit: 500,000
Data: <Contract bytecode>

Result: New contract deployed at deterministic address
Address = keccak256(RLP(sender_address, nonce))
```

### 3. Contract Interaction (Function Call)

**Purpose**: Call a function in a deployed smart contract.

```
From: 0xAlice...
To: 0xContractAddress...
Value: 0 ETH (or amount if payable function)
Gas Limit: 100,000
Data: <Encoded function call>

Example: Calling ERC-20 token transfer
Function: transfer(recipient, amount)
```

## Gas and Transaction Fees

### Gas Mechanics

**Gas**: Unit of computational work on Ethereum.

**Why Gas?**:

- Prevents infinite loops (runs out of gas)
- Pays for computation and storage
- Incentivizes miners/validators

**Gas Costs (Examples)**:

```
Addition (ADD): 3 gas
Multiplication (MUL): 5 gas
Storage (SSTORE): 20,000 gas (new value) or 5,000 gas (update)
SHA3 hash: 30 gas + 6 gas per word
Contract creation: 32,000 gas
```

### Fee Calculation

**Legacy (Pre-EIP-1559)**:

```
Transaction Fee = Gas Used × Gas Price

Example:
Gas Used: 21,000
Gas Price: 20 Gwei
Fee = 21,000 × 20 Gwei = 420,000 Gwei = 0.00042 ETH
```

**EIP-1559 (Post London Fork)**:

```
Transaction Fee = Gas Used × (Base Fee + Priority Fee)

Base Fee: Algorithmically determined, varies per block, BURNED
Priority Fee: Tip to validator

Example:
Gas Used: 21,000
Base Fee: 30 Gwei
Priority Fee: 2 Gwei
Fee = 21,000 × (30 + 2) = 672,000 Gwei = 0.000672 ETH

Burned: 21,000 × 30 = 630,000 Gwei
To Validator: 21,000 × 2 = 42,000 Gwei
```

### Gas Limit vs Gas Used

**Gas Limit**: Maximum gas you're willing to spend (set by user)

**Gas Used**: Actual gas consumed (determined by execution)

**Scenarios**:

```
Case 1: Gas Used < Gas Limit
 Transaction succeeds
 Unused gas refunded

Case 2: Gas Used = Gas Limit (and completes)
 Transaction succeeds
 No refund

Case 3: Gas Used > Gas Limit (out of gas)
 Transaction FAILS
 State changes REVERTED
 Gas fee STILL PAID (gas consumed before failure)
```

## Transaction Lifecycle

```
1. Creation and Signing:
 User creates transaction and signs with private key
 ↓
2. Broadcasting:
 Transaction broadcast to Ethereum network
 ↓
3. Transaction Pool (Mempool):
 Unconfirmed transactions wait in mempool
 Validators select transactions (highest priority fee first)
 ↓
4. Block Inclusion:
 Validator includes transaction in block
 ↓
5. Execution:
 EVM executes transaction
 State changes applied
 ↓
6. Block Finality (Proof of Stake):
 Block finalized after 2 epochs (~12.8 minutes)
 ↓
7. Confirmation:
 Transaction confirmed and irreversible
```

## Message Calls (Internal Transactions)

**Internal Transaction**: Contract-to-contract calls, not visible as separate transactions on blockchain.

**Example**:

```
User → Contract A (external transaction)
Contract A → Contract B (internal/message call)
Contract B → Contract C (internal/message call)

Only the first transaction appears in transaction list
Internal calls visible in transaction trace
```

## EIP-1559 Transaction Type

**Introduced**: London Hard Fork (August 2021)

**Benefits**:

- More predictable fees
- Better UX (wallet estimates fees automatically)
- Deflationary pressure (base fee burned)

**Structure**:

```
Type 2 Transaction (EIP-1559):
- Max Fee Per Gas: 100 Gwei (max you'll pay)
- Max Priority Fee: 2 Gwei (tip to validator)

If Base Fee = 80 Gwei:
 Actual Fee = Base Fee (80) + Priority Fee (2) = 82 Gwei
 Savings: 100 - 82 = 18 Gwei refunded
```

## Transaction Example

```
Transaction Hash: 0x7f9fade1c0d57a7af66ab4ead7c2eb7b11a91385

From: 0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb
To: 0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984 (UNI Token Contract)
Value: 0 ETH
Nonce: 123
Gas Limit: 150,000
Max Fee Per Gas: 50 Gwei
Max Priority Fee: 2 Gwei
Gas Used: 65,482

Data (Function Call): transfer(recipient, amount)
 0xa9059cbb
 0000000000000000000000009876543210abcdef... (recipient)
 00000000000000000000000000000000000000000000021e19e0c9bab2400000 (amount)

Status: Success
Block: 15,123,456
Confirmations: 1,234

Fees:
 Base Fee: 40 Gwei
 Priority Fee: 2 Gwei
 Total Fee Per Gas: 42 Gwei
 Total Fee: 65,482 × 42 Gwei = 0.002750244 ETH

 Burned (Base): 65,482 × 40 = 0.00261928 ETH
 To Validator: 65,482 × 2 = 0.00013096ETH
```

## Transaction Receipt

After transaction execution, a receipt is generated:

```
Receipt:
- Transaction Hash
- Status (1 = success, 0 = failure)
- Block Number
- Gas Used
- Cumulative Gas Used
- Logs (events emitted)
- Contract Address (if contract creation)
```

## Transaction Security

### Common Issues

1. **Replay Attacks**: Prevented by nonce and chain ID (EIP-155)
2. **Front-Running**: Miners/validators see pending transactions and can submit their own first
3. **Insufficient Gas**: Transaction fails, but gas fee still paid
4. **Reentrancy**: Smart contract vulnerability (prevented by checks-effects-interactions pattern)

### Best Practices

- Always set reasonable gas limits
- Use EIP-1559 for better fee estimation
- Verify contract addresses before interacting
- Check transaction status in receipts
- Use nonces correctly (sequential)

## Exam Tips

1. **Account model**: Ethereum uses accounts with balances, not UTXOs like Bitcoin
2. **Two account types**: EOA (user-controlled) vs Contract (code-controlled)
3. **Transaction fields**: Nonce, gas price/limit, to, value, data, signature (v,r,s)
4. **Gas**: Computational unit, prevents infinite loops, incentivizes validators
5. **EIP-1559**: Base fee (burned) + priority fee (validator), more predictable fees
6. **Gas limit vs used**: Limit is max, used is actual, unused refunded
7. **Transaction types**: ETH transfer, contract deployment, contract interaction
8. **Data field**: Empty for transfers, function calls for contracts, bytecode for deployment
9. **Internal transactions**: Contract-to-contract calls, not separate blockchain transactions
10. **Transaction receipt**: Contains status, logs (events), gas used, etc.
