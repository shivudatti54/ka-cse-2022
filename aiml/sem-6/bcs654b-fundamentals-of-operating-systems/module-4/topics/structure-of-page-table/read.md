# Structure of Page Table


## Table of Contents

- [Structure of Page Table](#structure-of-page-table)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Page Table Basics](#page-table-basics)
  - [Key Metrics](#key-metrics)
- [Page Table Structures](#page-table-structures)
  - [1. Single-Level Page Table](#1-single-level-page-table)
  - [2. Hierarchical/Multi-Level Page Table](#2-hierarchicalmulti-level-page-table)
  - [3. Hashed Page Table](#3-hashed-page-table)
  - [4. Inverted Page Table (IPT)](#4-inverted-page-table-ipt)
  - [5. Multi-Level Page Tables for 64-bit](#5-multi-level-page-tables-for-64-bit)
- [Examples](#examples)
  - [Example 1: Calculating Page Table Size](#example-1-calculating-page-table-size)
  - [Example 2: Address Translation in Inverted Page Table](#example-2-address-translation-in-inverted-page-table)
- [Exam Tips](#exam-tips)

## Introduction

Page tables are critical data structures in modern operating systems that enable **virtual memory management**. They map **virtual addresses** used by processes to **physical addresses** in main memory. The structure of page tables determines:

- Memory efficiency (space overhead)
- Address translation speed
- Support for large address spaces
- Hardware compatibility

With increasing memory demands (64-bit systems handling 48-52 bit virtual addresses) and diverse workloads (from IoT devices to cloud servers), efficient page table structures have become essential for:

1. Minimizing memory overhead
2. Supporting sparse address spaces
3. Enabling fast address translation (via TLB)
4. Facilitating memory protection

The choice of page table structure directly impacts system performance, with tradeoffs between memory consumption and access speed. Modern OSes like Linux and Windows use sophisticated multi-level page table implementations.

## Key Concepts

### Page Table Basics

- **Page Table Entry (PTE)**: Contains frame number + control bits (valid, dirty, protection)
- **Virtual Address**: `virtual_page_number (VPN) + page_offset`
- **Physical Address**: `frame_number + page_offset`
- **Page Size**: Typically 4KB-1GB (4KB common in x86_64)

### Key Metrics

1. **Space Overhead**: Total memory consumed by page tables

```math
Space = (Number of Entries) × (Entry Size)
```

2. **Translation Cost**: Time for address resolution (affected by table depth)

## Page Table Structures

### 1. Single-Level Page Table

**Structure**: Linear array mapping all virtual pages
**Address Split**: `[VPN | offset]`
**Example**: 32-bit system with 4KB pages

- VPN bits = 32 - 12 = 20 bits → 1M entries
- Entry size = 4B → 4MB table per process

**Advantages**:

- Simple implementation
- Fast direct access

**Disadvantages**:

- Impractical for large address spaces (64-bit needs 2⁵² entries)
- Wastes space for sparse memory usage

**Use Case**: Embedded systems with small address spaces

---

### 2. Hierarchical/Multi-Level Page Table

**Structure**: Tree-like structure with multiple page table levels
**Address Split**: `[L1 Index | L2 Index | ... | Offset]`

**Example**: Two-level table (32-bit, 4KB pages, 10+10+12 split)

- Outer Table: 2¹⁰ entries (1024)
- Inner Tables: 1024 entries each
- Only allocate inner tables for used memory regions

**Calculation**:

```math
Total Size = (Outer Entries × 4B) + (Active Inner Tables × 1024 × 4B)
```

**Advantages**:

- Saves space for sparse address spaces
- Natural support for memory protection per region

**Disadvantages**:

- Multiple memory accesses for translation (TLB mitigates this)
- Fixed division of bits

**Real-World Use**: x86 32-bit (2-level), ARMv7 (2-level)

---

### 3. Hashed Page Table

**Structure**: Hash table mapping VPNs to frame numbers
**Components**:

- Hash function (e.g., VPN mod N)
- Linked lists for collision resolution

**Operation**:

1. Compute hash of VPN
2. Traverse chain to find matching VPN
3. Return frame number

**Advantages**:

- Efficient for very large sparse spaces
- Dynamic size adjustment

**Disadvantages**:

- Variable access time (depends on collisions)
- Complex management

**Use Case**: PowerPC architectures

---

### 4. Inverted Page Table (IPT)

**Structure**: Global table with one entry per physical frame
**Entry Format**: `[PID | VPN | ...]`

**Address Translation**:

1. Search IPT for (PID, VPN) pair
2. Use hash table to accelerate search

**Advantages**:

- Constant space overhead (proportional to physical memory)
- No per-process tables

**Disadvantages**:

- Slow translation (requires hash lookup)
- Complex shared memory handling

**Real-World Use**: IBM AS/400, some ARM implementations

---

### 5. Multi-Level Page Tables for 64-bit

**Challenge**: 64-bit address space requires impractical depth
**Solution**: Combine multiple techniques:

- **Clustered Page Tables**: Group entries
- **Sparse Mapping**: Only map used regions
- **Huge Pages**: 2MB/1GB pages reduce levels

**Example**: x86_64 4-level paging

```
Virtual Address: [PML4 | Directory Ptr | Directory | Table | Offset]
```

Each level has 512 entries (9 bits)

---

## Examples

### Example 1: Calculating Page Table Size

**Problem**:
64-bit system with 48-bit virtual address, 4KB pages, 4-level hierarchy. Each PTE is 8B.
Calculate maximum page table size.

**Solution**:

1. Offset bits = log₂(4096) = 12
2. VPN bits = 48 - 12 = 36
3. Split 36 bits into 4 levels: 9+9+9+9
4. Entries per level = 2⁹ = 512

Maximum size calculation:

- Level 4: 512 entries × 8B = 4KB
- Level 3: 512 × 4KB = 2MB
- Level 2: 512 × 2MB = 1GB
- Level 1: 512 × 1GB = 512GB

**Conclusion**: Theoretical maximum is impractical (512GB), but actual usage is sparse.

---

### Example 2: Address Translation in Inverted Page Table

**System**:

- Physical memory: 4GB (2³²) → 1M frames (4KB each)
- IPT with 1M entries
- Hash function: (PID ⊕ VPN) mod 1M

**Translation Process**:

1. Virtual address: PID=45, VPN=0x12345
2. Compute hash: (45 ⊕ 0x12345) mod 1M = 0xABC
3. Check entry 0xABC:

- If (PID,VPN) match → return frame
- Else follow collision chain

**Efficiency**: Average O(1) with good hash function

---

## Exam Tips

1. **Key Formulas**:

- Page Table Size = Entries × Entry Size
- VPN bits = Virtual Address Bits - Offset Bits
- Entries per Level = 2^(Bits Allocated to Level)

2. **Structure Comparisons**:
   | Structure | Space Overhead | Access Speed | 64-bit Support |
   |-----------------|----------------|--------------|----------------|
   | Single-Level | Very High | Fast | No |
   | Multi-Level | Moderate | Medium | Yes |
   | Inverted | Low | Slow | Yes |
   | Hashed | Variable | Variable | Yes |

3. **TLB Interaction**: All structures benefit from TLB caching recent translations

4. **64-bit Handling**:

- Multi-level tables become deeper (4-5 levels common)
- Combine with hashing/huge pages for efficiency

5. **Real Systems**:

- x86_64: 4-level paging (PML4)
- ARMv8: 3/4-level with configurable page sizes
- Linux: Uses 5-level for future-proofing (4-level actual)

6. **Design Tradeoffs**:

- More levels → smaller tables but more memory accesses
- Sparse allocation saves space but complicates management

7. **Protection Bits**:
   Remember page tables store RWX permissions, user/supervisor bits, and dirty/accessed flags
