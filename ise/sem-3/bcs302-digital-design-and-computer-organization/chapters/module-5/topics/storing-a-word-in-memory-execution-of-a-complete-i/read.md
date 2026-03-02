Of course. Here is a comprehensive educational write-up on storing a word in memory and the execution of a complete instruction, tailored for  engineering students.

---

# Storing a Word in Memory & Instruction Execution

## 1. Introduction

In the realm of digital design and computer organization, understanding how a processor interacts with memory is fundamental. This module bridges the gap between the abstract idea of an "instruction" and the concrete electrical signals that make it happen. We will break down the process of storing a data word into memory and then follow the complete execution cycle of a typical `store` instruction, highlighting the role of the control unit, ALU, and memory hierarchy.

## 2. Core Concepts

### The Memory Subsystem

Computer memory is organized as a large array of contiguous locations, each with a unique **address**. Each location typically holds a fixed-size group of bits called a **word**. The word size is a key architectural parameter; for a 32-bit system, a word is 32 bits (4 bytes). Memory operations are fundamentally simple: **read** (load) from an address or **write** (store) to an address.

### The CPU's Role: The Datapath and Control Unit

The CPU is the brain that initiates all memory operations. It consists of:

- **Datapath:** The collection of functional components like the Arithmetic Logic Unit (ALU), registers, and internal buses where data is processed.
- **Control Unit:** The finite state machine that interprets the current instruction and asserts the necessary control signals (e.g., `MemRead`, `MemWrite`, `RegWrite`) to coordinate the movement and operation of data through the datapath.

### Executing a `Store` Instruction

Let's trace the execution of a MIPS assembly instruction: `sw $t0, 4($s1)`. This instruction means: "Store the word (32 bits) from register `$t0` into the memory address calculated by adding the constant 4 to the contents of register `$s1`."

The execution follows a multi-cycle pattern, often broken down into **Instruction Fetch (IF), Instruction Decode (ID), Execute (EX), Memory (MEM), and Write-Back (WB)** stages. For a store operation, the WB stage is not used.

#### Step 1: Instruction Fetch (IF)

The CPU fetches the instruction from the address in the **Program Counter (PC)** in memory. The PC is then incremented to point to the next instruction.

#### Step 2: Instruction Decode (ID)

The fetched instruction is decoded. The control unit examines the **opcode** (`sw`) and determines:

- The required operation is a memory write (`MemWrite` signal will be asserted later).
- It needs to read two registers: `$s1` (for the base address) and `$t0` (the data to store). Their values are read from the register file.
- It needs to sign-extend the 16-bit offset (4) from the instruction to a 32-bit value.

#### Step 3: Execute (EX)

The **ALU** performs the necessary computation. In this case, it adds the content of register `$s1` (the base address) to the sign-extended offset (4) to calculate the **effective memory address**.
`Effective Address = [Content of $s1] + 4`

#### Step 4: Memory (MEM)

This is the crucial stage for a store operation. The control unit asserts the `MemWrite` signal. The CPU now performs the following:

1.  It places the computed effective memory address on the **Memory Address Bus**.
2.  It places the data from register `$t0` (which was read in the ID stage) onto the **Memory Data Bus**.
3.  The `MemWrite` signal tells the memory hardware to take the data on the data bus and store it into the location specified by the address bus.

This action writes the 32-bit word from `$t0` into the calculated memory location.

#### Step 5: Write-Back (WB)

For a `load` instruction (`lw`), this stage would write the data fetched from memory back into a destination register. However, for a `store` instruction, **no result is written back to the register file**, so this stage is idle.

## 3. Example

Let's assume:

- Register `$s1` contains the value `0x1000_1000`.
- Register `$t0` contains the value `0xAABB_CCDD`.

**Execution of `sw $t0, 4($s1)`:**

1.  **Effective Address Calculation:** `0x1000_1000 + 4 = 0x1000_1004`
2.  **Memory Operation:** The CPU sends address `0x1000_1004` to memory. It sends the data `0xAABB_CCDD` to the memory data bus. The `MemWrite` signal is activated.
3.  **Result:** The memory location at address `0x1000_1004` now holds the value `0xAABB_CCDD`.

## 4. Key Points & Summary

| Concept               | Description                                                                                                                                                          |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Memory Word**       | The fundamental unit of data transferred between CPU and main memory (e.g., 32 bits).                                                                                |
| **Effective Address** | The final address computed by the ALU for a memory access (often Base + Offset).                                                                                     |
| **Control Signals**   | Signals like `MemWrite` and `MemRead` are generated by the control unit to dictate memory operation.                                                                 |
| **Instruction Cycle** | The process is pipelined into stages: IF (fetch), ID (decode/read registers), EX (calculate address), MEM (perform access), WB (write to register - for loads only). |
| **`sw` instruction**  | Does not require a Write-Back (WB) stage, as it writes to memory, not a register.                                                                                    |

**Summary:** Storing a word in memory is a coordinated effort between the CPU's datapath and control unit. The CPU calculates an effective address, places the data from a register onto the bus, and the control unit's `MemWrite` signal commands the memory to store it. Tracing the execution of an instruction through its stages (IF, ID, EX, MEM, WB) provides a clear, hierarchical understanding of how software instructions are transformed into hardware actions.
