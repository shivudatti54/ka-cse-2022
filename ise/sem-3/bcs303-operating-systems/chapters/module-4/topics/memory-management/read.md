# Memory Management

## Introduction

Memory management is a fundamental concept in operating systems that deals with the allocation and deallocation of memory to processes while ensuring efficient utilization of the computer's primary memory (RAM). In modern computing environments, multiple processes run concurrently, each requiring a portion of the limited physical memory. The operating system must manage this scarce resource intelligently to maximize performance, ensure process isolation, and provide the illusion of abundant memory through virtual memory techniques.

The importance of memory management cannot be overstated in the context of computer science. Without effective memory management, processes could interfere with each other's data, memory would become fragmented leading to inefficiency, and the system would be unable to run programs larger than the physical RAM available. Operating systems employ various memory management strategies ranging from simple contiguous allocation to sophisticated paging and segmentation mechanisms. Understanding these techniques is essential for any computer science student, as they form the backbone of system-level programming and influence application performance significantly.

This chapter explores the theoretical foundations and practical implementations of memory management in operating systems. We will examine the evolution of memory management techniques, from early single-user systems to modern multi-tasking environments. The discussion will cover both the fundamental concepts of memory allocation and the advanced virtual memory systems that enable modern computing capabilities like demand paging, page replacement algorithms, and thrashing prevention.

## Key Concepts

### Basic Memory Management Requirements

Memory management systems must satisfy several critical requirements to function effectively. The first requirement is RELOCATION, which allows processes to be loaded into any region of physical memory during execution. Since the exact memory location cannot be predetermined, the operating system must support dynamic address translation. The second requirement is PROTECTION, ensuring that processes cannot access memory belonging to other processes without authorization. This isolation prevents security breaches and system instability. The third requirement is SHARING, which permits multiple processes to access shared data structures when necessary, such as shared libraries or inter-process communication buffers. The fourth requirement is LOGICAL ORGANIZATION, reflecting the way programs are structured into modules with different access permissions. The fifth requirement is PHYSICAL ORGANIZATION, which deals with the hierarchy of memory including fast cache, main memory, and slower secondary storage.

### Swapping

Swapping is a memory management technique where entire processes are moved between main memory and secondary storage (typically the disk). When physical memory becomes full, the operating system selects a process that has been idle for some time and swaps its entire memory image to the swap space on the disk. The freed physical memory can then be used for another process. When the swapped-out process needs to run again, it is swapped back into memory, possibly in a different location than before.

Swapping was more common in early operating systems with limited memory. While less frequently used in modern systems as the primary memory management technique, swapping remains important for memory compression and in systems with very limited RAM. The key metrics for swapping performance are the swap time, which depends on the amount of data being transferred, and the swap frequency, which affects overall system responsiveness.

### Contiguous Memory Allocation

In contiguous memory allocation, each process is allocated a single continuous block of physical memory. The operating system maintains a memory map that tracks which portions of memory are free and which are occupied. When a process requests memory, the system searches for a free block large enough to accommodate it using one of several allocation strategies.

FIRST FIT allocates the first free block that is large enough for the process. It is generally fast as the search terminates quickly. BEST FIT searches all free blocks and allocates the smallest one that is large enough, minimizing wasted space but requiring a complete search. WORST FIT allocates the largest available free block, leaving larger remaining fragments but is generally less efficient. NEXT FIT is similar to first fit but begins the search from where the last allocation ended.

Contiguous allocation suffers from external fragmentation, where free memory is divided into small non-contiguous blocks, making it impossible to satisfy large requests even when the total free memory is sufficient. Internal fragmentation occurs when allocated memory is slightly larger than requested, wasting space within the allocated block.

### Paging

Paging is a memory management scheme that eliminates external fragmentation by dividing both physical and logical memory into fixed-size blocks called frames and pages respectively. The physical memory is divided into frames of size typically 4KB, while logical memory is divided into pages of the same size. A page table mapping translates logical page numbers to physical frame numbers.

When a process accesses a memory location, the CPU divides the logical address into a page number and offset. The page number indexes into the page table to obtain the corresponding frame number, which is combined with the offset to form the physical address. This translation is performed by a hardware component called the Memory Management Unit (MMU).

Paging introduces internal fragmentation because a process may not use all memory in its last page. However, the internal fragmentation is limited to at most one page per process, making it more efficient than contiguous allocation for large numbers of processes. The page table itself can become large, leading to the development of techniques like multi-level page tables, inverted page tables, and Translation Lookaside Buffers (TLB) for efficient address translation.

### Segmentation

Segmentation is a memory management technique that provides logical organization of memory by dividing it into variable-sized segments based on the program's logical structure. Typical segments include code, data, stack, and heap. Each segment has a name (or number) and a length, and logical addresses are specified as segment name plus offset.

The segment table stores the base address (starting location) and limit (length) for each segment. When translating a logical address, the system verifies that the offset is within the segment's limit, preventing access beyond segment boundaries. This provides natural protection, as different segments can have different access permissions (read-only for code, read-write for data).

Segmentation can be combined with paging, where each segment is divided into pages. This approach combines the logical benefits of segmentation with the physical memory management advantages of paging. The logical address in a segmented-paged system consists of segment number, page number within that segment, and offset within the page.

### Virtual Memory

Virtual memory is an extension of the basic paging and segmentation concepts that allows execution of processes that may not be completely in memory. It creates the illusion of a memory space larger than physical memory by using secondary storage to hold portions of processes that are not currently in use.

The key advantage of virtual memory is that programs can be larger than physical memory, and the operating system transparently loads code and data as needed. This also allows sharing of memory between processes and simplifies program loading. Virtual memory is implemented through demand paging, where pages are loaded into memory only when referenced, or through demand segmentation.

### Demand Paging

Demand paging is a virtual memory implementation where pages are loaded into memory only when a page fault occurs, meaning the referenced page is not currently in memory. This lazy loading approach defers the cost of loading pages until they are actually needed by the executing program.

When a process references a page not in memory, the operating system must handle the page fault by identifying the location of the needed page on disk, finding a free frame in memory, loading the page from disk into that frame, updating the page table, and restarting the interrupted instruction. The time to handle a page fault is orders of magnitude slower than a memory access, making page fault handling efficiency critical for system performance.

### Copy-on-Write

Copy-on-write is an optimization technique used in memory management where processes that share the same memory page initially share that page in read-only mode. When either process attempts to modify the shared page, the operating system creates a private copy of the page for the modifying process. This technique is particularly useful in fork operations, where the child process typically immediately execs a new program, making the copy operation unnecessary.

Copy-on-write significantly reduces memory overhead and improves performance by deferring or avoiding memory copies. Modern operating systems extensively use this technique for process creation and memory efficiency in applications that use fork.

### Page Replacement

When all frames in physical memory are occupied and a page fault occurs, the operating system must select a victim page to evict from memory to make room for the new page. The algorithm used to select this victim is called the page replacement algorithm.

The FIFO (First-In-First-Out) algorithm evicts the oldest page in memory. It is simple to implement but may evict frequently used pages, leading to poor performance. The OPTIMAL algorithm selects the page that will not be referenced for the longest time in the future, achieving the lowest possible page faults but is impossible to implement in practice as it requires future knowledge. The LRU (Least Recently Used) algorithm evicts the page that has not been referenced for the longest time, approximating optimal behavior and widely used in practice.

Other algorithms include CLOCK (Second Chance), which uses a reference bit to approximate LRU efficiently, and the WORKING SET model, which maintains pages that a process has referenced in its recent window.

### Thrashing

Thrashing occurs when a process spends more time paging (handling page faults) than executing. This happens when the process does not have enough frames allocated to it, causing constant page evictions and reloads. Thrashing severely degrades system performance as the CPU spends most of its time waiting for disk I/O.

The working set model helps prevent thrashing by keeping in memory the pages that a process has referenced in its recent time window. The system monitors each process's working set and allocates sufficient frames to accommodate it. When total memory demand exceeds available memory, the system may suspend or swap out processes to recover frames for active processes.

## Examples

### Example 1: Page Table Translation

Consider a system with 16-bit logical addresses and 4KB (2^12 bytes) page size. Calculate the number of bits for page number and offset, and translate the logical address 0x3F7A.

SOLUTION: With 4KB page size, the offset requires log2(4096) = 12 bits. The remaining 4 bits (16 - 12 = 4) are used for page number, giving 2^4 = 16 pages.

For logical address 0x3F7A:
- Convert to binary: 0011 1111 0111 1010
- Split into page number (first 4 bits) and offset (last 12 bits)
- Page number: 0011 (binary) = 3 (decimal)
- Offset: 1111 0111 1010 (binary) = 0xF7A = 3962 (decimal)

If the page table entry for page 3 shows frame number 5, the physical address is:
- Frame number: 5 (binary 0101)
- Offset: 0xF7A
- Physical address: 0101 1111 0111 1010 = 0x5F7A

### Example 2: Page Fault Calculation

A process accesses pages in the following order: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5. Using FIFO replacement with 3 frames, calculate the number of page faults.

SOLUTION:
- Initial: empty (3 frames available)
- Access 1: page 1 loaded (page fault)
- Access 2: page 2 loaded (page fault)
- Access 3: page 3 loaded (page fault)
- Access 4: page 4 needed, replace page 1 (oldest) (page fault)
- Access 1: page 1 needed, replace page 2 (oldest) (page fault)
- Access 2: page 2 needed, replace page 3 (page fault)
- Access 5: page 5 needed, replace page 4 (page fault)
- Access 1: page 1 already in memory (no fault)
- Access 2: page 2 already in memory (no fault)
- Access 3: page 3 needed, replace page 1 (page fault)
- Access 4: page 4 needed, replace page 2 (page fault)
- Access 5: page 5 already in memory (no fault)

Total page faults: 9

### Example 3: Contiguous Allocation

Consider a system with 1000 KB of memory. The operating system uses 100 KB, and the rest is available for user processes. Using best fit, allocate memory for processes requiring 200 KB, 150 KB, and 300 KB in that order. What is the remaining free memory after all allocations?

SOLUTION:
- Available memory: 1000 - 100 = 900 KB
- Process 1 (200 KB): Find smallest hole >= 200 KB = 200 KB hole at start (page fault - allocate 200 KB)
- Remaining: 900 - 200 = 700 KB (one hole of 700 KB)
- Process 2 (150 KB): Find smallest hole >= 150 KB = 700 KB hole (allocate 150 KB)
- Remaining: 700 - 150 = 550 KB (one hole of 550 KB)
- Process 3 (300 KB): Find smallest hole >= 300 KB = 550 KB hole (allocate 300 KB)
- Remaining: 550 - 300 = 250 KB (one hole of 250 KB)

Total allocated: 200 + 150 + 300 = 650 KB
Total remaining free: 900 - 650 = 250 KB

## Exam Tips

1. UNDERSTAND THE DIFFERENCE BETWEEN LOGICAL AND PHYSICAL ADDRESSES: Logical addresses are generated by the CPU and are relative to the program's address space, while physical addresses refer to actual memory locations. The MMU translates between them.

2. MEMORIZE THE PAGE TABLE STRUCTURE: For paging, remember that logical address = (page number × page size) + offset, and physical address = (frame number × frame size) + offset.

3. KNOW THE PAGE REPLACEMENT ALGORITHMS: Be able to trace through FIFO, LRU, and OPTIMAL algorithms for a given reference string and calculate page faults. FIFO is simplest to implement; LRU is the most common practical approximation.

4. UNDERSTAND THRASHING: Remember that thrashing occurs when processes spend more time in page faults than execution. The solution involves reducing the degree of multiprogramming or increasing the number of frames allocated.

5. DIFFERENTIATE BETWEEN INTERNAL AND EXTERNAL FRAGMENTATION: Internal fragmentation occurs within allocated blocks (paging), while external fragmentation occurs between free blocks (contiguous allocation). Paging eliminates external fragmentation but has internal fragmentation.

6. VIRTUAL MEMORY FUNDAMENTALS: Virtual memory allows programs larger than physical memory to run by keeping only active pages in memory and swapping others to disk. This is the basis for modern computing.

7. COPY-ON-WRITE IS EFFICIENT: Remember that copy-on-write defers copying until a write occurs, saving memory and time when child processes immediately execute new programs after fork.

8. TLB CACHING: The Translation Lookaside Buffer is a hardware cache that stores recent page table translations, significantly speeding up address translation. Higher TLB hit rate means better performance.