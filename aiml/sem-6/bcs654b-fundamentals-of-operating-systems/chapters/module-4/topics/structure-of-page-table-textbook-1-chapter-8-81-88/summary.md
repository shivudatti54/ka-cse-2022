# **Structure of Page Table Revision Notes**

**Chapter 8: Page Table Structure (8.1-8.8)**

- **Page Table**: A data structure used in operating systems to store the memory addresses of pages in physical memory.
- **Page Table Entry (PTE)**: A single entry in the page table, containing information about a page, such as its virtual address, physical address, and permissions.
- **Page Table Organization**: The page table is usually divided into two levels:
  - **Page Table Index (PTI)**: Maps virtual page numbers to physical frame numbers.
  - **Page Table (PT)**: Stores the PTEs.

**Chapter 9: Page Table Operations (9.1-9.4)**

- **Page Fault**: An event where a process tries to access a page that is not in physical memory.
- **Page Replacement Policy**: A strategy used to replace a page from physical memory when a new page fault occurs.
- **Page Replacement Algorithms**:
  - **First-In-First-Out (FIFO)**
  - **Least Recently Used (LRU)**
  - **Optimal**
- **Translation Lookaside Buffer (TLB)**: A cache used to store recently accessed page table entries to improve page fault performance.

**Important Formulas and Definitions**

- **Frame Number (FN)**: The physical frame number that contains a page.
- **Page Fault Rate (PFR)**: The number of page faults per unit time.

**Key Concepts**

- Page table structure and organization
- Page table operations (page faults, page replacement policies, algorithms)
- Translation Lookaside Buffer (TLB)

**Theorem:**

- If a process is in a valid state and has a valid page table, then it can access any page in physical memory.
