# Blockchain Security - Summary

## Key Definitions and Concepts
- **Byzantine Fault Tolerance**: System resilience against malicious nodes
- **Nonce**: Number used once in mining to vary hash output
- **UTXO**: Unspent Transaction Output model (Bitcoin)
- **Gas**: Computation pricing unit in Ethereum
- **Merkle Root**: Single hash representing all transactions in block

## Important Formulas and Theorems
- **SHA-256**: H(x) = (a*x + b) mod p (Cryptographic hash)
- **PoW Difficulty**: D = T / H where T=Target, H=Hashrate
- **Nakamoto Consensus Security**: P(attack) ≈ (q/p)^z (q=attacker hash power, z=confirmations)
- **Bonding Curve**: Price = k * supply (Token minting economics)

## Key Points
- Blockchain immutability depends on honest majority in consensus
- Smart contracts require formal verification (e.g., Certora Prover)
- Privacy coins face regulatory scrutiny (FATF Travel Rule)
- Layer-2 solutions introduce new attack surfaces (Plasma chain fraud proofs)
- Post-quantum threats: Shor's algorithm breaks ECDSA in O(n^3)
- India's Web3 strategy requires KYC-compliant DeFi
- Zero-knowledge rollups (zk-Rollups) enhance scalability & privacy

## Common Mistakes to Avoid
- Assuming "immutable" means unchangeable (forgetting hard forks)
- Confusing transaction privacy with identity anonymity
- Overlooking front-running in DEX arbitrage
- Ignoring gas optimization leading to DoS attacks

## Revision Tips
1. Create attack trees for different consensus mechanisms
2. Practice Solidity security patterns using Damn Vulnerable DeFi challenges
3. Compare PoW vs PoS security using Python simulations
4. Study RBI's blockchain sandbox reports for India-specific use cases