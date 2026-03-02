## Summary: The Target Language

### Introduction

The target language is the output representation of a compiler, translating source programs into a form executable by the target machine. It typically manifests as assembly language or machine code, serving as the final stage before hardware execution.

### Theoretical Foundations

- **Target Language Definition**: A mapping $C: L_S \rightarrow L_T$ where the compiler transforms source language $L_S$ into target language $L_T$
- **Instruction Set Architecture (ISA)**: The complete specification of supported operations, register sets, and data representations
- **Target Machine Model**: Abstract representation including registers, memory hierarchy, and instruction formats

### Addressing Modes

| Mode | Syntax | Memory Accesses |
|------|--------|-----------------|
| Immediate | `MOV R, #n` | 0 |
| Direct | `MOV R, [addr]` | 1 |
| Indirect | `MOV R, [Rn]` | 2 |
| Indexed | `MOV R, [Rn+Rm]` | 2 |
| Relative | `JMP +offset` | 0-1 |

### RISC vs CISC Comparison

- **RISC**: Fixed-length instructions, load-store architecture, single-cycle execution, pipeline-efficient
- **CISC**: Variable-length, memory-to-memory operations, variable cycle count, microcode implementation

### Key Theorems

- **Theorem 6.1**: RISC code requires more instructions than equivalent CISC code, but typically achieves better performance per instruction due to pipelining

### Code Generation Process

1. **Instruction Selection**: Map intermediate code to machine instructions
2. **Register Allocation**: Assign variables to有限 registers using graph coloring
3. **Instruction Scheduling**: Order instructions to maximize pipeline utilization
4. **Peephole Optimization**: Apply local transformations to improve code sequences

### Important Terminology

- **Target Language**: Output language of compilation
- **Addressing Mode**: Method of specifying operand locations
- **Register Allocation**: Process of assigning variables to processor registers
- **Peephole Optimization**: Local instruction sequence improvement technique
- **Three-Address Code**: Intermediate representation with operations on at most three operands