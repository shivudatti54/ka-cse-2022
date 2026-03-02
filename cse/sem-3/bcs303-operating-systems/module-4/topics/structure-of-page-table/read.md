# Structure of the Page Table

## Introduction

In a basic paging system, the page table is a simple array mapping each page number to a frame number. However, for modern systems with large logical address spaces (32-bit or 64-bit), a single flat page table becomes impractically large. For example, a 32-bit address space with 4 KB pages requires 2^20 = **1,048,576 entries** in the page table — and each process has its own page table.

To handle this, operating systems use structured page table techniques that reduce memory overhead while maintaining efficient address translation. The three main approaches are: **hierarchical page tables**, **hashed page tables**, and **inverted page tables**.

This topic corresponds to **Section 8.5** of Silberschatz (Operating System Concepts).

## The Problem with Flat Page Tables

Consider a 32-bit logical address space with 4 KB (2^12) page size:

```
Page table size = 2^(32-12) entries = 2^20 entries = 1,048,576 entries
Each entry ≈ 4 bytes
Total = 4 MB per process

If 100 processes are running: 100 × 4 MB = 400 MB just for page tables!
```

For a 64-bit address space, the problem is far worse — a flat page table would require **petabytes** of memory. Clearly, we need better structures.

## 1. Hierarchical Page Tables

### Two-Level Page Table

The most common approach is to **page the page table itself** — divide the page table into smaller pieces and only keep in memory the pieces that are actually needed.

For a 32-bit address space with 4 KB pages:

```
Logical Address (32 bits):
+----------+----------+----------+
| p1 (10) | p2 (10) | d (12) |
+----------+----------+----------+
 outer inner page
 page # page # offset

p1 = index into the outer page table
p2 = index into the inner page table (one of many)
d = offset within the page
```

**Address translation:**

```
 Logical Address
 +----+----+------+
 | p1 | p2 | d |
 +----+----+------+
 | | |
 v | |
 +------------+| |
 | Outer Page || |
 | Table || |
 |------------|v |
 | pointer |----> +------------+
 +------------+ | Inner Page |
 | Table |
 |------------|
 | frame # |----> Physical Memory
 +------------+ |
 v
 frame # × page_size + d
 = Physical Address
```

**How it saves memory:** Most of the logical address space is unused for a typical process. The outer page table has entries, but inner page tables are only created for address ranges that the process actually uses. Unused regions have NULL pointers in the outer table.

### Three-Level Page Table

For larger address spaces, we can add more levels. For example, a 64-bit system might use three or four levels:

```
64-bit Logical Address:
+----------+----------+----------+----------+
| p1 | p2 | p3 | d |
+----------+----------+----------+----------+
 Level 1 Level 2 Level 3 offset

Each level indexes into a smaller page table, with only used
tables actually allocated in memory.
```

**Trade-off:** More levels mean more memory accesses per translation (one per level + one for the actual data), increasing access time. But they dramatically reduce the total page table memory.

## 2. Hashed Page Tables

For address spaces larger than 32 bits, **hashed page tables** are often used. The page number is hashed to index into a hash table. Each entry in the hash table contains a **linked list** of elements that hash to the same location.

### Structure

Each element in the linked list contains three fields:

| Field                   | Description                                               |
| :---------------------- | :-------------------------------------------------------- |
| **Virtual page number** | The page number being mapped                              |
| **Frame number**        | The corresponding physical frame                          |
| **Next pointer**        | Pointer to the next element in the chain (for collisions) |

```
Logical Address:
+----------+--------+
| page # p | offset |
+----------+--------+
 |
 v
 hash(p) → index into hash table

Hash Table:
+---+---+---+---+---+---+
| 0 | 1 | 2 | 3 | 4 |...|
+---+---+---+---+---+---+
 |
 v
 +----+-------+------+
 | vp | frame | next |---> +----+-------+------+
 +----+-------+------+ | vp | frame | next |---> NULL
 +----+-------+------+

Search the chain for matching virtual page number.
If found → use the frame number.
```

### Clustered Page Tables

A variation of hashed page tables where each entry in the hash table refers to several pages (a cluster) rather than a single page. This is useful for **sparse** address spaces where memory references are non-contiguous but clustered.

## 3. Inverted Page Table

An **inverted page table** has one entry for each **physical frame** in the system, rather than one entry per logical page. This dramatically reduces the page table size.

### Structure

| Entry  | Contents                             |
| :----- | :----------------------------------- |
| Index  | Frame number (position in the table) |
| Fields | `<process-id, page-number>`          |

```
Inverted Page Table (one for entire system):

Frame # | PID | Page #
--------|------|-------
 0 | P1 | 3
 1 | P2 | 0
 2 | P1 | 7
 3 | P3 | 2
 4 | P2 | 5
 ... | ... | ...
```

### Address Translation

```
Logical Address from Process Pi:
+-----+----------+--------+
| pid | page # p | offset |
+-----+----------+--------+
 |
 v
 Search inverted page table for entry matching (pid, p)
 |
 v
 Found at index i → Frame number = i
 Physical address = i × page_size + offset
```

### Advantages and Disadvantages

| Advantage                                                                         | Disadvantage                                                                |
| :-------------------------------------------------------------------------------- | :-------------------------------------------------------------------------- |
| Only **one** page table for the entire system                                     | Search time is slow (must scan table for each address translation)          |
| Table size = number of physical frames (fixed, regardless of number of processes) | Shared memory is difficult (each frame maps to only one `<pid, page>` pair) |
| Much smaller than per-process page tables for large address spaces                |                                                                             |

### Improving Search Time

To speed up the linear search, an inverted page table is typically combined with a **hash table**:

```
Logical address (pid, page) → hash → index into hash table → chain →
find matching (pid, page) → frame number = table index
```

This reduces average search time from O(n) to O(1) with a good hash function.

## Comparison of Page Table Structures

| Structure                      | Table Size                      | Lookup Speed                        | Best For                                                       |
| :----------------------------- | :------------------------------ | :---------------------------------- | :------------------------------------------------------------- |
| **Flat (single-level)**        | Large (one entry per page)      | Fast (direct index)                 | Small address spaces                                           |
| **Hierarchical (multi-level)** | Only allocated for used regions | Moderate (multiple memory accesses) | 32-bit systems                                                 |
| **Hashed**                     | Proportional to allocated pages | Fast with good hash                 | Address spaces > 32 bits                                       |
| **Inverted**                   | One entry per frame (smallest)  | Slower (search required)            | Very large address spaces (64-bit), memory-constrained systems |

## TLB and Page Table Interaction

Regardless of the page table structure, the **Translation Lookaside Buffer (TLB)** — a fast hardware cache — is used to speed up address translation:

```
CPU generates logical address
 |
 v
 Check TLB
 |
 HIT → Get frame number directly (fast, ~1 ns)
 |
 MISS → Walk the page table structure (slow, multiple memory accesses)
 → Put result in TLB for next time
```

The TLB makes the page table structure largely irrelevant for frequently accessed pages, since TLB hits bypass the page table entirely.

## Summary

| Concept      | Key Point                                                                    |
| :----------- | :--------------------------------------------------------------------------- |
| Problem      | Flat page tables too large for modern address spaces                         |
| Hierarchical | Page the page table; only allocate used portions                             |
| Two-level    | 32-bit: split page number into p1 (outer) and p2 (inner)                     |
| Hashed       | Hash the page number; linked list handles collisions                         |
| Inverted     | One entry per physical frame; smallest table but slow search                 |
| TLB          | Hardware cache that makes page table structure less critical for performance |

## Exam Tips

1. **Two-level page table address breakdown** — frequently asks: "Given a 32-bit address with 4KB pages, show how the address is split into p1, p2, and d." Practice: 12 bits for offset, 10+10 for the two page table levels.
2. **Draw the two-level translation diagram** — Show outer table → inner table → frame → physical address. This is a common 10-mark question.
3. **Inverted page table** — Know the structure (pid + page number per frame), why it's small, and why search is slow. Mention the hash table optimization.
4. **Compare all three structures** — Use a comparison table. Know when each is appropriate.
5. **Calculate page table sizes** — Practice: "How large is the page table for a 32-bit address space with 4KB pages?" Then show how two-level reduces this.
6. **TLB** — Always mention TLB when discussing page table performance. The effective memory access time formula (TLB hit ratio × 1 access + miss ratio × multiple accesses) is frequently asked.
