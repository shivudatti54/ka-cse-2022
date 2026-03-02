# The Transaction Structure

## Overview

Bitcoin transactions are complex data structures containing version number, input list, output list, and locktime field. Each input references a previous unspent output with unlocking script, while each output specifies amount and locking script, implementing the UTXO model for value transfer.

## Key Points

- **Version Field (4 bytes)**: Transaction format version, typically 1 or 2
- **Input Count (VarInt)**: Number of transaction inputs (variable-length integer)
- **Input Structure**: Previous TX hash (32 bytes), output index (4 bytes), ScriptSig (variable), sequence (4 bytes)
- **Output Count (VarInt)**: Number of transaction outputs
- **Output Structure**: Value in satoshis (8 bytes), ScriptPubKey locking script (variable)
- **Locktime (4 bytes)**: Earliest time/block for transaction validity (0 = immediate, <500M = block height, ≥500M = timestamp)
- **Transaction ID**: Double SHA-256 hash of serialized transaction data

## Important Concepts

- ScriptSig (unlocking script) provides signature and public key to spend UTXO
- ScriptPubKey (locking script) defines spending conditions (P2PKH, P2SH, P2WPKH)
- Transaction fee implicitly calculated: Sum(Inputs) - Sum(Outputs)
- Sequence numbers enable relative timelocks via BIP68
- Locktime enables time-based or block-based transaction validity constraints

## Notes

- Understand complete input structure: prev hash, index, ScriptSig, sequence
- Know output structure: value (satoshis), ScriptPubKey
- Be able to calculate implicit transaction fee
- Remember Transaction ID is double SHA-256 of entire transaction
