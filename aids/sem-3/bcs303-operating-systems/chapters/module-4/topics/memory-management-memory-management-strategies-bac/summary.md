# Memory Management: Memory Management Strategies: Background

==============================================

## Key Concepts

---

- **Memory Management**: The process of managing the allocation and deallocation of memory in a computer system.
- **Memory Hierarchy**: A layered structure of memory, with different levels having varying sizes and speeds of access.

## Important Definitions

---

- **Virtual Memory**: The combination of physical RAM and hard disk storage used to extend the address space of a program.
- **Paging**: The division of memory into fixed-size blocks called pages.
- **Swapping**: The transfer of pages from RAM to hard disk storage when memory is low.

## Theoretical Background

---

- **Thompson's Thesis**: A fundamental theorem in operating system design, which states that there are three essential components of an operating system: memory management, file management, and process management.
- **Paged Memory Model**: A memory model where the program's address space is divided into fixed-size pages, and the operating system uses a page table to manage the mapping of virtual addresses to physical addresses.
- **Segmented Memory Model**: A memory model where the program's address space is divided into fixed-size segments, and the operating system uses a segment table to manage the mapping of virtual addresses to physical addresses.

## Memory Management Strategies

---

- **Paging**: A technique used to divide the memory into fixed-size blocks called pages, and to transfer pages from RAM to hard disk storage when memory is low.
- **Segmentation**: A technique used to divide the memory into fixed-size blocks called segments, and to use a segment table to manage the mapping of virtual addresses to physical addresses.
- **Relocation**: A technique used to move a program's code and data to different addresses in memory without changing the program's binary instructions.

## Important Formulas and Equations

---

- **Page Fault Equation**: `P = (v - p) * S`, where P is the number of page faults, v is the number of virtual pages, p is the number of physical pages, and S is the number of pages per segment.
- **Segmentation Formula**: `S = (v - s) * P`, where S is the number of segments, v is the number of virtual segments, s is the number of segments per page, and P is the number of pages per segment.

## Important Theorems

---

- **Thompson's Thesis Theorem**: A fundamental theorem in operating system design, which states that there are three essential components of an operating system: memory management, file management, and process management.
- **Paged Memory Theorem**: A theorem that states that the number of page faults is proportional to the number of virtual pages, the number of physical pages, and the number of pages per segment.
