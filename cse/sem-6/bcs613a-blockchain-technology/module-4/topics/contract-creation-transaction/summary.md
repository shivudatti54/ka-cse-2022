# Contract Creation Transaction

## Overview

Contract creation transactions deploy new smart contracts to Ethereum blockchain by sending transaction with bytecode in data field and empty recipient address. The transaction creates new contract account with unique address, initializes state, and stores code permanently on blockchain.

## Key Points

- **Empty Recipient**: Contract creation uses null address (0x0) as recipient to signal deployment
- **Bytecode Payload**: Transaction data field contains compiled contract bytecode and constructor parameters
- **Contract Address**: Deterministically derived from sender address and nonce using RLP encoding and Keccak-256
- **Gas Requirement**: Deployment requires substantial gas for code storage and initialization
- **Constructor Execution**: Runs once during deployment to initialize contract state
- **Deployment Cost**: Gas for bytecode storage (200 gas per byte) plus execution costs
- **Immutable Code**: Once deployed, contract code cannot be modified (state can change)

## Important Concepts

- Contract address calculation: keccak256(rlp([sender_address, nonce]))[12:]
- Constructor parameters encoded and appended to bytecode
- Failed deployment consumes gas but doesn't create contract
- CREATE2 opcode enables deterministic address calculation independent of nonce
- Contract deployment transaction has no function selector (constructor identified by bytecode)

## Notes

- Know contract address derivation formula using sender and nonce
- Understand deployment gas includes both storage and execution costs
- Be able to explain constructor role in initialization
- Remember deployed code is immutable but contract state is mutable
