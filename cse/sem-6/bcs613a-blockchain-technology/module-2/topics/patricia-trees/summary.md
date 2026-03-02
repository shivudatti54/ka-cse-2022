# Patricia Trees Summary

## Core Concepts
- A **Patricia tree** (radix tree) is a space-optimized trie that compresses single-child paths into single edges
- **Path compression** reduces space complexity while maintaining O(k) lookup time where k = key length
- **Merkle Patricia Trees (MPT)** combine Patricia tree structure with cryptographic hashing for tamper detection

## Node Types
| Node Type | Structure | Purpose |
|-----------|-----------|---------|
| Leaf | [encoded_path, value] | Stores terminal key-value pairs |
| Extension | [encoded_path, hash] | Consolidates shared prefixes |
| Branch | [16 children, value] | Handles key divergence points |

## Complexity Analysis
- **Search**: O(k) time, O(k) stack space
- **Insert**: O(k) time, O(k) space, O(log n) hash recomputation
- **Space**: O(k/c) where c = average compression factor

## Key Properties
- **Deterministic ordering** enables range queries
- **Root hash** provides cryptographic commitment to entire dataset
- **Merkle proofs** allow O(log n) verification without full data
- Used in Ethereum for state, storage, transaction, and receipts tries

## Important Formulas
- Node hash: `node_hash = keccak256(rlp_encode(node))`
- Proof verification reconstructs root hash from sibling hashes and path indices

## Trade-offs
- Advantages: Space efficiency, ordered traversal, cryptographic security, proof capability
- Disadvantages: Higher implementation complexity, insertion overhead, no automatic rebalancing