# Storing A Word In Memory - Summary

## Key Definitions

- **Store Word (SW)**: A memory write instruction that transfers a 32-bit word from a CPU register to main memory at a computed address
- **Effective Address**: The memory location where data will be stored, calculated by adding the sign-extended offset to the base register value
- **Displaced Addressing**: Memory addressing mode where the address is computed by adding an immediate offset to a base register value
- **MemWrite Control Signal**: Signal that enables writing data into memory when asserted (set to 1)

## Important Formulas

- **Effective Address Calculation**: Address = Base Register + SignExtended(Offset)
- **Offset Sign Extension**: 16-bit immediate → 32-bit by replicating the sign bit

## Key Points

1. Store instructions transfer data FROM registers TO memory (opposite of loads)
2. The store operation requires: base register read, offset sign-extension, ALU addition, and memory write
3. Critical control signals for store: MemWrite = 1, RegWrite = 0, ALUSrc = 1, MemRead = 0
4. No register writeback occurs during store instruction execution
5. The ALU computes effective address using addition operation (ALUOp = 00 for R-type)
6. In a five-stage pipeline, memory write occurs in the MEM (fourth) stage
7. Store instructions use the same address computation logic as load instructions
8. The data word flows through the ALU to memory without modification (ALU passes input B when performing addition)

## Common Mistakes

1. Confusing data direction: Remember stores move data TO memory, loads bring data FROM memory
2. Forgetting that RegWrite = 0 for stores since no register is being written
3. Incorrectly setting ALUSrc to 0, which would use a register instead of the immediate offset
4. Confusing MemWrite with MemRead signals (MemWrite enables writes, MemRead enables reads)
5. Assuming store instructions write to the register file during the write-back stage