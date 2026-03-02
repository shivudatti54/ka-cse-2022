# Hashing and Hash Tables

## Introduction
Hashing is a fundamental concept in computer science that enables efficient data retrieval through key-value pair storage. A hash table is a data structure that implements associative array abstract data type using hash functions to map keys to their corresponding values. This provides average-case O(1) time complexity for search, insert, and delete operations, making it indispensable in modern computing.

The importance of hashing extends across various domains: database indexing, compiler symbol tables, caching mechanisms (like Redis), and even cryptographic systems. With the exponential growth of data in web applications, efficient hashing techniques have become critical for handling large-scale datasets while maintaining performance.

Modern applications require sophisticated collision resolution strategies and dynamic resizing mechanisms. The choice of hash function directly impacts performance, with poor functions leading to clustering and degraded efficiency. Understanding these trade-offs is essential for designing robust systems in distributed databases (e.g., consistent hashing in DynamoDB) and real-time applications.

## Key Concepts
1. **Hash Functions**: 
   - Deterministic functions mapping arbitrary-sized keys to fixed-size indices
   - Properties: Uniform distribution, avalanche effect, minimal collisions
   - Types: Division method, multiplication method, cryptographic hashes (SHA-256)

2. **Collision Resolution**:
   - **Separate Chaining**: Uses linked lists at each bucket
   - **Open Addressing**:
     - Linear probing: h(k,i) = (h'(k) + i) mod m
     - Quadratic probing: h(k,i) = (h'(k) + c1*i + c2*i²) mod m
     - Double hashing: h(k,i) = (h1(k) + i*h2(k)) mod m

3. **Load Factor (α)**:
   - α = n/m (number of entries / table size)
   - Critical for determining rehashing thresholds (typically α ≥ 0.7 triggers resizing)

4. **Dynamic Resizing**:
   - Geometric expansion (usually double table size)
   - Incremental rehashing for real-time systems

5. **Universal Hashing**:
   - Randomized algorithm selecting hash function from a family
   - Guarantees low collision probability for any data distribution

## Examples
**Example 1: Insertion with Linear Probing**
```
Table size: 7, h(k) = k mod 7
Insert 18, 14, 21, 28, 35, 42

Step 1: 18 → 4 (no collision)
Step 2: 14 → 0
Step 3: 21 → 0 (collision) → probe 1
Step 4: 28 → 0 → probe 1 (occupied) → probe 2
Final positions: [14,21,28,35,42,_,18]
```

**Example 2: Double Hashing**
```
h1(k) = k mod 7, h2(k) = 5 - (k mod 5)
Insert 30:
h1(30)=2, h2(30)=5-0=5
Probes: 2 → (2+5) mod 7 = 0 → (2+10) mod 7 = 5
```

**Example 3: Rehashing**
```
Initial table size: 5, threshold α=0.6
Insert 5,10,15 (α=0.6 → resize to 11)
New hash function: k mod 11
Reinsert 5→5, 10→10, 15→4
```

## Exam Tips
1. Always mention time complexity trade-offs: O(1) average vs O(n) worst-case
2. For collision resolution questions, compare chaining (extra memory) vs open addressing (cache friendly)
3. When asked about load factor, discuss its impact on performance and rehashing strategies
4. In numerical problems, clearly show probing sequences step-by-step
5. Remember that cryptographic hash functions are deterministic but not suitable for hash tables
6. Universal hashing questions often involve probability calculations (1/m collision chance)
7. Real-world application questions expect specific examples like DNS lookup or password storage

Length: 2500 words, MCA (Master of Computer Applications) PG level