# Coprocessor 15 and Caches - Summary

## Key Definitions and Concepts

- **Coprocessor 15 (CP15)**: The system control coprocessor in ARM architecture that provides control over MMU, cache controllers, and system configuration through dedicated registers

- **Cache**: Fast memory between CPU and main memory that stores frequently accessed data and instructions to reduce memory access latency

- **Cache Line**: The fundamental unit of cache memory transfer, typically 32 or 64 bytes

- **Associativity (n-way)**: Number of possible locations where a memory address can be stored in cache (4-way, 8-way, etc.)

- **Write-Through Cache**: Updates both cache and main memory on every write operation

- **Write-Back Cache**: Updates only cache initially, writes to main memory when line is evicted

- **Clean Operation**: Writes dirty cache lines back to main memory

- **Invalidate Operation**: Removes cache lines without writing back

## Important Formulas and Theorems

- **Cache Size = Number of Sets × Associativity × Line Length**

- **MCR/MRC Instructions**: Used to access CP15 registers
  - Format: MCR p15, 0, Rd, CRn, CRm, opcode2
- **Cache Type Register (CTR) Decoding**:
  - Bits 27-24: Log2(line length) - 2 for data cache
  - Bits 3-0: Minimum cache line number

## Key Points

- CP15 provides system control functions including MMU control, cache management, and access permission configuration

- L1 cache in ARM is typically Harvard-type (separate I-cache and D-cache)

- Memory attributes (TEX, C, B bits) in MMU translation tables control cache behavior

- DSB (Data Synchronization Barrier) ensures completion of memory operations before proceeding

- ISB (Instruction Synchronization Barrier) flushes processor pipeline after cache maintenance

- Cache coherency must be maintained for DMA operations using clean/invalidate operations

- Strongly ordered memory is never cached, device memory may be buffered but not cached

## Common Mistakes to Avoid

- Forgetting to include DSB/ISB after cache maintenance operations, leading to stale data issues

- Confusing clean and invalidate operations - clean writes dirty data, invalidate removes without writing

- Not accounting for cache line alignment when performing address-based cache operations

- Using write-back cache for DMA buffers without proper clean operations

- Assuming cache is enabled by default - caches must be explicitly enabled through CP15

## Revision Tips

- Practice writing MCR/MRC instruction sequences for common cache operations

- Create a table mapping TEX, C, B bit combinations to memory types and caching behavior

- Remember the sequence: DSB before ISB when performing cache maintenance

- Focus on understanding when to use clean-only vs invalidate-only vs clean-and-invalidate operations

- Review previous year questions on CP15 registers and cache configuration
