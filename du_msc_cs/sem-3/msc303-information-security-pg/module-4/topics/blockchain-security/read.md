# Blockchain Security

## Introduction
Blockchain security is a critical domain combining cryptography, distributed systems, and game theory to protect decentralized ledgers. As blockchain adoption grows in finance, supply chain, and governance, understanding its security mechanisms becomes essential for preventing billion-dollar exploits like the $614M Poly Network hack (2021).

The fundamental security proposition of blockchain lies in its decentralized consensus mechanisms and cryptographic immutability. However, emerging attack vectors in smart contracts, consensus protocols, and wallet infrastructure demand sophisticated analysis. Current research focuses on formal verification of smart contracts, post-quantum cryptography adaptations, and layer-2 security enhancements.

This topic is particularly relevant for DU MSc CS students as India's Digital Rupee (e₹) initiative and SEBI's blockchain adoption in securities markets create urgent demand for blockchain security experts. Understanding both theoretical foundations (Byzantine Fault Tolerance models) and practical vulnerabilities (reentrancy attacks) positions graduates at the forefront of this field.

## Key Concepts
1. **Consensus Security**: 
   - Proof-of-Work (PoW): Energy-intensive but battle-tested (Bitcoin)
   - Proof-of-Stake (PoS): Energy-efficient but vulnerable to "nothing-at-stake" attacks
   - Practical Byzantine Fault Tolerance (PBFT): Used in Hyperledger, requires 2/3 honest nodes

2. **Cryptographic Foundations**:
   - Merkle Trees: Data integrity through hierarchical hashing
   - Elliptic Curve Digital Signature Algorithm (ECDSA): Used in Bitcoin wallets
   - zk-SNARKs: Zero-knowledge proofs for privacy (Zcash)

3. **Smart Contract Vulnerabilities**:
   - Reentrancy attacks (DAO Hack 2016)
   - Integer overflow/underflow
   - Front-running (MEV attacks)

4. **Network Layer Attacks**:
   - 51% attacks (Ethereum Classic 2020)
   - Eclipse attacks: Isolating nodes
   - Sybil attacks: Fake node creation

5. **Privacy-Utility Tradeoff**:
   - Blockchain analysis tools (Chainalysis)
   - CoinJoin mixing vs. regulatory compliance
   - GDPR right-to-erasure conflicts

## Examples

**Example 1: Reentrancy Attack Analysis**
```solidity
// Vulnerable contract
contract Bank {
    mapping(address => uint) balances;
    
    function withdraw() public {
        uint bal = balances[msg.sender];
        (bool sent, ) = msg.sender.call{value: bal}("");
        balances[msg.sender] = 0;
    }
}
```
*Attack Steps:*
1. Attacker deploys malicious contract with fallback function calling withdraw()
2. Initial withdraw() triggers recursive calls before balance reset
3. Drains entire contract funds

*Solution:* Use Checks-Effects-Interactions pattern:
```solidity
balances[msg.sender] = 0; 
(bool sent, ) = msg.sender.call{value: bal}("");
```

**Example 2: 51% Attack Cost Calculation**
Given Ethereum Classic's $0.12/kWh electricity cost:
```
Network Hashrate: 1.5 TH/s
Antminer E9 efficiency: 0.085 J/MH
Attack Cost = (Hashrate * Energy Efficiency * Electricity Cost) / 3.6e6
= (1.5e12 H/s * 0.085e-6 J/H * $0.12) / 3.6e6
= $4,250/hour
```

**Example 3: zk-SNARKs in Zcash**
1. Prover generates proof π for transaction validity
2. Verifier checks: e(π, [γ]G2) ?= e([α]G1 + [β]G1, [δ]G2)
3. Valid without revealing sender/receiver/amount

## Exam Tips
1. Memorize Nakamoto Consensus parameters: 6-block confirmation depth in Bitcoin
2. Understand BFT vs. Nakamoto consensus tradeoffs: Finality vs. probabilistic confirmation
3. Practice writing secure Solidity code with OpenZeppelin libraries
4. Study real-world attacks: DAO (2016), Parity Wallet (2017), Poly Network (2021)
5. Know EIPs: ERC-20 (fungible), ERC-721 (NFT), ERC-4337 (account abstraction)
6. Analyze consensus economics: Staking yields vs. slashing risks in PoS
7. Prepare for diagram questions: Merkle tree construction, UTXO model