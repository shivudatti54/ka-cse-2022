# Smart Contracts - Summary

## Key Definitions

- **Smart Contract**: A self-executing digital program stored on a blockchain that automatically enforces agreement terms when predefined conditions are met
- **Gas**: A computational unit measuring the work required to execute smart contract operations on Ethereum
- **EVM (Ethereum Virtual Machine)**: A runtime environment for executing smart contracts on the Ethereum network
- **Oracle**: External data service that provides off-chain information to smart contracts
- **Determinism**: The property where smart contracts produce identical outputs for the same inputs
- **Self-Destruct**: A function that removes contract code from the blockchain, terminating the contract

## Important Formulas

- **Total Transaction Fee** = Gas Used × Gas Price
- **Gas Limit** = Maximum gas a user is willing to consume for a transaction
- **Smart Contract Address**: Generated deterministically from deployer's address and nonce

## Key Points

1. Smart contracts were conceptualized by Nick Szabo in 1994, but practical implementation began with Ethereum in 2015
2. They operate on an "if-then" conditional logic - when conditions are met, actions execute automatically
3. Once deployed, smart contract code is immutable (cannot be changed), ensuring trust and security
4. The gas mechanism prevents infinite loops and ensures proper resource allocation on the network
5. Common standards include ERC-20 for fungible tokens and ERC-721 for non-fungible tokens (NFTs)
6. Smart contracts enable decentralized applications (DApps) and decentralized finance (DeFi) ecosystems
7. The "oracle problem" refers to the challenge of getting reliable external data into smart contracts
8. Smart contracts can be terminated through self-destruct functions or by becoming non-functional

## Common Mistakes

1. **Confusing smart contracts with legal contracts**: Smart contracts are executable code, not legally binding documents in traditional sense
2. **Ignoring the gas mechanism**: Failing to understand gas leads to failed transactions and financial losses
3. **Assuming immutability is absolute**: While code is immutable, data storage can be designed with update mechanisms
4. **Overlooking security vulnerabilities**: Reentrancy attacks, overflow errors, and access control issues are common exploit vectors in smart contracts