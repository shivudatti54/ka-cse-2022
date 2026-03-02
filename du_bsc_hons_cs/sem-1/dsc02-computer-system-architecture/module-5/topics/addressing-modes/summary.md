# Addressing Modes - Summary

## Key Definitions and Concepts

- **Addressing Mode**: A technique that specifies how to locate or compute the operand address within a machine instruction
- **Effective Address (EA)**: The actual memory location or register from which an operand is fetched or where a result is stored
- **Operand**: The data value or its location on which an operation is performed

## Important Addressing Modes

| Mode | Description | Example (x86/ARM) |
|------|-------------|-------------------|
| Immediate | Operand value in instruction | `MOV R0, #100` |
| Register | Operand in specified register | `MOV AX, BX` |
| Direct | Address in instruction | `MOV AX, [1000h]` |
| Indirect | Address points to another address | `MOV AX, [BX]` |
| Register Indirect | Register holds address | `MOV AX, [SI]` |
| Indexed | Base + Index register | `MOV AX, [SI+1000h]` |
| Based | Base register + displacement | `MOV AX, [BP+8]` |
| Relative | PC + displacement | `JMP label` |
| Stack | Implicit top of stack | `PUSH AX` |

## Key Points

- Addressing modes determine how CPU locates operands, directly impacting execution speed and code efficiency
- Register and immediate addressing are fastest (no memory access); indirect modes are slower (multiple memory accesses)
- Indexed addressing is essential for array traversal; based addressing for structure/record access
- Relative addressing enables position-independent code crucial for operating systems
- Stack addressing is implicit and automatic, ideal for function call management
- RISC architectures typically support fewer modes; CISC architectures offer extensive addressing flexibility
- The choice of addressing modes affects instruction format design and overall system performance

## Common Mistakes to Avoid

1. Confusing direct and indirect addressing—direct uses the address in instruction; indirect uses address stored at that location
2. Forgetting that indexed addressing requires both a base and index component
3. Assuming smaller addressing modes are always better—each has specific use cases
4. Ignoring the distinction between register contents and memory addresses when calculating effective addresses

## Revision Tips

1. Create a comparison table of all addressing modes with advantages and typical use cases
2. Practice calculating effective addresses from given register/memory values
3. Write sample assembly code segments using different addressing modes
4. Understand how compilers use addressing modes for high-level language constructs like arrays and structures
5. Review previous years' DU examination questions on this topic for pattern understanding