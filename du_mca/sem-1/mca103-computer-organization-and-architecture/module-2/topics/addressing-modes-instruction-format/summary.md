# Addressing Modes and Instruction Formats - Summary

## Key Definitions and Concepts

- **Instruction Format**: The binary structure of a machine instruction defining how different fields (opcode, operands, addressing mode) are arranged
- **Effective Address (EA)**: The actual memory location or register containing the operand data
- **Addressing Mode**: The method by which an instruction specifies the location of its operand(s)
- **Opcode**: The field in an instruction that specifies the operation to be performed

## Important Formulas and Theorems

- **Direct Addressing**: EA = Address (from instruction)
- **Indirect Addressing**: EA = memory[Address]
- **Register Indirect**: EA = Register contents
- **Indexed Addressing**: EA = Address + Index Register
- **Based Addressing**: EA = Base Register + Offset
- **Relative Addressing**: EA = PC + Offset
- **Instruction Length Calculation**: If n bits available, can address 2ⁿ distinct values

## Key Points

1. Zero-address instructions operate on stack (implicit operands); one-address uses accumulator; two-address has source-destination; three-address has separate source and destination

2. Immediate addressing provides fastest operand access but limited range; operand value is part of instruction

3. Register addressing is fastest but limited by number of registers; no memory access required

4. Indirect addressing provides flexibility through pointer indirection but requires two memory accesses

5. Indexed addressing is essential for array access; effective address = base + index

6. Relative addressing enables position-independent code; branches use PC-relative addressing in most modern architectures

7. Instruction format design requires balancing opcode space, operand fields, and address field sizes against overall instruction length

8. Modern RISC architectures predominantly use register-register (load-store) architectures with limited addressing modes for pipelining efficiency

## Common Mistakes to Avoid

1. Confusing indirect with direct addressing—indirect requires an extra memory access to get the actual address
2. Forgetting that PC changes after instruction fetch when calculating relative addresses
3. Not accounting for word size when calculating address field requirements
4. Mixing up indexed and based addressing—both add a displacement but to different registers

## Revision Tips

1. Practice calculating effective addresses with different initial register/memory values
2. Draw timing diagrams comparing memory accesses for different addressing modes
3. Remember: More addressing modes = more complex CPU but more flexible programming
4. For exam questions, always check whether the architecture uses word-addressable or byte-addressable memory
5. Review x86 and ARM instruction set documentation to see real-world addressing mode implementations