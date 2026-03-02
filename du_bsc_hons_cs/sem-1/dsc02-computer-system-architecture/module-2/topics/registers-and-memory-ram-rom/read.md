# Registers and Memory (RAM, ROM)

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

Memory and registers form the backbone of any computer system. While the CPU performs computations, it needs rapid access to data and instructions—this is where registers and memory come into play. Understanding these components is essential for grasping how computers execute programs, manage data, and optimize performance.

**Real-World Relevance:** Every application you use—from a simple calculator to complex machine learning models—relies on the interaction between registers and memory. When you open a document, the operating system loads it from secondary storage (hard drive) into RAM, and the CPU manipulates it using registers. Understanding this flow helps you appreciate why your computer "freezes" when RAM is exhausted, or why SSD upgrades improve responsiveness.

**Delhi University Syllabus Context:** This topic aligns with the **Computer System Architecture** paper under NEP 2024 UGCF. Students must understand the internal organization of computer memory, the difference between various memory types, and how they contribute to system performance.

---

## 2. Registers

### 2.1 Definition and Purpose

A **register** is a small, high-speed memory location within the CPU itself. Registers store data that the CPU is actively processing, including:

- **Data values** (operands for arithmetic/logical operations)
- **Memory addresses** (pointers to locations in RAM)
- **Instruction codes** (the current instruction being executed)
- **Control information** (flags, status bits)

Registers are measured in **bits**—a 32-bit CPU has 32-bit registers, meaning it can handle 32-bit data in a single operation.

### 2.2 Types of Registers

#### General-Purpose Registers (GPRs)
Used for temporary data storage during computations. In x86-64 architecture:
- **RAX, RBX, RCX, RDX** — Accumulators, base, count, data
- **RSI, RDI** — Source and destination indices
- **RBP, RSP** — Base pointer and stack pointer

#### Special-Purpose Registers

| Register | Function |
|----------|----------|
| **Program Counter (PC)** | Holds the address of the next instruction to fetch |
| **Instruction Register (IR)** | Stores the currently executing instruction |
| **Memory Address Register (MAR)** | Holds the memory address being accessed |
| **Memory Data Register (MDR)** | Holds data being transferred to/from memory |
| **Accumulator (ACC)** | Stores results of arithmetic operations |
| **Stack Pointer (SP)** | Points to top of stack in memory |
| **Base Register** | Used for addressing |
| **Index Register** | Used in indexed addressing modes |

#### Status/Flag Registers
Contain individual bits that indicate CPU state:
- **Zero Flag (ZF)** — Set when result is zero
- **Sign Flag (SF)** — Set when result is negative
- **Carry Flag (CF)** — Set when arithmetic overflow occurs
- **Overflow Flag (OF)** — Set on signed arithmetic overflow

### 2.3 Register Organization in 8086

The Intel 8086 microprocessor (foundational to modern x86) provides excellent register examples:

```
AX (16-bit) = AH (high 8) | AL (low 8)
BX = BH | BL
CX = CH | CL
DX = DH | DL
```

Each register can be accessed as 16-bit or 8-bit, demonstrating how compilers optimize data handling.

---

## 3. Random Access Memory (RAM)

### 3.1 Overview

**RAM** is volatile, read-write memory that stores data and instructions currently in use. "Random Access" means any memory location can be accessed directly without reading preceding locations.

### 3.2 SRAM (Static RAM)

**SRAM** uses flip-flop circuits to store each bit. Each bit requires 6 transistors.

**Characteristics:**
- **Speed:** Very fast (access times of 1-2ns)
- **Density:** Low (requires more transistors per bit)
- **Power Consumption:** Higher due to continuous power needed
- **Cost:** Expensive
- **Volatility:** Loses data without power
- **Use Cases:** CPU cache (L1, L2, L3), register files

```
SRAM Cell Structure:
┌─────────────┐
│  Transistor │──── Bit Line
│   (x6)      │
└─────────────┘
```

### 3.3 DRAM (Dynamic RAM)

**DRAM** uses capacitors and transistors to store each bit. Each bit requires 1 transistor + 1 capacitor.

**Characteristics:**
- **Speed:** Slower (access times of 50-100ns)
- **Density:** High (simpler cell structure)
- **Power Consumption:** Lower (requires refresh cycles)
- **Cost:** Inexpensive
- **Volatility:** Loses data without power
- **Use Cases:** Main system memory (RAM modules)

**Refresh Cycle:** Capacitors lose charge over time, requiring periodic refresh (typically every 64ms).

### 3.4 Comparison: SRAM vs DRAM

| Feature | SRAM | DRAM |
|---------|------|------|
| Cell Complexity | 6 transistors | 1 transistor + 1 capacitor |
| Access Time | 1-2 ns | 50-100 ns |
| Power Consumption | Higher | Lower (refresh overhead) |
| Cost per Bit | Higher | Lower |
| Density | Lower | Higher |
| Use Case | Cache, Registers | Main Memory |

---

## 4. Read-Only Memory (ROM)

### 4.1 Overview

**ROM** is non-volatile memory that retains data without power. Originally read-only, modern variants allow limited or full rewriting.

### 4.2 Types of ROM

#### Mask ROM (MROM)
- Programmable during manufacturing
- Cannot be modified after production
- Used for permanent firmware

#### PROM (Programmable ROM)
- Blank chips programmed by users once
- Uses fuses that are "blown" to store 0s
- One-time programmable

#### EPROM (Erasable PROM)
- Can be erased using UV light
- Requires special equipment
- Windowed chips (expensive)
- Thousands of write cycles

#### EEPROM (Electrically EPROM)
- Electrically erasable
- Byte-by-byte rewriting
- Limited write cycles (~100,000)
- Used for BIOS/UEFI firmware

#### Flash Memory
- Block-based erasing (faster than EEPROM)
- High density, low cost
- Used in USB drives, SSDs, embedded systems
- NAND Flash vs NOR Flash:
  - **NAND:** Sequential access, high density, cheaper (USB, SSD)
  - **NOR:** Random access, faster reads, more expensive (firmware)

---

## 5. Memory Hierarchy

Memory hierarchy optimizes cost-performance by using fast, expensive memory near the CPU and slower, cheaper memory further away.

```
┌────────────────────────────────────────────────────────────┐
│                    MEMORY HIERARCHY                        │
├────────────────────────────────────────────────────────────┤
│  Level 1: Registers      < 1 ns      ~1 KB    CPU          │
│  Level 2: L1 Cache       1-2 ns       ~64 KB   On-chip     │
│  Level 3: L2 Cache       3-10 ns      ~256 KB  On-chip     │
│  Level 4: L3 Cache       10-20 ns     ~8 MB    On-board    │
│  Level 5: Main Memory   50-100 ns    ~16 GB   DRAM         │
│  Level 6: SSD           10-100 µs    ~1 TB    NVMe/SATA    │
│  Level 7: HDD           5-10 ms      ~8 TB    Magnetic     │
│  Level 8: Tape/Cloud    Seconds      ∞        Magnetic     │
└────────────────────────────────────────────────────────────┘
```

### 5.1 Locality Principles

- **Temporal Locality:** Recently accessed items likely accessed again (loops)
- **Spatial Locality:** Items near recently accessed items likely accessed (arrays)

---

## 6. Cache Memory

### 6.1 Concept

Cache is a small, fast memory between CPU and main memory. It exploits locality to reduce memory access latency.

### 6.2 Cache Mapping Techniques

#### Direct Mapping
Each memory block maps to exactly one cache line:
```
Cache Line = (Block Address) mod (Number of Cache Lines)
```
Simple but causes conflicts.

#### Fully Associative
Any block can go anywhere in cache:
- Expensive (requires comparators)
- Maximum flexibility

#### Set Associative
Hybrid approach—cache divided into sets, each with N ways:
- Common: 2-way, 4-way, 8-way
- Balance of cost and performance

### 6.3 Cache Performance Metrics

- **Hit Rate:** Percentage of memory accesses found in cache
- **Miss Penalty:** Time to fetch from main memory
- **Average Memory Access Time (AMAT):**
  ```
  AMAT = Hit Time + (Miss Rate × Miss Penalty)
  ```

### 6.4 Write Policies

- **Write Through:** Write to both cache and memory (slow, consistent)
- **Write Back:** Write to cache, write to memory on eviction (fast, complex)

---

## 7. Virtual Memory

### 7.1 Concept

Virtual memory creates an illusion of each process having its own large, contiguous address space. Hardware (MMU) translates virtual addresses to physical addresses.

### 7.2 Paging

Memory divided into fixed-size **pages** (typically 4KB):
- **Page Table:** Maps virtual pages to physical frames
- **TLB (Translation Lookaside Buffer):** Cache of recent translations

### 7.3 Page Fault Handling

```
1. CPU generates virtual address
2. MMU checks TLB → miss
3. MMU checks page table → not in memory
4. OS loads page from disk to RAM
5. Update page table
6. Resume instruction
```

---

## 8. Bus Architecture

### 8.1 System Bus Types

- **Data Bus:** Carries actual data (width = bits per transfer)
- **Address Bus:** Carries memory addresses (determines max memory)
- **Control Bus:** Carries control signals (read/write, interrupt, clock)

### 8.2 Bus Cycles

A memory read cycle involves:
1. Address placed on address bus
2. Control signals (RD) activated
3. Wait states (if memory slow)
4. Data placed on data bus
5. Control signals deactivated

### 8.3 Example: Memory Read Operation Timing

```
Cycle 1: Address [0x1000] ──────╮
Cycle 2: Read Signal ────────────╯─────╮
Cycle 3: Data [0x42] Available ─────────╯─────
```

---

## 9. Concrete Examples with Code

### Example 1: Register Usage in Assembly (x86-64)

```c
// C Code
int sum = 0;
for (int i = 0; i < 10; i++) {
    sum += i;
}
```

```assembly
; Equivalent x86-64 Assembly (AT&T syntax)
    movl    $0, %eax        ; sum = 0 (use EAX as accumulator)
    movl    $0, %edi        ; i = 0
.L2:
    addl    %edi, %eax      ; sum += i
    incl    %edi            ; i++
    cmpl    $10, %edi       ; compare i with 10
    jne     .L2             ; if not equal, loop
    ; Result in EAX (sum = 45)
```

**Explanation:** 
- `EAX` serves as both accumulator and return value
- `EDI` holds loop counter
- Compiler automatically selects optimal registers

### Example 2: Memory Allocation and Cache Behavior

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 1000000

// Row-major order (C default)
void row_major_access(int arr[SIZE][SIZE]) {
    long long sum = 0;
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            sum += arr[i][j];
        }
    }
    printf("Row-major sum: %lld\n", sum);
}

// Column-major order
void col_major_access(int arr[SIZE][SIZE]) {
    long long sum = 0;
    for (int j = 0; j < SIZE; j++) {
        for (int i = 0; i < SIZE; i++) {
            sum += arr[i][j];
        }
    }
    printf("Col-major sum: %lld\n", sum);
}

int main() {
    int (*arr)[SIZE] = malloc(sizeof(int[SIZE][SIZE]));
    
    // Initialize
    for (int i = 0; i < SIZE; i++)
        for (int j = 0; j < SIZE; j++)
            arr[i][j] = 1;
    
    // Time row-major
    clock_t start = clock();
    row_major_access(arr);
    printf("Row-major time: %.3f seconds\n", 
           (double)(clock() - start) / CLOCKS_PER_SEC);
    
    // Time column-major
    start = clock();
    col_major_access(arr);
    printf("Column-major time: %.3f seconds\n", 
           (double)(clock() - start) / CLOCKS_PERSEC);
    
    free(arr);
    return 0;
}
```

**Expected Output (typical):**
```
Row-major sum: 1000000000
Row-major time: 0.234 seconds
Column-major sum: 1000000000
Column-major time: 2.891 seconds
```

**Analysis:** Row-major access is ~12x faster because:
- C stores arrays row-by-row in memory
- Row-major accesses sequential memory locations
- CPU prefetcher loads entire cache line (64 bytes)
- Column-major causes cache misses on every access

---

## 10. Multiple Choice Questions (Advanced Level)

### Question 1
In a direct-mapped cache with 64 lines, how many bits are required for the tag field if the system uses 32-bit addresses and each block is 16 bytes?

A) 32 bits  
B) 20 bits  
C) 16 bits  
D) 8 bits  

**Answer:** B  
**Explanation:**  
- Offset bits: log₂(16) = 4 bits  
- Index bits: log₂(64) = 6 bits  
- Tag bits: 32 - 4 - 6 = 20 bits

### Question 2
Which memory type has the fastest access time?

A) DRAM  
B) SRAM  
C) EEPROM  
D) NAND Flash  

**Answer:** B  
**Explanation:** SRAM has access times of 1-2ns, significantly faster than DRAM (50-100ns).

### Question 3
In a system with 16-bit addresses and a two-way set associative cache having 4 sets, what is the block size (in bytes) if each set contains 2 lines of 8 bytes?

A) 4 bytes  
B) 8 bytes  
C) 16 bytes  
D) 32 bytes  

**Answer:** B  
**Explanation:** Each line = 8 bytes (given). Block size = line size = 8 bytes.

### Question 4
A computer has 24-bit addresses and a physically indexed, physically tagged L1 cache with 64-byte blocks. If the cache has 4096 sets and is 8-way associative, what is the size of the cache (in KB)?

A) 256 KB  
B) 512 KB  
C) 1024 KB  
D) 2048 KB  

**Answer:** B  
**Explanation:**  
- Block offset: log₂(64) = 6 bits  
- Index bits: log₂(4096) = 12 bits  
- Tag bits: 24 - 6 - 12 = 6 bits  
- Cache size = (2^12 sets) × (8 ways) × (64 bytes) = 4096 × 8 × 64 = 2,097,152 bytes = 512 KB

### Question 5
Which of the following statements about virtual memory is FALSE?

A) Page tables are stored in main memory  
B) TLB misses always cause page faults  
C) Swapping allows processes to use more memory than physically available  
D) Segmentation provides variable-sized memory blocks  

**Answer:** B  
**Explanation:** TLB misses cause page table lookups, not necessarily page faults. A page fault occurs only if the page is not in physical memory.

### Question 6
In a write-back cache, when should the data in a modified cache line be written back to main memory?

A) On every write to the cache line  
B) When the cache line is evicted  
C) When the CPU reads from the same line  
D) Never, until explicitly requested  

**Answer:** B  
**Explanation:** Write-back delays writing until the cache line must be replaced (evicted).

### Question 7
Consider a system with the following memory hierarchy:
- L1 Cache: 4-cycle hit time, 20% miss rate
- L2 Cache: 12-cycle hit time, 10% of L1 misses
- Main Memory: 200-cycle access time

What is the average memory access time (in cycles)?

A) 4 + 0.2 × (12 + 0.1 × 200)  
B) 4 + 0.2 × 12 + 0.02 × 200  
C) 4 + 0.2 × 12 + 0.1 × 200  
D) 4 + 0.8 × (12 + 0.1 × 200)  

**Answer:** B  
**Explanation:**  
AMAT = L1_hit + (L1_miss × L2_hit_time) + (L1_miss × L2_miss × Memory_time)  
= 4 + (0.2 × 12) + (0.2 × 0.1 × 200) = 4 + 2.4 + 4 = 10.4 cycles

---

## 11. Flashcards

| Term | Definition |
|------|------------|
| **Register** | Small, fast internal CPU memory for storing operands, addresses, and control data |
| **SRAM** | Static RAM using flip-flops; fast, expensive, used in CPU cache |
| **DRAM** | Dynamic RAM using capacitors; slower, cheaper, used in main memory |
| **Cache Line** | Minimum unit of data transferred between cache and memory (typically 64 bytes) |
| **Hit Rate** | Percentage of memory accesses found in cache |
| **TLB** | Translation Lookaside Buffer—hardware cache for virtual-to-physical address translations |
| **Page Fault** | Exception when requested page is not in physical memory |
| **Write-Through** | Cache policy writing to both cache and main memory simultaneously |
| **Write-Back** | Cache policy writing to memory only when cache line is evicted |
| **Associativity** | Number of cache lines per set (direct-mapped = 1, 4-way = 4) |
| **Virtual Memory** | Technique using disk to extend apparent size of physical memory |
| **Bit Line** | Conductor in memory arrays that carries data during read/write operations |
| **Refresh Cycle** | Periodic recharging of DRAM capacitors to maintain data |
| **NOR Flash** | Flash memory with random-access read; used for code execution |
| **NAND Flash** | Flash memory with sequential access; used for data storage |

---

## 12. Key Takeaways

1. **Registers** are the fastest memory (sub-nanosecond access), directly within the CPU, and include general-purpose and special-purpose types (PC, MAR, MDR, IR).

2. **SRAM** uses flip-flops (6 transistors/bit) for cache memory, while **DRAM** uses capacitors (1 transistor + 1 capacitor/bit) for main memory—DRAM requires periodic refresh.

3. **Memory Hierarchy** balances cost and performance: registers → L1/L2/L3 cache → RAM → SSD → HDD → Cloud.

4. **Cache Memory** exploits temporal and spatial locality through direct-mapped, set-associative, or fully-associative organization.

5. **Virtual Memory** enables processes to use more memory than physically available through paging and demand loading.

6. **Bus Architecture** includes data, address, and control buses; memory operations require precise timing coordination.

7. **Code Optimization:** Array access patterns significantly impact performance due to cache behavior—row-major access in C is 10x+ faster than column-major for large arrays.

8. **Flash Memory** (NAND/NOR) has replaced traditional EEPROM in embedded systems and SSDs due to higher density and lower cost.

9. **Understanding memory systems** is critical for writing performant code and understanding computer architecture fundamentals at Delhi University examinations.

---

*Prepared for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)*  
*Subject: Computer System Architecture*