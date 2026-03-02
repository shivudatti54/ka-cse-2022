# Structure of Page Table

## Introduction

Memory management is a fundamental aspect of modern operating systems, and virtual memory has revolutionized how programs access memory by providing the illusion of a larger, contiguous address space. At the heart of virtual memory implementation lies the page table, a crucial data structure that maps virtual addresses to physical addresses. Understanding the structure of page tables is essential for comprehending how operating systems achieve memory protection, sharing, and efficient allocation.

In a paged memory management system, the physical memory is divided into fixed-size frames, while the logical address space is divided into pages of equal size. The page table serves as the translation mechanism between these two address spaces. Without an efficient and well-structured page table, the overhead of address translation would severely degrade system performance. As systems have grown more complex with larger address spaces, the structure of page tables has evolved to address challenges of space efficiency, access speed, and scalability.

This topic explores the internal structure of page table entries, various page table organizations, and the trade-offs involved in choosing different implementations. For students preparing for DU examinations, a thorough understanding of page table structure is crucial as it forms the foundation for advanced topics like page replacement algorithms, thrashing, and memory protection mechanisms.

## Key Concepts

### Page Table Entry Structure

A page table is essentially an array of page table entries (PTEs), where each entry corresponds to one virtual page. The structure of a PTE contains several critical fields that enable efficient and secure memory management.

The most fundamental component of a PTE is the frame number, which indicates the physical memory frame where the corresponding virtual page resides. In a system with physical memory of size 2^m bytes and page size of 2^n bytes, the frame number requires (m - n) bits. This field provides the physical address component needed for address translation.

The valid-invalid bit is a critical flag that indicates whether a particular virtual page is currently present in physical memory. When this bit is set to "valid," it means the page is resident in memory and the rest of the PTE contains meaningful translation information. When set to "invalid," it indicates either that the page has not been allocated or that it has been swapped out to secondary storage. When an invalid page is accessed, the hardware triggers a page fault, prompting the operating system to bring the required page into memory.

The protection bits specify the types of access permitted to the corresponding page. Typically, these bits encode read, write, and execute permissions. For instance, a three-bit protection field can represent different combinations: read-only, read-write, read-execute, or no access. These bits enable the operating system to enforce memory protection policies and prevent unauthorized access to memory regions.

The referenced bit, also known as the accessed bit, is set by the hardware whenever a page is accessed (either read from or written to). This bit is crucial for page replacement algorithms like the Clock algorithm, as it helps identify pages that have been recently used. The operating system periodically clears this bit to track page access patterns over time.

The modified bit, or dirty bit, indicates whether the page has been modified since it was last loaded into memory. This information is vital when a page needs to be evicted from memory. If the modified bit is set, the page must be written back to secondary storage before the frame can be reused. If the bit is clear, the frame can be simply overwritten without saving its contents, significantly reducing I/O overhead.

### Types of Page Table Organizations

The simplest form of page table is a single-level or linear page table, where entries are stored in a contiguous array indexed by the page number. While conceptually straightforward, this approach becomes problematic for large address spaces. For example, in a 32-bit system with 4KB pages, the page number requires 20 bits, meaning the page table would contain 2^20 (approximately one million) entries. If each entry is 4 bytes, the page table itself would occupy 4MB of memory—a significant overhead, especially when multiple processes are running.

To address the space inefficiency of single-level page tables, hierarchical paging was developed. In this approach, the page number is divided into multiple parts, with each part indexing into a separate level of the page table. The most common implementation is the two-level page table, where the page number is split into a page directory index and a page table index. The top-level page directory always remains in memory, while second-level page tables can be allocated on demand. This sparse allocation significantly reduces memory overhead for processes that do not use their entire address space.

For 64-bit address spaces, even two-level hierarchies become insufficient. Modern systems employ multi-level page tables, such as the four-level page table structure used in x86-64 architectures. Each level of the hierarchy adds complexity but provides finer granularity of allocation, ensuring that only necessary portions of the page table hierarchy occupy physical memory.

Inverted page tables represent a fundamentally different approach to page table organization. Instead of maintaining one entry per virtual page, an inverted page table maintains one entry per physical frame. Each entry contains information about which virtual page currently occupies that frame. While this approach dramatically reduces the memory required for page tables in systems with large address spaces, it introduces challenges in implementing shared memory and can create performance bottlenecks due to the need to search the entire table during address translation.

Hashed page tables provide another alternative, particularly useful for large address spaces. Virtual page numbers are hashed to create an index into a hash table. Each bucket in the hash table contains a chain of page table entries that hash to the same location. This approach efficiently handles sparse address spaces where only a small fraction of virtual pages are in use.

### Associative Memory and Translation Lookaside Buffers

Direct page table lookup for every memory access would introduce unacceptable performance overhead. To accelerate address translation, hardware support for associative memory, specifically Translation Lookaside Buffers (TLBs), is employed. A TLB is a special cache that stores recent virtual-to-physical address translations.

When a virtual address needs translation, the system first checks the TLB. If the translation is found (a TLB hit), the physical address is obtained immediately without accessing the page table. If the translation is not present (a TLB miss), the system must access the page table to obtain the translation, and this mapping is then stored in the TLB for future use.

TLB effectiveness depends on locality of reference. Temporal locality ensures that recently accessed pages are likely to be accessed again, while spatial locality suggests that nearby addresses will be accessed soon. Typical TLB hit rates exceed 90% in well-behaved programs, making them essential for maintaining reasonable memory access performance.

## Examples

**Example 1: Calculating Page Table Size for Single-Level Paging**

Consider a system with a 32-bit logical address space and page size of 4KB. Determine the size of a single-level page table assuming each page table entry is 4 bytes.

Solution:
Page size = 4KB = 2^12 bytes, so offset bits = 12
Logical address bits = 32, so virtual page number bits = 32 - 12 = 20
Number of virtual pages = 2^20 = 1,048,576
Page table entry size = 4 bytes
Page table size = 1,048,576 × 4 = 4,194,304 bytes = 4MB

This calculation demonstrates the memory overhead problem with single-level paging for large address spaces.

**Example 2: Two-Level Page Table Structure**

Given a system with 32-bit addresses, page size of 4KB, and page table entries of 4 bytes, design a two-level page table and calculate memory saved compared to single-level paging, assuming only 256 second-level page tables are needed.

Solution:
With 4KB pages, offset = 12 bits
For two-level paging with 10 bits at each level:
Outer page (page directory): 2^10 entries = 1024 entries
Each second-level page table: 2^10 entries = 1024 entries

Memory for page directory: 1024 × 4 = 4KB
Memory for 256 second-level tables: 256 × 4KB = 1024KB = 1MB
Total: 4KB + 1MB ≈ 1.008MB

Compared to single-level: 4MB - 1.008MB ≈ 3MB saved (75% reduction)

This example illustrates how hierarchical paging dramatically reduces memory requirements when address space utilization is sparse.

**Example 3: Interpreting Page Table Entry Bits**

A page table entry contains the following binary information (starting from MSB):
1 (valid bit) | 0 (modified bit) | 1 (referenced bit) | 00 (protection bits) | 00000000001101001010 (frame number)

Assume page size is 4KB and the entry is 32 bits. Determine the page protection, whether the page is dirty, and calculate the physical address if the virtual offset is 0xABC.

Solution:
Valid bit = 1: Page is resident in memory
Modified bit = 0: Page has not been modified
Referenced bit = 1: Page has been accessed
Protection bits = 00: Typically indicates no access or read-only

Frame number in binary = 00000000001101001010 = 0x00CA (in decimal: 202)
Physical address = Frame number × Page size + Offset
= 202 × 4096 + 0xABC
= 202 × 4096 + 2748
= 827392 + 2748 = 830140
In hex: 0x000C A6C

## Exam Tips

For DU semester examinations, several key points regarding page table structure frequently appear in exams. Understanding these concepts thoroughly will help secure good marks.

First, always remember the basic address translation formula: Physical Address = Frame Number × Page Size + Offset. This formula is fundamental and frequently tested in numerical problems. When solving such problems, clearly identify the number of bits for page number and offset based on the given page size.

Second, the trade-offs between different page table organizations are important. Single-level page tables are simple but waste space for sparse address spaces. Hierarchical page tables save space but introduce additional memory accesses during translation. Inverted page tables save enormous space but complicate shared memory implementation. Be prepared to explain when each approach is suitable.

Third, the various bits in a page table entry serve specific purposes and their understanding is crucial. The valid bit controls page fault generation, the modified bit determines if page replacement requires disk write, the referenced bit aids page replacement algorithms, and protection bits enforce memory security. Understand the interaction between these bits during page fault handling and page replacement.

Fourth, TLB hit rate significantly impacts effective memory access time. The effective access time formula is: EAT = Hit_Rate × TLB_Access_Time + (1 - Hit_Rate) × (TLB_Access_Time + Memory_Access_Time). Be prepared to calculate this for different hit rates.

Fifth, hierarchical page table design depends on the address space size and page table entry size. For a 32-bit address space with 4KB pages and 4-byte PTEs, two levels are sufficient. For larger address spaces, additional levels become necessary. Understand how to calculate the number of bits at each level.

Sixth, remember that page tables are stored in physical memory and their addresses are stored in special registers (like page table base register in x86). The CPU uses these registers to locate the page table during address translation. Any change to these registers requires care to avoid invalid translations.

Seventh, in inverted page tables, the search time can become a bottleneck. Hashing is often used to improve search performance. Understanding the hash function and collision resolution mechanisms in hashed page tables is important for advanced questions.