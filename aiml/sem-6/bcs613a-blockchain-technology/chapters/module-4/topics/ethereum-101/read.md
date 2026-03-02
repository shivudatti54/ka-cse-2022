# Introduction to Ethereum

## 1. What is Ethereum?

Ethereum is an open-source, globally decentralized computing infrastructure that executes programs called **smart contracts**. It is often described as a **world computer** or a **decentralized application platform**. Unlike Bitcoin, which was designed primarily as a peer-to-peer electronic cash system, Ethereum was created to be a programmable blockchain, allowing developers to build and deploy decentralized applications (dApps) of all kinds.

Proposed in late 2013 and developed in 2014 by Vitalik Buterin, Ethereum went live on July 30, 2015. Its native cryptocurrency is called **Ether (ETH)**.

**Key Differentiator from Bitcoin:** While Bitcoin's script language is limited and designed primarily for financial transactions, Ethereum's Turing-complete programming language allows for the creation of arbitrarily complex logic, enabling a vast ecosystem of applications beyond simple currency transfer.

## 2. The Ethereum Stack

The Ethereum ecosystem can be visualized as a technology stack comprising several layers.

```
+---------------------------------------+
|          Decentralized Apps (dApps)   |  Application Layer
+---------------------------------------+
|          Smart Contracts              |  Contract Layer
+---------------------------------------+
|          Ethereum Virtual Machine (EVM)|  Execution Layer
+---------------------------------------+
|          Consensus Mechanism (PoW/PoS)|  Consensus Layer
+---------------------------------------+
|          Ethereum Blockchain          |  Data Layer
+---------------------------------------+
|          Peer-to-Peer Network         |  Network Layer
+---------------------------------------+
```

**1. Network Layer:** The underlying peer-to-peer (P2P) protocol that allows nodes to discover each other and propagate transactions and blocks.
**2. Data Layer:** The blockchain itself, a cryptographically secured ledger of all transactions and data.
**3. Consensus Layer:** The mechanism (currently Proof-of-Stake) used to achieve agreement on the state of the blockchain.
**4. Execution Layer:** The Ethereum Virtual Machine (EVM), which executes the code of smart contracts.
**5. Contract Layer:** The smart contract code, written in languages like Solidity or Vyper.
**6. Application Layer:** The user-facing dApps, such as DeFi protocols, NFT marketplaces, and games, which interact with the underlying smart contracts.

## 3. The Ethereum Blockchain

At its core, the Ethereum blockchain is a transaction-based state machine. It begins with a **genesis state** and incrementally updates its state by processing transactions bundled into blocks.

**Block Structure:** An Ethereum block contains more information than a Bitcoin block, reflecting its more complex functionality.

| Component | Description |
| :--- | :--- |
| **Block Header** | Contains metadata about the block. |
| - parentHash | Hash of the parent block, linking it to the chain. |
| - ommersHash | Hash of the list of ommers (uncles) for this block. |
| - beneficiary | The address that receives the mining reward (fees). |
| - stateRoot | The root hash of the Merkle Patricia state tree. |
| - transactionsRoot | The root hash of the Merkle tree of all transactions in this block. |
| - receiptsRoot | The root hash of the Merkle tree of transaction receipts. |
| - logsBloom | A Bloom filter composed of indexable information (logs) from this block. |
| - difficulty | The pre-merge PoW difficulty target of this block. |
| - number | The block number (height). |
| - gasLimit | The maximum gas allowed in this block. |
| - gasUsed | The total gas used by all transactions in this block. |
| - timestamp | The Unix time when the block was mined. |
| - extraData | Optional extra data that can be included by miners. |
| - mixHash | A hash that proves the correct amount of computation was done (PoW). |
| - nonce | A value used in the PoW mining process. |
| **Transactions** | The list of transactions included in the block. |
| **Ommers (Uncles)** | Headers of blocks that are children of the parent but not part of the main chain. |

## 4. Ether (ETH) and Gas

### Ether (ETH)
Ether is the native cryptocurrency of the Ethereum network. It serves two primary purposes:
1.  **A Store of Value and Medium of Exchange:** It can be traded and used as a currency.
2.  **Fuel for the Network:** It is used to pay for the computational resources required to execute operations on the network. This payment is called **gas**.

### Gas
Every operation on the Ethereum Virtual Machine (EVM) has a fixed **gas cost**. Gas is the unit that measures the computational effort required to execute specific operations. The purpose of gas is to:
-   Compensate miners/validators for the resources (CPU, memory, storage) they use.
-   Prevent infinite loops and Denial-of-Service (DoS) attacks by requiring a cost for every computation. If a transaction runs out of gas, it fails and all changes are reverted, but the gas fee is still paid.

The total fee for a transaction is calculated as:
`Total Fee = Gas Units Used * Gas Price (in gwei)`

Where:
-   **Gas Units (Gas Limit):** The maximum amount of gas a user is willing to spend on a transaction. For simple ETH transfers, this is typically 21,000 gas. For contract interactions, it is much higher.
-   **Gas Price:** The price (in gwei) the user is willing to pay per unit of gas. 1 gwei = 10^-9 ETH.
-   **Base Fee:** A fee that is burned (destroyed), introduced by EIP-1559. It is algorithmically determined based on network congestion.
-   **Priority Fee (Tip):** An optional tip to the miner/validator to incentivize them to include the transaction.

## 5. Consensus Mechanism: From Proof-of-Work to Proof-of-Stake

Ethereum's consensus mechanism has undergone a monumental shift, known as "The Merge," from Proof-of-Work (PoW) to Proof-of-Stake (PoS).

### Proof-of-Work (PoW) - Historical
Ethereum initially used a PoW algorithm called **Ethash**, which was ASIC-resistant. Miners competed to solve a cryptographic puzzle. The first miner to find a valid solution (nonce) would broadcast the block to the network and receive a block reward. This process was energy-intensive, similar to Bitcoin's mechanism.

### Proof-of-Stake (PoS) - Current
The current consensus mechanism is called the **Gasper** protocol, a combination of the **Greedy Heaviest Observed Subtree (GHOST)** and **Casper the Friendly Finality Gadget (FFG)**.

**Key Participants:**
-   **Validators:** Instead of miners, validators are chosen to propose and attest to blocks. To become a validator, one must **stake** 32 ETH. This stake acts as a security deposit.
-   **Proposer:** A validator randomly selected to propose a new block for a specific slot.
-   **Attesters (Committee):** A group of validators randomly selected to vote on the validity of the proposed block.

**How it Works:**
1.  **Epochs and Slots:** Time is divided into **slots** (12 seconds) and **epochs** (32 slots = 6.4 minutes).
2.  **Block Proposal:** For each slot, one validator is randomly chosen to be the block proposer.
3.  **Attestation:** A committee of validators attests (votes) that they have seen the block and believe it is valid.
4.  **Finality:** Blocks are first "justified." After two epochs, if 2/3 of validators agree, a block becomes **finalized** and cannot be reverted without slashing (burning) the staked ETH of the attackers.

**Benefits of PoS:**
-   **Energy Efficiency:** ~99.95% less energy consumption than PoW.
-   **Increased Security:** Higher cost to attack the network (staking 33% of total ETH is far more expensive than acquiring 51% of hashrate).
-   **Decentralization:** Lower barrier to entry for participating in consensus (no need for expensive ASICs).

## 6. Transactions

An Ethereum transaction is a signed data package that authorizes a specific action on the network.

**Transaction Structure:**
-   **nonce:** A sequence number issued by the account, preventing replay attacks.
-   **gasPrice:** The price willing to be paid per gas unit (superseded by `maxFeePerGas` and `maxPriorityFeePerGas` post EIP-1559).
-   **gasLimit:** The maximum gas allotted for the transaction.
-   **to:** The recipient's address. If empty, it creates a new contract.
-   **value:** The amount of ETH (in wei) to transfer.
-   **data:** The payload containing the smart contract code or function call data.
-   **v, r, s:** The components of the ECDSA digital signature.

**Types of Transactions:**
1.  **Value Transfer:** Simple sending of ETH from one Externally Owned Account (EOA) to another.
2.  **Contract Deployment:** A transaction sent to the zero-address (`0x0`) with the contract code in the `data` field.
3.  **Contract Interaction:** A transaction sent to a contract address, with a function call and parameters encoded in the `data` field.

## 7. Ethereum Virtual Machine (EVM)

The EVM is the heart of Ethereum. It is a quasi-Turing-complete, sandboxed virtual stack machine that exists on every node in the network. Its purpose is to execute the bytecode compiled from smart contract code.

**Key Characteristics:**
-   **Sandboxed:** Code executed in the EVM has no access to the network, filesystem, or other processes of the host computer.
-   **Stack-based:** It uses a last-in-first-out (LIFO) stack with a depth of 1024 items.
-   **Deterministic:** The same input (transaction + current state) will always produce the same output on every node.
-   **Gas-metered:** Every opcode (e.g., `ADD`, `SSTORE`) has a gas cost, halting execution if the allotted gas is depleted.

```
+-----------------------------+
| Smart Contract (Solidity)   |
+-----------------------------+
            | Compilation
            V
+-----------------------------+
| Bytecode (deployed on-chain)|
+-----------------------------+
            | Execution
            V
+-----------------------------+
|   Ethereum Virtual Machine  |  <-- Runs on every node
+-----------------------------+
            | State Change
            V
+-----------------------------+
|   World State (Updated)     |
+-----------------------------+
```

## 8. Accounts

Ethereum has two fundamental types of accounts, a crucial difference from Bitcoin's UTXO model.

| Feature | Externally Owned Account (EOA) | Contract Account (CA) |
| :--- | :--- | :--- |
| **Control** | Controlled by a private key. | Controlled by its contract code. |
| **Creation** | Created automatically when a private key is generated. | Created by a transaction from an EOA or another contract. |
| **Private Key** | **Yes** | No |
| **Can Initiate Tx** | **Yes** | No (can only respond to a transaction) |
| **Has Code?** | No | **Yes** (bytecode) |
| **Has Storage?** | No | **Yes** |

-   An **Externally Owned Account (EOA)** is an account controlled by a private key. It can send transactions (transfer ETH or trigger contract code) and is identified by its public address.
-   A **Contract Account (CA)** is an account that has its own code and storage. It cannot initiate transactions on its own; it can only execute its code in response to a transaction sent from an EOA or another CA.

## 9. Ethereum Networks

There is not just one "Ethereum" network. Multiple networks exist for different purposes:

1.  **Mainnet:** The primary, public Ethereum production blockchain. Real value exists here.
2.  **Testnets:** Public networks used for testing without using real money. Common testnets include:
    -   **Sepolia:** The current recommended testnet for application development.
    -   **Goerli:** A previous primary testnet, now deprecated.
    -   **Holesky:** A testnet designed for protocol development and staking testing.
3.  **Devnets/Localnets:** Networks like Ganache or a local Hardhat node, run on a developer's machine for rapid testing and debugging.

## Exam Tips

-   **Understand the "Why":** Be prepared to explain why Ethereum was created and how its purpose differs from Bitcoin's. Focus on programmability and smart contracts.
-   **Gas Calculation is Key:** You will almost certainly be asked to calculate the cost of a transaction. Remember: `Total Fee = Gas Used * Gas Price`. Know the approximate gas cost for a simple transfer (21,000 gas).
-   **Account Model vs. UTXO:** Be able to clearly contrast Ethereum's account-based model with Bitcoin's UTXO model, listing the advantages and disadvantages of each.
-   **PoS Details Matter:** Since The Merge is a pivotal event, understand the roles of validators, proposers, attestors, and the concepts of staking, slashing, finality, and epochs/slots.
-   **EVM is a Stack Machine:** Remember that the EVM is stack-based and that its execution is entirely deterministic and isolated (sandboxed).
-   **Know the Networks:** Be able to distinguish between Mainnet, testnets (Sepolia, Goerli), and development networks, and understand their respective use cases.