# Contiguous Memory Allocation


## Table of Contents

- [Contiguous Memory Allocation](#contiguous-memory-allocation)
- [Introduction](#introduction)
- [Memory Partitioning](#memory-partitioning)
  - [Base and Limit Registers](#base-and-limit-registers)
- [Fixed Partitioning](#fixed-partitioning)
- [Variable (Dynamic) Partitioning](#variable-dynamic-partitioning)
- [Dynamic Storage Allocation Problem](#dynamic-storage-allocation-problem)
  - [First Fit](#first-fit)
  - [Best Fit](#best-fit)
  - [Worst Fit](#worst-fit)
  - [Comparison](#comparison)
- [Fragmentation](#fragmentation)
  - [Internal Fragmentation](#internal-fragmentation)
  - [External Fragmentation](#external-fragmentation)
  - [Solutions to External Fragmentation](#solutions-to-external-fragmentation)
- [Summary](#summary)
- [Exam Tips](#exam-tips)

## Introduction

**Contiguous memory allocation** is one of the earliest memory management techniques used by operating systems. In this scheme, each process is allocated a single **contiguous block** of memory — the process occupies a sequence of consecutive memory addresses. The OS must decide where in memory to place each process and how to manage the resulting free and occupied regions.

This topic corresponds to **Section 8.3** of Silberschatz (Operating System Concepts).

## Memory Partitioning

The main memory is usually divided into two partitions:

```
+---------------------------+ High Address
| |
| User Processes |
| (allocated from here) |
| |
+---------------------------+
| Operating System |
+---------------------------+ Low Address
```

The OS typically resides in low memory (with the interrupt vector), and user processes occupy the remaining memory. The OS must protect itself from user processes and protect user processes from each other using **base** and **limit** registers.

### Base and Limit Registers

| Register           | Purpose                                                          |
| :----------------- | :--------------------------------------------------------------- |
| **Base register**  | Holds the smallest legal physical memory address for the process |
| **Limit register** | Specifies the size of the range                                  |

A process can only access memory addresses from `base` to `base + limit`. Any access outside this range causes a trap to the OS (memory protection violation).

```
Memory Protection:

 +------------------+
 | Process P1 | base = 300040, limit = 120900
 | [300040...420939]|
 +------------------+

 CPU generates address A:
 If A < base OR A >= base + limit → TRAP (illegal access)
 Otherwise → access allowed
```

## Fixed Partitioning

The simplest approach: divide memory into a **fixed number of partitions** of predetermined sizes at system startup.

```
Fixed Partitions:
+------------------+
| OS |
+------------------+
| Partition 1 | 100 KB
| (P1) |
+------------------+
| Partition 2 | 200 KB
| (P2) |
+------------------+
| Partition 3 | 400 KB
| (empty) |
+------------------+
| Partition 4 | 300 KB
| (P3) |
+------------------+
```

| Advantage           | Disadvantage                                                                                 |
| :------------------ | :------------------------------------------------------------------------------------------- |
| Simple to implement | **Internal fragmentation** — a process smaller than the partition wastes the remaining space |
| Low overhead        | Number and size of partitions fixed at boot time                                             |
|                     | Limits degree of multiprogramming                                                            |

**Internal fragmentation** occurs when a process is allocated a partition larger than it needs. The unused space within the partition is wasted.

```
Internal Fragmentation Example:
 Partition size: 200 KB
 Process size: 150 KB
 Wasted space: 50 KB (internal fragmentation)
```

## Variable (Dynamic) Partitioning

Partitions are created **dynamically** to fit each process exactly. When a process arrives, it is allocated exactly the amount of memory it needs.

```
Variable Partitions (over time):

Initially:
+------------------+
| OS |
+------------------+
| |
| Free (1000 KB) |
| |
+------------------+

After loading P1 (200KB), P2 (400KB), P3 (300KB):
+------------------+
| OS |
+------------------+
| P1 (200 KB) |
+------------------+
| P2 (400 KB) |
+------------------+
| P3 (300 KB) |
+------------------+
| Free (100 KB) |
+------------------+

After P2 terminates:
+------------------+
| OS |
+------------------+
| P1 (200 KB) |
+------------------+
| Hole (400 KB) | ← External fragmentation
+------------------+
| P3 (300 KB) |
+------------------+
| Free (100 KB) |
+------------------+
```

**External fragmentation** occurs when total free memory is sufficient for a request, but it is not contiguous — it is scattered as small "holes" between allocated partitions.

## Dynamic Storage Allocation Problem

When a new process needs memory, the OS must choose which free hole to allocate. This is the **dynamic storage allocation problem**. Three common strategies:

### First Fit

Allocate the **first hole** that is big enough. Search starts from the beginning (or from where the last search ended).

```
Holes: [100KB] [500KB] [200KB] [300KB]
Request: 210KB
→ Allocate from the 500KB hole (first one big enough)
→ Remaining: [100KB] [290KB] [200KB] [300KB]
```

### Best Fit

Allocate the **smallest hole** that is big enough. Must search the entire list (unless sorted by size).

```
Holes: [100KB] [500KB] [200KB] [300KB]
Request: 210KB
→ Allocate from the 300KB hole (smallest that fits)
→ Remaining: [100KB] [500KB] [200KB] [90KB]
```

### Worst Fit

Allocate the **largest hole**. Must search the entire list.

```
Holes: [100KB] [500KB] [200KB] [300KB]
Request: 210KB
→ Allocate from the 500KB hole (largest)
→ Remaining: [100KB] [290KB] [200KB] [300KB]
```

### Comparison

| Strategy      | Speed                          | Fragmentation                                                   | Memory Utilization |
| :------------ | :----------------------------- | :-------------------------------------------------------------- | :----------------- |
| **First Fit** | Fastest (stops at first match) | Moderate                                                        | Good               |
| **Best Fit**  | Slow (searches entire list)    | Produces smallest leftover holes (many tiny unusable fragments) | Better             |
| **Worst Fit** | Slow (searches entire list)    | Produces largest leftover holes                                 | Worst              |

**Result from simulations:** First Fit and Best Fit are generally better than Worst Fit in terms of both speed and storage utilization. First Fit is typically preferred because it is fastest.

## Fragmentation

### Internal Fragmentation

Memory allocated to a process but **not used** by the process. Occurs in fixed partitioning.

### External Fragmentation

Total free memory is enough, but it is **not contiguous**. Occurs in variable partitioning.

**50-percent rule:** Statistical analysis shows that for First Fit, given N allocated blocks, approximately **0.5N blocks** will be lost to fragmentation. That means **one-third** of memory may be unusable.

### Solutions to External Fragmentation

**1. Compaction:** Move all processes to one end of memory, combining all free space into one large hole.

```
Before compaction: After compaction:
+--------+ +--------+
| OS | | OS |
+--------+ +--------+
| P1 | | P1 |
+--------+ +--------+
| hole | | P3 |
+--------+ +--------+
| P3 | | |
+--------+ | Free |
| hole | | (big) |
+--------+ | |
 +--------+
```

**Limitation:** Compaction is expensive — it requires moving large amounts of data. It is only possible if relocation is dynamic (done at execution time using a relocation register).

**2. Non-contiguous allocation:** Use **paging** or **segmentation** instead, which allow a process's memory to be scattered across non-contiguous frames. These techniques eliminate external fragmentation entirely.

## Summary

| Concept                | Key Point                                                     |
| :--------------------- | :------------------------------------------------------------ |
| Contiguous allocation  | Each process gets a single block of consecutive addresses     |
| Base/limit registers   | Hardware protection — process can only access its own range   |
| Fixed partitioning     | Predetermined partition sizes; causes internal fragmentation  |
| Variable partitioning  | Partitions fit process exactly; causes external fragmentation |
| First fit              | First hole big enough; fastest                                |
| Best fit               | Smallest hole big enough; leaves tiny fragments               |
| Worst fit              | Largest hole; worst utilization                               |
| Internal fragmentation | Unused space within an allocated partition                    |
| External fragmentation | Free space scattered in small non-contiguous holes            |
| Compaction             | Move processes to combine free holes; expensive               |

## Exam Tips

1. **First fit vs best fit vs worst fit** — This is a very common exam question (5-10 marks). Know all three, be able to trace through an example, and state which is best (first fit — fastest and comparable utilization).
2. **Internal vs external fragmentation** — Know the difference and which partitioning scheme causes which. Fixed → internal, Variable → external.
3. **50-percent rule** — Mention this when discussing external fragmentation with first fit.
4. **Compaction** — Know what it is, why it helps, and its limitation (only works with dynamic relocation).
5. **Draw memory diagrams** — Show partitions, holes, and how allocation strategies choose different holes. frequently asks diagram-based questions.
6. **Base and limit registers** — Be able to explain memory protection using these registers. Draw the hardware address-checking mechanism.
7. **Link to paging** — When discussing the problems of contiguous allocation, mention that paging (covered next) solves external fragmentation by allowing non-contiguous allocation.
