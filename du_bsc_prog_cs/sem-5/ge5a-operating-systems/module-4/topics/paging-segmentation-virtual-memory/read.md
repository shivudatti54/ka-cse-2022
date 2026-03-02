# Paging, Segmentation, and Virtual Memory

## Introduction

Memory management is one of the most critical functions of any modern operating system. As application software grew increasingly complex with larger codebases and data requirements, the physical memory available in computers became insufficient. This limitation necessitated the development of sophisticated memory management techniques that could create an illusion of having more memory than actually exists. Virtual memory, combined with paging and segmentation, represents the elegant solution that operating systems employ to address this fundamental challenge.

The concept of virtual memory revolutionized computing by allowing programs to use more memory than what is physically available in the system. It achieves this by dynamically swapping data between physical RAM and secondary storage (typically hard drives or SSDs). For University of Delhi Computer Science students, understanding these memory management techniques is essential not only for passing examinations but also for comprehending how modern operating systems optimize resource utilization. The interplay between paging and segmentation provides both flexibility and protection in memory allocation, making these topics fundamental to operating system design.

This module explores three interrelated concepts: paging, which divides memory into fixed-size blocks; segmentation, which divides memory into variable-sized logical units; and virtual memory, which combines both techniques to create an address space larger than physical memory. These concepts form the backbone of memory management in systems ranging from personal computers to enterprise servers.

## Key Concepts

### Paging: The Foundation of Virtual Memory

Paging is a memory management scheme that eliminates the need for contiguous allocation of physical memory. It divides both the process's virtual address space and the physical memory into fixed-size blocks called **pages** (in virtual memory) and **frames** (in physical memory). Typically, page sizes range from 4KB to 64KB depending on the system architecture.

The **page table** serves as the core data structure for mapping virtual pages to physical frames. Each process maintains its own page table, which contains one entry for each page in the process's virtual address space. This page table entry (PTE) stores the frame number and control bits such as valid/invalid bit, dirty bit, and access permission bits. When a CPU generates a virtual address, the memory management unit (MMU) uses the page table to translate it into a physical address.

**Translation Lookaside Buffer (TLB)** is a specialized cache that stores recent page table entries. Since accessing the page table in memory would require an additional memory reference (effectively doubling memory access time), the TLB provides hardware-level speedup. On a TLB hit, the translation completes in a single memory access. On a TLB miss, the system must access the page table in memory and update the TLB with the new entry.

**Multi-level page tables** address the problem of large address spaces requiring enormous single-level page tables. Instead of maintaining a flat page table, a hierarchical structure divides the page table into pages themselves. For 32-bit systems, two-level paging is common; for 64-bit systems, four-level or more sophisticated structures are used. This approach allows the system to allocate page table pages only for those parts of the address space that are actually in use.

**Inverted page tables** represent an alternative approach where the system maintains one entry per physical frame rather than per virtual page. This significantly reduces memory overhead for large address spaces but increases the time required to look up page table entries, often requiring hash tables for efficient searching.

### Segmentation: Logical Memory Organization

Segmentation complements paging by dividing memory into logically meaningful units called **segments**. Unlike the fixed-size pages, segments can be of variable size and represent logical divisions such as code, data, stack, heap, or shared libraries. Each segment has a base address (starting location) and a limit (size), providing natural protection boundaries for different program components.

The **segment table** stores the base address and limit for each segment, along with protection information. A segment selector in the CPU instruction specifies which segment is being accessed. The effective address is then checked against the segment limit, and if valid, the base address is added to produce the physical address.

Segmentation provides several advantages over pure paging. First, it offers natural protection because different segments can have different access rights (read, write, execute). Second, it allows programs to be written with logical clarity—programmers can think in terms of code, stack, and data segments rather than arbitrary memory addresses. Third, when a segment grows or shrinks, only that segment's limit needs adjustment, making dynamic data structures easier to manage.

The primary disadvantage of pure segmentation is **external fragmentation**. Because segments are variable-sized, freeing and allocating segments leaves holes in memory that cannot always be filled by available free segments. This led to the development of **combined segmentation and paging**, where segments are divided into pages, combining the benefits of both approaches.

### Virtual Memory: Demand Paging and Performance

Virtual memory extends the concept of paging to create the illusion of a larger, contiguous address space. The key innovation is **demand paging**, where pages are loaded into physical memory only when they are needed. This lazy loading approach means that a process can start execution with only a few pages in memory, and additional pages are brought in as needed.

The **page fault** is a critical event in demand paging. When a process accesses a page that is not currently in physical memory (marked as invalid in the page table), a page fault occurs. The operating system must then:
1. Determine the location of the requested page on disk
2. Find a free frame in physical memory
3. Load the page from disk into the selected frame
4. Update the page table entry
5. Restart the interrupted instruction

**Page replacement algorithms** become essential when all physical memory is in use and a new page must be loaded. The system must choose which existing page to evict. Key algorithms include:

**First-In-First-Out (FIFO)** maintains a queue of pages in memory and evicts the oldest page. While simple to implement, FIFO suffers from Belady's anomaly—increasing the number of frames can sometimes increase page faults.

**Least Recently Used (LRU)** evicts the page that has not been accessed for the longest time. This approximates the optimal algorithm but requires hardware support for tracking access times and can be expensive to implement perfectly.

**Optimal Page Replacement** evicts the page that will not be used for the longest time in the future. This algorithm produces the minimum possible page faults but requires future knowledge, making it unimplementable in practice. It serves as a theoretical benchmark.

**Second Chance (Clock)** is a practical approximation of LRU that uses a reference bit and circular scanning. Pages with the reference bit set get a second chance to remain in memory, making it efficient and commonly used in real systems.

### Thrashing and Working Set Theory

**Thrashing** occurs when a system spends more time swapping pages in and out of memory than executing processes. This typically happens when the degree of multiprogramming is too high or when processes don't have enough pages to fit their working set. The system becomes trapped in a cycle of constant page faults, severely degrading performance.

**Working set theory**, developed by Peter Denning, provides a framework for understanding and preventing thrashing. The working set of a process is the set of pages it has referenced in the recent past. If the total working set of all processes exceeds available physical memory, thrashing occurs. The operating system can use this theory to make intelligent scheduling decisions, ensuring each process has sufficient memory for its working set.

## Examples

### Example 1: Virtual Address Translation with Paging

Consider a system with 16-bit virtual addresses and 4KB page size. Determine the page number and offset for the virtual address 0x3F7A.

**Solution:**

Since page size is 4KB = 2^12 bytes, the offset requires 12 bits. Therefore, the remaining 4 bits (16 - 12 = 4) represent the page number.

Virtual address in binary: 0011 1111 0111 1010

- Page number (first 4 bits): 0011 = 3
- Offset (last 12 bits): 1111 0111 1010 = 0xF7A = 4,026

So, this address is in page 3, at offset 4,026 within that page.

### Example 2: Page Fault Calculation

A process references pages in the following order: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5. Using FIFO replacement with 3 frames, calculate the number of page faults.

**Solution:**

Initially, all frames are empty (page faults for first 3 accesses):

| Reference | Frames | Page Fault? |
|-----------|--------|-------------|
| 1 | [1] | Yes (1) |
| 2 | [1,2] | Yes (2) |
| 3 | [1,2,3] | Yes (3) |
| 4 | [4,2,3] | Yes (4) - Evicts 1 |
| 1 | [4,1,3] | Yes (5) - Evicts 2 |
| 2 | [4,1,2] | Yes (6) - Evicts 3 |
| 5 | [5,1,2] | Yes (7) - Evicts 4 |
| 1 | [5,1,2] | No - Already in memory |
| 2 | [5,1,2] | No |
| 3 | [3,1,2] | Yes (8) - Evicts 5 |
| 4 | [3,4,2] | Yes (9) - Evicts 1 |
| 5 | [3,4,5] | Yes (10) - Evicts 2 |

Total page faults = 10

### Example 3: Combined Segmentation and Paging

In a system with segmentation and paging, a logical address consists of a segment selector (8 bits), page number within segment (12 bits), and page offset (12 bits). If a process generates logical address 0xA1F3B456, determine the segment number, page number, and offset.

**Solution:**

Logical address breakdown:
- Segment selector: 8 bits = 0xA1
- Page number: 12 bits = 0xF3B
- Offset: 12 bits = 0x456

In hexadecimal: 0xA1F3B456

- Segment number: A1 (hex) = 161
- Page number: F3B (hex) = 3,899
- Offset: 456 (hex) = 1,110

The MMU first uses the segment selector to find the segment table entry, which provides the base address of the page table for that segment. Then it uses the page number to find the frame number, and finally adds the offset to get the physical address.

## Exam Tips

1. **Draw the address translation diagrams**: For exam questions, always include clear diagrams showing how virtual addresses are translated to physical addresses using page tables or segment tables. Visual representation earns marks.

2. **Remember the page table entry fields**: Know the standard bits in a PTE—valid/invalid bit, frame number, dirty bit, reference (access) bit, and protection bits. Questions frequently ask about the purpose of each bit.

3. **Calculate page fault rates correctly**: When solving problems, always check if the requested page is already in memory before deciding on a page fault. Track the current state of frames carefully.

4. **Understand Belady's Anomaly**: Know that FIFO can exhibit the counterintuitive behavior where more frames lead to more page faults. Be able to provide an example demonstrating this anomaly.

5. **Compare algorithms using reference strings**: When asked to compare page replacement algorithms, work through the same reference string with different algorithms and count the page faults.

6. **Know when to use each technique**: Understand that pure paging has no external fragmentation but may cause internal fragmentation, while pure segmentation may have external fragmentation but no internal fragmentation. Combined approaches aim to minimize both.

7. **TLB hit ratio calculation**: Be prepared to calculate effective memory access time given TLB hit ratio, TLB access time, and memory access time. The formula is: Effective Time = Hit Ratio × (TLB + Memory) + (1 - Hit Ratio) × (TLB + 2 × Memory).

8. **Thrashing prevention**: Know that the operating system can use working set models or page fault frequency to detect and prevent thrashing by adjusting the degree of multiprogramming.