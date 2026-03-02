# Structure of Page Table

## Introduction

Memory management is the cornerstone of modern operating systems, enabling efficient utilization of physical memory while providing each process with the illusion of a large, contiguous address space. Paging, one of the most widely used memory management techniques, divides both physical and virtual memory into fixed-size blocks called pages and frames respectively. The page table serves as the critical data structure that maps virtual page numbers to their corresponding physical frame numbers, making virtual memory possible.

Understanding the structure of page tables is essential for comprehending how operating systems implement virtual memory, handle memory protection, and optimize address translation performance. In practical terms, the page table structure directly impacts system performance, memory overhead, and the ability to support large address spaces efficiently. This topic becomes particularly important when designing systems that must handle thousands of processes simultaneously, as the choice of page table structure can significantly affect both memory consumption and access speed.

This chapter explores the internal organization of page tables, examining how they store mapping information, maintain additional metadata for memory management, and employ various structural approaches to handle different system requirements. We will analyze both simple and advanced page table structures, understanding their advantages, disadvantages, and trade-offs in real-world operating systems.

## Key Concepts

### Page Table Entry (PTE) Structure

A page table is essentially an array of page table entries, where each entry corresponds to one virtual page. The primary function of a PTE is to store the physical frame number where the corresponding virtual page resides in main memory. However, a complete PTE contains several additional fields that support memory management operations:

The most critical field is the **frame number** or **physical frame number (PFN)**, which indicates the location of the physical frame containing the virtual page. This field is combined with the offset within the page to form the complete physical address.

The **valid/invalid bit** indicates whether the page is currently resident in physical memory or not. When this bit is set to valid, the page table entry contains a valid frame number. When invalid, the page is either not allocated or has been swapped out to secondary storage. This bit is fundamental to demand paging and virtual memory implementation.

**Protection bits** specify what operations are permitted on the page. Typically, these include read, write, and execute permissions. For instance, code pages might be marked as readable and executable but not writable, while data pages might allow both read and write access. Some systems implement more granular protection using three separate bits for read, write, and execute permissions.

The **dirty** or **modified bit** tracks whether a page has been modified since it was loaded into memory. This information is crucial for page replacement algorithms and for determining whether a page must be written back to disk when being evicted from memory. If the dirty bit is clear, the page can be discarded without writing it back to secondary storage.

The **reference** or **accessed bit** indicates whether the page has been recently accessed. This information is vital for page replacement algorithms like LRU (Least Recently Used) that need to identify pages that have not been used for the longest time. The hardware updates this bit whenever the page is accessed.

The **cache disable** bit controls whether the page can be cached by the CPU's memory management unit. Certain memory-mapped I/O devices require that reads and writes go directly to the physical device without caching.

### Types of Page Table Structures

**Flat or Linear Page Table** represents the simplest structure where the page table is a single-level array indexed directly by the virtual page number. For a 32-bit address space with 4KB pages, the page table would contain 2^20 entries, requiring about 4MB of memory per process if each entry is 4 bytes. While conceptually simple, this approach wastes memory when processes use only a small portion of their virtual address space, as the entire table must be allocated even if most entries are invalid.

**Hierarchical Page Tables** address the memory overhead problem by partitioning the virtual address space into multiple levels. The most common implementation is a two-level page table where the first level (page directory) indexes into second-level page tables, which in turn point to physical frames. This approach only creates second-level page tables for virtual memory regions that are actually in use. For the same 32-bit address space example, a two-level structure might use a 10-bit page directory index and a 10-bit page table index, with the remaining 12 bits as the offset within the page. Modern 64-bit systems employ even deeper hierarchies, such as four-level page tables (PGD → PUD → PMD → PTE) used in Linux.

**Inverted Page Table** takes a radically different approach by maintaining one entry for each physical frame rather than for each virtual page. The entry records which process owns the page and which virtual page is mapped to that frame. To translate a virtual address, the system must search the entire inverted table, which is impractical without additional acceleration structures. Hash tables are commonly used alongside inverted page tables to speed up the search. While this structure drastically reduces memory overhead for large address spaces, it complicates shared memory implementation and can impact translation speed.

**Hash Page Tables** use a hash function to map virtual page numbers to entries in a hash table, with each bucket containing a chain of page table entries that hash to the same value. This approach can efficiently handle sparse address spaces where only a small fraction of virtual pages are valid. The hash function provides O(1) average-case access time, though hash collisions may require traversing the chain.

### Translation Lookaside Buffer (TLB)

The page table, even with hierarchical structures, introduces significant latency to every memory access. To mitigate this performance penalty, processors include a specialized cache called the Translation Lookaside Buffer (TLB) that stores recent virtual-to-physical address translations. The TLB operates as an associative cache, checking all entries in parallel for a matching virtual page number.

On a memory access, the processor first checks the TLB for the virtual page number. If the translation is found (a TLB hit), the physical address is constructed immediately without accessing the page table. If not found (a TLB miss), the system must access the page table to obtain the translation, update the TLB with the new entry, and then complete the memory access. TLB hit rates of 95% or higher are typical in well-designed systems, making virtual memory address translation nearly as fast as physical memory access.

Modern TLBs support multiple page sizes and include features like ASIDs (Address Space Identifiers) to distinguish translations from different processes, allowing TLB entries to remain valid across context switches.

## Examples

### Example 1: Calculating Page Table Size

Consider a system with a 32-bit virtual address space and 4KB pages. Each page table entry is 4 bytes. Calculate the size of a flat page table and explain why it might be problematic.

**Solution:**

With 32-bit addresses and 4KB (2^12) pages, the number of virtual pages is 2^(32-12) = 2^20 = 1,048,576 pages.

Each PTE is 4 bytes, so the flat page table requires:
1,048,576 × 4 bytes = 4,194,304 bytes = 4 MB

For a system running 100 processes, this would require 400 MB just for page tables, which is excessive. Additionally, the entire 4MB table must be allocated contiguously in physical memory, which may not always be possible. This example demonstrates why hierarchical or inverted page tables are preferred in systems with large address spaces.

### Example 2: Two-Level Page Table Translation

A system uses a two-level page table with the following configuration:
- First-level table (page directory): 10 bits
- Second-level page table: 10 bits
- Offset: 12 bits

Given the virtual address 0x12345678, determine:
(a) The page directory index
(b) The page table index
(c) The page offset

**Solution:**

First, convert the address to binary: 0x12345678 = 0001 0010 0011 0100 0101 0110 0111 1000

(a) Page directory index: Bits 31-22 (top 10 bits)
= 0001 0010 00 = 0x48 = 72

(b) Page table index: Bits 21-12 (next 10 bits)
= 11 0100 0101 = 0x345 = 837

(c) Page offset: Bits 11-0 (bottom 12 bits)
= 0110 0111 1000 = 0x678 = 1656

The MMU would first index into entry 72 of the page directory to find the appropriate second-level page table, then index into entry 837 of that page table to obtain the physical frame number, and finally add the offset 0x678 to generate the physical address.

### Example 3: Page Table Entry Bit Analysis

Suppose a page table entry contains the following binary value (from most significant to least significant bit):

1 0 0 1 0 1 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1

Assuming a 32-bit architecture where:
- Bits 31-20: Reserved for frame number
- Bit 19: Valid bit
- Bit 18: Dirty bit
- Bit 17: Reference bit
- Bit 16: Cache disable
- Bits 15-12: Protection bits
- Bits 11-0: Reserved

Determine the values of all these fields.

**Solution:**

Frame number (bits 31-20): 1001 0101 1011 = 0x95B = 2395
Valid bit (bit 19): 1 = Valid
Dirty bit (bit 18): 0 = Not modified
Reference bit (bit 17): 1 = Recently accessed
Cache disable (bit 16): 0 = Caching enabled
Protection bits (bits 15-12): 0001 = Read-only (assuming R=1, W=0, X=0)
Reserved bits: All zeros

This page is valid, has not been modified, has been accessed recently, caching is enabled, and it provides read-only access to the physical frame numbered 2395.

## Exam Tips

1. **Memorize PTE fields**: The standard page table entry fields—valid/invalid, frame number, protection bits, dirty bit, and reference bit—are frequently asked in DU examinations. Understand the purpose of each field clearly.

2. **Hierarchical vs. Inverted page tables**: Be prepared to explain the differences, advantages, and disadvantages of each structure. Hierarchical tables are faster but use more memory; inverted tables use less memory but slower translation.

3. **Address calculation**: Practice converting between virtual addresses and their components (page number, offset) for both single-level and multi-level page tables. This is a common short-answer question.

4. **TLB functionality**: Understand how TLB works as a cache for page table entries. Remember that TLB hits avoid page table access entirely, significantly improving performance.

5. **Real-world examples**: Mention specific operating systems where applicable. For instance, Linux uses a four-level page table on 64-bit systems, while early versions of x86 used two-level hierarchies.

6. **Page replacement connection**: The dirty and reference bits in PTEs are directly used by page replacement algorithms like LRU and clock algorithm. Understand how these bits are updated and cleared.

7. **Trade-offs matter**: When answering comparison questions, focus on memory usage vs. access time trade-offs. Flat page tables are simple but waste memory; hierarchical tables reduce memory usage but increase access time due to multiple memory lookups.

8. **Protection mechanisms**: Know how protection bits work and their role in preventing unauthorized access. Understand the difference between valid/invalid (page presence) and protection (access rights).

9. **Numericals**: Be prepared for calculations involving page table size, number of entries, and address translation. These are scoring questions if you show all steps clearly.

10. **Current relevance**: Understand that page table structures continue to evolve. Modern processors support larger pages (huge pages/1GB pages) to reduce TLB pressure and page table overhead for large workloads.