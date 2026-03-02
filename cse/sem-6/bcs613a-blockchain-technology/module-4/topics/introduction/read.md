# Introduction to Ethereum

## 1. What is Ethereum?

**Ethereum** is a decentralized, open-source blockchain platform that enables the creation and execution of **smart contracts** and **decentralized applications (dApps)**. While Bitcoin was designed primarily as a peer-to-peer digital currency, Ethereum extends blockchain technology into a general-purpose programmable platform.

**Key Definition:** Ethereum is a decentralized world computer -- a global, open-source platform for decentralized applications where developers can write code that controls digital value, runs exactly as programmed, and is accessible anywhere in the world.

**Founder:** Vitalik Buterin proposed Ethereum in late 2013; the network went live on July 30, 2015.

## 2. Ethereum vs Bitcoin

| Aspect                | Bitcoin                                       | Ethereum                                   |
| --------------------- | --------------------------------------------- | ------------------------------------------ |
| **Purpose**           | Digital currency / store of value             | Programmable blockchain / world computer   |
| **Scripting**         | Limited (Bitcoin Script, not Turing-complete) | Turing-complete (Solidity, Vyper)          |
| **Transaction Model** | UTXO (Unspent Transaction Output)             | Account-based model                        |
| **Block Time**        | ~10 minutes                                   | ~12 seconds                                |
| **Consensus**         | Proof of Work (SHA-256)                       | Proof of Stake (since The Merge, Sep 2022) |
| **Native Currency**   | BTC                                           | ETH (Ether)                                |
| **Smart Contracts**   | Very limited                                  | Full support                               |

## 3. Core Components of Ethereum

### 3.1 Ethereum Virtual Machine (EVM)

The **EVM** is the runtime environment for smart contracts on Ethereum. Every Ethereum node runs the EVM, ensuring that all nodes compute the same results for the same input.

**Key Properties:**

- **Deterministic:** Same input always produces same output
- **Sandboxed:** Smart contracts run in isolation, cannot access network or filesystem
- **Stack-based:** Uses a last-in, first-out stack architecture
- **Gas-metered:** Every operation costs gas, preventing infinite loops

```
Smart Contract (Solidity) --> Compiler --> Bytecode --> EVM Execution
```

### 3.2 Accounts

Ethereum has two types of accounts:

**Externally Owned Accounts (EOA):**

- Controlled by private keys (held by humans)
- Can initiate transactions
- No associated code
- Has address, balance, and nonce

**Contract Accounts:**

- Controlled by smart contract code
- Cannot initiate transactions on their own (must be triggered)
- Has code and persistent storage
- Has address, balance, nonce, code hash, and storage root

```
EOA (User with private key)
 |
 |-- sends transaction to -->
 |
Contract Account (Code + Storage)
 |
 |-- may call other contracts -->
 |
Another Contract Account
```

### 3.3 Ether (ETH) and Gas

**Ether (ETH):** The native cryptocurrency of Ethereum, used to pay for transactions and computational services.

**Gas:** A unit of measurement for computational work on Ethereum.

- Every operation (addition, storage write, contract call) has a gas cost
- Users set a gas limit and gas price when submitting transactions
- Gas prevents abuse (infinite loops would run out of gas)
- Unused gas is refunded; if gas runs out, the transaction fails but fees are still paid

**Denominations:**

```
1 ETH = 1,000,000,000 Gwei (10^9 Gwei)
1 ETH = 1,000,000,000,000,000,000 Wei (10^18 Wei)
1 Gwei = 1,000,000,000 Wei
```

## 4. Smart Contracts

A **smart contract** is a self-executing program stored on the blockchain that automatically enforces the terms of an agreement when predefined conditions are met.

**Characteristics:**

- **Immutable:** Once deployed, code cannot be changed
- **Deterministic:** Same inputs always produce same outputs
- **Autonomous:** Execute automatically when triggered
- **Transparent:** Code is publicly verifiable on the blockchain

**Simple Example (Solidity):**

```solidity
pragma solidity ^0.8.0;

contract SimpleStorage {
 uint256 storedData;

 function set(uint256 x) public {
 storedData = x;
 }

 function get() public view returns (uint256) {
 return storedData;
 }
}
```

## 5. Decentralized Applications (dApps)

A **dApp** is an application that runs on a decentralized network (Ethereum) rather than a centralized server.

**dApp Architecture:**

```
Frontend (Web/Mobile UI)
 |
 v
Web3 Library (ethers.js / web3.js)
 |
 v
Ethereum Node (JSON-RPC)
 |
 v
Smart Contracts on Ethereum Blockchain
```

**Categories of dApps:**

- **DeFi (Decentralized Finance):** Lending, borrowing, trading (e.g., Uniswap, Aave)
- **NFTs:** Digital ownership tokens (e.g., OpenSea)
- **DAOs:** Decentralized governance organizations
- **Gaming:** Play-to-earn, in-game assets
- **Identity:** Self-sovereign identity solutions

## 6. History and Evolution of Ethereum

| Year     | Milestone                                                    |
| -------- | ------------------------------------------------------------ |
| **2013** | Vitalik Buterin publishes Ethereum whitepaper                |
| **2014** | Crowdsale raises ~$18 million; Ethereum Foundation formed    |
| **2015** | Frontier launch (July 30) -- first live release              |
| **2016** | The DAO hack; Ethereum hard forks into ETH and ETC           |
| **2017** | Byzantium hard fork (Metropolis phase 1)                     |
| **2019** | Constantinople and Istanbul upgrades                         |
| **2020** | Beacon Chain launch (Proof of Stake chain)                   |
| **2021** | London hard fork (EIP-1559 fee market reform)                |
| **2022** | The Merge -- transition from Proof of Work to Proof of Stake |
| **2023** | Shanghai/Capella upgrade (staked ETH withdrawals enabled)    |

## 7. Ethereum's State Model

Unlike Bitcoin's UTXO model, Ethereum maintains a **world state** -- a mapping of addresses to account states.

```
World State (Merkle Patricia Trie):
 Address_1 --> { nonce, balance, storageRoot, codeHash }
 Address_2 --> { nonce, balance, storageRoot, codeHash }
 ...
```

Each transaction causes a **state transition:**

```
State(t) + Transaction --> State(t+1)
```

The EVM processes transactions and updates the world state accordingly.

## Exam Tips

1. **Ethereum = programmable blockchain** -- not just a cryptocurrency but a platform for smart contracts and dApps
2. **EVM** is the computation engine; it is Turing-complete, deterministic, and gas-metered
3. **Two account types**: EOA (human-controlled, initiates transactions) vs Contract (code-controlled, triggered by EOA)
4. **Gas** prevents abuse, measures computation, and is paid in ETH
5. **Account model** vs Bitcoin's UTXO model -- Ethereum tracks state per account
6. **The Merge (2022)** transitioned Ethereum from Proof of Work to Proof of Stake
