# Basic Concepts of Computer Organization and Architecture - Summary

## Key Definitions and Concepts

- **Computer Architecture**: The conceptual design of a computer, including the instruction set, word length, and addressing modes visible to programmers.
- **Computer Organization**: The actual hardware implementation, including the interconnection of functional units and control signals.
- **Von Neumann Architecture**: Computer design where instructions and data share the same memory, connected via a system bus.
- **Von Neumann Bottleneck**: Performance limitation caused by the single bus handling both instructions and data transfers.
- **Harvard Architecture**: Design with separate memory units for instructions and data, allowing simultaneous access.
- **Instruction Cycle**: The sequence of fetch and execute phases for processing a single machine instruction.
- **Bus**: A set of wires transmitting data, addresses, and control signals between components.

## Important Formulas and Theorems

- Maximum addressable memory = 2^(address bus bits) bytes
- Two's complement: For a negative number -n in k bits, representation = 2^k - n
- Number of distinct addresses = 2^n (for n-bit address bus)
- Instruction cycle time depends on clock frequency and number of cycles per instruction

## Key Points

1. The CPU consists of the control unit (directs operations), ALU (performs calculations), and registers (temporary storage).

2. The fetch cycle retrieves instructions from memory using the program counter (PC), memory address register (MAR), and instruction register (IR).

3. Three main bus types: data bus (carries data), address bus (carries memory addresses), control bus (carries control signals).

4. Word length (8, 16, 32, or 64 bits) determines the basic data unit the CPU processes.

5. Common addressing modes: immediate (value in instruction), direct (address in instruction), indirect (pointer to address), register (operand in register).

6. RISC uses simple, fixed-length instructions executing in one cycle; CISC uses complex, variable-length instructions potentially taking multiple cycles.

7. Two's complement representation simplifies arithmetic operations and is the standard for representing signed integers.

8. The program counter (PC) tracks the next instruction to execute; it increments after each fetch unless a jump occurs.

9. Register Transfer Notation (RTN) describes data movement between registers in a standardized format.

10. Understanding these basic concepts is essential before studying pipelining, cache memory, and advanced CPU optimizations.

## Common Mistakes to Avoid

1. Confusing computer architecture with computer organization—architecture is what the programmer sees, organization is the hardware implementation.

2. Forgetting that the program counter increments automatically after each instruction fetch unless a branch/jump occurs.

3. Misunderstanding that the address bus determines memory capacity, not the data bus—these are different specifications.

4. In two's complement conversion, remembering that only the most significant bit indicates the sign (not the entire number).

5. Not distinguishing between the fetch cycle and execute cycle—both are part of the complete instruction cycle.

## Revision Tips

1. Draw a labeled diagram of the CPU and memory interaction to visualize the instruction fetch cycle.

2. Practice converting decimal numbers to and from two's complement representation until it becomes automatic.

3. Memorize the formulas for calculating maximum addressable memory and practice with different bus width combinations.

4. Create a comparison table between von Neumann and Harvard architectures, and between RISC and CISC processors.

5. Review past DU examination questions on this topic to understand the exam pattern and important question types.