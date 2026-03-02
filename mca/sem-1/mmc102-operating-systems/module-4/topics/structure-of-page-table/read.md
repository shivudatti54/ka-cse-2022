# Structure Of Page Table


## Table of Contents

- [Structure Of Page Table](#structure-of-page-table)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Basics of Page Tables](#basics-of-page-tables)
  - [Single-Level Page Table](#single-level-page-table)
  - [Multi-Level Page Tables](#multi-level-page-tables)
  - [Inverted Page Table](#inverted-page-table)
  - [Hash Page Tables](#hash-page-tables)
  - [Frame Tables](#frame-tables)
- [Examples](#examples)
  - [Example 1: Two-Level Page Table Address Translation](#example-1-two-level-page-table-address-translation)
  - [Example 2: Memory Overhead Comparison](#example-2-memory-overhead-comparison)
  - [Example 3: Inverted Page Table Lookup](#example-3-inverted-page-table-lookup)
- [Exam Tips](#exam-tips)

## Introduction

Memory management is a fundamental aspect of modern operating systems, and virtual memory is the cornerstone technique that enables systems to provide the illusion of a larger, contiguous address space than physically available. At the heart of virtual memory implementation lies the page table—a critical data structure that maintains the mapping between virtual addresses used by processes and the corresponding physical addresses in main memory. Understanding the structure of page tables is essential for comprehending how operating systems achieve memory protection, sharing, and efficient utilization.

The page table serves as the translation mechanism that the Memory Management Unit (MMU) consults during every memory access. Without an efficient page table structure, the overhead of address translation would severely degrade system performance. As computer systems evolved, various page table structures emerged to address different challenges: the need to handle large address spaces, minimize memory consumption by page tables themselves, and accelerate translation lookups. This topic explores the fundamental structures of page tables, their implementations, trade-offs, and real-world applications in contemporary operating systems.

## Key Concepts

### Basics of Page Tables

A page table is a data structure maintained by the operating system that stores page table entries (PTEs). Each PTE contains essential information including the frame number where the corresponding virtual page resides in physical memory, status bits (valid/invalid, dirty, referenced), and protection bits (read, write, execute permissions). The MMU uses the virtual page number (VPN) extracted from the virtual address as an index into the page table to retrieve the corresponding PTE.

The page table is itself stored in main memory, and the MMU contains a dedicated register called the Page Table Base Register (PTBR) that points to the starting address of the current process's page table. Every memory access requires two memory operations: one to fetch the PTE from the page table and another to access the actual data—a significant overhead that motivated the design of the Translation Lookaside Buffer (TLB), a hardware cache for recently used PTEs.

### Single-Level Page Table

The simplest approach to page table organization is a single-level or linear page table. In this design, a single array of PTEs is indexed directly by the virtual page number. For a 32-bit virtual address space with 4KB pages, the page table would contain 2^20 (approximately one million) entries. Each PTE might require 4 bytes, resulting in a page table size of 4MB per process—a substantial memory overhead, especially when multiple processes run simultaneously.

The fundamental problem with single-level page tables is internal fragmentation of the page table itself and the requirement that the entire page table must remain resident in memory regardless of whether a process uses all its virtual pages. For large address spaces, this approach becomes impractical. Unix systems historically used a single-level page table design but had to implement complex memory management to handle the overhead.

### Multi-Level Page Tables

To address the limitations of single-level page tables, hierarchical or multi-level page tables were developed. The most common implementation is the two-level page table, where the first-level page table (called the page directory) points to second-level page tables, each of which contains actual page table entries. The virtual address is divided into three components: an offset into the page directory, an index into the second-level page table, and the page offset.

The key advantage of this hierarchical structure is that only those second-level page tables that correspond to used virtual address ranges need to be allocated in memory. If a process uses only a small portion of its virtual address space, only a few second-level tables are required, significantly reducing memory consumption. The page directory itself must always be present, but it is much smaller than a full single-level table.

Modern 64-bit systems extend this concept further with four-level or five-level page tables. For example, the x86-64 architecture uses a four-level page table hierarchy: PML4 (Page Map Level 4), PDPT (Page Directory Pointer Table), PD (Page Directory), and PT (Page Table). This hierarchical design allows systems to support massive virtual address spaces (up to 256 TB in x86-64) while maintaining reasonable memory overhead for page tables.

### Inverted Page Table

An inverted page table represents a fundamentally different approach to virtual memory mapping. Rather than maintaining one entry per virtual page, an inverted page table contains one entry per physical frame. Each entry stores information about which virtual page currently occupies that physical frame—including the owning process identifier and the virtual page number. This structure dramatically reduces the memory required to store page table information, especially for systems with large physical memories.

The challenge with inverted page tables lies in address translation. Since entries are indexed by physical frame number rather than virtual page number, the MMU must search through the inverted table to find the mapping for a given virtual address. This lookup is typically performed using hashing to improve search performance. IBM's AIX and IBM i operating systems are prominent examples of systems using inverted page tables.

### Hash Page Tables

Hashed page tables provide a middle ground between traditional page tables and inverted tables. In a hashed page table, virtual page numbers are hashed to produce an index into a hash table. Each bucket in the hash table contains a chain of page table entries that hash to the same location. The MMU hashes the virtual page number, traverses the corresponding chain, and locates the matching entry to obtain the physical frame number.

This approach efficiently handles sparse address spaces where processes use widely scattered virtual addresses. The memory overhead is proportional to the number of active virtual pages rather than the total virtual address space. However, hash collisions can degrade performance, and the chained structure introduces additional latency during translation. Some implementations use clustered page tables where each entry stores mappings for multiple adjacent pages to reduce the number of entries.

### Frame Tables

While not strictly a page table structure, frame tables are essential companions to page table implementations. A frame table contains one entry per physical memory frame, storing information such as whether the frame is allocated, which process and virtual page currently owns it, and whether the frame has been modified (is dirty). Frame tables are crucial for page replacement algorithms, enabling the operating system to identify victim frames when physical memory becomes full.

## Examples

### Example 1: Two-Level Page Table Address Translation

Consider a system with the following parameters: 32-bit virtual addresses, 4KB page size (12-bit offset), and a two-level page table where the first 10 bits index the page directory and the next 10 bits index the second-level page table.

Given virtual address 0x12345678, perform address translation:

1. Extract offset: Lower 12 bits = 0x678 = 1656
2. Extract second-level index: Bits 12-21 = 0x345 >> 0xD5 = 213
3. Extract first-level index: Bits 22-31 = 0x123 >> 0x048 = 72

The MMU uses index 72 to access entry 72 in the page directory, which points to a second-level page table. It then uses index 213 to access entry 213 in that second-level page table, retrieving the frame number. Finally, the physical address is constructed by concatenating the frame number with the offset.

### Example 2: Memory Overhead Comparison

Compare memory overhead for mapping 256 MB of virtual memory using 4 KB pages under different page table structures. Assume each PTE is 4 bytes.

For single-level: Number of virtual pages = 256 MB / 4 KB = 65536 pages. Page table size = 65536 × 4 bytes = 256 KB

For two-level with process using only 8 MB (2048 pages): 
- Page directory: 1024 entries × 4 bytes = 4 KB
- Second-level tables: 2 tables × 1024 entries × 4 bytes = 8 KB (only 2 second-level tables needed)
- Total: 12 KB (compared to 256 KB)

This example demonstrates how multi-level page tables achieve substantial memory savings for sparse address spaces.

### Example 3: Inverted Page Table Lookup

Consider a system with 1024 physical frames and an inverted page table. When process P1 accesses virtual page 2000, the MMU must locate which physical frame holds this page.

The system computes a hash of (process_id, virtual_page) = (P1, 2000) to obtain an index into the hash table. The hash table entry points to a bucket in the inverted page table. The MMU scans the bucket, comparing each entry's process ID and virtual page number until finding a match. When found, the frame number (say, frame 512) is retrieved, and the physical address is constructed as (frame 512 × 4096) + offset.

This lookup requires multiple memory accesses in the worst case, explaining why TLB hit rates are critical for systems using inverted page tables.

## Exam Tips

1. Understand that page tables are software structures managed by the OS but accessed hardware for translation; PTBR register holds the base address of the current page table.

2. Remember the fundamental trade-off: single-level tables are fast but consume excessive memory, while hierarchical tables save memory at the cost of additional memory accesses during translation.

3. For hierarchical page tables, always remember that the top-level table (page directory) must always be resident in memory, while lower-level tables can be paged out.

4. Inverted page tables index by physical frame number, not virtual page number—this is a crucial distinction from traditional page tables.

5. The TLB (Translation Lookaside Buffer) is a hardware cache that stores recent virtual-to-physical translations and is critical for hiding the performance overhead of page table access.

6. Page table entries typically contain: valid/invalid bit, frame number, protection bits (read/write/execute), dirty bit, and reference/accessed bit.

7. For exam questions involving address translation, always start by determining the number of bits for offset, page number, and any page table indexes based on the given parameters.

8. Multi-level page tables introduce additional page faults because of the extra levels—failure to allocate any level of the page table results in a page fault that the OS must handle.

9. The x86-64 architecture uses 4-level paging (PML4 → PDPT → PD → PT) and can support up to 48-bit virtual addresses in current implementations.