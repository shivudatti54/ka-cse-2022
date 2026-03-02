# Segmentation


## Table of Contents

- [Segmentation](#segmentation)
- [Introduction](#introduction)
- [User's View of Memory](#users-view-of-memory)
- [Segmentation Architecture](#segmentation-architecture)
  - [Segment Table](#segment-table)
  - [Address Translation](#address-translation)
  - [Example](#example)
- [Segmentation Hardware](#segmentation-hardware)
- [Protection and Sharing with Segmentation](#protection-and-sharing-with-segmentation)
  - [Protection](#protection)
  - [Sharing](#sharing)
- [Segmentation vs Paging](#segmentation-vs-paging)
- [Segmentation with Paging](#segmentation-with-paging)
- [Summary](#summary)
- [Exam Tips](#exam-tips)

## Introduction

**Segmentation** is a memory management scheme that supports the user's view of memory. A program is a collection of logical units — functions, arrays, stacks, data tables, objects — and segmentation allows each of these units to be treated as a separate segment in memory. Unlike paging, which divides memory into fixed-size pages regardless of program structure, segmentation divides memory according to the **logical structure** of the program.

This topic corresponds to **Section 8.4** of Silberschatz (Operating System Concepts).

## User's View of Memory

A programmer thinks of a program as a collection of logical segments, not as a linear sequence of bytes:

```
User's View of a Program:

+-------------+
| Main() | ← Code segment
+-------------+
| Function | ← Another code segment
+-------------+
| Stack | ← Stack segment
+-------------+
| Symbol |
| Table | ← Data segment
+-------------+
| Array | ← Data segment
+-------------+
| Heap | ← Heap segment
+-------------+
```

Each segment has a **name** (or number) and a **length**. Addresses within a segment specify an offset from the beginning of that segment. A logical address in a segmented system is a **two-dimensional** address:

```
Logical Address = <segment-number, offset>
```

## Segmentation Architecture

### Segment Table

The OS maintains a **segment table** for each process. Each entry in the segment table has two fields:

| Field     | Description                                        |
| :-------- | :------------------------------------------------- |
| **Base**  | Starting physical address of the segment in memory |
| **Limit** | Length of the segment                              |

```
Segment Table for Process P:

| Segment # | Base | Limit |
|-----------|-------|-------|
| 0 | 1400 | 1000 |
| 1 | 6300 | 400 |
| 2 | 4300 | 400 |
| 3 | 3200 | 1100 |
| 4 | 4700 | 1000 |
```

### Address Translation

To translate a logical address `<s, d>` (segment s, offset d):

```
Logical Address: <segment-number s, offset d>

1. Use s as index into the segment table
2. Get base and limit from segment table entry
3. If d >= limit → TRAP (segment overflow — illegal access)
4. Physical address = base + d

 Logical Address
 +----+--------+
 | s | d |
 +----+--------+
 | |
 v |
 +------------+ |
 |Segment | |
 |Table | |
 |------------| |
 | base|limit | |
 +-----+------+ |
 | | |
 | v |
 | d < limit?|
 | Yes No → TRAP
 | |
 v v
 base + d = Physical Address
```

### Example

Segment table:

| Segment | Base | Limit |
| :------ | :--- | :---- |
| 0       | 219  | 600   |
| 1       | 2300 | 14    |
| 2       | 90   | 100   |
| 3       | 1327 | 580   |
| 4       | 1952 | 96    |

Translate logical address `<2, 53>`:

- Segment 2: base = 90, limit = 100
- Offset 53 < limit 100? Yes (valid)
- Physical address = 90 + 53 = **143**

Translate logical address `<3, 852>`:

- Segment 3: base = 1327, limit = 580
- Offset 852 < limit 580? **No** → TRAP (segmentation fault)

## Segmentation Hardware

```
+--------+--------+ +-------------+
| Seg # | Offset | | Physical |
| s | d | | Memory |
+--------+--------+ | |
 | | | |
 | | +--------+------+ | +-------+ |
 | | | base | limit| | | | |
 | | +--------+------+ | | Seg 0 | |
 +-------->|---->| Segment Table | | | | |
 | +--------+------+ | +-------+ |
 | | | | |
 | | d<limit? | +-------+ |
 | | / \ | | | |
 | | yes no | | Seg 2 | |
 | | | TRAP | | | |
 | v v | +-------+ |
 +---> base + d --------->| target |
 +-------------+
```

## Protection and Sharing with Segmentation

### Protection

Since segments correspond to logical program units, it is natural to associate **protection bits** with each segment:

| Protection Bit | Meaning                          |
| :------------- | :------------------------------- |
| Read           | Segment can be read              |
| Write          | Segment can be modified          |
| Execute        | Segment contains executable code |

For example:

- A **code segment** can be marked as read-only and execute-only
- A **data segment** can be marked as read-write
- A **stack segment** can be marked as read-write

This is more natural than page-level protection because segments correspond to meaningful program units.

### Sharing

Segments can be shared between processes easily because they represent logical units. For example, a shared library can be a single segment that appears in the segment tables of multiple processes:

```
Process P1 Segment Table: Process P2 Segment Table:
| Seg | Base | Limit | | Seg | Base | Limit |
|-----|------|-------| |-----|------|-------|
| 0 | 1000 | 500 | ←--- Shared code segment
| 1 | 2000 | 200 | | 0 | 1000 | 500 | ←--- Same segment!
 | 1 | 3000 | 300 |
```

Both processes point to the same physical memory for the shared code segment. Each process has its own private data segment.

## Segmentation vs Paging

| Aspect                     | Segmentation                             | Paging                          |
| :------------------------- | :--------------------------------------- | :------------------------------ |
| **Division**               | Logical units (variable size)            | Fixed-size pages                |
| **User visible?**          | Yes (programmer aware)                   | No (transparent to programmer)  |
| **Address**                | 2D: `<segment, offset>`                  | 1D: page number + offset        |
| **Internal fragmentation** | No (segments fit exactly)                | Yes (last page may not be full) |
| **External fragmentation** | Yes (variable-size segments leave holes) | No (all frames are same size)   |
| **Protection**             | Natural (per logical unit)               | Less natural (per fixed page)   |
| **Sharing**                | Easy (share logical segments)            | More complex                    |
| **Table size**             | Depends on number of segments            | Can be very large (many pages)  |

## Segmentation with Paging

Some systems combine segmentation and paging to get the benefits of both. **Intel x86 architecture** historically used segmentation with paging:

1. Logical address → segmentation hardware → linear address
2. Linear address → paging hardware → physical address

```
Logical Address → [Segmentation Unit] → Linear Address → [Paging Unit] → Physical Address
```

This combination:

- Eliminates external fragmentation (paging handles physical allocation)
- Preserves the logical view of segments (protection and sharing)
- Used in Intel Pentium (IA-32) architecture

## Summary

| Concept                | Key Point                                                              |
| :--------------------- | :--------------------------------------------------------------------- |
| Segmentation           | Divides memory by logical program structure (functions, arrays, stack) |
| Logical address        | Two-dimensional: `<segment-number, offset>`                            |
| Segment table          | Maps segment number to (base, limit)                                   |
| Address translation    | Check offset < limit, then physical = base + offset                    |
| Protection             | Natural per-segment: read, write, execute bits                         |
| Sharing                | Easy — point multiple segment table entries to same physical segment   |
| External fragmentation | Yes (segments are variable size)                                       |
| Internal fragmentation | No                                                                     |

## Exam Tips

1. **Address translation example** — very frequently asks: "Given a segment table, translate logical address `<s, d>` to physical address." Practice this with numbers.
2. **Segmentation vs Paging table** — This is a classic 10-mark comparison question. Use the comparison table above.
3. **Draw the hardware diagram** — Be able to draw the segmentation hardware showing segment table lookup, limit check, and base+offset addition.
4. **Protection and sharing** — Explain why segmentation supports protection and sharing more naturally than paging (segments = logical units).
5. **Segmentation fault** — Explain what happens when offset >= limit (trap to OS). This is where the term "segfault" comes from.
6. **Segmentation with paging** — Know that Intel x86 combines both. Mention this when comparing segmentation and paging.
