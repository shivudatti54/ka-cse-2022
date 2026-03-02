# Accounts (Ethereum)

## Overview

Ethereum has two account types: Externally Owned Accounts (EOAs) controlled by private keys for initiating transactions, and Contract Accounts controlled by smart contract code executing when triggered. Both have ETH balance and nonce but differ fundamentally in control mechanisms and capabilities.

## Key Points

- **EOA Structure**: Address (20 bytes), balance (ETH amount), nonce (transaction count), controlled by private key
- **Contract Account Structure**: Address, balance, nonce, code hash (immutable contract code), storage hash (mutable state trie root)
- **EOA Capabilities**: Initiate transactions, send ETH, deploy contracts, call contract functions
- **Contract Capabilities**: Execute code when triggered, store data in persistent storage, call other contracts, emit events
- **Address Derivation**: EOA from public key keccak256 hash (last 20 bytes), contract from creator address and nonce
- **No Private Key for Contracts**: Contract accounts controlled solely by their code logic
- **Account State**: Part of world state trie, identified by 20-byte address

## Important Concepts

- Only EOAs can initiate transactions by signing with private key
- Contract accounts passively respond to received transactions
- Contract code immutable after deployment, storage state mutable
- All accounts stored in global state trie accessed by address
- Nonce prevents replay attacks for EOAs, counts contract creations for contracts

## Notes

- Understand fundamental difference: EOAs have private keys, contracts have code
- Know account structure fields for both types
- Be able to explain address derivation methods
- Remember only EOAs can originate transactions, contracts execute when called
