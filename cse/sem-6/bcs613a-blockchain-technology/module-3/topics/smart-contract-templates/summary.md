# Smart Contract Templates

## Overview

Smart contract templates are reusable code patterns and standardized implementations for common blockchain functionalities like token creation, multi-signature wallets, and decentralized exchanges. These templates accelerate development, reduce bugs through community auditing, and establish interoperability standards.

## Key Points

- **ERC-20**: Standard interface for fungible tokens on Ethereum (totalSupply, balanceOf, transfer, approve, transferFrom)
- **ERC-721**: Standard for non-fungible tokens (NFTs) representing unique digital assets
- **Multi-Signature Wallets**: Require M-of-N approvals for executing transactions
- **Escrow Contracts**: Hold funds until conditions met, then release to appropriate party
- **Time-Locked Contracts**: Release funds or execute functions after specific time/block
- **OpenZeppelin Library**: Battle-tested template library for secure contract development
- **Upgradeable Contracts**: Proxy patterns enabling contract logic updates while preserving state

## Important Concepts

- Token standards enable wallet and exchange interoperability
- Templates reduce security risks through community auditing and testing
- ERC-20 approve/transferFrom pattern enables decentralized exchanges
- NFT metadata standards define off-chain resource linking
- Proxy upgrade patterns separate logic from state storage

## Notes

- Know ERC-20 standard functions and their purposes
- Understand difference between fungible (ERC-20) and non-fungible (ERC-721) tokens
- Be able to explain multi-sig security benefits
- Remember templates accelerate development but require customization for specific use cases
