# Types of Transaction

## Overview

Bitcoin supports various transaction types serving different purposes: standard P2PKH transfers, coinbase transactions creating new bitcoin, multi-signature transactions requiring multiple approvals, and SegWit transactions improving efficiency and enabling Layer 2 solutions.

## Key Points

- **P2PKH (Pay-to-Public-Key-Hash)**: Most common type, pays to hashed public key address starting with '1'
- **P2SH (Pay-to-Script-Hash)**: Pays to script hash for multi-signature and complex conditions, addresses start with '3'
- **Coinbase Transaction**: First transaction in every block, creates new BTC, no inputs, 100-block maturity period
- **Multi-Signature**: Requires M-of-N signatures to spend (e.g., 2-of-3), used for escrow and enhanced security
- **P2WPKH/P2WSH (SegWit)**: Segregated Witness transactions separating signature data, smaller size, lower fees, addresses start with 'bc1'
- **Time-Locked Transactions**: Use locktime or sequence for delayed spending (HTLC for Lightning Network)

## Important Concepts

- P2PKH script: OP_DUP OP_HASH160 <PubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
- Coinbase transactions include block reward plus all transaction fees from block
- Multi-sig enables shared control for company funds or escrow services
- SegWit fixes transaction malleability enabling Lightning Network
- Different address formats indicate transaction type and network (mainnet vs testnet)

## Notes

- Know script structure for P2PKH transactions
- Understand coinbase special properties: no inputs, creates new BTC, maturity requirement
- Be able to explain multi-signature use cases and M-of-N notation
- Remember SegWit benefits: smaller transactions, lower fees, malleability fix
