# Addressing Modes and RISC vs CISC - Summary

## Key Definitions and Concepts

- **Addressing Mode**: A method that specifies how to locate the operand of an instruction (the data to be operated on).

- **RISC (Reduced Instruction Set Computer)**: Architecture with small, simple instruction set, fixed-length instructions, load-store model, and many registers.

- **CISC (Complex Instruction Set Computer)**: Architecture with large, complex instruction set, variable-length instructions, and operations directly on memory.

## Important Addressing Modes

| Mode | Description | Example |
|------|-------------|---------|
| Immediate | Operand in instruction | `MOV AX, 5` |
| Register | Operand in register | `MOV AX, BX` |
| Direct | Address in instruction | `MOV AX, [1000H]` |
| Register Indirect | Register holds address | `MOV AX, [BX]` |
| Indexed | Index + displacement | `MOV AX, [SI+1000H]` |
| Relative | Address relative to PC | `JMP LABEL` |
| Stack | Implicit top of stack | `PUSH AX` |

## RISC vs CISC Comparison

- **Instruction Set**: CISC = 100-250 complex instructions; RISC = 32-100 simple instructions
- **Instruction Length**: CISC = variable (1-15 bytes); RISC = fixed (32 bits)
- **Addressing Modes**: CISC = 20+ modes; RISC = 3-5 modes
- **Registers**: CISC = 8-16; RISC = 32-128
- **Execution**: CISC = multiple cycles, microcode; RISC = one cycle per instruction
- **Code Density**: CISC = higher; RISC = lower
- **Memory Access**: CISC = can operate directly on memory; RISC = load-store only

## Key Points

- Immediate addressing is fastest but limited to constants
- Register addressing requires no memory access
- Indexed addressing is ideal for array processing
- RISC emphasizes simplicity; CISC emphasizes hardware complexity
- ARM (RISC) powers most mobile devices; x86 (CISC) dominates desktops
- Modern x86 processors internally use RISC-like micro-operations
- Pipelining is easier with RISC due to uniform instruction timing

## Common Mistakes to Avoid

1. Confusing register addressing with register indirect addressing
2. Thinking RISC has no addressing modes (it has 3-5, just fewer than CISC)
3. Believing RISC and CISC are mutually exclusive in modern processors
4. Forgetting that CISC can also have registers—difference is in number and usage philosophy
5. Assuming all ARM processors are pure RISC (ARMv8+ has CISC-like features)

## Revision Tips

1. Practice writing one example for each addressing mode
2. Create a comparison table for RISC vs CISC with at least 8 points
3. Memorize real-world processor examples: x86/AMD → CISC, ARM/MIPS → RISC
4. Understand that "load-store" is a defining RISC characteristic
5. Review previous year DU question papers for pattern and important questions