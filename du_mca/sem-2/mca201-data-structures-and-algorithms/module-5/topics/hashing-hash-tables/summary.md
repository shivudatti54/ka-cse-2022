# Hashing and Hash Tables - Summary

## Key Definitions and Concepts
- **Hash Function**: Algorithm mapping keys to table indices
- **Collision**: Two keys hashing to same index
- **Load Factor**: Ratio of entries to table size (α = n/m)
- **Open Addressing**: Collision resolution using probing sequences
- **Universal Hashing**: Randomized hash function family

## Important Formulas and Theorems
- **Division Method**: h(k) = k mod m (m prime preferred)
- **Linear Probing**: h(k,i) = (h'(k) + i) mod m
- **Double Hashing**: h(k,i) = h1(k) + i*h2(k) mod m
- **Expected Probes** (Unsuccessful Search): ≈ 1/(1-α) for open addressing

## Key Points
- Optimal table size is prime number to reduce clustering
- Separate chaining handles collisions better for high α values
- Double hashing requires h2(k) ≠ 0 and coprime with table size
- Dynamic resizing maintains O(1) amortized time complexity
- Cryptographic hashes are computationally expensive for tables
- Cuckoo hashing provides worst-case O(1) lookups with multiple tables
- Distributed hash tables use consistent hashing for scalability

## Common Mistakes to Avoid
- Using non-prime table sizes with division method
- Forgetting to update size during rehashing operations
- Implementing h2(k) that returns 0 in double hashing
- Ignoring load factor leading to performance degradation

## Revision Tips
1. Practice probing sequences with different collision methods
2. Create comparison charts for collision resolution techniques
3. Solve numerical problems on load factor and rehashing
4. Study real implementations (Java HashMap, Python dict)
5. Memorize time complexity formulas for different operations

Length: 650 words