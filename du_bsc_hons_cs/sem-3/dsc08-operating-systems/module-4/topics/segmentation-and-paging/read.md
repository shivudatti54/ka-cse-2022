# Segmentation and Paging: Comprehensive Study Material

## Operating Systems — BSc (Hons) Computer Science, Delhi University (NEP 2024 UGCF)

---

## Table of Contents

1. [Introduction and Real-World Relevance](#1-introduction-and-real-world-relevance)
2. [Memory Management: The Problem Context](#2-memory-management-the-problem-context)
3. [Segmentation](#3-segmentation)
4. [Paging](#4-paging)
5. [Combined Segmentation and Paging](#5-combined-segmentation-and-paging)
6. [Page Table Structures](#6-page-table-structures)
7. [Translation Lookaside Buffer (TLB)](#7-translation-lookaside-buffer-tlb)
8. [Address Translation: Worked Examples](#8-address-translation-worked-examples)
9. [Page Replacement Algorithms](#9-page-replacement-algorithms)
10. [Memory Protection](#10-memory-protection)
11. [Key Takeaways](#11-key-takeaways)
12. [Multiple Choice Questions](#12-multiple-choice-questions)
13. [Flashcards](#13-flashcards)

---

## 1. Introduction and Real-World Relevance

Memory management is the heart of any modern operating system. As computer science students at Delhi University, understanding **Segmentation and Paging** is crucial because these are fundamental techniques that operating systems use to manage physical memory efficiently while providing each process with the illusion of a large, contiguous address space.

In real-world computing, when you run multiple applications on your computer—whether it's a web browser, a code editor, or a music player—each application believes it has exclusive access to the entire memory. This illusion is made possible through memory management techniques like segmentation and paging.

### Why This Matters for DU Students

This topic carries significant weight in the Delhi University BSc (Hons) Computer Science curriculum under the Operating Systems paper (Paper III: Operating Systems and Computer Networks). Questions on address translation, page table structures, and page replacement algorithms frequently appear in semester examinations.

### Learning Objectives

By the end of this study material, you will be able to:
- Explain the differences between segmentation and paging
- Perform address translation calculations for both schemes
- Describe multilevel page tables and inverted page tables
- Analyze the role of TLB in hardware performance
- Evaluate different page replacement algorithms
- Understand memory protection mechanisms

---

## 2. Memory Management: The Problem Context

Before diving into segmentation and paging, let's understand the problems they solve:

### 2.1 The Memory Management Problem

Physical RAM is a limited resource (e.g., 8GB, 16GB), but processes need:
- **Contiguous memory**: Many programs expect their code and data to be in consecutive memory locations
- **Isolation**: One process should not access another's memory
- **Efficiency**: Memory should not be wasted
- **Virtual Memory**: Programs should be able to use more memory than physically available

### 2.2 Historical Evolution

| Approach | Era | Key Feature |
|----------|-----|-------------|
| Contiguous Allocation | Early | Simple but causes external fragmentation |
| Segmentation | 1970s | Logical view matches programmer's perspective |
| Paging | 1970s | Fixed-size pages eliminate external fragmentation |
| Combined | Modern | Best of both worlds |

---

## 3. Segmentation

### 3.1 Concept Overview

**Segmentation** is a memory management technique that divides a program's address space into logically meaningful units called **segments**. Each segment represents a natural division of the program, such as:

- **Code Segment**: The executable instructions
- **Data Segment**: Global and static variables
- **Stack Segment**: Function calls, local variables
- **Heap Segment**: Dynamically allocated memory

Unlike paging (which divides memory into fixed-size chunks), segmentation divides memory based on **logical meaning**.

### 3.2 Key Properties of Segments

```
┌─────────────────────────────────────────┐
│           LOGICAL ADDRESS               │
├──────────────┬──────────────────────────┤
│  Segment     │    Offset (Displacement) │
│  Number (s)  │         (d)              │
└──────────────┴──────────────────────────┘
```

- **Segment Number**: Identifies which segment (0 = code, 1 = data, etc.)
- **Offset**: Location within that segment
- Each segment has a **segment table** entry containing:
  - **Base Address**: Starting physical address
  - **Limit (Length)**: Size of the segment

### 3.3 Address Translation in Segmentation

The translation from logical to physical address follows this formula:

```
Physical Address = Base[Segment Number] + Offset
```

**Validation Check**: The system must verify that `Offset < Limit` to prevent accessing memory outside the segment.

### 3.4 Example: Segmentation Address Translation

**Example 1: Simple Translation**

Consider a system with the following segment table:

| Segment | Base (Decimal) | Limit (Length) |
|---------|----------------|----------------|
| 0 (Code)| 1000           | 500            |
| 1 (Data)| 2000           | 1000           |
| 2 (Stack)| 4000          | 800            |

**Given Logical Address**: Segment = 1, Offset = 450

**Solution**:
- Segment 1's base = 2000
- Segment 1's limit = 1000
- Offset (450) < Limit (1000) ✓ Valid
- Physical Address = 2000 + 450 = **2450**

**Example 2: Invalid Address Detection**

**Given Logical Address**: Segment = 2, Offset = 900

**Solution**:
- Segment 2's base = 4000
- Segment 2's limit = 800
- Offset (900) > Limit (800) ✗ **Invalid**
- This generates a **segmentation fault** (trap to OS)

### 3.5 Advantages of Segmentation

1. **Logical Transparency**: Programmers think in terms of logical units (code, data, stack)
2. **Easy Sharing**: Segments can be shared between processes (e.g., shared libraries)
3. **Variable Size**: Each segment can grow/shrink independently
4. **Protection**: Different segments can have different access rights (read-only code, read-write data)

### 3.6 Disadvantages of Segmentation

1. **External Fragmentation**: Free memory exists in variable-sized chunks, leading to inefficient use
2. **Complex Memory Allocation**: Finding suitable holes for segments is computationally expensive
3. **Overhead**: Segment tables consume memory and CPU time

---

## 4. Paging

### 4.1 Concept Overview

**Paging** is a memory management technique that eliminates external fragmentation by dividing both physical memory and logical address space into fixed-size blocks called **pages** (logical) and **frames** (physical).

### 4.2 Key Terminology

| Term | Definition |
|------|------------|
| **Page** | Fixed-size block in logical address space |
| **Frame** | Fixed-size block in physical memory (same size as page) |
| **Page Size** | Typically 4KB, 8KB, or 16KB (power of 2) |
| **Page Table** | Data structure mapping page numbers to frame numbers |
| **Page Fault** | Occurs when a requested page is not in memory |

### 4.3 Address Structure in Paging

```
┌─────────────────┬─────────────────┐
│  Page Number    │    Page Offset  │
│      (p)        │       (d)       │
└─────────────────┴─────────────────┘
     └─ M bits ─┘    └─ N bits ─┘
     
Total bits = M + N = Logical Address Space (typically 32 or 64 bits)
```

- **Page Number (p)**: Index into the page table
- **Page Offset (d)**: Location within the page

**If page size = 2^N bytes, then offset needs N bits**

### 4.4 Page Table Entry (PTE) Structure

Each entry in the page table contains:

| Field | Purpose |
|-------|---------|
| **Frame Number** | Physical frame where the page resides |
| **Valid Bit** | Whether the page is in memory (1) or not (0) |
| **Protection Bits** | Read/Write/Execute permissions |
| **Dirty Bit** | Whether the page has been modified |
| **Reference Bit** | Used for page replacement algorithms |

### 4.5 Address Translation in Paging

```
Physical Address = (Frame Number × Page Size) + Offset
```

### 4.6 Example: Paging Address Translation

**Example: Two-Level Paging Calculation**

Consider a system with:
- Logical Address Space: 32 bits
- Page Size: 4KB = 2^12 bytes
- Physical Memory: 4GB = 2^32 bytes
- Frame Size: Same as page size (4KB)

**Calculations**:
- Offset bits: log₂(4096) = 12 bits
- Number of pages: 2^(32-12) = 2^20 = 1,048,576 pages
- Number of frames: 2^(32-12) = 2^20 frames
- Page table entries needed: 1,048,576

**Given Logical Address**: 0x12345678 (hexadecimal)

**Solution**:
```
Binary: 0001 0010 0011 0100 0101 0110 0111 1000

Offset (d):     0100 0101 0110 0111 1000 (12 bits) = 0x578
Page Number (p): 0001 0010 0011 0100 0101 (20 bits) = 0x12345

If Page 0x12345 maps to Frame 0x9ABC:
Physical Address = (0x9ABC × 4096) + 0x578
                = 0x9ABC000 + 0x578
                = 0x9ABC578
```

---

## 5. Combined Segmentation and Paging

### 5.1 Why Combine Both?

Each approach has limitations when used alone:

| Approach | Problem |
|----------|---------|
| Segmentation Only | External fragmentation, complex allocation |
| Paging Only | No logical meaning, no easy sharing of variable-sized regions |

**Combined approach** gives us the best of both worlds:
- **Segmentation** provides logical organization (code, data, stack)
- **Paging** eliminates external fragmentation within each segment

### 5.2 Address Translation in Combined Scheme

The logical address structure becomes:

```
┌──────────────┬───────────────┬─────────────────┐
│  Segment     │    Page       │    Page Offset  │
│  Number (s)  │  Number (p)   │      (d)        │
└──────────────┴───────────────┴─────────────────┘
```

**Translation Process**:

```
1. Use Segment Number to find Segment Table Entry
2. Check that Offset < Segment Limit (valid segment access)
3. Extract Base Address of the segment
4. Use Page Number to find Page Table Entry (within that segment)
5. Get Frame Number
6. Physical Address = (Frame Number × Page Size) + Offset
```

### 5.3 Example: Combined Segmentation + Paging

**Example: Translation in Combined Scheme**

Consider a system:
- Logical Address: Segment = 2, Page = 1, Offset = 500
- Page Size: 4KB
- Segment Table for Segment 2:
  - Base: 0x10000
  - Limit: 0x3000
- Page Table for Segment 2:
  - Page 0 → Frame 5
  - Page 1 → Frame 12
  - Page 2 → Frame 8

**Solution**:

**Step 1**: Validate segment access
- Offset (500) < Segment Limit (0x3000 = 12288) ✓ Valid

**Step 2**: Find frame
- Page 1 maps to Frame 12

**Step 3**: Calculate physical address
- Frame 12 base = 12 × 4096 = 49152
- Physical Address = 49152 + 500 = 49652

---

## 6. Page Table Structures

### 6.1 Single-Level Page Table

The simplest approach—a linear array indexed by page number.

**Problems**:
- For a 32-bit address space with 4KB pages: 2^20 entries needed
- If each PTE is 4 bytes: 4MB page table per process
- For 100 processes: 400MB just for page tables!

### 6.2 Two-Level Page Table

Hierarchical structure that breaks the page table into smaller chunks.

**Structure**:
```
┌──────────┬──────────┬──────────┐
│  PGD     │  PTE     │  Offset  │
│ (Page    │ (Page    │          │
│ Directory│ Table    │          │
│ Index)   │ Index)   │          │
└──────────┴──────────┴──────────┘
```

**Example: Two-Level Paging**

Given:
- 32-bit logical address
- Page size: 4KB (12 bits offset)
- PTE size: 4 bytes
- Entries per page table: 4KB/4 = 1024 = 2^10

**Address breakdown**:
- PGD Index: 10 bits (top-level page directory)
- PTE Index: 10 bits (second-level page table)
- Offset: 12 bits

**Advantages**:
- Only allocate page tables for valid pages
- Can swap out unused page tables to disk

### 6.3 Inverted Page Table

Instead of one entry per virtual page, we have one entry per physical frame.

**Structure**:
| Frame | PID | Virtual Page Number | Control Bits |
|-------|-----|---------------------|--------------|
| 0     | 5   | 1234               | Valid, R/W   |
| 1     | 3   | 567                | Valid, R/O   |
| ...   |     |                    |              |

**Advantages**:
- Requires only as many entries as physical frames
- Reduces memory overhead significantly

**Disadvantages**:
- Complex lookup (must search entire table or use hashing)
- Difficult to implement shared memory

### 6.4 Example: Inverted Page Table Calculation

**Example: Inverted Page Table Lookup**

Consider a system:
- Physical Memory: 16 frames
- Page/Frame Size: 4KB
- Inverted Page Table entries: 16

**Given**: PID = 5, Virtual Page = 100
**Search**: Find which frame contains this virtual page

```
Inverted Page Table:
[0] PID:2, VPN:50
[1] PID:5, VPN:100  ← Found at Frame 1!
[2] PID:3, VPN:200
[3] PID:5, VPN:101
...
```

**Physical Address Calculation**:
- Frame 1 base = 1 × 4096 = 4096
- If Offset = 0x200 (512), then:
- Physical Address = 4096 + 512 = 4608

---

## 7. Translation Lookaside Buffer (TLB)

### 7.1 The Performance Problem

Every memory access with paging requires TWO memory accesses:
1. First: Access page table to get frame number
2. Second: Access actual data at physical address

This effectively **doubles** memory access time!

### 7.2 TLB Solution

A **Translation Lookaside Buffer (TLB)** is a special high-speed associative cache that stores recent page table entries.

**TLB Structure**:
```
┌──────────────────────────────────────────┐
│           TLB (Hardware Cache)            │
├──────────────┬──────────────┬────────────┤
│   VPN        │    PFN       │  Protection│
├──────────────┼──────────────┼────────────┤
│   0x1234     │   0x56       │    R/W     │
│   0x5678     │   0x9A       │    R/O     │
│   ...        │   ...        │   ...      │
└──────────────┴──────────────┴────────────┘
```

### 7.3 TLB Address Translation Process

```
1. Extract Virtual Page Number from logical address
2. Search TLB for matching VPN
   ├── IF FOUND (TLB Hit):
   │   └── Get Frame Number from TLB
   │   └── Calculate Physical Address
   │   └── Access memory (1 memory access)
   │
   └── IF NOT FOUND (TLB Miss):
       └── Access Page Table in memory (1st access)
       └── Get Frame Number
       └── Update TLB with new entry
       └── Access actual data (2nd access)
```

### 7.4 TLB Performance Metrics

**Effective Memory Access Time (EMAT)**:

```
EMAT = Hit_Rate × (T_memo) + Miss_Rate × (2 × T_memo + T_TLB)

Where:
- T_TLB = TLB lookup time (typically 1-2 cycles)
- T_memo = Main memory access time (typically 50-200 ns)
- Typical Hit Rate = 80-99%
```

**Example: TLB Performance Calculation**

Given:
- TLB Hit Rate: 90%
- TLB Lookup Time: 5 ns
- Memory Access Time: 100 ns

**Solution**:

**With TLB**:
```
EMAT = 0.90 × (5 + 100) + 0.10 × (5 + 100 + 100)
     = 0.90 × 105 + 0.10 × 205
     = 94.5 + 20.5
     = 115 ns
```

**Without TLB**:
```
EMAT = 2 × 100 = 200 ns
```

**Improvement**: (200 - 115) / 200 = 42.5% faster!

### 7.5 TLB Replacement Policies

When TLB is full, we need to replace an entry:
- **LRU (Least Recently Used)**: Replace the entry not used for longest time
- **Random**: Randomly choose an entry to replace
- **FIFO (First In, First Out)**: Replace the oldest entry

### 7.6 TLB Coverage and ASIDs

- **Address Space Identifier (ASID)**: Identifies which process owns each TLB entry, allowing entries from different processes to coexist
- **TLB Coverage**: Total virtual memory that can be mapped by TLB entries
  - Coverage = TLB_Entries × Page_Size
  - Example: 256 entries × 4KB = 1MB coverage

---

## 8. Address Translation: Worked Examples

### 8.1 Complete Segmentation Example

**Example 1**: For BSc CS Delhi University Exam

A system uses segmentation with the following segment table:

| Segment | Base (decimal) | Limit (decimal) |
|---------|----------------|-----------------|
| 0       | 200            | 1000            |
| 1       | 1500           | 800             |
| 2       | 3000           | 1200            |
| 3       | 5000           | 500             |

**Calculate physical address for logical address (2, 500)**:

**Solution**:
```
Segment Number = 2
Offset = 500

Base[2] = 3000
Limit[2] = 1200

Check: 500 < 1200 ✓ Valid

Physical Address = Base + Offset
                 = 3000 + 500
                 = 3500
```

**What about logical address (3, 600)?**

**Solution**:
```
Segment Number = 3
Offset = 600

Limit[3] = 500

Check: 600 > 500 ✗ INVALID!
Result: Segmentation Fault (trap to OS)
```

### 8.2 Complete Paging Example

**Example 2**: Delhi University Question Pattern

A computer system has:
- Logical address space: 16 pages
- Physical memory: 8 frames
- Page size: 512 bytes

Page table (valid entries):
| Page | Frame | Valid |
|------|-------|-------|
| 0    | 4     | 1     |
| 1    | -     | 0     |
| 2    | 1     | 1     |
| 3    | 7     | 1     |
| 4    | -     | 0     |
| 5    | 3     | 1     |
| 6    | -     | 0     |
| 7    | 2     | 1     |

**Find physical address for logical address 3640 (decimal)**

**Solution**:
```
Page Number = 3640 / 512 = 7
Page Offset = 3640 % 512 = 3640 - (7 × 512) = 3640 - 3584 = 56

From table: Page 7 → Frame 2

Physical Address = (Frame × Frame Size) + Offset
                 = (2 × 512) + 56
                 = 1024 + 56
                 = 1080
```

### 8.3 Combined Scheme Example

**Example 3**: Combined Segmentation + Paging

System specifications:
- Segment size: 8KB
- Page size: 2KB
- Maximum segments: 4
- Maximum pages per segment: 4

Given logical address: Binary `01 10 00101101` (split as Segment|Page|Offset)

**Solution**:
```
Segment = 01 (binary) = 1 (decimal)
Page = 10 (binary) = 2 (decimal)
Offset = 00101101 (binary) = 45 (decimal)

Segment 1 Table:
- Limit = 8192 (8KB)
- Base Page Table = 0x1000

Page 2 of Segment 1 → Frame 5

Physical Address = (Frame × Page Size) + Offset
                 = (5 × 2048) + 45
                 = 10240 + 45
                 = 10285
```

---

## 9. Page Replacement Algorithms

### 9.1 The Page Fault Problem

When a process needs a page that's not in memory, the OS must:
1. Find a free frame OR
2. Evict (replace) a page from an existing frame
3. Load the needed page into that frame
4. Update page tables
5. Resume the process

### 9.2 FIFO (First In First Out)

**Principle**: Replace the page that has been in memory the longest.

**Example**:

Reference String: `1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5`
Frames: 3

```
Time    1   2   3   4   5   6   7   8   9   10  11  12
Ref     1   2   3   4   1   2   5   1   2   3   4   5
Frame1  1   1   1   4   4   4   5   5   5   3   3   3
Frame2      2   2   2   1   1   1   1   2   2   4   4
Frame3          3   3   3   3   2   2   2   2   5   5
Fault    *   *   *   *   *   *   *   *   *   *   *   *
          1   2   3   4   5   6   7   8   9   10  11  12
```

**Page Faults = 9**

**Problem with FIFO**: May replace a heavily used page (Belady's Anomaly)

### 9.3 Optimal Page Replacement (OPT)

**Principle**: Replace the page that will not be used for the longest time in the future.

**Note**: This is theoretical—requires future knowledge, but used as a benchmark.

**Example** (same reference string):

```
Page Faults = 5 (optimal)
```

### 9.4 LRU (Least Recently Used)

**Principle**: Replace the page that was used least recently.

**Example** (same reference string):

```
Time    1   2   3   4   5   6   7   8   9   10  11  12
Ref     1   2   3   4   1   2   5   1   2   3   4   5
Frame1  1   1   1   1   1   1   5   5   5   3   3   3
Frame2      2   2   2   2   2   2   1   1   1   4   4
Frame3          3   3   3   3   3   3   2   2   2   5
Fault    *   *   *   *   *   *   *   *   *   *   *   *
```

**Page Faults = 10**

### 9.5 Second Chance (Clock) Algorithm

**Principle**: FIFO with a "reference bit" check—give pages a second chance if recently used.

**Implementation**:
- Circular list of pages
- If reference bit = 0: replace this page
- If reference bit = 1: clear bit and move to next

### 9.6 Algorithm Comparison

| Algorithm | Page Faults | Pros | Cons |
|-----------|-------------|------|------|
| FIFO | 9 | Simple, low overhead | Suffers from Belady's Anomaly |
| OPT | 5 | Best possible | Requires future knowledge |
| LRU | 10 | Good approximation of OPT | Hardware support needed |
| Second Chance | 7-9 | Practical approximation | Not as good as LRU |

---

## 10. Memory Protection

### 10.1 Why Protection Matters

In a multiprogrammed system, processes must be isolated from each other. Memory protection prevents:
- One process from reading/writing another process's memory
- A process from accessing OS memory
- Unauthorized access to hardware

### 10.2 Protection Mechanisms in Segmentation

Each segment table entry can store **protection bits**:

| Bit | Meaning |
|-----|---------|
| Read (R) | Can read from segment |
| Write (W) | Can write to segment |
| Execute (X) | Can execute code in segment |

**Example**:
- Code segment: R = 1, W = 0, X = 1 (read-only, executable)
- Data segment: R = 1, W = 1, X = 0 (read-write, not executable)
- Stack segment: R = 1, W = 1, X = 0

### 10.3 Protection in Paging

Page table entries include protection bits:

| Protection Field | Access Allowed |
|------------------|----------------|
| 000 | None |
| 001 | Execute only |
| 010 | Read only |
| 011 | Read/Execute |
| 100 | Write only |
| 101 | Write/Execute |
| 110 | Read/Write |
| 111 | Read/Write/Execute |

### 10.4 Valid/Invalid Bit Mechanism

- **Valid Bit = 1**: Page is in memory, access allowed
- **Valid Bit = 0**: Page not in memory OR not allocated

When accessing an invalid page:
1. Hardware generates a **trap**
2. OS handles the **page fault**
3. If page not in memory: load from disk
4. If not allocated: send **SIGSEGV** to process (segmentation fault)

---

## 11. Key Takeaways

### For Delhi University Examination

1. **Segmentation** provides logical organization (code, data, stack) but suffers from external fragmentation
2. **Paging** uses fixed-size pages/frames to eliminate external fragmentation but loses logical meaning
3. **Combined approach** uses segmentation for logical view and paging for physical memory management
4. **Address translation** requires understanding of:
   - Segment number + Offset (segmentation)
   - Page number + Offset (paging)
   - Multi-level breakdown (combined schemes)
5. **TLB** is critical for performance—reduces memory access from 2 to ~1.1 on average
6. **Page replacement algorithms** (FIFO, LRU, OPT) differ in complexity and effectiveness
7. **Memory protection** is implemented through protection bits in both segment and page tables

### Important Formulas

```
Physical Address (Segmentation) = Base[seg] + Offset
Physical Address (Paging) = Frame[page] × PageSize + Offset
EMAT = Hit_Rate × (T_TLB + T_mem) + Miss_Rate × (T_TLB + 2 × T_mem)
Page Fault Rate = Page Faults / Total Memory References
```

---

## 12. Multiple Choice Questions

### Section A: Fundamentals

**Question 1**: In segmentation, the logical address consists of:
- (a) Page number and offset
- (b) Segment number and offset ✓
- (c) Frame number and offset
- (d) None of the above

**Question 2**: The main advantage of paging over segmentation is:
- (a) It provides logical memory view
- (b) It eliminates external fragmentation ✓
- (c) It supports sharing
- (d) It provides protection

**Question 3**: In a paged memory system, if page size is 4KB, how many bits are needed for the offset?
- (a) 10 bits
- (b) 12 bits ✓
- (c) 14 bits
- (d) 16 bits

**Question 4**: A page fault occurs when:
- (a) The requested page is in memory
- (b) The requested page is not in memory ✓
- (c) The TLB has a hit
- (d) Memory is full

**Question 5**: Which page replacement algorithm may suffer from Belady's anomaly?
- (a) LRU
- (b) OPT
- (c) FIFO ✓
- (d) All of the above

### Section B: Advanced Concepts

**Question 6**: In a combined segmentation and paging system, the address format is:
- (a) Segment number | Page number | Offset ✓
- (b) Page number | Segment number | Offset
- (c) Only segment number and offset
- (d) Only page number and offset

**Question 7**: The TLB is a:
- (a) Main memory cache
- (b) Associative cache for page table entries ✓
- (c) Type of page table
- (d) Disk cache

**Question 8**: An inverted page table has:
- (a) One entry per virtual page
- (b) One entry per physical frame ✓
- (c) Multiple levels
- (d) No practical use

**Question 9**: If TLB hit rate is 80% and memory access time is 100ns, what is the effective access time with a TLB lookup of 5ns?
- (a) 100ns
- (b) 105ns
- (c) 115ns ✓
- (d) 205ns

**Question 10**: The dirty bit in a page table entry is used for:
- (a) Indicating whether page is valid
- (b) Tracking if page has been modified ✓
- (c) Page replacement decisions
- (d) Protection

### Section C: Numerical Problems

**Question 11**: In a system with 16KB pages and 64KB physical memory, how many frames exist?
- (a) 4
- (b) 8
- (c) 16 ✓
- (d) 32

**Question 12**: A process has 4 pages and uses FIFO replacement. If the reference string is 1,2,3,4,1,2,5 with 3 frames, how many page faults occur?
- (a) 5
- (b) 6 ✓
- (c) 7
- (d) 8

---

## 13. Flashcards

### Flashcard 1
**Q**: What is segmentation in memory management?
**A**: A memory management technique that divides a program's address space into variable-sized segments based on logical units (code, data, stack).

### Flashcard 2
**Q**: What is paging?
**A**: A memory management technique that divides both logical and physical memory into fixed-size blocks called pages and frames respectively.

### Flashcard 3
**Q**: What is a page fault?
**A**: An interrupt that occurs when a process accesses a page that is not currently in physical memory (valid bit = 0).

### Flashcard 4
**Q**: What is the purpose of a TLB?
**A**: The Translation Lookaside Buffer (TLB) is a hardware cache that stores recent page table entries to speed up address translation, avoiding the need to access memory twice.

### Flashcard 5
**Q**: What is Belady's Anomaly?
**A**: The phenomenon where increasing the number of page frames can actually increase the number of page faults (observed in FIFO algorithm).

### Flashcard 6
**Q**: What is the difference between internal and external fragmentation?
**A**: Internal fragmentation: wasted space within allocated blocks (paging). External fragmentation: free memory scattered in small holes (segmentation).

### Flashcard 7
**Q**: Why is two-level paging used?
**A**: To reduce memory overhead of page tables by only allocating page table structures for valid virtual addresses, avoiding the need for a massive single-level page table.

### Flashcard 8
**Q**: What is an inverted page table?
**A**: A page table structure with one entry per physical frame, containing the PID and virtual page number that occupies that frame, reducing memory overhead.

### Flashcard 9
**Q**: What is the role of the valid bit in a page table?
**A**: Indicates whether the page is currently resident in physical memory (1 = valid/in memory, 0 = invalid/not in memory).

### Flashcard 10
**Q**: What is the difference between LRU and FIFO page replacement?
**A**: FIFO replaces the oldest page in memory regardless of usage. LRU (Least Recently Used) replaces the page that hasn't been used for the longest time.

---

## References for Delhi University Students

- **Recommended Textbooks**:
  - Operating System Concepts by Silberschatz, Galvin, Gagne
  - Modern Operating Systems by Andrew S. Tanenbaum
  - Operating Systems: Design and Implementation by Andrew S. Tanenbaum

- **Delhi University Syllabus Reference**:
  - Unit III: Memory Management (as per NEP 2024 UGCF)
  - Topics: Contiguous allocation, Paging, Segmentation, Virtual Memory, Page Replacement

- **Previous Year Question Papers**: Available on DU official portal for practice

---

*Study Material prepared for BSc (Hons) Computer Science, Delhi University — NEP 2024 UGCF Curriculum*