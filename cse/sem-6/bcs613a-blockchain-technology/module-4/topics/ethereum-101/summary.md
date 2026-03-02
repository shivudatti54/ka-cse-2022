# Ethereum 101

## Overview

Ethereum 101 covers fundamental concepts including accounts, transactions, gas, the Ethereum Virtual Machine, and smart contracts. It introduces the state transition function where transactions trigger state changes, and explains how Ethereum combines cryptocurrency functionality with programmable logic execution.

## Key Points

- **Two Account Types**: EOAs (externally owned, private key controlled) and Contract Accounts (code controlled, no private key)
- **Transaction Types**: Value transfers, contract deployment, contract function calls
- **Gas and Gas Price**: Gas measures computation, gas price in Gwei determines transaction cost
- **EVM Execution**: Stack-based virtual machine executing smart contract bytecode deterministically
- **Block Time**: Approximately 12 seconds per block (much faster than Bitcoin's 10 minutes)
- **Consensus Evolution**: Initially Proof-of-Work (Ethash), transitioned to Proof-of-Stake
- **State Trie**: Modified Merkle Patricia Trie stores account states efficiently

## Important Concepts

- EOA initiates transactions by signing with private key
- Contract accounts execute when triggered by transactions
- Gas limit prevents infinite loops, unused gas refunded
- Every operation has gas cost based on computational complexity
- World state contains all account balances and contract storage
- Transactions are atomic: fully succeed or fully revert

## Notes

- Know difference between EOA and contract accounts thoroughly
- Understand gas calculation: Gas Used × Gas Price = Transaction Fee
- Be able to explain EVM's role in executing smart contracts
- Remember Ethereum's faster block time enables quicker confirmations than Bitcoin
