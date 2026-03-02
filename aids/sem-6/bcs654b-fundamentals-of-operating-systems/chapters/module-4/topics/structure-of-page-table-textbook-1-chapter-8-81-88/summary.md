# **Structure of Page Table**

### Chapter 8: Page Table Basics

- **Page Table**: A data structure that maps virtual page numbers to physical frame numbers in memory.
- **Page Table Entry (PTE)**: A single entry in the page table that contains:
  - Virtual page number (VPN)
  - Physical frame number (PFN)
  - Page protection bits (e.g., read-only, write-only)
- **Page Table Organization**: Typically stored in main memory, often in a contiguous block.
- **Page Table Walk**: A process of traversing the page table to resolve a virtual address.

### Chapter 9: Page Table Operations

- **Page Fault**: An event that occurs when the operating system encounters a virtual address that is not in memory.
- **Page Fault Handling**: The process of handling page faults, including:
  - **Page Replacement**: Replacing a page in memory to accommodate the new page.
  - **Page Refill**: Refilling a page from disk storage.
- **Page Table Updates**: Updating the page table entries after a page fault.

### Important Formulas and Definitions

- **Page Fault Rate**: The number of page faults per unit time.
- **Page Replacement Algorithm**: An algorithm used to select the page to replace in memory, e.g., First-In-First-Out (FIFO), Least Recently Used (LRU).
- **Page Table Size**: The number of entries in the page table.

### Important Theorems

- **Thompson's Page Replacement Algorithm**: A page replacement algorithm that minimizes the average number of page faults.
