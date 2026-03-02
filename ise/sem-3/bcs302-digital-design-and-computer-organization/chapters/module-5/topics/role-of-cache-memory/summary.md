# Role of Cache Memory - Summary

## Key Definitions and Concepts

- CACHE MEMORY is a small, fast memory located close to the processor that stores frequently accessed data and instructions to reduce memory access time

- LOCALITY OF REFERENCE is the observation that programs tend to access the same memory locations repeatedly (temporal) and nearby locations (spatial)

- HIT RATE is the fraction of memory accesses found in cache; MISS RATE is the complement (1 - hit rate)

- HIT TIME is the time to access cache and find data; MISS PENALTY is the additional time when data is not in cache

- AVERAGE MEMORY ACCESS TIME (AMAT) = Hit Time + (Miss Rate × Miss Penalty)

## Important Formulas and Theorems

- Cache Line Index = (Block Address) mod (Number of Cache Lines)
- Tag bits = Address bits - Index bits - Offset bits
- AMAT (single level) = Hit Time + (Miss Rate × Miss Penalty)
- AMAT (two-level) = L1 Hit Time + L1 Miss Rate × (L2 Hit Time + L2 Miss Rate × L2 Miss Penalty)

## Key Points

- CACHE MAPPING: Direct mapping is simple but can cause conflicts; fully associative offers best flexibility but requires expensive hardware; set-associative balances both

- WRITE POLICIES: Write-through updates both cache and memory simultaneously; write-back updates memory only on eviction, reducing traffic but requiring dirty bit tracking

- REPLACEMENT ALGORITHMS: LRU evicts least recently used block; FIFO evicts oldest block; Random is simple but unpredictable

- MULTI-LEVEL CACHE: L1 is fastest and smallest, L2 is larger and slower, L3 (when present) is shared among cores

- MODERN CACHES typically use split L1 (separate instruction/data), set-associative organization (4-16 way), and write-back policies

## Common Mistakes to Ignore

- CONFUSING BLOCK NUMBER with Block Address - block address includes the tag
- FORGETTING that block offset uses log₂(Block Size) bits, not the block size itself
- IGNORING that write-through requires memory access on every write, increasing latency
- NOT accounting for both levels in multi-level cache AMAT calculations

## Revision Tips

- PRACTICE address decomposition problems: given address size, cache size, and block size, determine index, offset, and tag bits

- MEMORIZE the AMAT formula and practice numerical problems with different hit times and miss penalties

- UNDERSTAND the trade-offs: higher associativity improves hit rate but increases hardware complexity and access time

- KNOW the typical characteristics: L1 cache is split (Harvard), L2 is unified, access times decrease from L1 to L3