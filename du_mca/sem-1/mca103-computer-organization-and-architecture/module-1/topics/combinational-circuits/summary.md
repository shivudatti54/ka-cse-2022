# Combinational Circuits - Summary

## Key Definitions and Concepts
- **Combinational Circuit**: Digital circuit where outputs depend only on current inputs
- **Propagation Delay**: Time between input change and stable output
- **Fan-out**: Maximum number of gate inputs a gate output can drive
- **Hazard**: Temporary output glitch due to unequal path delays

## Important Formulas and Theorems
- **Half-Adder**:  
  Sum = A ⊕ B  
  Carry = A·B
- **Full-Adder**:  
  Sum = A ⊕ B ⊕ Cin  
  Cout = AB + Cin(A⊕B)
- **Multiplexer Output**:  
  Y = Σ(m_i D_i) where m_i are minterms of select lines
- **De Morgan's Theorem**:  
  (A+B)' = A'·B' and (A·B)' = A'+B'

## Key Points
- No memory elements - outputs purely input-dependent
- Design process: Specifications → Truth Table → Minimization → Implementation
- K-map simplification essential for cost-effective implementations
- Multiplexers can implement any Boolean function (universal logic)
- Parallel adders use carry generate (G) and propagate (P) signals
- Magnitude comparators use cascaded 1-bit comparators
- ALUs combine adder, subtractor, and logic operations using control lines

## Common Mistakes to Avoid
- Forgetting don't-care conditions in K-map simplification
- Miscalculating fan-out requirements in multi-stage circuits
- Missing invalid cases in priority encoder designs
- Confusing decoder and demultiplexer functionalities

## Revision Tips
- Practice K-map grouping with 3/4 variable maps (DU exam favorite)
- Memorize full-adder equations and carry look-ahead logic
- Understand multiplexer truth tables for 4:1 and 8:1 configurations
- Solve previous years' questions on ALU control signal mapping

Length: 650 words