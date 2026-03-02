# Transactions (Ethereum)

## Overview

Ethereum transactions are signed messages transitioning world state, containing nonce, gas price, gas limit, recipient, value, data, and signature components. They trigger state changes through value transfers, contract deployments, or contract function calls, forming the fundamental state transition mechanism.

## Key Points

- **Transaction Fields**: Nonce (sender transaction count), gas price (Gwei per gas), gas limit (max gas), to (recipient), value (ETH amount), data (bytecode/function call), v/r/s (signature)
- **Transaction Types**: Legacy (type 0), EIP-2930 (type 1 with access lists), EIP-1559 (type 2 with base fee)
- **EIP-1559**: Separates base fee (burned) from priority fee (to miners), improving fee predictability
- **Nonce Purpose**: Prevents replay attacks, ensures transaction ordering
- **Signature**: ECDSA signature proving transaction authorization by private key holder
- **Transaction Hash**: Keccak-256 hash serving as unique transaction identifier
- **Atomic Execution**: Either fully succeeds or fully reverts, no partial execution

## Important Concepts

- EIP-1559 burns base fee, reducing ETH supply over time (deflationary pressure)
- Gas limit sets maximum computation allowed, unused gas refunded
- Nonce must increment sequentially from sender account
- Transaction pool (mempool) holds pending transactions awaiting inclusion
- Revert operations roll back state changes but still consume gas

## Notes

- Know EIP-1559 fee structure: base fee + priority fee (tip)
- Understand nonce role in preventing replay and ensuring order
- Be able to explain transaction signature components (v, r, s)
- Remember three transaction types: legacy, EIP-2930, EIP-1559
