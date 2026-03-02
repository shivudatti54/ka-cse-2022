# Instruction Codes, Format, and Cycle - Summary

## Key Definitions and Concepts

- **Instruction Code**: A binary pattern representing an operation to be performed by the CPU, consisting of an opcode and operand addresses.

- **Opcode (Operation Code)**: The portion of an instruction that specifies the operation to be performed (e.g., ADD, LOAD, STORE).

- **Instruction Format**: The structure defining how fields (opcode, addresses) are arranged in an instruction word.

- **Instruction Cycle**: The complete process of fetching, decoding, and executing an instruction, also known as the fetch-decode-execute cycle.

- **Addressing Mode**: The method used to specify the location of an operand (direct, indirect, immediate, register).

## Important Formulas and Theorems

- **Instruction Word Size**: Total bits = opcode bits + (number of address fields × address field bits)

- **Maximum Addressable Memory**: For an n-bit address field = 2^n memory locations

- **Execution Time**: Clock cycles per instruction × clock period = instruction execution time

- **Effective Address Calculation**:
  - Direct: EA = Address field contents
  - Indirect: EA = Contents of memory location pointed by address field
  - Immediate: EA = Address field itself (operand is part of instruction)

## Key Points

- The instruction cycle has three main phases: Fetch, Decode, and Execute, with an optional Interrupt phase.

- CPU registers involved: Program Counter (PC), Memory Address Register (MAR), Memory Buffer Register (MBR), Instruction Register (IR), and Accumulator (AC).

- Instruction codes are classified by the number of address fields: zero-address (stack), one-address (accumulator), two-address, and three-address.

- Fixed-length instruction formats simplify decoding but may waste memory; variable-length formats are more complex but efficient.

- The Program Counter (PC) holds the address of the next instruction and is automatically incremented after each fetch.

- Modern CPUs use pipelining to overlap the instruction cycle phases, improving throughput.

- The opcode determines which control signals are generated to route data through the ALU and registers.

## Common Mistakes to Avoid

- Confusing the opcode with the operand address; the opcode specifies what to do, the operand specifies on what data.

- Forgetting that the PC must be incremented during the fetch cycle (except for jump/branch instructions).

- Mixing up direct and indirect addressing—direct addressing uses the address field as the effective address, while indirect addressing uses the address field to find a pointer.

- Not considering that memory access during the fetch and execute phases takes multiple clock cycles in simple implementations.

## Revision Tips

- Draw and label the fetch-execute cycle diagram from memory, including all registers and data paths.

- Practice converting assembly-like instructions into binary instruction codes with specific formats.

- Create a comparison table of different addressing modes with examples and trade-offs.

- Solve at least 5-10 previous year DU question papers to understand the exam pattern and frequently asked topics.