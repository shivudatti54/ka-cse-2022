# Ethereum Virtual Machine (EVM)

## Overview

The Ethereum Virtual Machine is a Turing-complete, stack-based virtual machine that executes smart contract bytecode deterministically across all Ethereum nodes. It provides isolated sandbox environment ensuring contract execution produces identical results network-wide, enabling trustless computation.

## Key Points

- **Stack-Based Architecture**: 256-bit word size stack with 1024 depth limit for operation execution
- **Bytecode Execution**: Compiles high-level languages (Solidity, Vyper) to EVM bytecode opcodes
- **Deterministic**: Same input always produces same output across all nodes globally
- **Gas Metering**: Every operation has gas cost preventing infinite loops and incentivizing efficiency
- **Isolation**: Sandboxed environment where contracts cannot access node's file system or network
- **State Persistence**: Modified Merkle Patricia Trie stores contract storage permanently on blockchain
- **Opcodes**: 140+ operations including arithmetic, logical, storage, memory, and flow control

## Important Concepts

- EVM executes bytecode, not source code directly (compilation required)
- Gas costs vary by operation complexity: storage expensive, arithmetic cheap
- Stack manipulation and memory operations form core of contract logic
- Contract state persists between function calls via storage trie
- Reverting execution rolls back all state changes, consuming gas

## Notes

- Understand stack-based execution model fundamentals
- Know difference between memory (temporary) and storage (permanent)
- Be able to explain gas metering purpose and mechanism
- Remember deterministic execution ensures network consensus on contract results
