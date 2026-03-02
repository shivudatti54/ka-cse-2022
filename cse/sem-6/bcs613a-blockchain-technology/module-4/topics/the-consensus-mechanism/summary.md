# The Consensus Mechanism

## Overview

Ethereum evolved from Proof-of-Work (Ethash algorithm) to Proof-of-Stake (Beacon Chain) through "The Merge" in September 2022. This transition reduced energy consumption by 99.95% while maintaining decentralization and security through economic stake rather than computational power.

## Key Points

- **Pre-Merge (PoW)**: Ethash algorithm requiring 4GB+ memory, ASIC-resistant design favoring GPUs
- **The Merge (Sept 2022)**: Transition from PoW to PoS consensus, combining execution and consensus layers
- **Proof-of-Stake**: Validators stake 32 ETH to propose and attest blocks, earning rewards
- **Beacon Chain**: PoS consensus layer coordinating validators and managing stake
- **Finality**: Casper FFG provides checkpoint finality after two epochs (approximately 13 minutes)
- **Slashing**: Validators lose staked ETH for malicious behavior or downtime
- **Random Selection**: VRF-based validator selection for fairness and security

## Important Concepts

- PoS validators lock capital (32 ETH) creating economic security model
- Slashing mechanism punishes dishonest validators, losing portion of stake
- Finality stronger than PoW probabilistic confirmation
- Energy efficiency: PoS requires minimal computational resources vs PoW mining
- Validator rewards from block proposal, attestations, and sync committee participation

## Notes

- Understand PoW to PoS transition motivation: energy efficiency, security, scalability
- Know minimum stake requirement: 32 ETH per validator
- Be able to explain slashing conditions and penalties
- Remember The Merge date: September 15, 2022
