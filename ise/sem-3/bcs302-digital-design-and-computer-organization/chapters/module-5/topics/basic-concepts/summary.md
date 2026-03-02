# Basic Concepts of Computer Organization and Architecture - Summary

## Key Definitions and Concepts

- **Computer Architecture**: The attributes visible to the programmer, including instruction set, addressing modes, and data types.

- **Computer Organization**: The implementation of architectural specifications in hardware, including control signals and physical components.

- **Von Neumann Architecture**: Computer design where both instructions and data are stored in the same memory unit.

- **Instruction Cycle**: The sequence of fetch, decode, execute, and store phases for processing each machine instruction.

- **Two's Complement**: The standard method for representing signed integers, allowing addition and subtraction with the same circuitry.

## Important Formulas and Theorems

- Effective Address (Indexed Addressing) = Base Register Contents + Offset Value

- Two's Complement Conversion: To negate a number, invert all bits and add 1

- Maximum Memory Addressable = 2^(address bus width)

- Data Transfer Rate = (data bus width / 8) × clock frequency (bytes per second)

## Key Points

- The CPU consists of Control Unit, Arithmetic Logic Unit (ALU), and registers working in coordination.

- The stored program concept enables self-modifying programs but creates the von Neumann bottleneck.

- Instruction execution requires the four-phase cycle: fetch, decode, execute, and store.

- Addressing modes (immediate, direct, indirect, register, indexed) provide flexibility in operand access.

- Two's complement representation simplifies hardware design for arithmetic operations.

- The system bus comprises address, data, and control buses for inter-component communication.

- Registers within the CPU provide the fastest data access, faster than cache or main memory.

## Common Mistakes to Avoid

- Confusing computer organization with computer architecture—remember architecture is the "what" and organization is the "how."

- Forgetting that the Program Counter (PC) automatically increments after each instruction fetch.

- Making errors in two's complement conversion—ensure proper bit inversion and addition of 1.

- Assuming all addressing modes provide the same performance—register addressing is fastest.

- Overlooking the fact that both instructions and data use the same memory in von Neumann architecture.

## Revision Tips

- Draw and label the basic computer structure diagram repeatedly until you can reproduce it from memory.

- Practice converting numbers to and from two's complement representation with various bit sizes.

- Create a table comparing all addressing modes with examples and their typical use cases.

- Rehearse the instruction cycle by tracing through sample instructions step by step.