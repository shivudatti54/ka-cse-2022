# RISC vs CISC - Summary

## Key Definitions and Concepts

- **RISC (Reduced Instruction Set Computer)**: Architectural philosophy using a small, simple instruction set with fixed-length instructions and load-store memory model
- **CISC (Complex Instruction Set Computer)**: Architectural philosophy using a large instruction set with variable-length, complex instructions that can directly manipulate memory
- **ISA (Instruction Set Architecture)**: The interface between software and hardware defining available instructions, registers, and addressing modes
- **Load-Store Architecture**: Design where only dedicated load/store instructions access memory; arithmetic operations work only on registers

## Important Formulas and Theorems

- **CPI (Cycles Per Instruction)**: RISC aims for CPI = 1; CISC has variable CPI
- **Code Density**: CISC typically achieves better code density (2-3x more code in RISC for equivalent programs)
- **Pipeline Stages**: RISC typically uses 5+ stage pipelines; simpler instruction decoding enables deeper pipelining

## Key Points

1. RISC emerged in the 1980s as a response to CISC limitations, focusing on simplicity and efficiency
2. RISC instructions are fixed-length (typically 32-bit), while CISC uses variable-length (1-15 bytes)
3. RISC places complexity in the compiler (register allocation, instruction scheduling); CISC places complexity in hardware (microcode)
4. CISC allows memory-to-memory operations; RISC strictly uses register-to-register with separate load/store
5. RISC typically has 32 registers vs CISC's traditional 8-16 registers
6. Modern x86 processors internally translate CISC to RISC-like micro-operations
7. ARM dominates mobile devices due to RISC's power efficiency advantages
8. The debate has largely converged—modern processors combine best practices from both approaches

## Common Mistakes to Avoid

- **Assuming RISC is always faster**: Performance depends on implementation, workload, and optimization
- **Confusing ISA with implementation**: x86 is CISC ISA but RISC-like internal design
- **Ignoring modern context**: Pure RISC or pure CISC no longer exists in commercial processors
- **Overlooking compiler complexity**: Many students underestimate the sophisticated optimization required for RISC code generation

## Revision Tips

1. Create a comparison table listing 8-10 characteristics side-by-side
2. Trace through an example program in both RISC and CISC assembly to understand the practical difference
3. Research how your smartphone (likely ARM) and laptop/desktop (likely x86) processors embody these principles
4. Understand why ARM's efficiency made it the choice for Apple Silicon and mobile devices
5. Remember: the debate is historical—focus on understanding the principles and their modern application