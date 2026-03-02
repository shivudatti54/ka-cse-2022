# Static Allocation vs Linked Allocation

## Overview

Static allocation uses arrays with fixed size determined at compile time, while linked allocation uses dynamic nodes created at runtime connected via pointers. Each approach has distinct advantages and trade-offs for different application scenarios.

## Key Points

- **Static Allocation**: Fixed-size array allocated at compile time, contiguous memory
- **Linked Allocation**: Dynamic nodes allocated at runtime using malloc, non-contiguous memory
- **Size Flexibility**: Static fixed and predetermined, linked grows/shrinks as needed
- **Memory Usage**: Static can waste space or overflow, linked uses exactly what's needed plus pointer overhead
- **Access Speed**: Static O(1) random access, linked O(n) sequential access
- **Insertion/Deletion**: Static O(n) requires shifting, linked O(1) at known position
- **Memory Requirements**: Static needs large contiguous block, linked uses scattered locations

## Important Concepts

- Static allocation simple and fast for known fixed-size requirements
- Linked allocation flexible for unpredictable or varying sizes
- Static cache-friendly due to contiguity, linked suffers cache misses
- Linked requires extra memory for pointers in each node
- Static suffers from fragmentation in middle operations
- Linked ideal for frequent insertions/deletions, static for frequent access

## Notes

- Create comparison table showing all differences for exam
- Understand when to choose each allocation type based on requirements
- Know memory layout differences: contiguous vs scattered
- Practice calculating memory overhead for both approaches
- Be able to justify choice of allocation method for given scenarios
