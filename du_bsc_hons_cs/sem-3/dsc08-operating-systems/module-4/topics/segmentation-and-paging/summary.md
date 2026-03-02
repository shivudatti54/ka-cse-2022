# Segmentation And Paging — Quick Revision Notes

**Subject:** Operating Systems | **Course:** BSc (Hons) Computer Science (DU NEP 2024)

---

### Introduction

Memory management is a critical function of any operating system that optimizes the allocation and access of physical memory. Two fundamental techniques used for this purpose are **Segmentation** and **Paging**. While segmentation provides a logical view of memory based on program structures, paging ensures efficient physical memory utilization by eliminating external fragmentation.

---

### 1. Segmentation

*   **Concept**: Divides a program into variable-sized logical segments (e.g., code, data, stack, heap).
*   **Logical Address**: Consists of a **Segment Number** and an **Offset**.
*   **Segment Table**: Maps segment numbers to their **base address** (starting location) and **limit** (length) in physical memory.
*   **Translation**: OS adds the offset to the segment base to generate the physical address.
*   **Advantages**:
    *   Reflects natural program structure.
    *   Simplifies protection (each segment can have distinct permissions).
    *   Enables sharing of specific segments (e.g., shared code).
    *   Eliminates internal fragmentation within segments.

---

### 2. Paging

*   **Concept**: Divides both physical and logical memory into fixed-size blocks called **Frames** and **Pages** respectively.
*   **Logical Address**: Consists of a **Page Number** and an **Offset**.
*   **Page Table**: Maps page numbers to frame numbers. It is stored in main memory.
*   **Translation**: The page number indexes the page table to find the frame number; the offset is added to the frame number to get the physical address.
*   **Advantages**:
    *   **Eliminates external fragmentation** completely.
    *   Simple and efficient memory allocation.
    *   Facilitates virtual memory implementation.
*   **Disadvantage**: Introduces internal fragmentation (unused space in the last page).

---

### 3. Combined Segmentation and Paging

This hybrid approach leverages the benefits of both methods.

*   **Process**: The logical address is first interpreted as a **Segment Number + Offset**.
*   **Segment Table Lookup**: The offset is divided into a **Page Number** and **Page Offset**.
*   **Page Table Lookup**: The page number indexes the segment's page table to find the physical frame.
*   **Physical Address**: The frame number is combined with the page offset.
*   **Benefit**: Provides protection and logical structure (segmentation) along with efficient memory management (paging).

---

### 4. Key Differences (Exam Focus)

| Feature | Segmentation | Paging |
| :--- | :--- | :--- |
| **Size** | Variable | Fixed |
| **View** | Logical/Physical | Physical/Logical |
| **Fragmentation** | External | Internal |
| **Address** | (Segment, Offset) | (Page, Offset) |

---

### Conclusion

Segmentation and paging are essential techniques for implementing memory management in modern operating systems. While segmentation organizes memory according to program logic, paging ensures efficient utilization of physical RAM. Understanding their mechanisms, advantages, and differences is crucial for grasping how OSes manage memory virtually— a core topic in the Delhi University syllabus.