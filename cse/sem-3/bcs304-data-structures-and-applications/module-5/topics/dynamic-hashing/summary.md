# Dynamic Hashing

## Overview

Dynamic hashing techniques allow the hash table to grow and shrink gracefully without rehashing all existing records at once, addressing the limitations of static hashing. Two primary techniques are extendible hashing and linear hashing.

## Key Points

- Extendible hashing uses a directory of pointers to buckets, doubling in size when needed.
- Linear hashing uses a family of hash functions and a split pointer to split buckets in a round-robin fashion.
- Both techniques avoid full rehashing and support incremental growth.
- Extendible hashing offers fast lookups but may have high directory overhead.
- Linear hashing has lower space overhead but may require following overflow chains.

## Important Definitions

- **Directory**: An array of pointers to buckets in extendible hashing.
- **Global Depth (d)**: Number of bits of the hash value used to index into the directory.
- **Local Depth (d')**: Number of bits of the hash value common to all keys in a bucket.
- **Split Pointer (p)**: Points to the next bucket to be split in linear hashing.
- **Level (l)**: Current round of splitting in linear hashing.

## Key Formulas / Syntax

- Extendible Hashing: `h(key) = key mod (2^d)`
- Linear Hashing: `h_l(key) = key mod (2^l * N)`, `h_{l+1}(key) = key mod (2^(l+1) * N)`

## Comparisons

| Feature           | Extendible Hashing        | Linear Hashing                    |
| ----------------- | ------------------------- | --------------------------------- |
| Directory         | Uses a directory          | No directory needed               |
| Splitting         | Splits overflowing bucket | Splits bucket at split pointer    |
| Space Overhead    | High directory overhead   | No directory overhead             |
| Overflow Handling | No overflow chains        | Uses overflow chains              |
| Access Time       | At most 2 disk accesses   | May need to follow overflow chain |

## Exam Tips

- Practice directory doubling in extendible hashing.
- Understand the difference between global depth and local depth.
- Know how the split pointer works in linear hashing.
- Be ready to trace through insertions step by step.
- Memorize the comparison table between extendible and linear hashing.
- Remember the hash functions for linear hashing.
- Understand space complexity differences between the two techniques.
- Recognize practical applications in database management systems.
