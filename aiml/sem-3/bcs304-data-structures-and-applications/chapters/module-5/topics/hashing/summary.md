# Hashing - Summary

## Key Definitions and Concepts

- **Hash Function**: A mathematical function that maps keys to array indices, typically producing a fixed-size output from variable-size input.
- **Collision**: When two different keys hash to the same index in the hash table.
- **Load Factor (α)**: The ratio of the number of elements (n) to the table size (m), i.e., α = n/m.
- **Separate Chaining**: Collision resolution where each bucket holds a linked list of all keys hashing to that bucket.
- **Open Addressing**: Collision resolution where all elements are stored in the table, using probing to find empty slots.
- **Linear Probing**: Open addressing using h(k, i) = (h'(k) + i) mod m.
- **Quadratic Probing**: Open addressing using h(k, i) = (h'(k) + c₁i + c₂i²) mod m.
- **Double Hashing**: Open addressing using h(k, i) = (h₁(k) + i·h₂(k)) mod m.
- **Static Hashing**: Fixed-size table requiring complete rehashing when resized.
- **Dynamic Hashing**: Allows table growth/shrinkage without complete rehashing.
- **Universal Hashing**: Random selection from a family of hash functions for probabilistic guarantees.

## Important Formulas and Theorems

- Division method: h(k) = k mod m
- Multiplication method: h(k) = floor(m(kA mod 1)), where A ≈ 0.618
- Expected probes (successful search, open addressing): (1/α)·ln(1/(1-α))
- Expected probes (unsuccessful search, open addressing): 1/(1-α)
- Universal hashing condition: P(h(x) = h(y)) ≤ 1/m for distinct x, y

## Key Points

- Hashing provides O(1) average-case time complexity for insert, search, and delete operations.
- A good hash function must be deterministic, uniform, and computationally efficient.
- Table size m should be a prime number not close to powers of 2 for the division method.
- Open addressing requires load factor below 0.5-0.7; separate chaining can handle higher loads.
- Linear probing suffers from primary clustering; double hashing eliminates this problem.
- Dynamic hashing (extendible, linear) avoids costly rehashing but adds implementation complexity.
- The choice between collision resolution techniques depends on expected load factor and memory constraints.
- Universal hashing provides probabilistic guarantees against adversarial input sequences.

## Common Mistakes to Avoid

1. Choosing table size as a power of 2 in division method, which causes keys with certain bit patterns to cluster.
2. Not handling deletion properly in open addressing—simply removing elements breaks probe sequences.
3. Ignoring load factor thresholds—allowing α to exceed recommended values severely degrades performance.
4. Using poor hash functions that don't distribute keys uniformly, leading to excessive collisions.
5. Confusing static and dynamic hashing—the former requires complete rehashing during resize, the latter does not.

## Revision Tips

1. Practice inserting and searching in hash tables by hand for all collision resolution techniques.
2. Remember the probe sequence formulas for linear, quadratic, and double hashing.
3. Know the load factor thresholds: 0.5-0.7 for open addressing, 1.0 for separate chaining.
4. Understand when to use each collision resolution technique based on application requirements.
5. Review extendible hashing concepts including global depth, local depth, and directory expansion.