# Wallets

## Overview

Bitcoin wallets are software applications that manage private keys, generate addresses, construct transactions, and interact with the blockchain. They range from full nodes storing the entire blockchain to lightweight SPV clients to hardware wallets providing offline key storage for enhanced security.

## Key Points

- **Wallet Types**: Full node wallets, SPV/lightweight wallets, web wallets, mobile wallets, hardware wallets, paper wallets
- **Key Management**: Generate, store, and secure private keys; derive public keys and addresses
- **Hierarchical Deterministic (HD) Wallets**: Generate multiple keys from single seed using BIP32/BIP44 standards
- **Seed Phrase**: 12-24 word mnemonic enabling wallet recovery (BIP39 standard)
- **Address Generation**: Wallet creates new addresses for each transaction to enhance privacy
- **Transaction Construction**: Builds transactions by selecting UTXOs, calculating fees, creating change outputs
- **Backup and Recovery**: Seed phrase backup allows wallet restoration on any compatible software

## Important Concepts

- Private keys never leave secure wallet environment in properly designed systems
- HD wallets derive unlimited addresses deterministically from single seed
- Hardware wallets keep private keys on isolated device, signing transactions offline
- SPV wallets verify payments using Merkle proofs without full blockchain download
- Multi-signature wallets require multiple keys for spending, enhancing security

## Notes

- Understand difference between hot wallets (online) and cold storage (offline)
- Know HD wallet advantages: single backup, address derivation, improved privacy
- Be able to explain seed phrase importance for recovery
- Remember wallet types and their security/convenience trade-offs
