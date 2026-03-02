# RISC vs CISC Architectures - Summary

## Key Definitions and Concepts

- **CISC (Complex Instruction Set Computer)**: Architecture design philosophy emphasizing complex instructions that perform multiple operations, reducing instruction count at the cost of hardware complexity. Examples: Intel x86, Motorola 68000.

- **RISC (Reduced Instruction Set Computer)**: Architecture design philosophy emphasizing simple, single-cycle instructions with complexity shifted to software (compilers). Examples: ARM, MIPS, SPARC, PowerPC.

- **Load-Store Architecture**: RISC design principle where arithmetic operations work only on registers; memory access is limited to dedicated load and store instructions.

- **Micro-operations (μOps)**: Internal RISC-like operations that modern CISC processors translate complex instructions into for efficient execution.

## Important Formulas and Theorems

- **RISC Execution Time**: Total Cycles = Number of Instructions × Cycles per Instruction
- **Code Density Ratio**: CISC typically achieves 40-60% better code density than RISC
- **Register Pressure**: Additional registers in RISC (typically 32) vs CISC (typically 8-16) reduce memory spills proportionally

## Key Points

- CISC evolved to simplify assembly programming; RISC evolved to enable efficient pipelining and higher performance
- RISC uses fixed-length (typically 32-bit) instructions; CISC uses variable-length instructions (1-15 bytes)
- RISC implements load-store architecture; CISC allows memory-to-memory operations
- RISC relies on hardwired control units for speed; CISC typically uses microcoded control
- Modern x86 processors internally translate CISC instructions to RISC-like micro-ops
- ARM architecture dominates mobile devices due to power efficiency
- The debate has largely resolved with modern processors combining best of both approaches
- Large register files in RISC significantly reduce memory traffic from register spills

## Common Mistakes to Avoid

1. **Assuming pure architectures exist**: Modern processors are hybrids; don't classify x86 as purely CISC or ARM as purely RISC without nuance
2. **Confusing instruction count with performance**: RISC has more instructions but each executes faster
3. **Ignoring the compiler role**: RISC heavily depends on compiler optimization; this is part of the architecture
4. **Overlooking code density**: CISC still offers advantages in code size for memory-constrained environments

## Revision Tips

1. Create a comparison table of RISC vs CISC characteristics for quick reference
2. Understand why simple instructions pipeline better — think about the five-stage pipeline
3. Know specific examples: x86 (CISC), ARM, MIPS (RISC), and modern hybrids
4. Review how modern x86 uses micro-ops to achieve RISC-like efficiency
5. Focus on the "why" behind design choices rather than just memorizing characteristics
6. Practice explaining the tradeoffs in simple terms — this frequently appears in exams