# Paging

## Concept

- Physical memory divided into fixed-size blocks called **frames**
- Logical memory divided into same-size blocks called **pages**
- Page size = Frame size (typically 4KB)
- Eliminates external fragmentation

## Address Translation

### Logical Address Structure

```
| Page Number (p) | Page Offset (d) |
 n-m bits m bits
```

For page size = 2^m bytes, offset has m bits.

### Translation Process

1. Extract page number (p) from logical address
2. Look up frame number (f) in page table
3. Physical address = f × page_size + d

### Formula

```
Physical Address = (Page Table[p]) × Page Size + Offset

Given: Logical address, Page size
Page Number = Logical Address / Page Size
Offset = Logical Address % Page Size
```

## Page Table

Each process has its own page table mapping pages to frames.

### Page Table Entry (PTE) Contents

| Field             | Purpose                 |
| ----------------- | ----------------------- |
| Frame number      | Physical frame location |
| Valid/Invalid bit | Is page in memory?      |
| Protection bits   | Read/Write/Execute      |
| Dirty bit         | Page modified?          |
| Reference bit     | Page accessed recently? |

## Page Table Implementation

### 1. Page Table Base Register (PTBR)

- Points to page table in memory
- Problem: Two memory accesses per reference (table + data)

### 2. Translation Lookaside Buffer (TLB)

- Fast cache for recent page table entries
- Hit: One memory access
- Miss: Two accesses + TLB update

### TLB Performance

```
Effective Access Time =
 hit_rate × (TLB_time + memory_time) +
 (1 - hit_rate) × (TLB_time + 2 × memory_time)
```

## Multi-Level Paging

### Problem

Large address space → huge page table

### Solution: Hierarchical paging

```
Two-Level:
| Outer Page | Inner Page | Offset |

Outer table points to inner tables
Inner tables point to frames
```

## Inverted Page Table

- One entry per frame (not per page)
- Entry contains: process ID + page number
- Search required (use hash for speed)
- Saves memory but slower lookup
