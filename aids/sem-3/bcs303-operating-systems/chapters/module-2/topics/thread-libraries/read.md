# Web3 Libraries

## Overview

Web3 libraries provide JavaScript/Python interfaces to interact with Ethereum nodes. They handle RPC communication, transaction signing, ABI encoding/decoding, and other blockchain operations.

## Major Web3 Libraries

### 1. ethers.js

The most popular library for Ethereum interaction:

```javascript
const { ethers } = require('ethers');

// Connect to provider
const provider = new ethers.JsonRpcProvider('https://mainnet.infura.io/v3/KEY');

// Create wallet
const wallet = new ethers.Wallet(privateKey, provider);

// Contract interaction
const contract = new ethers.Contract(address, abi, wallet);
```

**Key Features:**

- Lightweight (~120KB)
- TypeScript support
- ENS integration
- Human-readable ABI
- Multiple provider types

### 2. web3.js

The original Ethereum JavaScript library:

```javascript
const Web3 = require('web3');

// Connect
const web3 = new Web3('https://mainnet.infura.io/v3/KEY');

// Contract
const contract = new web3.eth.Contract(abi, address);
```

### 3. web3.py (Python)

Python library for Ethereum:

```python
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/KEY'))
contract = w3.eth.contract(address=addr, abi=abi)
```

## ethers.js Deep Dive

### Providers

```javascript
// JSON-RPC Provider (most common)
const provider = new ethers.JsonRpcProvider(url);

// WebSocket Provider (for subscriptions)
const wsProvider = new ethers.WebSocketProvider(wsUrl);

// Browser Provider (MetaMask)
const browserProvider = new ethers.BrowserProvider(window.ethereum);

// Default Provider (multiple sources)
const defaultProvider = ethers.getDefaultProvider('mainnet', {
  infura: 'KEY',
  alchemy: 'KEY',
});
```

### Signers

```javascript
// Wallet from private key
const wallet = new ethers.Wallet(privateKey, provider);

// Wallet from mnemonic
const wallet = ethers.Wallet.fromPhrase(mnemonic);

// Random wallet
const randomWallet = ethers.Wallet.createRandom();

// Hardware wallet (via provider)
const signer = await browserProvider.getSigner();
```

### Contract Interaction

```javascript
// Contract interface
const abi = [
  'function balanceOf(address) view returns (uint256)',
  'function transfer(address to, uint256 amount) returns (bool)',
  'event Transfer(address indexed from, address indexed to, uint256 value)',
];

// Read-only contract
const contract = new ethers.Contract(address, abi, provider);
const balance = await contract.balanceOf(userAddress);

// Writable contract
const contractWithSigner = contract.connect(signer);
const tx = await contractWithSigner.transfer(recipient, amount);
await tx.wait();
```

### Utilities

```javascript
// Unit conversion
ethers.parseEther('1.5'); // 1.5 ETH -> Wei
ethers.formatEther(weiAmount); // Wei -> ETH string
ethers.parseUnits('100', 6); // 100 with 6 decimals
ethers.formatUnits(amount, 6); // Format with 6 decimals

// Hashing
ethers.keccak256(data);
ethers.id('Transfer(address,address,uint256)'); // Event topic

// ABI encoding
const iface = new ethers.Interface(abi);
const data = iface.encodeFunctionData('transfer', [to, amount]);
const decoded = iface.decodeFunctionResult('balanceOf', result);

// Address utilities
ethers.isAddress(address);
ethers.getAddress(address); // Checksum
```

## Event Handling

### Listening for Events

```javascript
// Listen for Transfer events
contract.on('Transfer', (from, to, value, event) => {
  console.log(`Transfer: ${from} -> ${to}: ${value}`);
});

// Query past events
const filter = contract.filters.Transfer(fromAddress, null);
const events = await contract.queryFilter(filter, startBlock, endBlock);

// Remove listener
contract.off('Transfer', listener);
```

### Event Filtering

```javascript
// Filter by indexed parameters
const filter = contract.filters.Transfer(
  '0xSenderAddress', // from (indexed)
  null // to (any)
);

// All transfers to specific address
const filter = contract.filters.Transfer(null, '0xRecipient');
```

## Transaction Management

### Building Transactions

```javascript
const tx = {
  to: recipient,
  value: ethers.parseEther('1.0'),
  gasLimit: 21000,
  maxFeePerGas: ethers.parseUnits('30', 'gwei'),
  maxPriorityFeePerGas: ethers.parseUnits('2', 'gwei'),
  nonce: await provider.getTransactionCount(wallet.address),
  chainId: 1,
};

const signedTx = await wallet.signTransaction(tx);
const response = await provider.broadcastTransaction(signedTx);
```

### Gas Estimation

```javascript
// Estimate gas for transaction
const gasEstimate = await provider.estimateGas({
  to: address,
  data: calldata,
});

// Estimate gas for contract call
const gasEstimate = await contract.transfer.estimateGas(to, amount);

// Get current fee data
const feeData = await provider.getFeeData();
console.log('Max Fee:', ethers.formatUnits(feeData.maxFeePerGas, 'gwei'));
```

## ENS Integration

```javascript
// Resolve ENS name to address
const address = await provider.resolveName('vitalik.eth');

// Reverse lookup
const name = await provider.lookupAddress(address);

// Get avatar
const avatar = await provider.getAvatar('vitalik.eth');
```

## Comparison: ethers.js vs web3.js

| Feature         | ethers.js      | web3.js     |
| --------------- | -------------- | ----------- |
| Size            | ~120KB         | ~590KB      |
| TypeScript      | Native         | Added later |
| License         | MIT            | LGPL        |
| Provider/Signer | Separated      | Combined    |
| ABI             | Human-readable | JSON only   |
| Maintenance     | Active         | Active      |

## Summary

- **ethers.js** is the recommended library for modern dApps
- **Providers** connect to the network (read operations)
- **Signers** sign transactions (write operations)
- **Contracts** provide typed interfaces to smart contracts
- **Events** enable reactive programming patterns
- **Utilities** handle unit conversion, hashing, encoding
