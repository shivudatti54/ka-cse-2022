# The Ethereum Stack

## Introduction

The **Ethereum Stack** refers to the layered architecture and ecosystem of technologies that enable decentralized applications (dApps) to run on the Ethereum blockchain. Understanding this stack is essential for developing and interacting with Ethereum-based applications.

## Ethereum Stack Layers

The Ethereum stack can be visualized as layers, from the blockchain foundation to the user interface:

```
┌──────────────────────────────────┐
│ Layer 4: Application Layer │ (dApps, Wallets, User Interfaces)
├──────────────────────────────────┤
│ Layer 3: Development Tools │ (Hardhat, Truffle, Web3.js, Ethers.js)
├──────────────────────────────────┤
│ Layer 2: Smart Contracts │ (Solidity, Vyper, ERC Standards)
├──────────────────────────────────┤
│ Layer 1: Execution Layer (EVM) │ (Ethereum Virtual Machine)
├──────────────────────────────────┤
│ Layer 0: Consensus & Network │ (Proof of Stake, P2P Network, Blocks, Transactions)
└──────────────────────────────────┘
```

## Layer 0: Consensus and Network Layer

### Components

1. **Consensus Mechanism**: Proof of Stake (PoS) post-Merge (September 2022)

- **Validators**: Stake 32 ETH to participate
- **Attestations**: Validators vote on blocks
- **Finality**: 2 epochs (~12.8 minutes)

2. **Beacon Chain**: Coordinates validators and consensus

3. **P2P Network**: Nodes communicate via gossip protocol

4. **Blockchain**: Chain of blocks containing transactions

### Role

- Maintains distributed ledger
- Achieves consensus on state
- Provides security and decentralization

## Layer 1: Execution Layer - Ethereum Virtual Machine (EVM)

### What is the EVM?

**Definition**: The Ethereum Virtual Machine is a Turing-complete, stack-based virtual machine that executes smart contract bytecode.

**Key Properties**:

- **Deterministic**: Same input always produces same output
- **Isolated**: Sandboxed environment (can't access filesystem, network)
- **Turing-complete**: Can execute any computational logic
- **Gas-metered**: Every operation costs gas

### EVM Architecture

```
┌─────────────────────────────────┐
│ EVM Stack │ (256-bit words, max 1024 depth)
├─────────────────────────────────┤
│ Memory │ (Volatile, cleared between transactions)
├─────────────────────────────────┤
│ Storage │ (Persistent, key-value store, expensive)
├─────────────────────────────────┤
│ Program Counter │ (Points to next instruction)
├─────────────────────────────────┤
│ Gas Available │ (Remaining gas for execution)
└─────────────────────────────────┘
```

### EVM Execution Flow

```
1. Transaction received
 ↓
2. Load contract bytecode
 ↓
3. Initialize EVM state
 ↓
4. Execute bytecode instructions (opcodes)
 ↓
5. Update world state (account balances, storage)
 ↓
6. Emit logs (events)
 ↓
7. Return result or revert if error
```

### Opcodes (EVM Instructions)

**Examples**:

```
ADD: Pop two items from stack, push sum
MUL: Pop two items, push product
PUSH: Push value onto stack
POP: Remove top item from stack
MSTORE: Store word in memory
SSTORE: Store word in persistent storage (expensive!)
CALL: Call another contract
REVERT: Revert state changes and return
```

**Gas Costs**:

- `ADD`: 3 gas
- `MUL`: 5 gas
- `SSTORE`: 20,000 gas (new slot) or 5,000 gas (update)
- `CALL`: 700 gas + cost of called function

### World State

**Definition**: The global state of all Ethereum accounts and their storage.

**Structure**:

```
World State = {
 Account_1: {balance, nonce, code, storage},
 Account_2: {balance, nonce, code, storage},
 ...
}
```

## Layer 2: Smart Contract Layer

### What are Smart Contracts?

**Definition**: Self-executing programs stored on the blockchain that automatically enforce agreements when conditions are met.

**Properties**:

- **Immutable**: Once deployed, code cannot be changed
- **Transparent**: Code and executions are public
- **Trustless**: Execution guaranteed by blockchain
- **Composable**: Contracts can call other contracts

### Programming Languages

#### 1. Solidity (Most Popular)

**Syntax**: JavaScript-like, object-oriented

**Example**:

```solidity
pragma solidity ^0.8.0;

contract SimpleStorage {
 uint256 private storedData;

 // Store a value
 function set(uint256 x) public {
 storedData = x;
 }

 // Retrieve the value
 function get() public view returns (uint256) {
 return storedData;
 }
}
```

**Features**:

- Inheritance
- Libraries
- Events
- Modifiers
- Multiple contract types (contracts, interfaces, libraries)

#### 2. Vyper

**Syntax**: Python-like

**Philosophy**: Security through simplicity (deliberately limits features)

**Example**:

```python
# @version ^0.3.0

storedData: public(uint256)

@external
def set(x: uint256):
 self.storedData = x

@external
@view
def get() -> uint256:
 return self.storedData
```

### ERC Standards (Ethereum Request for Comments)

#### ERC-20: Fungible Tokens

**Purpose**: Standard interface for tokens (like currencies)

**Required Functions**:

```solidity
function totalSupply() public view returns (uint256)
function balanceOf(address account) public view returns (uint256)
function transfer(address recipient, uint256 amount) public returns (bool)
function allowance(address owner, address spender) public view returns (uint256)
function approve(address spender, uint256 amount) public returns (bool)
function transferFrom(address sender, address recipient, uint256 amount) public returns (bool)
```

**Examples**: USDT, LINK, UNI

#### ERC-721: Non-Fungible Tokens (NFTs)

**Purpose**: Unique, non-interchangeable tokens

**Key Functions**:

```solidity
function ownerOf(uint256 tokenId) public view returns (address)
function transferFrom(address from, address to, uint256 tokenId) public
function approve(address to, uint256 tokenId) public
```

**Examples**: CryptoPunks, Bored Ape Yacht Club

#### ERC-1155: Multi-Token Standard

**Purpose**: Single contract managing multiple token types (fungible + non-fungible)

**Use Case**: Gaming (weapons, armor, currency in one contract)

### Smart Contract Compilation

**Process**:

```
Solidity Source Code (.sol)
 ↓
Compiler (solc)
 ↓
Bytecode (EVM machine code)
 ↓
ABI (Application Binary Interface - JSON describing functions)
```

**Example Output**:

```json
{
  "bytecode": "0x608060405234801561001057600080fd5b50...",
  "abi": [
    {
      "inputs": [{ "name": "x", "type": "uint256" }],
      "name": "set",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]
}
```

## Layer 3: Development Tools and Libraries

### Development Frameworks

#### 1. Hardhat

**Purpose**: Ethereum development environment

**Features**:

- Local Ethereum network for testing
- Console for debugging
- Gas reporting
- Contract verification

**Example**:

```javascript
const { ethers } = require('hardhat');

async function main() {
  const SimpleStorage = await ethers.getContractFactory('SimpleStorage');
  const contract = await SimpleStorage.deploy();
  await contract.deployed();

  console.log('Contract deployed to:', contract.address);
}

main();
```

#### 2. Truffle

**Purpose**: Development framework (older, widely used)

**Components**:

- Truffle: Compilation, deployment, testing
- Ganache: Local blockchain
- Drizzle: Frontend integration

#### 3. Foundry

**Purpose**: Fast, Rust-based development framework

**Features**:

- Tests written in Solidity
- Extremely fast execution
- Gas optimization tools

### Web3 Libraries

#### 1. Web3.js

**Purpose**: JavaScript library to interact with Ethereum

**Example**:

```javascript
const Web3 = require('web3');
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR-PROJECT-ID');

// Read account balance
const balance = await web3.eth.getBalance('0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb');
console.log(web3.utils.fromWei(balance, 'ether'), 'ETH');

// Send transaction
await web3.eth.sendTransaction({
  from: '0xAlice...',
  to: '0xBob...',
  value: web3.utils.toWei('1', 'ether'),
});

// Interact with contract
const contract = new web3.eth.Contract(ABI, contractAddress);
const result = await contract.methods.get().call();
```

#### 2. Ethers.js

**Purpose**: Lightweight, modern alternative to Web3.js

**Example**:

```javascript
const { ethers } = require('ethers');

// Connect to provider
const provider = new ethers.providers.JsonRpcProvider(
  'https://mainnet.infura.io/v3/YOUR-PROJECT-ID'
);

// Read balance
const balance = await provider.getBalance('0x742d35Cc...');
console.log(ethers.utils.formatEther(balance), 'ETH');

// Connect wallet
const wallet = new ethers.Wallet(privateKey, provider);

// Interact with contract
const contract = new ethers.Contract(contractAddress, ABI, wallet);
await contract.set(42);
const value = await contract.get();
```

### Node Providers

**Purpose**: Access Ethereum network without running full node

**Providers**:

- **Infura**: Most popular, easy to use
- **Alchemy**: Advanced features, analytics
- **QuickNode**: Fast, multi-chain support

### Testing Tools

1. **Mocha/Chai**: JavaScript testing frameworks
2. **Waffle**: Smart contract testing with Ethers.js
3. **Hardhat Network**: Local Ethereum instance
4. **Tenderly**: Debugging and monitoring

### Security Tools

1. **Slither**: Static analysis for Solidity
2. **Mythril**: Security analysis tool
3. **OpenZeppelin Contracts**: Audited, secure contract templates
4. **Etherscan**: Contract verification and analysis

## Layer 4: Application Layer

### Components

1. **Wallets**:

- **MetaMask**: Browser extension wallet
- **WalletConnect**: Mobile wallet connection
- **Ledger/Trezor**: Hardware wallets

2. **Decentralized Applications (dApps)**:

- DeFi (Uniswap, Aave, Compound)
- NFT Marketplaces (OpenSea, Rarible)
- DAOs (governance platforms)
- Games (Axie Infinity, Decentraland)

3. **User Interfaces**:

- React/Vue/Angular frontends
- Mobile apps
- Web3 integrations

### dApp Architecture

```
┌─────────────────────┐
│ Frontend (React) │
│ - User Interface │
│ - Web3.js/Ethers │
└──────────┬──────────┘
 │
 ↓
┌─────────────────────┐
│ Smart Contracts │
│ - Business Logic │
│ - State Storage │
└──────────┬──────────┘
 │
 ↓
┌─────────────────────┐
│ Ethereum Blockchain│
│ - EVM Execution │
│ - Consensus │
└─────────────────────┘
```

### Example dApp Interaction

```javascript
// 1. User clicks "Buy NFT" button in frontend

// 2. Frontend calls Web3 library
const contract = new ethers.Contract(nftAddress, ABI, signer);

// 3. Create transaction
const tx = await contract.mint(tokenId, {
  value: ethers.utils.parseEther('0.1'), // 0.1 ETH price
});

// 4. User approves in wallet (MetaMask popup)

// 5. Transaction sent to Ethereum network

// 6. Miners/validators include in block

// 7. Smart contract executes mint function

// 8. NFT ownership transferred

// 9. Event emitted (Transfer event)

// 10. Frontend updates UI
const receipt = await tx.wait();
console.log('NFT minted! Transaction:', receipt.transactionHash);
```

## Complete Stack Example: ERC-20 Token

### 1. Smart Contract (Solidity)

```solidity
pragma solidity ^0.8.0;

contract MyToken {
 string public name = "MyToken";
 string public symbol = "MTK";
 uint256 public totalSupply = 1000000;
 mapping(address => uint256) public balanceOf;

 event Transfer(address indexed from, address indexed to, uint256 value);

 constructor() {
 balanceOf[msg.sender] = totalSupply;
 }

 function transfer(address to, uint256 amount) public returns (bool) {
 require(balanceOf[msg.sender] >= amount, "Insufficient balance");
 balanceOf[msg.sender] -= amount;
 balanceOf[to] += amount;
 emit Transfer(msg.sender, to, amount);
 return true;
 }
}
```

### 2. Deployment Script (Hardhat)

```javascript
async function main() {
  const MyToken = await ethers.getContractFactory('MyToken');
  const token = await MyToken.deploy();
  await token.deployed();
  console.log('Token deployed to:', token.address);
}

main();
```

### 3. Frontend Integration (React + Ethers.js)

```javascript
import { ethers } from 'ethers';

function App() {
  const [balance, setBalance] = useState(0);

  async function checkBalance() {
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const contract = new ethers.Contract(tokenAddress, ABI, provider);
    const balance = await contract.balanceOf(userAddress);
    setBalance(ethers.utils.formatUnits(balance, 0));
  }

  async function sendTokens(recipient, amount) {
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    const contract = new ethers.Contract(tokenAddress, ABI, signer);
    const tx = await contract.transfer(recipient, amount);
    await tx.wait();
    alert('Tokens sent!');
  }

  return (
    <div>
      <h1>My Token Balance: {balance}</h1>
      <button onClick={checkBalance}>Check Balance</button>
      <button onClick={() => sendTokens('0xRecipient...', 100)}>Send 100 Tokens</button>
    </div>
  );
}
```

## Ethereum Ecosystem Tools

### Storage Solutions

- **IPFS**: Decentralized file storage
- **Arweave**: Permanent data storage
- **Filecoin**: Decentralized storage marketplace

### Oracles

- **Chainlink**: Bring real-world data to smart contracts
- **Band Protocol**: Cross-chain data oracle

### Layer 2 Scaling

- **Optimism**: Optimistic rollups
- **Arbitrum**: Optimistic rollups
- **Polygon**: Sidechain solution
- **zkSync**: Zero-knowledge rollups

### Indexing & Querying

- **The Graph**: Index and query blockchain data
- **Covalent**: Unified API for blockchain data

## Exam Tips

1. **Understand the layers**: Network/Consensus → EVM → Smart Contracts → Tools → dApps
2. **Know EVM basics**: Stack-based, gas-metered, Turing-complete
3. **Solidity syntax**: Be able to read and understand simple contracts
4. **ERC standards**: ERC-20 (fungible), ERC-721 (NFTs), ERC-1155 (multi-token)
5. **Development tools**: Hardhat (dev env), Ethers.js/Web3.js (libraries)
6. **Compilation**: Solidity → Bytecode + ABI
7. **dApp architecture**: Frontend → Web3 library → Smart contract → Blockchain
8. **Wallets**: MetaMask for browser, hardware wallets for security
9. **Gas**: Every operation costs gas, SSTORE is expensive
10. **Smart contract properties**: Immutable, transparent, trustless, composable
