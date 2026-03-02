# **Structure of Page Table Revision Notes**

## **Chapter 8: Page Tables (8.1-8.8)**

- **Definition:** A page table is a data structure used in operating systems to manage virtual memory.
- **Components:**
  - Page Table Entry (PTE): a table entry that maps a virtual page to a physical frame
  - Page Directory: a data structure that contains a set of PTEs
  - Page Table Base Address: the base address of the page table
- **Structure:**
  - Page Tables: a separate memory space for each process, mapped to a page directory
  - Page Directory: a linear array of PTEs, each mapping a 4KB page to a physical frame
- **Page Table Entries (PTEs):**
  - Format: `(virtual_address, page_frame_number)`
  - Fields: `virtual_address` and `page_frame_number`

## **Chapter 9: Memory Management (9.1-9.4)**

- **Definition:** Memory management refers to the process of managing a computer's memory, including allocation, deallocation, and protection.
- **Theorem:** **Cache Invalidation**
  - If a cache line is replaced, the replaced line must be removed from the cache
- **Formula:** `M = (P \* V) / (P + V)`
  - where `M` is the memory size, `P` is the page size, and `V` is the number of pages
- **Types of Memory Protection:**
  - **Page Protection:** protects each page individually
  - **Segment Protection:** protects each segment individually
