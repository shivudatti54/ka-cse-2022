# CPU Design: ALU and Control Unit - Summary

## Key Definitions and Concepts
- ALU: Performs arithmetic (+, -, ×) and logic (AND, OR) operations
- Control Unit: Generates timing signals and coordinates data movement
- Microoperation: Atomic CPU action (e.g., register transfer)
- Status Flags: Condition codes set by ALU operations
- Microinstruction: Low-level control store entry

## Important Formulas and Theorems
- Two's Complement Range: -2^(n-1) to 2^(n-1)-1
- Overflow Detection: V = Cₙ ⊕ Cₙ₋₁
- Carry Lookahead: G = G₃ + P₃G₂ + P₃P₂G₁ + P₃P₂P₁G₀
- Microcode Storage: Control Store Size = 2^m × n bits

## Key Points
- ALU design determines fundamental computational capabilities
- Hardwired control is faster but less flexible than microprogrammed
- Control signals are synchronized with clock cycles
- Status flags enable conditional branching decisions
- Modern CPUs use hybrid control unit designs
- Pipeline staging requires precise control signal coordination
- Microcode allows post-fabrication instruction set updates

## Common Mistakes to Avoid
- Confusing overflow and carry flags in signed operations
- Neglecting propagation delays in control signal timing
- Misinterpreting horizontal vs vertical microcode formats
- Forgetting to reset status flags between operations

## Revision Tips
1. Practice flag calculations with edge cases (-128 + 1 in 8-bit)
2. Draw datapath diagrams for common instructions (ADD, LOAD, JUMP)
3. Compare MIPS (hardwired) and x86 (microprogrammed) control units
4. Use simulator tools (Logisim) to visualize control signal flow
5. Memorize control signal tables for basic operations