# Structure of Page Table

=====================================

## Introduction

---

In this section, we will discuss the structure of page tables, which is a crucial concept in operating system design. Page tables are used to map virtual addresses to physical addresses in a computer system.

## What is a Page Table?

---

A page table is a data structure that maps a set of virtual addresses to a set of physical addresses. It is used to translate virtual addresses into physical addresses, allowing the operating system to manage memory efficiently.

### Page Table Structure

A page table typically consists of the following components:

### Virtual Page Number (VPN)

- A 32-bit (or 64-bit) value that represents the virtual page number.

### Page Table Entry (PTE)

- A 64-bit (or 32-bit) value that represents the physical address of a page.
- Typically consists of three fields:
  - **Base Address** (12 bits or 64 bits): the base address of the page.
  - **Page Size** (12 bits or 64 bits): the size of the page.
  - **Present** (1 bit): a flag indicating whether the page is present in RAM.

### Page Directory Entry (PDE)

- A 32-bit (or 64-bit) value that represents the address of a page table.
- Typically consists of four fields:
  - **Page Frame Number** (12 bits or 64 bits): the frame number of the page table entry.
  - **Page Table Offset** (10 bits or 32 bits): the offset of the page table entry within the page directory.
  - **Page Table Type** (2 bits or 4 bits): the type of page table (e.g., unified, indexed, or split).
  - **Present** (1 bit): a flag indicating whether the page table is present.

## Page Table Types

---

There are several types of page tables, including:

- **Unified Page Table**: maps all virtual addresses to a single physical address space.
- **Indexed Page Table**: maps virtual addresses to physical addresses using an index.
- **Split Page Table**: divides the page table into two parts: a directory and a table.

## Example

---

Here is an example of a page table structure:

| Virtual Page Number (VPN) | Page Table Entry (PTE)                                   |
| ------------------------- | -------------------------------------------------------- |
| 00000000                  | 0100000000000000 (Base Address: 0x1000, Page Size: 4096) |
| 00000001                  | 0100000100000000 (Base Address: 0x2000, Page Size: 4096) |
| ...                       | ...                                                      |

| Page Directory Entry (PDE) |
| -------------------------- | ------------------------------------------------------------------------------------------------------- |
| 00000000                   | 0001000000000000 (Page Frame Number: 0x100, Page Table Offset: 0, Page Table Type: Unified, Present: 1) |
| 00000001                   | 0001000100000000 (Page Frame Number: 0x200, Page Table Offset: 4, Page Table Type: Unified, Present: 1) |
| ...                        | ...                                                                                                     |

## Summary

---

In this section, we discussed the structure of page tables, including the virtual page number, page table entry, and page directory entry. We also covered different types of page tables and provided an example of a page table structure.

### Key Concepts:

- Virtual page number (VPN)
- Page table entry (PTE)
- Page directory entry (PDE)
- Unified page table
- Indexed page table
- Split page table
