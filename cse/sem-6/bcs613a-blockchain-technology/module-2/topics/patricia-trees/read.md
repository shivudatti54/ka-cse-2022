# Patricia Trees (Radix Trees)

## Introduction

A **Patricia tree** (Practical Algorithm to Retrieve Information Coded in Alphanumeric), also known as a **radix tree** or **compact prefix tree**, is a space-optimized trie (prefix tree) data structure used in computer science for efficient storage and retrieval of strings and associated values. Unlike a standard trie where each node represents a single character, a Patricia tree compresses paths by merging nodes that have only one child, significantly reducing memory consumption while maintaining O(k) time complexity for insert and lookup operations, where k represents the length of the key.

In blockchain technology, Patricia trees serve as the foundational data structure for state management. Most notably, Ethereum employs **Merkle Patricia Trees (MPT)** to organize its world state, transaction receipts, and storage trie. The tree structure enables efficient state updates, light client proof verification, and tamper detection through cryptographic root hashes.

## Formal Definition

A Patricia tree is defined as a rooted tree T = (V, E) where:

- **V** represents the set of nodes, partitioned into leaf nodes and internal nodes
- **E** represents the set of edges, each labeled with a string fragment (nibble sequence in Ethereum)
- For every internal node v ∈ V, the edge labels to its children are pairwise distinct
- Each leaf node stores a value corresponding to the complete key formed by concatenating edge labels from the root

The key property distinguishing Patricia trees from standard tries is **path compression** (also called radix compression), where chains of nodes with single children are collapsed into single edges.

## Node Structure and Types

In the Ethereum implementation, a Merkle Patricia Tree employs three distinct node types:

### 1. Leaf Nodes (RLP encoded)

```
Leaf Node = [encoded_path, value]
```

The `encoded_path` encodes the remaining nibbles of the key, with the first nibble indicating the prefix type (even or odd length).

### 2. Extension Nodes

```
Extension Node = [encoded_path, next_node_hash]
```

Extension nodes consolidate paths where multiple keys share common prefixes, optimizing tree depth.

### 3. Branch Nodes

```
Branch Node = [v0, v1, ..., v15, vt]
```

Branch nodes handle key divergence at any position, with 17 children (v0-v15 for hexadecimal nibbles, vt for terminal values).

### Node Hash Computation

Each node is serialized using **Recursive Length Prefix (RLP)** encoding before being hashed using Keccak-256:

```
node_hash = keccak256(rlp_encode(node))
```

The root hash is computed from the hash of the root node, providing a cryptographic commitment to the entire dataset.

## Operations and Algorithms

### Search Operation

```
function find(node, key):
 if node is NULL:
 return NULL
 if key is empty:
 return node.value

 nibble = key[0]
 child = node.children[nibble]
 if child is NULL:
 return NULL

 return find(child, key[1:])
```

**Time Complexity**: O(k) where k = key length in nibbles
**Space Complexity**: O(k) for the recursion stack

### Insertion Operation

When inserting a key-value pair:

1. Traverse from root following key nibbles
2. At divergence point, create branch node
3. If path compression applies, create extension node
4. Insert value at terminal node

### Update and Delete

Updates require recalculating hashes along the affected path, propagating changes upward to maintain cryptographic integrity. Deletion may trigger tree reorganization if nodes become single-child chains.

## Merkle Proof Verification

One of the most significant advantages of Merkle Patricia Trees is the ability to generate **compact proofs** for light client verification:

### Types of Proofs

1. **Existence Proof**: Demonstrates a specific key-value pair exists in the tree
2. **Non-Existence Proof**: Proves a key is absent from the tree

A Merkle proof consists of:

- The target node's value
- Sibling node hashes at each level
- Path indices indicating left/right positions

The verifier reconstructs the root hash and compares it against the canonical root, achieving O(log N) verification complexity.

## Advantages and Trade-offs

### Advantages

| Property                     | Description                                                                            |
| ---------------------------- | -------------------------------------------------------------------------------------- |
| **Space Efficiency**         | Path compression reduces nodes from O(k) to O(k/c) where c is average path compression |
| **Search Complexity**        | O(k) worst case, often better due to compression                                       |
| **Deterministic Ordering**   | Keys maintain lexicographic ordering enabling range queries                            |
| **Cryptographic Commitment** | Root hash provides tamper-evident state                                                |

### Trade-offs

| Aspect                        | Consideration                                                                  |
| ----------------------------- | ------------------------------------------------------------------------------ |
| **Insertion Overhead**        | Requires hash recomputation O(log N) per insert                                |
| **Implementation Complexity** | More complex than hash tables                                                  |
| **Memory Usage**              | Higher overhead per node than simple key-value stores                          |
| **Rebalancing**               | Unlike B-trees, no automatic rebalancing; structure depends on insertion order |

## Ethereum-Specific Implementation

Ethereum employs three distinct Merkle Patricia Trees:

1. **State Trie**: Maps address → [nonce, balance, storageRoot, codeHash]
2. **Storage Trie**: Contract-specific key-value storage
3. **Transaction Trie**: Maps transaction index → transaction data
4. **Receipts Trie**: Maps transaction index → receipt data

The state trie uses 160-bit addresses as keys, while storage and transaction tries use varying key structures depending on context.

## Comparison with Alternative Data Structures

| Data Structure | Search   | Insert   | Space | Ordered | Merkle Proof |
| -------------- | -------- | -------- | ----- | ------- | ------------ |
| Patricia Tree  | O(k)     | O(k)     | O(k)  | Yes     | Yes          |
| Hash Table     | O(1)\*   | O(1)\*   | O(n)  | No      | No           |
| B-Tree         | O(log n) | O(log n) | O(n)  | Yes     | No           |
| Bloom Filter   | O(k)     | O(k)     | O(n)  | No      | No           |

\*Average case; worst case O(n)

## Exam Tips

1. **Understand path compression**: The fundamental distinction between tries and Patricia trees
2. **Know the three node types**: Leaf, Extension, and Branch nodes and their RLP encoding
3. **Merkle proof verification**: Be able to explain how root hash reconstruction enables trustless verification
4. **Ethereum context**: Understand why Ethereum chose MPTs over alternatives for state management
5. **Complexity analysis**: Memorize time and space complexities for all operations
6. **Proof of inclusion**: Understand how light clients use Merkle proofs to verify state without full node data
