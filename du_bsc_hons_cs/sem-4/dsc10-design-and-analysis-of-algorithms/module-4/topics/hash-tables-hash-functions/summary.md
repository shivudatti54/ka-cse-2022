# Hash Tables and Hash Functions - Summary

## Key Definitions and Concepts

- **Hash Table:** A data structure implementing an associative array that maps keys to values using a hash function for O(1) average-case operations.

- **Hash Function:** A function h(k) that computes an index in the range [0, m-1] for a given key k, where m is the table size.

- **Collision:** When two different keys hash to the same index, requiring resolution strategies.

- **Load Factor (α):** The ratio α = n/m, where n is the number of elements and m is table size. Critical for performance analysis.

- **Simple Uniform Hashing:** The theoretical assumption that each key is equally likely to hash to any bucket.

## Important Formulas and Theorems

| Method | Insert/Search Average | Space |
|--------|----------------------|-------|
| Chaining | O(1 + α) | O(n + m) |
| Linear Probing | O(1/(1-α)) | O(m) |
| Quadratic Probing | O(1/(1-α)) | O(m) |
| Double Hashing | O(1/(1-α)) | O(m) |

**Linear Probing Formula:** h(k, i) = (h'(k) + i) mod m

**Double Hashing Formula:** h(k, i) = (h₁(k) + i·h₂(k)) mod m

**Successful Search (Linear Probing):** (1/α) · ln(1/(1-α))

## Key Points

- Hash tables provide O(1) average-case time complexity for INSERT, DELETE, and SEARCH operations.

- Good hash functions must distribute keys uniformly across all buckets to minimize collisions.

- For division method, choose table size m as a prime number not close to powers of 2.

- Chaining handles collisions by maintaining a linked list at each bucket; can handle any load factor.

- Open addressing stores all elements in the table itself; requires load factor α < 1.

- Linear probing suffers from primary clustering; double hashing eliminates clustering using two hash functions.

- When load factor exceeds threshold (≈ 0.7 for open addressing), resize the table and rehash all elements.

- Universal hashing provides probabilistic guarantees against worst-case behavior.

## Common Mistakes to Avoid

1. Confusing load factor calculations—remember α = n/m, not m/n.

2. Forgetting that open addressing requires empty slots; operations fail when table is full.

3. Using poor table sizes (powers of 2 for division method) that cause poor distribution.

4. Assuming O(1) worst case—hash tables have O(n) worst case due to collisions.

5. Direct deletion in open addressing without using lazy deletion creates gaps in probe sequences.

## Revision Tips

1. Practice numerical problems: Given a sequence of keys, draw the final hash table for both chaining and linear probing.

2. Memorize the time complexity formulas and understand when each applies.

3. Review probe sequence calculations—be able to compute index positions for linear probing and double hashing.

4. Understand why certain table sizes and hash functions perform better through the uniformity principle.

5. Solve previous year DU questions on hash tables to familiarize with exam patterns and common question types.