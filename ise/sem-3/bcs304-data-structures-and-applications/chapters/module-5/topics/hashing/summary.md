# Hashing - Summary

## Key Definitions and Concepts

- **Hashing**: A technique for mapping keys to array indices using a hash function for O(1) average-case data retrieval
- **Hash Table**: A data structure that implements an associative array, storing key-value pairs and enabling fast lookup
- **Hash Function**: A mathematical function that converts a key into a hash code (array index)
- **Collision**: Occurs when two different keys produce the same hash value
- **Load Factor (α)**: The ratio n/m where n is the number of elements and m is the table size; determines hash table efficiency

## Important Formulas and Theorems

- **Hash Function (Division Method)**: h(key) = key mod table_size
- **Linear Probing**: Probe sequence = (h(key) + i) mod m for i = 0, 1, 2, ...
- **Quadratic Probing**: Probe sequence = (h(key) + i²) mod m for i = 0, 1, 2, ...
- **Double Hashing**: Probe sequence = (h1(key) + i × h2(key)) mod m
- **Load Factor**: α = n/m, where n = elements stored, m = table size
- **Optimal Load Factor**: α < 0.5 for open addressing, α < 1.0 for separate chaining

## Key Points

- Hashing provides constant time O(1) average-case complexity for insertion, deletion, and search operations
- A good hash function must be deterministic, efficient, and uniformly distribute keys
- Open addressing stores collisions in alternative slots; separate chaining uses linked lists at each bucket
- Linear probing suffers from primary clustering; quadratic probing suffers from secondary clustering
- Double hashing eliminates both clustering problems using a secondary hash function
- Rehashing is required when load factor exceeds threshold (typically 0.7) to maintain performance
- Table size should preferably be a prime number not close to powers of 2 for the division method

## Common Mistakes to Avoid

- Choosing a table size that is a power of 2, which causes the hash function to only use lower-order bits
- Ignoring load factor leading to degraded performance and excessive collisions
- Confusing primary and secondary clustering when describing probing methods
- Forgetting that worst-case time complexity for all operations is O(n) when all keys collide

## Revision Tips

1. Practice inserting at least 10 keys into a hash table using different collision resolution methods
2. Draw the hash table after each insertion to visualize the distribution
3. Memorize the probe sequence formulas for each probing technique
4. Remember that rehashing doubles the table size and recomputes all hash values
5. Review comparison between hash tables and other structures like BST for exam preparation