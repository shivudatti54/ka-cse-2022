# Performing ALU Operations - Summary

## Key Definitions and Concepts

- **ALU (Arithmetic Logic Unit)**: The core processor component that performs all arithmetic, logical, and shift operations on binary data.

- **Two's Complement**: The standard representation for signed numbers in computers, where negative numbers are formed by inverting all bits and adding 1.

- **Ripple-Carry Adder**: An n-bit adder constructed from n full adders connected in series, with each adder passing its carry output to the next stage.

- **Status Flags**: Special bits in the Program Status Word that indicate conditions resulting from the most recent operation (Zero, Negative, Carry, Overflow).

- **Control Signals**: Signals from the control unit that select which ALU operation to perform by activating specific functional units.

## Important Formulas and Theorems

- **Two's Complement Negation**: -N = NOT(N) + 1
- **Overflow Detection (Signed)**: Overflow occurs when the carry into the sign bit differs from the carry out of the sign bit
- **Carry Detection (Unsigned)**: Carry flag equals the carry out of the most significant bit position
- **ALU Select Lines**: For N operations, require ceil(log₂N) select lines

## Key Points

- The ALU contains dedicated hardware for arithmetic operations (adders, multipliers), logical operations (AND/OR/XOR gates), and shift operations (shift registers)

- Arithmetic operations use binary addition as the fundamental building block, with subtraction implemented through two's complement addition

- Logical operations work on individual bits without numeric interpretation—AND masks bits, OR combines bit patterns, XOR detects differences

- Status flags enable conditional branching and error detection but are set automatically by hardware after every operation

- The multiplexer-based organization allows multiple functional units to share outputs while maintaining efficiency

- ALU operations are synchronous with the processor clock, completing within one or more clock cycles depending on complexity

## Common Mistakes to Avoid

- Confusing the carry flag with the overflow flag—carry applies to unsigned arithmetic while overflow applies to signed arithmetic

- Forgetting that subtraction uses addition of the two's complement, not direct binary subtraction

- Assuming the ALU makes decisions—only the control unit and program logic determine operation selection

- Overlooking that logical operations treat operands as pure bit patterns regardless of their numeric interpretation

## Revision Tips

- Draw the ALU block diagram from memory and label all components including inputs, select lines, and outputs

- Practice computing two's complement representations and performing subtraction step-by-step

- Memorize the conditions for setting each status flag through repeated examples

- Understand how the instruction opcode maps to ALU control signals through the control unit