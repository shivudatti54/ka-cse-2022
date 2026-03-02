# Bitcoin Transactions

## Overview

Bitcoin transactions are signed data structures transferring value through inputs and outputs, using the UTXO (Unspent Transaction Output) model rather than account balances. Each transaction references previous unspent outputs, provides cryptographic proof of ownership, and creates new outputs for recipients and change.

## Key Points

- **UTXO Model**: Must spend entire unspent outputs; leftover returns as change to new address
- **Transaction Components**: Version, input count, inputs (previous TX hash, output index, ScriptSig, sequence), output count, outputs (value, ScriptPubKey), locktime
- **ScriptSig**: Unlocking script providing signature and public key to prove ownership
- **ScriptPubKey**: Locking script defining spending conditions (P2PKH, P2SH, P2WPKH types)
- **Transaction Fee**: Calculated as Sum(Inputs) - Sum(Outputs), incentivizes miners
- **Coinbase Transaction**: First transaction in block creating new bitcoins, no inputs, must mature 100 blocks
- **Transaction Verification**: Nodes check valid inputs, signatures, sufficient funds, script execution, size limits

## Important Concepts

- Transaction lifecycle: create → sign → broadcast → mempool → mining → confirmation → finality (6 confirmations)
- Fee rate measured in satoshis per byte determines confirmation priority
- P2PKH script execution uses stack-based operations: OP_DUP, OP_HASH160, OP_EQUALVERIFY, OP_CHECKSIG
- SegWit (Segregated Witness) fixes transaction malleability by separating signature data
- Transaction ID is double SHA-256 hash of transaction data

## Notes

- Understand UTXO model fundamentally different from account-based systems
- Know all transaction component structures and their purposes
- Be able to calculate transaction fees and explain fee rate impact
- Remember coinbase transactions are special: create new BTC, no inputs, 100-block maturity
