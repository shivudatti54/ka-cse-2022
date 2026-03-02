# The Ethereum Network - Summary

## Core Concepts

- **Ethereum**: A programmable blockchain platform enabling smart contracts and dApps
- **Clients**: Multiple implementations (Geth, Besu, Nethermind) ensure network resilience
- **Stack Architecture**: Four-layer model (Network, Data, Consensus, Application)
- **Native Tokens**: ETH (primary) and ETC (DAO fork legacy)
- **Gas**: Computational unit preventing infinite execution; EIP-1559 introduced base fee burning
- **Consensus**: Transitioned from PoW to PoS (The Merge, 2022), achieving 99.95% energy reduction
- **World State**: Account-based model using Merkle Patricia Trie for efficient state verification
- **EVM**: Stack-based Turing-complete virtual machine with gas-limited execution

## Technical Definitions

- **Gas**: Unit measuring computational work (1 gas = minimum unit for simple operation)
- **Merkle Patricia Trie**: Cryptographic data structure enabling efficient state verification
- **Byzantine Fault Tolerance**: Property allowing continued operation with up to ⅓ faulty/malicious nodes
- **EOA (Externally Owned Account)**: User-controlled account signed by private key

## Key Formulas

- **Transaction Fee**: Gas Used × (Base Fee + Priority Fee)
- **Block Gas Limit**: Maximum computational work per block (~30 million gas post-1559)