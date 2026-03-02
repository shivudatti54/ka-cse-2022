Of course. Here is a comprehensive educational note on "Storing a Word in Memory" and "Execution of a Complete Instruction" for  Engineering students.

# Storing a Word in Memory & Execution of a Complete Instruction

## Introduction

In previous modules, we learned about the fundamental components of a computer: the processor (CPU), memory, and the datapath. This module connects these components to show how they work in concert to execute a single machine instruction. Understanding this process is crucial for grasping computer organization, as it forms the basis for all software execution. We will focus on the `store word` instruction (`sw` in MIPS-like architectures), which moves data from a CPU register to the main memory.

## Core Concepts

### 1. The Memory Subsystem
Modern computers use a **byte-addressable memory**. This means each unique memory address points to a single byte (8 bits) of data. However, processors typically operate on larger units of data called **words**. A word is the natural unit of data used by a particular processor architecture. For a 32-bit machine (like our example), a word is 32 bits, or 4 bytes.

When storing a 32-bit word, we must therefore write to four consecutive memory addresses. The address we specify in the instruction is the base address, typically the address of the **least significant byte** of the word.

### 2. The `store word` Instruction
The generic format for a store instruction is:
`sw Rs, offset(Rt)`

*   `sw`: The operation code (opcode) for "store word".
*   `Rs`: The source register whose 32-bit contents we want to store in memory.
*   `offset`: A constant value (displacement).
*   `Rt`: The base register that holds a memory address.

The **effective memory address** is calculated as: `Effective Address = Contents_of_Rt + offset`

This effective address must be **word-aligned**. This means the address must be a multiple of 4 (its last two bits must be `00`). This alignment simplifies the hardware design for memory access.

### 3. The Execution Process: A Step-by-Step Walkthrough

Let's execute the instruction: `sw $t0, 12($s1)`
This means: *Store the 32-bit word from register `$t0` into the memory location calculated by adding 12 to the contents of register `$s1`.*

**Assumptions:**
*   `$s1` contains the value `1000`.
*   `$t0` contains the value `0xABCD1234`.

The execution follows a standard cycle, often orchestrated by a finite state machine (FSM) in the control unit.

**Step 1: Instruction Fetch (IF)**
The Program Counter (PC) holds the address of the current `sw` instruction. This address is sent to the instruction memory (IMEM), which returns the instruction (`sw $t0, 12($s1)`) to the CPU.

**Step 2: Instruction Decode (ID)**
The control unit decodes the opcode (`sw`) and recognizes it as a store operation. It reads the values from the specified registers:
*   It reads the base address from `Rt` (`$s1`), which is `1000`.
*   It reads the data to be stored from `Rs` (`$t0`), which is `0xABCD1234`.
The sign-extend unit extends the 16-bit `offset` (`12`) to a 32-bit value (`...000C` hex).

**Step 3: Execute / Address Calculation (EX)**
The Arithmetic Logic Unit (ALU) performs the addition to compute the effective address:
`Effective Address = $s1 + offset = 1000 + 12 = 1012`

**Step 4: Memory Access (MEM)**
This is the crucial step for a store operation. The CPU prepares the data and the address for memory:
*   The calculated effective address (`1012`) is sent to the data memory (DMEM).
*   The data from `$t0` (`0xABCD1234`) is sent to the DMEM's write data (WD) port.
*   The control unit sets the memory write signal (`MemWrite`) to `1`, enabling the write operation.

The memory subsystem now writes the 32-bit word into the four bytes starting at address `1012`. The byte ordering (**endianness**) determines how the bytes are stored. Assuming a **little-endian** system (common in x86 and many modern systems):
*   Address `1012`: `0x34` (Least Significant Byte)
*   Address `1013`: `0x12`
*   Address `1014`: `0xCD`
*   Address `1015`: `0xAB` (Most Significant Byte)

**Step 5: Writeback (WB)**
For a `store` instruction, **there is no Writeback stage**. The result has been written to memory, not to a register. The CPU simply updates the Program Counter (PC) to point to the next instruction (`PC = PC + 4`), and the cycle begins again.

---

## Example Scenario

**Instruction:** `sw $t0, 12($s1)`
**Register Values:**
*   `$s1 = 0x000003E8` (which is 1000 in decimal)
*   `$t0 = 0xABCD1234`

**Execution:**
1.  **Effective Address Calculation:**
    `$s1 (1000) + offset (12) = 1012 (decimal)`
    `1012 decimal = 0x000003F4` in hex.
2.  **Memory Write:**
    The word `0xABCD1234` is stored starting at address `0x3F4`.
3.  **Memory Contents (Little-Endian):**
    *   `Mem[0x3F4] = 0x34`
    *   `Mem[0x3F5] = 0x12`
    *   `Mem[0x3F6] = 0xCD`
    *   `Mem[0x3F7] = 0xAB`

## Key Points / Summary

*   **Purpose:** The `store word` (`sw`) instruction transfers data from a CPU register to the main memory (RAM).
*   **Address Calculation:** The effective memory address is computed as `Contents_of(Base_Register) + offset`.
*   **Alignment:** The effective address for a word operation must be word-aligned (divisible by 4).
*   **Execution Stages:** The instruction is executed through a multi-stage process: **Fetch -> Decode -> Execute (Address Calc) -> Memory Access -> (No Writeback)**.
*   **Memory Access (MEM Stage):** This is the active stage for a store. The control unit activates the `MemWrite` signal, and the 32-bit data is written to the four consecutive bytes starting at the calculated address.
*   **Endianness Matters:** The byte order (big or little-endian) defines how the word is broken down and stored in the byte-addressable memory.
*   **Contrast with `lw`:** The `store word` instruction is fundamentally the reverse of the `load word` (`lw`) instruction, which moves data from memory to a register. `sw` has no Writeback stage, while `lw` does.