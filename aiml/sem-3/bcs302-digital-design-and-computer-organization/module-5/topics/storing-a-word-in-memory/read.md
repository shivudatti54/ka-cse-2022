# Storing a Word in Memory


## Table of Contents

- [Storing a Word in Memory](#storing-a-word-in-memory)
- [1. Introduction](#1-introduction)
- [2. Formal Definition and Register Transfer Notation](#2-formal-definition-and-register-transfer-notation)
  - [2.1 Basic Definition](#21-basic-definition)
  - [2.2 Register Transfer Language (RTL) Specification](#22-register-transfer-language-rtl-specification)
- [3. Detailed Step-by-Step Store Sequence](#3-detailed-step-by-step-store-sequence)
  - [Step 1: Effective Address Computation](#step-1-effective-address-computation)
  - [Step 2: Load Data into MDR](#step-2-load-data-into-mdr)
  - [Step 3: Activate Write Control Signal](#step-3-activate-write-control-signal)
  - [Step 4: Bus Transfer and Memory Write](#step-4-bus-transfer-and-memory-write)
  - [Step 5: Memory Function Complete (MFC)](#step-5-memory-function-complete-mfc)
- [4. Formal Timing Analysis](#4-formal-timing-analysis)
  - [4.1 Timing Diagram Representation](#41-timing-diagram-representation)
  - [4.2 Timing Table with Control Word Encoding](#42-timing-table-with-control-word-encoding)
  - [4.3 Mathematical Analysis of Store Latency](#43-mathematical-analysis-of-store-latency)
- [5. Comparative Analysis: Fetch vs. Store](#5-comparative-analysis-fetch-vs-store)
- [6. Word Alignment in Store Operations](#6-word-alignment-in-store-operations)
  - [6.1 Definition and Formal Treatment](#61-definition-and-formal-treatment)
  - [6.2 Alignment Requirements by Word Size](#62-alignment-requirements-by-word-size)
  - [6.3 Performance Implications](#63-performance-implications)
- [7. Byte Ordering (Endianness)](#7-byte-ordering-endianness)
  - [7.1 Formal Definition](#71-formal-definition)
  - [7.2 Mathematical Representation](#72-mathematical-representation)
  - [7.3 Complete Storage Example](#73-complete-storage-example)
  - [7.4 Implications for Software](#74-implications-for-software)
- [8. Cache Memory Interaction and Write Policies](#8-cache-memory-interaction-and-write-policies)
  - [8.1 Write-Through Policy](#81-write-through-policy)
  - [8.2 Write-Back Policy](#82-write-back-policy)
  - [8.3 Store Buffer](#83-store-buffer)
- [9. Pipeline Hazards and Store Operations](#9-pipeline-hazards-and-store-operations)
  - [9.1 Store-to-Load Forwarding](#91-store-to-load-forwarding)
  - [9.2 Store Ordering and Memory Coherence](#92-store-ordering-and-memory-coherence)
- [10. Summary of Key Concepts](#10-summary-of-key-concepts)

## 1. Introduction

The **Store** (or Write) operation constitutes one of the two fundamental memory transfer operations in a processor, the other being the Fetch (or Read) operation. While fetching retrieves data from memory into a processor register, the store operation performs the inverse function: transferring data from a CPU register to a specified memory location. This operation is essential for preserving computational results, saving program state, and maintaining data structures in main memory.

Understanding the store operation at the hardware level requires examining the coordinated action of several processor components: the Memory Address Register (MAR), Memory Data Register (MDR), address bus, data bus, and various control signals. The store operation demonstrates the principle of **bidirectional data flow** in computer systems, where data travels from the processor to memory through the data bus.

## 2. Formal Definition and Register Transfer Notation

### 2.1 Basic Definition

A **Store** operation transfers a word of data from a processor register to a memory location addressed by an effective address. This operation modifies the state of memory while leaving the source register contents unchanged (preserving data for potential subsequent operations).

### 2.2 Register Transfer Language (RTL) Specification

The store operation can be formally specified using Register Transfer Notation:

```
[M] ← R₁
```

Where:

- **M** represents the memory location specified by the effective address
- **R₁** denotes the source processor register containing the data to be stored
- **←** indicates the direction of data transfer (from right to left)

For microarchitectural description, the operation decomposes into sequential register transfers:

```
MAR ← EA // Load effective address into Memory Address Register
MDR ← R₁ // Load data from source register into Memory Data Register
M[MAR] ← MDR // Transfer data from MDR to memory location addressed by MAR
```

**Theorem**: The store operation is complete when the memory location M contains the original value of R₁ and R₁ remains unchanged.

_Proof_: The RTL specification M[MAR] ← MDR defines a write operation where the content of MDR is copied to the memory location indexed by MAR. Since the assignment operation copies rather than moves data, the source register R₁ retains its original value. Upon receiving the Memory Function Complete (MFC) signal, the memory subsystem confirms that the write operation has been successfully completed, thus satisfying the postcondition M[EA] = old(R₁). ∎

## 3. Detailed Step-by-Step Store Sequence

The store operation executes through a precisely coordinated sequence of steps, each involving specific hardware components and control signals:

### Step 1: Effective Address Computation

The processor first computes the **effective address** (EA) of the target memory location. This computation may involve different addressing modes:

- **Direct Addressing**: EA is contained directly in the instruction
- **Register Indirect**: EA is contained in a register specified by the instruction
- **Base + Offset**: EA = Base Register + Sign-Extended Immediate Offset
- **Indexed**: EA = Base Register + Index Register

```
ALU_Output ← R_base + Sign_Extend(offset)
MAR ← ALU_Output
```

### Step 2: Load Data into MDR

The source register's contents are copied into the Memory Data Register:

```
MDR ← R_source
```

The MDR now holds the exact bit pattern to be written to memory.

### Step 3: Activate Write Control Signal

The Control Unit issues the **Write** signal on the control bus:

```
Control_Signals ← {Read=0, Write=1, Memory_Enable=1}
```

This binary encoding indicates to the memory subsystem that a write operation is requested.

### Step 4: Bus Transfer and Memory Write

The address and data are simultaneously placed on their respective buses:

- **Address Bus**: Carries the contents of MAR (the effective address)
- **Data Bus**: Carries the contents of MDR (the data to be stored)

```
Address_Bus ← MAR[15:0]
Data_Bus ← MDR[31:0]
```

The memory unit receives both signals and performs the write operation at the addressed location.

### Step 5: Memory Function Complete (MFC)

Upon successful completion of the write operation, the memory asserts the MFC signal:

```
MFC ← 1 // Memory Function Complete received
```

The processor monitors this signal and proceeds to the next instruction upon acknowledgment.

## 4. Formal Timing Analysis

### 4.1 Timing Diagram Representation

The store operation requires multiple clock cycles, with precise timing relationships between control signals and bus activities:

```
Clock: ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐
 │ │ │ │ │ │ │
 │ T1 │ │ T2 │ │ T3 │ │ T4 │
 └─────┘ └─────┘ └─────┘ └─────┘

MAR: ┌─────────────────┐
 │ Effective │
 │ Address │
 └─────────────────┘

MDR: ┌─────────────────┐
 │ Data to │
 │ Store │
 └─────────────────┘

Write: ┌───────────┐
 │ 1 │
 └───────────┘

MFC: ┌───────┐
 │ 1 │
 └───────┘
```

### 4.2 Timing Table with Control Word Encoding

| Cycle | MAR      | MDR        | Control Word (16-bit) | Bus Activity        | MFC |
| ----- | -------- | ---------- | --------------------- | ------------------- | --- |
| T1    | ← EA     | Unchanged  | 0001 0000 1000 0001   | Address placed      | 0   |
| T2    | Holds EA | ← R_source | 0001 0000 0100 0010   | Data placed on bus  | 0   |
| T3    | Holds EA | Holds Data | 0001 0000 0010 0100   | Write signal active | 0→1 |
| T4    | ← Next   | ← Next     | Depends on next instr | MFC received        | 1→0 |

**Control Word Encoding Convention**:

- Bit 15-12: Operation type (0001 = Store)
- Bit 11-8: MAR source (0000 = ALU, 0001 = IR)
- Bit 7-4: MDR source (0010 = Register file)
- Bit 3-0: Control signals (0001 = Write, 0010 = MFC enable)

### 4.3 Mathematical Analysis of Store Latency

For a processor with memory access time **t_mem** and clock period **t_clk**, the store instruction requires:

```
T_store = t_mem + 2t_clk // Minimum (without cache)
```

In a **pipelined processor** with write-through cache:

```
T_store_pipeline = t_cache + t_mem // Typically 1-2 cycles + memory
```

## 5. Comparative Analysis: Fetch vs. Store

The following table systematically compares the Fetch and Store operations:

| Aspect            | Fetch Operation          | Store Operation                      |
| ----------------- | ------------------------ | ------------------------------------ |
| Data Direction    | Memory → CPU Register    | CPU Register → Memory                |
| MDR Role          | Holds data from memory   | Holds data to be written             |
| Control Signal    | Read = 1, Write = 0      | Read = 0, Write = 1                  |
| Bus Usage         | Data bus carries input   | Data bus carries output              |
| Register Affected | Destination register     | Source register unchanged            |
| Memory State      | Unchanged                | Modified                             |
| Typical Timing    | T1: MAR←EA, T2: Read+MFC | T1: MAR←EA, T2: MDR←R, T3: Write+MFC |

## 6. Word Alignment in Store Operations

### 6.1 Definition and Formal Treatment

A word is **naturally aligned** in memory if its starting address is a multiple of its size in bytes. For an n-byte word:

```
Aligned: Address mod n = 0
Unaligned: Address mod n ≠ 0
```

### 6.2 Alignment Requirements by Word Size

| Word Size | Aligned Addresses (Hex) | Unaligned Examples     |
| --------- | ----------------------- | ---------------------- |
| 2 bytes   | 0, 2, 4, 6, 8, A, C, E  | 1, 3, 5, 7, 9, B, D, F |
| 4 bytes   | 0, 4, 8, C              | 1, 2, 3, 5, 6, 7, 9... |
| 8 bytes   | 0, 8                    | 1-7, 9-F               |

### 6.3 Performance Implications

**Theorem**: Aligned memory accesses are more efficient than unaligned accesses.

_Proof_: Modern memory systems are organized as arrays of bytes arranged in rows (lines) of fixed width (typically 8 or 16 bytes). An aligned access to an n-byte word at address A requires accessing floor(A/w) word lines, where w is the word line size in bytes. An unaligned access spanning a word line boundary requires two memory operations instead of one. Since memory access time is typically the dominant latency in the memory hierarchy, unaligned accesses incur approximately 2× the latency of aligned accesses. ∎

**Example Calculation**:
For a 32-bit (4-byte) word stored at address 0x1003 (unaligned) on a system with 8-byte (64-bit) memory lines:

- The word spans from byte 3 to byte 6 of line 0x1000
- Two memory read operations required to assemble the 4-byte word
- Latency: 2 × t_mem vs. 1 × t_mem for aligned access at 0x1000

## 7. Byte Ordering (Endianness)

### 7.1 Formal Definition

**Endianness** defines the byte ordering of multi-byte words in memory. The choice affects how processors interpret and store binary data:

- **Big-Endian**: The most significant byte (MSB) occupies the lowest memory address
- **Little-Endian**: The least significant byte (LSB) occupies the lowest memory address

### 7.2 Mathematical Representation

For a 32-bit word W = b₃b₂b₁b₀ (where b₃ is MSB, b₀ is LSB):

```
Big-Endian: M[A] = b₃, M[A+1] = b₂, M[A+2] = b₁, M[A+3] = b₀
Little-Endian: M[A] = b₀, M[A+1] = b₁, M[A+2] = b₂, M[A+3] = b₃
```

### 7.3 Complete Storage Example

**Problem**: Store the 32-bit hexadecimal value **0x1A2B3C4D** at base address **0x1000**

| Address | Big-Endian Value | Little-Endian Value |
| ------- | ---------------- | ------------------- |
| 0x1000  | 0x1A (b₃ = MSB)  | 0x4D (b₀ = LSB)     |
| 0x1001  | 0x2B             | 0x3C                |
| 0x1002  | 0x3C             | 0x2B                |
| 0x1003  | 0x4D (b₀ = LSB)  | 0x1A (b₃ = MSB)     |

### 7.4 Implications for Software

- **Network Protocols** specify Big-Endian byte order (network byte order)
- **x86 architectures** use Little-Endian
- **Reading byte sequences**: Little-Endian allows intuitive reading as little-endian integers without byte swapping when the LSB is at the lowest address

## 8. Cache Memory Interaction and Write Policies

### 8.1 Write-Through Policy

In a **write-through** cache, every store operation updates both the cache and main memory:

```
Write-Through Algorithm:
 if (cache_hit) then
 cache_line ← data
 memory[MAR] ← data // Also update main memory
 else
 memory[MAR] ← data // Allocate on write (optional)
```

**Advantages**: Simple coherency, memory always contains current data
**Disadvantage**: Higher memory traffic, increased write latency

### 8.2 Write-Back Policy

In a **write-back** cache, stores update only the cache line, marking it as **dirty**:

```
Write-Back Algorithm:
 if (cache_hit) then
 cache_line ← data
 dirty_bit ← 1
 else
 // Allocate line from memory
 cache_line ← fetch_from_memory(address)
 cache_line ← data
 dirty_bit ← 1
```

The dirty line is written back to memory only when evicted.

**Advantages**: Reduces memory traffic, faster stores
**Disadvantage**: Requires coherency protocols for multiprocessor systems

### 8.3 Store Buffer

Modern processors include a **store buffer** to decouple execution from memory:

```
Store Buffer Operation:
 1. Store execution: SB[head] ← {address, data}
 2. Memory controller: Reads from SB and writes to cache/memory
 3. Execution continues: Processor not blocked by slow memory
```

This enables the processor to execute subsequent instructions while the store is pending in the buffer.

## 9. Pipeline Hazards and Store Operations

### 9.1 Store-to-Load Forwarding

In a pipelined processor, a load instruction following a store may require data that was just stored:

**Sequence**:

```
STORE R1, 0(R2) // Store R1 to address in R2
LOAD R3, 0(R2) // Load from same address into R3
```

**Hazard**: Without forwarding, the load would read stale data from memory.

**Solution**: Store-to-load forwarding transfers data directly from the store buffer to the load unit:

```
if (SB.address == load.address) then
 R3 ← SB.data // Forward from store buffer
else
 R3 ← Cache/Memory[load.address]
```

### 9.2 Store Ordering and Memory Coherence

In weakly ordered memory models, stores may be reordered by the processor. Memory barriers (e.g., `MFENCE` on x86) enforce ordering:

```
// Without ordering guarantee
STORE A, 1
STORE B, 1
// Loads might observe B=1 before A=1

// With MFENCE
STORE A, 1
MFENCE
STORE B, 1
// Loads observe A=1 before B=1
```

## 10. Summary of Key Concepts

1. **Store Operation**: Transfers data from CPU register to memory: M[EA] ← R_source

2. **Hardware Components**: MAR holds effective address, MDR holds data to be written, control signals coordinate the operation

3. **Control Signal Encoding**: Write signal (active high), MFC acknowledgment

4. **Timing**: Requires minimum 2-3 clock cycles for main memory; faster with cache

5. **Word Alignment**: Aligned stores (address multiple of word size) complete in single operation; unaligned may require multiple memory accesses

6. **Endianness**: Big-Endian stores MSB at lowest address; Little-Endian stores LSB at lowest address

7. **Cache Write Policies**: Write-through updates memory immediately; write-back defers until eviction

8. **Pipeline Hazards**: Store-to-load forwarding resolves data hazards; memory barriers enforce ordering

9. **Store Buffer**: Decouples execution from memory, improving performance

10. **Instruction Cycle Stage**: Store operations execute in MEM stage, not WB stage
