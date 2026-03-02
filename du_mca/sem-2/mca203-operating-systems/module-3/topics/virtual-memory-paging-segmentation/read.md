# Virtual Memory: Paging & Segmentation

## Introduction
Virtual memory is a fundamental memory management technique that enables processes to execute with more memory than physically available. This abstraction layer creates the illusion of contiguous memory space while using physical RAM and secondary storage strategically. Modern operating systems implement virtual memory through two primary techniques: paging and segmentation.

The importance of virtual memory lies in its ability to:
1. Enable efficient memory utilization through demand paging
2. Provide memory protection between processes
3. Allow programs to exceed physical memory limitations
4. Simplify programming by abstracting physical memory constraints

In professional computing environments, virtual memory is critical for running memory-intensive applications like databases, scientific simulations, and modern web browsers. The Delhi University MCA curriculum emphasizes this topic due to its practical significance in system design and optimization.

## Key Concepts

**1. Paging**
- Divides memory into fixed-size blocks (pages)
- Physical memory divided into page frames
- Page table maintains mapping between logical and physical addresses
- Enables non-contiguous physical allocation of memory pages

**2. Segmentation**
- Divides memory into variable-sized logical units
- Segments correspond to program structure (code, data, stack)
- Uses segment table with base-limit pairs
- Provides better memory protection and sharing capabilities

**3. Page Table Structure**
- Hierarchical page tables for large address spaces
- Translation Lookaside Buffer (TLB) for faster address translation
- Inverted page tables for memory-constrained systems

**4. Address Translation**
- Logical address = Page number + Page offset
- Physical address = Frame number + Page offset
- Segmentation uses segment number + offset

**5. Page Replacement Algorithms**
- Optimal (OPT)
- Least Recently Used (LRU)
- First-In-First-Out (FIFO)
- Clock (Second Chance)

## Examples

**Example 1: Page Table Translation**
Given:
- 32-bit logical address space
- 4KB page size
- Page table entry: 0x0000C3A7 (valid bit=1, frame=0xC3A)

Calculate physical address for logical address 0x00456789

Solution:
1. Page offset = 12 bits (4KB = 2^12)
2. Page number = 0x00456 (20 bits)
3. From page table: Frame = 0xC3A
4. Physical address = (0xC3A << 12) + 0x789 = 0xC3A789

**Example 2: Segmentation Fault Analysis**
Process segments:
- Code: Base=0x4000, Limit=0x1000
- Data: Base=0x8000, Limit=0x2000

Determine validity of address (Segment 1, Offset 0x1500)

Solution:
1. Segment 1 (Data) limit = 0x2000
2. 0x1500 < 0x2000 → Valid
3. Physical address = 0x8000 + 0x1500 = 0x9500

**Example 3: LRU Page Replacement**
Reference string: 1 2 3 4 1 2 5 1 2 3 4 5
3 frame allocation:

| Ref | Frames     | Page Fault |
|-----|------------|------------|
| 1   | [1]        | Yes        |
| 2   | [1,2]      | Yes        |
| 3   | [1,2,3]    | Yes        |
| 4   | [2,3,4]    | Yes (LRU=1)|
| 1   | [3,4,1]    | Yes (LRU=2)|
| Total faults: 9 |

## Exam Tips
1. Always draw memory diagrams for address translation questions
2. Memorize formulas: 
   - Page number = logical address / page size
   - Offset = logical address % page size
3. For segmentation questions, verify offset < segment limit
4. Understand TLB hit ratio calculations:
   Effective Access Time = (TLB_time + mem_access) * hit_ratio + (2*mem_access) * (1-hit_ratio)
5. Practice working of different page replacement algorithms with at least 3 examples
6. Compare paging vs segmentation in tabular form
7. Remember Linux uses combination of paging and segmentation (flat memory model)