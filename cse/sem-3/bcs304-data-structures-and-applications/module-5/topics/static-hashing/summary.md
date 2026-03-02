# Static Hashing

## Overview

Static hashing is a hashing technique where the hash table size is fixed at the time of creation and does not change during the lifetime of the table. It maps keys to table indices using a hash function, enabling O(1) average-case performance for insertion, search, and deletion. However, performance degrades as the load factor increases.

## Key Points

- Hash table size is fixed and determined at creation time.
- Hash function maps keys to indices in the range [0, m-1], where m is the table size.
- Collision resolution methods include separate chaining and open addressing.
- Load factor (alpha = n/m) affects performance, and linear probing degrades beyond alpha = 0.75.
- Lazy deletion is necessary in open addressing to ensure correct search results.
- Separate chaining uses linked lists at each bucket, while open addressing stores all elements in the table.

## Important Definitions

- **Hash function**: Maps a key to an integer index in the range [0, m-1].
- **Collision**: Occurs when two keys hash to the same index.
- **Load factor (alpha)**: Ratio of the number of elements stored to the table size (n/m).
- **Lazy deletion**: Marks a deleted slot as DELETED instead of EMPTY to ensure correct search results.

## Key Formulas / Syntax

- Division method: `h(key) = key % m`
- Mid-square method: `h(key) = (key^2) % m`
- Folding method: `h(key) = (sum of parts) % m`
- Double hashing: `h(key, i) = (h1(key) + i * h2(key)) % m`

## Comparisons

| Feature           | Separate Chaining    | Linear Probing     | Quadratic Probing    | Double Hashing |
| ----------------- | -------------------- | ------------------ | -------------------- | -------------- |
| Storage           | Array + Linked Lists | Array only         | Array only           | Array only     |
| Load factor limit | Can exceed 1.0       | Must be < 1.0      | Must be < 1.0        | Must be < 1.0  |
| Clustering        | None                 | Primary clustering | Secondary clustering | No clustering  |

## Exam Tips

- Know the division method formula and why m should be prime.
- Be able to trace insertions step by step for linear probing, quadratic probing, and double hashing.
- Understand the difference between separate chaining and open addressing.
- Memorize the load factor formula and know how it affects performance.
- Remember that lazy deletion is necessary in open addressing.
- Know why double hashing avoids primary and secondary clustering.
- Practice worked examples for each collision resolution technique.
