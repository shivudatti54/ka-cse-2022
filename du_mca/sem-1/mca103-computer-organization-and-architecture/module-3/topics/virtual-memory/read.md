# Virtual Memory

## Introduction
Virtual memory is a fundamental memory management technique that enables computers to use disk storage as an extension of RAM. This abstraction allows processes to operate as if they have contiguous memory space larger than physical memory, while actual data may reside in physical memory or secondary storage. 

The concept revolutionized computing by solving three critical problems: 1) Allowing execution of processes larger than physical memory 2) Enabling efficient memory sharing between processes 3) Providing memory protection through address space isolation. Modern operating systems like Linux and Windows implement sophisticated virtual memory systems using demand paging and segmentation.

For MCA students, understanding virtual memory is crucial for system programming, performance optimization, and working with modern computer architectures. It forms the basis for memory management in cloud computing, database systems, and embedded systems.

## Key Concepts
1. **Demand Paging**: 
   - Pages are loaded into memory only when needed (page fault occurs)
   - Uses valid/invalid bit in page table entries
   - Enables efficient memory utilization through lazy loading

2. **Page Replacement Algorithms**:
   - FIFO (First-In First-Out): Replace oldest page
   - Optimal: Replace page not used for longest future time (theoretical)
   - LRU (Least Recently Used): Track page usage recency
   - Clock (Second Chance): Circular buffer with reference bit

3. **Translation Lookaside Buffer (TLB)**:
   - Hardware cache for page table entries
   - Reduces memory access time by avoiding page table walks
   - TLB hit vs TLB miss handling

4. **Address Translation**:
   - Virtual address = Page number + Page offset
   - Physical address = Frame number + Page offset
   - Multi-level page tables for large address spaces

5. **Working Set Model**:
   - Set of pages actively used by process in time window
   - Basis for preventing thrashing
   - Working set window (Δ) determines locality

6. **Segmentation with Paging**:
   - Combines logical segmentation with paged memory
   - Two-level translation: Segment table → Page table
   - Used in Intel x86 architecture

## Examples

**Example 1: LRU Page Replacement**
Reference String: 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2
Frame Count: 3

Solution:
1. Page 7 loaded (Frames: [7])
2. Page 0 loaded (Frames: [7,0])
3. Page 1 loaded (Frames: [7,0,1]) 
4. Page 2 replaces LRU page 7 (Frames: [0,1,2])
5. Page 0 hits (New order: [1,2,0])
6. Continue tracking recency... Total page faults: 9

**Example 2: Address Translation**
Virtual Address: 0x3A7F (16-bit)
Page size: 4KB (12-bit offset)
Page number: 0x3 (0011)
Offset: 0xA7F

Page table entry 3 contains frame 0x5A
Physical address = (0x5A << 12) | 0xA7F = 0x5AA7F

**Example 3: TLB Impact Calculation**
TLB hit ratio: 80%
TLB access time: 10ns
Memory access time: 100ns
Effective Access Time (EAT) = 0.8*(10+100) + 0.2*(10+100+100) = 130ns

## Exam Tips
1. Always draw page tables/TLB structures for numerical problems
2. For replacement algorithms, track usage timestamps/queue positions
3. Remember Optimal is theoretical - used as benchmark
4. Differentiate between segmentation fault and page fault
5. Calculate EAT considering TLB misses and page faults
6. Thrashing occurs when ∑working sets > physical memory
7. Inverted page tables reduce memory overhead but increase lookup time

Length: 1500-3000 words, MCA (Master of Computer Applications) PG level