# HASHING - Summary

## Key Definitions and Concepts

- HASH FUNCTION: A mathematical function that maps keys to array indices in a hash table, typically using modulo arithmetic or multiplication methods.

- COLLISION: Occurs when two different keys produce the same hash value and must be stored in the same table location.

- LOAD FACTOR (α): The ratio of the number of elements stored (n) to the table size (m), expressed as α = n/m. It determines the efficiency of hash table operations.

- OPEN ADDRESSING: Collision resolution method where all elements are stored within the hash table itself, using probing sequences to find alternative slots.

- CHAINING: Collision resolution method where each hash table slot contains a linked list of all elements hashing to that location.

## Important Formulas and Theorems

- Division method: h(k) = k mod m (where m is table size)
- Multiplication method: h(k) = floor(m × (k × A mod 1))
- Average case search time: O(1 + α) for simple hashing
- Worst case search time: O(n) for chaining when all keys collide
- Rehashing threshold: Typically when α exceeds 0.5 to 0.75

## Key Points

- A good hash function must be deterministic, efficient to compute, and distribute keys uniformly to minimize collisions.

- Linear probing suffers from PRIMARY CLUSTERING where large contiguous blocks of occupied slots form, degrading performance.

- Double hashing eliminates both primary and secondary clustering by using a secondary hash function for the probe sequence.

- Chaining outperforms open addressing when the load factor exceeds 0.5 or when the number of elements is unknown.

- The table size in open addressing should be a prime number not close to powers of 2 to ensure better distribution.

- Rehashing maintains O(1) average performance by rebuilding the table with a larger size when load factor becomes too high.

- Perfect hashing guarantees O(1) worst-case lookup but requires advance knowledge of all keys.

## Common Mistakes to Avoid

- Forgetting to recalculate hash values during rehashing—this invalidates all stored data if not done correctly.

- Using a non-prime table size in open addressing, which can lead to clustering patterns and poor distribution.

- Ignoring the load factor when analyzing performance—operations become O(n) as α approaches 1.

- Confusing linear and quadratic probing sequences—quadratic uses squares (1, 4, 9...) not multiples.

- Assuming O(1) guaranteed lookup time—O(1) is AVERAGE CASE only; worst case can be much worse.

## Revision Tips

- Practice inserting at least 5-6 keys using each collision resolution technique to build procedural memory.

- Create a comparison table of all hashing techniques listing probe sequence, clustering behavior, and best use cases.

- Memorize the relationship between load factor and time complexity: as α increases, performance degrades.

- Solve previous years' DU examination questions on hashing to understand the question patterns and answer formatting.

- Remember that chaining handles deletions gracefully while open addressing requires special handling (tombstones) to maintain probe sequences.