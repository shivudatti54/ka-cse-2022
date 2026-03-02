# Memory Segmentation

## What is Segmentation?

**Segmentation** is a memory management technique where memory is divided into variable-sized segments based on the logical structure of a program.

## Segments in a Program

A program consists of logical segments:

- **Code segment**: Program instructions
- **Data segment**: Global variables
- **Stack segment**: Function calls, local variables
- **Heap segment**: Dynamically allocated memory

## User's View of Memory

```
┌─────────────┐
│    Stack    │ Segment 3
├─────────────┤
│    Heap     │ Segment 2
├─────────────┤
│    Data     │ Segment 1
├─────────────┤
│    Code     │ Segment 0
└─────────────┘
```

## Logical Address Structure

Address = (segment-number, offset)

Example: (2, 100) = segment 2, offset 100 bytes

## Segment Table

Each process has a segment table with entries:

- **Base**: Starting physical address
- **Limit**: Length of segment

| Segment | Base | Limit |
| ------- | ---- | ----- |
| 0       | 1400 | 1000  |
| 1       | 6300 | 400   |
| 2       | 4300 | 400   |
| 3       | 3200 | 1100  |

## Address Translation

```
Logical: (segment, offset)
         ↓
1. Check: offset < limit[segment]?
   NO → Trap (segmentation fault)
   YES → Continue
         ↓
2. Physical = base[segment] + offset
```

### Example

Logical address: (2, 53)

- Limit[2] = 400, 53 < 400 ✓
- Base[2] = 4300
- Physical = 4300 + 53 = 4353

## Hardware Support

```
┌─────────────────────────────────────────────┐
│  CPU generates: (segment_num, offset)       │
└──────────────────┬──────────────────────────┘
                   ↓
┌──────────────────┴──────────────────────────┐
│           Segment Table                      │
│  ┌─────────┬──────────┬───────────┐         │
│  │ Segment │  Base    │  Limit    │         │
│  ├─────────┼──────────┼───────────┤         │
│  │    s    │  base[s] │  limit[s] │         │
│  └─────────┴──────────┴───────────┘         │
└──────────────────┬──────────────────────────┘
                   ↓
          offset < limit?
          /            \
        YES            NO
         ↓              ↓
  base + offset    TRAP (fault)
         ↓
  Physical Address
```

## Protection and Sharing

### Protection Bits

Each segment can have:

- Read (R)
- Write (W)
- Execute (X)

Example:

- Code: R-X (read, execute)
- Data: RW- (read, write)
- Stack: RW- (read, write)

### Sharing

Code segments can be shared between processes:

- Same base address in multiple segment tables
- Only one copy in memory
- Each process has private data/stack segments

## Segmentation vs Paging

| Aspect        | Segmentation         | Paging            |
| ------------- | -------------------- | ----------------- |
| Unit size     | Variable             | Fixed (page size) |
| User view     | Logical divisions    | Transparent       |
| Fragmentation | External             | Internal          |
| Sharing       | Easy (whole segment) | Complex           |
| Protection    | Per segment          | Per page          |

## Fragmentation Problem

**External Fragmentation**: Free memory scattered in small pieces

Solutions:

1. **Compaction**: Move segments to consolidate free space
2. **Best Fit / First Fit**: Allocation algorithms
3. **Paged Segmentation**: Combine both techniques

## Paged Segmentation

Combine benefits of both:

- Segments are divided into pages
- No external fragmentation
- Preserves logical view

Address: (segment, page, offset)
