# Hash Tables: Collision Resolution - Summary

## Key Definitions and Concepts

- **Hash Table**: A data structure that implements an associative array, mapping keys to values using a hash function for O(1) average-case access.

- **Collision**: When two or more distinct keys hash to the same table index.

- **Load Factor (α)**: The ratio n/m, where n is the number of elements and m is the table size. Determines collision probability and performance.

- **Open Addressing**: All elements stored within the table; collisions resolved by probing to find next empty slot.

- **Chaining**: Each bucket contains a linked list of elements hashing to that index; collisions handled by list insertion.

- **Rehashing**: Process of creating a new, larger hash table and re-inserting all existing elements when load factor exceeds threshold.

## Important Formulas and Theorems

| Technique | Probe Sequence Index |
|-----------|---------------------|
| Linear Probing | (h(k) + i) mod m |
| Quadratic Probing | (h(k) + i²) mod m |
| Double Hashing | (h₁(k) + i × h₂(k)) mod m |

- **Average successful search time (open addressing)**: ≈ (1/α) × ln(1/(1-α))
- **Average unsuccessful search time (open addressing)**: ≈ (1/(1-α))
- **Chaining average search**: O(1 + α)

## Key Points

1. Collisions are unavoidable when n > m (pigeonhole principle).

2. Linear probing suffers from primary clustering; quadratic probing reduces it but may have secondary clustering.

3. Double hashing eliminates both clustering problems using a secondary hash function.

4. For open addressing, keep load factor α < 0.5 for optimal performance.

5. Chaining handles deletions easily; open addressing requires special deletion handling (tombstones).

6. Chaining has O(n) worst-case but graceful degradation; open addressing has better cache performance.

7. Universal hashing provides probabilistic guarantees against worst-case inputs.

8. Common secondary hash function: h₂(k) = prime - (k mod prime), where prime < m.

## Common Mistakes to Avoid

1. **Confusing open addressing with chaining**: Remember open addressing stores elements in the table itself; chaining uses auxiliary data structures.

2. **Ignoring load factor**: Operating with α > 0.7 in open addressing causes severe performance degradation.

3. **Forgetting to handle deletions**: In open addressing, simply removing an element breaks probe sequences—use tombstones.

4. **Choosing non-prime table size**: Prime table sizes ensure better distribution in division method hashing.

5. **Assuming O(1) worst-case**: Hash tables have O(n) worst-case; O(1) is only average-case with good hash function and low load factor.

## Revision Tips

1. Practice drawing hash tables and tracing insertions with each probing technique.

2. Memorize the time complexity formulas and understand when each applies.

3. Remember that double hashing is generally preferred over linear/quadratic probing in open addressing.

4. For exams, be prepared to calculate probe sequences and final table states for given insertion sequences.

5. Understand the trade-offs table: Chaining = simple, handles high load; Open Addressing = cache-friendly, requires rehashing at lower α.