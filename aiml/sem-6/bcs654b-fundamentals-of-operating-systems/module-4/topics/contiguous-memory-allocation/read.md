# Contiguous Memory Allocation


## Table of Contents

- [Contiguous Memory Allocation](#contiguous-memory-allocation)
- [Introduction](#introduction)
- [System Model for Memory Allocation](#system-model-for-memory-allocation)
- [Fixed Partitioning](#fixed-partitioning)
  - [Concept](#concept)
  - [Example](#example)
- [Dynamic Partitioning](#dynamic-partitioning)
  - [Concept](#concept)
- [Memory Allocation Strategies](#memory-allocation-strategies)
  - [1. First-Fit Allocation](#1-first-fit-allocation)
  - [2. Best-Fit Allocation](#2-best-fit-allocation)
  - [3. Worst-Fit Allocation](#3-worst-fit-allocation)
  - [Allocation Example](#allocation-example)
- [Fragmentation Management](#fragmentation-management)
  - [Types of Fragmentation](#types-of-fragmentation)
  - [Compaction Technique](#compaction-technique)
- [Real-World Applications](#real-world-applications)
- [Examples](#examples)
  - [Example 1: First-Fit Allocation](#example-1-first-fit-allocation)
  - [Example 2: Fragmentation Calculation](#example-2-fragmentation-calculation)
  - [Example 3: Compaction Process](#example-3-compaction-process)
- [Exam Tips](#exam-tips)

## Introduction

Contiguous memory allocation is a fundamental memory management technique where each process is allocated a single contiguous block of physical memory. This approach ensures that all addresses required by a process are sequentially arranged in physical RAM, simplifying memory access and address translation.

In operating systems, contiguous allocation plays a critical role in early-stage memory management systems. While modern systems predominantly use non-contiguous methods (like paging), understanding contiguous allocation is essential for grasping memory fragmentation challenges and evolution of memory management techniques.

Key advantages include:

1. Simple implementation with minimal hardware requirements
2. Fast memory access through base+limit register addressing
3. Predictable performance for sequential memory operations

## System Model for Memory Allocation

The operating system maintains a memory map consisting of:

- **Occupied partitions**: Memory blocks allocated to processes
- **Free partitions (holes)**: Available memory blocks
- **Memory Management Table**: Tracks allocated/free blocks using data structures like:
- Bitmaps
- Linked lists
- Partition allocation tables

![Memory Layout Diagram](Described: Memory divided into fixed/variable partitions with occupied and free blocks marked. OS maintains allocation table.)

## Fixed Partitioning

### Concept

Memory is divided into fixed-size partitions during system initialization. Common in early batch processing systems.

**Characteristics:**

- Partition sizes predetermined (e.g., 1MB, 4MB, 8MB)
- Process assigned to smallest available partition that can accommodate it
- Internal fragmentation occurs when process < partition size

**Internal Fragmentation Formula:**

```
Fragmentation = Σ(Partition Size - Process Size)
for all allocated partitions
```

### Example

Partition Sizes: [4MB, 4MB, 8MB]
Processes: P1(3MB), P2(5MB), P3(2MB)
Allocation:

- P1 → 4MB partition (1MB fragmentation)
- P2 → 8MB partition (3MB fragmentation)
- P3 → 4MB partition (2MB fragmentation)
  Total Internal Fragmentation = 6MB

## Dynamic Partitioning

### Concept

Memory partitions created dynamically based on process requirements. Introduced to reduce internal fragmentation.

**Characteristics:**

- Variable partition sizes
- External fragmentation occurs over time
- Requires complex memory management

**External Fragmentation Example:**
After multiple allocations/deallocations, free memory becomes scattered in small blocks that cannot be used for larger processes.

## Memory Allocation Strategies

Three principal algorithms for dynamic partitioning:

### 1. First-Fit Allocation

- **Mechanism:** Allocate to first hole ≥ process size
- **Advantage:** Fast search
- **Disadvantage:** Creates uneven holes

### 2. Best-Fit Allocation

- **Mechanism:** Allocate to smallest hole ≥ process size
- **Advantage:** Minimizes leftover space
- **Disadvantage:** Leaves small unusable fragments

### 3. Worst-Fit Allocation

- **Mechanism:** Allocate to largest available hole
- **Advantage:** Reduces small fragments
- **Disadvantage:** Quickly eliminates large holes

### Allocation Example

**Memory State:** Free blocks [200KB, 400KB, 300KB, 250KB]
**Process Request:** 210KB

| Strategy  | Selected Block | Remaining Space |
| --------- | -------------- | --------------- |
| First-Fit | 400KB          | 190KB           |
| Best-Fit  | 250KB          | 40KB            |
| Worst-Fit | 400KB          | 190KB           |

## Fragmentation Management

### Types of Fragmentation

1. **Internal Fragmentation:**
   Wasted space within allocated partitions
   `Occurs in fixed partitioning`

2. **External Fragmentation:**
   Total free memory exists but not contiguous
   `Occurs in dynamic partitioning`

### Compaction Technique

**Process:**

1. Stop all process execution
2. Move allocated partitions to one end
3. Merge all free space into single block
4. Update base registers

**Overhead Considerations:**

- Requires relocation hardware support
- Time-consuming for large memory
- Cannot be done while processes are running

## Real-World Applications

1. **DOS Systems:** Used contiguous allocation for .COM executables
2. **Embedded Systems:** Simple microcontrollers with fixed memory needs
3. **Database Systems:** Optimized sequential access for large datasets
4. **Early UNIX Versions:** Used for process memory allocation before paging

## Examples

### Example 1: First-Fit Allocation

**Memory Map:** [100KB (free), 500KB (free), 200KB (free)]
**Process Request:** 450KB

1. Check first block (100KB): Too small
2. Check second block (500KB): Allocate 450KB
3. Remaining space: 50KB new hole
   **Resulting Memory:** [100KB, [450KB allocated], 50KB, 200KB]

### Example 2: Fragmentation Calculation

**Fixed Partitions:** 5 partitions of 10MB each
**Processes:** P1(4MB), P2(7MB), P3(3MB)

Internal Fragmentation:

- P1: 10-4 = 6MB
- P2: 10-7 = 3MB
- P3: 10-3 = 7MB
  Total = 16MB

### Example 3: Compaction Process

**Initial Memory:**
[200KB allocated], [100KB free], [300KB allocated], [150KB free]

After Compaction:
[200KB allocated][300KB allocated][250KB free]
Free space consolidated into single 250KB block

## Exam Tips

1. **Allocation Strategy Identification:** Be prepared to identify which strategy was used given allocation patterns
2. **Fragmentation Calculations:** Practice both internal and external fragmentation numerical problems
3. **Compaction Overhead:** Understand why compaction is expensive and when it's used
4. **First-Fit vs Best-Fit:** Know performance differences - Best-Fit generally causes more external fragmentation
5. **Base+Limit Registers:** Remember these are essential hardware components for contiguous allocation
6. **Real-World Comparison:** Be able to contrast contiguous vs non-contiguous allocation in modern systems
7. **Partition Table Management:** Understand how linked lists vs bitmaps affect allocation speed
