# Memory Management Techniques

## Introduction
Memory management is a critical component of modern computer systems that ensures efficient utilization of primary memory resources. In multiprogramming environments where multiple processes reside in memory simultaneously, effective memory management techniques prevent conflicts, optimize performance, and enable virtual memory capabilities that exceed physical RAM limitations.

With the increasing complexity of applications and growing memory demands, techniques like paging, segmentation, and virtual memory have become fundamental to operating system design. Proper memory management directly impacts system performance, security, and ability to support large-scale applications - making it essential knowledge for computer architects and system programmers.

In contemporary systems, memory management units (MMUs) work with operating systems to implement these techniques transparently. Understanding these mechanisms is crucial for optimizing application performance, debugging memory-related issues, and designing efficient computing systems.

## Key Concepts
1. **Contiguous Memory Allocation**: 
   - Fixed Partitioning: Divides memory into fixed-size partitions
   - Variable Partitioning: Dynamic allocation using holes management
   - Fragmentation: Internal (unused space within partitions) vs External (unused space between partitions)

2. **Paging**:
   - Divides memory into fixed-size frames and logical memory into pages
   - Page table translates logical to physical addresses
   - Translation Lookaside Buffer (TLB) accelerates address translation

3. **Segmentation**:
   - Memory divided into variable-sized segments based on logical units
   - Uses segment table with base and limit registers
   - Supports better memory protection and sharing

4. **Virtual Memory**:
   - Demand paging: Pages loaded only when needed
   - Page replacement algorithms (FIFO, LRU, OPT)
   - Thrashing prevention through working set model

5. **Memory Protection**:
   - Base and limit registers
   - Read/write/execute protection bits
   - Address space isolation between processes

## Examples

**Example 1: Paging Address Translation**
```
Logical address: 0x2A5 (681 in decimal)
Page size: 256 bytes
Page table entries: [0:3, 1:7, 2:5, 3:2]

Solution:
1. Page number = 681 // 256 = 2
2. Offset = 681 % 256 = 169
3. Physical frame = 5
4. Physical address = (5 * 256) + 169 = 1449 = 0x5A9
```

**Example 2: LRU Page Replacement**
```
Reference string: 1 2 3 4 2 1 5 6 2 1
Frame count: 3

Page Fault Analysis:
1. 1 [1]         (Fault)
2. 2 [1,2]       (Fault)
3. 3 [1,2,3]     (Fault)
4. 4 [2,3,4]     (Fault) LRU=1
5. 2 [3,4,2]     (Hit)
6. 1 [4,2,1]     (Fault) LRU=3
7. 5 [2,1,5]     (Fault) LRU=4
8. 6 [1,5,6]     (Fault) LRU=2
9. 2 [5,6,2]     (Fault) LRU=1
10.1 [6,2,1]     (Fault) LRU=5
Total faults: 9
```

**Example 3: Segmentation Protection**
```
Segment Table:
Segment | Base | Limit | Protection
0       | 2000 | 500   | R/W
1       | 3500 | 800   | R

Logical address: (1, 600)

Check:
1. Segment 1 limit is 800 → 600 < 800 (valid)
2. Protection is Read-only
3. Physical address = 3500 + 600 = 4100
Attempted write operation → Generates protection fault
```

## Exam Tips
1. Practice numerical problems on address translation for both paging and segmentation
2. Memorize page replacement algorithms with their Belady's anomaly status
3. Understand the hardware-software interaction in TLB management
4. Compare and contrast internal vs external fragmentation with examples
5. Learn to calculate effective memory access time with TLB hit ratio
6. Study real-world implementations (Linux buddy system, Windows virtual memory)
7. Prepare to draw and explain memory hierarchy diagrams with access times