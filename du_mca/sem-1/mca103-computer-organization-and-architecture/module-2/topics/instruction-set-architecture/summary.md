# Instruction Set Architecture - Summary

## Key Definitions and Concepts

- **Instruction Set Architecture (ISA)**: The abstract interface between software and hardware, defining instructions, data types, registers, memory organization, and addressing modes
- **Opcode**: The field in an instruction that specifies the operation to be performed
- **Addressing Mode**: The method used to specify the location of an operand
- **CISC (Complex Instruction Set Computer)**: Architecture with large, complex instruction sets emphasizing hardware complexity
- **RISC (Reduced Instruction Set Computer)**: Architecture with simplified instruction set emphasizing compiler and pipeline efficiency
- **Microarchitecture**: The internal implementation of an ISA (e.g., Pentium vs. Core i7 both implement x86)
- **Endianness**: Byte ordering in memory - big-endian stores MSB first, little-endian stores LSB first

## Important Formulas and Theorems

- **Effective Address Calculation**:
  - Direct: EA = Address field value
  - Register Indirect: EA = Contents of specified register
  - Indexed: EA = Base address + Index register contents
  - Base-Offset: EA = Base register + Displacement value
  - Relative: EA = PC + Displacement

- **Memory Address Calculation for Arrays**:
  - Byte address = Base address + (Element index × Element size in bytes)

- **Instruction Encoding (MIPS R-type)**:
  - 32-bit format: [6-bit opcode][5-bit rs][5-bit rt][5-bit rd][5-bit shamt][6-bit funct]

## Key Points

- ISA serves as a contract between software (compilers) and hardware (processors)
- Instruction format specifies binary encoding; must balance opcode space, operand count, and address range
- CISC aims to reduce instruction count and code size; RISC aims for simplicity and pipeline efficiency
- Load-store architecture (RISC) separates memory access from arithmetic operations
- Common addressing modes: immediate, register, direct, indirect, indexed, relative
- Instruction execution cycle: Fetch → Decode → Execute → Store → Update PC
- Endianness affects multi-byte data interpretation; must be consistent for communication between systems
- x86 uses condition flags for branches; MIPS uses register-based comparison

## Common Mistakes to Avoid

1. **Confusing ISA with Microarchitecture**: Remember that x86 is an ISA; Core i7, Ryzen, and Athlon are different microarchitectures implementing x86
2. **Ignoring Endianness**: When reading memory dumps or network packets, always verify byte order
3. **Forgetting Register Size**: 32-bit ISAs (x86, ARM) operate on 32-bit registers; operations on smaller sizes require specific instructions
4. **Incorrect Addressing Mode Selection**: Using wrong addressing mode leads to incorrect address calculation, especially with array indexing

## Revision Tips

1. **Practice encoding**: Convert MIPS assembly to binary and vice versa - this reinforces format understanding
2. **Trace execution**: Manually simulate instruction execution cycle for different addressing modes
3. **Compare architectures**: Create a comparison table of x86, ARM, and MIPS addressing modes and instruction types
4. **Understand trade-offs**: For each ISA design decision, consider implications on compiler, hardware, and performance
5. **Use simulators**: Run code on MIPS simulators (MARS, SPIM) to observe instruction execution and register/memory changes