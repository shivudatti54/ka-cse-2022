# Consensus

## Overview

Consensus is the fundamental process enabling distributed blockchain nodes to agree on transaction validity, order, and ledger state without central authority. It solves the challenge of achieving agreement among potentially unreliable or malicious participants through cryptographic proofs and economic incentives.

## Key Points

- **Agreement**: All non-faulty nodes must decide on the same value or block validity
- **Validity**: Consensus output must reflect actual proposed values, not arbitrary results
- **Termination**: All non-faulty nodes must eventually reach decision without infinite loops
- **Integrity**: Nodes can only decide on values actually proposed by network participants
- **Byzantine Fault Handling**: System tolerates nodes sending conflicting or malicious messages
- **Crash Fault Tolerance**: System continues functioning when nodes simply stop working
- **CAP Theorem Navigation**: Blockchains balance consistency, availability, and partition tolerance trade-offs

## Important Concepts

- Consensus distinguishes blockchain from traditional centralized databases
- Permissioned blockchains use efficient voting protocols (PBFT) with known participants
- Permissionless blockchains require Sybil-resistant mechanisms (PoW, PoS) for anonymous participants
- Different consensus types suit different trust models and performance requirements
- Foundation for all blockchain functionality including transaction validation and state management

## Notes

- Understand core properties: agreement, validity, termination, integrity
- Know difference between crash faults and Byzantine faults
- Be able to explain why consensus is harder in trustless environments
- Remember that consensus mechanisms are the solution to the Byzantine Generals Problem
